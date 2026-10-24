"""Check release pairing, artifact hashes and preservation of upstream files.

Usage: python profile/check_release.py [--write-manifest]
No FreeCAD or third-party Python packages required.
"""
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BASELINE = '55017419fae89409b1098540212e1620b1e46d0b'


def files_to_hash():
    selected = [ROOT/name for name in ('VERSION','UPSTREAM.md','CHANGELOG.md','README.md','LICENSE','.gitattributes','.gitignore')]
    selected += list((ROOT/'docs/superpowers').rglob('*.md'))
    selected += [p for p in (ROOT/'profile').rglob('*') if p.is_file()
                 and p.suffix in {'.json','.csv','.md','.py','.FCMacro','.FCStd','.step','.png'}]
    selected += list((ROOT/'tests').glob('test_profile*.py'))
    selected += list((ROOT/'.github/workflows').glob('profile*.yml'))
    return sorted(set(selected))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check():
    version = (ROOT/'VERSION').read_text().strip()
    cfg = json.loads((ROOT/'profile/config.json').read_text(encoding='utf-8'))
    validation = json.loads((ROOT/'profile/VALIDATION.json').read_text(encoding='utf-8'))
    assert cfg['version'] == validation['version'] == version, 'Version mismatch'
    assert validation['status'] == 'GEOMETRY_CHECKS_PASSED', 'No successful geometry evidence'
    assert validation['load_rating_validated'] is False, 'Unproven load rating claimed'
    assert validation['physical_test_performed'] is False, 'Physical test status incorrect'
    assert validation['assembly_ready'] is cfg['assembly_ready'] is False, 'Unproven assembly-ready claim'
    assert validation['checked_pull_positions_mm'] == [0,-cfg['pull_travel_mm']], 'Travel evidence mismatch'
    native = ROOT/('profile/cad/OpenPull_Profile_v'+version+'.FCStd')
    step = native.with_suffix('.step')
    assert native.is_file() and step.is_file(), 'Missing CAD deliverable'
    with zipfile.ZipFile(native) as archive:
        assert archive.testzip() is None, 'Corrupt native CAD archive'
        assert 'Document.xml' in archive.namelist(), 'Not a FreeCAD document'
    assert step.read_bytes().startswith(b'ISO-10303-21;'), 'Not a STEP exchange file'
    with (ROOT/'profile/CUT_LIST.csv').open(encoding='utf-8-sig',newline='') as f:
        cuts = {r['part_id']:r for r in csv.DictReader(f)}
    assert int(cuts['EX-COL']['cut_length_mm']) == cfg['column_length_mm']
    assert int(cuts['EX-BEAM']['cut_length_mm']) == cfg['crossmember_length_mm']
    assert int(cuts['EX-BASE']['cut_length_mm']) == cfg['base_length_mm']
    assert [int(cuts[k]['quantity']) for k in ('EX-COL','EX-BEAM','EX-BASE')] == [2,4,2]
    with (ROOT/'profile/BOM.csv').open(encoding='utf-8-sig',newline='') as f:
        bom = list(csv.DictReader(f))
    assert len({r['id'] for r in bom}) == len(bom), 'Duplicate BOM id'
    assert all(r['selection_status'] for r in bom), 'Missing sourcing status'
    assert any(r['id']=='FB' and r['selection_status']=='UNRESOLVED_DO_NOT_POWER' for r in bom)
    if (ROOT/'.git').exists():
        subprocess.run(['git','diff','--exit-code',BASELINE,'--','CAD','Arduino','Electronics','Documents','LICENSE'],cwd=ROOT,check=True)
    manifest = ROOT/'profile/MANIFEST.sha256'
    if '--write-manifest' in sys.argv:
        manifest.write_text(''.join(digest(p)+'  '+p.relative_to(ROOT).as_posix()+'\n' for p in files_to_hash()),encoding='utf-8',newline='\n')
    entries = [line.split('  ',1) for line in manifest.read_text(encoding='utf-8').splitlines()]
    expected = {p.relative_to(ROOT).as_posix() for p in files_to_hash()}
    assert {name for _,name in entries} == expected, 'Manifest file set out of date'
    for sha,name in entries:
        assert digest(ROOT/name) == sha, 'Artifact hash mismatch: '+name
    print(json.dumps({'status':'PASS','version':version,'hashes_checked':len(entries),
                      'upstream_preserved':True if (ROOT/'.git').exists() else 'not checked: clone required',
                      'geometry_evidence_parts':validation['checked_parts'],
                      'physical_load_rating':False},indent=2))


if __name__ == '__main__':
    check()
