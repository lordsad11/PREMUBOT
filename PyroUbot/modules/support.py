from PyroUbot import *



@PY.CALLBACK("profil")
async def _(client, callback_query):
    await profilcallback(client, callback_query)
