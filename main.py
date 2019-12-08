#!/usr/local/bin/python3

from bs4 import BeautifulSoup
from generators import AtCoderProblemRetriver, BaseGenerator
from fire import core
import os, sys
from jinja2 import Template, FileSystemLoader, Environment
from logging import config, getLogger
from pathlib import Path

class ProblemGenerator:
    def __init__(self):
        super().__init__()
        self.logger = getLogger(__name__)

    def generate(self, site_name, contest_name):
        if not os.path.exists("%s/%s/tests" % (os.getcwd(), contest_name)):
            self.logger.debug("Creating test directories...")
            os.makedirs("%s/%s/tests" % (os.getcwd(), contest_name))
            Path("%s/%s/__init__.py" % (os.getcwd(), contest_name)).touch()
            
        if site_name == "atcoder":
            self.logger.info("Generator... AtCoderProblemRetriver")
            generator = AtCoderProblemRetriver.AtCoderProblemRetriver()
            problems = generator.get_problems(contest_name)
            pass

        problem_generator = BaseGenerator.BaseGenerator()
        problem_generator.generate_problem_files(problems=problems, contest_name=contest_name)
        problem_generator.generate_test_files(problems, contest_name)

if __name__ == "__main__":
    core.Fire(ProblemGenerator)