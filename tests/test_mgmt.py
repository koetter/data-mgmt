import pytest
from data_mgmt import mgmt

def test_assert_false():
    assert False

def test_assert_true():
    assert True

def test_Config_init():
    con = mgmt.Config()
    # print(dir(cf))
    assert con.PROJKEY == "Uu9-beHvHjbQruTWrs8Pe5jb3FMisrv2XxCaW0U3Ro0="

