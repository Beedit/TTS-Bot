# TTS-Bot
# This bot does not work well right now. Like at all. It should not be used.
## A Discord Text-To-Speech bot written in python.

#### To do list
- [x] Make the bot work
- [ ] Make a queue system so that no messages get skipped (currently working kinda but not if message is too small.)
- [ ] Make the channel specific for each server to use tts in instead of the entire server
- [ ] Give each user using the bot a different voice using different language tts bots for voices (toggleable maybe)

### Why?

Got bored. Thought it would be fun. 

## How to use it

1. Install GTTS, dotenv, Pycord and FFMPEG

```
pip install gtts py-cord python-dotenv ffmpeg
```

2. In the file named .env, add your bot token.

3. In main.py, add your server ids to the servers list.

4. Run the bot with the command:

```
python3 main.py
```
