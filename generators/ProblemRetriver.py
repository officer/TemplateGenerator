from abc import ABCMeta, abstractmethod

class ProblemRetriver():

  def __init__(self):
    super().__init__()

    """
    Get Problems
    {
        'a': [
            'input': [,,,],
            'output': [,,]
        ]
    }
    """
  @abstractmethod
  def get_problems(self, contest_name):
    pass
  