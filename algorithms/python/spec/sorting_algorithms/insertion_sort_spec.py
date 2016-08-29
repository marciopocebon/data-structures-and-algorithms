from ivoire import describe, context
from expects import expect
from expects.matchers.built_in import equal, be_below_or_equal
from src.sorting_algorithms.insertion_sort import insertion_sort
import random

with describe(insertion_sort) as it:
  @it.before
  def before(test):
    unodered_list = [random.randrange(-1000,1000) for x in xrange(100)]
    test.manual_sorted_list, test.swaps = insertion_sort(unodered_list)
    test.automatic_sorted_list = sorted(unodered_list)
    test.worst_case = len(test.manual_sorted_list)**2

  with it('sorts the list') as test:
    expect(test.manual_sorted_list).to(equal(test.automatic_sorted_list))

  with it('performs better/equal to O(n**2) in the worst case') as test:
    expect(test.swaps).to(be_below_or_equal(test.worst_case))
