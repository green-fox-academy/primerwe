# selection sort:
def return_second_biggest_item(array):
  
  def sort_array():
    
    for i in range(len(array)):
      max_index = i
      for j in range(i+1, len(array)):
        if array[j] > array[max_index]:
          max_index = j
      temp = array[i]
      array[i] = array[max_index]
      array[max_index] = temp
    return array

  return sort_array()[1]

print ('The second biggest item is: ', return_second_biggest_item([5, 4, 2, 1, 1, 5, 3]))


def bubble_sort_second_biggest_item(array):
  
  for number in range(len(array)-1, 0, -1):
    for i in range(number):
      if array[i] > array[i+1]:
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp

  print('print This is bubblesorted: ', array)

bubble_sort_second_biggest_item([5, 4, 2, 1, 1, 5, 3])

