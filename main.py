"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.


def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def quadratic_multiply(x, y):
  # this just converts the result from a BinaryNumber to a regular int
  return _quadratic_multiply(x, y).decimal_val


def _quadratic_multiply(x, y):

    # obtain the xvec and yvec, the binary values of x and y
    xvec = x.binary_vec
    yvec = y.binary_vec

    # pad the xvec and yvec with leading 0s if not even number of bits
    xvec, yvec = pad(xvec, yvec)
    print(xvec, yvec)
  
  # base case
    if x.decimal_val <= 1 and y.decimal_val <= 1:
      return BinaryNumber(x.decimal_val * y.decimal_val)

    # Otherwise, split xvec and yvec into halves each
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

    # use quadratic multiply
    left_left = _quadratic_multiply(x_left, y_left)
    right_right = _quadratic_multiply(x_right, y_right)
    left_right = _quadratic_multiply(x_left, y_right)
    right_left = _quadratic_multiply(x_right, y_left)

    # use bitshift
    bitshift_LL = bit_shift(left_left, len(xvec))
    bitshift_LR = bit_shift(left_right, len(xvec) // 2)
    bitshift_RL = bit_shift(right_left, len(xvec) // 2)

    # sum combine halves
    sum = bitshift_LL.decimal_val + bitshift_LR.decimal_val + bitshift_RL.decimal_val + right_right.decimal_val

    # return the sum of all of the parts
    return BinaryNumber(sum)


def test_quadratic_multiply(x, y, f):
  start = time.time()
  # multiply two numbers x, y using function f
  
  # not entirely sure where to implement this - Sofia
  _quadratic_multiply(x, y)
  return (time.time() - start) * 1000



print(quadratic_multiply(BinaryNumber(5), BinaryNumber(5)))
print(
    test_quadratic_multiply(BinaryNumber(3), BinaryNumber(5),
                            quadratic_multiply))
