import nextcord #type: ignore
from nextcord.ext import commands #type: ignore
import aiosqlite #type: ignore
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

intents = nextcord.Intents.all()
guild_id = 1273388243626496033
client = commands.Bot(command_prefix="?", intents=intents)
DATABASE_PATH = "database.db"


# Assuming you have commands defined in commands.py

from commands import *
client.run("MTI3MzM4MjAwOTY3MDIwNTUwMQ.G6tskb.ldV6KfB7QOsmSoO0-wBcVjqr3aVQkagtz009Dk")

