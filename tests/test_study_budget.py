"""Budget/scope and exchange-integrity regression checks; no physical rating."""
import hashlib
import json
from pathlib import Path
import unittest
import zipfile

ROOT=Path(__file__).resolve().parents[1]
STUDY=ROOT/'profile/study-v0.4'

class StudyBudgetTests(unittest.TestCase):
    def test_latest_user_budget_and_no_false_2kn_guarantee(self):
        q=json.loads((STUDY/'CURRENT_QUOTE.json').read_text(encoding='utf-8'))
        self.assertEqual(q['recommended_budget_KRW'],600000)
        self.assertEqual(q['strict_ceiling_KRW'],800000)
        self.assertTrue(q['printing_costs_excluded'])
        self.assertEqual(sum(r['amount_krw'] for r in q['public_price_lines']),240084)
        self.assertNotIn('rigid_pla_2kg',[r['id'] for r in q['base_allowances']])
        for s in q['scenarios']:
            computed=sum(r['amount_krw'] for r in q['public_price_lines']+q['base_allowances']+s['additional_allowances'])
            self.assertEqual(computed,s['total_krw'])
            self.assertLess(computed,s['budget_limit_krw'])
            self.assertFalse(s['minimum_2kN_validated'])
            self.assertFalse(s['is_purchase_ready_quote'])

    def test_actual_area_not_material_name_sets_force(self):
        # A full nominal PPA-CF coupon exceeds2kN; reducing it changes the test.
        self.assertEqual(168*40,6720)
        self.assertEqual(168*4,672)
        self.assertGreater(250*(10.2*4.2),10000)
        c=json.loads((STUDY/'DESIGN_INPUTS.json').read_text(encoding='utf-8'))
        self.assertFalse(c['ISO_conformance_established'])
        self.assertFalse(c['physical_force_test_performed'])
        self.assertFalse(c['assembly_ready'])

    def test_saved_native_and_step_exchange_pairing(self):
        r=json.loads((STUDY/'EXCHANGE_CHECK.json').read_text(encoding='utf-8'))
        self.assertEqual(len(r['models']),3)
        with zipfile.ZipFile(STUDY/'STEP_exchange.zip') as archive:
            self.assertIsNone(archive.testzip())
            for m in r['models']:
                p=STUDY/m['native_path']
                self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),m['native_sha256'])
                with zipfile.ZipFile(p) as cad:
                    self.assertIsNone(cad.testzip());self.assertIn('Document.xml',cad.namelist())
                data=archive.read(m['step_member'])
                self.assertTrue(data.startswith(b'ISO-10303-21;'))
                self.assertEqual(hashlib.sha256(data).hexdigest(),m['step_sha256'])
                self.assertTrue(m['native_reopened_from_disk'])
                self.assertTrue(m['step_shapes_valid'])
                self.assertLessEqual(m['volume_relative_tolerance'],1e-5)
                self.assertLess(m['volume_relative_difference'],m['volume_relative_tolerance'])

if __name__=='__main__':unittest.main()
