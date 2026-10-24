"""Independent drawing checks; run in FreeCAD Python. No structural certification."""
import json
import hashlib
from pathlib import Path
import FreeCAD as App

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'profile/domestic-v0.2'
MODEL = OUT/'cad/OpenPull_Profile_v0.2.0-interface-review.FCStd'


def run():
    assert MODEL.is_file(), 'v0.2 drawing-derived model has not been generated'
    # FreeCAD otherwise reuses an already-open older document at this path.
    for opened in list(App.listDocuments().values()):
        if opened.FileName and Path(opened.FileName)==MODEL:
            App.closeDocument(opened.Name)
    doc = App.openDocument(str(MODEL))
    parts = [o for o in doc.Objects if hasattr(o, 'PartID')]
    invalid = [o.Name for o in parts if o.Shape.isNull() or not o.Shape.isValid()]
    assert not invalid, invalid
    def close(a,b):
        a=a.Value if hasattr(a,'Value') else a
        b=b.Value if hasattr(b,'Value') else b
        assert abs(a-b)<0.002, (a,b)
    def empty(obj, point):
        assert not obj.Shape.isInside(App.Vector(*point),1e-5,False), (obj.Name,point)
    # Manufacturer 2021 57CM23-3A drawing. The 4A STEP is not substituted.
    close(doc.Motor.Shape.BoundBox.ZLength,76.5)
    close(doc.Motor.Shape.BoundBox.XLength,57.2)
    my=doc.MotorShaft.Shape.BoundBox.Center.y
    close(doc.MotorShaft.Shape.BoundBox.ZLength,21)
    close(doc.MotorShaft.Shape.BoundBox.XLength,8)
    close(doc.DesignStatus.MotorWrapDegrees,72.4985097970)
    close(doc.DesignStatus.MotorTeethInMesh,4.0276949887)
    for x in (-23.57,23.57):
        for y in (-23.57,23.57):
            empty(doc.MotorMount,(x,my+y,1008))
    close(doc.MotorMount.Shape.distToShape(doc.Motor.Shape)[0],0)
    close(doc.MotorMount.Shape.common(doc.Motor.Shape).Volume,0)
    for obj in (doc.MotorBridge50,doc.MotorBridge44):
        close(obj.Shape.common(doc.BearingRoof.Shape).Volume,0)
        close(obj.Shape.common(doc.MotorMount.Shape).Volume,0)
    for obj in (doc.CrossheadTop,doc.CrossheadBottom):
        close(obj.Shape.common(doc.CrossheadFront.Shape).Volume,0)
    for obj in doc.Drive.Group:
        if obj.Name.startswith('FFBolt'):
            for fixed in (doc.LowerBeamFront,doc.LowerBeamRear):
                close(obj.Shape.common(fixed.Shape).Volume,0)
    # Two actual stepped shafts, not an unmachined cylinder.
    for suffix,x in (('Left',-160),('Right',160)):
        screw=getattr(doc,'Screw'+suffix)
        close(screw.Shape.BoundBox.ZLength,861)
        close(screw.Shape.BoundBox.ZMin,164.5)
        assert screw.Shape.isInside(App.Vector(x+7,0,500),1e-5,False)
        empty(screw,(x+7,0,1020))  # driven tail is diameter10, not16
        empty(screw,(x+6.5,0,985)) # fixed journal is diameter12
        close(getattr(doc,'FK'+suffix).MountPlane,992)
        close(getattr(doc,'FF'+suffix).MountPlane,172)
        assert getattr(doc,'FK'+suffix).Shape.common(doc.BearingRoof.Shape).Volume<0.01
        assert getattr(doc,'FF'+suffix).Shape.common(doc.FloatingSupportPlate.Shape).Volume<0.01
        nut=getattr(doc,'Nut'+suffix)
        close(nut.Shape.BoundBox.ZLength,42)
        close(nut.Shape.optimalBoundingBox(False).YLength,48)
        close(nut.Shape.optimalBoundingBox(False).XLength,40)
        close(nut.Shape.common(doc.CrossheadTop.Shape).Volume,0)
        rail=getattr(doc,'Rail'+suffix)
        for i in range(12):
            empty(rail,(230 if x>0 else -230,-48,220+60*i))
    # H=28 is installed height from rail mounting base, not block thickness.
    close(doc.GuideBlockL1.Shape.BoundBox.YMin,-68)
    close(doc.GuideBlockL1.Shape.BoundBox.YMax,-44.3)
    close(doc.CrossheadFront.Shape.BoundBox.YMax,-68)
    for suffix,x in (('L',-230),('R',230)):
        for k,z in ((1,360),(2,440)):
            block=getattr(doc,'GuideBlock'+suffix+str(k))
            for dx in (-13,13):
                for dz in (-13,13):
                    empty(block,(x+dx,-66,z+dz))
                    empty(doc.CrossheadFront,(x+dx,-74,z+dz))
    # The imported original grip has diameter17 x22 mounting cavity.
    # No invented M8 stem is retained as a connected load path.
    assert doc.getObject('LowerStem') is None
    assert doc.getObject('UpperStem') is None
    assert doc.getObject('CellTopStem') is None
    close(doc.LoadCell.Shape.BoundBox.ZLength,76)
    close(doc.LoadCell.Shape.BoundBox.XLength,51)
    close(doc.LoadCell.Shape.BoundBox.YLength,27)
    fixed=[getattr(doc,n) for n in ('ColumnLeft','ColumnRight','LowerBeamFront',
        'LowerBeamRear','UpperBeamFront','UpperBeamRear','LowerJointPlate',
        'UpperJointPlate','BearingRoof','FloatingSupportPlate','FixedGripPlate',
        'FFLeft','FFRight','RailLeft','RailRight')]
    moving=[o for o in doc.Moving.Group if hasattr(o,'PartID')]
    collisions=[]
    # Sample the whole commanded interval, including intermediate positions.
    positions=list(range(0,-101,-10))
    for dz in positions:
        for o in moving:
            s=o.Shape.copy();s.translate(App.Vector(0,0,dz))
            for f in fixed:
                if s.BoundBox.intersect(f.Shape.BoundBox):
                    volume=s.common(f.Shape).Volume
                    if volume>.05:collisions.append([o.Name,f.Name,dz,round(volume,3)])
    assert not collisions, collisions
    result={'version':'0.2.0-interface-review','status':'DRAWING_INTERFACE_CHECKS_PASSED',
        'native_sha256':hashlib.sha256(MODEL.read_bytes()).hexdigest(),
        'parts_checked':len(parts),'invalid_shapes':invalid,'pull_positions_mm':positions,
        'moving_fixed_collisions':collisions,'assembly_ready':False,
        'motor_wrap_deg':doc.DesignStatus.MotorWrapDegrees,
        'motor_teeth_in_mesh':doc.DesignStatus.MotorTeethInMesh,
        'load_path_complete':False,'load_rating_validated':False,'physical_test_performed':False,
        'remaining_gates':['profile family and slot fastening','shaft-pulley torque transmission and low belt wrap',
            'FK axial rating and seating verification','CAS tap depth and grip adapters',
            'brake/capture, guards and electronics commissioning']}
    (OUT/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(result,indent=2))
    return result


if __name__=='__main__':run()
