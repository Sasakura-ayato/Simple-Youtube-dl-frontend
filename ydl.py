from __future__ import unicode_literals
from pkg_resources import require
import youtube_dl
import argparse
import sys

ydl_opts = {}

def ydl(url, type = 'audio'):
    if url == 'unset':
        print('You didn\'t insert video URL. - e.g.) ydl.py -u {Video URL}')
        sys.exit()
    else:
        if type == 'audio':
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                    'preferredquality': '320'},
                    {'key': 'FFmpegMetadata'},
                ],
            }
        elif type == 'video':
            ydl_opts = {
                'format': 'best'
            }
        download = youtube_dl.YoutubeDL(ydl_opts)
        info_dict = download.extract_info(url, download=True)

if __name__ == "__main__":
    psr = argparse.ArgumentParser(
        prog = 'Youtube Downloader Frontend for youtube-dl.py v1.00',
        usage = 'ydl.py -u {Video url} -t {type[e.g.) video, audio]}',
        description = 'Please download videos in compliance with the terms of use of each distributor and the laws and regulations of your country.'
    )

    psr.add_argument('-u', '--url', required=False, default='unset', help='URL of a Video in Youtube')
    psr.add_argument('-t', '--type', required=False, default='unset', help='video or audio. default: audio')

    args = psr.parse_args()

    url = str(args.url)
    type = str(args.type)

    if type == 'unset':
        ydl(url)
    else:
        ydl(url, type)
