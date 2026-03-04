from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information
###############################################
##  CopyRight & Creator File And Programing  ##
##                                           ##
##     #######  ######  #####*     *##*      ##
##     #  #  #  ###     #     *   *    *     ##
##     #     #  ##      #     *   *    *     ##
##     #     #  #####   #####*     *##*      ##
##                                           ##
###############################################

################################
## Dev By: @LeoMedo & @N2GEH  ##
################################

@Client.on_callback_query(filters.regex("^quran (\\d+)$"))
async def quran(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("فارس عباد 📖", callback_data="fares " + str(m.from_user.id))] +
        [InlineKeyboardButton("ناصر القطامى 📖", callback_data="naser " + str(m.from_user.id))],
        [InlineKeyboardButton("اسلام صبحى 📖", callback_data="eslam " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبدالباسط عبد الصمد 📖", callback_data="abdelbaset " + str(m.from_user.id))],
        [InlineKeyboardButton("ياسر الدوسري 📖", callback_data="eldosary " + str(m.from_user.id))] +

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.reply_text("• اهلا بك فى القرءان الكريم اختر احدى المقرئين\n√", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^quran2 (\\d+)$"))
async def quran2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("فارس عباد 📖", callback_data="fares " + str(m.from_user.id))] +
        [InlineKeyboardButton("ناصر القطامى 📖", callback_data="naser " + str(m.from_user.id))],
        [InlineKeyboardButton("اسلام صبحى 📖", callback_data="eslam " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبدالباسط عبد الصمد 📖", callback_data="abdelbaset " + str(m.from_user.id))],
        [InlineKeyboardButton("ياسر الدوسري 📖", callback_data="eldosary " + str(m.from_user.id))] +

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("• اختر السوره\n√", reply_markup=keyboard, disable_web_page_preview=True)


########################################################################################################################
########################################################################################################################

@Client.on_callback_query(filters.regex("^fares (\\d+)$"))
async def fares(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xf1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xf2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xf3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xf4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xf5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xf6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xf7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xf8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xf9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xf10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xf11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xf12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xf13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xf14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xf15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xf16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xf17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xf18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xf19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xf20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xf21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xf22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xf23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xf24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xf25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xf26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xf27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xf28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xf29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xf30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xf31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xf32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xf33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xf34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xf35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xf36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xf37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xf38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xf39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xf40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xf41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xf42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xf43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xf44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xf45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xf46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xf47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xf48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xf49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xf50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xf51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="fares2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ فارس عباد\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^fares2 (\\d+)$"))
async def fares2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xf52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xf53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xf54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xf55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xf56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xf57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xf58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xf59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xf60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xf61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xf62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xf63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xf64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xf65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xf66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xf67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xf68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xf69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xf70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xf71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xf72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xf73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xf74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xf75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xf76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xf77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xf78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xf79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xf80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xf81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xf82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xf83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xf84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xf85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xf86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xf87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xf88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xf89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xf90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xf91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xf92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xf93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xf94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xf95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xf96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xf97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xf98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xf99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xf100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xf101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xf102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xf103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xf104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xf105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xf106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xf107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xf108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xf109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xf110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xf111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xf112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xf113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xf114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="fares " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ فارس عباد\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xf1 (\\d+)$"))
async def xf1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/235", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf2 (\\d+)$"))
async def xf2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/236", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf3 (\\d+)$"))
async def xf3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/237", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf4 (\\d+)$"))
async def xf4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/238", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf5 (\\d+)$"))
async def xf5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/239", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf6 (\\d+)$"))
async def xf6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/240", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf7 (\\d+)$"))
async def xf7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/241", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf8 (\\d+)$"))
async def xf8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/242", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf9 (\\d+)$"))
async def xf9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/243", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf10 (\\d+)$"))
async def xf10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/244", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf11 (\\d+)$"))
async def xf11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/245", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf12 (\\d+)$"))
async def xf12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/246", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf13 (\\d+)$"))
async def xf13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/247", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf14 (\\d+)$"))
async def xf14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/248", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf15 (\\d+)$"))
async def xf15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/249", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf16 (\\d+)$"))
async def xf16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/250", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf17 (\\d+)$"))
async def xf17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/251", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf18 (\\d+)$"))
async def xf18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/252", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf19 (\\d+)$"))
async def xf19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/253", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf20 (\\d+)$"))
async def xf20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/254", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf21 (\\d+)$"))
async def xf21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/255", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf22 (\\d+)$"))
async def xf22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/256", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf23 (\\d+)$"))
async def xf23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/257", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf24 (\\d+)$"))
async def xf24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/258", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf25 (\\d+)$"))
async def xf25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/259", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf26 (\\d+)$"))
async def xf26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/260", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf27 (\\d+)$"))
async def xf27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/261", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf28 (\\d+)$"))
async def xf28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/262", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf29 (\\d+)$"))
async def xf29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/263", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf30 (\\d+)$"))
async def xf30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/264", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf31 (\\d+)$"))
async def xf31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/265", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf32 (\\d+)$"))
async def xf32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/266", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf33 (\\d+)$"))
async def xf33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/267", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf34 (\\d+)$"))
async def xf34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/268", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf35 (\\d+)$"))
async def xf35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/269", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf36 (\\d+)$"))
async def xf36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/270", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf37 (\\d+)$"))
async def xf37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/271", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf38 (\\d+)$"))
async def xf38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/272", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf39 (\\d+)$"))
async def xf39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/273", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf40 (\\d+)$"))
async def xf40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/274", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf41 (\\d+)$"))
async def xf41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/275", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf42 (\\d+)$"))
async def xf42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/276", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf43 (\\d+)$"))
async def xf43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/277", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf44 (\\d+)$"))
async def xf44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/278", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf45 (\\d+)$"))
async def xf45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/279", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf46 (\\d+)$"))
async def xf46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/280", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf47 (\\d+)$"))
async def xf47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/281", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf48 (\\d+)$"))
async def xf48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/282", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf49 (\\d+)$"))
async def xf49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/283", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf50 (\\d+)$"))
async def xf50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/284", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf51 (\\d+)$"))
async def xf51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/285", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf52 (\\d+)$"))
async def xf52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/286", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf53 (\\d+)$"))
async def xf53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/287", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf54 (\\d+)$"))
async def xf54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/288", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf55 (\\d+)$"))
async def xf55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/289", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf56 (\\d+)$"))
async def xf56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/290", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf57 (\\d+)$"))
async def xf57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/291", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf58 (\\d+)$"))
async def xf58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/292", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf59 (\\d+)$"))
async def xf59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/293", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf60 (\\d+)$"))
async def xf60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/294", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf61 (\\d+)$"))
async def xf61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/295", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf62 (\\d+)$"))
async def xf62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/296", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf63 (\\d+)$"))
async def xf63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/297", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf64 (\\d+)$"))
async def xf64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/298", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf65 (\\d+)$"))
async def xf65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/299", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf66 (\\d+)$"))
async def xf66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/300", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf67 (\\d+)$"))
async def xf67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/301", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf68 (\\d+)$"))
async def xf68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/302", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf69 (\\d+)$"))
async def xf69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/303", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf70 (\\d+)$"))
async def xf70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/304", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf71 (\\d+)$"))
async def xf71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/305", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf72 (\\d+)$"))
async def xf72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/306", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf73 (\\d+)$"))
async def xf73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/307", reply_to_message_id=mid)
    
@Client.on_callback_query(filters.regex("^xf74 (\\d+)$"))
async def xf74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/308", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf75 (\\d+)$"))
async def xf75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/309", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf76 (\\d+)$"))
async def xf76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/310", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf77 (\\d+)$"))
async def xf77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/311", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf78 (\\d+)$"))
async def xf78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/312", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf79 (\\d+)$"))
async def xf79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/313", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf80 (\\d+)$"))
async def xf80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/314", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf81 (\\d+)$"))
async def xf81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/315", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf82 (\\d+)$"))
async def xf82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/316", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf83 (\\d+)$"))
async def xf83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/317", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf84 (\\d+)$"))
async def xf84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/318", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf85 (\\d+)$"))
async def xf85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/319", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf86 (\\d+)$"))
async def xf86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/320", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf87 (\\d+)$"))
async def xf87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/321", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf88 (\\d+)$"))
async def xf88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/322", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf89 (\\d+)$"))
async def xf89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/323", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf90 (\\d+)$"))
async def xf90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/324", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf91 (\\d+)$"))
async def xf91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/325", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf92 (\\d+)$"))
async def xf92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/326", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf93 (\\d+)$"))
async def xf93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/327", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf94 (\\d+)$"))
async def xf94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/328", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf95 (\\d+)$"))
async def xf95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/329", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf96 (\\d+)$"))
async def xf96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/330", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf97 (\\d+)$"))
async def xf97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/331", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf98 (\\d+)$"))
async def xf98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/332", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf99 (\\d+)$"))
async def xf99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/333", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf100 (\\d+)$"))
async def xf100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/334", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf101 (\\d+)$"))
async def xf101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/335", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf102 (\\d+)$"))
async def xf102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/336", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf103 (\\d+)$"))
async def xf103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/337", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf104 (\\d+)$"))
async def xf104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/338", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf105 (\\d+)$"))
async def xf105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/339", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf106 (\\d+)$"))
async def xf106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/340", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf107 (\\d+)$"))
async def xf107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/341", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf108 (\\d+)$"))
async def xf108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/342", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf109 (\\d+)$"))
async def xf109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/343", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf110 (\\d+)$"))
async def xf110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/342", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf111 (\\d+)$"))
async def xf111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/343", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf112 (\\d+)$"))
async def xf112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/344", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf113 (\\d+)$"))
async def xf113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/345", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xf114 (\\d+)$"))
async def xf114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/346", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^naser (\\d+)$"))
async def naser(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xn1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xn2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xn3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xn4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xn5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xn6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xn7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xn8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xn9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xn10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xn11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xn12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xn13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xn14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xn15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xn16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xn17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xn18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xn19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xn20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xn21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xn22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xn23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xn24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xn25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xn26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xn27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xn28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xn29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xn30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xn31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xn32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xn33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xn34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xn35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xn36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xn37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xn38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xn39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xn40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xn41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xn42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xn43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xn44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xn45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xn46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xn47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xn48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xn49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xn50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xn51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="naser2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ ناصر القطامي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^naser2 (\\d+)$"))
async def naser2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xn52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xn53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xn54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xn55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xn56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xn57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xn58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xn59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xn60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xn61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xn62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xn63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xn64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xn65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xn66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xn67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xn68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xn69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xn70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xn71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xn72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xn73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xn74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xn75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xn76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xn77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xn78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xn79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xn80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xn81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xn82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xn83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xn84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xn85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xn86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xn87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xn88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xn89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xn90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xn91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xn92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xn93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xn94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xn95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xn96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xn97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xn98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xn99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xn100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xn101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xn102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xn103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xn104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xn105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xn106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xn107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xn108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xn109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xn110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xn111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xn112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xn113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xn114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="naser " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ ناصر القطامي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xn1 (\\d+)$"))
async def xn1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/348", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn2 (\\d+)$"))
async def xn2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/349", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn3 (\\d+)$"))
async def xn3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/350", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn4 (\\d+)$"))
async def xn4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/351", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn5 (\\d+)$"))
async def xn5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/352", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn6 (\\d+)$"))
async def xn6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/353", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn7 (\\d+)$"))
async def xn7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/354", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn8 (\\d+)$"))
async def xn8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/355", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn9 (\\d+)$"))
async def xn9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/356", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn10 (\\d+)$"))
async def xn10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/357", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn11 (\\d+)$"))
async def xn11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/358", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn12 (\\d+)$"))
async def xn12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/359", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn13 (\\d+)$"))
async def xn13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/360", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn14 (\\d+)$"))
async def xn14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/361", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn15 (\\d+)$"))
async def xn15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/362", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn16 (\\d+)$"))
async def xn16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/363", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn17 (\\d+)$"))
async def xn17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/364", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn18 (\\d+)$"))
async def xn18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/365", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn19 (\\d+)$"))
async def xn19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/366", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn20 (\\d+)$"))
async def xn20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/367", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn21 (\\d+)$"))
async def xn21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/368", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn22 (\\d+)$"))
async def xn22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/369", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn23 (\\d+)$"))
async def xn23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/370", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn24 (\\d+)$"))
async def xn24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/371", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn25 (\\d+)$"))
async def xn25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/372", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn26 (\\d+)$"))
async def xn26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/373", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn27 (\\d+)$"))
async def xn27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/374", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn28 (\\d+)$"))
async def xn28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/375", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn29 (\\d+)$"))
async def xn29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/376", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn30 (\\d+)$"))
async def xn30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/377", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn31 (\\d+)$"))
async def xn31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/378", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn32 (\\d+)$"))
async def xn32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/379", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn33 (\\d+)$"))
async def xn33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/380", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn34 (\\d+)$"))
async def xn34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/381", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn35 (\\d+)$"))
async def xn35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/382", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn36 (\\d+)$"))
async def xn36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/383", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn37 (\\d+)$"))
async def xn37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/384", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn38 (\\d+)$"))
async def xn38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/385", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn39 (\\d+)$"))
async def xn39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/386", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn40 (\\d+)$"))
async def xn40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/387", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn41 (\\d+)$"))
async def xn41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/388", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn42 (\\d+)$"))
async def xn42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/389", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn43 (\\d+)$"))
async def xn43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/390", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn44 (\\d+)$"))
async def xn44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/391", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn45 (\\d+)$"))
async def xn45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/392", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn46 (\\d+)$"))
async def xn46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/393", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn47 (\\d+)$"))
async def xn47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/394", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn48 (\\d+)$"))
async def xn48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/395", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn49 (\\d+)$"))
async def xn49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/396", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn50 (\\d+)$"))
async def xn50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/397", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn51 (\\d+)$"))
async def xn51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/398", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn52 (\\d+)$"))
async def xn52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/399", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn53 (\\d+)$"))
async def xn53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/400", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn54 (\\d+)$"))
async def xn54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/411", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn55 (\\d+)$"))
async def xn55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/412", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn56 (\\d+)$"))
async def xn56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/413", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn57 (\\d+)$"))
async def xn57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/414", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn58 (\\d+)$"))
async def xn58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/415", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn59 (\\d+)$"))
async def xn59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/416", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn60 (\\d+)$"))
async def xn60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/417", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn61 (\\d+)$"))
async def xn61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/418", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn62 (\\d+)$"))
async def xn62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/419", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn63 (\\d+)$"))
async def xn63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/420", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn64 (\\d+)$"))
async def xn64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/421", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn65 (\\d+)$"))
async def xn65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/422", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn66 (\\d+)$"))
async def xn66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/423", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn67 (\\d+)$"))
async def xn67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/424", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn68 (\\d+)$"))
async def xn68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/425", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn69 (\\d+)$"))
async def xn69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/426", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn70 (\\d+)$"))
async def xn70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/427", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn71 (\\d+)$"))
async def xn71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/428", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn72 (\\d+)$"))
async def xn72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/429", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn73 (\\d+)$"))
async def xn73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/430", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn74 (\\d+)$"))
async def xn74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/431", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn75 (\\d+)$"))
async def xn75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/432", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn76 (\\d+)$"))
async def xn76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/433", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn77 (\\d+)$"))
async def xn77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/434", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn78 (\\d+)$"))
async def xn78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/435", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn79 (\\d+)$"))
async def xn79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/436", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn80 (\\d+)$"))
async def xn80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/437", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn81 (\\d+)$"))
async def xn81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/438", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn82 (\\d+)$"))
async def xn82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/439", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn83 (\\d+)$"))
async def xn83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/440", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn84 (\\d+)$"))
async def xn84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/441", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn85 (\\d+)$"))
async def xn85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/442", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn86 (\\d+)$"))
async def xn86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/443", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn87 (\\d+)$"))
async def xn87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/444", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn88 (\\d+)$"))
async def xn88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/445", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn89 (\\d+)$"))
async def xn89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/446", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn90 (\\d+)$"))
async def xn90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/447", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn91 (\\d+)$"))
async def xn91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/448", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn92 (\\d+)$"))
async def xn92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/449", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn93 (\\d+)$"))
async def xn93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/450", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn94 (\\d+)$"))
async def xn94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/451", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn95 (\\d+)$"))
async def xn95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/452", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn96 (\\d+)$"))
async def xn96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/453", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn97 (\\d+)$"))
async def xn97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/454", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn98 (\\d+)$"))
async def xn98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/455", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn99 (\\d+)$"))
async def xn99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/456", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn100 (\\d+)$"))
async def xn100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/457", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn101 (\\d+)$"))
async def xn101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/458", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn102 (\\d+)$"))
async def xn102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/459", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn103 (\\d+)$"))
async def xn103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/460", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn104 (\\d+)$"))
async def xn104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/461", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn105 (\\d+)$"))
async def xn105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/462", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn106 (\\d+)$"))
async def xn106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/463", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn107 (\\d+)$"))
async def xn107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/462", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn108 (\\d+)$"))
async def xn108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/463", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn109 (\\d+)$"))
async def xn109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/464", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn110 (\\d+)$"))
async def xn110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/465", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn111 (\\d+)$"))
async def xn111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/466", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn112 (\\d+)$"))
async def xn112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/467", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn113 (\\d+)$"))
async def xn113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/468", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xn114 (\\d+)$"))
async def xn114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/469", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^eslam (\\d+)$"))
async def eslam(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الرعد 🕋", callback_data="xes13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xes17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xes18 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xes26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("لقمان 🕋", callback_data="xes31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xes32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xes41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xes42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الدخان 🕋", callback_data="xes44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xes50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xes53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xes54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xes55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xes56 " + str(m.from_user.id))] +

        [InlineKeyboardButton("➡️ التالي", callback_data="eslam2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ اسلام صبحي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^eslam2 (\\d+)$"))
async def eslam2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الحشر 🕋", callback_data="xes59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التغابن 🕋", callback_data="xes64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xes66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xes67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xes68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المعارج 🕋", callback_data="xes70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xes72 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xes76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النازعات 🕋", callback_data="xes79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البروج 🕋", callback_data="xes85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xes88 " + str(m.from_user.id))] +


        [InlineKeyboardButton("رجوع ⬅️", callback_data="eslam " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ اسلام صبحي\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xes13 (\\d+)$"))
async def xes13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/471", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes17 (\\d+)$"))
async def xes17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/472", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes18 (\\d+)$"))
async def xes18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/473", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes26 (\\d+)$"))
async def xes26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/474", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes31 (\\d+)$"))
async def xes31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/475", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes32 (\\d+)$"))
async def xes32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/476", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes41 (\\d+)$"))
async def xes41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/477", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes42 (\\d+)$"))
async def xes42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/478", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes44 (\\d+)$"))
async def xes44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/479", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes50 (\\d+)$"))
async def xes50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/480", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes53 (\\d+)$"))
async def xes53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/481", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes54 (\\d+)$"))
async def xes54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/482", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes55 (\\d+)$"))
async def xes55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/483", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes56 (\\d+)$"))
async def xes56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/484", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes59 (\\d+)$"))
async def xes59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/485", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes64 (\\d+)$"))
async def xes64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/486", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes66 (\\d+)$"))
async def xes66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/487", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes67 (\\d+)$"))
async def xes67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/488", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes68 (\\d+)$"))
async def xes68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/489", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes70 (\\d+)$"))
async def xes70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/490", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes72 (\\d+)$"))
async def xes72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/491", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes76 (\\d+)$"))
async def xes76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/492", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes79 (\\d+)$"))
async def xes79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/493", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes85 (\\d+)$"))
async def xes85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/494", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xes88 (\\d+)$"))
async def xes88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/495", reply_to_message_id=mid)


############################################################################################
############################################################################################


@Client.on_callback_query(filters.regex("^abdelbaset (\\d+)$"))
async def abdelbaset(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xabd1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xabd2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xabd3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xabd4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xabd5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xabd6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xabd7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xabd8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xabd9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xabd10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xabd11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xabd12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xabd13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xabd14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xabd15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xabd16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xabd17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xabd18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xabd19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xabd20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xabd21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xabd22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xabd23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xabd24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xabd25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xabd26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xabd27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xabd28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xabd29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xabd30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xabd31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xabd32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xabd33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xabd34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xabd35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xabd36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xabd37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xabd38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xabd39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xabd40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xabd41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xabd42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xabd43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xabd44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xabd45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xabd46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xabd47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xabd48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xabd49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xabd50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xabd51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="abdelbaset2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("• اختر سوره للقارئ عبدالباسط عبدالصمد\n√", reply_markup=keyboard,
                              disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^abdelbaset2 (\\d+)$"))
async def abdelbaset2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("الطور 🕋", callback_data="xabd52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xabd53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xabd54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xabd55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xabd56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xabd57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xabd58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xabd59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xabd60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xabd61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xabd62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xabd63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xabd64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xabd65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xabd66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xabd67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xabd68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xabd69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xabd70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xabd71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xabd72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xabd73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xabd74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xabd75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xabd76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xabd77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xabd78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xabd79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xabd80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xabd81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xabd82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xabd83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xabd84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xabd85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xabd86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xabd87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xabd88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xabd89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xabd90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xabd91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xabd92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xabd93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xabd94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xabd95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xabd96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xabd97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xabd98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xabd99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xabd100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xabd101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xabd102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xabd103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xabd104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xabd105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xabd106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xabd107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xabd108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xabd109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xabd110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xabd111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xabd112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xabd113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xabd114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="abdelbaset " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ عبدالباسط عبدالصمد\n√", reply_markup=keyboard,
                              disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xabd1 (\\d+)$"))
async def xabd1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/491", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd2 (\\d+)$"))
async def xabd2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/492", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd3 (\\d+)$"))
async def xabd3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/493", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd4 (\\d+)$"))
async def xabd4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/494", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd5 (\\d+)$"))
async def xabd5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/495", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd6 (\\d+)$"))
async def xabd6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/496", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd7 (\\d+)$"))
async def xabd7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/497", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd8 (\\d+)$"))
async def xabd8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/498", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd9 (\\d+)$"))
async def xabd9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/499", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd10 (\\d+)$"))
async def xabd10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/500", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd11 (\\d+)$"))
async def xabd11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/501", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd12 (\\d+)$"))
async def xabd12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/502", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd13 (\\d+)$"))
async def xabd13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/503", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd14 (\\d+)$"))
async def xabd14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/504", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd15 (\\d+)$"))
async def xabd15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/505", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd16 (\\d+)$"))
async def xabd16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/506", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd17 (\\d+)$"))
async def xabd17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/507", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd18 (\\d+)$"))
async def xabd18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/508", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd19 (\\d+)$"))
async def xabd19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/509", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd20 (\\d+)$"))
async def xabd20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/510", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd21 (\\d+)$"))
async def xabd21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/511", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd22 (\\d+)$"))
async def xabd22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/512", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd23 (\\d+)$"))
async def xabd23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/513", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd24 (\\d+)$"))
async def xabd24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/514", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd25 (\\d+)$"))
async def xabd25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/515", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd26 (\\d+)$"))
async def xabd26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/516", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd27 (\\d+)$"))
async def xabd27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/517", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd28 (\\d+)$"))
async def xabd28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/518", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd29 (\\d+)$"))
async def xabd29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/519", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd30 (\\d+)$"))
async def xabd30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/520", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd31 (\\d+)$"))
async def xabd31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/521", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd32 (\\d+)$"))
async def xabd32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/522", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd33 (\\d+)$"))
async def xabd33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/523", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd34 (\\d+)$"))
async def xabd34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/524", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd35 (\\d+)$"))
async def xabd35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/525", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd36 (\\d+)$"))
async def xabd36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/526", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd37 (\\d+)$"))
async def xabd37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/527", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd38 (\\d+)$"))
async def xabd38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/528", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd39 (\\d+)$"))
async def xabd39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/529", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd40 (\\d+)$"))
async def xabd40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/530", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd41 (\\d+)$"))
async def xabd41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/531", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd42 (\\d+)$"))
async def xabd42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/532", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd43 (\\d+)$"))
async def xabd43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/533", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd44 (\\d+)$"))
async def xabd44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/534", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd45 (\\d+)$"))
async def xabd45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/535", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd46 (\\d+)$"))
async def xabd46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/536", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd47 (\\d+)$"))
async def xabd47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/537", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd48 (\\d+)$"))
async def xabd48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/538", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd49 (\\d+)$"))
async def xabd49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/539", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd50 (\\d+)$"))
async def xabd50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/540", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd51 (\\d+)$"))
async def xabd51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/541", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd52 (\\d+)$"))
async def xabd52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/542", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd53 (\\d+)$"))
async def xabd53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/543", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd54 (\\d+)$"))
async def xabd54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/544", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd55 (\\d+)$"))
async def xabd55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/545", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd56 (\\d+)$"))
async def xabd56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/546", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd57 (\\d+)$"))
async def xabd57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/547", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd58 (\\d+)$"))
async def xabd58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/548", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd59 (\\d+)$"))
async def xabd59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/549", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd60 (\\d+)$"))
async def xabd60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/550", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd61 (\\d+)$"))
async def xabd61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/551", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd62 (\\d+)$"))
async def xabd62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/552", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd63 (\\d+)$"))
async def xabd63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/553", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd64 (\\d+)$"))
async def xabd64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/554", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd65 (\\d+)$"))
async def xabd65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/555", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd66 (\\d+)$"))
async def xabd66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/556", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd67 (\\d+)$"))
async def xabd67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/557", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd68 (\\d+)$"))
async def xabd68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/558", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd69 (\\d+)$"))
async def xabd69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/559", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd70 (\\d+)$"))
async def xabd70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/560", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd71 (\\d+)$"))
async def xabd71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/561", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd72 (\\d+)$"))
async def xabd72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/562", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd73 (\\d+)$"))
async def xabd73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/563", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd74 (\\d+)$"))
async def xabd74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/564", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd75 (\\d+)$"))
async def xabd75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/565", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd76 (\\d+)$"))
async def xabd76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/566", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd77 (\\d+)$"))
async def xabd77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/567", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd78 (\\d+)$"))
async def xabd78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/568", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd79 (\\d+)$"))
async def xabd79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/569", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd80 (\\d+)$"))
async def xabd80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/570", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd81 (\\d+)$"))
async def xabd81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/571", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd82 (\\d+)$"))
async def xabd82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/572", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd83 (\\d+)$"))
async def xabd83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/573", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd84 (\\d+)$"))
async def xabd84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/574", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd85 (\\d+)$"))
async def xabd85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/575", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd86 (\\d+)$"))
async def xabd86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/576", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd87 (\\d+)$"))
async def xabd87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/577", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd88 (\\d+)$"))
async def xabd88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/578", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd89 (\\d+)$"))
async def xabd89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/579", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd90 (\\d+)$"))
async def xabd90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/580", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd91 (\\d+)$"))
async def xabd91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/581", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd92 (\\d+)$"))
async def xabd92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/582", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd93 (\\d+)$"))
async def xabd93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/583", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd94 (\\d+)$"))
async def xabd94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/584", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd95 (\\d+)$"))
async def xabd95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/585", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd96 (\\d+)$"))
async def xabd96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/586", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd97 (\\d+)$"))
async def xabd97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/587", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd98 (\\d+)$"))
async def xabd98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/588", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd99 (\\d+)$"))
async def xabd99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/589", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd100 (\\d+)$"))
async def xabd100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/590", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd101 (\\d+)$"))
async def xabd101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/591", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd102 (\\d+)$"))
async def xabd102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/592", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd103 (\\d+)$"))
async def xabd103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/593", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd104 (\\d+)$"))
async def xabd104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/594", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd105 (\\d+)$"))
async def xabd105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/595", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd106 (\\d+)$"))
async def xabd106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/596", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd107 (\\d+)$"))
async def xabd107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/597", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd108 (\\d+)$"))
async def xabd108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/598", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd109 (\\d+)$"))
async def xabd109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/599", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd110 (\\d+)$"))
async def xabd110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/600", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd111 (\\d+)$"))
async def xabd111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/601", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xabd112 (\\d+)$"))
async def xabd112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/602", reply_to_message_id=mid)
    
@Client.on_callback_query(filters.regex("^xabd113 (\\d+)$"))
async def xabd113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/603", reply_to_message_id=mid)
    
@Client.on_callback_query(filters.regex("^xabd114 (\\d+)$"))
async def xabd114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("hhttps://t.me/botAlamy/604", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################


@Client.on_callback_query(filters.regex("^eldosary (\\d+)$"))
async def eldosary(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الفاتحه 🕋", callback_data="xdos1 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البقرة 🕋", callback_data="xdos2 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ال عمران 🕋", callback_data="xdos3 " + str(m.from_user.id))],
        [InlineKeyboardButton("النساء 🕋", callback_data="xdos4 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المائدة 🕋", callback_data="xdos5 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانعام 🕋", callback_data="xdos6 " + str(m.from_user.id))],
        [InlineKeyboardButton("الأعراف 🕋", callback_data="xdos7 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنفال 🕋", callback_data="xdos8 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التوبة 🕋", callback_data="xdos9 " + str(m.from_user.id))],
        [InlineKeyboardButton("يونس 🕋", callback_data="xdos10 " + str(m.from_user.id))] +
        [InlineKeyboardButton("هود 🕋", callback_data="xdos11 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يوسف 🕋", callback_data="xdos12 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرعد 🕋", callback_data="xdos13 " + str(m.from_user.id))] +
        [InlineKeyboardButton("أبراهيم 🕋", callback_data="xdos14 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحجر 🕋", callback_data="xdos15 " + str(m.from_user.id))],
        [InlineKeyboardButton("النحل 🕋", callback_data="xdos16 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاسراء 🕋", callback_data="xdos17 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكهف 🕋", callback_data="xdos18 " + str(m.from_user.id))],
        [InlineKeyboardButton("مريم 🕋", callback_data="xdos19 " + str(m.from_user.id))] +
        [InlineKeyboardButton("طه 🕋", callback_data="xdos20 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الأنبياء 🕋", callback_data="xdos21 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحج 🕋", callback_data="xdos22 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المؤمنون 🕋", callback_data="xdos23 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النور 🕋", callback_data="xdos24 " + str(m.from_user.id))],
        [InlineKeyboardButton("الفرقان 🕋", callback_data="xdos25 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشعراء 🕋", callback_data="xdos26 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النحل 🕋", callback_data="xdos27 " + str(m.from_user.id))],
        [InlineKeyboardButton("القصص 🕋", callback_data="xdos28 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العنكبوت 🕋", callback_data="xdos29 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الروم 🕋", callback_data="xdos30 " + str(m.from_user.id))],
        [InlineKeyboardButton("لقمان 🕋", callback_data="xdos31 " + str(m.from_user.id))] +
        [InlineKeyboardButton("السجدة 🕋", callback_data="xdos32 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاحزاب 🕋", callback_data="xdos33 " + str(m.from_user.id))],
        [InlineKeyboardButton("سبأ 🕋", callback_data="xdos34 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فاطر 🕋", callback_data="xdos35 " + str(m.from_user.id))] +
        [InlineKeyboardButton("يس 🕋", callback_data="xdos36 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصافات 🕋", callback_data="xdos37 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ص 🕋", callback_data="xdos38 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزمر 🕋", callback_data="xdos39 " + str(m.from_user.id))],
        [InlineKeyboardButton("غافر 🕋", callback_data="xdos40 " + str(m.from_user.id))] +
        [InlineKeyboardButton("فصلت 🕋", callback_data="xdos41 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الشورئ 🕋", callback_data="xdos42 " + str(m.from_user.id))],
        [InlineKeyboardButton("الزخرف 🕋", callback_data="xdos43 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الدخان 🕋", callback_data="xdos44 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجاثيه 🕋", callback_data="xdos45 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاحقاف 🕋", callback_data="xdos46 " + str(m.from_user.id))] +
        [InlineKeyboardButton("محمد 🕋", callback_data="xdos47 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفتح 🕋", callback_data="xdos48 " + str(m.from_user.id))],
        [InlineKeyboardButton("الحجرات 🕋", callback_data="xdos49 " + str(m.from_user.id))] +
        [InlineKeyboardButton("ق 🕋", callback_data="xdos50 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الذاريات 🕋", callback_data="xdos51 " + str(m.from_user.id))],

        [InlineKeyboardButton("➡️ التالي", callback_data="eldosary2 " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ ياسر الدوسري\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^eldosary2 (\\d+)$"))
async def eldosary2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الطور 🕋", callback_data="xdos52 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النجم 🕋", callback_data="xdos53 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القمر 🕋", callback_data="xdos54 " + str(m.from_user.id))],
        [InlineKeyboardButton("الرحمن 🕋", callback_data="xdos55 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الواقعه 🕋", callback_data="xdos56 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحديد 🕋", callback_data="xdos57 " + str(m.from_user.id))],
        [InlineKeyboardButton("المجادلة 🕋", callback_data="xdos58 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحشر 🕋", callback_data="xdos59 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الممتحنة 🕋", callback_data="xdos60 " + str(m.from_user.id))],
        [InlineKeyboardButton("الصف 🕋", callback_data="xdos61 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجمعة 🕋", callback_data="xdos62 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المنافقون 🕋", callback_data="xdos63 " + str(m.from_user.id))],
        [InlineKeyboardButton("التغابن 🕋", callback_data="xdos64 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطلاق 🕋", callback_data="xdos65 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التحريم 🕋", callback_data="xdos66 " + str(m.from_user.id))],
        [InlineKeyboardButton("الملك 🕋", callback_data="xdos67 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القلم 🕋", callback_data="xdos68 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الحاقة 🕋", callback_data="xdos69 " + str(m.from_user.id))],
        [InlineKeyboardButton("المعارج 🕋", callback_data="xdos70 " + str(m.from_user.id))] +
        [InlineKeyboardButton("نوح 🕋", callback_data="xdos71 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الجن 🕋", callback_data="xdos72 " + str(m.from_user.id))],
        [InlineKeyboardButton("المزمل 🕋", callback_data="xdos73 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المدثر 🕋", callback_data="xdos74 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القيامة 🕋", callback_data="xdos75 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانسان 🕋", callback_data="xdos76 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المرسلات 🕋", callback_data="xdos77 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النبأ 🕋", callback_data="xdos78 " + str(m.from_user.id))],
        [InlineKeyboardButton("النازعات 🕋", callback_data="xdos79 " + str(m.from_user.id))] +
        [InlineKeyboardButton("عبس 🕋", callback_data="xdos80 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكوير 🕋", callback_data="xdos81 " + str(m.from_user.id))],
        [InlineKeyboardButton("الانفطار 🕋", callback_data="xdos82 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المطففين 🕋", callback_data="xdos83 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الانشقاق 🕋", callback_data="xdos84 " + str(m.from_user.id))],
        [InlineKeyboardButton("البروج 🕋", callback_data="xdos85 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الطارق 🕋", callback_data="xdos86 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الاعلي 🕋", callback_data="xdos87 " + str(m.from_user.id))],
        [InlineKeyboardButton("الغاشية 🕋", callback_data="xdos88 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفجر 🕋", callback_data="xdos89 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البلد 🕋", callback_data="xdos90 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشمس 🕋", callback_data="xdos91 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الليل 🕋", callback_data="xdos92 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الضحئ 🕋", callback_data="xdos93 " + str(m.from_user.id))],
        [InlineKeyboardButton("الشرح 🕋", callback_data="xdos94 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التين 🕋", callback_data="xdos95 " + str(m.from_user.id))] +
        [InlineKeyboardButton("العلق 🕋", callback_data="xdos96 " + str(m.from_user.id))],
        [InlineKeyboardButton("القدر 🕋", callback_data="xdos97 " + str(m.from_user.id))] +
        [InlineKeyboardButton("البينة 🕋", callback_data="xdos98 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الزلزلة 🕋", callback_data="xdos99 " + str(m.from_user.id))],
        [InlineKeyboardButton("العاديات 🕋", callback_data="xdos100 " + str(m.from_user.id))] +
        [InlineKeyboardButton("القارعة 🕋", callback_data="xdos101 " + str(m.from_user.id))] +
        [InlineKeyboardButton("التكاثر 🕋", callback_data="xdos102 " + str(m.from_user.id))],
        [InlineKeyboardButton("العصر 🕋", callback_data="xdos103 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الهمزة 🕋", callback_data="xdos104 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفيل 🕋", callback_data="xdos105 " + str(m.from_user.id))],
        [InlineKeyboardButton("قريش 🕋", callback_data="xdos106 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الماعون 🕋", callback_data="xdos107 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الكوثر 🕋", callback_data="xdos108 " + str(m.from_user.id))],
        [InlineKeyboardButton("الكافرون 🕋", callback_data="xdos109 " + str(m.from_user.id))] +
        [InlineKeyboardButton("النصر 🕋", callback_data="xdos110 " + str(m.from_user.id))] +
        [InlineKeyboardButton("المسد 🕋", callback_data="xdos111 " + str(m.from_user.id))],
        [InlineKeyboardButton("الاخلاص 🕋", callback_data="xdos112 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الفلق 🕋", callback_data="xdos113 " + str(m.from_user.id))] +
        [InlineKeyboardButton("الناس 🕋", callback_data="xdos114 " + str(m.from_user.id))],

        [InlineKeyboardButton("رجوع ⬅️", callback_data="eldosary " + str(m.from_user.id))],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="quran2 " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("• اختر سوره للقارئ ياسر الدوسري\n√", reply_markup=keyboard, disable_web_page_preview=True)


@Client.on_callback_query(filters.regex("^xdos1 (\\d+)$"))
async def xdos1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/608", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos2 (\\d+)$"))
async def xdos2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/609", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos3 (\\d+)$"))
async def xdos3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/610", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos4 (\\d+)$"))
async def xdos4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/611", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos5 (\\d+)$"))
async def xdos5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/612", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos6 (\\d+)$"))
async def xdos6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/613", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos7 (\\d+)$"))
async def xdos7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/614", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos8 (\\d+)$"))
async def xdos8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/615", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos9 (\\d+)$"))
async def xdos9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/616", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos10 (\\d+)$"))
async def xdos10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/617", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos11 (\\d+)$"))
async def xdos11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/618", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos12 (\\d+)$"))
async def xdos12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/619", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos13 (\\d+)$"))
async def xdos13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/620", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos14 (\\d+)$"))
async def xdos14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/621", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos15 (\\d+)$"))
async def xdos15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/622", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos16 (\\d+)$"))
async def xdos16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/623", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos17 (\\d+)$"))
async def xdos17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/624", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos18 (\\d+)$"))
async def xdos18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/625", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos19 (\\d+)$"))
async def xdos19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/626", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos20 (\\d+)$"))
async def xdos20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/627", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos21 (\\d+)$"))
async def xdos21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/628", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos22 (\\d+)$"))
async def xdos22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/629", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos23 (\\d+)$"))
async def xdos23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/630", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos24 (\\d+)$"))
async def xdos24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/631", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos25 (\\d+)$"))
async def xdos25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/632", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos26 (\\d+)$"))
async def xdos26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/633", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos27 (\\d+)$"))
async def xdos27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/634", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos28 (\\d+)$"))
async def xdos28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/635", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos29 (\\d+)$"))
async def xdos30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/636", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos30 (\\d+)$"))
async def xdos31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/637", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos31 (\\d+)$"))
async def xdos32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/638", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos32 (\\d+)$"))
async def xdos33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/639", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos33 (\\d+)$"))
async def xdos34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/640", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos34 (\\d+)$"))
async def xdos35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/641", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos35 (\\d+)$"))
async def xdos36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/642", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos36 (\\d+)$"))
async def xdos37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/643", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos37 (\\d+)$"))
async def xdos38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/644", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos38 (\\d+)$"))
async def xdos39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/645", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos39 (\\d+)$"))
async def xdos40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/646", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos40 (\\d+)$"))
async def xdos41(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/647", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos41 (\\d+)$"))
async def xdos42(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/648", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos42 (\\d+)$"))
async def xdos43(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/649", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos43 (\\d+)$"))
async def xdos44(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/650", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos44 (\\d+)$"))
async def xdos45(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/651", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos45 (\\d+)$"))
async def xdos46(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/652", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos46 (\\d+)$"))
async def xdos47(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/653", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos47 (\\d+)$"))
async def xdos48(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/654", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos48 (\\d+)$"))
async def xdos49(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/655", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos49 (\\d+)$"))
async def xdos50(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/656", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos50 (\\d+)$"))
async def xdos51(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/657", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos51 (\\d+)$"))
async def xdos52(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/658", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos52 (\\d+)$"))
async def xdos53(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/659", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos53 (\\d+)$"))
async def xdos54(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/660", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos54 (\\d+)$"))
async def xdos55(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/661", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos55 (\\d+)$"))
async def xdos56(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/662", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos56 (\\d+)$"))
async def xdos57(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/663", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos57 (\\d+)$"))
async def xdos58(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/664", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos58 (\\d+)$"))
async def xdos59(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/665", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos59 (\\d+)$"))
async def xdos60(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/666", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos60 (\\d+)$"))
async def xdos61(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/667", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos61 (\\d+)$"))
async def xdos62(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/668", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos62 (\\d+)$"))
async def xdos63(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/669", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos63 (\\d+)$"))
async def xdos64(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/670", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos64 (\\d+)$"))
async def xdos65(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/671", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos65 (\\d+)$"))
async def xdos66(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/672", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos66 (\\d+)$"))
async def xdos67(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/673", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos67 (\\d+)$"))
async def xdos68(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/674", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos68 (\\d+)$"))
async def xdos69(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/675", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos69 (\\d+)$"))
async def xdos70(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/676", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos70 (\\d+)$"))
async def xdos71(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/677", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos71 (\\d+)$"))
async def xdos72(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/678", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos72 (\\d+)$"))
async def xdos73(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/679", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos73 (\\d+)$"))
async def xdos74(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/680", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos74 (\\d+)$"))
async def xdos75(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/681", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos75 (\\d+)$"))
async def xdos76(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/682", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos76 (\\d+)$"))
async def xdos77(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/683", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos77 (\\d+)$"))
async def xdos78(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/684", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos78 (\\d+)$"))
async def xdos79(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/685", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos79 (\\d+)$"))
async def xdos80(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/686", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos80 (\\d+)$"))
async def xdos81(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/687", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos81 (\\d+)$"))
async def xdos82(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/688", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos82 (\\d+)$"))
async def xdos83(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/689", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos83 (\\d+)$"))
async def xdos84(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/690", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos84 (\\d+)$"))
async def xdos85(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/691", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos85 (\\d+)$"))
async def xdos86(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/692", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos86 (\\d+)$"))
async def xdos87(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/693", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos87 (\\d+)$"))
async def xdos88(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/694", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos88 (\\d+)$"))
async def xdos89(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/695", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos89 (\\d+)$"))
async def xdos90(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/696", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos90 (\\d+)$"))
async def xdos91(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/697", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos91 (\\d+)$"))
async def xdos92(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/698", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos92 (\\d+)$"))
async def xdos93(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/699", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos93 (\\d+)$"))
async def xdos94(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/700", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos94 (\\d+)$"))
async def xdos95(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/701", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos95 (\\d+)$"))
async def xdos96(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/702", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos96 (\\d+)$"))
async def xdos97(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/703", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos97 (\\d+)$"))
async def xdos98(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/704", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos98 (\\d+)$"))
async def xdos99(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/705", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos99 (\\d+)$"))
async def xdos100(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/706", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos100 (\\d+)$"))
async def xdos101(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/707", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos101 (\\d+)$"))
async def xdos102(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/708", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos102 (\\d+)$"))
async def xdos103(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/709", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos103 (\\d+)$"))
async def xdos104(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/710", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos104 (\\d+)$"))
async def xdos105(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/711", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos105 (\\d+)$"))
async def xdos106(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/712", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos106 (\\d+)$"))
async def xdos107(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/713", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos107 (\\d+)$"))
async def xdos108(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/714", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos108 (\\d+)$"))
async def xdos109(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/715", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos109 (\\d+)$"))
async def xdos110(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/716", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos110 (\\d+)$"))
async def xdos111(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/717", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos111 (\\d+)$"))
async def xdos112(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/718", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos112 (\\d+)$"))
async def xdos113(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/719", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos113 (\\d+)$"))
async def xdos114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/720", reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^xdos114 (\\d+)$"))
async def xdos114(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/botAlamy/721", reply_to_message_id=mid)


########################################################################################################################
########################################################################################################################

