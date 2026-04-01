# For coverage testing, run this file in the terminal with:
# coverage run -m unittest test_patient_registry.py
# And comment out the last two lines

import unittest
from patient_registry import PatientRegistry


# Phase 2
class TestPatientRegistryUnit(unittest.TestCase):
    def setUp(self):
        self.registry = PatientRegistry()

    # TESTS: REQ-01
    # UT-01
    def test_register_patient_normal(self):
        pid = self.registry.register_patient("Alice")
        self.assertEqual(pid, "P-101")
        self.assertIn(pid, self.registry._database)
    # UT-02
    def test_register_patient_edge_special_char(self):
        pid = self.registry.register_patient("\\")
        self.assertEqual(pid, "P-101")
    # UT-03
    def test_register_patient_boundary_empty_string(self):
        with self.assertRaises(ValueError):
            self.registry.register_patient("")
    # UT-04
    def test_register_patient_invalid_none(self):
        with self.assertRaises(ValueError):
            self.registry.register_patient(None)

    # TESTS: REQ-02
    # UT-05
    def test_get_patient_normal(self):
        pid = self.registry.register_patient("Alice")
        patient = self.registry.get_patient(pid)
        self.assertEqual(patient["name"], "Alice")
    # UT-06
    def test_get_patient_edge_existing_special(self):
        pid = self.registry.register_patient("\"")
        patient = self.registry.get_patient(pid)
        self.assertEqual(patient["name"], "\"")
    # UT-07
    def test_get_patient_boundary_nonexistent(self):
        with self.assertRaises(LookupError):
            self.registry.get_patient("P-100")
    # UT-08
    def test_get_patient_invalid_empty(self):
        with self.assertRaises(ValueError):
            self.registry.get_patient("")

    # TESTS: REQ-04
    # UT-09
    def test_update_patient_normal(self):
        pid = self.registry.register_patient("Alice")
        updated = self.registry.update_patient_name(pid, "Janet")
        self.assertEqual(updated["name"], "Janet")
    # UT-10
    def test_update_patient_edge_name_like_id(self):
        pid = self.registry.register_patient("Alice")
        updated = self.registry.update_patient_name(pid, "P-102")
        self.assertEqual(updated["name"], "P-102")
    # UT-11
    def test_update_patient_boundary_empty_name(self):
        with self.assertRaises(ValueError):
            pid = self.registry.register_patient("Alice")
            self.registry.update_patient_name(pid, "")
    # UT-12
    def test_update_patient_invalid_id(self):
        with self.assertRaises(LookupError):
            self.registry.update_patient_name("P-999", "Jon")

    # TESTS: REQ-05
    # UT-13
    def test_delete_patient_normal(self):
        pid = self.registry.register_patient("Alice")
        self.registry.register_patient("Bob")
        result = self.registry.delete_patient(pid)
        self.assertTrue(result)
    # UT-14
    def test_delete_patient_edge_only_entry(self):
        pid = self.registry.register_patient("Alice")
        result = self.registry.delete_patient(pid)
        self.assertTrue(result)
    # UT-15
    def test_delete_patient_boundary_empty_db(self):
        with self.assertRaises(LookupError):
            self.registry.delete_patient("P-101")
    # UT-16
    def test_delete_patient_invalid_empty_id(self):
        with self.assertRaises(ValueError):
            self.registry.delete_patient("")


# Phase 3
class TestPatientRegistryComponent(unittest.TestCase):
    def setUp(self):
        self.registry = PatientRegistry()

    # CT-01
    # TESTS: REQ-01, REQ-03, REQ-04
    def test_register_update_retrieve_normal(self):
        pid = self.registry.register_patient("Alice")
        self.registry.update_patient_name(pid, "Bob")
        patient = self.registry.get_patient(pid)

        self.assertEqual(patient["patient_id"], pid)
        self.assertEqual(patient["name"], "Bob")

    # CT-02
    # TESTS: REQ-01, REQ-03, REQ-04
    def test_update_name_like_id(self):
        pid = self.registry.register_patient("Alice")
        self.registry.update_patient_name(pid, "P-102")
        patient = self.registry.get_patient(pid)

        self.assertEqual(patient["patient_id"], pid)
        self.assertEqual(patient["name"], "P-102")

    # CT-03
    # TESTS: REQ-01, REQ-03, REQ-04
    def test_update_nonexistent_patient(self):
        pid = self.registry.register_patient("Alice")

        with self.assertRaises(LookupError):
            self.registry.update_patient_name("P-999", "Clyde")

        patient = self.registry.get_patient(pid)
        self.assertEqual(patient["name"], "Alice")
        self.assertEqual(patient["patient_id"], pid)
    
    # CT-04
    # TESTS: REQ-01, REQ-05
    def test_CT12_delete_invalid_id(self):
        pid = self.registry.register_patient("Alice")

        with self.assertRaises(LookupError):
            self.registry.delete_patient("P-")

        patient = self.registry.get_patient(pid)
        self.assertEqual(patient["patient_id"], pid)
        self.assertEqual(patient["name"], "Alice")


# Phase 4
class TestCoverageExecution(unittest.TestCase):
    def test_dummy(self):
        # This ensures unittest runs even if isolated
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()