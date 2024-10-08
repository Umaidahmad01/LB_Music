import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "20718334"))
API_HASH = getenv("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6690642431:AAGSF6SvAuOx-Wu6ztRExET6e85DcTroTz8")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Umaid:umaid@cluster0.k2yxsvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5585016974"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music", # dont Change this otherwise u get error 🧧
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/PikaSub_News")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/Pika_Discussion")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQF--m0AaxiduF9c2Rm_MRtPsRdKHr91hGIUZUj36ausjWvl3VZnAdVucz2fMskPsrS09OKVCw6afuJaIatzUZQ3F2L-kRR7ewNrP16-6nrMhW8KArQjO-TW0mgVuGfhCxnNwpBLzy9GYx22aBVvTYWZZ3eodlPuBncr6VzBav7PRyY1vzXl8zOa7iOizWxG449tILBcQYeV_jmCpUN-eVviD4RImsCeKVpc9gjgvoE3FBgu-ynPv5C_Y7OIZe9IQVcL8jmEu1XI2zezL7HtGV-vL8f90yKVYCiIJDEgMv4CW5Wa6iepBDw2j2h1cPSOxgEmcBzneeM4GuYF0cWfa4RHWS-6FwAAAAGOyxn_AQ")
STRING2 = getenv("STRING_SESSION2", "BQF--m0AaxiduF9c2Rm_MRtPsRdKHr91hGIUZUj36ausjWvl3VZnAdVucz2fMskPsrS09OKVCw6afuJaIatzUZQ3F2L-kRR7ewNrP16-6nrMhW8KArQjO-TW0mgVuGfhCxnNwpBLzy9GYx22aBVvTYWZZ3eodlPuBncr6VzBav7PRyY1vzXl8zOa7iOizWxG449tILBcQYeV_jmCpUN-eVviD4RImsCeKVpc9gjgvoE3FBgu-ynPv5C_Y7OIZe9IQVcL8jmEu1XI2zezL7HtGV-vL8f90yKVYCiIJDEgMv4CW5Wa6iepBDw2j2h1cPSOxgEmcBzneeM4GuYF0cWfa4RHWS-6FwAAAAGOyxn_AQ")
STRING3 = getenv("STRING_SESSION3", "BQF--m0AaxiduF9c2Rm_MRtPsRdKHr91hGIUZUj36ausjWvl3VZnAdVucz2fMskPsrS09OKVCw6afuJaIatzUZQ3F2L-kRR7ewNrP16-6nrMhW8KArQjO-TW0mgVuGfhCxnNwpBLzy9GYx22aBVvTYWZZ3eodlPuBncr6VzBav7PRyY1vzXl8zOa7iOizWxG449tILBcQYeV_jmCpUN-eVviD4RImsCeKVpc9gjgvoE3FBgu-ynPv5C_Y7OIZe9IQVcL8jmEu1XI2zezL7HtGV-vL8f90yKVYCiIJDEgMv4CW5Wa6iepBDw2j2h1cPSOxgEmcBzneeM4GuYF0cWfa4RHWS-6FwAAAAGOyxn_AQ")
STRING4 = getenv("STRING_SESSION4", "BQF--m0AaxiduF9c2Rm_MRtPsRdKHr91hGIUZUj36ausjWvl3VZnAdVucz2fMskPsrS09OKVCw6afuJaIatzUZQ3F2L-kRR7ewNrP16-6nrMhW8KArQjO-TW0mgVuGfhCxnNwpBLzy9GYx22aBVvTYWZZ3eodlPuBncr6VzBav7PRyY1vzXl8zOa7iOizWxG449tILBcQYeV_jmCpUN-eVviD4RImsCeKVpc9gjgvoE3FBgu-ynPv5C_Y7OIZe9IQVcL8jmEu1XI2zezL7HtGV-vL8f90yKVYCiIJDEgMv4CW5Wa6iepBDw2j2h1cPSOxgEmcBzneeM4GuYF0cWfa4RHWS-6FwAAAAGOyxn_AQ")
STRING5 = getenv("STRING_SESSION5", "BQF--m0AaxiduF9c2Rm_MRtPsRdKHr91hGIUZUj36ausjWvl3VZnAdVucz2fMskPsrS09OKVCw6afuJaIatzUZQ3F2L-kRR7ewNrP16-6nrMhW8KArQjO-TW0mgVuGfhCxnNwpBLzy9GYx22aBVvTYWZZ3eodlPuBncr6VzBav7PRyY1vzXl8zOa7iOizWxG449tILBcQYeV_jmCpUN-eVviD4RImsCeKVpc9gjgvoE3FBgu-ynPv5C_Y7OIZe9IQVcL8jmEu1XI2zezL7HtGV-vL8f90yKVYCiIJDEgMv4CW5Wa6iepBDw2j2h1cPSOxgEmcBzneeM4GuYF0cWfa4RHWS-6FwAAAAGOyxn_AQ")


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
STATS_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
STREAM_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/7e7c0564bfb98e9ec652f.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
