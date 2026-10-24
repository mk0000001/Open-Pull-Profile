"""Cost arithmetic, truthful evidence flags, and native/exchange artifact pairing."""
import hashlib
import json
from pathlib import Path
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'profile/build-v0.3'

class CostdownRelease(unittest.TestCase):
    def test_quote_has_no_hidden_sensor_or_zero_shipping(self):
        q=json.loads((OUT/'COST_SUMMARY.json').read_text(encoding='utf-8'))
        self.assertEqual(sum(r['line_total_KRW'] for r in q['rows']),q['common_machine_without_load_cell_KRW'])
        self.assertGreater(q['allowances_KRW'],0)
        self.assertFalse(q['original_BOM_total_known'])
        self.assertFalse(q['physical_rating_guaranteed'])
        alternate=q['sensor_options'][1]
        self.assertEqual(alternate['machine_planning_total_KRW'],q['common_machine_without_load_cell_KRW']+alternate['sensor_allowance_KRW'])
        self.assertGreater(alternate['gap_to_budget_KRW'],0)
        validation=json.loads((OUT/'VALIDATION.json').read_text(encoding='utf-8'))
        self.assertLess(validation['new_printed_PETG_kg_at_1_27'],4)

    def test_saved_artifacts_match_actual_FreeCAD_evidence(self):
        report=json.loads((OUT/'ROUNDTRIP.json').read_text(encoding='utf-8'))
        self.assertEqual(len(report['variants']),3)
        with zipfile.ZipFile(OUT/'cad/STEP_exchange.zip') as exchange:
            for row in report['variants']:
                name='OpenPull_v0.3.0-'+row['variant']
                native=OUT/'cad'/(name+'.FCStd')
                self.assertEqual(hashlib.sha256(native.read_bytes()).hexdigest(),row['native_sha256'])
                with zipfile.ZipFile(native) as model:
                    self.assertIsNone(model.testzip());self.assertIn('Document.xml',model.namelist())
                data=exchange.read(name+'.step')
                self.assertTrue(data.startswith(b'ISO-10303-21;'))
                self.assertEqual(hashlib.sha256(data).hexdigest(),row['STEP_sha256'])
                self.assertTrue(row['native_reopened_from_disk'])
                self.assertLess(row['STEP_volume_relative_difference'],1e-7)
                self.assertEqual(row['screened_pull_positions_mm'],list(range(0,101,10)))
                self.assertEqual(row['moving_vs_column_collar_overlap'],[])

    def test_screening_does_not_become_a_rating(self):
        r=json.loads((OUT/'SCREENING.json').read_text(encoding='utf-8'))
        self.assertFalse(r['FEA_performed']);self.assertFalse(r['rating_established'])
        cases=r['sensitivity']
        self.assertGreater(cases[0]['ideal_total_frame_opening_compliance_mm'],4)
        self.assertGreater(cases[0]['ideal_total_frame_opening_compliance_mm'],cases[-1]['ideal_total_frame_opening_compliance_mm'])
        self.assertLess(cases[0]['M8_unbraced_780_Euler_N'],cases[0]['hybrid_ideal_force_per_M8_rod_N'])

if __name__=='__main__':unittest.main()
