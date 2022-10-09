## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQB5vEAXoDP3Lljnj9P5WBbUFHF3fkvfCDyRpXrA3xkk8v_LlwwWkxUSHRd3i4BMbMicSEvtDjLC7DsSKJ6m5_iTcxJCX3cXeliD1I3mYsfSy9L21hymN73hamGEgM--XEVqjwxITfVbTSR0SjR1NjZQIW4AndtQyWukTSlbhZep3rw8r4ji6Vm64XZrR7MvvByWl-QufVxv6d9o7dU0KUV-OqOngmWSLoWCRp-NVVE6h5zneRrBrnJUlE77i7Y17wV_7Ud997c985lZZ7pWGdtRrn7_YyLJ--zQbdkmvLZT9AsH9Q_Ximj-4Z_Q62qLo8Qs5dhv2EOAeUMrqEzEwoasAAAAAHtUSyUA")
BOT_TOKEN = getenv("BOT_TOKEN", "5715328706:AAFjtnPijxuM5bzrJTU7pQy821xcizBPWA8")
BOT_NAME = getenv("BOT_NAME", " Sunny music")
API_ID = int(getenv("API_ID", "13102178"))
API_HASH = getenv("API_HASH", "b6862f55a8927b55d3991bda2d2731e3")
OWNER_NAME = getenv("OWNER_NAME", "Sunnybabuu")
ALIVE_NAME = getenv("ALIVE_NAME", "SUNNY")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "All_competitive_musicc")
BOT_USERNAME = getenv("BOT_USERNAME", "sunnymusic_bbot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SUNNY MUSIC")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "all_competitive_examm")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "all_compatative_exam_channel")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "1200"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
