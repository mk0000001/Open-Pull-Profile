"""FreeCAD integration checks. Run with FreeCAD Python, not system Python.

Detects missing deliverables, invalid solids, reversed specimen placement,
frame collisions and a claimed travel that crashes into the support bearings.
These tests do not establish a structural load rating.
"""
import json
from pathlib import Path
import FreeCAD as App

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / 'profile/cad/OpenPull_Profile_v0.1.0-design.FCStd'

def run():
    assert MODEL.is_file(), 'Native FCStd has not been generated'
    doc = App.openDocument(str(MODEL))
    visible = [o for o in doc.Objects if hasattr(o, 'Shape') and hasattr(o, 'PartID')]
    assert len(visible) > 35, 'Assembly is missing major components'
    invalid = [o.Name for o in visible if o.Shape.isNull() or not o.Shape.isValid()]
    assert not invalid, 'Invalid shapes: ' + str(invalid)
    assert abs(doc.ColumnLeft.Shape.BoundBox.ZLength - 900) < 0.01
    assert abs(doc.ColumnRight.Shape.BoundBox.XMin - 210) < 0.01
    assert abs(doc.ScrewLeft.Shape.BoundBox.XMin + 168) < 0.01
    assert abs(doc.ScrewRight.Shape.BoundBox.XMax - 168) < 0.01
    assert abs(doc.LowerGrip.Shape.BoundBox.ZMin - 500) < 0.1
    assert abs(doc.UpperGrip.Shape.BoundBox.ZMin - 681) < 0.1
    assert doc.Specimen.Shape.BoundBox.ZMin < doc.LowerGrip.Shape.BoundBox.ZMax
    assert doc.Specimen.Shape.BoundBox.ZMax > doc.UpperGrip.Shape.BoundBox.ZMin
    # Test load and screw axes share the same depth; the original gripper body
    # envelope is asymmetric, so use the explicit reference axis on the stems.
    assert abs(doc.LowerStem.Shape.BoundBox.Center.y) < 0.01
    assert abs(doc.UpperStem.Shape.BoundBox.Center.y) < 0.01
    frame = [doc.ColumnLeft, doc.ColumnRight, doc.LowerBeamFront,
             doc.LowerBeamRear, doc.UpperBeamFront, doc.UpperBeamRear]
    moving = [doc.CrossheadFront, doc.CrossheadTop, doc.CrossheadBottom,
              doc.CrossheadRear, doc.LowerGrip, doc.LowerStem,
              doc.NutLeft, doc.NutRight]
    collisions = []
    for dz in (0, -100):
        for obj in moving:
            shape = obj.Shape.copy()
            shape.translate(App.Vector(0, 0, dz))
            for fixed in frame + [doc.BFLeft, doc.BFRight]:
                if shape.BoundBox.intersect(fixed.Shape.BoundBox):
                    v = shape.common(fixed.Shape).Volume
                    if v > 0.05:
                        collisions.append([obj.Name, fixed.Name, dz, round(v, 3)])
    assert not collisions, 'Travel/frame collisions: ' + str(collisions)
    assert doc.NutLeft.Shape.BoundBox.ZMin - 100 > doc.BFLeft.Shape.BoundBox.ZMax
    assert doc.GuideBlockL1.Shape.BoundBox.ZMin - 100 >= doc.RailLeft.Shape.BoundBox.ZMin
    assert abs(doc.Sizing.BeltLength - 920) < 0.01
    assert abs(doc.Sizing.StepsPerMillimetre - 640) < 0.001
    result = {'version': '0.1.0-design', 'status': 'GEOMETRY_CHECKS_PASSED',
              'checked_parts': len(visible), 'invalid_shapes': invalid,
              'checked_pull_positions_mm': [0, -100], 'frame_collisions': collisions,
              'load_rating_validated': False, 'physical_test_performed': False,
              'belt_pitch_length_mm': doc.Sizing.BeltLength,
              'motor_y_mm': doc.Sizing.MotorY,
              'steps_per_mm_proposal': doc.Sizing.StepsPerMillimetre}
    out = ROOT / 'profile/VALIDATION.json'
    out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8',newline='\n')
    print(json.dumps(result, indent=2))
    return result

if __name__ == '__main__':
    run()
