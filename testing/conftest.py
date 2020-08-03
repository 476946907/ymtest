import pytest


@pytest.fixture(autouse=True)
def calcu():
    print("开始计算")
    yield
    print("计算结束")