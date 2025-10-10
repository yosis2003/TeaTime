from pytube import YouTube, Search
import os


keywords = [
    "tiktok memes", "funny fails", "gaming highlights",
    "philosophy lecture", "religion debate", "self improvement",
    "history documentary", "anime edit", "music video"
]

def download_videos(keywords, limit=10):
    for keyword in keywords:
        search = Search(keyword)
        for i, video in enumerate(search.results[:limit]):
            try:
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=f"downloads/{keyword}")
            except Exception as e:
                print(f"Error downloading {video.title}: {e}")


download_videos(keywords, 10)