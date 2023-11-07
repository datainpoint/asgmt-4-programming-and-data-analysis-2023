# asgmt-4-programming-and-data-analysis-2023

> Assignment 4: Programming and Data Analysis 2023.

Define functions or classes in `asgmt-four.py` with given names and templates then run `test-runner.py`.

## 01. Define a class `Pet` which instantiates objects with 1 attribute `species` and 1 method `make_sound()`.

```python
class Pet:
    """
    >>> dog = Pet('Dog', 'Bark')
    >>> type(dog)
    '__main__.Pet'
    >>> dog.species
    'Dog'
    >>> dog.make_sound()
    'Bark'
    >>> kitty = Pet('Cat', 'Meow')
    >>> type(kitty)
    '__main__.Pet'
    >>> kitty.species
    'Cat'
    >>> kitty.make_sound()
    'Meow'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a class `Hogwarts` which instantiates objects with 3 attributes `location`, `founders`, and `houses`.

```python
class Hogwarts:
    """
    >>> hogwarts = Hogwarts()
    >>> type(hogwarts)
    '__main__.Hogwarts'
    >>> hogwarts.location
    'Scotland'
    >>> hogwarts.founders
    ['Godric Gryffindor', 'Salazar Slytherin', 'Rowena Ravenclaw', 'Helga Hufflepuff']
    >>> hogwarts.houses
    ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a class named `Gryffindor` which instantiates objects with 2 attributes `traits` and `colors`, 1 method `cast_a_spell()`.

```python
class Gryffindor:
    """
    >>> harry_potter = Gryffindor("Harry Potter")
    >>> type(harry_potter)
    '__main__.Gryffindor'
    >>> harry_potter.name
    'Harry Potter'
    >>> harry_potter.traits
    ['courage', 'bravery', 'nerve', 'chivalry']
    >>> harry_potter.colors
    ['scarlet red', 'gold']
    >>> harry_potter.cast_a_spell()
    'Expelliarmus!'
    >>> hermione_granger = Gryffindor("Hermione Granger")
    >>> type(hermione_granger)
    '__main__.Gryffindor'
    >>> hermione_granger.name
    'Hermione Granger'
    >>> hermione_granger.traits
    ['courage', 'bravery', 'nerve', 'chivalry']
    >>> hermione_granger.colors
    ['scarlet red', 'gold']
    >>> hermione_granger.cast_a_spell()
    'Expelliarmus!'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a class `StrCase` which instantiates objects with 3 methods `upper_case()`, `lower_case()`, and `swap_case()`.

```python
class StrCase:
    """
    >>> luke = StrCase('Luke Skywalker')
    >>> type(luke)
    '__main__.StrCase'
    >>> luke.upper_case()
    'LUKE SKYWALKER'
    >>> luke.lower_case()
    'luke skywalker'
    >>> luke.swap_case()
    'lUKE sKYWALKER'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a class `MethodCalculator` which instantiates objects with 5 methods `add()`, `substract()`, `multiply()`, `divide()`, and `power()`.

```python
class MethodCalculator:
    """
    >>> method_calculator = MethodCalculator(10, 2)
    >>> type(method_calculator)
    '__main__.MethodCalculator'
    >>> method_calculator.add()
    12
    >>> method_calculator.subtract()
    8
    >>> method_calculator.multiply()
    20
    >>> method_calculator.divide()
    5.0
    >>> method_calculator.power()
    100
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a class `SymbolicCalculator` which instantiates objects with 1 method `calculate()`.

```python
class SymbolicCalculator:
    """
    >>> symbolic_calculator = SymbolicCalculator(10, 2)
    >>> type(symbolic_calculator)
    '__main__.SymbolicCalculator'
    >>> symbolic_calculator.calculate('+')
    12
    >>> symbolic_calculator.calculate('-')
    8
    >>> symbolic_calculator.calculate('*')
    20
    >>> symbolic_calculator.calculate('/')
    5.0
    >>> symbolic_calculator.calculate('**')
    100
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a class named `ArrayGetAttrs` which instantiates objects with 4 methods `get_ndim()`, `get_shape()`, `get_size()`, and `get_dtype()`.

```python
class ArrayGetAttrs:
    """
    >>> arr = np.array([5, 5, 6, 6])
    >>> aga = ArrayGetAttrs(arr)
    >>> aga.get_ndim()
    1
    >>> aga.get_shape()
    (4,)
    >>> aga.get_size()
    4
    >>> aga.get_dtype()
    dtype('int64')
    >>> arr = np.array([[5, 5],
                        [6, 6]])
    >>> aga = ArrayGetAttrs(arr)
    >>> aga.get_ndim()
    2
    >>> aga.get_shape()
    (2, 2)
    >>> aga.get_size()
    4
    >>> aga.get_dtype()
    dtype('int64')
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `add_intercepts()` which horizontally combines a `(m, 1)` array of ones to a given array.

```python
def add_intercepts(arr: np.ndarray) -> np.ndarray:
    """
    >>> A = np.array([5, 5, 6, 6]).reshape(-1, 1)
    >>> add_intercepts(A)
    array([[1, 5],
           [1, 5],
           [1, 6],
           [1, 6]])
    >>> B = np.arange(10, dtype=int).reshape(5, 2)
    >>> add_intercepts(B)
    array([[1, 0, 1],
           [1, 2, 3],
           [1, 4, 5],
           [1, 6, 7],
           [1, 8, 9]])
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `create_square_matrix()` which generates a square matrix with elements equal to the multiplication of row number and column number.

```python
def create_square_matrix(n: int) -> np.ndarray:
    """
    >>> create_square_matrix(3)
    array([[1, 2, 3],
           [2, 4, 6],
           [3, 6, 9]])
    >>> create_square_matrix(4)
    array([[ 1,  2,  3,  4],
           [ 2,  4,  6,  8],
           [ 3,  6,  9, 12],
           [ 4,  8, 12, 16]])
    >>> create_square_matrix(5)
    array([[ 1,  2,  3,  4,  5],
           [ 2,  4,  6,  8, 10],
           [ 3,  6,  9, 12, 15],
           [ 4,  8, 12, 16, 20],
           [ 5, 10, 15, 20, 25]])
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `create_diagonal_split_matrix()` which generates a diagonal matrix given `n` as the order, `fill_int` as the elements outside the main diagonal and zeros as the main diagonal.

```python
def create_diagonal_split_matrix(n: int, fill_int: int) -> np.ndarray:
    """
    >>> create_diagonal_split_matrix(2, 5566)
    array([[   0, 5566],
           [5566,    0]])
    >>> create_diagonal_split_matrix(3, 55)
    array([[ 0, 55, 55],
           [55,  0, 55],
           [55, 55,  0]])
    >>> create_diagonal_split_matrix(4, 66)
    array([[ 0, 66, 66, 66],
           [66,  0, 66, 66],
           [66, 66,  0, 66],
           [66, 66, 66,  0]])
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```