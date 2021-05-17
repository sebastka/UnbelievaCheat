#!/usr/bin/env python3
import discum
import time

def execute(commands: list) -> int:
	my_token: str = '' # Your personal or bot token
	channel_id: str = '' # Channgel to post into
	bot_id: str = '' # UnbelievaBoat

	# Login
	bot = discum.Client(
		token = my_token,
		log = {
			'console': False,
			'file': 'log.txt'
		},
		user_agent = 'random'
	)

	# Execute each command and wait five seconds
	for command in commands:
		bot.sendMessage(channel_id, f'<@!{bot_id}> {command}')
		time.sleep(5)

	return 0
