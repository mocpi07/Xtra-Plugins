from main_startup.config_var import Config
from main_startup.core.decorators import friday_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_readable_time, delete_or_pass, progress, get_text
import asyncio
import math
import os
from datetime import datetime
from pyrogram import filters
from main_startup.config_var import Config
import requests
import wget
from bs4 import BeautifulSoup
import re
import time

@friday_on_cmd(["modapk", "mapp"])
async def anime(client, message):
    pablo = await edit_or_reply(message, "`Searching For Mod App.....`")
    sgname = get_text(message)
    if not sgname:
        await pablo.edit("Invalid Command Syntax, Please Check Help Menu To Know More!")
        return
    PabloEscobar = f"https://an1.com/tags/MOD/?story={sgname}&do=search&subaction=search"
    r = requests.get(PabloEscobar)
    soup = BeautifulSoup(r.content, 'html5lib')
    mydivs = soup.find_all("div", {"class": "search-results"})
    Pop = soup.find_all("div", {"class": "title"})
    sucker = mydivs[0]
    pH9=sucker.find("a").contents[0]
    file_name = pH9
    print(2)
    pH=sucker.findAll("img")
    imme = wget.download(pH[0]["src"])
    Pablo = Pop[0].a['href']
    print(3)
    ro = requests.get(Pablo)
    soup = BeautifulSoup(ro.content, 'html5lib')
       
    mydis = soup.find_all("a", {"class": "get-product"})
      
    Lol = mydis[0]
      
    lemk = "https://an1.com"+ Lol["href"]

    rr = requests.get(lemk)
    soup = BeautifulSoup(rr.content, 'html5lib')
    print(4)
    script = soup.find('script', type='text/javascript')

    leek = re.search(r'href=[\'"]?([^\'" >]+)', script.text).group()
    dl_link = leek[5:]
      
    print(5)
    r = requests.get(dl_link)
    await pablo.edit("Downloading Mod App")
    open(f"{file_name}.apk", "wb").write(r.content)
    c_time = time.time()
    await pablo.edit(f"`Downloaded {file_name}! Now Uploading Song...`")
    await client.send_document(message.chat.id, document = open(f"{file_name}.apk", "rb"), thumb = imme, progress=progress, progress_args=(pablo, c_time, f'`Uploading {file_name} Mod App`', f"{file_name}.apk"))
    os.remove(f"{file_name}.apk")
    os.remove(imme)
    await pablo.delete()

_name_ = "Mod AppDl"

_help_ = """
**「Mod AppDl」**
♦ `{ch}modapk (app-name)`
➠ Download Mod Apps Just With Name.
"""
