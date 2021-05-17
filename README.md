# UnbelievaCheat

## Instructions

1. Configure `execute.py` with your token, the channel ID and the bot ID;
2. Run `crime.py`, `rob.py` and `work.py`

## Automation

Use cron:
```
0 * * * * python3 work.py # Every hour
0 */4 * * * python3 crime.py # Every four hours
0 20 * * * python3 /home/sebastian/Dev/Python/Slave/rob.py # Every day at 20:00
```
