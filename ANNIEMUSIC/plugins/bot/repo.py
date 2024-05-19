from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ANNIEMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє ƒσя ʙᴜɢ яєρσѕ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
     
            [ 
            InlineKeyboardButton("ᴋɪᴅɴᴀᴘ ᴍᴇ ʙᴇʙʏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
            ],
     
            [
             InlineKeyboardButton("🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url="https://t.me/NoT_uR_SoHeL"),
             InlineKeyboardButton("❄ ᴄʜᴀɴɴᴇʟ ❄", url="https://t.me/xD_Feelings"),
             ],
     
             [
             InlineKeyboardButton("❄ 𝐃ᴘs 𝐒ᴛᴏʀᴇ ❄", url="https://t.me/Unconditional_Dps"),          
             InlineKeyboardButton("︎☁️ sᴏᴜʀᴄᴇ ☁️", url=f"https://t.me/Flames_xD"),
             ],
     
              ]
 
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/7dbad520debdbc51478c5.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
