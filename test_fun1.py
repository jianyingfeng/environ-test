import pytest
import requests


base_url = os.environ['base_url']


def test_001(get_sex):
    r = requests.get(url=base_url+'/testcases/5/')
    assert r.json('testcase_name') == '查看项目列表接口_正向用例'