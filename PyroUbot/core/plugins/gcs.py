import asyncio
from gc import get_objects

from pyrogram.enums import ChatType

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from PyroUbot import *
from PyroUbot.config import *

#gcast
async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats

async def broadcast_group_cmd(client, message):
    if not message.reply_to_message:
        return await message.reply("ᴛᴇxᴛ ᴀɴᴅᴀ ᴍᴀɴᴀ ᴛᴜᴀɴ")
    emot_1 = await get_vars(client.me.id, "EMOJI_PROSES")
    emot_2 = await get_vars(client.me.id, "EMOJI_CEKLIS")
    emot_proses = emot_1 if emot_1 else "6298454498884978957"
    emot_ceklis = emot_2 if emot_2 else "5852871561983299073"
    if client.me.is_premium:
        _broadcast = f"""
<b><emoji id={emot_proses}></emoji>ᴘʀᴏsᴇs ɢɪᴋᴇs ᴛᴜᴀɴ</b>
"""
    else:
        _broadcast = f"""
<b>ᴘʀᴏsᴇs ɢɪᴋᴇs ᴛᴜᴀɴ</b>
"""
    msg = await message.reply(_broadcast, quote=True)

    send = get_message(message)

    chats = await get_broadcast_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    for chat_id in chats:
        if chat_id in blacklist:
            continue
        elif chat_id in BLACKLIST_CHAT:
            continue

        try:
            await send.copy(chat_id)
            done += 1
        except FloodWait as e:
            await send.copy(chat_id)
            done += 1
        except:
            pass

    emot_1 = await get_vars(client.me.id, "EMOJI_CEKLIS")
    emot_ceklis = emot_1 if emot_1 else "5852871561983299073"
    if client.me.is_premium:
        _ceklis = f"""
<b><emoji id={emot_ceklis}></emoji>✅ᴅᴀʜ sᴀᴍᴘᴀɪ ᴛᴜᴀɴ ᴅɪ {done} ɢʀᴏᴜᴘ ʙᴜsᴜᴋ</b>
"""
    else:
        _ceklis = f"""
<b> ᴅᴀʜ sᴀᴍᴘᴀɪ ᴛᴜᴀɴ ᴅɪ {done} ɢʀᴏᴜᴘ ʙᴜsᴜᴋ</b>
"""
    return await msg.edit(_ceklis)

async def broadcast_users_cmd(client, message):
    if not message.reply_to_message:
        return await message.reply("ᴛᴇxᴛ ʟᴜ ᴍᴀɴᴀ ᴀɴᴊɪɴɢ")
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ", quote=True)

    send = get_message(message)

    chats = await get_broadcast_id(client, "users")

    done = 0
    for chat_id in chats:
        if chat_id == client.me.id:
            continue
        elif chat_id in DEVS:
            continue

        try:
            await send.copy(chat_id)
            done += 1
        except FloodWait as e:
            await send.copy(chat_id)
            done += 1
        except:
            pass

    return await msg.edit(f"<b> ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛᴇʀᴋɪʀɪᴍ ᴋᴇ {done} ᴜsᴇʀs</b>")

async def broadcast_bot(client, message):
    msg = await message.reply("sᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏsᴇs ᴍᴏʜᴏɴ ʙᴇʀsᴀʙᴀʀ", quote=True)

    send = get_message(message)
    if not send:
        return await msg.edit("ᴍᴏʜᴏɴ ʙᴀʟᴀs sᴇsᴜᴀᴛᴜ ᴀᴛᴀᴜ ᴋᴇᴛɪᴋ sᴇsᴜᴀᴛᴜ...")
        
    susers = await get_list_from_vars(client.me.id, "SAVED_USERS")
    done = 0
    for chat_id in susers:
        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except:
            pass

    return await msg.edit(f"<b> ᴘᴇsᴀɴ ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴᴅᴀ ᴛ {done} ᴜsᴇʀs</b>")


async def send_msg_cmd(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ᴋᴇᴛɪᴋ ʏᴀɴɢ ʙᴇɴᴇʀ")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            if "_" in chat_id:
                msg_id, to_chat = chat_id.split("_")
                return await client.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
            else:
                return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(f"{t}")


async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if m:
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ],
    )
