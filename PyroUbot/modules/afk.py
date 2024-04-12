

from PyroUbot import *

__MODULE__ = "Afk"
__HELP__ = """
Bantuan Untuk Afk

• Perintah: <code>{0}afk</code> [alasan]
• Penjelasan: Untuk mengaktifkan mode afk.
"""


@PY.UBOT("afk")
async def _(client, message):
    await set_afk(client, message)
    
