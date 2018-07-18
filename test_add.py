import add


def test_add_1_with_1_expect_2():
    assert add.add(1, 1) == 2


def test_add_1_with_3_expect_2():
    assert add.add(1, 3) == 10


def test_sub_2_with_1_expect_1():
    assert add.sub(2, 1) == 1