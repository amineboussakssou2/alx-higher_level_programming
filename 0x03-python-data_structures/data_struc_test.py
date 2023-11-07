#!/usr/bin/python3
my_list = [10,72,100,54,25,90,40]
max = my_list[0]
for idx in range(len(my_list)):
  if my_list[idx] > max:
    max = my_list[idx]
    idx += 1
 
print("Max index is : {}".format(max))
