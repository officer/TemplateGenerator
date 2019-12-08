from abc import ABCMeta, abstractmethod
from jinja2 import Template, FileSystemLoader, Environment
import os
from logging import getLogger
from pathlib import Path

class BaseGenerator:
  def __init__(self):
    super().__init__()
    self.logger = getLogger(__name__)
    
  
  def generate_problem_files(self, problems, contest_name):
    template_loader = FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)) + "/template")
    template_environment = Environment(loader=template_loader)
    test_template = template_environment.get_template("main.py")
    
    for problem_index, value in problems.items():
      path = "%s/%s/%s.py" % (os.getcwd(), contest_name, problem_index)
      with open(path, "w") as fp:
        fp.write(test_template.render())

  def generate_test_files(self, problems, contest_name):
    template_loader = FileSystemLoader(searchpath=os.path.dirname(os.path.abspath(__file__)) + "/template")
    template_environment = Environment(loader=template_loader)
    test_template = template_environment.get_template("test.py")

    # Problem and test generator
    for problem_index, datas in problems.items():
        test_dir = "%s/%s/tests/%s" % (os.getcwd(), contest_name, problem_index)
        if not os.path.exists( test_dir):
          os.mkdir(test_dir)
        for index, data in enumerate(datas):
            for category, value in data.items():
              path = "%s/%s/tests/%s/%s_%s.%s" % (os.getcwd(), contest_name, problem_index, problem_index, index, category)
              with open(path, "w") as fp:
                self.logger.debug("Writing into %s" % path)
                fp.write(value)


              self.logger.info("Generating tests...")
              # generate tests
              test_output = test_template.render(
                  {
                      "problem_index": problem_index,
                      "contest_name": contest_name,
                      "index": index
                  }
              )

              path = "%s/%s/tests/%s/test_%s_%s_%d.py" % (os.getcwd(), contest_name, problem_index, contest_name, problem_index, index)
              with open(path, "w") as fp:
                  self.logger.debug("Writing into %s" % path)
                  fp.write(test_output)