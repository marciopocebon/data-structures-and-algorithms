def swap(array, x, y):
  """
    Swaps element from index x by y from the array.

    Running time: O(1)
  """

  temp_x = array[x]
  array[x] = array[y]
  array[y] = temp_x

def select_smallest_element(array, lower_bound):
  """
    Finds the smallest number on the array and returns its value and its index.

    Running time: O(n)
  """

  max = float('inf')
  min = (max, -1)

  for i in xrange(lower_bound, len(array)):
    if array[i] < min[0]:
      min = (array[i], i)

  return min


def selection_sort(array):
  """
    Sorts the array and returns it.

    Running time: O(n**2)
  """

  lower_bound = 0

  # Running time: O(n)
  while(lower_bound <= len(array)-1):
    value, index = select_smallest_element(array, lower_bound)

    swap(array, index, lower_bound)

    lower_bound = lower_bound + 1

  return array
