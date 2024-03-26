from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", 28025330))
API_HASH = getenv("API_HASH", "935e4ad87ef7ed016bd926baf95c4323")
BOT_TOKEN = getenv("BOT_TOKEN", None)
OWNER_ID = int(getenv("OWNER_ID", "1380008589"))
MONGO_URL = getenv("MONGO_URL", None)
SUPPORT_GRP = getenv("SUPPORT_GRP", "DEVELOPERSOFBOT")
UPDATE_CHNL = getenv("UPDATE_CHNL", "DEVELOPERSOFBOT")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@ZODEX66")

# Random Start Images
IMG = [
    "https://graph.org/file/7d5a442370c9981258fbe.jpg"
]


# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]


EMOJIOS = [
    "💣",
    "💥",
    "🪄",
    "🧨",
    "⚡",
    "🤡",
    "👻",
    "🎃",
    "🎩",
    "🕊",
]
