from ivoire import describe, context
from expects import expect
from expects.matchers.built_in import equal, be_below_or_equal
from src.searching_algorithms.breadth_first_search import breadth_first_search
import random

with describe(breadth_first_search) as it:
  @it.before
  def before(test):
    test.adjacency_list = [
      [1, 2, 3, 4],
      [0, 3],
      [0],
      [0, 1, 5, 7],
      [0, 7],
      [3, 6, 7],
      [5],
      [3, 4, 5],
    ]

  with it('makes a breadth first traversal') as test:
    response = breadth_first_search(test.adjacency_list, 0)

    expected_response = [
      {'predecessor': None, 'distance': 0},
      {'predecessor': 0, 'distance': 1},
      {'predecessor': 0, 'distance': 1},
      {'predecessor': 0, 'distance': 1},
      {'predecessor': 0, 'distance': 1},
      {'predecessor': 3, 'distance': 2},
      {'predecessor': 5, 'distance': 3},
      {'predecessor': 3, 'distance': 2}
    ]

    expect(response).to(equal(expected_response))
