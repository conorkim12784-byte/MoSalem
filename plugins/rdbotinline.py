from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information
from plugins.admin import *
from plugins.general import *
from plugins.developer import *
from plugins.group_rtb import *
from plugins.sudos import del_message, restart

################################
## Dev By: @ccqxx & debo ##
################################

@Client.on_callback_query(filters.regex("^rdbotinline (\\d+)$"))
async def rdbotinline(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("𝐢𝐧𝐟𝐨 🤖", callback_data="infobotinline " + str(m.from_user.id))],

    ])
    await m.reply_text("""
• كنت بشقط منك لله خير اؤمرني 😂❤️
""", reply_markup=keyboard)
@Client.on_callback_query(filters.regex("^rdbotinline2 (\\d+)$"))
async def rdbotinline2(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("𝐢𝐧𝐟𝐨 🤖", callback_data="infobotinline " + str(m.from_user.id))],

    ])
    await m.message.edit_text("""
• كنت بشقط منك لله خير اؤمرني 😂❤️
""", reply_markup=keyboard)
@Client.on_callback_query(filters.regex("^infobotinline (\\d+)$"))
async def infobotinline(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("𝗦𝗼𝗨𝗿𝗖𝗲 𝗕𝗲𝗧𝗮 👨‍💻", url=f"https://t.me/Ops_TALASHNY")],
        [InlineKeyboardButton("𝐛𝐚𝐜𝐤 ⬅️", callback_data="rdbotinline2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
• مرحبا بك عزيزي
• انا ك بوت بحبك اه والله 
dev { @Cv_TALASHNY } ♡
    """, reply_markup=keyboard)
