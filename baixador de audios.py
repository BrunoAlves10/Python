import youtube_dl
import sys
import os

link = input('Digite o link do youtube: ')

ydl = youtube_dl.YoutubeDL({
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
})
with ydl:
    result = ydl.extract_info(link, download=True)