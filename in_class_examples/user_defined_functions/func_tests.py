x = 1
print(x)
def example_func(local_x):
	local_x = local_x + 1
	print(local_x)
	return local_x
x = example_func(x)
print(x)