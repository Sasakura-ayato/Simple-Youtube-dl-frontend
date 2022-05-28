from email.mime import audio
from apiclient.discovery import build
from apiclient.errors import HttpError
import subprocess
import argparse
import ydl

DEVELOPER_KEY = '{DEVELOPER_KEY}'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(
    YOUTUBE_API_SERVICE_NAME, 
    YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY
    )

psr = argparse.ArgumentParser(
    prog = 'Searcher with Youtube Downloader Frontend for youtube-dl.py v1.00',
    usage = 'ydl_search.py -k {keyword}',
    description = 'Please download videos in compliance with the terms of use of each distributor and the laws and regulations of your country.'
)

psr.add_argument('-k', '--keyword', required=True, help='Keyword')

args = psr.parse_args()

keyword = args.keyword

search_response = youtube.search().list(
  q=keyword,
  part='id,snippet',
  type='video'
).execute()

resultId = []

for i , sr in enumerate(search_response.get("items", [])):
    print('== [ ' + str(i) + ' ]==')
    print(sr['snippet']['title'] + ' / ' + sr['snippet']['channelTitle'])
    print('https://youtu.be/' + sr['id']['videoId'])
    print('')
    resultId.append(sr['id']['videoId'])
    

input_number = int(input('Select Video Number : '))
mode = input('Convert Mode (video or audio / default: audio) : ')

if mode == '':
    mode = audio

selected_url = 'https://youtu.be/' + resultId[input_number]

ydl.ydl(str(selected_url))
