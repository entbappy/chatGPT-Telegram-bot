import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
import openai

class Reference:
    """
    A class to store the previous response from the chatGPT API.
    """
    def __init__(self) -> None:
        self.response = ""


# Load environment variables
load_dotenv()

# Set up OpenAI API key

# Create a reference object to store the previous response

# Bot token can be obtained via https://t.me/BotFahter
TOKEN = os.getenv("TOKEN")

# Model used in chatGPT

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot)

def clear_past():
    """
    A function to clear the previous conversation and context.
    """
    raise NotImplementedError

@dispatcher.message_handler(commands=['start'])
async def welcome(message: types.Message):
    """
    A handler to welcome the user and clear past conversation and context.
    """
    raise NotImplementedError

@dispatcher.message_handler(commands=['clear'])
async def clear(message: types.Message):
    """
    A handler to clear the previous conversation and context.
    """
    raise NotImplementedError

@dispatcher.message_handler(commands=['help'])
async def helper(message: types.Message):
    """
    A handler to display the help menu.
    """
    raise NotImplementedError

@dispatcher.message_handler()
async def chatgpt(message: types.Message):
    """
    A handler to process the user's input and generate a response using the chatGPT API.
    """
    raise NotImplementedError


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
