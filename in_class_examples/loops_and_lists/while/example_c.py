def run_command(cmd):
	print(f"Pretend this running the {cmd} command!")

command = input()
while command != 'quit':
	run_command(command)
	command = input()