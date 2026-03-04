import random
import re
from pyrogram import Client
from pyrogram.types import Message
from database import get_db_addcustomid, get_db_mypointgame, get_db_mymessage, get_db_mycontact
from localization import use_chat_lang
from config import get_bot_information
from plugins.admin import get_available_adminstrator
from plugins.rtp_function import get_Rank


def get_mycontact(m):
    if get_db_mycontact(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mycontact(m.from_user.id, m.chat.id)
    return num


def get_mypoint(m):
    if get_db_mypointgame(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mypointgame(m.from_user.id, m.chat.id)
    return num


def get_mymessage(m):
    if get_db_mymessage(m.from_user.id, m.chat.id) is None:
        num = 0
    else:
        num = get_db_mymessage(m.from_user.id, m.chat.id)
    return num


def get_mymessage_interaction(m):
    interaction_msg = ''
    if m < 100:
        interaction_msg = 'غير متفاعل 😒'
    else:
        if m < 200:
            interaction_msg = 'متفاعل ضعيف 😞'
        else:
            if m < 400:
                interaction_msg = 'تفاعلك ضعيف ليش 😕'
            else:
                if m < 700:
                    interaction_msg = 'تفاعل موحلو 😤'
                else:
                    if m < 1200:
                        interaction_msg = 'شبه متفاعل 🙊🥺'
                    else:
                        if m < 2000:
                            interaction_msg = 'متفاعل جدا 😂'
                        else:
                            if m < 3500:
                                interaction_msg = 'معشش فى الجروب 🔥😹'
                            else:
                                if m < 4000:
                                    interaction_msg = 'متفاعل نار 🔥😁'
                                else:
                                    if m < 4500:
                                        interaction_msg = 'قمة التفاعل ☺️'
                                    else:
                                        if m < 5500:
                                            interaction_msg = 'ملك التفاعل 😼'
                                        else:
                                            if m < 7000:
                                                interaction_msg = 'قنبله تفاعل 🌟'
                                            else:
                                                if m < 9500:
                                                    interaction_msg = 'امبروطور التفاعل 😉'
                                                else:
                                                    if m < 10000000000:
                                                        interaction_msg = 'تفاعل نار وشرار 🔥🖤'
    return interaction_msg


@use_chat_lang()
async def ids_private(c: Client, m: Message, strings):
    user_data = m.from_user
    await m.reply_text(strings("info_private").format(
                           first_name=user_data.first_name,
                           last_name=user_data.last_name or "",
                           username="@" + user_data.username if user_data.username else strings("none"),
                           user_id=user_data.id,
                           user_dc=user_data.dc_id or strings("unknown"),
                           lang=user_data.language_code or strings("unknown"),
                           chat_type=m.chat.type
                       ))


async def ids_default(c: Client, m: Message, strings):
    randomtext = [
        'ملاك وعسل ياناس 😟',
        "خايف عليك ☹️ ",
        "احسن صوره 🐼❤️",
        "كيكك والله🥺",
        "بحب هاى الصوره🥺",
        "غير هيى الصوره الان😒",
        "بطل نتانه بقالك كام سنه حاطط الصوره دى😒"
    ]
    if m.reply_to_message:
        user_data = m.reply_to_message.from_user
        user_data2 = m.reply_to_message
    else:
        user_data = m.from_user
        user_data2 = m

    if user_data.first_name:
        first_name = user_data.first_name + " "
    else:
        first_name = " "
    if user_data.last_name:
        last_name = user_data.last_name
    else:
        last_name = ""

    if user_data.username:
        username = user_data.username
    else:
        username = "لايوجد"

    check = await get_available_adminstrator(c, m)
    if check[0]:
        adminrom = "مشرف"
    else:
        adminrom = "عضو"

    medooid = f"""
عذراً عزيزي انت لا تمتلك صورة او أنك قمت بحظر البوت اضغط استارت [هنا](tg://user?id={get_bot_information()[0]}) وتاكد

💎╖ ايدِيڪ ⇇ `{user_data.id}`
🐣╢ اسمڪ ⇇ `{first_name + last_name}`
☀️╢ يوزرڪ ⇇ @{username}
🎈╢ نقاطك ⇇ *{get_mypoint(m)}*
👁╢ رسائلك ⇇ *{get_mymessage(m)}*
👥╢ جهاتك ⇇ *{get_mycontact(m)}*
🏅╢ تفاعلك ⇇ {get_mymessage_interaction(get_mymessage(m))}
👮‍♂️╢ رتبتڪ بالبـوت ⇇ {await get_Rank(user_data2)}
🌍╢ رتبتڪ بالـروم ⇇ {adminrom}
💬╜ رسـائل الجـرۆب ⇇ *{m.message_id + 1}*
        """

    medooid2 = f"""
{random.choice(randomtext)}
💎╖ ايدِيڪ ⇇ `{user_data.id}`
🐣╢ اسمڪ ⇇ `{first_name + last_name}`
☀️╢ يوزرڪ ⇇ @{username}
🎈╢ نقاطك ⇇ *{get_mypoint(m)}*
👁╢ رسائلك ⇇ *{get_mymessage(m)}*
👥╢ جهاتك ⇇ *{get_mycontact(m)}*
🏅╢ تفاعلك ⇇ {get_mymessage_interaction(get_mymessage(m))}
👮‍♂️╢ رتبتڪ بالبـوت ⇇ {await get_Rank(user_data2)}
🌍╢ رتبتڪ بالـروم ⇇ {adminrom}
💬╜ رسـائل الجـرۆب ⇇ *{m.message_id + 1}*
            """

    elnagarid = f"""
💎╖ ايدِيڪ ⇇ `{user_data.id}`
🐣╢ اسمڪ ⇇ `{first_name + last_name}`
☀️╢ يوزرڪ ⇇ @{username}
🎈╢ نقاطك ⇇ *{get_mypoint(m)}*
👁╢ رسائلك ⇇ *{get_mymessage(m)}*
👥╢ جهاتك ⇇ *{get_mycontact(m)}*
🏅╢ تفاعلك ⇇ {get_mymessage_interaction(get_mymessage(m))}
👮‍♂️╢ رتبتڪ بالبـوت ⇇ {await get_Rank(user_data2)}
🌍╢ رتبتڪ بالـروم ⇇ {adminrom}
💬╜ رسـائل الجـرۆب ⇇ *{m.message_id + 1}*
            """

    if not await c.get_profile_photos(user_data.id, limit=1):
        await m.reply_text(medooid, parse_mode="Markdown")

    async for photo in c.iter_profile_photos(user_data.id, limit=1):
        await m.reply_photo(photo.file_id, caption=medooid2, parse_mode="Markdown")


async def ids(c: Client, m: Message):
    if get_db_addcustomid(m.chat.id) is None:
        await ids_default(c, m)
    else:
        for per in get_db_addcustomid(m.chat.id):
            if per[1] == m.chat.id:
                randomtext = [
                    'ملاك وعسل ياناس 😟',
                    "خايف عليك ☹️ ",
                    "احسن صوره 🐼❤️",
                    "كيكك والله🥺",
                    "بحب هاى الصوره🥺",
                    "غير هيى الصوره الان😒",
                    "بطل نتانه بقالك كام سنه حاطط الصوره دى😒"
                ]
                if m.reply_to_message:
                    user_data = m.reply_to_message.from_user
                    user_data2 = m.reply_to_message
                else:
                    user_data = m.from_user
                    user_data2 = m

                if user_data.first_name:
                    first_name = user_data.first_name + " "
                else:
                    first_name = " "
                if user_data.last_name:
                    last_name = user_data.last_name
                else:
                    last_name = ""

                if user_data.username:
                    username = user_data.username
                else:
                    username = "لايوجد"

                check = await get_available_adminstrator(c, m)
                if check[0]:
                    adminrom = "مشرف"
                else:
                    adminrom = "عضو"
                a = re.sub("#rdphoto", random.choice(randomtext), per[0])
                a = re.sub("#fname", str(first_name), a)
                a = re.sub("#lname", str(last_name), a)
                a = re.sub("#id", str(m.from_user.id), a)
                a = re.sub("#user", "@" + str(username), a)
                a = re.sub("#mention", f"[{first_name + last_name}](tg://user?id={m.from_user.id})", a)
                a = re.sub("#game", str(get_mypoint(m)), a)
                a = re.sub("#msgs", str(get_mymessage(m)), a)
                a = re.sub("#contact", str(get_mycontact(m)), a)
                a = re.sub("#auto", str(get_mymessage_interaction(get_mymessage(m))), a)
                a = re.sub("#brank", str(await get_Rank(user_data2)), a)
                a = re.sub("#grank", str(adminrom), a)
                a = re.sub("#gmsgs", str(m.message_id + 1), a)

                if not await c.get_profile_photos(user_data.id, limit=1):
                    await m.reply_text(a, parse_mode="Markdown")
                    return

                async for photo in c.iter_profile_photos(user_data.id, limit=1):
                    await m.reply_photo(photo.file_id, caption=a, parse_mode="Markdown")
                    return
        await ids_default(c, m)
