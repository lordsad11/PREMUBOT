import asyncio
from datetime import datetime

from pyrogram.types import InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import bot, ubot
from PyroUbot.config import LOGS_MAKER_UBOT
from PyroUbot.core.database import (get_chat, get_expired_date,
                                    rem_expired_date, remove_chat, remove_ubot,
                                    rm_all)
from PyroUbot.core.helpers import MSG, Button


async def expiredUserbots():
    while True:
        for X in ubot._ubot:
            try:
                time = datetime.now(timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
                exp = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")
                if time == exp:
                    await X.unblock_user(bot.me.username)
                    for chat in await get_chat(X.me.id):
                        await remove_chat(X.me.id, chat)
                    await rm_all(X.me.id)
                    await remove_ubot(X.me.id)
                    await rem_expired_date(X.me.id)
                    ubot._get_my_id.remove(X.me.id)
                    ubot._ubot.remove(X)
                    await X.log_out()
                    await bot.send_message(
                        LOGS_MAKER_UBOT,
                        MSG.EXPIRED_MSG_BOT(X),
                        reply_markup=InlineKeyboardMarkup(Button.expired_button_bot()),
                    )
                    await bot.send_message(
                        X.me.id, "<b>💬 ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴀɴᴅᴀ ᴛᴇʟᴀʜ ʙᴇʀᴀᴋʜɪʀ"
                    )
            except:
                pass
        text = await bot.send_message(
            LOGS_MAKER_UBOT,
            f"<b>🗓️ Tanggal:</b> <code>{time}</code>\n<b>🕕 Jam:</b> <code>{clock}</code>",
        )
        await asyncio.sleep(3600)
        await text.delete()


async def rebot():
    while True:
        await asyncio.sleep(3600)
        try:
            await bot.send_message(LOGS_MAKER_UBOT, "<b>Auto Restart On...</b>")
            LOGGER(__name__).info("BOT SERVER RESTARTED !!")
        except Exception as err:
            LOGGER(__name__).info(f"{err}")
        await asyncio.sleep(2)
        await bot.send_message(LOGS_MAKER_UBOT, "✅ <b>Bot Berhasil Di Restart.</b>")
        args = [sys.executable, "-m", "PyroUbot"]
        execle(sys.executable, *args, environ)


async def restart_all():
    asyncio.get_event_loop().create_task(rebot())
  
            except Exception as e:
                print(f"Error: - {X.me.id} - :{str(e)}")
        await asyncio.sleep(10)
