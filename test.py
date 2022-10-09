import unittest
import qc_eqmo
import numpy as np

class test_v_body_to_inertial(unittest.TestCase):
    def test_a(self):
        v_body = np.array([0.5, 0, 0])
        w_body = np.array([0, 0, 0])
        assert np.array_equal(qc_eqmo.v_body_to_inertial(v_body, w_body), v_body) , "Bad v body to inertial calc"

    def test_b(self):
        v_body = np.array([0.5, 0, 0])
        w_body = np.array([0.0, 0.1, 0])
        assert np.array_equal(qc_eqmo.v_body_to_inertial(v_body, w_body), np.array([0.5, 0, 0.05])) , "Bad v body to inertial calc"

class test_prop_thrust_to_body_force(unittest.TestCase):
    def test_a(self):
        prop_thrust = np.array([10, 10, 10, 10])
        assert np.array_equal(qc_eqmo.prop_thrust_to_body_force(prop_thrust), np.array([0,0,-40]))


unittest.main()