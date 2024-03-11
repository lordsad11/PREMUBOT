from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


async def getubot_cmd(client, message):
    x = await client.get_inline_bot_results(
        bot.me.username, f"ambil_ubot"
    )
    await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)



async def getubot_query(client, inline_query):
    msg = await MSG.USERBOT(0)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="💬",
                    reply_markup=InlineKeyboardMarkup(Button.ambil_akun(ubot._ubot[0].me.id, 0)),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )

