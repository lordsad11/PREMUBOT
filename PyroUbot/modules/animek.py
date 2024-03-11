from PyroUbot import *

__MODULE__ = "anime"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀᴅᴍɪɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>wall</code> 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>waifu</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> 

"""


@PY.UBOT("wall|waifu", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await anime_cmd(client, message)
