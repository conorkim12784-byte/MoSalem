from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

################################
## Dev By: @ccqxx & debo ##
################################

@Client.on_callback_query(filters.regex("^commandtrteb (\\d+)$"))
async def commandtrteb(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("{اوامر الرفع المرتبه}", callback_data="raf3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("{اوامر التسليه المرتبه}", callback_data="tasliy4 " + str(m.from_user.id))],
        [InlineKeyboardButton("{اوامر القفل المرتبه}", callback_data="fat5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("{اوامر الفتح المرتبه}", callback_data="qefl " + str(m.from_user.id))],
        [InlineKeyboardButton("{اوامر التاك والكشف المرتبه}", callback_data="takk " + str(m.from_user.id))] +

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("""
⌔︙اهلا بك عزيزي في قائمه الاوامر المرتبه
—————————————
⌔︙{ الرفع } ← اوامــر الرفع
⌔︙{ الفتح } ← اوامــر الفتح
⌔︙{ القفل } ← اوامــر القفل
⌔︙{ التاك } ← اوامـر الكشف و التاك
⌔︙{ التسليه } ← اوامــر التسليه
""", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^commandtrteb2 (\\d+)$"))
async def commandtrteb2(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("{اوامر الرفع المرتبه}", callback_data="raf3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("{اوامر التسليه المرتبه}", callback_data="tasliy4 " + str(m.from_user.id))],
        [InlineKeyboardButton("{اوامر القفل المرتبه}", callback_data="fat5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("{اوامر الفتح المرتبه}", callback_data="qefl " + str(m.from_user.id))],
        [InlineKeyboardButton("{اوامر التاك والكشف المرتبه}", callback_data="takk " + str(m.from_user.id))] +

        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⌔︙اهلا بك عزيزي في قائمه الاوامر المرتبه
—————————————
⌔︙{ الرفع } ← اوامــر الرفع
⌔︙{ الفتح } ← اوامــر الفتح
⌔︙{ القفل } ← اوامــر القفل
⌔︙{ التاك } ← اوامـر الكشف و التاك
⌔︙{ التسليه } ← اوامــر التسليه
""", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^raf3 (\\d+)$"))
async def raf3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="commandtrteb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⌔︙اوامر الرفع المرتبه كالتالي ...
—————————————
⌔︙رفع مميز ← م
⌔︙رفع ادمن ← اد
⌔︙رفع منشئ ← من
—————————————
⌔︙رفع مطور ← مط
⌔︙رفع مطور ثانوي ← ثانوي
—————————————
    """, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^fat5 (\\d+)$"))
async def fat5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="commandtrteb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⌔︙اهلا بك عزيزي في اوامر الفتح المرتبه ...
—————————————
⌔︙فتح الاشعارات ← فف
⌔︙فتح الرابط ← فر
⌔︙فتح جمالي ← فج
⌔︙فتح الردود ← ررف
⌔️︙فتح الدردشه ← فد
⌔︙فتح المعرفات ← فا
⌔︙فتح الملصقات ← فص
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^qefl (\\d+)$"))
async def qefl(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="commandtrteb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⌔︙ اهلا بك عزيزي في اوامر القفل ...
—————————————
⌔︙ قفل الاشعارات ← قق
—————————————
⌔︙ قفل الرابط ← قر
⌔︙ قفل جمالي ← قج
⌔︙ قفل الردود ← ررق
—————————————
 قفل الدردشه ← قد
—————————————
⌔︙ قفل المعرفات ← قا
—————————————
⌔︙ قفل الملصقات ← قص
—————————————
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^takk (\\d+)$"))
async def takk(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="commandtrteb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⌔︙ اهلا بك في اوامر التاك و الكشف المرتبه ..
—————————————
▶️╖ كشف ← ك
🎶╢ كشف القيود ← كق
📹╢ تاك ← تت
🔴╢ تاك للكل ← تك
🔴╢ رفع القيود ← رف
—————————————
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^tasliy4 (\\d+)$"))
async def tasliy4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="commandtrteb2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("""
⌔︙ اهلا بك عزيزي في اوامر التسليه ...
⌔︙ مسح المكتومين ← ،،
—————————————
⌔︙ اضف رد ← رد
⌔︙ اضف رد عام ← رع
⌔︙ حذف رد عام ← حع
⌔︙ اضف امر ← امر
⌔︙ غنيلي ← غ
⌔︙ نقاطي ← ن
⌔︙ رسائلي ← رس
⌔︙ لغز ← ل
⌔︙ معاني ← مع
⌔︙ حزوره ← ح
—————————————
    """, reply_markup=keyboard)
