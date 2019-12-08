import sys, os
import collections
from {{ contest_name }} import {{ problem_index }}

def test_{{ contest_name }}_{{ problem_index }}():
  with open("{{ contest_name }}/tests/{{ problem_index }}/{{ problem_index }}_{{ index }}.input") as fp:
    output = {{ problem_index }}.solve(fp)
    with open("{{ contest_name }}/tests/{{ problem_index }}/{{ problem_index }}_{{ index }}.output") as fp2:
      lines = [ line.strip() for line in fp2.readlines() ]
      assert lines == output
