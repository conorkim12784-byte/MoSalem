from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

################################
## Dev By: TALASHNY ##
################################

@Client.on_callback_query(filters.regex("^command (\\d+)$"))
async def command(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🛡️ الحماية", callback_data="m1 " + str(m.from_user.id)),
         InlineKeyboardButton("🎮 التسلية", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("👥 الأعضاء", callback_data="m3 " + str(m.from_user.id)),
         InlineKeyboardButton("⭐ الرتب", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("👨‍💻 المطورين", callback_data="m6 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.reply_text("""
⌔︙اوامــر البــوت الرئيسيـة 
—————————————
⌔︙🛡️ اوامــر الحمايـه
⌔︙🎮 اوامــر التسليه
⌔︙👥 اوامــر الاعضاء
⌔︙⭐ اوامـر اصحاب الرتب
⌔︙👨‍💻 اوامر المطورين

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^command2 (\\d+)$"))
async def command2(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🛡️ الحماية", callback_data="m1 " + str(m.from_user.id)),
         InlineKeyboardButton("🎮 التسلية", callback_data="m2 " + str(m.from_user.id))],
        [InlineKeyboardButton("👥 الأعضاء", callback_data="m3 " + str(m.from_user.id)),
         InlineKeyboardButton("⭐ الرتب", callback_data="m4 " + str(m.from_user.id))],
        [InlineKeyboardButton("👨‍💻 المطورين", callback_data="m6 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("""
⌔︙اوامــر البــوت الرئيسيـة 
—————————————
⌔︙🛡️ اوامــر الحمايـه
⌔︙🎮 اوامــر التسليه
⌔︙👥 اوامــر الاعضاء
⌔︙⭐ اوامـر اصحاب الرتب
⌔︙👨‍💻 اوامر المطورين

""", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m1 (\\d+)$"))
async def m1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("""
⌔︙اوامر الحمايه كالاتي ...
—————————————
⌔︙قفل ، فتح ← الامر 
⌔︙تستطيع قفل حمايه كما يلي ...
⌔︙← { بالتقييد ، بالطرد ، بالكتم }
—————————————
⌔︙الكل ~ الدخول
⌔︙الروابط ~ المعرف
⌔︙التاك ~ الشارحه
⌔︙التعديل ~ تعديل الميديا
⌔︙المتحركه ~ الملفات
⌔︙الصور ~ الفيديو 
—————————————
⌔︙الماركداون ~ البوتات
⌔︙التكرار ~ الكلايش
⌔︙السيلفي ~ الملصقات
⌔︙الانلاين ~ الدردشه
⌔︙الهمسه
—————————————
⌔︙التوجيه ~ الاغاني
⌔︙الصوت ~ الجهات
⌔︙الاشعارات ~ التثبيت 
⌔︙الوسائط ~ التفليش
⌔︙وسائط المميزين
⌔︙الفشار ~ ارسال القناة
⌔︙القنوات ~ الموقع
—————————————
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mxx (\\d+)$"))
async def mxx(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("1⃣ التسلية الأولى", callback_data="mx1 " + str(m.from_user.id)),
         InlineKeyboardButton("2⃣ التسلية الثانية", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text(" ⌔︙ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m2 (\\d+)$"))
async def m2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("1⃣ التسلية الأولى", callback_data="mx1 " + str(m.from_user.id)),
         InlineKeyboardButton("2⃣ التسلية الثانية", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text(" ⌔︙ اهلا بك فى اوامر التسليه\n√", reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^mx1 (\\d+)$"))
async def mx1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("➡️ التالي", callback_data="mx2 " + str(m.from_user.id))],
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("""⌔︙ ❬ م2 ❭ 1⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
━─━──━━━──━─━
⌔︙ متوحد «» متوحده
💬╢ تاج للمتوحدين 
📎╜ مسح المتوحدين
━─━──━━━──━─━
💢╖ بقره 
💬╢ تاج للبقرات
📎╜ مسح البقرات
━─━──━━━──━─━
🐒╖ غبي
💬╢ تاج للاغبيه
📎╜ مسح الاغبيه
━─━──━━━──━─━
🤪╖ حمار
💬╢ تاج للحمير
📎╜ مسح الحمير
━─━──━━━──━─━
🐕╖ كلب
💬╢ تاج للكلاب
📎╜ مسح الكلاب
━─━──━━━──━─━
🐰╖ قرد
💬╢ تاج للقرود
📎╜ مسح القرود
━─━──━━━──━─━
🤡╖ فرسه
💬╢ تاج للفرسات
📎╜ مسح الفرسات
━─━──━━━──━─━
🤰╖ عره
💬╢ تاج للعرر
📎╜ مسح العرر
━─━──━━━──━─━
👰╖ زوجتي
💬╢ تاج للزوجات
📎╜ مسح المتزوجات
━─━──━━━──━─━
👩‍❤️‍👨╖ زواج «» طلاق
💬╢ تاج للمتزوجين 
📎╜ مسح المتزوجين
━─━──━━━──━─━
💘╖ رفع بقلبي «» تنزيل من قلبي
💬╢ تاج للي بقلبي
📎╜ مسح من قلبي
━─━──━━━──━─━
🙊╖ بيستي 
💬╢ تاج للبيست
📎╜ مسح البيستيه
━─━──━━━──━─━

    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^mx2 (\\d+)$"))
async def mx2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="mxx " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("""⌔︙ ❬ م2 ❭ 2⃣ اوامر التسليه ⇊
🔐╜ رفع «» تنزيل + الامر 
━─━──━━━──━─━
⌔︙ وتكه
💬╢ تاج للوتكات 
📎╜ مسح الوتكات
━─━──━━━──━─━
💢╖ رقاصه 
💬╢ تاج للرقاصات
📎╜ مسح الرقاصات
━─━──━━━──━─━
🐒╖ مهزء
💬╢ تاج للمهزئين
📎╜ مسح المهزئين
━─━──━━━──━─━
🤪╖ حيوان
💬╢ تاج للحيوانات
📎╜ الحيوانات 
━─━──━━━──━─━
🐕╖ فاشل
💬╢ تاج للفشله
📎╜ مسح الفشله
━─━──━━━──━─━
🐰╖ دكري
💬╢ تاج للدكور
📎╜ مسح الدكور
━─━──━━━──━─━
🤡╖ قطتي
💬╢ تاج للقطط
📎╜ مسح القطط
━─━──━━━──━─━
🤰╖ ابني
💬╢ تاج للابناء
📎╜ مسح الابناء
━─━──━━━──━─━
👰╖ بنتي
💬╢ تاج للبنوتات
📎╜ مسح البنوتات
━─━──━━━──━─━
👩‍❤️‍👨╖ حبيبي
💬╢ تاج للحبايب 
📎╜ مسح الحبايب
━─━──━━━──━─━
💘╖ زوجي
💬╢ تاج للازواج
📎╜ مسح الازواج
━─━──━━━──━─━
🙊╖ زوجتي 
💬╢ تاج للزوجات
📎╜ مسح الزوجات
━─━──━━━──━─━
👰╖ خاين
💬╢ تاج للخونه
📎╜ مسح الخونه
━─━──━━━──━─━
👩‍❤️‍👨╖ خاينه
💬╢ تاج للخاينين 
📎╜ مسح الخاينين
━─━──━━━──━─━
💘╖ عبيط
💬╢ تاج للعبط
📎╜ مسح العبط
━─━──━━━──━─━
🙊╖ متخزوق 
💬╢ تاج للمتخزوقين
📎╜ مسح المتخزوقين
━─━──━━━──━─━

    """, reply_markup=keyboard)

@Client.on_callback_query(filters.regex("^m3 (\\d+)$"))
async def m3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("""
⌔︙اوامر الاعضاء في المجموعه
—————————————
⌔︙رفع ، تنزيل ← ادمن
⌔︙الادمنيه ← مسح الادمنيه
⌔︙رفع الادمنيه 
⌔︙تنزيل الكل ← {بالرد ، بالمعرف}
⌔️︙كشف ، طرد ، قفل ← البوتات
⌔︙قفل البوتات ← بالطرد
⌔︙فحص ← البوت
⌔︙طرد ← المحذوفين 
⌔︙قفل فتح ← القنوات
⌔︙مسح التعديل 
—————————————
⌔︙اضف ، مسح تاك
⌔︙قائمه تاك الاسم
⌔︙مسح قائمه تاك الاسم
—————————————
⌔︙حظر ، طرد اسم + الاسم
⌔︙الغاء حظر اسم + الاسم 
⌔︙الاسماء المحظوره
⌔︙مسح الاسماء المحظوره
—————————————
⌔︙وضع الرتب ← { بالرد ، بالمعرف}
⌔︙ضع رتبه ← { اسم الرتبه }
⌔︙مسح رتبه ← { بالرد ، بالمعرف}
—————————————
⌔︙وضع ، ضع ← الاوامر التاليه
⌔︙اسم + اسم المجموعه
⌔︙رابط ، صوره
⌔︙قوانين ، وصف ،الترحيب 
—————————————
⌔︙مسح الرابط ، انشاء رابط
⌔︙تفعيل ، تعطيل الرابط العادي 
—————————————
⌔︙تفعيل ، تعطيل ← التالي :
⌔︙الايدي ، الايدي بالصوره
⌔︙ايدي العضو ، البايو , الرابط
⌔︙الترحيب ، منشن ، انطق
⌔︙صورتي ، اسمي ؛ نبذه
⌔︙الردود ، الابراج ، التفاعل
⌔︙غنيلي ، شعر ، قصيده 
⌔︙صوره ، متحركه ، الصيغ ، قول 
⌔︙الصوتيات ، الصوتيات العامه
⌔︙الاذكار ، وظيفته :(ارسال اذكار كل 1 ساعه)
—————————————
⌔︙مسح ← + { الامر } 
⌔︙المحظورين ، المطرودين
⌔︙المكتومين ← المقيدين
—————————————
⌔︙ترتيب الاوامر ← استعاده الاوامر
⌔︙اضف ، مسح ← { رد }
⌔︙الردود ، قائمه الردود 
⌔︙مسح الردود
⌔︙اضف ، مسح ← { رد متعدد}
⌔︙الردود المتعدده
⌔︙مسح الردود المتعدده
⌔︙اضف مسح رد انلاين 
⌔︙الردود انلاين
⌔︙مسح الردود انلاين
⌔︙تفعيل تعطيل الردود انلاين
⌔︙تاك عام ، all
⌔︙الكلمه + @all
⌔︙جهاتي «» حذف جهاتي
⌔︙اطردني «» اكتمني
⌔︙سورس «» المطور
⌔︙رتبتي «» كشف
⌔︙بوسو «» بوسها
⌔︙رابط الحذف
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m4 (\\d+)$"))
async def m4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("""
⌔︙ ❬ م4 ❭ اوامر اصحاب الرتب ⇊
⌔︙ الادمن «» المنشئ «» المالك
—————————————
⌔︙ « المميز » ⇊
—————————————
⌔︙ كشف
⌔︙ المحظورين
⌔︙ المكتومين
—————————————
 « الادمن » ⇊
—————————————
⌔︙ رفع مميز «» تنزيل مميز
⌔︙ الترحيب
⌔︙ اضف مغادره «» مسح المغادره
⌔︙ رساله المغادره
⌔︙ كشف البوتات
⌔︙ المميزين «» حذف المميزين
⌔︙ حظر «» الغاء حظر
⌔︙ كتم «» الغاء كتم
⌔︙ حظر لمده + المده
⌔︙ كتم لمده + المده
⌔︙ طرد «» تطهير 
⌔︙ تثبيت «» تثبيت بدون اشعار
⌔︙ الغاء تثبيت الكل
⌔︙ ❬ + ❭ جميع ماسبق
—————————————
⌔︙ « المنشئ » ⇊
—————————————
⌔︙ رفع «» تنزيل ادمن
⌔︙ اضف «» حذف  ❬ رد ❭
⌔︙ الردود «» حذف الردود
⌔︙ ايقاف المنشن
⌔︙ تعيين «» مسح  ❬ الايدي ❭
⌔︙ الادمنيه «» حذف الادمنيه
⌔︙ اضف ترحيب
⌔︙ حذف المحظورين «» المكتومين
⌔︙ منع + الكلمه
⌔︙ الغاء منع + الكلمه
⌔︙ حذف الكلمات الممنوعه
⌔︙ المميزين عام
—————————————
⌔︙ « المالك » ⇊ اوامر
—————————————
⌔︙ اضف صوره «» وصف (للجروب)
⌔︙ رفع منشئ «» تنزيل منشئ
⌔︙ تاج للاعضاء «» للكل
⌔︙ اضف رابط «» مسح الرابط
⌔︙ اضف «» حذف  ❬ امر ❭
⌔︙ الاوامر المضافه
⌔︙ حذف الاوامر المضافه
⌔︙ اضف اسم «» تحديث
⌔︙ المنشئين «» حذف المنشئين
    """, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^m6 (\\d+)$"))
async def m6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("🔙 القائمه الرئيسيه", callback_data="command2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text("""
⌔︙ ❬ م6 ❭ اوامر المطورين ⇊
⌔︙ « المطور » ⇊
—————————————
⌔︙ رفع «» تنزيل ❬ مالك ❭
⌔︙ تغيير رابط الجروب
⌔︙ اذاعه بالمجموعات
⌔︙ اذاعه بالتوجيه للمجموعات
⌔︙ اذاعه موجهه بالتثبيت
⌔︙ اذاعه خاص
⌔︙ اذاعه بالتوجيه خاص
⌔︙ اذاعه بالتثبيت
⌔︙ جلب نسخه احتياطيه
⌔︙ رفع نسخه احتياطيه
⌔︙ الاحصائيات
⌔︙ حذف المالكين
⌔︙ ❬ + ❭ جميع ماسبق
—————————————
⌔︙ « المطور الاساسي » ⇊
—————————————
⌔︙ اضف «» حذف رد عام
⌔︙ رفع «» تنزيل ❬ مميز عام ❭
⌔︙ مسح المميزين عام
⌔︙ الردود العامه
⌔︙ حذف الردود العامه
⌔︙ اذاعه بالتوجيه خاص
⌔︙ اذاعه بالتوجيه للمجموعات
⌔︙ اذاعه بالتثبيت
⌔︙ اذاعه موجهه بالتثبيت
⌔︙ جلب «» رفع ❬نسخه احتياطيه❭
⌔︙ الاحصائيات
⌔︙ رفع «» تنزيل ❬ مطور ❭
⌔︙ المطورين «» حذف المطورين
⌔︙ ضع اسم للبوت
⌔︙ تغيير رساله المغادره
⌔︙ حظر «» كتم  ❬ عام ❭
⌔︙ المكتومين  عام 
⌔︙ المحظورين عام
⌔︙ الغاء العام
—————————————
    """, reply_markup=keyboard)
