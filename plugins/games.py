import random
import re
import requests
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import TOKEN, get_bot_information
from database import set_db_waitg, get_db_waitg, del_db_waitg, set_db_mypointgame
from plugins.general import waitg_test
from plugins.locks import lock_games_test, set_db_wait, lock_myphoto_test
from plugins.rtp_function import sudo2


@Client.on_callback_query(filters.regex("^moderngame (\\d+)$"))
async def moderngame(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    newgames = "بعض الالعاب المتطوره اختر لعبه وم ثم اختر الشات الذى ترغب باللعب به❤️🥺"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("فلابي بيرد 🐥", url="http://t.me/awesomebot?game=FlappyBird")],
        [InlineKeyboardButton("تبديل النجوم  ⭐️", url="http://t.me/gamee?game=Switchy")] +
        [InlineKeyboardButton("الموتيسكلات 🚴‍♂️", url="http://t.me/gamee?game=motofx")],
        [InlineKeyboardButton("تجميع الالوان 🎛️", url="http://t.me/awesomebot?game=Hextris")] +
        [InlineKeyboardButton("المجوهرات 💎", url="http://t.me/gamee?game=DiamondRows")],
        [InlineKeyboardButton("كره القدم ⚽️", url="http://t.me/gamee?game=Footballstar")] +
        [InlineKeyboardButton("اطلاق النار 🔥", url="http://t.me/gamee?game=NeonBlaster")],
        [InlineKeyboardButton("ركل الكره 🏌️", url="http://t.me/gamee?game=KeepitUP")] +
        [InlineKeyboardButton("بطوله السحق ☣️", url="http://t.me/gamee?game=SmashRoyale")],
        [InlineKeyboardButton("السمك الشائك 🐠", url="http://t.me/gamee?game=SpikyFish3")] +
        [InlineKeyboardButton("الحفر العميق 🕳️", url="http://t.me/gamee?game=BigDig")],
        [InlineKeyboardButton("لعبه 2048 🔢", url="http://t.me/awesomebot?game=g2048")] +
        [InlineKeyboardButton("القط المجنون 🤪", url="http://t.me/gamee?game=CrazyCat")],
        [InlineKeyboardButton("كره السله 🏀", url="http://t.me/gamee?game=BasketBoy")],
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="allgame2 " + str(m.from_user.id))],

    ])
    await m.message.edit_text(newgames, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^sourcegame (\\d+)$"))
async def sourcegame(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    game_message = """💎 الالعاب الخاصه بالسورس
•━━━━━━━━━━━━━•ٴ
⚙️╖ لفتح الالعاب او قفلها ارسل ⇊
🔰╜ قفل الالعاب ࿗ فتح الالعاب
•━━━━━━━━━━━━━•ٴ
🎱╖ لعبه XO ࿗ ❬اكس او❭
😎╢ لعبة الصراحه ࿗ ❬صراحه❭
💃╢ لعبة مريم ࿗ ❬مريم❭
🥺╢ لعبة عقاب ࿗ ❬عقاب❭
💥╢ جمالى % ࿗ ❬نسبه جمالي❭
❤️╢ نسبه الحب ࿗ ❬نسبه الحب❭
👺╢ الكذب ࿗ ❬كشف الكذب❭
🐜╢ لعبه النمله الجامده ࿗ ❬نمله❭
🦗╢ الصرصار الجامد ࿗ ❬صرصار❭
🐷╢ الخنزير الجامد ࿗ ❬خنزير❭
🏀╢ كره السله ࿗ ❬كره السله❭
🎯╢ لعبة النشال ࿗ ❬النشال❭
🎲╢ لعبة النرد او الزهر ࿗ ❬النرد❭
💎╢ كت تويت ࿗ ❬تويت❭
👀╢ كت تويت ࿗ ❬تويت بالصور❭
🤹‍♂️╢ اسرع شخص ࿗ ❬الاسرع❭
🏤╢ لعبة المطابقه ࿗  ❬التشابه❭
⁦🏜⁩╢ لعبة الذكاء ࿗ ❬المختلف❭
🎰╢ لعبة الارقام ࿗ ❬الرياضيات❭
🌐╢ لعبة ترجمه ࿗ ❬الانجليزي❭
🎎╢ لعبة تصحيح ࿗  ❬الامثله❭
⁦♻️⁩╢ لعبة عكس ࿗ الكلمات ❬العكس❭
🤔╢ لعبة التفكير ࿗  ❬الفزوره❭
🎬╜ اللعبه الشهيره ࿗  ❬المعاني❭
•━━━━━━━━━━━━━•ٴ


    """
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("القائمه الرئيسيه ⏺", callback_data="allgame2 " + str(m.from_user.id))],
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅",
                              url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
    ])
    await m.message.edit_text(game_message, reply_markup=keyboard)


@Client.on_callback_query(filters.regex("^allgame2 (\\d+)$"))
async def games2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("العاب السورس 🎱", callback_data="sourcegame " + str(m.from_user.id))],
        [InlineKeyboardButton("العاب متطوره 🏓", callback_data="moderngame " + str(m.from_user.id))],
        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅",
                              url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.message.edit_text("◍ أهلا بيك بقائمه العاب سورس زيرو قم باختيار احذى الازرار\n√", reply_markup=keyboard)


async def games(c: Client, m: Message):
    if m.text == "الالعاب" or m.text == "الالعاب 🎯" or m.text == "الالعاب 🏓" or m.text == "لعبه" or m.text == "لعبة":
        if not lock_games_test(m):
            keyboard = InlineKeyboardMarkup(inline_keyboard=[

                [InlineKeyboardButton("العاب السورس 🎱", callback_data="sourcegame " + str(m.from_user.id))],
                [InlineKeyboardButton("العاب متطوره 🏓", callback_data="moderngame " + str(m.from_user.id))],
                [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅",
                                      url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

            ])
            await m.reply_text("◍ أهلا بيك بقائمه العاب سورس الهكر قم باختيار احذى الازرار\n√", reply_markup=keyboard)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "صراحه" or m.text == "لعبه صراحه" or m.text == "لعبة صراحة" or m.text == "صراحة":
        if not lock_games_test(m):
            saraha = [
                "شادو جدع ولا مش جدع 👀👀",
                " سيزر جدع ولا مش جدع 👀👀",
                "حبيت كام مره 💏",
                "اتعاكست كام مره☹️☹️",
                "خونت كام مره 😈",
                "موقف محرج حصلك😳",
                "اكتر شخص حبيته وكسرك💔",
                "شايف نفسك فين  بعد 5 سنين🤑",
                "لو بقيت بنت ليوم اول حاجه هتعملها ايه والعكس لو بقيتي ولد ليوم اول حاجه هتعمليها ايه🤐🤐",
                "اغرب موقف حصلك🤨",
                "اقرب انسان لقلبك 💑",
                "قولي اغلي 5 اشخاص في حياتك 👨‍👩‍👦‍👦",
                "اوصف نفسك في كلمتين👼",
                "لو ليك 3 امنيات هيبقوا ايه 🧚‍♂️🧚‍♀️",
                "اكتر شخص بتحبه هنا مين😍",
                "اوصف صاحب ليك في 3 كلمات😌",
                "عاكست قبل كده وكان مين😘",
                "اتخانت قبل كده ؟🤣",
                "لو اتجبرت علي جواز صالونات هتوافق 👰🤵",
                "لو هترتبط بحد في الروم هيبقي مين 😉",
                "اهلك بيدلعوك بيقولولك ايه 😁😁",
                'صراحه  |  صوتك حلو؟',
                'صراحه  |  لقيت الناس اللي بوشين؟',
                'صراحه  |  شيء وكنت تحقق اللسان؟',
                'صراحه  |  أنا شخص ضعيف عندما؟',
                'صراحه  |  هل ترغب في إظهار حبك ومرفق لشخص أو رؤية هذا الضعف؟',
                'صراحه  |  هل الكذب يكون ضروري وقتا ما؟',
                'صراحه  |  أتشعر بالوحدة على الرغم انه يحاط بك الكثير من البشر؟',
                'صراحه  |  كيفية الكشف عن من يكمن عليك؟',
                'صراحه  |  إذا حاول شخص ما أن يكرهه أن يقترب منك ويهتم بك تعطيه فرصة؟',
                'صراحه  |  أشجع حاجه حلوه ف حياتك؟',
                'صراحه  |  طريقة جيدة يقنع حتى لو كانت الفكرة خاطئة" توافق؟',
                'صراحه  |  كيف تتصرف مع من يسيئون فهمك ويأخذ على ذهنه ثم ينتظر أن يرفض؟',
                'صراحه  |  التغيير العادي عندما يكون الشخص الذي يحبه؟',
                'صراحه  |  المواقف الصعبة تضعف لك ولا ترفع؟',
                'صراحه  |  نظرة و يفسد الصداقة؟',
                'صراحه  |  ‏‏لو حد قالك كلام سئ في الغالب اي رد فعلك؟',
                'صراحه  |  شخص معاك بالحلوه والمُره؟',
                'صراحه  |  ‏هل تحب إظهار حبك وتعلقك بالشخص أم ترى ذلك ضعف؟',
                'صراحه  |  تاخد بكلام اللي ينصحك وماتعملش اللي انت عاوزة؟',
                'صراحه  |  اي تتمني الناس تعرفه عليك؟',
                'صراحه  |  ابيع المجرة عشان؟',
                'صراحه  |  أحيانا بحس ان الناس ، كمل؟',
                'صراحه  |  صدفة العمر الحلوة هي اني؟',
                'صراحه  |  الكُره العظيم دايم يجي بعد حُب قوي " تتفق؟',
                'صراحه  |  صفة تحبها في نفسك؟',
                'صراحه  |  ‏الفقر فقر العقول ليس الجيوب " ، تتفق؟',
                'صراحه  |  تصلي صلواتك الخمس كلها؟',
                'صراحه  |  ‏تجامل أحد على راحتك؟',
                'صراحه  |  اشجع شيء عملته ف حياتك؟',
                'صراحه  |  ناوي تعمل اي النهارده؟',
                'صراحه  |  اي بيكون شعورك لما بتشوف المطر؟',
                'صراحه  |  غيرتك هاديه ومابتعملش مشاكل؟',
                'صراحه  |  اي اكتر حاجه ندمت عليها؟',
                'صراحه  |  اي الدول اللي تتمنى تزورها؟',
                'صراحه  |  اخره مره بكيت امتي؟',
                'صراحه  |  تقييم حظك ؟ من عشره؟',
                'صراحه  |  هل تعتقد ان حظك سيئ؟',
                'صراحه  |  شـخــص تتمنــي الإنتقــام منـــه؟',
                'صراحه  |  كلمة تود سماعها كل يوم؟',
                'صراحه  |  **هل تُتقن عملك أم تشعر بالممل؟',
                'صراحه  |  هل قمت بانتحال أحد الشخصيات لتكذب على من حولك؟',
                'صراحه  |  متى آخر مرة قمت بعمل مُشكلة كبيرة وتسببت في خسائر؟',
                'صراحه  |  ما هو اسوأ خبر سمعته بحياتك؟',
                '‏صراحه | هل جرحت شخص تحبه من قبل ؟',
                'صراحه  |  ما هي العادة التي تُحب أن تبتعد عنها؟',
                '‏صراحه | هل تحب عائلتك ام تكرههم؟',
                '‏صراحه  |  من هو الشخص الذي يأتي في قلبك بعد الله – سبحانه وتعالى- ورسوله الكريم – صلى الله عليه وسلم؟',
                '‏صراحه  |  هل خجلت من نفسك من قبل؟',
                '‏صراحه  |  ما هو ا الحلم الذي لم تستطيع ان تحققه؟',
                '‏صراحه  |  ما هو الشخص الذي تحلم به كل ليلة؟',
                '‏صراحه  |  هل تعرضت إلى موقف مُحرج جعلك تكره صاحبهُ؟',
                '‏صراحه  |  هل قمت بالبكاء أمام من تُحب؟',
                '‏صراحه  |  ماذا تختار حبيبك أم صديقك؟',
                '‏صراحه  | هل حياتك سعيدة أم حزينة؟',
                'صراحه  |  ما هي أجمل سنة عشتها بحياتك؟',
                '‏صراحه  |  ما هو عمرك الحقيقي؟',
                'صراحه  |  ما هي أمنياتك المُستقبلية؟‏'

            ]
            await m.reply_text(random.choice(saraha), reply_to_message_id=m.message_id)
            set_db_wait("saraha", m.from_user.id, m.chat.id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "مريم" or m.text == "لعبه مريم" or m.text == "لعبة مريم" or m.text == "العاب مريم":
        if not lock_games_test(m):
            mariam = [

                "*** انا اسمي مريم ***\n√",
                "*** مرحباَ ماهو اسمك ؟ ***\n√",
                "`*** اهلا بك ! انا تائهه في هذا المكان  ***`",
                "*** هل تود مساعدتي ؟ ***\n√",
                "*** لماذا هل انت قاسي القلب ؟ ***\n√",
                "*** انني اشفق عليك عليك يجب ان تطهر روحك وتحب الخير للجميع ***\n√",
                "*** ابتعد عني قليل انني متعبة ***\n√",
                "*** هل انت نادم على ماقلت ؟ ***\n√",
                "*** ابتعد عني قليل انني متعبة ***\n√",
                "*** هل انت نادم على ماقلت ؟ ***\n√",
                "*** هل تود مساعدتي ؟ ***\n√",
                "*** واو اشك??ك انك شخصاَ رائع ! ***\n√",
                "*** ابحث معي عن منزلي لقد كان قريباَ من هنا ***\n√",
                "*** ولاكن عندما حل الليل لم اعد ارى اي شيء ***\n√",
                "*** مذا تظن اين يوجد ؟ يمين او يسار ***\n√",
                "*** هيا اذاَ ***\n√",
                "*** اود ان اسئلك سؤال ونحن في الطريق ***\n√",
                "*** هل تراني فتاة لطيفة ام مخيفة ***\n√",
                "*** اشكرك !  ***\n√",
                "*** لقد وصلنا الى المنزل شكراَ جزيلَ انتطرني ثواني وسوف اعود ***\n√",
                "*** هل انت جاهز ؟ ***\n√",
                "*** لقد اخبرت والدي عنك وهم متحمسين لرؤيتك ***\n√",
                "*** هل تود ان تراهم الان ***\n√",
                "*** انا لست الحوت الازرق كما يدعون ***\n√",
                "*** انا لست كاذبة صدقني***\n√",
                "*** لماذا ارى في عينيك الخوف ؟ ***\n√",
                "*** انا مجرد فتاة لطيفة تحب اللعب مع الجميع ***\n√",
                "*** اعرف كل شيء يحدث اسمع ذالك بالراديو ***\n√",
                "*** سمعت ان البشر يقتلون من اجل المال فقط ***\n√",
                "*** لماذا لم تدخل الغرفة ؟ ***\n√",
                "*** ههههههههههههههههههه انت الان مسجون في هذه الغرفة ***\n√",
                "*** لن تخرج حتى اعود لك بعد قليل ***\n√",
                "*** المفت????ح معك ! اكتب .مريم  ***\n√",
                "*** مفتاح احمر , هل حصلت عليه ؟ ***\n√",
                "*** ان لم تحصل عليه , اكتب .مريم مرة اخرى ***\n√",
                "*** مفتاح اسود . هل حصلت عليه ؟ ***\n√",
                "*** اين تريد ان تختبئ بسرعة قبل ان تعود ***\n√",
                "*** لقد عادت من جديد الى المنزل ***\n√",
                "*** لا تصدر اي صوت ! ***\n√",
                "*** مريم : لقد عدت ***\n√",
                "*** مريم : يا ايها ا??مخادع اين انت ***\n√",
                "*** مريم : اعلم انك هنا في المنزل ***\n√",
                "*** مريم : ماذا تريد ان تسمع ***\n√",
                "*** مريم : اضغط على الرابط اهداء مني لك | https://www.youtube.com/watch?v=hvSiuQccmtg ***\n√",
                "*** احد ما خرج من المنزل ***\n√",
                "*** ها ها ها وجتك ***\n√",
                "*** هي انت ستندم سأقتلك ***\n√",
                "*** فلتاتي الي هنا ***\n√",
                "*** سأنال منك انا اسن السكين ها ها ***\n√",
                "*** اتركني وشأني***\n√",
                "*** سأمزقك اربا ***\n√",

            ]
            await m.reply_text(random.choice(mariam), reply_to_message_id=m.message_id)
            set_db_wait("mariam", m.from_user.id, m.chat.id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "عقاب" or m.text == "لعبه عقاب" or m.text == "لعبة عقاب" or m.text == "العاب عقاب":
        if not lock_games_test(m):
            eqab = [

                "◍ صورة وجهك او رجلك او خشمك او يدك\n√",
                "◍ اصدر اي صوت يطلبه منك الاعبين\n√",
                "◍ سكر خشمك و قول كلمة من اختيار الاعبين الي معك\n√",
                "◍ روح الى اي قروب عندك في الواتس اب و اكتب اي شيء يطلبه منك الاعبين  الحد الاقصى 3 رسائل\n√",
                "◍ قول نكتة اذا و ??ازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية\n√",
                "◍ سمعنا صوتك و غن اي اغنية من اختيار الاعبين الي معك\n√",
                "◍ ذي المرة لك لا تعيدها\n√",
                "◍ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام\n√",
                "◍ صور اي شيء يطلبه منك الاعبين\n√",
                "◍ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل....\n√",
                "◍ سكر خشمك و قول كلمة من اختيار الاعبين الي معك\n√",
                "◍ سو مشهد تمثيلي عن مصرية بتولد\n√",
                "◍ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت الكف\n√",
                "◍ ذي المرة لك لا تعيدها\n√",
                "◍ ارمي جوالك على الارض بقوة و اذا انكسر صور الجوال و ارسله في الشات العام\n√",
                "◍ روح عند اي احد بالخاص و قول له انك تحبه و الخ\n√",
                "◍ اكتب في الشات اي شيء يطلبه منك الاعبين في الخاص\n√",
                "◍ قول نكتة اذا و لازم احد الاعبين يضحك اذا محد ضحك يعطونك ميوت الى ان يجي دورك مرة ثانية\n√",
                "◍ سامحتك خلاص مافيه عقاب لك :slight_smile:\n√",
                "◍ اتصل على احد من اخوياك  خوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك\n√",
                "◍ غير اسمك الى اسم من اختيار الاعبين الي معك\n√",
                "◍ اتصل على امك و قول لها انك تحبها :heart:\n√",
                "◍ لا يوجد سؤال لك سامحتك :slight_smile:\n√",
                "◍ قل لواحد ماتعرفه عطني كف\n√",
                "◍ منشن الجميع وقل انا اكرهكم\n√",
                "◍ اتصل لاخوك و قول له انك سويت حادث و الخ....\n√",
                "◍ روح المطبخ و اكسر صحن او كوب\n√",
                "◍ اعطي اي احد جنبك كف اذا مافيه احد جنبك اعطي نفسك و نبي نسمع صوت ا??كف\n√",
                "◍ قول لاي بنت موجود في الروم كلمة حلوه\n√",
                "◍ تكلم باللغة الانجليزية الين يجي دورك مرة ثانية لازم تتكلم اذا ما تكلمت تنفذ عقاب ثاني\n√",
                "◍ لا تتكلم ولا كلمة الين يجي دورك مرة ثانية و اذا تكلمت يجيك باند لمدة يوم كامل من السيرفر\n√",
                "◍ قول قصيدة \n√",
                "◍ تكلم باللهجة السودانية الين يجي دورك مرة ثانية\n√",
                "◍ اتصل على احد من اخوياك  خوياتك , و اطلب منهم مبلغ على اساس انك صدمت بسيارتك\n√",
                "◍ اول واحد تشوفه عطه كف\n√",
                "◍ سو مشهد تمثيلي عن اي شيء يطلبه منك الاعبين\n√",
                "◍ سامحتك خلاص مافيه عقاب لك :slight_smile:\n√",
                "◍ اتصل على ابوك و قول له انك رحت مع بنت و احين هي حامل....\n√",
                "◍ روح اكل ملح + ليمون اذا مافيه اكل اي شيء من اختيار الي معك\n√",
                "◍ تاخذ عقابين\n√",
                "◍ قول اسم امك افتخر بأسم امك\n√",
                "◍ ار??ي اي شيء قدامك على اي احد موجود او على نفسك\n√",
                "◍ اذا انت ولد اكسر اغلى او احسن عطور عندك اذا انتي بنت اكسري الروج حقك او الميك اب حقك\n√",
                "◍ اذهب الى واحد ماتعرفه وقل له انا كيوت وابي بوسه\n√",
                "◍ تتصل على الوالده  و تقول لها خطفت شخص\n√",
                "◍  تتصل على الوالده  و تقول لها تزوجت با سر\n√",
                "◍ ????تصل على الوالده  و تقول لها  احب وحده\n√",
                "◍ تتصل على شرطي تقول له عندكم مطافي\n√",
                "◍ خلاص سامحتك\n√",
                "◍  تصيح في الشارع انا  مجنوون\n√",
                "◍  تروح عند شخص تقول له احبك\n√"

            ]
            await m.reply_text(random.choice(eqab), reply_to_message_id=m.message_id)
            set_db_wait("eqab", m.from_user.id, m.chat.id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "نسبه جمالى" or m.text == "نسبة جمالي" or m.text == "جمالي":
        if not lock_myphoto_test(m):
            if sudo2(m):
                async for photo in c.iter_profile_photos(m.from_user.id, limit=1):
                    await m.reply_photo(photo.file_id,
                                        caption="◍ نسبه جمالك هي ~⪼ 500% مطور بقا وكده ولازم اطبل حبتين ❤️🙄")
            else:
                gmalnumbers = [

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
                if not await c.get_profile_photos(m.from_user.id, limit=1):
                    await m.reply_text("◍ للاسف لايوجد صوره لديك\n√")
                async for photo in c.iter_profile_photos(m.from_user.id, limit=1):
                    await m.reply_photo(photo.file_id,
                                        caption="◍ نسبه جمالك هي ~⪼ " + random.choice(gmalnumbers) + "% ❤️🙄")
        else:
            await m.reply_text("◍ صورتي معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "كشف الكذب" or m.text == "كشف الكدب":
        if not lock_games_test(m):
            await m.reply_text("ارسل لى الجمله لتعرف صدق ام كذب😳😂", reply_to_message_id=m.message_id)
            set_db_wait("kshfelkzb", m.from_user.id, m.chat.id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "نسبه الحب" or m.text == "نسبة الحب":
        if not lock_games_test(m):
            await m.reply_text("❤️💞حسنا ارسل اسمك واسم حبيبتك او العكس \n مثال: محمد وندا!!",
                               reply_to_message_id=m.message_id)
            set_db_wait("nsptelhob", m.from_user.id, m.chat.id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "كره السله" or m.text == "كرة السله" or m.text == "كرة السلة":
        if not lock_games_test(m):
            requests.get("https://api.telegram.org/bot" + TOKEN + "/sendDice?chat_id=" + str(m.chat.id) +
                         "&reply_to_message_id=" + str(m.message_id) + "&emoji=🏀")
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "النشال" or m.text == "ألنشال":
        if not lock_games_test(m):
            requests.get("https://api.telegram.org/bot" + TOKEN + "/sendDice?chat_id=" + str(m.chat.id) +
                         "&reply_to_message_id=" + str(m.message_id) + "&emoji=🎯")
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "النرد" or m.text == "الزهر" or m.text == "ألنرد":
        if not lock_games_test(m):
            requests.get("https://api.telegram.org/bot" + TOKEN + "/sendDice?chat_id=" + str(m.chat.id) +
                         "&reply_to_message_id=" + str(m.message_id) + "&emoji=🎲")
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "الاسرع" or m.text == "ترتيب" or m.text == "ألاسرع":
        if not lock_games_test(m):
            del_db_waitg("speedgame")
            klamspeed = [
                "سحور", "سياره", "استقبال", "قنافه", "ايفون", "بطاطس", "مطبخ",
                "كرستيانو", "دجاجه", "مدرسه", "الوان", "غرفه", "ثلاجه", "قهوه",
                "سفينه", "مصر", "محطه", "طياره", "رادار", "منزل", "مستشفى",
                "كهرباء", "تفاحه", "اخطبوط", "سنترال", "فرنسا", "برتقاله", "تفاح",
                "مطرقه", "هريسه", "لبانه", "شباك", "باص", "سمكه", "ذباب", "تلفاز",
                "حاسوب", "انترنت", "ساحه", "جسر"
            ]
            name = random.choice(klamspeed)
            set_db_waitg("speedgame", name, m.chat.id)
            name = re.sub('سحور', 'س ر و ح', name)
            name = re.sub('سياره', 'ه ر س ي ا', name)
            name = re.sub('استقبال', 'ل ب ا ت ق س ا', name)
            name = re.sub('قنافه', 'ه ق ا ن ف', name)
            name = re.sub('ايفون', 'و ن ف ا', name)
            name = re.sub('بطاطس', 'ب ط ا ط س', name)
            name = re.sub('مطبخ', 'خ ب ط م', name)
            name = re.sub('كرستيانو', 'س ت ا ن و ك ر ي', name)
            name = re.sub('دجاجه', 'ج ج ا د ه', name)
            name = re.sub('مدرسه', 'ه م د ر س', name)
            name = re.sub('الوان', 'ن ا و ا ل', name)
            name = re.sub('غرفه', 'غ ه ر ف', name)
            name = re.sub('ثلاجه', 'ج ه ت ل ا', name)
            name = re.sub('قهوه', 'ه ق ه و', name)
            name = re.sub('سفينه', 'ه ن ف ي س', name)
            name = re.sub('مصر', 'ر م ص', name)
            name = re.sub('محطه', 'ه ط م ح', name)
            name = re.sub('طياره', 'ر ا ط ي ه', name)
            name = re.sub('رادار', 'ر ا ر ا د', name)
            name = re.sub('منزل', 'ن ز م ل', name)
            name = re.sub('مستشفى', 'ى ش س ف ت م', name)
            name = re.sub('كهرباء', 'ر ب ك ه ا ء', name)
            name = re.sub('تفاحه', 'ح ه ا ت ف', name)
            name = re.sub('اخطبوط', 'ط ب و ا خ ط', name)
            name = re.sub('سنترال', 'ن ر ت ل ا س', name)
            name = re.sub('فرنسا', 'ن ف ر س ا', name)
            name = re.sub('برتقاله', 'ر ت ق ب ا ه ل', name)
            name = re.sub('تفاح', 'ح ف ا ت', name)
            name = re.sub('مطرقه', 'ه ط م ر ق', name)
            name = re.sub('هريسه', 'س ه ر ي ه', name)
            name = re.sub('لبانه', 'ب ن ل ه ا', name)
            name = re.sub('شباك', 'ب ش ا ك', name)
            name = re.sub('باص', 'ص ا ب', name)
            name = re.sub('سمكه', 'ك س م ه', name)
            name = re.sub('ذباب', 'ب ا ب ذ', name)
            name = re.sub('تلفاز', 'ت ف ل ز ا', name)
            name = re.sub('حاسوب', 'س ا ح و ب', name)
            name = re.sub('انترنت', 'ا ت ن ر ن ت', name)
            name = re.sub('ساحه', 'ح ا ه س', name)
            name = re.sub('جسر', 'ر ج س', name)
            await m.reply_text(f"◍ اسرع واحد يرتبها » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "speedgame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ الاسرع , ترتيب }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("speedgame")
                return

    if m.text == "التشابه" or m.text == "اموشنات" or m.text == "ايموشنات" or m.text == "ايموشن":
        if not lock_games_test(m):
            del_db_waitg("randomamotion")
            amotion = ["🍏", "🍎", "🍐", "🍊", "😘", "🍉", "🍇", "🍓", "🍈", "🍒", "🍑", "🍍", "💋", "🥝",
                       "🍅", "🍆", "🥑", "🥦", "🥒", "🌶", "🌽", "🥕", "🥔", "🥖", "🥐", "🍞", "🥨", "🍟",
                       "🧀", "🥚", "🍳", "🥓", "🥩", "🍗", "🍖", "🌭", "🍔", "🍠", "🍕", "🥪", "🥙", "☕️",
                       "🍵", "🥤", "🍶", "🍺", "🍻", "🏀", "⚽️", "🏈", "⚾️", "🎾", "🏐", "🏉", "🎱", "🏓", "🏸",
                       "🥅", "🎰", "🎮", "🎳", "🎯", "🎲", "🎻", "🎸", "🎺", "🥁", "🎹", "🎼", "🎧", "🎤",
                       "🎬", "🎨", "🎭", "🎪", "🎟", "🎫", "🎗", "🏵", "🎖", "🏆", "🥌", "🛷", "🚗", "🚌",
                       "🏎", "🚓", "🚑", "🚚", "🚛", "🚜", "🇮🇶", "⚔", "🛡", "🔮", "🌡", "💣", "📌", "📍",
                       "📓", "📗", "📂", "📅", "📪", "📫", "📬", "📭", "⏰", "📺", "🎚", "☎️", "📡"
                       ]
            randomamotion = random.choice(amotion)
            set_db_waitg("randomamotion", randomamotion, m.chat.id)
            await m.reply_text(f"◍ اسرع واحد يكتبها » {randomamotion}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "randomamotion"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت ع نقطه\n◍ للعب مره اخره ارسل »{ اموشنات , التشابه }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("randomamotion")
                return

    if m.text == "المختلف" or m.text == "ألمختلف" or m.text == "مختلف":
        if not lock_games_test(m):
            del_db_waitg("moktlfgame")
            mktlf = ["😸", "☠", "🐼", "🐇", "🌚", "⭐️", "✨", "⛈", "🌥", "⛄️", "👨‍🔬",
                     "👨‍💻", "👨‍🔧", "👩‍🍳", "🧚‍♀", "🙍‍♂", "🧖‍♂", "👬", "👨‍👨‍👧", "🕒",
                     "🕤", "⌛️", "📅"
                     ]
            name = random.choice(mktlf)
            set_db_waitg("moktlfgame", name, m.chat.id)
            name = re.sub("😸", "😹😹😹😹😹😹😹😹😸😹😹😹😹", name)
            name = re.sub("☠", "💀💀💀💀💀💀💀☠💀💀💀💀💀", name)
            name = re.sub("🐼", "👻👻👻🐼👻👻👻👻👻👻👻", name)
            name = re.sub("🐇", "🕊🕊🕊🕊🕊🐇🕊🕊🕊🕊", name)
            name = re.sub("🌑", "🌚🌚🌚🌚🌚🌑🌚🌚🌚", name)
            name = re.sub("🌚", "🌑🌑🌑🌑🌑🌚🌑🌑🌑", name)
            name = re.sub("⭐️", "🌟🌟🌟🌟🌟🌟🌟🌟⭐️🌟🌟🌟", name)
            name = re.sub("✨", "💫💫💫💫💫✨💫💫💫💫", name)
            name = re.sub("⛈", "🌨🌨🌨🌨🌨⛈🌨🌨🌨🌨", name)
            name = re.sub("🌥", "⛅️⛅️⛅️⛅️⛅️⛅️🌥⛅️⛅️⛅️⛅️", name)
            name = re.sub("⛄️", "☃☃☃☃☃☃⛄️☃☃☃☃", name)
            name = re.sub("👨‍🔬", "👩‍🔬👩‍🔬👩‍🔬👩‍🔬👩‍🔬👩‍🔬👩‍🔬👩‍🔬👨‍🔬👩‍🔬👩‍🔬👩‍🔬", name)
            name = re.sub("👨‍💻", "👩‍💻👩‍💻👩‍‍💻👩‍‍💻👩‍💻👨‍💻👩‍💻👩‍💻👩‍💻", name)
            name = re.sub("👨‍🔧", "👩‍🔧👩‍🔧👩‍🔧👩‍🔧👩‍🔧👩‍🔧👨‍🔧👩‍🔧", name)
            name = re.sub("👩‍🍳", "👨‍🍳👨‍🍳👨‍🍳👨‍🍳👨‍🍳👩‍🍳👨‍🍳👨‍🍳👨‍🍳", name)
            name = re.sub("🧚‍♀", "🧚‍♂🧚‍♂🧚‍♂🧚‍♂🧚‍♀🧚‍♂🧚‍♂", name)
            name = re.sub("🧜‍♂", "🧜‍♀🧜‍♀🧜‍♀🧜‍♀🧜‍♀🧚‍♂🧜‍♀🧜‍♀🧜‍♀", name)
            name = re.sub("🧝‍♂", "🧝‍♀🧝‍♀🧝‍♀🧝‍♀🧝‍♀🧝‍♂🧝‍♀🧝‍♀🧝‍♀", name)
            name = re.sub("🙍‍♂️", "🙎‍♂️🙎‍♂️🙎‍♂️🙎‍♂️🙎‍♂️🙍‍♂️🙎‍♂️🙎‍♂️🙎‍♂️", name)
            name = re.sub("🧖‍♂️", "🧖‍♀️🧖‍♀️🧖‍♀️🧖‍♀️🧖‍♀️🧖‍♂️🧖‍♀️🧖‍♀️🧖‍♀️🧖‍♀️", name)
            name = re.sub("👬", "👭👭👭👭👭👬👭👭👭", name)
            name = re.sub("👨‍👨‍👧", "👨‍👨‍👦👨‍👨‍👦👨‍👨‍👦👨‍👨‍👦👨‍👨‍👧👨‍👨‍👦👨‍👨‍👦", name)
            name = re.sub("🕒", "🕒🕒🕒🕒🕒🕒🕓🕒🕒🕒", name)
            name = re.sub("🕤", "🕥🕥🕥🕥🕥🕤🕥🕥🕥", name)
            name = re.sub("⌛️", "⏳⏳⏳⏳⏳⏳⌛️⏳⏳", name)
            name = re.sub("📅", "📆📆📆📆📆📆📅📆📆", name)
            await m.reply_text(f"◍ اسرع واحد يطلع المختلف » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "moktlfgame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ المختلف }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("moktlfgame")
                return

    if m.text == "الرياضيات" or m.text == "رياضه" or m.text == "رياضيات":
        if not lock_games_test(m):
            del_db_waitg("ryadagame")
            ryada = ["22", "30", "33", "60", "90", "2", "5", "36", "16", "88", "50", "10", "19",
                     "125", "150", "20", "18", "27"
                     ]
            name = random.choice(ryada)
            set_db_waitg("ryadagame", name, m.chat.id)
            name = re.sub("22", "2+20=", name)
            name = re.sub("30", "10*3=", name)
            name = re.sub("33", "30+3=", name)
            name = re.sub("60", "33+27=", name)
            name = re.sub("90", "9*9+9=", name)
            name = re.sub("2", "2*1=", name)
            name = re.sub("5", "5*1=", name)
            name = re.sub("36", "6*6=", name)
            name = re.sub("16", "2*8=", name)
            name = re.sub("88", "8+80=", name)
            name = re.sub("50", "30+20=", name)
            name = re.sub("10", "2+8=", name)
            name = re.sub("19", "6+13=", name)
            name = re.sub("125", "5*5*5=", name)
            name = re.sub("150", "5*10+100=", name)
            name = re.sub("20", "30-6-4=", name)
            name = re.sub("20", "30-6-4=", name)
            name = re.sub("20", "2+3*3=", name)
            name = re.sub("27", "3+3*3=", name)
            await m.reply_text(f"◍ اسرع واحد يحل المسأله » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "ryadagame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ الرياضيات }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("ryadagame")
                return

    if m.text == "الانجليزي" or m.text == "الانجليزى" or m.text == "انجليزي":
        if not lock_games_test(m):
            del_db_waitg("englishgame")
            english = ["معلومات", "قنوات", "مجموعات", "كتاب", "تفاحه",
                       "مختلف", "مصر", "فلوس", "اعلم", "ذئب", "تمساح",
                       "ذكي", "كلب", "صقر", "مشكله", "كمبيوتر", "وايرليس",
                       "اصدقاء", "منضده"
                       ]
            name = random.choice(english)
            set_db_waitg("englishgame", name, m.chat.id)
            name = re.sub("ذئب", "wolf", name)
            name = re.sub("معلومات", "information", name)
            name = re.sub("قنوات", "channels", name)
            name = re.sub("مجموعات", "groups", name)
            name = re.sub("كتاب", "book", name)
            name = re.sub("تفاحه", "apple", name)
            name = re.sub("مصر", "egypt", name)
            name = re.sub("فلوس", "money", name)
            name = re.sub("اعلم", "i know", name)
            name = re.sub("تمساح", "crocodile", name)
            name = re.sub("مختلف", "different", name)
            name = re.sub("ذكي", "intelligent", name)
            name = re.sub("كلب", "dog", name)
            name = re.sub("صقر", "falcon", name)
            name = re.sub("مشكله", "error", name)
            name = re.sub("كمبيوتر", "computer", name)
            name = re.sub("وايرليس", "wifi", name)
            name = re.sub("اصدقاء", "friends", name)
            name = re.sub("منضده", "table", name)
            await m.reply_text(f"◍ اسرع واحد يجاوب » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "englishgame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ الانكليزي }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("englishgame")
                return

    if m.text == "الامثله" or m.text == "امثله":
        if not lock_games_test(m):
            del_db_waitg("amselahgame")
            mthal = ["اخوات", "زيهم", "الزبيب", "داره", "الوالدين", "شمعتك", "مرايه", "الرءوس", "حدو",
                     "رجالها", "عدوك", "الغراب", "الغطاس", "ماتو", "اتمكن", "زجاج", "فار", "شهر",
                     "القتيل", "يكحله", "امه"
                     ]
            name = random.choice(mthal)
            set_db_waitg("amselahgame", name, m.chat.id)
            name = re.sub("اخوات", "لو قلبك مات متجيش على اتنين___", name)
            name = re.sub("زيهم", "اى ياعمهم اشتكيلك منهم تعمل___", name)
            name = re.sub("شمعتك", "دارى على___تقيد", name)
            name = re.sub("داره", "من خرج من___قل مقداره", name)
            name = re.sub("الوالدين", "رضا___احسن من ابوك وامك", name)
            name = re.sub("الرءوس", "اذا تطاول الايدي تساوت___", name)
            name = re.sub("مرايه", "فى الوش___وفى القفه سلايه", name)
            name = re.sub("حدو", "الشئ اللى يزيد عن___ ينقلب لضدو", name)
            name = re.sub("رجالها", "مايجبها الا ___", name)
            name = re.sub("عدوك", "امشى عدل يحتار___فيك", name)
            name = re.sub("الزبيب", "ضرب الحبيب زى اكل ___", name)
            name = re.sub("الغراب", "ياما جاب___ لامه", name)
            name = re.sub("ماتو", "اللى اغتشو___", name)
            name = re.sub("اتمكن", "اتمسكن لحد ما___", name)
            name = re.sub("زجاج", "اللى بيتو من___مايحدفش الناس بالطوب", name)
            name = re.sub("فار", "لو غاب القط العب يا___", name)
            name = re.sub("شهر", "امشي__ولا تعدى نهر", name)
            name = re.sub("القتيل", "يقتل___ويمشى فى جنازته", name)
            name = re.sub("الغطاس", "المايه تكدب___", name)
            name = re.sub("يكحلها", "جه___عماها", name)
            name = re.sub("امه", "القرد فى عين___غزال", name)
            await m.reply_text(f"◍ اسرع واحد يكمل المثل الشعبى » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "amselahgame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ الامثله }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("amselahgame")
                return

    if m.text == "العكس" or m.text == "عكس":
        if not lock_games_test(m):
            del_db_waitg("elaksgame")
            katu = ["باي", "فهمت", "شرق", "ظلام", "احبك", "وحش", "حادق", "بعيد", "واطي",
                    "فقير", "سريع", "مظلوم", "طويل", "جديد", "ضعيف", "فرح", "شجاع", "رحت", "يقين",
                    "نشيط", "شبعان", "عطشان", "سماء", "بكي", "هادئ"
                    ]
            name = random.choice(katu)
            set_db_waitg("elaksgame", name, m.chat.id)
            name = re.sub("باي", "هاي", name)
            name = re.sub("فهمت", "مفهمتش", name)
            name = re.sub("شرق", "غرب", name)
            name = re.sub("ظلام", "نور", name)
            name = re.sub("احبك", "اكرهك", name)
            name = re.sub("وحش", "حلو", name)
            name = re.sub("حادق", "مسكر", name)
            name = re.sub("بعيد", "قريب", name)
            name = re.sub("واطي", "عالي", name)
            name = re.sub("فقير", "غني", name)
            name = re.sub("سريع", "بطيء", name)
            name = re.sub("مظلوم", "ظالم", name)
            name = re.sub("طويل", "قصير", name)
            name = re.sub("جديد", "قديم", name)
            name = re.sub("ضعيف", "قوي", name)
            name = re.sub("فرح", "حزن", name)
            name = re.sub("شجاع", "جبان", name)
            name = re.sub("رحت", "جيت", name)
            name = re.sub("يقين", "شك", name)
            name = re.sub("نشيط", "كسول", name)
            name = re.sub("شبعان", "جعان", name)
            name = re.sub("عطشان", "ظمئان", name)
            name = re.sub("سماء", "ارض", name)
            name = re.sub("بكي", "ضحك", name)
            name = re.sub("هادئ", "عصبي", name)
            await m.reply_text(f"◍ اسرع واحد يقول عكس الكلمه » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "elaksgame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ العكس }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("elaksgame")
                return

    if m.text == "معاني" or m.text == "نع":
        if not lock_games_test(m):
            del_db_waitg("elmaanygame")
            maanyrand = ["قرد", "دجاجه", "بطريق", "ضفدع", "بومه", "نحله", "ديك", "جمل", "بقره", "دولفين", "تمساح",
                         "قرش", "نمر", "اخطبوط", "سمكه", "خفاش", "اسد", "فأر", "ذئب", "فراشه", "عقرب", "زرافه", "قنفذ",
                         "تفاحه", "باذنجان", "قوس قزح", "بزازه", "بطيخ", "وزه", "كتكوت"
                         ]
            name = random.choice(maanyrand)
            set_db_waitg("elmaanygame", name, m.chat.id)
            name = re.sub("قرد", "🐒", name)
            name = re.sub("دجاجه", "🐔", name)
            name = re.sub("بطريق", "🐧", name)
            name = re.sub("ضفدع", "🐸", name)
            name = re.sub("بومه", "🦉", name)
            name = re.sub("نحله", "🐝", name)
            name = re.sub("ديك", "🐓", name)
            name = re.sub("جمل", "🐫", name)
            name = re.sub("بقره", "🐄", name)
            name = re.sub("دولفين", "🐳", name)
            name = re.sub("تمساح", "🐊", name)
            name = re.sub("قرش", "🦈", name)
            name = re.sub("نمر", "🐅", name)
            name = re.sub("اخطبوط", "🐙", name)
            name = re.sub("سمكه", "🐟", name)
            name = re.sub("خفاش", "🦇", name)
            name = re.sub("اسد", "🦁", name)
            name = re.sub("فأر", "🐭", name)
            name = re.sub("ذئب", "🐺", name)
            name = re.sub("فراشه", "🦋", name)
            name = re.sub("عقرب", "🦂", name)
            name = re.sub("زرافه", "🦒", name)
            name = re.sub("قنفذ", "🦔", name)
            name = re.sub("تفاحه", "🍎", name)
            name = re.sub("باذنجان", "🍆", name)
            name = re.sub("قوس قزح", "🌈", name)
            name = re.sub("بزازه", "🍼", name)
            name = re.sub("بطيخ", "🍉", name)
            name = re.sub("وزه", "🦆", name)
            name = re.sub("كتكوت", "🐣", name)
            await m.reply_text(f"◍ اسرع واحد يقول اسم الاموشن » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "elmaanygame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ المعاني }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("elmaanygame")
                return

    if m.text == "الحزوره" or m.text == "ح" or m.text == "فزوره" or m.text == "فزورة" or m.text == "حزورة" or m.text == "حزوره":
        if not lock_games_test(m):
            del_db_waitg("fazoragame")
            fazoraa = ["الجرس", "عقرب الساعه", "السمك", "المطر", "5", "الكتاب", "البسمار", "7", "الكعبه",
                       "بيت الشعر", "لهانه", "انا", "امي", "الابره", "الساعه", "22", "غلط", "كم الساعه",
                       "البيتنجان", "البيض", "المرايه", "الضوء", "الهواء", "الضل", "العمر", "القلم", "المشط",
                       "الحفره", "البحر", "الثلج", "الاسفنج", "الصوت", "بلم"]
            name = random.choice(fazoraa)
            set_db_waitg("fazoragame", name, m.chat.id)
            name = re.sub("الجرس", "شيئ اذا لمسته صرخ ما هوه ؟", name)
            name = re.sub("عقرب الساعه", "اخوان لا يستطيعان تمضيه اكثر من دقيقه معا فما هما ؟", name)
            name = re.sub("السمك", "ما هو الحيوان الذي لم يصعد الى سفينة نوح عليه السلام ؟", name)
            name = re.sub("المطر", "شيئ يسقط على رأسك من الاعلى ولا يجرحك فما هو ؟", name)
            name = re.sub("5", "ما العدد الذي اذا ضربته بنفسه واضفت عليه 5 يصبح ثلاثين ", name)
            name = re.sub("الكتاب", "ما الشيئ الذي له اوراق وليس له جذور ؟", name)
            name = re.sub("البسمار", "ما هو الشيئ الذي لا يمشي الا بالضرب ؟", name)
            name = re.sub("7", "عائله مؤلفه من 6 بنات واخ لكل منهن .فكم عدد افراد العائله ", name)
            name = re.sub("الكعبه", "ما هو الشيئ الموجود وسط مكة ؟", name)
            name = re.sub("بيت الشعر", "ما هو البيت الذي ليس فيه ابواب ولا نوافذ ؟ ", name)
            name = re.sub("لهانه", "وحده حلوه ومغروره تلبس مية تنوره .من هيه ؟ ", name)
            name = re.sub("انا", "ابن امك وابن ابيك وليس باختك ولا باخيك فمن يكون ؟", name)
            name = re.sub("امي", "اخت خالك وليست خالتك من تكون ؟ ", name)
            name = re.sub("الابره", "ما هو الشيئ الذي كلما خطا خطوه فقد شيئا من ذيله ؟ ", name)
            name = re.sub("الساعه", "ما هو الشيئ الذي يقول الصدق ولكنه اذا جاع كذب ؟", name)
            name = re.sub("22", "كم مره ينطبق عقربا الساعه على بعضهما في اليوم الواحد ", name)
            name = re.sub("غلط", "ما هي الكلمه الوحيده التي تلفض غلط دائما ؟ ", name)
            name = re.sub("كم الساعه", "ما هو السؤال الذي تختلف اجابته دائما ؟", name)
            name = re.sub("البيتنجان", "جسم اسود وقلب ابيض وراس اخظر فما هو ؟", name)
            name = re.sub("البيض", "ماهو الشيئ الذي اسمه على لونه ؟", name)
            name = re.sub("المرايه", "ارى كل شيئ من دون عيون من اكون ؟ ", name)
            name = re.sub("الضوء", "ما هو الشيئ الذي يخترق الزجاج ولا يكسره ؟", name)
            name = re.sub("الهواء", "ما هو الشيئ الذي يسير امامك ولا تراه ؟", name)
            name = re.sub("الضل", "ما هو الشيئ الذي يلاحقك اينما تذهب ؟ ", name)
            name = re.sub("العمر", "ما هو الشيء الذي كلما طال قصر ؟ ", name)
            name = re.sub("القلم", "ما هو الشيئ الذي يكتب ولا يقرأ ؟", name)
            name = re.sub("المشط", "له أسنان ولا يعض ما هو ؟ ", name)
            name = re.sub("الحفره", "ما هو الشيئ اذا أخذنا منه ازداد وكبر ؟", name)
            name = re.sub("البحر", "ما هو الشيئ الذي يرفع اثقال ولا يقدر يرفع مسمار ؟", name)
            name = re.sub("الثلج", "انا ابن الماء فان تركوني في الماء مت فمن انا ؟", name)
            name = re.sub("الاسفنج", "كلي ثقوب ومع ذالك احفض الماء فمن اكون ؟", name)
            name = re.sub("الصوت", "اسير بلا رجلين ولا ادخل الا بالاذنين فمن انا ؟", name)
            name = re.sub("بلم", "حامل ومحمول نصف ناشف ونصف مبلول فمن اكون ؟ ", name)
            await m.reply_text(f"◍ اسرع واحد يحل الفزوره » {name}\n√", reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if waitg_test(m, "fazoragame"):
        for wtr in get_db_waitg(m.chat.id):
            if wtr[1] == m.text:
                set_db_mypointgame(1, m.from_user.id, m.chat.id)
                await m.reply_text("◍ الف مبروك لقد فزت وحصلت على نقطه\n◍ للعب مره اخره ارسل »{ الفزوره }\n√",
                                   reply_to_message_id=m.message_id)
                del_db_waitg("fazoragame")
                return

    if m.text == "تويت" or m.text == "كت تويت" or m.text == "كت تويت 🎲" or m.text == "كات تويت":
        if not lock_games_test(m):
            tweet = [
                "كت تويت ‏| تخيّل لو أنك سترسم شيء وحيد فيصبح حقيقة، ماذا سترسم؟",
                "كت تويت | أكثر شيء يُسكِت الطفل برأيك؟",
                "كت تويت | الحرية لـ ... ؟",
                "كت تويت | قناة الكرتون المفضلة في طفولتك؟",
                "كت تويت ‏| كلمة للصُداع؟",
                "كت تويت ‏| ما الشيء الذي يُفارقك؟",
                "كت تويت | موقف مميز فعلته مع شخص ولا يزال يذكره لك؟",
                "كت تويت ‏| أيهما ينتصر، الكبرياء أم الحب؟",
                "كت تويت | بعد ١٠ سنين ايش بتكون ؟",
                "كت تويت ‏| مِن أغرب وأجمل الأسماء التي مرت عليك؟",
                "‏كت تويت | عمرك شلت مصيبة عن شخص برغبتك ؟",
                "كت تويت | أكثر سؤال وجِّه إليك مؤخرًا؟",
                "‏كت تويت | ما هو الشيء الذي يجعلك تشعر بالخوف؟",
                "‏كت تويت | وش يفسد الصداقة؟",
                "‏كت تويت | شخص لاترفض له طلبا ؟",
                "‏كت تويت | كم مره خسرت شخص تحبه؟.",
                "‏كت تويت | كيف تتعامل مع الاشخاص السلبيين ؟",
                "‏كت تويت | كلمة تشعر بالخجل اذا قيلت لك؟",
                "‏كت تويت | جسمك اكبر من عٌمرك او العكسّ ؟!",
                "‏كت تويت |أقوى كذبة مشت عليك ؟",
                "‏كت تويت | تتأثر بدموع شخص يبكي قدامك قبل تعرف السبب ؟",
                "كت تويت | هل حدث وضحيت من أجل شخصٍ أحببت؟",
                "‏كت تويت | أكثر تطبيق تستخدمه مؤخرًا؟",
                "‏كت تويت | ‏اكثر شي يرضيك اذا زعلت بدون تفكير ؟",
                "‏كت تويت | وش محتاج عشان تكون مبسوط ؟",
                "‏كت تويت | مطلبك الوحيد الحين ؟",
                "‏كت تويت | هل حدث وشعرت بأنك ارتكبت أحد الذنوب أثناء الصيام؟",
                "‏كت تويت | كم عمرك ؟",
                "‏كت تويت | اسم تحب الكل يناديك فيه ؟",
                "‏كت تويت | تاريخ تحبه ؟",
                "‏كت تويت | يوم من أيام الأسبوع تحبه ؟",
                "‏كت تويت | أحلى مطعم عندك ؟",
                "‏كت تويت | أفضل سنه دراسية عندك ؟",
                "‏كت تويت | أفضل مغني تحبه ؟",
                "‏كت تويت | نوم ولا أكل ؟",
                "‏كت تويت | الحباة ما تمشي بدون ؟",
                "‏كت تويت | حساب لازم تتابعه كل يوم ؟",
                "‏كت تويت | تاريخ ما تنساه ؟",
                "‏كت تويت | عندك استعداد تخسر كل شيء الا ؟",
                "‏كت تويت | منشن لـ اقرب شخص لك بالتليجرام ؟",
                "‏كت تويت | شيل اول حرف من اسمك واخر حرف وشوف هيبقى اى ؟",
                "‏كت تويت | كيف حال قلبك الان ؟",
                "‏كت تويت | كم الساعه بهاتفك الان ؟",
                "‏كت تويت | اسم اول حب بحياتك ؟",
                "‏كت تويت | ماهو افضل بوت على التليجرام ؟"

            ]
            await m.reply_text(random.choice(tweet), reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "تويت بالصور" or m.text == "كت تويت بالصور" or m.text == "كات تويت بالصور":
        if not lock_games_test(m):
            tweetphoto = [
                "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51",
                "52", "53", "54", "55", "56", "57", "58"
            ]

            await m.reply_photo("https://t.me/cattwit/" + random.choice(tweetphoto), reply_to_message_id=m.message_id)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "نمله" or m.text == "النمله":
        if not lock_games_test(m):
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton("🐜", callback_data="antgame")],
            ])
            await m.reply_photo("https://t.me/UURTBOT/41", reply_markup=keyboard)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "صرصار" or m.text == "صرصور" or m.text == "الصرصار":
        if not lock_games_test(m):
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton("🦗", callback_data="cockroachgame")],
            ])
            await m.reply_photo("https://t.me/UURTBOT/42", reply_markup=keyboard)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)

    if m.text == "خنزير" or m.text == "خنزيره" or m.text == "الخنزير":
        if not lock_games_test(m):
            keyboard = InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton("🐷", callback_data="piggame")],
            ])
            await m.reply_photo("https://t.me/UURTBOT/43", reply_markup=keyboard)
        else:
            await m.reply_text("◍ الالعاب معطله يرجى تفعيلها اولا\n√", reply_to_message_id=m.message_id)


@Client.on_callback_query(filters.regex("^ttgwzeny$"))
async def ttgwzeny(c: Client, m: CallbackQuery):
    await message.reply_text(
        f"""✨ **Welcome {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **Allows you to play music and video on groups through the Telegram Group video chat!**
💡 **Find out all the Bot's commands and how they work by clicking on the » 📚 Commands button!**
🔖 **To know how to use this bot, please click on the » ❓ Basic Guide button!**
""")

@Client.on_callback_query(filters.regex("^antgame$"))
async def antgame(c: Client, m: CallbackQuery):
    await c.answer_callback_query(m.id, text="ياكلب ياللي معندكش رحمه بتموتها لي..😒😢", show_alert=True)
    await m.message.delete()
    await m.message.reply_photo("https://t.me/UURTBOT/44",
                                caption=f"هو الكلب ده اللي موتها يجماعه😂👇\n["
                                        f"{m.from_user.first_name}](tg://user?id={m.from_user.id})",
                                parse_mode="Markdown")


@Client.on_callback_query(filters.regex("^cockroachgame$"))
async def cockroachgame(c: Client, m: CallbackQuery):
    await c.answer_callback_query(m.id, text="يخربييت ام دى عفانه..😒😢", show_alert=True)
    await m.message.delete()
    await m.message.reply_animation("https://t.me/UURTBOT/45",
                                    caption=f"هو المعفن اللى صحي الصرصار يجماعه😂👇\n["
                                            f"{m.from_user.first_name}](tg://user?id={m.from_user.id})",
                                    parse_mode="Markdown")


@Client.on_callback_query(filters.regex("^piggame$"))
async def piggame(c: Client, m: CallbackQuery):
    await c.answer_callback_query(m.id, text="قتلت اخوك ياخنزير..😒😢", show_alert=True)
    await m.message.delete()
    await m.message.reply_photo("https://t.me/UURTBOT/46",
                                caption=f"هو الخنزير اللى قتل اخوه يجماعه😂👇\n["
                                        f"{m.from_user.first_name}](tg://user?id={m.from_user.id})",
                                parse_mode="Markdown")

