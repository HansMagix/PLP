my_list = []
to_append = [10, 20, 30, 40]
another_one = [50, 60, 70]
my_list += to_append
my_list += another_one
my_list.remove(my_list[-1])
my_list.sort()
print(my_list.index(30))