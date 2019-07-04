import hello_world


def test_increment():
    assert hello_world.increment(1) == 2


def test_decrement():
    assert hello_world.decrement(5) == 4
