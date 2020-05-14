import pytest


class Test1:

    def setup_class(self):
        print("setup_class")

    def teardown_class(self):
        print("teardown_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test1(self):
        print("test")
        assert 1 == 2

if __name__ == '__main__':
    pytest.main()
