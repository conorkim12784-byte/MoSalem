from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

id = {}
@Client.on_message(filters.command(["المعجبين", "فنزاتي"], ""))
async def llo(client, message):
   text = "قائمة المعجبين\n"
   o = 0
   if not id.get(message.from_user.id) or len(id[message.from_user.id]) == 0:
      return await message.reply_text("لا يوجد لديك معجبين")
   for i in id[message.from_user.id]:
       o += 1
       text += f"{o}- {i}\n"
   return await message.reply_text(text)

@Client.on_callback_query(filters.regex("heart"))  
async def heart(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("heart", "")  
    username = int(callback_request)
    usr = await client.get_chat(username)
    if not query.from_user.mention in id[usr.id]:
         id[usr.id].append(query.from_user.mention)
         try:
            await client.send_message(usr.id, f"**قام هذا الشخص : {query.from_user.mention}**\n**بالاعجاب بالايدي الخاص بك**\nا**لايدي الخاص به : {query.from_user.id}**")
         except:
            pass
    else:
         id[usr.id].remove(query.from_user.mention)
         try:
            await client.send_message(usr.id, f"**قام هذا الشخص : {query.from_user.mention}**\n**بالغاء الاعجاب بالايدي الخاص بك**\nا**لايدي الخاص به : {query.from_user.id}**")
         except:
            pass
    idd = len(id[usr.id])
    await query.message.edit_replay_markup(reply_markup=InlineKeyboardMarkup(  
            [  
                [
                    InlineKeyboardButton(  
                        "• 𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝙻 𝙷𝙰𝙲𝙺𝙴𝚁 𖠶", url=f"https://t.me/source_hacker")  
                ],  
                [
                    InlineKeyboardButton("• 𝙸𝙳", callback_data=f"idc{usr.id}")] + [InlineKeyboardButton("• 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴", callback_data=f"usernamec{usr.id}")
                ],
                [
                    InlineKeyboardButton(  
                        "• 𝙽𝙰𝙼𝙴", callback_data=f"namec{usr.id}")
                ],           
            ]
        ),  
    )

@Client.on_callback_query(filters.regex("usernamec"))  
async def xxuser(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("usernamec", "")  
    username = int(callback_request) 
    if not query.from_user.id == username: 
       return await query.answer("لايمكنك طباعه معلومات شخص اخر : 💕", show_alert=True) 
    user = await client.get_chat(username) 
    username = f"معرفك هو : @{user.username}" if user.username else "ليس لديك معرف" 
    await query.message.reply_to_message.reply_text(username)  
@Client.on_callback_query(filters.regex("namec"))  
async def xxname(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("namec", "")  
    username = int(callback_request) 
    if not query.from_user.id == username: 
       return await query.answer("لايمكنك طباعه معلومات شخص اخر : 💕", show_alert=True) 
    user = await client.get_chat(username) 
    name = f"اسمك هو : `{user.first_name}`" if user.first_name else "اسم لديك اسم"  
    await query.message.reply_to_message.reply_text(name)  
@Client.on_callback_query(filters.regex("bioc"))  
async def xxbio(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("bioc", "")  
    username = int(callback_request) 
    if not query.from_user.id == username: 
       return await query.answer("لايمكنك طباعه معلومات شخص اخر : 💕", show_alert=True) 
    user = await client.get_chat(username) 
    user = f"البايو هو : `{user.bio}`" if user.bio else "ليس لديك بايو"  
    await query.message.reply_to_message.reply_text(user) 
@Client.on_callback_query(filters.regex("idc"))  
async def xxid(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("idc", "")  
    username = int(callback_request) 
    if not query.from_user.id == username: 
       return await query.answer("لايمكنك طباعه معلومات شخص اخر : 💕", show_alert=True) 
    username = f"ايديك هو : `{username}`" if username else "ليس لديك ايدي" 
    await query.message.reply_to_message.reply_text(username)  
@Client.on_message(  
    filters.command(["ايدي", "ا", "معلوماتك 💡"], "")  
)  
async def ssorh(client, message):  
    usr = await client.get_chat(message.from_user.id)  
    name = usr.first_name
    if not id.get(message.from_user.id):
       id[usr.id] = []
    idd = len(id[usr.id])
    photo = await client.download_media(usr.photo.big_file_id)  
    await client.send_photo(message.chat.id, photo=photo, caption=f"صورتك اهي متقرفناش يعم {message.from_user.first_name}", reply_to_message_id=message.message_id,  
    reply_markup=InlineKeyboardMarkup(  
            [  
                [
                    InlineKeyboardButton(  
                        "• 𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝙻 𝙷𝙰𝙲𝙺𝙴𝚁 𖠶", url=f"https://t.me/source_hacker")  
                ],  
                [
                    InlineKeyboardButton("• 𝙸𝙳", callback_data=f"idc{usr.id}")] + [InlineKeyboardButton("• 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴", callback_data=f"usernamec{usr.id}")
                ],
                [
                    InlineKeyboardButton("• 𝙽𝙰𝙼𝙴", callback_data=f"namec{usr.id}")] + [InlineKeyboardButton("• 𝙱𝙸𝙾", callback_data=f"bioc{usr.id}")
                ],           
            ]
        ),  
    )
@Client.on_callback_query(filters.regex("ph"))  
async def phh(client, query: CallbackQuery):  
    callback_data = query.data.strip()  
    callback_request = callback_data.replace("usernamec", "")
    username = int(callback_request) 
    if not query.from_user.id == username: 
       return await query.answer("لايمكنك طباعه معلومات شخص اخر : 💕", show_alert=True) 
    ii = query.message.reply_markup.inline_keyboard[6].text.replace("الصوره ", "")
    o = 0
    i = ii + 1
    photo = None
    async for photo in client.get_chat_photos(username):
         o += 1
         if o == i:
           photo = photo.file_id
    if not photo:
       return await query.answer("لا يوجد صور أخري", show_alert=True) 
    usr = await client.get_chat(username)
    await query.message.edit_message_media(InputMediaPhoto(photo), caption=f"صورتك اهي متقرفناش يعم {query.from_user.first_name}",
    reply_markup=InlineKeyboardMarkup(  
            [  
                [
                    InlineKeyboardButton(  
                        "• 𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝙻 𝙷𝙰𝙲𝙺𝙴𝚁 𖠶", url=f"https://t.me/source_hacker")  
                ],  
                [
                    InlineKeyboardButton("• 𝙸𝙳", callback_data=f"idc{usr.id}")] + [InlineKeyboardButton("• 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴", callback_data=f"usernamec{usr.id}")
                ],
                [
                    InlineKeyboardButton("• 𝙽𝙰𝙼𝙴", callback_data=f"namec{usr.id}")] + [InlineKeyboardButton("• 𝙱𝙸𝙾", callback_data=f"bioc{usr.id}")
                ],           
            ]
        ),  
    )
