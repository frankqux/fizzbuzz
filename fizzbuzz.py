def check(num: int):
    if num % 15 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


def test_fizz():
    assert check(3) == ("Fizz")


def test_buzz():
    assert check(5) == ("Buzz")


def test_fizzbuzz():
    assert check(15) == ("FizzBuzz")


def test_number():
    assert check(1) == ("1")
