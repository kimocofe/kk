import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonXMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonXMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["السورس","ياسورس","يا سورس","سورس"],""))
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/2620724698142362d328d.mp4",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[Sᴏᴜʀᴄᴇ kimo](https://t.me/R_Y_I)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @T_5_C ❫
◉ 𝙸𝙳      : ❪ 611122715 ❫
◉ 𝙱𝙸𝙾    : ❪ أنَا لاَ أفهمُ نَفسِي أتَفهمنِي أنتَ؟. ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᴅᴇᴠ kimo", url=f"https://t.me/T_5_C"), 
                 ],[
                   InlineKeyboardButton(
                        "☭ ՏΌႮᎡᏟᎬ  KiMo ☭", url=f"https://t.me/R_Y_I"),
                ],

            ]

        ),

    )
