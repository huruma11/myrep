Calculator
A simple Python calculator library with four basic arithmetic operations.
Functions
Function	Description
`add(a, b)`	Returns the sum of `a` and `b`
`subtract(a, b)`	Returns `a` minus `b`
`multiply(a, b)`	Returns the product of `a` and `b`
`divide(a, b)`	Returns `a` divided by `b`
Usage
```python
from calculator import add, subtract, multiply, divide

add(10, 5)       # 15
subtract(10, 5)  # 5
multiply(10, 5)  # 50
divide(10, 5)    # 2.0
```
Error handling
`divide` raises a `ValueError` if the divisor is zero:
```python
divide(10, 0)  # raises ValueError: Cannot divide by zero
```
Running the tests
Install pytest if you haven't already:
```bash
pip install pytest
```
Then run:
```bash
pytest test_calculator.py -v
```
All 23 tests should pass.
Project structure
```
.
├── calculator.py        # Core arithmetic functions
├── test_calculator.py   # Unit tests
└── README.md
```
