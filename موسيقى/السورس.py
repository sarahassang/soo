import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS, OWNER_NAME, OWNER, PING_PIC

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("**Sat**", 60 * 60 * 24 * 7),
    ("**Day**", 60 * 60 * 24),
    ("**h**", 60 * 60),
    ("**m**", 60),
    ("**s**", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنق","تيست","ping"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡ | جار حساب سرعه البوت")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"**✶ مرحباً بك عزيزي بوت الأغاني يعمل بنجاح .**\n[ㅤㅤㅤㅤㅤㅤ]({PING_PIC})\n**⌯ 𝐏𝐢𝐧𝐠 ⇝** `{delta_ping * 1000:.3f}ms ` \n**⌯ 𝐔𝐩𝐭𝐢𝐦𝐞 ⇝**  {uptime}\n\n  ⌯  [𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚 🎵](t.me/SO_SELVA)\n "
    )

@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["restart","سيلفا","ريستارت"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    mada = await m.reply("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 1**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 2**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 3**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 4**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 5**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 6**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 7**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 8**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ جار اعادة تشغيل البوت 9**")
    await mada.edit("**مرحباً عزيزي المالك\n⌯ تم اعادة تشغيل يوزر بوت بنجاح ✔️**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["اوامر","اغاني"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HEPZ = f"""
**- مرحباً {m.from_user.mention}**

  ⊱ 𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚 𝐔𝐬𝐞𝐫𝐛𝐨𝐭 🎵 اوامر ⊰
⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰

⌯ | لتشغيل صوتية في المكالمة أرسل ↞ ⊰ `{HNDLR}تشغيل  + اسم الاغنية` ⊱
⌯ | لتشغيل فيديو في المكالمة  ↞ ⊰ `{HNDLR}تشغيل_فيديو  + اسم الاغنية` ⊱

⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰

⌯ | لأيقاف الاغنية او الفيديو مؤقتآ  ↞ ⊰ `{HNDLR}مؤقت` ⊱ او  ⊰ `{HNDLR}وقف` ⊱

⌯ | لأعاده تشغيل الاغنية ↞  ⊰ `{HNDLR}متابعه` ⊱     او    ⊰ `{HNDLR}كمل` ⊱

⌯ | لأيقاف الاغنية  ↞ ⊰ `{HNDLR}ايقاف` ⊱   او   ⊰ `{HNDLR}انهاء` ⊱

⌯ | لتخطي الاغنية  ↞ ⊰ `{HNDLR}تقدم` ⊱   او   ⊰ `{HNDLR}سكب` ⊱ او ⊰ `{HNDLR}تخطي` ⊱
⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰

⌯ | لتحميل صوتية أرسل ↞ ⊰ `{HNDLR}تحميل + اسم الاغنية او الرابط` ⊱  او ⊰ `{HNDLR}تنزيل+ اسم الاغنية او الرابط` ⊱

⌯ | لتحميل فيديو  ↞  ⊰ `{HNDLR}فيديو + اسم الاغنية او الرابط` ⊱  او   ⊰ `{HNDLR}تحميل_فيديو + اسم الاغنية او الرابط` ⊱

⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰

⌯ | لعرض قائمه تشغيل  ↞  ⊰ `{HNDLR}قائمه` ⊱

⌯ | لتشغيل 10 اغاني عشوائيه من جروب او قناة ↞ ⊰ `{HNDLR}عشوائيه` + معرف القناه او الجروب  ⊱ 
                                
                                او   ↞  ⊰ `{HNDLR}بحث_اغاني` + معرف القناه او الجروب  ⊱

⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰

⌯ | لعرض معلومات البينج  ↞  ⊰ `{HNDLR}بنق` ⊱ او  ⊰ `{HNDLR}تيست` ⊱

⌯ | لعرض معلومات السورس ↞  ⊰ `{HNDLR}سورس` ⊱  او   ⊰ `{HNDLR}المطور` ⊱

⌯ | لاعادة تشغيل يوزر بوت ↞  ⊰ `{HNDLR}ريستارت` ⊱  
⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰
- ➮ [𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚 🎵](t.me/SO_SELVA) 
"""
    await m.reply(HEPZ, disable_web_page_preview=True)


@Client.on_message(filters.command(["السورس","سورس","المالك","المطور"], prefixes=f"{HNDLR}"))
async def repo(client, m: Message):
    await m.delete()
    REPZ = f"""
<b>**⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰**

 **⌯ اهلا بك يا  ❪ {m.from_user.mention} ❫**

**⌯ في سورس [🎵 سيلفا  الاك ميوزك](t.me/SO_SELVA)  \n\n**⌯  قناة السورس ↞ [𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚 🎵](t.me/SO_SELVA)  **\n\n⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰\n\n**༄⌯[مطورين اݪسورس ☊](t.me/SO_SELVA)⌯**\n**⌯ المطور ↞ [⊰ تيمو ⊱](t.me/tt_t_4)**\n\n**⌯ المطور ↞ [⊰ ليدو ⊱](t.me/J0KER7x)**\n\n**⌯ المطور ↞ [⊰ تيتو ⊱](t.me/XXX_xx_XXX0)**\n\n⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰\n\n**⌯ صاحب الاك ميوزك ↞  ⊰ [{OWNER_NAME}](t.me/{OWNER}) ⊱**\n\n⊱┉┉┉⊶𓄼•𝐌𝐮𝐬𝐢𝐜 𝐒𝐞𝐥𝐯𝐚•𓄹⊷┉┉┉⊰\n\n                     
"""
    await m.reply(REPZ, disable_web_page_preview=True)
