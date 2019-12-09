from bs4 import BeautifulSoup
from generators import ProblemRetriver
from logging import getLogger
import requests

base_url = "https://atcoder.jp"
problem_list_path = "/contests/%s/tasks"
numbering = "abcdefghijklmnopqrstu"



class AtCoderProblemRetriver():
  def __init__(self):
    self.logger = getLogger(__name__)
    self._session = requests.Session()
    
  def get_problems(self, contest_name):
    problem_urls = self.get_problem_list(contest_name)
    problems = {}
    for index, problem_url in enumerate(problem_urls):
      result = self.get_single_problem(numbering[index], contest_name, problem_url)
      if result == None:
        break
      problems[numbering[index]] =  result
    return problems
  
  def get_problem_list(self, contest_name):
    urls = []
    problem_list_url = base_url + problem_list_path % (contest_name)
    
    self.logger.info("Accessing %s" % problem_list_url)

    response = self._session.get(problem_list_url)
    parser = BeautifulSoup(response.text, "html.parser")
    tbody = parser.find("tbody")
    trs = tbody.findAll("tr")
    for tr in trs:
      url = base_url + tr.find("td").find("a")["href"]
      self.logger.debug("Add %s" % url)
      urls.append(url)
    return urls

  def get_single_problem(self, problem_number, contest_name, problem_url):
    inputs = []
    outputs = []
    response = self._session.get(problem_url)
    if response.status_code != 200:
      self.logger.error("Error from remote url code: %d" % response.status_code)
      return None

    parser = BeautifulSoup(response.text, "html.parser")
    divs = parser.findAll("div", class_="part")

    is_input = True

    for index in range(len(divs)):
      element = divs[index].find("pre")
      if element != None and element.string != None:
        if is_input:
          inputs.append(element.string.strip())
          is_input = False
        else:
          outputs.append(element.string.strip())
          is_input = True
    res = []
    for ins, outs in zip(inputs, outputs):
      res.append({
        "input": ins,
        "output": outs
      })
    return res[:int(len(res)/2)]
