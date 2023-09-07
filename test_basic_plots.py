import io
import contextlib
import random
import subprocess
import unittest

import numpy as np

import basic_circuit
import basic_plots_sol
import charging_capacitor
import error_coding
import gravitational_force

class TestIntro(unittest.TestCase):

    def test_gravity(self):

        print("\ntesting gravity()")
        m1 = 100*random.random()
        m2 = 100*random.random()
        r = 1000*random.random()
        
        sol = basic_plots_sol.gravity(m1, m2, r)
        sub = gravitational_force.gravity(m1, m2, r)

        self.assertEqual(sol, sub)

        
    def test_gravitational_force(self):

        print("\ntesting gravitational_force.py")

        with open("gravitational_force.py", "r") as file:
            content = file.read()

        hard_code_check = False
        # check if string present or not
        if "1.9848" in content:
            hard_code_check = True

        self.assertFalse(hard_code_check,
                         "You are illegally hard "
                         "coding the answer")

        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            basic_plots_sol.gravity_script()
        gravity_string_sol = f.getvalue().strip()

        result = subprocess.run(["python",
                                 "gravitational_force.py"],
                                stdout=subprocess.PIPE)
        gravity_string = result.stdout.decode("UTF-8").strip()
        
        self.assertEqual(gravity_string_sol, gravity_string)


    def test_capacitor(self):

        print("\ntesting capacitor()")
        
        V = 30*random.random()
        C = 10e-6*random.random()
        R = 10e3*random.random()
        t = 20e-3*random.random()
        
        sol = basic_plots_sol.capacitor(V, t, R, C)
        sub = charging_capacitor.capacitor(V, t, R, C)

        self.assertEqual(sol, sub)

        
    def test_charging_capacitor(self):

        print("\ntesting charging_capacitor.py")

        with open("charging_capacitor.py", "r") as file:
            content = file.read()

        hard_code_check = False
        # check if string present or not
        if "0.162" in content:
            hard_code_check = True

        self.assertFalse(hard_code_check,
                         "You are illegally hard "
                         "coding the answer")

        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            basic_plots_sol.capacitor_script()
        capacitor_string_sol = f.getvalue().strip()

        result = subprocess.run(["python",
                                 "charging_capacitor.py"],
                                stdout=subprocess.PIPE)
        capacitor_string = result.stdout.decode("UTF-8").strip()
        
        self.assertEqual(capacitor_string_sol, capacitor_string)

        
    def test_resistor(self):

        print("\ntesting resistor()")
        
        resistance = 50e3*random.random()
        current = 100e-3*random.random()
        
        sol_v, sol_p = basic_plots_sol.resistor(current,
                                                resistance)
        sub_v, sub_p = basic_circuit.resistor(current,
                                              resistance)

        self.assertEqual(sol_v, sub_v,
                         "The voltage values don't match")

        self.assertEqual(sol_p, sub_p,
                         "The power values don't match")


    def test_basic_circuit(self):

        print("\ntesting basic_circuit.py")

        with open("basic_circuit.py", "r") as file:
            content = file.read()

        hard_code_check = False
        # check if string present or not
        if ("200.00" in content) or ("4.00" in content):
            hard_code_check = True

        self.assertFalse(hard_code_check,
                         "You are illegally hard "
                         "coding the answer")

        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            basic_plots_sol.resistor_script()
        resistor_string_sol = f.getvalue().strip()

        result = subprocess.run(["python",
                                 "basic_circuit.py"],
                                stdout=subprocess.PIPE)
        resistor_string = result.stdout.decode("UTF-8").strip()
        
        self.assertEqual(resistor_string_sol, resistor_string)


    def test_redundant_bits(self):

        print("\ntesting redundant_bits()")

        for _ in range(32):
            bit_string = "".join(random.choices(["0","1"],k=5))
            
            
            sol = basic_plots_sol.redundant_bits(bit_string)
            sub = error_coding.redundant_bits(bit_string)

            self.assertEqual(sol, sub,
                             "The output bits don't match")

            
    def test_error_coding(self):

        print("\ntesting error_coding.py")
        
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            basic_plots_sol.redundant_bits_script()
        error_string_sol = f.getvalue().strip()

        result = subprocess.run(["python",
                                 "error_coding.py"],
                                stdout=subprocess.PIPE)
        error_string = result.stdout.decode("UTF-8").strip()
        
        self.assertEqual(error_string_sol, error_string)

        
if __name__ == '__main__':
    unittest.main()




