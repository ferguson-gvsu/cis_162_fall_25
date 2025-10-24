def my_func(in_str):
	return in_str[-1]
my_list = ['dog', 'cat', 'doe', 'ant']
print(sorted(my_list, key=my_func))
