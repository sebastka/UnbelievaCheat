#!/usr/bin/env python3
from execute import execute

def main() -> int:
	commands: list = [
		'work',
		'deposit all'
	]

	return execute(commands)

exit(main())
