import unittest
import importlib
import numpy as np

class TestAssignmentFour(unittest.TestCase):
    def test_01_Pet(self):
        dog = asgmt.Pet('Dog', 'Bark')
        self.assertEqual(dog.species, 'Dog')
        self.assertEqual(dog.make_sound(), 'Bark')
        kitty = asgmt.Pet('Cat', 'Meow')
        self.assertEqual(kitty.species, 'Cat')
        self.assertEqual(kitty.make_sound(), 'Meow')
    def test_02_Hogwarts(self):
        hogwarts = asgmt.Hogwarts()
        self.assertEqual(hogwarts.location, 'Scotland')
        self.assertEqual(hogwarts.founders, ['Godric Gryffindor', 'Salazar Slytherin', 'Rowena Ravenclaw', 'Helga Hufflepuff'])
        self.assertEqual(hogwarts.houses, ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff'])
    def test_03_Gryffindor(self):
        harry_potter = asgmt.Gryffindor("Harry Potter")
        self.assertIsInstance(harry_potter.name, str)
        self.assertIsInstance(harry_potter.traits, list)
        self.assertIsInstance(harry_potter.colors, list)
        self.assertEqual(harry_potter.cast_a_spell(), 'Expelliarmus!')
        hermione_granger = asgmt.Gryffindor("Hermione Granger")
        self.assertIsInstance(hermione_granger.name, str)
        self.assertIsInstance(hermione_granger.traits, list)
        self.assertIsInstance(hermione_granger.colors, list)
        self.assertEqual(hermione_granger.cast_a_spell(), 'Expelliarmus!')
    def test_04_StrCase(self):
        luke = asgmt.StrCase('Luke Skywalker')
        self.assertEqual(luke.upper_case(), 'LUKE SKYWALKER')
        self.assertEqual(luke.lower_case(), 'luke skywalker')
        self.assertEqual(luke.swap_case(), 'lUKE sKYWALKER')
        anakin = asgmt.StrCase('Anakin Skywalker')
        self.assertEqual(anakin.upper_case(), 'ANAKIN SKYWALKER')
        self.assertEqual(anakin.lower_case(), 'anakin skywalker')
        self.assertEqual(anakin.swap_case(), 'aNAKIN sKYWALKER')
    def test_05_MethodCalculator(self):
        method_calculator = asgmt.MethodCalculator(5, 6)
        self.assertEqual(method_calculator.add(), 11)
        self.assertEqual(method_calculator.subtract(), -1)
        self.assertEqual(method_calculator.multiply(), 30)
        self.assertGreaterEqual(method_calculator.divide(), 0.8)
        method_calculator = asgmt.MethodCalculator(10, 10)
        self.assertEqual(method_calculator.add(), 20)
        self.assertEqual(method_calculator.subtract(), 0)
        self.assertEqual(method_calculator.multiply(), 100)
        self.assertGreaterEqual(method_calculator.divide(), 1)
    def test_06_SymbolicCalculator(self):
        symbolic_calculator = asgmt.SymbolicCalculator(10, 2)
        self.assertGreaterEqual(symbolic_calculator.calculate('+'), 12)
        self.assertGreaterEqual(symbolic_calculator.calculate('-'), 8)
        self.assertGreaterEqual(symbolic_calculator.calculate('*'), 20)
        self.assertGreaterEqual(symbolic_calculator.calculate('/'), 5.0)
        self.assertGreaterEqual(symbolic_calculator.calculate('**'), 100)
        symbolic_calculator = asgmt.SymbolicCalculator(10, 5)
        self.assertGreaterEqual(symbolic_calculator.calculate('+'), 15)
        self.assertGreaterEqual(symbolic_calculator.calculate('-'), 5)
        self.assertGreaterEqual(symbolic_calculator.calculate('*'), 50)
        self.assertGreaterEqual(symbolic_calculator.calculate('/'), 2.0)
        self.assertGreaterEqual(symbolic_calculator.calculate('**'), 100000)
    def test_07_ArrayGetAttrs(self):
        arr = np.array([5, 5, 6, 6])
        aga = asgmt.ArrayGetAttrs(arr)
        self.assertEqual(aga.get_ndim(), 1)
        self.assertEqual(aga.get_shape(), (4,))
        self.assertEqual(aga.get_size(), 4)
        arr = np.array([[5, 5],
                        [6, 6]])
        aga = asgmt.ArrayGetAttrs(arr)
        self.assertEqual(aga.get_ndim(), 2)
        self.assertEqual(aga.get_shape(), (2, 2))
        self.assertEqual(aga.get_size(), 4)
    def test_08_add_intercepts(self):
        A = np.array([5, 5, 6, 6]).reshape(-1, 1)
        np.testing.assert_array_equal(asgmt.add_intercepts(A),
        np.array([[1, 5],
                  [1, 5],
                  [1, 6],
                  [1, 6]]))
        B = np.arange(10).reshape(5, 2)
        np.testing.assert_array_equal(asgmt.add_intercepts(B),
        np.array([[1, 0, 1],
                  [1, 2, 3],
                  [1, 4, 5],
                  [1, 6, 7],
                  [1, 8, 9]]))
        C = np.array([5, 6, 7, 8]).reshape(-1, 1)
        np.testing.assert_array_equal(asgmt.add_intercepts(C),
        np.array([[1, 5],
                  [1, 6],
                  [1, 7],
                  [1, 8]]))
    def test_09_create_diagonal_split_matrix(self):
        np.testing.assert_array_equal(asgmt.create_diagonal_split_matrix(2, 5566),
        np.array([[   0, 5566],
                  [5566,    0]]))
        np.testing.assert_array_equal(asgmt.create_diagonal_split_matrix(3, 55),
        np.array([[ 0, 55, 55],
                  [55,  0, 55],
                  [55, 55,  0]]))
        np.testing.assert_array_equal(asgmt.create_diagonal_split_matrix(4, 66),
        np.array([[ 0, 66, 66, 66],
                  [66,  0, 66, 66],
                  [66, 66,  0, 66],
                  [66, 66, 66,  0]]))
    def test_10_create_square_matrix(self):
        np.testing.assert_array_equal(asgmt.create_square_matrix(3),
        np.array([[1, 2, 3],
                  [2, 4, 6],
                  [3, 6, 9]]))
        np.testing.assert_array_equal(asgmt.create_square_matrix(4),
        np.array([[ 1,  2,  3,  4],
                  [ 2,  4,  6,  8],
                  [ 3,  6,  9, 12],
                  [ 4,  8, 12, 16]]))
        np.testing.assert_array_equal(asgmt.create_square_matrix(5),
        np.array([[ 1,  2,  3,  4,  5],
                  [ 2,  4,  6,  8, 10],
                  [ 3,  6,  9, 12, 15],
                  [ 4,  8, 12, 16, 20],
                  [ 5, 10, 15, 20, 25]]))

asgmt = importlib.import_module("asgmt-four")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFour)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))