import json
import random
import requests
from pyrogram import Client
from pyrogram.types import Message
from database import del_db_wait, set_db_wait, set_db_greply, del_db_greply, set_db_botname, set_db_replygroup, \
    del_db_replygroup, set_db_addlinkgroup, set_db_addwelcomegroup, set_db_addbyegroup, del_db_addcommand, \
    set_db_addcommand, del_db_addcustomid, set_db_addcustomid, set_db_mypointgame, set_db_mymessage
from plugins.general import wait_test
from plugins.ids import get_mypoint
from plugins.keyboard_private import broadcast_group, broadcast_user, broadcast_forward_group, broadcast_forward_user, \
    broadcast_pin_user, broadcast_forward_pin_user
from plugins.sudos import restart
from plugins.youtube import ntagyoutube, downfromlink, youttsearch, youttsearch_video
from plugins.zhrafa import zahrafa


async def wait_all(c: Client, m: Message):
    try:
        if wait_test(m, "addgreply"):
            if m.text == "الغاء":
                del_db_wait("addgreply")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("addgreply")
            global qrw
            qrw = m.text
            await m.reply_text("⌔ ارسل الان الرد على هذه الكلمه\n√", reply_to_message_id=m.message_id)
            set_db_wait("addgreply2", m.from_user.id, m.chat.id)
            return

        if wait_test(m, "addgreply2"):
            del_db_wait("addgreply2")
            b = m.text
            if m.text:
                b = m.text
            if m.photo:
                b = m.photo.file_id + ".png"
            if m.sticker:
                b = m.sticker.file_id + ".webp"
            if m.document:
                b = m.document.file_id + ".pdf"
            if m.animation:
                b = m.animation.file_id + ".gif"
            if m.video:
                b = m.video.file_id + ".mp4"
            if m.audio:
                b = m.audio.file_id + ".mp3"
            if m.voice:
                b = m.voice.file_id + ".ogg"
            set_db_greply(qrw, b)
            await m.reply_text("⌔ تم اضافه الرد بنجاح\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "delgreply"):
            del_db_wait("delgreply")
            del_db_greply(m.text)
            await m.reply_text("⌔ تم حذف الكلمه بنجاح من الردود العامه\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "addreplygroup"):
            if m.text == "الغاء":
                del_db_wait("addreplygroup")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("addreplygroup")
            global qrw2
            qrw2 = m.text
            await m.reply_text("⌔ ارسل الان الرد على هذه الكلمه\n√", reply_to_message_id=m.message_id)
            set_db_wait("addreplygroup2", m.from_user.id, m.chat.id)
            return

        if wait_test(m, "addreplygroup2"):
            del_db_wait("addreplygroup2")
            b = m.text
            if m.text:
                b = m.text
            if m.photo:
                b = m.photo.file_id + ".png"
            if m.sticker:
                b = m.sticker.file_id + ".webp"
            if m.document:
                b = m.document.file_id + ".pdf"
            if m.animation:
                b = m.animation.file_id + ".gif"
            if m.video:
                b = m.video.file_id + ".mp4"
            if m.audio:
                b = m.audio.file_id + ".mp3"
            if m.voice:
                b = m.voice.file_id + ".ogg"
            set_db_replygroup(qrw2, b, m.chat.id)
            await m.reply_text("⌔ تم اضافه الرد بنجاح\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "delreplygroup"):
            del_db_wait("delreplygroup")
            del_db_replygroup(m.text, m.chat.id)
            await m.reply_text("⌔ تم حذف الكلمه بنجاح من الردود\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "namebot"):
            if m.text == "الغاء":
                del_db_wait("namebot")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("namebot")
            set_db_botname(m.text)
            await m.reply_text("⌔ تم تغيير اسم البوت\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "saraha"):
            del_db_wait("saraha")
            sarahareplay = [
                "كدااب اوى🙄😒",
                "الكلام ده مظبوط🙂😹",
                "ڪلُآمك صادق 💘",
                "فعلا كل الي كلته صح 😁💋",
                "عينى فى عينك كده👀🌚",
                "اى الكدب ده😔💔",
                "احس هل شي كذب 🌚💕"
            ]
            await m.reply_text(random.choice(sarahareplay), reply_to_message_id=m.message_id)
            return

        if wait_test(m, "kshfelkzb"):
            del_db_wait("kshfelkzb")
            kshfelkzp = [
                "الكلام ده كلو كدب🙄😒",
                "الكلام ده مظبوط🙂😹",
                "اه حصل وابصم بالعشره💘",
                "الكلام اللى بتقولو ده جى من مصدر موثوق واكدلك على كده كمان❤️😂",
                "عايز اقلك الكلام ده كدب واللى قالولك كداب وانت كداب واللى بيتفرج كمان كداب🤝😂",
                "فعلا كل الي قلتو صح 😁💋",
                "الكلام ده برجوله وموثق كمان❤️😁",
                "اما قله ادب صحيح كلو كدب فى كدب😔💔",
                "اووه يااه ابغى اقلك كل ده كدب👀🌚",
                "اى الكدب ده😔💔",
                "احس هل شي كذب🌚💕"
            ]
            await m.reply_text(random.choice(kshfelkzp), reply_to_message_id=m.message_id)
            return

        if wait_test(m, "nsptelhob"):
            del_db_wait("nsptelhob")
            nsptelhob = [
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
                "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
                "41", "42", "43", "44", "45", "46", "47", "48", "49", "50",
                "51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
                "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
                "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
                "81", "82", "83", "84", "85", "86", "87", "88", "89", "90",
                "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"
            ]
            await m.reply_text(" نسبه الحب بينكم هى ~⪼ " + random.choice(nsptelhob) + " ❤️🙄",
                               reply_to_message_id=m.message_id)
            return

        if wait_test(m, "addlinkgroup"):
            if m.text == "الغاء":
                del_db_wait("addlinkgroup")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("addlinkgroup")
            set_db_addlinkgroup(m.text, m.chat.id)
            await m.reply_text("⌔ تم تغيير لينك الجروب\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "addwelcomegroup"):
            if m.text == "الغاء":
                del_db_wait("addwelcomegroup")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("addwelcomegroup")
            set_db_addwelcomegroup(m.text, m.chat.id)
            await m.reply_text("⌔ تم تغيير ترحيب الجروب\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "addbyegroup"):
            if m.text == "الغاء":
                del_db_wait("addbyegroup")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("addbyegroup")
            set_db_addbyegroup(m.text, m.chat.id)
            await m.reply_text("⌔ تم تغيير رساله مغادره الجروب\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "calcomrak"):
            try:
                del_db_wait("calcomrak")
                r = requests.get("https://immense-fjord-82492.herokuapp.com/omr.php?birthDate=" + m.text)
                rj = r.json()
                x = f"""
        🔎╖ بص بقا يازميلى عمرك:
        🌐╢ {str(rj["year"])} سنه و {str(rj["month"])} شهور و {str(rj["day"])} يوم
        🔊╢ انت عِشت {str(rj["days"])} يوم
        ✨╢ انت عِشت {str(rj["hours"])} ساعه
        🀄️╢ انت عِشت {str(rj["minutes"])} دقيقه
        ♨️╜ انت عِشت {str(rj["seconds"])} ثانيه
                                 """
                await m.reply_text(x, reply_to_message_id=m.message_id)
                return
            except Exception as e:
                await m.reply_text(str(e) + "\n\n" +
                                   "سبب ظهور هذا الخطأ لم يستطع البوت الوصول لايدي الشخص تاكد من ان هذا الحساب ليس مخفى وجرب مره اخرى",
                                   reply_to_message_id=m.message_id, parse_mode="Markdown")

        if wait_test(m, "zhrfa"):
            del_db_wait("zhrfa")
            await zahrafa(c, m)
            return

        if wait_test(m, "ntagyoutube"):
            del_db_wait("ntagyoutube")
            await ntagyoutube(m)
            return

        if wait_test(m, "downyout"):
            del_db_wait("downyout")
            await downfromlink(m)
            return

        if wait_test(m, "searchyout"):
            del_db_wait("searchyout")
            await youttsearch(m)
            return

        if wait_test(m, "searchyoutvideo"):
            del_db_wait("searchyoutvideo")
            await youttsearch_video(m)
            return

        if wait_test(m, "gbroadcast"):
            if m.text == "الغاء ⁦🛠️⁩" or m.text == "الغاء":
                del_db_wait("gbroadcast")
                await m.reply_text("⌔ تم الغاء الاذاعه بنجاح\n√", reply_to_message_id=m.message_id)
                return
            else:
                del_db_wait("gbroadcast")
                u = await m.reply_text("⌔ جارى عمل اذاعه انتظر...\n√", reply_to_message_id=m.message_id)
                b = await broadcast_group(c, m, m.text)
                await u.delete()
                await m.reply_text("⌔ تم الاذاعه الى " + str(b) + " من المجموعات\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "ubroadcast"):
            if m.text == "الغاء ⁦🛠️⁩" or m.text == "الغاء":
                del_db_wait("ubroadcast")
                await m.reply_text("⌔ تم الغاء الاذاعه بنجاح\n√", reply_to_message_id=m.message_id)
                return
            else:
                del_db_wait("ubroadcast")
                u = await m.reply_text("⌔ جارى عمل اذاعه انتظر...\n√", reply_to_message_id=m.message_id)
                b = await broadcast_user(c, m, m.text)
                await u.delete()
                await m.reply_text("⌔ تم الاذاعه الى " + str(b) + " من الاشخاص\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "gforwardbroadcast"):
            if m.text == "الغاء ⁦🛠️⁩" or m.text == "الغاء":
                del_db_wait("gforwardbroadcast")
                await m.reply_text("⌔ تم الغاء الاذاعه بنجاح\n√", reply_to_message_id=m.message_id)
                return
            else:
                del_db_wait("gforwardbroadcast")
                u = await m.reply_text("⌔ جارى عمل اذاعه انتظر...\n√", reply_to_message_id=m.message_id)
                b = await broadcast_forward_group(c, m)
                await u.delete()
                await m.reply_text("⌔ تم الاذاعه الى " + str(b) + " من المجموعات\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "uforwardbroadcast"):
            if m.text == "الغاء ⁦🛠️⁩" or m.text == "الغاء":
                del_db_wait("uforwardbroadcast")
                await m.reply_text("⌔ تم الغاء الاذاعه بنجاح\n√", reply_to_message_id=m.message_id)
                return
            else:
                del_db_wait("uforwardbroadcast")
                u = await m.reply_text("⌔ جارى عمل اذاعه انتظر...\n√", reply_to_message_id=m.message_id)
                b = await broadcast_forward_user(c, m)
                await u.delete()
                await m.reply_text("⌔ تم الاذاعه الى " + str(b) + " من الاشخاص\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "gpinbroadcast"):
            if m.text == "الغاء ⁦🛠️⁩" or m.text == "الغاء":
                del_db_wait("gpinbroadcast")
                await m.reply_text("⌔ تم الغاء الاذاعه بنجاح\n√", reply_to_message_id=m.message_id)
                return
            else:
                del_db_wait("gpinbroadcast")
                u = await m.reply_text("⌔ جارى عمل اذاعه انتظر...\n√", reply_to_message_id=m.message_id)
                b = await broadcast_pin_user(c, m)
                await u.delete()
                await m.reply_text("⌔ تم الاذاعه الى " + str(b) + " من المجموعات\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "uforwardpinbroadcast"):
            if m.text == "الغاء ⁦🛠️⁩" or m.text == "الغاء":
                del_db_wait("uforwardpinbroadcast")
                await m.reply_text("⌔ تم الغاء الاذاعه بنجاح\n√", reply_to_message_id=m.message_id)
                return
            else:
                del_db_wait("uforwardpinbroadcast")
                u = await m.reply_text("⌔ جارى عمل اذاعه انتظر...\n√", reply_to_message_id=m.message_id)
                b = await broadcast_forward_pin_user(c, m)
                await u.delete()
                await m.reply_text("⌔ تم الاذاعه الى " + str(b) + " من المجموعات\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "addphotogroup"):
            if m.text == "الغاء":
                del_db_wait("addphotogroup")
                return
            if m.text:
                await m.reply_text("⌔ من فضلك ارسل لى صوره وليس كلام\n√", reply_to_message_id=m.message_id)
                return
            if m.photo:
                del_db_wait("addphotogroup")
                await c.set_chat_photo(m.chat.id, photo=m.photo.file_id)
                await m.reply_text("⌔ تم تغير صوره الجروب\n√", reply_to_message_id=m.message_id)
                return
            if m.video:
                del_db_wait("addphotogroup")
                await c.set_chat_photo(m.chat.id, video=m.video.file_id)
                await m.reply_text("⌔ تم تغير صوره الجروب الى فديو\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "adddescreptiongroup"):
            if m.text == "الغاء":
                del_db_wait("adddescreptiongroup")
                return
            del_db_wait("adddescreptiongroup")
            if m.text:
                await c.set_chat_description(m.chat.id, m.text)
                await m.reply_text("⌔ تم تغير وصف الجروب\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "addnamegroup"):
            if m.text == "الغاء":
                del_db_wait("addnamegroup")
                return
            del_db_wait("addnamegroup")
            if m.text:
                await c.set_chat_title(m.chat.id, m.text)
                await m.reply_text("⌔ تم تغير اسم الجروب\n√", reply_to_message_id=m.message_id)
                return

        if wait_test(m, "dellnewcommand"):
            if m.text == "الغاء":
                del_db_wait("dellnewcommand")
                return
            del_db_wait("dellnewcommand")
            del_db_addcommand(m.text, m.chat.id)
            await m.reply_text("⌔ تم حذف الكلمه بنجاح من الاوامر المضافه\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "addnewcommand"):
            if m.text == "الغاء":
                del_db_wait("addnewcommand")
                return
            del_db_wait("addnewcommand")
            qrw = m.text
            await m.reply_text("⌔ ارسل الامر الجديد\n√", reply_to_message_id=m.message_id)
            set_db_wait("addnewcommand2", m.from_user.id, m.chat.id)
            return

        if wait_test(m, "addnewcommand2"):
            if m.text == "الغاء":
                del_db_wait("addnewcommand2")
                return
            del_db_wait("addnewcommand2")
            b = m.text
            set_db_addcommand(qrw, b, m.chat.id)
            await m.reply_text("⌔ تم اضافه الامر بنجاح\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "addcustomid"):
            if m.text == "الغاء":
                del_db_wait("addcustomid")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("addcustomid")
            del_db_addcustomid(m.chat.id)
            set_db_addcustomid(m.text, m.chat.id)
            await m.reply_text("⌔ تم تغيير الايدي\n√", reply_to_message_id=m.message_id)
            return

        if wait_test(m, "sellmypoint"):
            del_db_wait("sellmypoint")
            if m.text.isdigit():
                if int(m.text) == 0:
                    await m.reply_text("⌔ ينعل ابو الغباء هتبيع 0 نقط ازاي\n√",
                                       reply_to_message_id=m.message_id)
                    del_db_wait("sellmypoint")
                    return
                else:
                    if int(m.text) > get_mypoint(m):
                        await m.reply_text("⌔ نقاطك اقل من الرقم الى كتبتو\n√",
                                           reply_to_message_id=m.message_id)
                        del_db_wait("sellmypoint")
                        return
                    else:
                        set_db_mypointgame(-int(m.text), m.from_user.id, m.chat.id)
                        set_db_mymessage(int(m.text) * 10, m.from_user.id, m.chat.id)
                        await m.reply_text(f"⌔ تم خصم -> *{int(m.text)}* من نقاطك \n⌔"
                                           f" وتم اضافة -> *{int(m.text) * 10}* رساله الى رسالك\n√",
                                           reply_to_message_id=m.message_id)
                        del_db_wait("sellmypoint")
                        return
            else:
                await m.reply_text("⌔ ارسلت رقم خاطئ\n√",
                                   reply_to_message_id=m.message_id)
                del_db_wait("sellmypoint")
                return

        if wait_test(m, "changesudo"):
            if m.text == "الغاء":
                del_db_wait("changesudo")
                await m.reply_text("⌔ تم الالغاء\n√", reply_to_message_id=m.message_id)
                return
            del_db_wait("changesudo")
            f = open('info.json', )
            data = json.load(f)
            token = data['Token']
            f.close()
            adict = {"Token": token, "idSudo": int(m.text)}
            jsonstring = json.dumps(adict)
            jsonfile = open("info.json", "w")
            jsonfile.write(jsonstring)
            jsonfile.close()
            await m.reply_text("⌔ تم تغيير المطور الاساسي\n√", reply_to_message_id=m.message_id)
            await restart(c, m)
            return

    except Exception as e:
        print("wait" + str(e))
        return
