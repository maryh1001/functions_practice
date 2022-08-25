# print a greeting to user
def hello():
    print ("Hi User!!")
# accepts three arguments and returns a list with the arguments inside as list elements
def pack(item1, item2, item3):
    return [item1,item2, item3]

# accept a list of any length and print a series of strings that say "First I eat__" .. etc to "My lunch box is empty."

def eat_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

hello()
pack("a","b","c")
print(pack(1,2,3))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])
    


