import pytest
import requests_mock
import requests
from generators.AtCoderProblemRetriver import AtCoderProblemRetriver
import sys, os

@pytest.fixture(scope="module")
def pwd():
  path = os.path.dirname( os.path.abspath(__file__) )
  return path

def test_AtCoder_problem_list(pwd):
  with requests_mock.mock() as m:
    problem_list = open(pwd + "/contents/test_list.html")
    content = "".join(problem_list.readlines())
    m.get("https://atcoder.jp/contests/test/tasks", text=content)
    generator = AtCoderProblemRetriver()
    generator.get_problem_list("test")



