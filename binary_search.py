print("Print welcome to the game!!!")



def binary_search(a_list, an_item):
   first = 0
   last = len(a_list) - 1

   while first <= last:
       mid_point = (first + last) // 2
       if a_list[mid_point] == an_item:
           return True
       else:
           if an_item < a_list[mid_point]:
               last = mid_point - 1
           else:
               first = mid_point + 1
   return False



if __name__ == '__main__':
   a_list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]

