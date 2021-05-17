#!/usr/bin/env python3
from execute import execute

def main() -> int:
	users: list = [
		'x', # IDs of users to rob from
		'y'
	]

	commands: list = [ f'rob <@!{user}>' for user in users ]
	commands.append('deposit all')

	return execute(commands)

exit(main())
