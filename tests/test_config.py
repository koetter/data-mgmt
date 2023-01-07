import pytest
from data_mgmt import configuration

def test_assert_false():
    assert False

def test_assert_true():
    assert True

def test_Config_init():
    # print(dir(cf))
    assert configuration.PROJKEY == "Uu9-beHvHjbQruTWrs8Pe5jb3FMisrv2XxCaW0U3Ro0="

