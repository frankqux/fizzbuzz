# def check(num: int):
#     if num % 15 == 0:
#         return "FizzBuzz"
#     elif num % 5 == 0:
#         return "Buzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     else:
#         return str(num)
#
#
import fizzbuzz


def test_fizz():
    assert fizzbuzz.check(3) == ("Fizz")


def test_buzz():
    assert fizzbuzz.check(5) == ("Buzz")


def test_fizzbuzz():
    assert fizzbuzz.check(15) == ("FizzBuzz")


def test_number():
    assert fizzbuzz.check(1) == ("1")


# Whoops.
def test_crap():
    pass
