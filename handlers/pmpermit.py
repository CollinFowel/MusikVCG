# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.




from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo, Apa yang dapat bot ini lakukan ? 🤔 \n\n \n\n 🇮🇩 Bot ini dapat memutar lagu yang kamu mau pada telepon grup \n\n \n\n 🇬🇧 This bot can play the song you want in the voice call group \n\n \n\n ⚠️ How to use / bagaimana cara menggunakan bot ini ? ↓ \n\n \n\n Read / Baca → @MusikVcgChannel ← \n\n \n\n 👤 **Own :** @CollinFowel 🇮🇩 \n\n \n\n #️⃣ **CATATAN : BATAS DURASI MUSIK TIDAK BOLEH LEBIH DARI 15 MENIT DAN KALO ERROR SILAHKAN LAPOR KE** @MusikVCGSupport")
  return                        
