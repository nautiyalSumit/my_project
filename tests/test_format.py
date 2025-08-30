from my_project import __version__


def test_version():
    assert __version__ is not None


def test_addition():
    assert 2 + 2 == 4
