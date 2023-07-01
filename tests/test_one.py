def test_passing():
    assert (1, 2, 3) == (1, 2, 3)


# def test_fail():
#    assert 'test' == 'testing'

def test_pass_1():
    assert 'test' != 'testing'


def test_pass_2():
    assert 'test' in 'testing'


def test_not():
    a = 'test'
    b = 'testing'
    assert not a == b


def test_not_equal():
    x = ["a", "b", "c"]
    y = [1, 2, 3]
    assert not x == y
