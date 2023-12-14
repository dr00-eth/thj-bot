from thjbotapi import ThjBotAPI
from streambot import StreamBot
import constants
import os
import logging

# Create a logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('your_log_file.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#Prompt 0 - THJ Bot
streambot1 = StreamBot(os.getenv('OPENAI_KEY'), "THJ Bot", genesis_prompt=constants.OPENAI_PROMPT[0], verbosity=0)

api = ThjBotAPI([streambot1], origins=["NEED URL OF PROD UI HERE"], verbosity=0, debug=False, port=8008, allow_model_override=True)

server = api.start()
