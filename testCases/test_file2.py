import pytest

@pytest.mark.group1
class Test_002:
    def test_sum_004(self):
        a = 3
        b = 4
        sum = a+b
        print(sum)
        if sum == 7:
            print("test_sum_002 is passed")
            assert True

        else:
            print("test_sum_002 is failed")
            assert False

