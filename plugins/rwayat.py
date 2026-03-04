"""
        [InlineKeyboardButton("رجوع ⬅️", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("➡️ التالي", callback_data="Yrw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
"""

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information


################################
## Dev By: @LeoMedo & @N2GEH  ##
################################

@Client.on_callback_query(filters.regex("^rwaiat (\\d+)$"))
async def rwaiat(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("1-| الروايات والقصص | 📚", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("2-| المكتبة الإسلامية |🕋 ", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("3-| الأدب والشعر |📜 ", callback_data="Yrw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("4-| التقنية والبرمجة |💻 ", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("5-| علم النفس والمجتمع |👥 ", callback_data="Yrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("6-| مكتبة اللغات |🌐 ", callback_data="Yrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("7-| مكتبة الموضوعات |💬 ", callback_data="Yrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("8-| كتب الأطفال |👦🏻 ", callback_data="Yrw7 " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("اهلا بيك في مكتبة روايات الشامله\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^rwaiat2 (\\d+)$"))
async def rwaiat2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("1-| الروايات والقصص | 📚", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("2-| المكتبة الإسلامية |🕋 ", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("3-| الأدب والشعر |📜 ", callback_data="Yrw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("4-| التقنية والبرمجة |💻 ", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("5-| علم النفس والمجتمع |👥 ", callback_data="Yrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("6-| مكتبة اللغات |🌐 ", callback_data="Yrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("7-| مكتبة الموضوعات |💬 ", callback_data="Yrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("8-| كتب الأطفال |👦🏻 ", callback_data="Yrw7 " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مكتبة روايات الشامله\n√", reply_markup=keyboard)
    return


# rwaiat 1 rw & kssas
@Client.on_callback_query(filters.regex("^Yrw1 (\\d+)$"))
async def Yrw1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("1- | روايات عربية | • 🌻 •", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("2- | روايات عالمية | • 🎭 •", callback_data="rwglb " + str(m.from_user.id))],
        [InlineKeyboardButton("3- | روايات مترجمة | • ♻️ •", callback_data="rwtr " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | روايات والقصص |\n√", reply_markup=keyboard)
    return


# rwaiat 1 ما بداخل اقسام روايات العربيه
@Client.on_callback_query(filters.regex("^rwar (\\d+)$"))
async def rwar(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 دعاء عبدالرحمن", callback_data="Zrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منى سلامة", callback_data="Zrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 نور عبد المجيد", callback_data="Zrw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 نجيب الكيلاني", callback_data="Zrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 أشرف العشماوي", callback_data="Zrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 الف ليله وليله", callback_data="Zrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منوعات عربيه", callback_data="Zrw7 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة | روايات عربية | \n√", reply_markup=keyboard)
    return


# rwaiat 2 ما بداخل رواياات عالميه
@Client.on_callback_query(filters.regex("^rwglb (\\d+)$"))
async def rwglb(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 مذكرات طالب", callback_data="Zrw8 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 محمد ياسر", callback_data="Zrw9 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منوعات عالميه", callback_data="Zrw10 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات العالميه \n√", reply_markup=keyboard)
    return


# rwaiat 3 ما بداخل روايات مترجمه
@Client.on_callback_query(filters.regex("^rwtr (\\d+)$"))
async def rwtr(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 وليام شكسبير", callback_data="Zrw11 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 ميلان كونديرا", callback_data="Zrw12 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 مارغريت آتوود", callback_data="Zrw13 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 أوسكار وايلد", callback_data="Zrw14 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 كارلوس زافون", callback_data="Zrw15 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw1 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة | روايات عالمية |\n√", reply_markup=keyboard)
    return


##################################################################################
# rwaiat List 1

@Client.on_callback_query(filters.regex("^Zrw1 (\\d+)$"))
async def Zrw1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ اغتصاب ولكن تحت سقف واحد", callback_data="ZZrw14 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اكتشفت زوجي في الاوتوبيس", callback_data="ZZrw15 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مع وقف التنفيذ", callback_data="ZZrw16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ولا في الاحلام", callback_data="ZZrw17 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عصير الكتب ايماجو", callback_data="ZZrw18 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ولو بعد حين", callback_data="ZZrw19 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ وقالت لي", callback_data="ZZrw20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ داو الا قليلا", callback_data="ZZrw21 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمه روايات 📚 دعاء عبدالرحمن\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw2 (\\d+)$"))
async def Zrw2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ كيغار", callback_data="ZZrw23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ من وراء حجاب", callback_data="ZZrw24 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قزم مينورا", callback_data="ZZrw25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ثاني اكسيد الحب", callback_data="ZZrw26 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ القصر الاسود", callback_data="ZZrw27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بلاد تركب العنكبوت", callback_data="ZZrw28 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جواد بلا فارس", callback_data="ZZrw29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مزرعة الدموع", callback_data="ZZrw30 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 منى سلامة \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw3 (\\d+)$"))
async def Zrw3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ أنا شهيره", callback_data="ZZrw32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أنا الخائن", callback_data="ZZrw33 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أريد رجلا", callback_data="ZZrw34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ لاسكالا", callback_data="ZZrw35 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحرمان الكبير", callback_data="ZZrw36 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ رغم الفراق", callback_data="ZZrw37 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أحلام ممنوعه", callback_data="ZZrw38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ذكريات محرمه", callback_data="ZZrw39 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أنتِ مني", callback_data="ZZrw40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ نساء ولكن", callback_data="ZZrw41 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ صولو", callback_data="ZZrw42 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 نور عبد المجيد \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw4 (\\d+)$"))
async def Zrw4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ أرض الأنبياء", callback_data="ZZrw44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حارة اليهود", callback_data="ZZrw45 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اعترافات", callback_data="ZZrw46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الذين يحترقون", callback_data="ZZrw47 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الرايات السوداء", callback_data="ZZrw48 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الرجل الذي أمن", callback_data="ZZrw49 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الربيع العاصف", callback_data="ZZrw50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ النداء الخالد", callback_data="ZZrw51 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أميرة الجبل", callback_data="ZZrw52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الطريق الطويل", callback_data="ZZrw53 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الظل الأسود", callback_data="ZZrw54 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ رحلة الي الله", callback_data="ZZrw55 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رجال وذئاب", callback_data="ZZrw56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ عذراء جاكرتا", callback_data="ZZrw57 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عمر يظهر في القدس", callback_data="ZZrw58 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ليل وقضبان", callback_data="ZZrw59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كفر الطماعين", callback_data="ZZrw60 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سرايفو حبيبتي", callback_data="ZZrw61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ اقبال الشاعر الثائر", callback_data="ZZrw62 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ في رحاب الطب النبوي", callback_data="ZZrw63 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تحت راية الأسلام", callback_data="ZZrw64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ نحن والأسلام", callback_data="ZZrw65 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حول الدين والدوله", callback_data="ZZrw66 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تجربتي الذاتيه", callback_data="ZZrw67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مذكرات الكيلاني", callback_data="ZZrw68 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 نجيب الكيلاني \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw5 (\\d+)$"))
async def Zrw5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ تويا", callback_data="ZZrw70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ البارمان", callback_data="ZZrw71 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بيت القبطيه", callback_data="ZZrw72 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كلاب الراعي", callback_data="ZZrw73 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ زمن الضباع", callback_data="ZZrw74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سيدة الزمالك", callback_data="ZZrw75 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تذكرة وحيده للقاهرة", callback_data="ZZrw76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المرشد", callback_data="ZZrw77 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سرقات مشروعة", callback_data="ZZrw78 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 أشرف العشماوي \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw6 (\\d+)$"))
async def Zrw6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الجزء 1", callback_data="ZZrw80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجزء 2", callback_data="ZZrw81 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء 3", callback_data="ZZrw82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجزء 4", callback_data="ZZrw83 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء 5", callback_data="ZZrw84 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجزء 6", callback_data="ZZrw85 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء 7", callback_data="ZZrw86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجزء 8", callback_data="ZZrw87 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء 10", callback_data="ZZrw88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجزء 11", callback_data="ZZrw89 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء 12", callback_data="ZZrw90 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجزء 13", callback_data="ZZrw91 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 الف ليله وليله \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw7 (\\d+)$"))
async def Zrw7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ حبيبي زوج صديقتي", callback_data="ZZrw93 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ خارج اسوار القلب", callback_data="ZZrw94 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تيستروجين", callback_data="ZZrw95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ في الحلال", callback_data="ZZrw96 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحب الملعون", callback_data="ZZrw97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أنا وانتي يساوي", callback_data="ZZrw98 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ينقصني انت", callback_data="ZZrw99 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ شبهة", callback_data="ZZrw100 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الشطار", callback_data="ZZrw101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مقتل بائع الكتب", callback_data="ZZrw102 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هوكر المحتال الأمريكي", callback_data="ZZrw103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أنثي لرجل واحد", callback_data="ZZrw104 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ زوجي مازال حبيبي", callback_data="ZZrw105 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ لعبة التحدي ", callback_data="ZZrw106 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحشاش", callback_data="ZZrw107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بره الدنيا", callback_data="ZZrw108 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مدينة الحب لا يسكنها العقلاء", callback_data="ZZrw109 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رجل يكره الأحذية", callback_data="ZZrw110 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwar " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 منوعات عربيه \n√", reply_markup=keyboard)
    return


# روايات عالميه
@Client.on_callback_query(filters.regex("^Zrw8 (\\d+)$"))
async def Zrw8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ جيف كيني", callback_data="ZZrw112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قوانين الأخ الأكبر", callback_data="ZZrw113 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ القشة الأخيره", callback_data="ZZrw114 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أيام الكلاب", callback_data="ZZrw115 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحقيقة المرة", callback_data="ZZrw116 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جنون المنزل", callback_data="ZZrw117 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ العجلة الثالثه", callback_data="ZZrw118 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحظ العاثر", callback_data="ZZrw119 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الرحلة الشاقة", callback_data="ZZrw120 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أيام زمان", callback_data="ZZrw121 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخطة الفاشلة", callback_data="ZZrw122 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بقلمك أنت", callback_data="ZZrw123 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رحلة الأحلام", callback_data="ZZrw124 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحرب الباردة", callback_data="ZZrw125 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رائع حقا", callback_data="ZZrw126 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwglb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 مذكرات طالب \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw9 (\\d+)$"))
async def Zrw9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ يوميات مكتئب", callback_data="ZZrw128 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بعد النسيان", callback_data="ZZrw129 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwglb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 محمد ياسر \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw10 (\\d+)$"))
async def Zrw10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ القارئ المخلص", callback_data="ZZrw131 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ موبي ديك", callback_data="ZZrw132 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أبناء غوندوانا", callback_data="ZZrw133 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جامع الأحلام الأرجوانية", callback_data="ZZrw134 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ احلام اينشتاين", callback_data="ZZrw135 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بيت الجمال", callback_data="ZZrw136 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ابنة البخيل", callback_data="ZZrw137 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مغامرات سبوتنيك", callback_data="ZZrw138 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عدوي اللدود", callback_data="ZZrw139 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ خالي العزيز نابليون", callback_data="ZZrw140 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ابقي معي", callback_data="ZZrw141 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ صاحب الظل الطويل", callback_data="ZZrw142 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تحت شمس توسكانا", callback_data="ZZrw143 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حكايات القط الشقي", callback_data="ZZrw144 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دون كيخوت", callback_data="ZZrw145 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المريضة الصامتة", callback_data="ZZrw146 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هيروشيما حبيبي", callback_data="ZZrw147 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كلهم علي حق", callback_data="ZZrw148 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ نسيم الصبا", callback_data="ZZrw149 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الهرطوقي", callback_data="ZZrw150 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مةت الراقصات", callback_data="ZZrw151 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ماريو بنديتي", callback_data="ZZrw152 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ كالماء للشوكولاتة", callback_data="ZZrw153 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أنماط غريبة من الحب", callback_data="ZZrw154 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حيث تركت روحي", callback_data="ZZrw155 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كيف تقع في الحب", callback_data="ZZrw156 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الفراشة", callback_data="ZZrw157 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حامض حلو", callback_data="ZZrw158 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ثقة", callback_data="ZZrw159 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كيف أصبحت غبيا", callback_data="ZZrw160 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أعجوبة", callback_data="ZZrw161 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بقايا القهوة", callback_data="ZZrw162 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الدجاجة التي حلمت بالطيران", callback_data="ZZrw163 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حياتك الثانيه تبدء", callback_data="ZZrw164 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ايزرابيل", callback_data="ZZrw165 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحديقة الخربة", callback_data="ZZrw166 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المليونير المتشرد", callback_data="ZZrw167 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بائعة الكتب", callback_data="ZZrw168 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سارقة الكتب", callback_data="ZZrw169 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الساعة ال 25", callback_data="ZZrw170 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحارس في حقل الشوفان", callback_data="ZZrw171 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ لا تقولي انك خائفة", callback_data="ZZrw172 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الزوجة التي بيننا", callback_data="ZZrw173 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwglb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 منوعات عالميه \n√", reply_markup=keyboard)
    return


# روايات مترجمة
@Client.on_callback_query(filters.regex("^Zrw11 (\\d+)$"))
async def Zrw11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الغنائيات ج1", callback_data="ZZrw175 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الغنائيات ج2", callback_data="ZZrw176 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ السونيتات الكامله", callback_data="ZZrw177 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ يوليوس قيصر", callback_data="ZZrw178 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هنري السادس", callback_data="ZZrw179 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ هنري الرابع", callback_data="ZZrw180 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هنري الخامس", callback_data="ZZrw181 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مكبث", callback_data="ZZrw182 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هاملت", callback_data="ZZrw183 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مأساه كيرولانس", callback_data="ZZrw184 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فينوس وأدونيس", callback_data="ZZrw185 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ عطيل", callback_data="ZZrw186 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سمبلين", callback_data="ZZrw187 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سيدان من فيرونا", callback_data="ZZrw188 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ضجة فارغة", callback_data="ZZrw189 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ عذاب الحب", callback_data="ZZrw190 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علي هواك", callback_data="ZZrw191 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ روميو وجوليت", callback_data="ZZrw192 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ريتشارد الثالث", callback_data="ZZrw193 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ زوجات وندسور", callback_data="ZZrw194 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دقة بدقة", callback_data="ZZrw195 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ خاب سعي العشاق", callback_data="ZZrw196 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حلم ليلة في منتصف الليل", callback_data="ZZrw197 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جعجعة بدون طحن", callback_data="ZZrw198 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تيمون الأثيني", callback_data="ZZrw199 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تيطس أندرونيكوس", callback_data="ZZrw200 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ترويلرس وكريسدا", callback_data="ZZrw201 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ترويض الشرسه", callback_data="ZZrw202 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تأجر البندقية", callback_data="ZZrw203 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بيريكليس", callback_data="ZZrw204 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الملك لير", callback_data="ZZrw205 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الملك ريتشارد ال2", callback_data="ZZrw206 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العين بالعين", callback_data="ZZrw207 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الملك جون", callback_data="ZZrw208 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العاصفة", callback_data="ZZrw209 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ العبرة ف النهاية", callback_data="ZZrw210 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الزوبعة", callback_data="ZZrw211 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أنطونيوس وكليوباترا", callback_data="ZZrw212 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ صاعا بصاع", callback_data="ZZrw213 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خير الأمور أحمدها", callback_data="ZZrw214 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtr " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 وليام شكسبير \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw12 (\\d+)$"))
async def Zrw12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ كائن لا تحتمل خفتة", callback_data="ZZrw216 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كتاب الضحك والنسيان", callback_data="ZZrw217 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الستارة", callback_data="ZZrw218 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الوصايا المغدورة", callback_data="ZZrw219 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ البطء", callback_data="ZZrw220 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحياه في مكان اخر", callback_data="ZZrw221 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخلود", callback_data="ZZrw222 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ غرامات مرحة", callback_data="ZZrw223 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الهوية", callback_data="ZZrw224 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ لقاء ميلان", callback_data="ZZrw225 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المزحة", callback_data="ZZrw226 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المحاورة", callback_data="ZZrw227 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فالس الوداع", callback_data="ZZrw228 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجهل", callback_data="ZZrw229 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فن الروايه", callback_data="ZZrw230 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حفلة التفاهة", callback_data="ZZrw231 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ادوار و الله", callback_data="ZZrw232 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ثلاثية حول الرواية", callback_data="ZZrw233 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtr " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 ميلان كونديرا \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw13 (\\d+)$"))
async def Zrw13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ كريك وأوريكس", callback_data="ZZrw235 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ عين القطة", callback_data="ZZrw236 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مفاوضات مع الموتي", callback_data="ZZrw237 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ البينيلوبيه", callback_data="ZZrw238 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ السفاح الأعمي", callback_data="ZZrw239 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حكاية الجارية", callback_data="ZZrw240 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المذنبة", callback_data="ZZrw241 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtr " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 مارغريت آتوود \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw14 (\\d+)$"))
async def Zrw14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ من الأعماق", callback_data="ZZrw243 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ صورة دوريان جراي", callback_data="ZZrw244 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ امرأة بلا أهميه", callback_data="ZZrw245 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سالومي", callback_data="ZZrw246 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الأمير السعيد", callback_data="ZZrw247 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سمفونية البحر", callback_data="ZZrw248 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ شبح كانترفيل", callback_data="ZZrw249 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جريمة اللورد سافيل", callback_data="ZZrw250 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بيت الرمان", callback_data="ZZrw251 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtr " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 أوسكار وايلد \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw15 (\\d+)$"))
async def Zrw15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ ظل الريح", callback_data="ZZrw253 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ لعبة الملاك", callback_data="ZZrw254 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سجين السماء", callback_data="ZZrw255 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ متاههة الأرواح", callback_data="ZZrw256 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtr " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 كارلوس زافون \n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat Link List 1
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw14 (\\d+)$"))
async def ZZrw14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/14", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw15 (\\d+)$"))
async def ZZrw15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/15", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw16 (\\d+)$"))
async def ZZrw16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/16", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw17 (\\d+)$"))
async def ZZrw17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/17", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw18 (\\d+)$"))
async def ZZrw18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/18", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw19 (\\d+)$"))
async def ZZrw19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/19", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw20 (\\d+)$"))
async def ZZrw20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/20", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw21 (\\d+)$"))
async def ZZrw21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/21", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw23 (\\d+)$"))
async def ZZrw23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/23", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw24 (\\d+)$"))
async def ZZrw24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/24", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw25 (\\d+)$"))
async def ZZrw25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/25", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw26 (\\d+)$"))
async def ZZrw26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/26", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw27 (\\d+)$"))
async def ZZrw27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/27", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw28 (\\d+)$"))
async def ZZrw28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/28", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw29 (\\d+)$"))
async def ZZrw29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/29", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw30 (\\d+)$"))
async def ZZrw30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/30", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw32 (\\d+)$"))
async def ZZrw32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/32", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw33 (\\d+)$"))
async def ZZrw33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/33", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw34 (\\d+)$"))
async def ZZrw34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/34", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw35 (\\d+)$"))
async def ZZrw35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/35", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw36 (\\d+)$"))
async def ZZrw36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/36", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw37 (\\d+)$"))
async def ZZrw37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/37", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw38 (\\d+)$"))
async def ZZrw38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/38", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw39 (\\d+)$"))
async def ZZrw39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/39", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw40 (\\d+)$"))
async def ZZrw40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/40", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw41 (\\d+)$"))
async def ZZrw41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/41", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw42 (\\d+)$"))
async def ZZrw42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/42", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw44 (\\d+)$"))
async def ZZrw44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/44", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw45 (\\d+)$"))
async def ZZrw45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/45", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw46 (\\d+)$"))
async def ZZrw46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/46", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw47 (\\d+)$"))
async def ZZrw47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/47", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw48 (\\d+)$"))
async def ZZrw48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/48", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw49 (\\d+)$"))
async def ZZrw49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/49", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw50 (\\d+)$"))
async def ZZrw50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/50", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw51 (\\d+)$"))
async def ZZrw51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/51", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw52 (\\d+)$"))
async def ZZrw52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/52", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw53 (\\d+)$"))
async def ZZrw53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/53", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw54 (\\d+)$"))
async def ZZrw54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/54", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw55 (\\d+)$"))
async def ZZrw55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/55", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw56 (\\d+)$"))
async def ZZrw56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/56", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw57 (\\d+)$"))
async def ZZrw57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/57", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw58 (\\d+)$"))
async def ZZrw58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/58", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw59 (\\d+)$"))
async def ZZrw59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/59", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw60 (\\d+)$"))
async def ZZrw60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/60", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw61 (\\d+)$"))
async def ZZrw61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/61", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw62 (\\d+)$"))
async def ZZrw62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/62", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw63 (\\d+)$"))
async def ZZrw63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/63", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw64 (\\d+)$"))
async def ZZrw64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/64", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw65 (\\d+)$"))
async def ZZrw65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/65", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw66 (\\d+)$"))
async def ZZrw66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/66", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw67 (\\d+)$"))
async def ZZrw67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/67", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw68 (\\d+)$"))
async def ZZrw68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/68", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw70 (\\d+)$"))
async def ZZrw70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/70", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw71 (\\d+)$"))
async def ZZrw71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/71", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw72 (\\d+)$"))
async def ZZrw72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/72", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw73 (\\d+)$"))
async def ZZrw73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/73", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw74 (\\d+)$"))
async def ZZrw74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/74", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw75 (\\d+)$"))
async def ZZrw75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/75", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw76 (\\d+)$"))
async def ZZrw76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/76", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw77 (\\d+)$"))
async def ZZrw77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/77", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw78 (\\d+)$"))
async def ZZrw78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/78", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw80 (\\d+)$"))
async def ZZrw80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/80", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw81 (\\d+)$"))
async def ZZrw81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/81", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw82 (\\d+)$"))
async def ZZrw82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/82", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw83 (\\d+)$"))
async def ZZrw83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/83", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw84 (\\d+)$"))
async def ZZrw84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/84", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw85 (\\d+)$"))
async def ZZrw85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/85", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw86 (\\d+)$"))
async def ZZrw86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/86", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw87 (\\d+)$"))
async def ZZrw87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/87", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw88 (\\d+)$"))
async def ZZrw88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/88", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw89 (\\d+)$"))
async def ZZrw89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/89", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw90 (\\d+)$"))
async def ZZrw90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/90", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw91 (\\d+)$"))
async def ZZrw91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/91", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw93 (\\d+)$"))
async def ZZrw93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/93", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw94 (\\d+)$"))
async def ZZrw94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/94", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw95 (\\d+)$"))
async def ZZrw95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/95", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw96 (\\d+)$"))
async def ZZrw96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/96", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw97 (\\d+)$"))
async def ZZrw97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/97", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw98 (\\d+)$"))
async def ZZrw98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/98", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw99 (\\d+)$"))
async def ZZrw99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/99", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw100 (\\d+)$"))
async def ZZrw100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/100", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw101 (\\d+)$"))
async def ZZrw101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/101", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw102 (\\d+)$"))
async def ZZrw102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/102", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw103 (\\d+)$"))
async def ZZrw103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/103", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw104 (\\d+)$"))
async def ZZrw104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/104", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw105 (\\d+)$"))
async def ZZrw105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/105", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw106 (\\d+)$"))
async def ZZrw106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/106", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw107 (\\d+)$"))
async def ZZrw107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/107", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw108 (\\d+)$"))
async def ZZrw108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/108", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw109 (\\d+)$"))
async def ZZrw109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/109", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw110 (\\d+)$"))
async def ZZrw110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/110", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw112 (\\d+)$"))
async def ZZrw112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/112", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw113 (\\d+)$"))
async def ZZrw113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/113", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw114 (\\d+)$"))
async def ZZrw114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/114", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw115 (\\d+)$"))
async def ZZrw115(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/115", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw116 (\\d+)$"))
async def ZZrw116(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/116", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw117 (\\d+)$"))
async def ZZrw117(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/117", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw118 (\\d+)$"))
async def ZZrw118(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/118", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw119 (\\d+)$"))
async def ZZrw119(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/119", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw120 (\\d+)$"))
async def ZZrw120(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/120", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw121 (\\d+)$"))
async def ZZrw121(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/121", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw122 (\\d+)$"))
async def ZZrw122(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/122", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw123 (\\d+)$"))
async def ZZrw123(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/123", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw124 (\\d+)$"))
async def ZZrw124(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/124", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw125 (\\d+)$"))
async def ZZrw125(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/125", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw126 (\\d+)$"))
async def ZZrw126(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/126", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw128 (\\d+)$"))
async def ZZrw128(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/128", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw129 (\\d+)$"))
async def ZZrw129(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/129", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw131 (\\d+)$"))
async def ZZrw131(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/131", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw132 (\\d+)$"))
async def ZZrw132(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/132", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw133 (\\d+)$"))
async def ZZrw133(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/133", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw134 (\\d+)$"))
async def ZZrw134(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/134", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw135 (\\d+)$"))
async def ZZrw135(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/135", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw136 (\\d+)$"))
async def ZZrw136(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/136", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw137 (\\d+)$"))
async def ZZrw137(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/137", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw138 (\\d+)$"))
async def ZZrw138(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/138", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw139 (\\d+)$"))
async def ZZrw139(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/139", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw140 (\\d+)$"))
async def ZZrw140(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/140", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw141 (\\d+)$"))
async def ZZrw141(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/141", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw142 (\\d+)$"))
async def ZZrw142(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/142", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw143 (\\d+)$"))
async def ZZrw143(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/143", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw144 (\\d+)$"))
async def ZZrw144(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/144", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw145 (\\d+)$"))
async def ZZrw145(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/145", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw146 (\\d+)$"))
async def ZZrw146(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/146", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw147 (\\d+)$"))
async def ZZrw147(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/147", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw148 (\\d+)$"))
async def ZZrw148(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/148", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw149 (\\d+)$"))
async def ZZrw149(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/149", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw150 (\\d+)$"))
async def ZZrw150(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/150", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw151 (\\d+)$"))
async def ZZrw151(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/151", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw152 (\\d+)$"))
async def ZZrw152(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/152", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw153 (\\d+)$"))
async def ZZrw153(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/153", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw154 (\\d+)$"))
async def ZZrw154(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/154", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw155 (\\d+)$"))
async def ZZrw155(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/155", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw156 (\\d+)$"))
async def ZZrw156(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/156", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw157 (\\d+)$"))
async def ZZrw157(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/157", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw158 (\\d+)$"))
async def ZZrw158(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/158", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw159 (\\d+)$"))
async def ZZrw159(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/159", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw160 (\\d+)$"))
async def ZZrw160(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/160", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw161 (\\d+)$"))
async def ZZrw161(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/161", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw162 (\\d+)$"))
async def ZZrw162(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/162", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw163 (\\d+)$"))
async def ZZrw163(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/163", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw164 (\\d+)$"))
async def ZZrw164(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/164", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw165 (\\d+)$"))
async def ZZrw165(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/165", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw166 (\\d+)$"))
async def ZZrw166(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/166", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw167 (\\d+)$"))
async def ZZrw167(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/167", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw168 (\\d+)$"))
async def ZZrw168(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/168", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw169 (\\d+)$"))
async def ZZrw169(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/169", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw170 (\\d+)$"))
async def ZZrw170(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/170", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw171 (\\d+)$"))
async def ZZrw171(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/171", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw172 (\\d+)$"))
async def ZZrw172(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/172", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw173 (\\d+)$"))
async def ZZrw173(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/173", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw175 (\\d+)$"))
async def ZZrw175(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/175", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw176 (\\d+)$"))
async def ZZrw176(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/176", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw177 (\\d+)$"))
async def ZZrw177(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/177", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw178 (\\d+)$"))
async def ZZrw178(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/178", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw179 (\\d+)$"))
async def ZZrw179(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/179", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw180 (\\d+)$"))
async def ZZrw180(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/180", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw181 (\\d+)$"))
async def ZZrw181(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/181", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw182 (\\d+)$"))
async def ZZrw182(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/182", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw183 (\\d+)$"))
async def ZZrw183(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/183", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw184 (\\d+)$"))
async def ZZrw184(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/184", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw185 (\\d+)$"))
async def ZZrw185(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/185", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw186 (\\d+)$"))
async def ZZrw186(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/186", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw187 (\\d+)$"))
async def ZZrw187(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/187", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw188 (\\d+)$"))
async def ZZrw188(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/188", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw189 (\\d+)$"))
async def ZZrw189(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/189", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw190 (\\d+)$"))
async def ZZrw190(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/190", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw191 (\\d+)$"))
async def ZZrw191(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/191", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw192 (\\d+)$"))
async def ZZrw192(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/192", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw193 (\\d+)$"))
async def ZZrw193(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/193", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw194 (\\d+)$"))
async def ZZrw194(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/194", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw195 (\\d+)$"))
async def ZZrw195(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/195", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw196 (\\d+)$"))
async def ZZrw196(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/196", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw197 (\\d+)$"))
async def ZZrw197(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/197", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw198 (\\d+)$"))
async def ZZrw198(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/198", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw199 (\\d+)$"))
async def ZZrw199(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/199", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw200 (\\d+)$"))
async def ZZrw200(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/200", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw201 (\\d+)$"))
async def ZZrw201(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/201", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw202 (\\d+)$"))
async def ZZrw202(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/202", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw203 (\\d+)$"))
async def ZZrw203(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/203", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw204 (\\d+)$"))
async def ZZrw204(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/204", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw205 (\\d+)$"))
async def ZZrw205(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/205", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw206 (\\d+)$"))
async def ZZrw206(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/206", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw207 (\\d+)$"))
async def ZZrw207(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/207", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw208 (\\d+)$"))
async def ZZrw208(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/208", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw209 (\\d+)$"))
async def ZZrw209(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/209", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw210 (\\d+)$"))
async def ZZrw210(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/210", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw211 (\\d+)$"))
async def ZZrw211(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/211", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw212 (\\d+)$"))
async def ZZrw212(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/212", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw213 (\\d+)$"))
async def ZZrw213(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/213", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw214 (\\d+)$"))
async def ZZrw214(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/214", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw216 (\\d+)$"))
async def ZZrw216(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/216", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw217 (\\d+)$"))
async def ZZrw217(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/217", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw218 (\\d+)$"))
async def ZZrw218(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/218", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw219 (\\d+)$"))
async def ZZrw219(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/219", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw220 (\\d+)$"))
async def ZZrw220(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/220", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw221 (\\d+)$"))
async def ZZrw221(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/221", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw222 (\\d+)$"))
async def ZZrw222(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/222", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw223 (\\d+)$"))
async def ZZrw223(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/223", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw224 (\\d+)$"))
async def ZZrw224(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/224", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw225 (\\d+)$"))
async def ZZrw225(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/225", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw226 (\\d+)$"))
async def ZZrw226(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/226", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw227 (\\d+)$"))
async def ZZrw227(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/227", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw228 (\\d+)$"))
async def ZZrw228(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/228", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw229 (\\d+)$"))
async def ZZrw229(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/229", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw230 (\\d+)$"))
async def ZZrw230(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/230", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw231 (\\d+)$"))
async def ZZrw231(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/231", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw232 (\\d+)$"))
async def ZZrw232(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/232", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw233 (\\d+)$"))
async def ZZrw233(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/233", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw235 (\\d+)$"))
async def ZZrw235(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/235", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw236 (\\d+)$"))
async def ZZrw236(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/236", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw237 (\\d+)$"))
async def ZZrw237(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/237", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw238 (\\d+)$"))
async def ZZrw238(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/238", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw239 (\\d+)$"))
async def ZZrw239(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/239", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw240 (\\d+)$"))
async def ZZrw240(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/240", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw241 (\\d+)$"))
async def ZZrw241(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/241", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw243 (\\d+)$"))
async def ZZrw243(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/243", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw244 (\\d+)$"))
async def ZZrw244(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/244", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw245 (\\d+)$"))
async def ZZrw245(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/245", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw246 (\\d+)$"))
async def ZZrw246(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/246", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw247 (\\d+)$"))
async def ZZrw247(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/247", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw248 (\\d+)$"))
async def ZZrw248(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/248", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw249 (\\d+)$"))
async def ZZrw249(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/249", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw250 (\\d+)$"))
async def ZZrw250(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/250", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw251 (\\d+)$"))
async def ZZrw251(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/251", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw253 (\\d+)$"))
async def ZZrw253(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/253", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw254 (\\d+)$"))
async def ZZrw254(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/254", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw255 (\\d+)$"))
async def ZZrw255(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/255", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw256 (\\d+)$"))
async def ZZrw256(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/256", reply_to_message_id=mid)


####################################################################################
## rwaiat list 2 (islamic)
####################################################################################

@Client.on_callback_query(filters.regex("^Yrw2 (\\d+)$"))
async def Yrw2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 تفسير القرآن الكريم", callback_data="Zrw16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 كتب الحديث الستة", callback_data="Zrw17 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 علم التجويد", callback_data="Zrw18 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 أحمد ديدات", callback_data="Zrw19 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 محمد متولي الشعراوي", callback_data="Zrw20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚  عائض القرني", callback_data="Zrw21 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 مصطفى حسني", callback_data="Zrw22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 محمد راتب النابلسي", callback_data="Zrw23 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منوعات اسلاميه", callback_data="Zrw24 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى 🔘 | المكتبة الإسلامية | • 🕋 • \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw16 (\\d+)$"))
async def Zrw16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ زبدة التفسير", callback_data="ZZrw261 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الاجماع في التفسير", callback_data="ZZrw262 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مقدمة", callback_data="ZZrw263 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التفسير اللغوي", callback_data="ZZrw264 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير وبيان مفردات", callback_data="ZZrw265 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير السعدي", callback_data="ZZrw266 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير القرآن", callback_data="ZZrw267 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير الشعراوي", callback_data="ZZrw268 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التفسير واعرابه", callback_data="ZZrw269 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ابن كثير", callback_data="ZZrw270 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى مكتبة 📚 تفسير القرآن الكريم \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw17 (\\d+)$"))
async def Zrw17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ البخاري", callback_data="ZZrw272 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مسلم", callback_data="ZZrw273 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أبو داود", callback_data="ZZrw274 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الترمذي", callback_data="ZZrw275 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ النسائي", callback_data="ZZrw276 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ابن ماجه", callback_data="ZZrw277 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 كتب الحديث الستة \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw18 (\\d+)$"))
async def Zrw18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ التيسير التجويد", callback_data="ZZrw279 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أحكام التجويد", callback_data="ZZrw280 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أبحاث  بعلم التجويد", callback_data="ZZrw281 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجامع", callback_data="ZZrw282 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المنهج العملي", callback_data="ZZrw283 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التجويد المبسط 1", callback_data="ZZrw284 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الواضح", callback_data="ZZrw285 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التجويد المبسط 2", callback_data="ZZrw286 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تبسيط التجويد", callback_data="ZZrw287 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الميسر", callback_data="ZZrw288 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الوجيز", callback_data="ZZrw289 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أحكام", callback_data="ZZrw290 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ القول السديد", callback_data="ZZrw291 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجامع", callback_data="ZZrw292 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ القول المفيد", callback_data="ZZrw293 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التجويد المصور 1", callback_data="ZZrw294 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التجويد المصور 2", callback_data="ZZrw295 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ معلم التجويد", callback_data="ZZrw296 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علم التجويد", callback_data="ZZrw297 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التجويد قالون", callback_data="ZZrw298 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التجويد ورش", callback_data="ZZrw299 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التجويد كامل", callback_data="ZZrw300 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التجويد ملون", callback_data="ZZrw301 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التجويد ملون", callback_data="ZZrw302 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المفيد", callback_data="ZZrw303 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التمهيد", callback_data="ZZrw304 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الملخص المفيد", callback_data="ZZrw305 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ غاية المريد", callback_data="ZZrw306 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الواضح 2", callback_data="ZZrw307 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أطلش التجويد", callback_data="ZZrw308 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 علم التجويد \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw19 (\\d+)$"))
async def Zrw19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ حوار", callback_data="ZZrw310 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الله", callback_data="ZZrw311 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ العرب واسرائيل", callback_data="ZZrw312 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العنصريه", callback_data="ZZrw313 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الرسول الاعظم ص", callback_data="ZZrw314 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ماذا يقول الكتاب المقدس عن محمد ص", callback_data="ZZrw315 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هل الكتاب المقدس كتاب الله", callback_data="ZZrw316 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ من دحرج الحجر", callback_data="ZZrw317 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ من المعمدانيه الي الاسلام", callback_data="ZZrw318 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مناظرة العصر", callback_data="ZZrw319 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مسألة صلب المسيح", callback_data="ZZrw320 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اساقفه الكنيسة ؟", callback_data="ZZrw321 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المسيح في الاسلام", callback_data="ZZrw322 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الصلب وهم ام حقيقه ؟", callback_data="ZZrw323 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العبادة", callback_data="ZZrw324 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هل المسيح هو الله ؟", callback_data="ZZrw325 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مناظرتان في استوكهولم", callback_data="ZZrw326 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هل مات المسيح علي الصليب ؟", callback_data="ZZrw327 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ شيطانية الايات", callback_data="ZZrw328 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حوار مع مبشر", callback_data="ZZrw329 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المسلم في الصلاة", callback_data="ZZrw330 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ محمد ص اعظم عظماء العالم", callback_data="ZZrw331 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخلاف الحقيقي بين المسلمين والمسيح", callback_data="ZZrw332 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخمر بين المسيحية والاسلام", callback_data="ZZrw333 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هل القرآن كلام الله ؟", callback_data="ZZrw334 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ خمسون الف خطأ", callback_data="ZZrw335 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ محمد ص الخليفه الطبيعي للمسيح", callback_data="ZZrw336 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ذاكر نائيك - ديدات الأكبر", callback_data="ZZrw337 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 أحمد ديدات\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw20 (\\d+)$"))
async def Zrw20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ تفسير 1", callback_data="ZZrw339 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 2", callback_data="ZZrw340 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 3", callback_data="ZZrw341 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير 4", callback_data="ZZrw342 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 5", callback_data="ZZrw343 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 6", callback_data="ZZrw344 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير 7", callback_data="ZZrw345 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 8", callback_data="ZZrw346 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 9", callback_data="ZZrw347 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير 10", callback_data="ZZrw348 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 11", callback_data="ZZrw349 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 12", callback_data="ZZrw350 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير 13", callback_data="ZZrw351 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 14", callback_data="ZZrw352 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 15", callback_data="ZZrw353 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير 16", callback_data="ZZrw354 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 17", callback_data="ZZrw355 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 18", callback_data="ZZrw356 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تفسير 19", callback_data="ZZrw357 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تفسير 20", callback_data="ZZrw358 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قصص الصحابة", callback_data="ZZrw359 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الظلم والظالمون", callback_data="ZZrw360 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ نهاية العالم", callback_data="ZZrw361 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ خواطر الشعراوي", callback_data="ZZrw362 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الهجرة النبوية", callback_data="ZZrw363 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ فقه المسلمة", callback_data="ZZrw364 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عذاب النار", callback_data="ZZrw365 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ دعاء الأنبياء", callback_data="ZZrw366 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الشيطان والانسان", callback_data="ZZrw367 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ السحر والحسد", callback_data="ZZrw368 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الله والنفس البشرية", callback_data="ZZrw369 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التوبة", callback_data="ZZrw370 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخير والشر", callback_data="ZZrw371 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحياة والموت", callback_data="ZZrw372 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 محمد متولي الشعراوي  \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw21 (\\d+)$"))
async def Zrw21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ وأخيرا اكتشفت السعادة", callback_data="ZZrw374 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دروس المسجد في رمضان", callback_data="ZZrw375 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سياط القلوب", callback_data="ZZrw376 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قصائد قتلتها أصحابها", callback_data="ZZrw377 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أسعد امرأة في العالم", callback_data="ZZrw378 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ابتسم", callback_data="ZZrw379 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ لا تحزن", callback_data="ZZrw380 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚  عائض القرني \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw22 (\\d+)$"))
async def Zrw22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ عيش اللحظة", callback_data="ZZrw382 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خدعوك فقالوا", callback_data="ZZrw383 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ انسان جديد", callback_data="ZZrw384 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الكنز المفقود", callback_data="ZZrw385 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سحر الدنيا", callback_data="ZZrw386 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 مصطفى حسني\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw23 (\\d+)$"))
async def Zrw23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ اسماء الله الحسني", callback_data="ZZrw388 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كتاب الله أكبر", callback_data="ZZrw389 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الاسراء والمعراج", callback_data="ZZrw390 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مدارج السالكين", callback_data="ZZrw391 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تأملات في الأسلام", callback_data="ZZrw392 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المناسبات الدينيه", callback_data="ZZrw393 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ آيات الله في الانسان", callback_data="ZZrw394 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ آيات الله في الأفاق", callback_data="ZZrw395 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ موسوعة الاعجاز العلمي", callback_data="ZZrw396 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علم القلوب", callback_data="ZZrw397 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الهجرة", callback_data="ZZrw398 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رياض الصالحين", callback_data="ZZrw399 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ رجال حول الرسول", callback_data="ZZrw400 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الزواج في ظل الاسلام", callback_data="ZZrw401 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فقه السرة النبوية", callback_data="ZZrw402 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العبادات الشعائرية", callback_data="ZZrw403 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الشباب في الاسلام", callback_data="ZZrw404 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تربية الاولاد في الاسلام", callback_data="ZZrw405 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المرأة المسلمة", callback_data="ZZrw406 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 محمد راتب النابلسي\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw24 (\\d+)$"))
async def Zrw24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ روائع القصص", callback_data="ZZrw408 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ملخص منهاج السنة", callback_data="ZZrw409 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الاجابة القرآنية", callback_data="ZZrw410 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ صحبة الجنه", callback_data="ZZrw411 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التلخيص المصور في اخطاء المصلين", callback_data="ZZrw412 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فاني قريب", callback_data="ZZrw413 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سابغات", callback_data="ZZrw414 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سير أعلام النبلاء", callback_data="ZZrw415 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رجال حول الرسول ص", callback_data="ZZrw416 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخارطة الذهنية للقرآن", callback_data="ZZrw417 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اني رزقت حبها", callback_data="ZZrw418 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سهرة عائلية", callback_data="ZZrw419 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قبسات علمية من القرآن والسنة", callback_data="ZZrw420 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المصحف الموضوعي", callback_data="ZZrw421 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المشوق الي القرآن", callback_data="ZZrw422 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دعاء من الكتاب والسنة", callback_data="ZZrw423 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خطوات نحو الملك جل جلاله", callback_data="ZZrw424 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 المنوعات الاسلاميه\n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat Link List 2
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw261 (\\d+)$"))
async def ZZrw261(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/261", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw262 (\\d+)$"))
async def ZZrw262(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/262", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw263 (\\d+)$"))
async def ZZrw263(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/263", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw264 (\\d+)$"))
async def ZZrw264(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/264", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw265 (\\d+)$"))
async def ZZrw265(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/265", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw266 (\\d+)$"))
async def ZZrw266(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/266", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw267 (\\d+)$"))
async def ZZrw267(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/267", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw268 (\\d+)$"))
async def ZZrw268(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/268", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw269 (\\d+)$"))
async def ZZrw269(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/269", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw270 (\\d+)$"))
async def ZZrw270(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/270", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw272 (\\d+)$"))
async def ZZrw272(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/272", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw273 (\\d+)$"))
async def ZZrw273(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/273", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw274 (\\d+)$"))
async def ZZrw274(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/274", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw275 (\\d+)$"))
async def ZZrw275(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/275", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw276 (\\d+)$"))
async def ZZrw276(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/276", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw277 (\\d+)$"))
async def ZZrw277(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/277", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw279 (\\d+)$"))
async def ZZrw279(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/279", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw280 (\\d+)$"))
async def ZZrw280(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/280", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw281 (\\d+)$"))
async def ZZrw281(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/281", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw282 (\\d+)$"))
async def ZZrw282(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/282", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw283 (\\d+)$"))
async def ZZrw283(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/283", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw284 (\\d+)$"))
async def ZZrw284(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/284", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw285 (\\d+)$"))
async def ZZrw285(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/285", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw286 (\\d+)$"))
async def ZZrw286(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/286", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw287 (\\d+)$"))
async def ZZrw287(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/287", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw288 (\\d+)$"))
async def ZZrw288(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/288", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw289 (\\d+)$"))
async def ZZrw289(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/289", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw290 (\\d+)$"))
async def ZZrw290(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/290", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw291 (\\d+)$"))
async def ZZrw291(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/291", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw292 (\\d+)$"))
async def ZZrw292(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/292", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw293 (\\d+)$"))
async def ZZrw293(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/293", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw294 (\\d+)$"))
async def ZZrw294(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/294", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw295 (\\d+)$"))
async def ZZrw295(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/295", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw296 (\\d+)$"))
async def ZZrw296(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/296", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw297 (\\d+)$"))
async def ZZrw297(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/297", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw298 (\\d+)$"))
async def ZZrw298(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/298", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw299 (\\d+)$"))
async def ZZrw299(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/299", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw300 (\\d+)$"))
async def ZZrw300(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/300", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw301 (\\d+)$"))
async def ZZrw301(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/301", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw302 (\\d+)$"))
async def ZZrw302(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/302", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw303 (\\d+)$"))
async def ZZrw303(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/303", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw304 (\\d+)$"))
async def ZZrw304(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/304", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw305 (\\d+)$"))
async def ZZrw305(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/305", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw306 (\\d+)$"))
async def ZZrw306(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/306", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw307 (\\d+)$"))
async def ZZrw307(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/307", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw308 (\\d+)$"))
async def ZZrw308(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/308", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw310 (\\d+)$"))
async def ZZrw310(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/310", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw311 (\\d+)$"))
async def ZZrw311(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/311", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw312 (\\d+)$"))
async def ZZrw312(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/312", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw313 (\\d+)$"))
async def ZZrw313(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/313", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw314 (\\d+)$"))
async def ZZrw314(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/314", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw315 (\\d+)$"))
async def ZZrw315(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/315", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw316 (\\d+)$"))
async def ZZrw316(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/316", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw317 (\\d+)$"))
async def ZZrw317(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/317", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw318 (\\d+)$"))
async def ZZrw318(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/318", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw319 (\\d+)$"))
async def ZZrw319(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/319", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw320 (\\d+)$"))
async def ZZrw320(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/320", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw321 (\\d+)$"))
async def ZZrw321(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/321", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw322 (\\d+)$"))
async def ZZrw322(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/322", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw323 (\\d+)$"))
async def ZZrw323(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/323", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw324 (\\d+)$"))
async def ZZrw324(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/324", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw325 (\\d+)$"))
async def ZZrw325(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/325", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw326 (\\d+)$"))
async def ZZrw326(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/326", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw327 (\\d+)$"))
async def ZZrw327(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/327", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw328 (\\d+)$"))
async def ZZrw328(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/328", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw329 (\\d+)$"))
async def ZZrw329(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/329", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw330 (\\d+)$"))
async def ZZrw330(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/330", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw331 (\\d+)$"))
async def ZZrw331(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/331", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw332 (\\d+)$"))
async def ZZrw332(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/332", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw333 (\\d+)$"))
async def ZZrw333(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/333", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw334 (\\d+)$"))
async def ZZrw334(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/334", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw335 (\\d+)$"))
async def ZZrw335(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/335", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw336 (\\d+)$"))
async def ZZrw336(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/336", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw337 (\\d+)$"))
async def ZZrw337(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/337", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw339 (\\d+)$"))
async def ZZrw339(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/339", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw340 (\\d+)$"))
async def ZZrw340(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/340", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw341 (\\d+)$"))
async def ZZrw341(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/341", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw342 (\\d+)$"))
async def ZZrw342(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/342", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw343 (\\d+)$"))
async def ZZrw343(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/343", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw344 (\\d+)$"))
async def ZZrw344(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/344", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw345 (\\d+)$"))
async def ZZrw345(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/345", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw346 (\\d+)$"))
async def ZZrw346(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/346", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw347 (\\d+)$"))
async def ZZrw347(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/347", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw348 (\\d+)$"))
async def ZZrw348(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/348", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw349 (\\d+)$"))
async def ZZrw349(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/349", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw350 (\\d+)$"))
async def ZZrw350(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/350", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw351 (\\d+)$"))
async def ZZrw351(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/351", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw352 (\\d+)$"))
async def ZZrw352(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/352", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw353 (\\d+)$"))
async def ZZrw353(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/353", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw354 (\\d+)$"))
async def ZZrw354(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/354", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw355 (\\d+)$"))
async def ZZrw355(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/355", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw356 (\\d+)$"))
async def ZZrw356(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/356", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw357 (\\d+)$"))
async def ZZrw357(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/357", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw358 (\\d+)$"))
async def ZZrw358(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/358", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw359 (\\d+)$"))
async def ZZrw359(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/359", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw360 (\\d+)$"))
async def ZZrw360(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/360", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw361 (\\d+)$"))
async def ZZrw361(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/361", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw362 (\\d+)$"))
async def ZZrw362(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/362", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw363 (\\d+)$"))
async def ZZrw363(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/363", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw364 (\\d+)$"))
async def ZZrw364(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/364", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw365 (\\d+)$"))
async def ZZrw365(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/365", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw366 (\\d+)$"))
async def ZZrw366(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/366", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw367 (\\d+)$"))
async def ZZrw367(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/367", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw368 (\\d+)$"))
async def ZZrw368(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/368", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw369 (\\d+)$"))
async def ZZrw369(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/369", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw370 (\\d+)$"))
async def ZZrw370(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/370", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw371 (\\d+)$"))
async def ZZrw371(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/371", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw372 (\\d+)$"))
async def ZZrw372(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/372", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw374 (\\d+)$"))
async def ZZrw374(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/374", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw375 (\\d+)$"))
async def ZZrw375(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/375", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw376 (\\d+)$"))
async def ZZrw376(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/376", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw377 (\\d+)$"))
async def ZZrw377(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/377", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw378 (\\d+)$"))
async def ZZrw378(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/378", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw379 (\\d+)$"))
async def ZZrw379(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/379", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw380 (\\d+)$"))
async def ZZrw380(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/380", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw382 (\\d+)$"))
async def ZZrw382(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/382", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw383 (\\d+)$"))
async def ZZrw383(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/383", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw384 (\\d+)$"))
async def ZZrw384(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/384", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw385 (\\d+)$"))
async def ZZrw385(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/385", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw386 (\\d+)$"))
async def ZZrw386(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/386", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw388 (\\d+)$"))
async def ZZrw388(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/388", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw389 (\\d+)$"))
async def ZZrw389(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/389", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw390 (\\d+)$"))
async def ZZrw390(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/390", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw391 (\\d+)$"))
async def ZZrw391(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/391", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw392 (\\d+)$"))
async def ZZrw392(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/392", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw393 (\\d+)$"))
async def ZZrw393(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/393", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw394 (\\d+)$"))
async def ZZrw394(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/394", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw395 (\\d+)$"))
async def ZZrw395(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/395", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw396 (\\d+)$"))
async def ZZrw396(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/396", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw397 (\\d+)$"))
async def ZZrw397(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/397", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw398 (\\d+)$"))
async def ZZrw398(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/398", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw399 (\\d+)$"))
async def ZZrw399(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/399", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw400 (\\d+)$"))
async def ZZrw400(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/400", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw401 (\\d+)$"))
async def ZZrw401(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/401", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw402 (\\d+)$"))
async def ZZrw402(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/402", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw403 (\\d+)$"))
async def ZZrw403(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/403", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw404 (\\d+)$"))
async def ZZrw404(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/404", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw405 (\\d+)$"))
async def ZZrw405(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/405", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw406 (\\d+)$"))
async def ZZrw406(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/406", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw408 (\\d+)$"))
async def ZZrw408(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/408", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw409 (\\d+)$"))
async def ZZrw409(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/409", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw410 (\\d+)$"))
async def ZZrw410(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/410", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw411 (\\d+)$"))
async def ZZrw411(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/411", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw412 (\\d+)$"))
async def ZZrw412(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/412", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw413 (\\d+)$"))
async def ZZrw413(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/413", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw414 (\\d+)$"))
async def ZZrw414(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/414", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw415 (\\d+)$"))
async def ZZrw415(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/415", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw416 (\\d+)$"))
async def ZZrw416(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/416", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw417 (\\d+)$"))
async def ZZrw417(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/417", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw418 (\\d+)$"))
async def ZZrw418(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/418", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw419 (\\d+)$"))
async def ZZrw419(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/419", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw420 (\\d+)$"))
async def ZZrw420(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/420", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw421 (\\d+)$"))
async def ZZrw421(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/421", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw422 (\\d+)$"))
async def ZZrw422(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/422", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw423 (\\d+)$"))
async def ZZrw423(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/423", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw424 (\\d+)$"))
async def ZZrw424(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/424", reply_to_message_id=mid)


######################################################################################
## rwaiat List 3
######################################################################################

@Client.on_callback_query(filters.regex("^Yrw3 (\\d+)$"))
async def Yrw3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ 1- | النصوص والخواطر | • 🍿 •", callback_data="rwtxt " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ 2- | كُتاب شعر | • 📘 •", callback_data="rwktb " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 🔘 | الأدب والشعر | • 📜 • \n√", reply_markup=keyboard)
    return


# النصوص والخواطر
@Client.on_callback_query(filters.regex("^rwtxt (\\d+)$"))
async def rwtxt(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 محمد السالم", callback_data="Zrw25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 فهد العودة", callback_data="Zrw26 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 شهرزاد", callback_data="Zrw27 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 منوعات وخواطر", callback_data="Zrw28 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 الأدب الساخر", callback_data="Zrw29 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات | النصوص والخواطر | • 🍿 •\n√", reply_markup=keyboard)
    return


# الكتب والشعر
@Client.on_callback_query(filters.regex("^rwktb (\\d+)$"))
async def rwktb(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 جبران خليل جبران", callback_data="Zrw30 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 نجيب محفوظ", callback_data="Zrw31 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 طه حسين", callback_data="Zrw32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 نزار قباني", callback_data="Zrw33 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منوعات الأدب والشعر", callback_data="Zrw34 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة | كُتاب شعر | • 📘 •\n√", reply_markup=keyboard)
    return


# يداية النصوص والخواطر
@Client.on_callback_query(filters.regex("^Zrw25 (\\d+)$"))
async def Zrw25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ مرحبا يا سكر", callback_data="ZZrw431 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حبيبتي بكماء", callback_data="ZZrw432 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجليل والصلعوك", callback_data="ZZrw433 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كلك الليلة في صدري", callback_data="ZZrw434 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أحبك وكفي", callback_data="ZZrw435 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ سلام الله علي عينيك", callback_data="ZZrw436 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ شغفها حبا", callback_data="ZZrw437 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtxt " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 محمد السالم\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw26 (\\d+)$"))
async def Zrw26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ مدينة لا تنام", callback_data="ZZrw439 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ما معني ان تكون وحيدا", callback_data="ZZrw440 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حب في زمن الجاهلية", callback_data="ZZrw441 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اخاف عليك", callback_data="ZZrw442 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قل وداعا", callback_data="ZZrw443 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtxt " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات ا📚 فهد العودة\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw27 (\\d+)$"))
async def Zrw27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ ع حيطان الجيران", callback_data="ZZrw452 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الذين احببناهم ولم", callback_data="ZZrw453 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعال أعيشك", callback_data="ZZrw454 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أنثي الكتب", callback_data="ZZrw455 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ظننته حبا", callback_data="ZZrw456 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtxt " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 شهرزاد\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw28 (\\d+)$"))
async def Zrw28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ تمهل أيها الفأس ان نصفك شجرة", callback_data="ZZrw464 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ في عقيدة الحب كلنا يهود", callback_data="ZZrw465 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ كن لنفسك كل شئ", callback_data="ZZrw466 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عذرا اذا انقطع الكلام", callback_data="ZZrw467 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ كاردل", callback_data="ZZrw468 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ شغف", callback_data="ZZrw469 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ وجع غافي", callback_data="ZZrw470 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ خواطر للحياة", callback_data="ZZrw471 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ليتها تقرأ", callback_data="ZZrw472 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ عن أشياء تؤلمك", callback_data="ZZrw473 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtxt " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 منوعات نصوص وخواطر\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw29 (\\d+)$"))
async def Zrw29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ بالطو وفانله وتاب", callback_data="ZZrw475 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رحلتي من الطب الي سو", callback_data="ZZrw476 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اعترافات جامدة جدا", callback_data="ZZrw477 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مسكين عالم الذكور", callback_data="ZZrw478 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فوق بلاد السواد", callback_data="ZZrw479 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الورقة ج1", callback_data="ZZrw480 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التجربة الفكرية لروح امه", callback_data="ZZrw481 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الورقة ج2", callback_data="ZZrw482 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حرف ..", callback_data="ZZrw484 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ موسوعة النكت والطرائف", callback_data="ZZrw483 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أخبار الحمقي والمغفلين", callback_data="ZZrw485 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwtxt " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 الأدب الساخر\n√", reply_markup=keyboard)
    return


# بداية الكتب والشعر
@Client.on_callback_query(filters.regex("^Zrw30 (\\d+)$"))
async def Zrw30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ المؤلفات العربية", callback_data="ZZrw488 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ديوان", callback_data="ZZrw489 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دمعة وابتسامة", callback_data="ZZrw490 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الأجنجة المكسورة", callback_data="ZZrw491 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أوراق عربية", callback_data="ZZrw492 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الموسيقي", callback_data="ZZrw493 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ نصوص خارج المجموعة", callback_data="ZZrw494 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ البدائع والطرائف", callback_data="ZZrw495 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رمل وزبد", callback_data="ZZrw496 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العواصف", callback_data="ZZrw497 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المجنون", callback_data="ZZrw498 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الشعلة الزرقاء", callback_data="ZZrw499 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwktb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 جبران خليل جبران\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw31 (\\d+)$"))
async def Zrw31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ أولاد حارتنا", callback_data="ZZrw501 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مصر القديمة", callback_data="ZZrw502 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ السكرية", callback_data="ZZrw503 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قصر الشوق", callback_data="ZZrw504 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بين القصرين", callback_data="ZZrw505 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أحلام فترة التفاهة", callback_data="ZZrw506 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فتوة العطوف", callback_data="ZZrw507 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أحلام فترة النقاهة", callback_data="ZZrw508 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المسرحيات", callback_data="ZZrw509 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ القرار الاخير", callback_data="ZZrw510 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ صدي النسيان", callback_data="ZZrw511 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أصداء السيرة الذاتية", callback_data="ZZrw512 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الفجر الكاذب", callback_data="ZZrw513 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قشتمر", callback_data="ZZrw514 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ صباح الورد", callback_data="ZZrw515 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ حديث الصباح والمساء", callback_data="ZZrw516 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أفراح القبة", callback_data="ZZrw517 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ يوم قتل الزعيم", callback_data="ZZrw518 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أمام العرش", callback_data="ZZrw519 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ رأيت فيما يري النائم", callback_data="ZZrw520 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رحلة ابن فطومة", callback_data="ZZrw521 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العائش في الحقيقة", callback_data="ZZrw522 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الشيطان يعظ", callback_data="ZZrw523 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التنظيم السري", callback_data="ZZrw524 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عصر الحب", callback_data="ZZrw525 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قلب الليل", callback_data="ZZrw526 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الكرنك", callback_data="ZZrw527 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجريمة", callback_data="ZZrw528 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حضرة المحترم", callback_data="ZZrw529 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ليالي ألف ليلة", callback_data="ZZrw530 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحب تحت المطر", callback_data="ZZrw531 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحب فوق هضمة الهرم", callback_data="ZZrw532 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المرايا رواية", callback_data="ZZrw533 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ شهر العسل", callback_data="ZZrw534 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الباقي من الزمن ساعة", callback_data="ZZrw535 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حكاية بلا بداية ولا نهاية", callback_data="ZZrw536 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تحت المظلة", callback_data="ZZrw537 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ميرامار", callback_data="ZZrw538 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خمارة القط الأسود", callback_data="ZZrw539 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwktb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 نجيب محفوظ\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw32 (\\d+)$"))
async def Zrw32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ جنة الشوك", callback_data="ZZrw563 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الأوراق المجهولة", callback_data="ZZrw564 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فصول في الأدب والنقد", callback_data="ZZrw565 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ معك سوزان", callback_data="ZZrw566 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الأيام", callback_data="ZZrw567 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ دعاء الكروان", callback_data="ZZrw568 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ نفوس للبيع", callback_data="ZZrw569 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ شجرة البؤس", callback_data="ZZrw570 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الوان", callback_data="ZZrw571 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ المعذبون في الارض", callback_data="ZZrw572 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الفتنة الكبري", callback_data="ZZrw573 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مع المتبني", callback_data="ZZrw574 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الكتابات الاولي", callback_data="ZZrw575 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ محاكمة فكر", callback_data="ZZrw576 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أحاديث", callback_data="ZZrw577 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قادة الفكر", callback_data="ZZrw578 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ في الشعر الجاهلي", callback_data="ZZrw579 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أديب", callback_data="ZZrw580 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مرآه الاسلام", callback_data="ZZrw581 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الشيخان", callback_data="ZZrw582 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحب الضائع", callback_data="ZZrw583 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwktb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 طه حسين\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw33 (\\d+)$"))
async def Zrw33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ ديوان قصائد", callback_data="ZZrw585 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ديوان الرسم بالكلمات", callback_data="ZZrw586 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ديوان طفولة نهد", callback_data="ZZrw587 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الكتابة عمل انقلابي", callback_data="ZZrw588 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سندريلا والسندباد", callback_data="ZZrw589 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بعنوان لا", callback_data="ZZrw590 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الي بيروت مع حبي", callback_data="ZZrw591 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ انا رجل واحد وانت قبيلة من النساء", callback_data="ZZrw592 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أنت لي", callback_data="ZZrw593 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قالت لي السمراء", callback_data="ZZrw594 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مائة رسالة حب", callback_data="ZZrw595 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ابجدية الياسمين", callback_data="ZZrw596 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ احلي قصائدي", callback_data="ZZrw597 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwktb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة روايات 📚 نزار قباني\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw34 (\\d+)$"))
async def Zrw34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ عناية وشرح حمدو", callback_data="ZZrw599 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تحقيق عبدالرحمن", callback_data="ZZrw600 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تحقيق", callback_data="ZZrw601 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ديوان بن ابي طالب", callback_data="ZZrw602 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ديوان الشافعي", callback_data="ZZrw603 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ديوان المتبني", callback_data="ZZrw604 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ديوان ابو القاسم", callback_data="ZZrw605 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ديوان هشام الجخ", callback_data="ZZrw606 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اوراق العشب", callback_data="ZZrw607 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قصيدة حب", callback_data="ZZrw608 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سماء وأرض", callback_data="ZZrw609 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ متعة الحديث 2", callback_data="ZZrw610 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خزانة الكتب الجميلة", callback_data="ZZrw611 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ كبرياء جريح", callback_data="ZZrw612 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ كيف كانو يكتبون", callback_data="ZZrw613 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ متعة الحديث", callback_data="ZZrw614 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwktb " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 منوعات الأدب والشعر\n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat Link List 3
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw431 (\\d+)$"))
async def ZZrw431(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/431", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw432 (\\d+)$"))
async def ZZrw432(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/432", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw433 (\\d+)$"))
async def ZZrw433(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/433", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw434 (\\d+)$"))
async def ZZrw434(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/434", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw435 (\\d+)$"))
async def ZZrw435(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/435", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw436 (\\d+)$"))
async def ZZrw436(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/436", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw437 (\\d+)$"))
async def ZZrw437(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/437", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw439 (\\d+)$"))
async def ZZrw439(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/439", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw440 (\\d+)$"))
async def ZZrw440(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/440", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw441 (\\d+)$"))
async def ZZrw441(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/441", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw442 (\\d+)$"))
async def ZZrw442(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/442", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw443 (\\d+)$"))
async def ZZrw443(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/443", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw452 (\\d+)$"))
async def ZZrw452(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/452", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw453 (\\d+)$"))
async def ZZrw453(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/453", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw454 (\\d+)$"))
async def ZZrw454(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/454", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw455 (\\d+)$"))
async def ZZrw455(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/455", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw456 (\\d+)$"))
async def ZZrw456(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/456", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw464 (\\d+)$"))
async def ZZrw464(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/464", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw465 (\\d+)$"))
async def ZZrw465(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/465", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw466 (\\d+)$"))
async def ZZrw466(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/466", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw467 (\\d+)$"))
async def ZZrw467(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/467", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw468 (\\d+)$"))
async def ZZrw468(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/468", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw469 (\\d+)$"))
async def ZZrw469(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/469", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw470 (\\d+)$"))
async def ZZrw470(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/470", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw471 (\\d+)$"))
async def ZZrw471(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/471", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw472 (\\d+)$"))
async def ZZrw472(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/472", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw473 (\\d+)$"))
async def ZZrw473(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/473", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw475 (\\d+)$"))
async def ZZrw475(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/475", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw476 (\\d+)$"))
async def ZZrw476(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/476", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw477 (\\d+)$"))
async def ZZrw477(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/477", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw478 (\\d+)$"))
async def ZZrw478(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/478", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw479 (\\d+)$"))
async def ZZrw479(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/479", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw480 (\\d+)$"))
async def ZZrw480(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/480", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw481 (\\d+)$"))
async def ZZrw481(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/481", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw482 (\\d+)$"))
async def ZZrw482(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/482", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw483 (\\d+)$"))
async def ZZrw483(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/483", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw484 (\\d+)$"))
async def ZZrw484(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/484", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw485 (\\d+)$"))
async def ZZrw485(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/485", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw488 (\\d+)$"))
async def ZZrw488(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/488", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw489 (\\d+)$"))
async def ZZrw489(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/489", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw490 (\\d+)$"))
async def ZZrw490(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/490", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw491 (\\d+)$"))
async def ZZrw491(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/491", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw492 (\\d+)$"))
async def ZZrw492(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/492", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw493 (\\d+)$"))
async def ZZrw493(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/493", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw494 (\\d+)$"))
async def ZZrw494(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/494", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw495 (\\d+)$"))
async def ZZrw495(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/495", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw496 (\\d+)$"))
async def ZZrw496(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/496", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw497 (\\d+)$"))
async def ZZrw497(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/497", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw498 (\\d+)$"))
async def ZZrw498(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/498", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw499 (\\d+)$"))
async def ZZrw499(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/499", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw501 (\\d+)$"))
async def ZZrw501(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/501", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw502 (\\d+)$"))
async def ZZrw502(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/502", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw503 (\\d+)$"))
async def ZZrw503(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/503", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw504 (\\d+)$"))
async def ZZrw504(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/504", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw505 (\\d+)$"))
async def ZZrw505(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/505", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw506 (\\d+)$"))
async def ZZrw506(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/506", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw507 (\\d+)$"))
async def ZZrw507(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/507", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw508 (\\d+)$"))
async def ZZrw508(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/508", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw509 (\\d+)$"))
async def ZZrw509(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/509", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw510 (\\d+)$"))
async def ZZrw510(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/510", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw511 (\\d+)$"))
async def ZZrw511(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/511", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw512 (\\d+)$"))
async def ZZrw512(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/512", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw513 (\\d+)$"))
async def ZZrw513(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/513", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw514 (\\d+)$"))
async def ZZrw514(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/514", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw515 (\\d+)$"))
async def ZZrw515(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/515", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw516 (\\d+)$"))
async def ZZrw516(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/516", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw517 (\\d+)$"))
async def ZZrw517(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/517", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw518 (\\d+)$"))
async def ZZrw518(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/518", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw519 (\\d+)$"))
async def ZZrw519(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/519", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw520 (\\d+)$"))
async def ZZrw520(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/520", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw521 (\\d+)$"))
async def ZZrw521(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/521", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw522 (\\d+)$"))
async def ZZrw522(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/522", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw523 (\\d+)$"))
async def ZZrw523(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/523", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw524 (\\d+)$"))
async def ZZrw524(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/524", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw525 (\\d+)$"))
async def ZZrw525(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/525", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw526 (\\d+)$"))
async def ZZrw526(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/526", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw527 (\\d+)$"))
async def ZZrw527(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/527", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw528 (\\d+)$"))
async def ZZrw528(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/528", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw529 (\\d+)$"))
async def ZZrw529(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/529", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw530 (\\d+)$"))
async def ZZrw530(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/530", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw531 (\\d+)$"))
async def ZZrw531(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/531", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw532 (\\d+)$"))
async def ZZrw532(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/532", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw533 (\\d+)$"))
async def ZZrw533(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/533", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw534 (\\d+)$"))
async def ZZrw534(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/534", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw535 (\\d+)$"))
async def ZZrw535(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/535", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw536 (\\d+)$"))
async def ZZrw536(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/536", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw537 (\\d+)$"))
async def ZZrw537(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/537", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw538 (\\d+)$"))
async def ZZrw538(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/538", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw539 (\\d+)$"))
async def ZZrw539(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/539", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw563 (\\d+)$"))
async def ZZrw563(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/563", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw564 (\\d+)$"))
async def ZZrw564(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/564", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw565 (\\d+)$"))
async def ZZrw565(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/565", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw566 (\\d+)$"))
async def ZZrw566(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/566", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw567 (\\d+)$"))
async def ZZrw567(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/567", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw568 (\\d+)$"))
async def ZZrw568(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/568", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw569 (\\d+)$"))
async def ZZrw569(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/569", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw570 (\\d+)$"))
async def ZZrw570(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/570", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw571 (\\d+)$"))
async def ZZrw571(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/571", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw572 (\\d+)$"))
async def ZZrw572(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/572", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw573 (\\d+)$"))
async def ZZrw573(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/573", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw574 (\\d+)$"))
async def ZZrw574(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/574", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw575 (\\d+)$"))
async def ZZrw575(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/575", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw576 (\\d+)$"))
async def ZZrw576(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/576", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw577 (\\d+)$"))
async def ZZrw577(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/577", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw578 (\\d+)$"))
async def ZZrw578(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/578", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw579 (\\d+)$"))
async def ZZrw579(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/579", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw580 (\\d+)$"))
async def ZZrw580(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/580", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw581 (\\d+)$"))
async def ZZrw581(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/581", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw582 (\\d+)$"))
async def ZZrw582(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/582", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw583 (\\d+)$"))
async def ZZrw583(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/583", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw584 (\\d+)$"))
async def ZZrw584(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/584", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw585 (\\d+)$"))
async def ZZrw585(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/585", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw586 (\\d+)$"))
async def ZZrw586(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/586", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw587 (\\d+)$"))
async def ZZrw587(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/587", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw588 (\\d+)$"))
async def ZZrw588(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/588", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw589 (\\d+)$"))
async def ZZrw589(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/589", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw590 (\\d+)$"))
async def ZZrw590(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/590", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw591 (\\d+)$"))
async def ZZrw591(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/591", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw592 (\\d+)$"))
async def ZZrw592(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/592", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw593 (\\d+)$"))
async def ZZrw593(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/593", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw594 (\\d+)$"))
async def ZZrw594(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/594", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw595 (\\d+)$"))
async def ZZrw595(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/595", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw596 (\\d+)$"))
async def ZZrw596(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/596", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw597 (\\d+)$"))
async def ZZrw597(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/597", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw599 (\\d+)$"))
async def ZZrw599(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/599", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw600 (\\d+)$"))
async def ZZrw600(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/600", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw601 (\\d+)$"))
async def ZZrw601(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/601", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw602 (\\d+)$"))
async def ZZrw602(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/602", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw603 (\\d+)$"))
async def ZZrw603(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/603", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw604 (\\d+)$"))
async def ZZrw604(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/604", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw605 (\\d+)$"))
async def ZZrw605(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/605", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw606 (\\d+)$"))
async def ZZrw606(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/606", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw607 (\\d+)$"))
async def ZZrw607(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/607", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw608 (\\d+)$"))
async def ZZrw608(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/608", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw609 (\\d+)$"))
async def ZZrw609(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/609", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw610 (\\d+)$"))
async def ZZrw610(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/610", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw611 (\\d+)$"))
async def ZZrw611(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/611", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw612 (\\d+)$"))
async def ZZrw612(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/612", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw613 (\\d+)$"))
async def ZZrw613(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/613", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw614 (\\d+)$"))
async def ZZrw614(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/614", reply_to_message_id=mid)


######################################################################################
## rwaiat List Orw3
######################################################################################

@Client.on_callback_query(filters.regex("^Orw3 (\\d+)$"))
async def Orw3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 الموسوعة الحاسوبية", callback_data="OOrw1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 تطوير مواقع الويب", callback_data="OOrw2 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 شبكات الحاسوب", callback_data="OOrw3 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 أمن المعلومات", callback_data="OOrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 قواعد البيانات", callback_data="OOrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 تطبيقات قواعد البيانات", callback_data="OOrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 أساسيات البرمجة", callback_data="OOrw7 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منوعات التقنية والبرمجة", callback_data="OOrw8 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 🔘 | التقنية والبرمجة | • 💻 •\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw1 (\\d+)$"))
async def OOrw1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الجزء الاول", callback_data="ZZrw618 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء الثاني", callback_data="ZZrw619 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء الثالث", callback_data="ZZrw620 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء الرابع", callback_data="ZZrw621 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء الخامس", callback_data="ZZrw622 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 الموسوعة الحاسوبية\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw2 (\\d+)$"))
async def OOrw2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ HTML5 Code", callback_data="ZZrw624 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Mestring HTML5 & CSS3", callback_data="ZZrw625 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ HTML & CSS", callback_data="ZZrw626 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Advanced HTML5 & CSS3", callback_data="ZZrw627 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ HTML5 & CSS3", callback_data="ZZrw628 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ HTML من البداية", callback_data="ZZrw629 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ BOOTSTRAP 1", callback_data="ZZrw630 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ BOOTSTRAP 2", callback_data="ZZrw631 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ BOOTSTRAP 3", callback_data="ZZrw632 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 تطوير مواقع الويب\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw3 (\\d+)$"))
async def OOrw3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ من البداية للاحتراف", callback_data="ZZrw634 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ اساسيات الكمبيوتر", callback_data="ZZrw635 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اساسيات الشبكات", callback_data="ZZrw636 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ برمجة الشبكات", callback_data="ZZrw637 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بروتوكولات الشبكة", callback_data="ZZrw638 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بروتوكولات برمجة الشبكة", callback_data="ZZrw639 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بروتوكولات الشبكة اللاسلكيه", callback_data="ZZrw640 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الف سؤال وجواب", callback_data="ZZrw641 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ Computer Networks 1", callback_data="ZZrw642 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ البروتوكولات عربي", callback_data="ZZrw643 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ Computer Networks 2", callback_data="ZZrw644 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 شبكات الحاسوب\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw4 (\\d+)$"))
async def OOrw4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ تقنيات التشفير", callback_data="ZZrw646 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تشفير الملفات", callback_data="ZZrw647 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ امن الشبكات 1", callback_data="ZZrw648 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ امن الشبكات 2", callback_data="ZZrw652 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ امن الشبكات اللاسلكية 1", callback_data="ZZrw649 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ امن المعلومات", callback_data="ZZrw650 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ امن الشبكات اللاسلكية 2", callback_data="ZZrw651 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دليل حماية قواعد البيانات", callback_data="ZZrw653 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 أمن المعلومات\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw5 (\\d+)$"))
async def OOrw5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ قواعد بيانات 1", callback_data="ZZrw655 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قواعد بيانات 2", callback_data="ZZrw656 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قواعد بيانات 3", callback_data="ZZrw657 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ DBMS 1", callback_data="ZZrw658 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ DBMS 2", callback_data="ZZrw659 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ DBMS 3", callback_data="ZZrw660 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 قواعد البيانات\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw6 (\\d+)$"))
async def OOrw6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ PL-SQL 1", callback_data="ZZrw662 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ PL-SQL 2", callback_data="ZZrw663 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ PL-SQL 3", callback_data="ZZrw664 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ PL-SQL 4", callback_data="ZZrw665 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 تطبيقات قواعد البيانات\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw7 (\\d+)$"))
async def OOrw7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ واجهات جافا", callback_data="ZZrw667 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ OOP 1", callback_data="ZZrw668 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ OOP 2", callback_data="ZZrw669 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ OOP 3", callback_data="ZZrw671 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اساسيات البرمجه", callback_data="ZZrw670 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اساسيات البرمجة جافا", callback_data="ZZrw672 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ أسرع طرق للتعلم", callback_data="ZZrw673 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 أساسيات البرمجة\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^OOrw8 (\\d+)$"))
async def OOrw8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ اختصارات الكيبورد 1", callback_data="ZZrw675 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اختصارات الكيبورد 2", callback_data="ZZrw676 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم EXEL", callback_data="ZZrw677 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم Power Point", callback_data="ZZrw678 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم Word", callback_data="ZZrw679 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الذكاء الاصطناعي", callback_data="ZZrw680 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ شبكات الحاسب", callback_data="ZZrw681 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دوائر الكترونية", callback_data="ZZrw682 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم C#", callback_data="ZZrw683 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Orw3 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 منوعات التقنية والبرمجة\n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat List Orw3
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw618 (\\d+)$"))
async def ZZrw618(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/618", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw619 (\\d+)$"))
async def ZZrw619(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/619", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw620 (\\d+)$"))
async def ZZrw620(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/620", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw621 (\\d+)$"))
async def ZZrw621(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/621", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw622 (\\d+)$"))
async def ZZrw622(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/622", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw624 (\\d+)$"))
async def ZZrw624(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/624", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw625 (\\d+)$"))
async def ZZrw625(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/625", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw626 (\\d+)$"))
async def ZZrw626(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/626", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw627 (\\d+)$"))
async def ZZrw627(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/627", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw628 (\\d+)$"))
async def ZZrw628(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/628", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw629 (\\d+)$"))
async def ZZrw629(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/629", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw630 (\\d+)$"))
async def ZZrw630(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/630", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw631 (\\d+)$"))
async def ZZrw631(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/631", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw632 (\\d+)$"))
async def ZZrw632(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/632", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw634 (\\d+)$"))
async def ZZrw634(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/634", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw635 (\\d+)$"))
async def ZZrw635(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/635", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw636 (\\d+)$"))
async def ZZrw636(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/636", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw637 (\\d+)$"))
async def ZZrw637(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/637", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw638 (\\d+)$"))
async def ZZrw638(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/638", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw639 (\\d+)$"))
async def ZZrw639(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/639", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw640 (\\d+)$"))
async def ZZrw640(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/640", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw641 (\\d+)$"))
async def ZZrw641(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/641", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw642 (\\d+)$"))
async def ZZrw642(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/642", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw643 (\\d+)$"))
async def ZZrw643(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/643", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw644 (\\d+)$"))
async def ZZrw644(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/644", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw646 (\\d+)$"))
async def ZZrw646(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/646", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw647 (\\d+)$"))
async def ZZrw647(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/647", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw648 (\\d+)$"))
async def ZZrw648(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/648", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw649 (\\d+)$"))
async def ZZrw649(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/649", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw650 (\\d+)$"))
async def ZZrw650(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/650", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw651 (\\d+)$"))
async def ZZrw651(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/651", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw652 (\\d+)$"))
async def ZZrw652(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/652", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw653 (\\d+)$"))
async def ZZrw653(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/653", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw655 (\\d+)$"))
async def ZZrw655(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/655", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw656 (\\d+)$"))
async def ZZrw656(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/656", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw657 (\\d+)$"))
async def ZZrw657(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/657", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw658 (\\d+)$"))
async def ZZrw658(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/658", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw659 (\\d+)$"))
async def ZZrw659(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/659", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw660 (\\d+)$"))
async def ZZrw660(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/660", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw662 (\\d+)$"))
async def ZZrw662(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/662", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw663 (\\d+)$"))
async def ZZrw663(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/663", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw664 (\\d+)$"))
async def ZZrw664(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/664", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw665 (\\d+)$"))
async def ZZrw665(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/665", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw667 (\\d+)$"))
async def ZZrw667(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/667", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw668 (\\d+)$"))
async def ZZrw668(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/668", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw669 (\\d+)$"))
async def ZZrw669(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/669", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw670 (\\d+)$"))
async def ZZrw670(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/670", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw671 (\\d+)$"))
async def ZZrw671(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/671", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw672 (\\d+)$"))
async def ZZrw672(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/672", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw673 (\\d+)$"))
async def ZZrw673(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/673", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw675 (\\d+)$"))
async def ZZrw675(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/675", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw676 (\\d+)$"))
async def ZZrw676(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/676", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw677 (\\d+)$"))
async def ZZrw677(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/677", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw678 (\\d+)$"))
async def ZZrw678(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/678", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw679 (\\d+)$"))
async def ZZrw679(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/679", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw680 (\\d+)$"))
async def ZZrw680(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/680", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw681 (\\d+)$"))
async def ZZrw681(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/681", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw682 (\\d+)$"))
async def ZZrw682(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/682", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw683 (\\d+)$"))
async def ZZrw683(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/683", reply_to_message_id=mid)


######################################################################################
## rwaiat List 4
######################################################################################

@Client.on_callback_query(filters.regex("^Yrw4 (\\d+)$"))
async def Yrw4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 سيجموند فرويد", callback_data="Zrw35 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 علي الوردي", callback_data="Zrw36 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 د. محمد طه", callback_data="Zrw37 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منوعات علم النفس", callback_data="Zrw38 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 🔘 | علم النفس والمجتمع | • 👥 •\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw35 (\\d+)$"))
async def Zrw35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ التحليل النفسي 1", callback_data="ZZrw687 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ التحليل النفسي 2", callback_data="ZZrw688 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التحليل النفسي للاطفال", callback_data="ZZrw689 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التحليل النفسي للعصاب", callback_data="ZZrw690 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الحلم وتأويلة", callback_data="ZZrw691 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحب والحرب", callback_data="ZZrw692 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ افكار لأزمنة الحرب", callback_data="ZZrw693 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الموجز ف التحليل", callback_data="ZZrw694 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حياتي والتحليل النفسي", callback_data="ZZrw695 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علم نفس الجماهير", callback_data="ZZrw696 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ في التحليل النفسي", callback_data="ZZrw697 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التحليل النفسي للهستيريا", callback_data="ZZrw698 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فكر فرويد", callback_data="ZZrw699 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مستقبل وهم", callback_data="ZZrw700 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الأنا والهو", callback_data="ZZrw701 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 سيجموند فرويد\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw36 (\\d+)$"))
async def Zrw36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ مهزلة العقل البشري", callback_data="ZZrw703 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هكذا قتلوا قرة العين", callback_data="ZZrw704 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ خوارق اللاشعور", callback_data="ZZrw705 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ في الطبيعة البشرية", callback_data="ZZrw706 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اسطورة الادب الرفيع", callback_data="ZZrw707 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ من وحي الثمانين", callback_data="ZZrw708 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ منطق ابن خلدون", callback_data="ZZrw709 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الاخلاق", callback_data="ZZrw710 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الفرد العراقي", callback_data="ZZrw711 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ في النفس والمجتمع", callback_data="ZZrw712 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ وعاظ السلاطين", callback_data="ZZrw713 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الاحلام بين العلم والعقيدة", callback_data="ZZrw714 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دراسة في طبيعة المجتمع", callback_data="ZZrw715 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 علي الوردي \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw37 (\\d+)$"))
async def Zrw37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ علاقات خطرة", callback_data="ZZrw717 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخروج عن النص", callback_data="ZZrw718 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ لأ بطعم الفلامنكو", callback_data="ZZrw719 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 د. محمد طه \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw38 (\\d+)$"))
async def Zrw38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ علم النفس وكيف يمكن ان يساعدك", callback_data="ZZrw721 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اهم 50 كتابا في علم النفس", callback_data="ZZrw722 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اسس علم النفس العام", callback_data="ZZrw723 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علم النفس واهميتة", callback_data="ZZrw724 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اشهر 50 خرافة في علم النفس", callback_data="ZZrw725 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ رحلة ف علم النفس", callback_data="ZZrw726 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحاسة السادسة", callback_data="ZZrw727 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علم النفس الارشادي", callback_data="ZZrw728 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أدباء منحرون", callback_data="ZZrw729 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التكرار مغامرة", callback_data="ZZrw730 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ علم النفس الفزيولوجي", callback_data="ZZrw731 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الصداقة", callback_data="ZZrw732 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ يوميات طبيب نفساني", callback_data="ZZrw733 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الهشاشة النفسية", callback_data="ZZrw734 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الطب النفسي", callback_data="ZZrw735 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ وطرائق علم النفس", callback_data="ZZrw736 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw4 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 منوعات علم النفس \n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat Link List 4
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw687 (\\d+)$"))
async def ZZrw687(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/687", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw688 (\\d+)$"))
async def ZZrw688(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/688", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw689 (\\d+)$"))
async def ZZrw689(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/689", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw690 (\\d+)$"))
async def ZZrw690(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/690", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw691 (\\d+)$"))
async def ZZrw691(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/691", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw692 (\\d+)$"))
async def ZZrw692(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/692", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw693 (\\d+)$"))
async def ZZrw693(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/693", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw694 (\\d+)$"))
async def ZZrw694(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/694", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw695 (\\d+)$"))
async def ZZrw695(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/695", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw696 (\\d+)$"))
async def ZZrw696(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/696", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw697 (\\d+)$"))
async def ZZrw697(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/697", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw698 (\\d+)$"))
async def ZZrw698(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/698", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw699 (\\d+)$"))
async def ZZrw699(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/699", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw700 (\\d+)$"))
async def ZZrw700(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/700", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw701 (\\d+)$"))
async def ZZrw701(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/701", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw703 (\\d+)$"))
async def ZZrw703(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/703", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw704 (\\d+)$"))
async def ZZrw704(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/704", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw705 (\\d+)$"))
async def ZZrw705(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/705", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw706 (\\d+)$"))
async def ZZrw706(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/706", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw707 (\\d+)$"))
async def ZZrw707(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/707", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw708 (\\d+)$"))
async def ZZrw708(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/708", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw709 (\\d+)$"))
async def ZZrw709(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/709", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw710 (\\d+)$"))
async def ZZrw710(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/710", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw711 (\\d+)$"))
async def ZZrw711(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/711", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw712 (\\d+)$"))
async def ZZrw712(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/712", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw713 (\\d+)$"))
async def ZZrw713(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/713", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw714 (\\d+)$"))
async def ZZrw714(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/714", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw715 (\\d+)$"))
async def ZZrw715(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/715", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw717 (\\d+)$"))
async def ZZrw717(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/717", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw718 (\\d+)$"))
async def ZZrw718(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/718", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw719 (\\d+)$"))
async def ZZrw719(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/719", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw721 (\\d+)$"))
async def ZZrw721(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/721", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw722 (\\d+)$"))
async def ZZrw722(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/722", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw723 (\\d+)$"))
async def ZZrw723(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/723", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw724 (\\d+)$"))
async def ZZrw724(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/724", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw725 (\\d+)$"))
async def ZZrw725(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/725", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw726 (\\d+)$"))
async def ZZrw726(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/726", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw727 (\\d+)$"))
async def ZZrw727(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/727", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw728 (\\d+)$"))
async def ZZrw728(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/728", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw729 (\\d+)$"))
async def ZZrw729(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/729", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw730 (\\d+)$"))
async def ZZrw730(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/730", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw731 (\\d+)$"))
async def ZZrw731(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/731", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw732 (\\d+)$"))
async def ZZrw732(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/732", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw733 (\\d+)$"))
async def ZZrw733(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/733", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw734 (\\d+)$"))
async def ZZrw734(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/734", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw735 (\\d+)$"))
async def ZZrw735(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/735", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw736 (\\d+)$"))
async def ZZrw736(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/736", reply_to_message_id=mid)


######################################################################################
## rwaiat List 5
######################################################################################

@Client.on_callback_query(filters.regex("^Yrw5 (\\d+)$"))
async def Yrw5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🇦🇺 اللغة الإنجليزية ⌯", callback_data="rwen " + str(m.from_user.id))] +
        [InlineKeyboardButton("🇫🇷 اللغة الفرنسية ⌯", callback_data="Zrw45 " + str(m.from_user.id))],
        [InlineKeyboardButton("🇩🇪 اللغة الألمانية ⌯", callback_data="Zrw46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("🇹🇳 اللغة التركية ⌯", callback_data="Zrw47 " + str(m.from_user.id))],
        [InlineKeyboardButton("🇯🇵 اللغة اليابانية ⌯", callback_data="Zrw48 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة | مكتبة اللغات | • 🌐 •\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^rwen (\\d+)$"))
async def rwen(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 TOEFL", callback_data="Zrw39 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 IELTS ", callback_data="Zrw40 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 Dictionary", callback_data="Zrw41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("📚 Grammar", callback_data="Zrw42 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 English in Use", callback_data="Zrw43 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 منوعات اللغه الانجليزيه", callback_data="Zrw44 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 🇦🇺 اللغة الإنجليزية\n√", reply_markup=keyboard)
    return


#### Start Lang En
@Client.on_callback_query(filters.regex("^Zrw39 (\\d+)$"))
async def Zrw39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ اختبار التوفل", callback_data="ZZrw743 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ اجتياز التوفل", callback_data="ZZrw744 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ TOFEL", callback_data="ZZrw745 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ The Complete Guide", callback_data="ZZrw746 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ 400 Must have Words", callback_data="ZZrw747 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Prepare TOFEL", callback_data="ZZrw748 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Offical Guide TOFEL", callback_data="ZZrw749 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Essential Vocabulary TOFEL", callback_data="ZZrw750 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ longman complete", callback_data="ZZrw751 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Barron's TOFEL iBT", callback_data="ZZrw752 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwen " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 TOEFL \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw40 (\\d+)$"))
async def Zrw40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ TELTS Vocabulary 1", callback_data="ZZrw754 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Acadmy Wiriting", callback_data="ZZrw755 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Check Your Vocabu", callback_data="ZZrw756 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ TELTS Vocabulary 2", callback_data="ZZrw757 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Speaking", callback_data="ZZrw758 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ Wiriting", callback_data="ZZrw759 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Get Ready 1", callback_data="ZZrw760 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ Get Ready 2", callback_data="ZZrw761 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwen " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 IELTS\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw41 (\\d+)$"))
async def Zrw41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ قاموس لونجمان", callback_data="ZZrw780 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ Oxford Picture", callback_data="ZZrw781 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Collins English", callback_data="ZZrw782 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Senence Dictionary", callback_data="ZZrw783 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Oxford Collocations", callback_data="ZZrw784 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ The Heinle", callback_data="ZZrw785 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwen " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 Dictionary \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw42 (\\d+)$"))
async def Zrw42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ Complete Greate", callback_data="ZZrw804 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ Oxford Living", callback_data="ZZrw805 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ The Blue Book", callback_data="ZZrw806 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ The Good Grammar", callback_data="ZZrw807 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Macmillan Grammar", callback_data="ZZrw808 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Swan", callback_data="ZZrw809 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwen " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 Grammar \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw43 (\\d+)$"))
async def Zrw43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ Phrasal Verb", callback_data="ZZrw811 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ldioms Advanced", callback_data="ZZrw812 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Collocations", callback_data="ZZrw813 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ Elementary", callback_data="ZZrw814 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Pre-intermediate", callback_data="ZZrw815 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Upper-inermediate", callback_data="ZZrw816 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwen " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 English in Use\n√", reply_markup=keyboard)
    return


##### End Lang En
@Client.on_callback_query(filters.regex("^Zrw44 (\\d+)$"))
async def Zrw44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الانجليزية الشاملة", callback_data="ZZrw818 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فعل انجليزي", callback_data="ZZrw819 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عائلة الكلمات", callback_data="ZZrw820 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ The Leader Pharse", callback_data="ZZrw821 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwen " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 📚 منوعات اللغه الانجليزيه\n√", reply_markup=keyboard)
    return


##### Start Lang Fr
@Client.on_callback_query(filters.regex("^Zrw45 (\\d+)$"))
async def Zrw45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الجملة الفرنسية", callback_data="ZZrw823 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ علم نفسك", callback_data="ZZrw824 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم بنفسك", callback_data="ZZrw825 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قواعد اللغة", callback_data="ZZrw826 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المعجم", callback_data="ZZrw827 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 🇫🇷 اللغة الفرنسية\n√", reply_markup=keyboard)
    return


# Start Lang Germ
@Client.on_callback_query(filters.regex("^Zrw46 (\\d+)$"))
async def Zrw46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ تعلم اللغة 1", callback_data="ZZrw842 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم اللغة 2", callback_data="ZZrw843 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ القواعد", callback_data="ZZrw844 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ادوات الاستقهام", callback_data="ZZrw845 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الظروف في تعلم اللغه 3", callback_data="ZZrw846 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ Meineallerersten", callback_data="ZZrw847 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الافعال المساعدة", callback_data="ZZrw848 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ deutsch-fur-araber", callback_data="ZZrw849 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 🇩🇪 اللغة الألمانية\n√", reply_markup=keyboard)
    return


# Start Tur
@Client.on_callback_query(filters.regex("^Zrw47 (\\d+)$"))
async def Zrw47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ مرجعك الدائم", callback_data="ZZrw855 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التركية المبسطة", callback_data="ZZrw856 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم اللغة 1", callback_data="ZZrw857 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ تعلم اللغة 2", callback_data="ZZrw858 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قواعد اللغة", callback_data="ZZrw859 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 🇹🇳 اللغة التركية\n√", reply_markup=keyboard)
    return


# Start Lang Jap
@Client.on_callback_query(filters.regex("^Zrw48 (\\d+)$"))
async def Zrw48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ تعلم اللغة", callback_data="ZZrw861 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قواعد اللغة", callback_data="ZZrw862 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw5 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة كتب 🇯🇵 اللغة اليابانية\n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat Link List 5
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw743 (\\d+)$"))
async def ZZrw743(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/743", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw744 (\\d+)$"))
async def ZZrw744(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/744", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw745 (\\d+)$"))
async def ZZrw745(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/745", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw746 (\\d+)$"))
async def ZZrw746(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/746", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw747 (\\d+)$"))
async def ZZrw747(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/747", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw748 (\\d+)$"))
async def ZZrw748(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/748", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw749 (\\d+)$"))
async def ZZrw749(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/749", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw754 (\\d+)$"))
async def ZZrw754(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/754", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw755 (\\d+)$"))
async def ZZrw755(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/755", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw756 (\\d+)$"))
async def ZZrw756(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/756", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw757 (\\d+)$"))
async def ZZrw757(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/757", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw758 (\\d+)$"))
async def ZZrw758(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/758", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw759 (\\d+)$"))
async def ZZrw759(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/759", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw760 (\\d+)$"))
async def ZZrw760(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/760", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw761 (\\d+)$"))
async def ZZrw761(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/761", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw780 (\\d+)$"))
async def ZZrw780(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/780", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw781 (\\d+)$"))
async def ZZrw781(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/781", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw782 (\\d+)$"))
async def ZZrw782(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/782", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw783 (\\d+)$"))
async def ZZrw783(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/783", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw784 (\\d+)$"))
async def ZZrw784(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/784", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw785 (\\d+)$"))
async def ZZrw785(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/785", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw804 (\\d+)$"))
async def ZZrw804(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/804", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw805 (\\d+)$"))
async def ZZrw805(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/805", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw806 (\\d+)$"))
async def ZZrw806(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/806", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw807 (\\d+)$"))
async def ZZrw807(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/807", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw808 (\\d+)$"))
async def ZZrw808(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/808", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw809 (\\d+)$"))
async def ZZrw809(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/809", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw811 (\\d+)$"))
async def ZZrw811(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/811", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw812 (\\d+)$"))
async def ZZrw812(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/812", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw813 (\\d+)$"))
async def ZZrw813(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/813", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw814 (\\d+)$"))
async def ZZrw814(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/814", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw815 (\\d+)$"))
async def ZZrw815(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/815", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw816 (\\d+)$"))
async def ZZrw816(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/816", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw818 (\\d+)$"))
async def ZZrw818(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/818", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw819 (\\d+)$"))
async def ZZrw819(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/819", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw820 (\\d+)$"))
async def ZZrw820(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/820", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw821 (\\d+)$"))
async def ZZrw821(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/821", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw823 (\\d+)$"))
async def ZZrw823(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/823", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw824 (\\d+)$"))
async def ZZrw824(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/824", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw825 (\\d+)$"))
async def ZZrw825(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/825", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw826 (\\d+)$"))
async def ZZrw826(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/826", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw827 (\\d+)$"))
async def ZZrw827(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/827", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw842 (\\d+)$"))
async def ZZrw842(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/842", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw843 (\\d+)$"))
async def ZZrw843(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/843", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw844 (\\d+)$"))
async def ZZrw844(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/844", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw845 (\\d+)$"))
async def ZZrw845(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/845", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw846 (\\d+)$"))
async def ZZrw846(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/846", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw847 (\\d+)$"))
async def ZZrw847(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/847", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw848 (\\d+)$"))
async def ZZrw848(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/848", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw849 (\\d+)$"))
async def ZZrw849(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/849", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw850 (\\d+)$"))
async def ZZrw850(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/850", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw851 (\\d+)$"))
async def ZZrw851(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/851", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw852 (\\d+)$"))
async def ZZrw852(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/852", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw853 (\\d+)$"))
async def ZZrw853(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/853", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw855 (\\d+)$"))
async def ZZrw855(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/855", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw856 (\\d+)$"))
async def ZZrw856(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/856", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw857 (\\d+)$"))
async def ZZrw857(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/857", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw858 (\\d+)$"))
async def ZZrw858(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/858", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw859 (\\d+)$"))
async def ZZrw859(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/859", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw861 (\\d+)$"))
async def ZZrw861(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/861", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw862 (\\d+)$"))
async def ZZrw862(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/862", reply_to_message_id=mid)


######################################################################################
## rwaiat List 6
#####################################################################################


@Client.on_callback_query(filters.regex("^Yrw6 (\\d+)$"))
async def Yrw6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 كتاب في دقائق", callback_data="Zrw49 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 إدارة الوقت", callback_data="Zrw50 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 الثقة بالنفس", callback_data="Zrw51 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 التخلص من الإباحية", callback_data="Zrw52 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى 🔘 | مكتبة الموضوعات | • 💬 • \n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw49 (\\d+)$"))
async def Zrw49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ انت فرد وحدك", callback_data="ZZrw866 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ صناعة المبتكرين", callback_data="ZZrw867 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ فن جذب الانتباه", callback_data="ZZrw868 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ افرض حضورك", callback_data="ZZrw869 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الروح الايجابية", callback_data="ZZrw870 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الادارة والاداء", callback_data="ZZrw871 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ التنشة الاقتصادية للابناء", callback_data="ZZrw872 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قمة المتعة وقلة الراحة", callback_data="ZZrw873 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ نظم حياتك", callback_data="ZZrw874 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الثقة الابداعية", callback_data="ZZrw875 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حدد اهدافك", callback_data="ZZrw876 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 |  كتاب في دقائق\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw50 (\\d+)$"))
async def Zrw50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ ادارة الوقت 1", callback_data="ZZrw879 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ادارة الوقت الفقي", callback_data="ZZrw880 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ادارة الوقت ملون", callback_data="ZZrw881 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ استثمار الوقت", callback_data="ZZrw882 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مصيدة الوقت", callback_data="ZZrw883 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 إدارة الوقت\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw51 (\\d+)$"))
async def Zrw51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الثقة بالنفس بالكلمات", callback_data="ZZrw892 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الثقة والاعتزاز بالنفس", callback_data="ZZrw893 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الثقة بالنفس الفقي", callback_data="ZZrw894 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الثقة التامه بالنفس", callback_data="ZZrw895 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 الثقة بالنفس\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw52 (\\d+)$"))
async def Zrw52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ كيف تقلع الاباحية للأبد", callback_data="ZZrw904 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دماغك تحت تأثير الاباحية", callback_data="ZZrw905 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سبيل التنعافي", callback_data="ZZrw906 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الخطوات السبعة", callback_data="ZZrw907 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اثار الاباحية علي الدماغ", callback_data="ZZrw908 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ كيف توقف العادة السرية", callback_data="ZZrw909 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عشرة مفاتيح للتخلص من الاباحية", callback_data="ZZrw910 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الانتصار علي العادة السرية", callback_data="ZZrw911 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هوايات وعادات", callback_data="ZZrw912 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw6 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 التخلص من الإباحية\n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat Link List 6
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw866 (\\d+)$"))
async def ZZrw866(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/866", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw867 (\\d+)$"))
async def ZZrw867(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/867", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw868 (\\d+)$"))
async def ZZrw868(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/868", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw869 (\\d+)$"))
async def ZZrw869(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/869", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw870 (\\d+)$"))
async def ZZrw870(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/870", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw871 (\\d+)$"))
async def ZZrw871(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/871", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw872 (\\d+)$"))
async def ZZrw872(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/872", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw873 (\\d+)$"))
async def ZZrw873(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/873", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw874 (\\d+)$"))
async def ZZrw874(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/874", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw875 (\\d+)$"))
async def ZZrw875(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/875", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw876 (\\d+)$"))
async def ZZrw876(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/876", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw879 (\\d+)$"))
async def ZZrw879(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/879", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw880 (\\d+)$"))
async def ZZrw880(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/880", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw881 (\\d+)$"))
async def ZZrw881(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/881", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw882 (\\d+)$"))
async def ZZrw882(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/882", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw883 (\\d+)$"))
async def ZZrw883(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/883", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw892 (\\d+)$"))
async def ZZrw892(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/892", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw893 (\\d+)$"))
async def ZZrw893(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/893", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw894 (\\d+)$"))
async def ZZrw894(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/894", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw895 (\\d+)$"))
async def ZZrw895(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/895", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw904 (\\d+)$"))
async def ZZrw904(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/904", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw905 (\\d+)$"))
async def ZZrw905(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/905", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw906 (\\d+)$"))
async def ZZrw906(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/906", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw907 (\\d+)$"))
async def ZZrw907(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/907", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw908 (\\d+)$"))
async def ZZrw908(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/908", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw909 (\\d+)$"))
async def ZZrw909(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/909", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw910 (\\d+)$"))
async def ZZrw910(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/910", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw911 (\\d+)$"))
async def ZZrw911(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/911", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw912 (\\d+)$"))
async def ZZrw912(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/912", reply_to_message_id=mid)


######################################################################################
## rwaiat List 7
######################################################################################

@Client.on_callback_query(filters.regex("^Yrw7 (\\d+)$"))
async def Yrw7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("📚 سلسلة المغامرون الخمسة", callback_data="Zrw53 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 نوادر جحا للأطفال", callback_data="Zrw54 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 مجلة ميكي", callback_data="Zrw55 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 قصص الأنبياء للأطفال", callback_data="Zrw56 " + str(m.from_user.id))],
        [InlineKeyboardButton("📚 قصص الحيوان", callback_data="Zrw57 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="rwaiat2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 🔘 || كتب الأطفال || • 👦🏻 •\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw53 (\\d+)$"))
async def Zrw53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الكوخ المحترق", callback_data="ZZrw915 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ البيت الخفي", callback_data="ZZrw916 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ العقد المفقود", callback_data="ZZrw917 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الشبح الأسود", callback_data="ZZrw918 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المنزل رقم 98", callback_data="ZZrw919 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ لغز الألغاز", callback_data="ZZrw920 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الرسائل الغامضه", callback_data="ZZrw921 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ القفاز الأحمر", callback_data="ZZrw922 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الأمير المخطوف", callback_data="ZZrw923 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ القصر الأخضر", callback_data="ZZrw924 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اللص الشبح", callback_data="ZZrw925 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ اختفاء الخنفس", callback_data="ZZrw926 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سرقة البنسيون", callback_data="ZZrw927 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الوثائق السرية", callback_data="ZZrw928 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزيرة المهجورة", callback_data="ZZrw929 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الحقيبة السوداء", callback_data="ZZrw930 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ لغز التسعة", callback_data="ZZrw931 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الغابة الملعونة", callback_data="ZZrw932 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ وادي الذئاب", callback_data="ZZrw933 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw7 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى 📚 سلسلة المغامرون الخمسة\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw54 (\\d+)$"))
async def Zrw54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ خذ انت الدرهم", callback_data="ZZrw935 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مرق الأرنب", callback_data="ZZrw936 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ ثيابي أولي مني", callback_data="ZZrw937 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أجرك  صوت الدرهم", callback_data="ZZrw938 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الذي يعطي الكثير", callback_data="ZZrw939 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الله يعطيك", callback_data="ZZrw940 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ والله لن أشتريك", callback_data="ZZrw941 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أجرك لا شئ", callback_data="ZZrw942 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جحا والضيف المريض", callback_data="ZZrw943 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا وكلام الناس", callback_data="ZZrw944 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ من حفر حفرة", callback_data="ZZrw945 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا في دار البخلاء", callback_data="ZZrw946 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جحا والملك", callback_data="ZZrw947 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا يصنع معروفا", callback_data="ZZrw948 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ من أجل خمسة قروش", callback_data="ZZrw949 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا يظهر فجأة", callback_data="ZZrw950 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جحا بائع الحرير", callback_data="ZZrw951 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ان شاء الله", callback_data="ZZrw952 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دعوة البخيل", callback_data="ZZrw953 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ الجار البخيل", callback_data="ZZrw954 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جحا والطعام الطائر", callback_data="ZZrw955 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا شجاع جدا", callback_data="ZZrw956 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجار الطماع", callback_data="ZZrw957 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا ينفذ وعده", callback_data="ZZrw958 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جحا عنيد جدا", callback_data="ZZrw959 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا والحمار الناقص", callback_data="ZZrw960 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جحا وثروة من ذهب", callback_data="ZZrw961 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا المجنون", callback_data="ZZrw962 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ جحا وصديقة في ورطة", callback_data="ZZrw963 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا اشتري حماره", callback_data="ZZrw964 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ حساب الجرة", callback_data="ZZrw965 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ جحا والحمار المشاغب", callback_data="ZZrw966 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw7 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى 📚 نوادر جحا للأطفال\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw55 (\\d+)$"))
async def Zrw55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ قصص اطفال 1", callback_data="ZZrw968 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قصص اطفال 2", callback_data="ZZrw969 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قصص اطفال 3", callback_data="ZZrw970 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ قصص اطفال 4", callback_data="ZZrw971 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ قصص اطفال 5", callback_data="ZZrw972 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ العدد 48", callback_data="ZZrw973 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجدة بطة والمحاسب الحديد", callback_data="ZZrw974 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ أشبال الأنترنت", callback_data="ZZrw975 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ البيضة الذهبيه", callback_data="ZZrw976 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ السباق الرهيب", callback_data="ZZrw977 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ المدينة المثالية", callback_data="ZZrw978 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ بندق ممثل اول", callback_data="ZZrw979 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ بندق والعصفور", callback_data="ZZrw980 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ تنظيف المنزل", callback_data="ZZrw981 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ دهب يأخذ مقلب", callback_data="ZZrw982 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ رنات الجرس", callback_data="ZZrw983 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ شجرة عم دهب", callback_data="ZZrw984 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ريجيم قاس جدا", callback_data="ZZrw985 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سوء تفاهم", callback_data="ZZrw986 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ماتش كورة", callback_data="ZZrw987 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مباراة حاسمة", callback_data="ZZrw988 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ مسألة حظ", callback_data="ZZrw989 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مصيدة الوقت", callback_data="ZZrw990 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ من سيربح المليون", callback_data="ZZrw991 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ مهرجان الظرفاء", callback_data="ZZrw992 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ وليمة مبتكره جدا", callback_data="ZZrw993 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اوكازيون", callback_data="ZZrw994 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ابطال حمل الاثقال", callback_data="ZZrw995 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اطفال ابطال", callback_data="ZZrw996 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw7 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى 📚 مجلة ميكي\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw56 (\\d+)$"))
async def Zrw56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ ادم", callback_data="ZZrw1006 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ نوح", callback_data="ZZrw1007 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ داوود", callback_data="ZZrw1008 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ صالح", callback_data="ZZrw1009 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ هود", callback_data="ZZrw1010 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ ابراهيم", callback_data="ZZrw1011 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ اسماعيل", callback_data="ZZrw1012 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ يوسف", callback_data="ZZrw1013 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ سليمان", callback_data="ZZrw1014 " + str(m.from_user.id))] +
        [InlineKeyboardButton("⌯ موسي", callback_data="ZZrw1015 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ عيسي", callback_data="ZZrw1016 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw7 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى📚 قصص الأنبياء للأطفال\n√", reply_markup=keyboard)
    return


@Client.on_callback_query(filters.regex("^Zrw57 (\\d+)$"))
async def Zrw57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الجزء الاول", callback_data="ZZrw1018 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء التاني", callback_data="ZZrw1019 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء التالت", callback_data="ZZrw1020 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء الرابع", callback_data="ZZrw1021 " + str(m.from_user.id))],
        [InlineKeyboardButton("⌯ الجزء الخامس", callback_data="ZZrw1022 " + str(m.from_user.id))],

        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="Yrw7 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("◍ اهلا بيك فى قائمة 📚 قصص الحيوان\n√", reply_markup=keyboard)
    return


######################################################################################
## rwaiat Link List 7
######################################################################################

@Client.on_callback_query(filters.regex("^ZZrw915 (\\d+)$"))
async def ZZrw915(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/915", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw916 (\\d+)$"))
async def ZZrw916(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/916", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw917 (\\d+)$"))
async def ZZrw917(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/917", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw918 (\\d+)$"))
async def ZZrw918(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/918", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw919 (\\d+)$"))
async def ZZrw919(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/919", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw920 (\\d+)$"))
async def ZZrw920(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/920", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw921 (\\d+)$"))
async def ZZrw921(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/921", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw922 (\\d+)$"))
async def ZZrw922(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/922", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw923 (\\d+)$"))
async def ZZrw923(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/923", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw924 (\\d+)$"))
async def ZZrw924(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/924", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw925 (\\d+)$"))
async def ZZrw925(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/925", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw926 (\\d+)$"))
async def ZZrw926(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/926", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw927 (\\d+)$"))
async def ZZrw927(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/927", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw928 (\\d+)$"))
async def ZZrw928(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/928", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw929 (\\d+)$"))
async def ZZrw929(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/929", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw930 (\\d+)$"))
async def ZZrw930(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/930", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw931 (\\d+)$"))
async def ZZrw931(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/931", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw932 (\\d+)$"))
async def ZZrw932(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/932", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw933 (\\d+)$"))
async def ZZrw933(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/933", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw935 (\\d+)$"))
async def ZZrw935(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/935", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw936 (\\d+)$"))
async def ZZrw936(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/936", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw937 (\\d+)$"))
async def ZZrw937(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/937", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw938 (\\d+)$"))
async def ZZrw938(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/938", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw939 (\\d+)$"))
async def ZZrw939(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/939", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw940 (\\d+)$"))
async def ZZrw940(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/940", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw941 (\\d+)$"))
async def ZZrw941(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/941", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw942 (\\d+)$"))
async def ZZrw942(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/942", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw943 (\\d+)$"))
async def ZZrw943(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/943", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw944 (\\d+)$"))
async def ZZrw944(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/944", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw945 (\\d+)$"))
async def ZZrw945(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/945", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw946 (\\d+)$"))
async def ZZrw946(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/946", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw947 (\\d+)$"))
async def ZZrw947(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/947", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw948 (\\d+)$"))
async def ZZrw948(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/948", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw949 (\\d+)$"))
async def ZZrw949(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/949", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw950 (\\d+)$"))
async def ZZrw950(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/950", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw951 (\\d+)$"))
async def ZZrw951(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/951", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw952 (\\d+)$"))
async def ZZrw952(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/952", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw953 (\\d+)$"))
async def ZZrw953(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/953", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw954 (\\d+)$"))
async def ZZrw954(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/954", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw955 (\\d+)$"))
async def ZZrw955(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/955", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw956 (\\d+)$"))
async def ZZrw956(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/956", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw957 (\\d+)$"))
async def ZZrw957(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/957", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw958 (\\d+)$"))
async def ZZrw958(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/958", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw959 (\\d+)$"))
async def ZZrw959(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/959", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw960 (\\d+)$"))
async def ZZrw960(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/960", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw961 (\\d+)$"))
async def ZZrw961(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/961", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw962 (\\d+)$"))
async def ZZrw962(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/962", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw963 (\\d+)$"))
async def ZZrw963(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/963", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw964 (\\d+)$"))
async def ZZrw964(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/964", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw965 (\\d+)$"))
async def ZZrw965(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/965", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw966 (\\d+)$"))
async def ZZrw966(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/966", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw968 (\\d+)$"))
async def ZZrw968(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/968", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw969 (\\d+)$"))
async def ZZrw969(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/969", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw970 (\\d+)$"))
async def ZZrw970(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/970", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw971 (\\d+)$"))
async def ZZrw971(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/971", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw972 (\\d+)$"))
async def ZZrw972(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/972", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw973 (\\d+)$"))
async def ZZrw973(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/973", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw974 (\\d+)$"))
async def ZZrw974(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/974", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw975 (\\d+)$"))
async def ZZrw975(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/975", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw976 (\\d+)$"))
async def ZZrw976(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/976", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw977 (\\d+)$"))
async def ZZrw977(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/977", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw978 (\\d+)$"))
async def ZZrw978(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/978", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw979 (\\d+)$"))
async def ZZrw979(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/979", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw980 (\\d+)$"))
async def ZZrw980(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/980", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw981 (\\d+)$"))
async def ZZrw981(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/981", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw982 (\\d+)$"))
async def ZZrw982(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/982", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw983 (\\d+)$"))
async def ZZrw983(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/983", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw984 (\\d+)$"))
async def ZZrw984(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/984", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw985 (\\d+)$"))
async def ZZrw985(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/985", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw986 (\\d+)$"))
async def ZZrw986(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/986", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw987 (\\d+)$"))
async def ZZrw987(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/987", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw988 (\\d+)$"))
async def ZZrw988(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/988", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw989 (\\d+)$"))
async def ZZrw989(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/989", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw990 (\\d+)$"))
async def ZZrw990(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/990", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw991 (\\d+)$"))
async def ZZrw991(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/991", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw992 (\\d+)$"))
async def ZZrw992(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/992", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw993 (\\d+)$"))
async def ZZrw993(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/993", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw994 (\\d+)$"))
async def ZZrw994(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/994", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw995 (\\d+)$"))
async def ZZrw995(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/995", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw996 (\\d+)$"))
async def ZZrw996(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/996", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1006 (\\d+)$"))
async def ZZrw1006(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1006", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1007 (\\d+)$"))
async def ZZrw1007(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1007", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1008 (\\d+)$"))
async def ZZrw1008(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1008", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1009 (\\d+)$"))
async def ZZrw1009(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1009", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1010 (\\d+)$"))
async def ZZrw1010(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1010", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1011 (\\d+)$"))
async def ZZrw1011(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1011", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1012 (\\d+)$"))
async def ZZrw1012(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1012", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1013 (\\d+)$"))
async def ZZrw1013(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1013", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1014 (\\d+)$"))
async def ZZrw1014(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1014", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1015 (\\d+)$"))
async def ZZrw1015(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1015", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1016 (\\d+)$"))
async def ZZrw1016(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1016", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1018 (\\d+)$"))
async def ZZrw1018(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1018", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1019 (\\d+)$"))
async def ZZrw1019(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1019", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1020 (\\d+)$"))
async def ZZrw1020(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1020", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1021 (\\d+)$"))
async def ZZrw1021(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1021", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^ZZrw1022 (\\d+)$"))
async def ZZrw1022(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UKtab/1022", reply_to_message_id=mid)

###############################################################################
##                                                                           ##
##   END Code :) "All Copy Right And Coding Whrite" ==> @LeoMedo & @N2GEH    ##
##                                                                           ##
###############################################################################