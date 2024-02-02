import os

DEVS = [
    1978415696,
    2033248262,
    6980654842,
]

API_ID = int(os.getenv("API_ID", "14920143"))

API_HASH = os.getenv("API_HASH", "5a316e55fb121d9b5e891b5ff07d4677")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6715085237:AAG_e-Wz-4Ch4YqkNgVF5YGm2xe69NlrQeI")

OWNER_ID = int(os.getenv("OWNER_ID", "1978415696"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002073424041"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001994121863,-1001812143750,-1001473548283,-1001390552926,-1001573099403,-1001810928340,-1001619428365,-1001825363971,-1001864253073").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "550"))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

COMMAND = os.getenv("COMMAND", ".")
PREFIX = COMMAND.split()

OPENAI_KEY = os.getenv(
    "OPENAI_KEY",
    "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",
).split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://vewonon211:vewonon211@joysoy.kokbtub.mongodb.net/?retryWrites=true&w=majority",
)


