# downloader.py
from pytube import YouTube

def download_video(url: str, output_path: str = ".", audio_only: bool = False, resolution: str = None):
    yt = YouTube(url)
    if audio_only:
        stream = yt.streams.filter(only_audio=True).first()
        desc = "Audio only"
    elif resolution:
        stream = yt.streams.filter(progressive=True, file_extension="mp4", res=resolution).first()
        if not stream:
            stream = yt.streams.get_highest_resolution()
            desc = f"Resolution {resolution} not available. Using highest."
        else:
            desc = f"Video {resolution}"
    else:
        stream = yt.streams.get_highest_resolution()
        desc = f"Video {stream.resolution}"

    stream.download(output_path=output_path)
    return f"✅ Download complete: {yt.title} ({desc})"
