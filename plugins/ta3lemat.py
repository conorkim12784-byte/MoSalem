from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from config import get_bot_information


async def ta3lemat(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("حمايه المجموعات", callback_data="hemayagroup " + str(m.from_user.id))] +
        [InlineKeyboardButton("حمايه القنوات", callback_data="hemayachannel " + str(m.from_user.id))],
        [InlineKeyboardButton("كيبورد الاعضاء", callback_data="keb3dw " + str(m.from_user.id))] +
        [InlineKeyboardButton("حذف حسابك", callback_data="deletacc " + str(m.from_user.id))],
        [InlineKeyboardButton("تفعيل البوت", callback_data="taf3elbot " + str(m.from_user.id))] +

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("◍ اهلا بيك بقائمه ارشادات الاستخدام او تعليمات السورس", reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^hemayagroup (\\d+)$"))
async def hemayagroup(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    ta3lemat_text = """💟 》مرحبا بك عزيزي
💟 》اليك معلومات استخدام حمايه مجموعات 🔔
• • { ⚡ @TALASHNY ⚡} • •
💟 》يمكنك استخدام البوت في حمايه مجموعتك من الفارسيه
• • { ⚡ @TALASHNY ⚡} • •
💟 》وايضا يمكنك من تفعيل الحمايه القصوي لتامين المجموعه من الاسبام والرسائل المزعجه
• • { ⚡ @TALASHNY ⚡} • •
• يمكنني ايضا ارسال الاغاني واوامر التسليه الاخري ⚡
"""
    await m.message.reply_text(ta3lemat_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^hemayachannel (\\d+)$"))
async def hemayachannel(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    ta3lemat_text = """💟 》مرحبا بك عزيزي
💟 》اليك معلومات استخدام حمايه القنوات 😱
• • { ⚡ @TALASHNY ⚡} • •
💟 》يمكنك استخدام البوت في حمايه قناتك من التصفيه
• • { ⚡ @TALASHNY ⚡} • •
💟 》وايضا يمكنك من تفعيل الاغاني في مكالمات الصوتيه ف قناتك
• • { ⚡ @TALASHNY ⚡} • •
• يمكنني ايضا ارسال الاغاني واوامر التسليه الاخري ⚡
"""
    await m.message.reply_text(ta3lemat_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^keb3dw (\\d+)$"))
async def keb3dw(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    ta3lemat_text = """💟 》كيبورد العضو
💟 》سيتم تشغيل كيبورد العضو في تحديد V3.9
• • { ⚡ @TALASHNY ⚡} • •
💟 》يمكنك من خلال كيبورد العضو التحكم في الاوامر التاليه :- 
• • { ⚡ @TALASHNY ⚡} • •
💟 》اختيار الاغاني التي تريدها { البحث في يوتيوب • قرائه الروايات • مشاهده الافلام و المسرحيات • الاستماع الي القران الكريم • قراءه الاذكار }
• • { ⚡ @TALASHNY ⚡} • •
💟 》تحميل الخلفيات والرمزيات { حذف حسابك }
"""
    await m.message.reply_text(ta3lemat_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^deletacc (\\d+)$"))
async def deletacc(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    ta3lemat_text = """💟 》 حذف حسابك الخاص بالتليجرام
💟 》سيتم توافر هذه الميزه في تحديث v3.9
• • { ⚡ @TALASHNY ⚡} • •
💟 》سيكون بامكانك حذف حسابك عن طريق ارسال امر /delet_me
• • { ⚡ @TALASHNY ⚡} • •
💟 》وهذا الامر يقون بحذف حسابك من التليجرام بشكل كامل
• • { ⚡ @TALASHNY ⚡} • •
احذر ياصديقي ! سيتم فقد جميع المحادثات والمعلومات الخاصه بك علي تليجرام
"""
    await m.message.reply_text(ta3lemat_text, reply_to_message_id=mid)


@Client.on_callback_query(filters.regex("^taf3elbot (\\d+)$"))
async def taf3elbot(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 💕", show_alert=True)
        return
    await m.message.delete()
    ta3lemat_text = """💟 》تفعيل البوت
💟 》كل ماعليك فعله لتفعيل البوت هو التالي :- 
• • { ⚡ @TALASHNY ⚡} • •
💟 》1 : اضف البوت الي مجموعتك
• • { ⚡ @TALASHNY ⚡} • •
💟 》2 : قم برفع البوت مشرف في المجموعه
• • { ⚡ @TALASHNY ⚡} • •
💟 》ملحوظه 》 عند رفع البوت مشرف في مجموعتك يقوم بتفعيل نفسه
"""
    await m.message.reply_text(ta3lemat_text, reply_to_message_id=mid)
    
