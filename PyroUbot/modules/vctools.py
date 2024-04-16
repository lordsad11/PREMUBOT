from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from PyroUbot import *
from pytgcalls.exceptions import AlreadyJoinedError
from pytgcalls.types.input_stream import InputAudioStream, InputStream


MODULE = "vctools"
HELP = f"""
✘ Bantuan Untuk Voice Chat

๏ Perintah: <code>startvc</code>
◉ Penjelasan: Untuk memulai voice chat grup.

๏ Perintah: <code>stopvc</code>
◉ Penjelasan: Untuk mengakhiri voice chat grup.
           
๏ Perintah: <code>joinvc</code>
◉ Penjelasan: Untuk bergabung voice chat grup.

๏ Perintah: <code>leavevc</code>
◉ Penjelasan: Untuk meninggalkan voice chat grup.
"""


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"No group call Found {err_msg}")
    return False

list_data = []


def remove_list(user_id):
    list_data[:] = [item for item in list_data if item.get("id") != user_id]


def add_list(user_id, text):
    data = {"id": user_id, "nama": text}
    list_data.append(data)


def get_list():
    if not list_data:
        return "<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜsᴇʀ ᴅɪ ᴅᴀʟᴀᴍ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴍᴀɴᴀᴘᴜɴ</b>"

    msg = "\n".join(item["nama"] for item in list_data)
    return msg


@PY.UBOT("joinvc")
async def _(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    text = f"• <b>[{client.me.first_name} {client.me.last_name or ''}](tg://user?id={client.me.id})</b> | <code>{chat_id}</code>"
    try:
        await client.PyroUbot.start(chat_id, join_as=client.me.id)
    except Exception as e:
        return await message.reply(f"ERROR: {e}")
    await message.reply("<b>izin parkir puh</b>")
    await asyncio.sleep(5)
    await client.PyroUbot.set_is_mute(True)
    add_list(client.me.id, text)


@PY.UBOT("leavevc")
async def _(client, message):
    try:
        await client.PyroUbot.stop()
    except Exception as e:
        return await message.reply(f"ERROR: {e}")
    remove_list(client.me.id)
    return await message.reply("<b>izin turun puh</b>")


@PY.UBOT("listos")
async def _(client, message):
    await message.reply(get_list())
