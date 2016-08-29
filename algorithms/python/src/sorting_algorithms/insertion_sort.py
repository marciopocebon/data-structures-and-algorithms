import random

def insertion_sort(items):
  """Return the list in sort order and the number of swaps.

  Implements insertion sort algorithm.
  """

  swaps = 0

  # caches the size of the list
  items_size = len(items)

  # iterates over the list, skipping the first item,
  # since there is no previous items to compare to
  for i in xrange(1, items_size):
    # stores the index of the previous item
    j = i-1

    # iterates over the list backwards
    # and swaps items when necessary
    while j >= 0 and items[i] < items[j]:
      swaps = swaps + 1
      # caches both values from i and j
      item_i = items[i]
      item_j = items[j]

      # swap
      items[j] = item_i
      items[i] = item_j

      # decrements j and i
      # in order to be able to compare previous items
      i = i - 1
      j = j - 1

  # returns the sorted list
  return items, swaps
