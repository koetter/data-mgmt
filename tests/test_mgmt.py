import pytest
from data_mgmt import mgmt

def test_assert_false():
    assert False

def test_assert_true():
    assert True

def test_Config_init():
    con = mgmt.Config("dev")
    # print(dir(cf))
    assert con.env == "dev"

