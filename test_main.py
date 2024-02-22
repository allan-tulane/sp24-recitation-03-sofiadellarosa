from main import *


## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3 * 3

  # added tests
  assert quadratic_multiply(BinaryNumber(10), BinaryNumber(10)) == 10 * 10
  assert quadratic_multiply(BinaryNumber(20), BinaryNumber(20)) == 20 * 20
  assert quadratic_multiply(BinaryNumber(150), BinaryNumber(100)) == 150 * 100
  assert quadratic_multiply(BinaryNumber(999), BinaryNumber(999)) == 999 * 999
  assert quadratic_multiply(BinaryNumber(18), BinaryNumber(2)) == 2 * 18
