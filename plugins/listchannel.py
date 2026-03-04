import datetime
import random
from pyrogram import Client
from pyrogram.types import Message



async def listchannel(c: Client, m: Message):
    if datetime.datetime.now().hour == 3 or datetime.datetime.now().hour == 6 or datetime.datetime.now().hour == 9 \
            or datetime.datetime.now().hour == 12 or datetime.datetime.now().hour == 15 \
            or datetime.datetime.now().hour == 18 or datetime.datetime.now().hour == 21 \
            or datetime.datetime.now().hour == 24:
        listChannel = ["✨  𝒋𝒐𝒊𝒏 𝒉𝒆𝒓𝒆 { @SoUrCe_HaCkEr } 👨‍💻",
                     "✨ انا بحبك خدبالك وهحبك اكتر لو جيت هنا { @SoUrCe_HaCkEr } 👨‍💻",
                     """✨ مرحبا عزيزي يمكنك تنصيب بوت خاص بك

💬 يمكنك دخول قناه السورس لمراسله المبرمج                     

🤖 وتشغيل بوت خاص بك الان .                     

✅ قناه السورس { @SoUrCe_HaCkEr }                     
                     """,
                     "💫 متيجي هنا وانا احبك { @SoUrCe_HaCkEr } 🦋",]
        await c.send_message(m.chat.id, random.choice(listChannel))
