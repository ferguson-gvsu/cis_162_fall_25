x = 1
print(x)
def example_func():
	global x
	x = x + 1
	print(x)
example_func()
print(x)