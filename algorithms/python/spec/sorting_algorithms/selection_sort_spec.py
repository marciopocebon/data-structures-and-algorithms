from ivoire import describe, context
from expects import expect
from expects.matchers.built_in import equal, be_below_or_equal
from src.sorting_algorithms.selection_sort import selection_sort
import random

with describe(selection_sort) as it:
  @it.before
  def before(test):
    unodered_list = [random.randrange(-1000,1000) for x in xrange(100)]
    test.manual_sorted_list = selection_sort(unodered_list)
    test.automatic_sorted_list = sorted(unodered_list)

  with it('sorts the list') as test:
    expect(test.manual_sorted_list).to(equal(test.automatic_sorted_list))
