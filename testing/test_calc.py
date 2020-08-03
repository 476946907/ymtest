import pytest
import yaml
from decimal import *
import sys
sys.path.append("..")
from pythoncode.calc import Calculator


class TestCalc:
    def setup_class(self):
        self.cal = Calculator()

    @pytest.mark.parametrize(['a', 'b', 'result'], yaml.safe_load(open("./data.yaml"))['add'],
                             ids=['int', 'big num', 'xiaoshu', 'fushu', 'xiaoshu1'])
    def test_add(self, a, b, result):
        assert Decimal(result) == self.cal.add(a, b)

    @pytest.mark.parametrize(['a', 'b', 'result'], yaml.safe_load(open('./data.yaml'))['sub'],
                             ids=['int', 'big num', 'xiaoshu', 'fushu'])
    def test_sub(self, a, b, result):
        assert Decimal(result) == self.cal.sub(a, b)


    @pytest.mark.parametrize(['a', 'b', 'result'], yaml.safe_load(open('./data.yaml'))['mul'],
                              ids=['int', 'big num', 'xiaoshu', 'fushu'])


    def test_mul(self, a, b, result):
        assert Decimal(result) == self.cal.mul(a, b)

    @pytest.mark.parametrize(['a', 'b', 'result'], yaml.safe_load(open('./data.yaml'))['div'],
                             ids=['int', 'big num', 'xiaoshu', 'fushu'])
    def test_div(self, a, b, result):
        assert Decimal(result) == self.cal.div(a, b)
