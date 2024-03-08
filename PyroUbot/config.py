import os

DEVS = [
    1978415696,
    
]

API_ID = int(os.getenv("API_ID", "22377432"))

API_HASH = os.getenv("API_HASH", "69dbb3a23605d52444caf76c39631dd6")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7078858216:AAHTyGjfPsaoo5oclMqChGmNojUX0yyQXgY")

OWNER_ID = int(os.getenv("OWNER_ID", "1978415696"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002073087511"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002073087511").split()))

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


