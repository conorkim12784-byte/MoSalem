from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import get_bot_information


async def taquum(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⭐", callback_data="starone " + str(m.from_user.id))],
        [InlineKeyboardButton("⭐⭐", callback_data="startwo " + str(m.from_user.id))],
        [InlineKeyboardButton("⭐⭐⭐", callback_data="starthree " + str(m.from_user.id))],
        [InlineKeyboardButton("⭐⭐⭐⭐", callback_data="starfor " + str(m.from_user.id))],
        [InlineKeyboardButton("⭐⭐⭐⭐⭐", callback_data="starfive " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("◍ مرحبا بك ياعزيزي يمكنك الان تقييم البوت 🌟", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^starone (\\d+)$"))
async def starone(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    taquum_text = """◍|مرحبا بك عزيزي المستخدم
• تقييمك هو ⭐
شكرا لك علي التقييم
"""
    await m.message.reply_text(taquum_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^startwo (\\d+)$"))
async def startwo(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    taquum_text = """◍|مرحبا بك عزيزي المستخدم
• تقييمك هو ⭐⭐
شكرا لك علي التقييم
"""
    await m.message.reply_text(taquum_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^starthree (\\d+)$"))
async def starthree(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    taquum_text = """◍|مرحبا بك عزيزي المستخدم
• تقييمك هو ⭐⭐⭐
شكرا لك علي التقييم
"""
    await m.message.reply_text(taquum_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^starfor (\\d+)$"))
async def starfor(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    taquum_text = """◍|مرحبا بك عزيزي المستخدم
• تقييمك هو ⭐⭐⭐⭐
شكرا لك علي التقييم
"""
    await m.message.reply_text(taquum_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^starfive (\\d+)$"))
async def starfive(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    taquum_text = """◍|مرحبا بك عزيزي المستخدم
• تقييمك هو ⭐⭐⭐⭐⭐
شكرا لك علي التقييم
"""
    await m.message.reply_text(taquum_text, reply_to_message_id=mid)
    