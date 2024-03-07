from src.main import ret1


def capital_case(x):
    return x.capitalize()


def test_capital_case():
    assert capital_case("semaphore") == "Semaphore"


def test_ret1():
    assert ret1() == 1


def test_main2():
    print("Hi")
