import os
from urllib import request
import ctypes
import imghdr
import random
import praw
import time
from urllib.error import HTTPError


def background_changer(sub):
    USER_AGENT = 'wallpaper changer for windows by /u/Jeremy11'
    REDDIT_ID = "Jeremy11"
    REDDIT_PASS = ""

    reddit = praw.Reddit(USER_AGENT)
    reddit.login(REDDIT_ID, REDDIT_PASS)
    images = reddit.get_subreddit(sub)

    for sub in images.get_hot(limit=5):
        image_link = sub.url
        print(image_link)
        file_name = "temp"
        request.urlretrieve(image_link, file_name)
        file_exts = ('png', 'bmp', 'gif', 'jpeg', 'jpg')
        if imghdr.what(file_name) in file_exts or image_link.endswith(file_exts):
            change_background(file_name)
            return True
    return False


def change_background(image_file):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    SPIF_SENDCHANGE = 2
    image_path = os.path.abspath(image_file)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                                               0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)


def get_subs():
    return ["HighRes", "earthporn", "pics", "hdpics", "topwalls", "OldSchoolCool", "QuotesPorn",
            "spaceporn", "pictureswithpatrick"]


def main():
    wallpaper_set = False
    while not wallpaper_set:
        try:
            subs = ["QuotesPorn"]
            wallpaper_set = background_changer(random.choice(subs))
        except HTTPError:
            time.sleep(15)
            continue

main()