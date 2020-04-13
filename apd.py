#!/usr/bin/python
import argparse
import requests as req
from bs4 import BeautifulSoup as bs
import progressbar


def usage():
    return """
        Use "" around link to avoid bad things :>
        adp.py "Link" [quality]
        python apd.py "https://www.aparat.com/v/d13rh3"
        python apd.py "https://www.aparat.com/v/d13rh3" -q 480

        The default quality is 480.
    """

def main():
    print("Please wait...")
    mainPage = req.get(link).content
    main_soup = bs(mainPage, 'html.parser')

    if type_dl == "playlist":
        playlist = main_soup.find('div', attrs={'class':'playlist-body'})
        playListLinks = playlist.find_all('a', attrs={'class':'title'})

        video_pages = [f"https://www.aparat.com{video.get('href')}" for video in playListLinks]
        count=len(video_pages)
        print(f"This playlist contains {count} videos")
    elif type_dl == "single":
        video_pages = [link]
        count=len(video_pages)
        print(f"{count} video to download")
    elif type_dl == "all":
        playlist = main_soup.find('div', attrs={'class':'grid-thumbnail'})
        playListLinks = playlist.find_all('a', attrs={'class':'title'})

        video_pages = [f"https://www.aparat.com{video.get('href')}" for video in playListLinks]
        count=len(video_pages)
        print(f"This channel; contains {count} videos")


    bar=progressbar.ProgressBar(maxval=count,
    widgets=[progressbar.Bar('=','[',']'),progressbar.Percentage()])
    bar.start()

    links = {}
    for index,page in enumerate(video_pages) :
        bar.update(index+1)
        html = req.get(page).content
        soup = bs(html, 'html.parser')
        name = soup.find("h1", attrs={"id":"videoTitle", "class":"title"}).text.encode()
        qualitys = soup.find('div', attrs={'class':'dropdown-content'}).find_all('a')
        for qual in qualitys :
            if quality in qual.get('aria-label'):
                links[name] = qual.get('href')
            elif "480" in qual.get('aria-label'):
                links[name] = qual.get('href')
    bar.finish()
    print("writing download list ...")

    
    with open('apd_output.sh', 'w') as file:
        file.write(f"#!/bin/bash\n")
        i = 1
        for name, videoLink in links.items():
            file.write('aria2c -x16 -s16 -k1M {} -o \"{:03d}_{}.mp4\"\n'.format(videoLink,i,name.decode('utf-8')))
            i += 1



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Aparat Playlist Downloader(APD)", usage=usage())
    parser.add_argument("link", help="main page Link")
    parser.add_argument("-q", "--quality", help="eg: [124, 360, 480, 720, ...]", default='480')
    parser.add_argument("-t", "--type", help="eg: [playlist, single, all]", default='playlist')

    args = parser.parse_args()
    link = args.link
    quality = args.quality
    type_dl = args.type

    if args.quality :
        main()
    else:
        usage()

