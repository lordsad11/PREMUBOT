from PyroUbot import *



__MODULE__ = "asupan"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴘᴀɴ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}asupan</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ɢᴀʙᴜᴛ ᴅᴏᴀɴɢ ɪɴɪ 

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}sex</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴅᴀᴘᴀᴛᴋᴀɴ ᴘᴀᴘ ʙᴜɢɪʟ ᴅᴀʀɪ ᴛᴜʜᴀɴ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}ayang</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ʙᴏᴋᴇᴘ  ʙɪᴀʀ ᴜɴᴛᴜᴋ ᴄᴏʟɪ  ᴅᴀɴ ᴄᴏʟᴍᴇᴋ
  """


@PY.UBOT("asupan", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await asupan(client, message)


@PY.UBOT("sex", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await xnxx(client, message)


@PY.UBOT("ayang", sudo=True)
@PY.TOP_CMD
async def _(client, message):
    await ayang(client, message)
