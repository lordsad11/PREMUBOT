import os

DEVS = [
    5302505460,
    6583031844,
    
]

API_ID = int(os.getenv("API_ID", "23806826"))

API_HASH = os.getenv("API_HASH", "8da7a71f393f6149c7e1bc36731fca9a")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7065858309:AAGkRoIs3tUS8hytC9crBTFybredcxsGGuk")

OWNER_ID = int(os.getenv("OWNER_ID", "5302505460" "6583031844"))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002024655650"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002073087511 -1001361294038 -1001387666944 -1001109500936 -1001050982793 -1001256902287 -1001473548283 -1001599474353 -1001692751821 -1001473548283 -1001459812644 -1001433238829 -1001476936696 -1001327032795 -1001294181499 -1001419516987 -1001209432070 -1001296934585 -1001481357570 -1001459701099 -1001109837870 -1001485393652 -1001354786862 -1001109500936 -1001387666944 -1001390552926 -1001752592753 -1001777428244 -1001771438298 -1001287188817 -1001812143750 -1001883961446 -1001753840975 -1001896051491 -1001578091827 -1001284445583 -1001927904459 -1001675396283 -1001825363971 -1001537280879 -1001302879778 -1001797285258 -1001864253073 -1001876092598 -1001608847572 -1001451642443 -1001538826310 -1001608701614 -1001861414061 -1001406767793 -1001306409796 -1002136866494").split()))

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
    "mongodb+srv://musik:0@cluster8.j9rtyke.mongodb.net/?retryWrites=true&w=majority&appName=Cluster8",
)


