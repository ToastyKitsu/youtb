import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips
from yt_dlp import YoutubeDL

# Step 1: Get all video URLs from the channel
def get_shorts_urls(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'dump_single_json': True,
        'force_generic_extractor': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
        if 'entries' in result:
            return [entry['url'] for entry in result['entries'] if 'shorts' in entry['url']]
        else:
            return []

# Step 2: Download Shorts
def download_videos(urls, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title).40s.%(ext)s'),
        'format': 'mp4',
        'quiet': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download([url])
            except Exception as e:
                print(f"Failed to download {url}: {e}")

# Step 3: Merge videos
def merge_videos(input_dir="downloads", output_path="merged_shorts.mp4"):
    clips = []
    for file in sorted(os.listdir(input_dir)):
        if file.endswith(".mp4"):
            clip_path = os.path.join(input_dir, file)
            try:
                clip = VideoFileClip(clip_path)
                clips.append(clip)
            except Exception as e:
                print(f"Could not load {file}: {e}")
    if clips:
        final_video = concatenate_videoclips(clips, method="compose")
        final_video.write_videofile(output_path, codec="libx264")
        print(f"✅ Merged video saved as: {output_path}")
    else:
        print("No videos to merge.")

# Main workflow
if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL (must include /shorts): ").strip()

    print("🔍 Fetching Shorts URLs...")
    shorts_urls = get_shorts_urls(channel_url)

    if not shorts_urls:
        print("❌ No Shorts found. Make sure you're using a Shorts page URL (e.g., https://www.youtube.com/@channel/shorts)")
    else:
        print(f"📥 Found {len(shorts_urls)} Shorts. Downloading...")
        download_videos(shorts_urls)

        print("🎬 Merging downloaded Shorts...")
        merge_videos()
import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips
from yt_dlp import YoutubeDL

# Step 1: Get all video URLs from the channel
def get_shorts_urls(channel_url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'dump_single_json': True,
        'force_generic_extractor': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(channel_url, download=False)
        if 'entries' in result:
            return [entry['url'] for entry in result['entries'] if 'shorts' in entry['url']]
        else:
            return []

# Step 2: Download Shorts
def download_videos(urls, output_dir="downloads"):
    os.makedirs(output_dir, exist_ok=True)
    ydl_opts = {
        'outtmpl': os.path.join(output_dir, '%(title).40s.%(ext)s'),
        'format': 'mp4',
        'quiet': False,
    }

    with YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download([url])
            except Exception as e:
                print(f"Failed to download {url}: {e}")

# Step 3: Merge videos
def merge_videos(input_dir="downloads", output_path="merged_shorts.mp4"):
    clips = []
    for file in sorted(os.listdir(input_dir)):
        if file.endswith(".mp4"):
            clip_path = os.path.join(input_dir, file)
            try:
                clip = VideoFileClip(clip_path)
                clips.append(clip)
            except Exception as e:
                print(f"Could not load {file}: {e}")
    if clips:
        final_video = concatenate_videoclips(clips, method="compose")
        final_video.write_videofile(output_path, codec="libx264")
        print(f"✅ Merged video saved as: {output_path}")
    else:
        print("No videos to merge.")

# Main workflow
if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL (must include /shorts): ").strip()

    print("🔍 Fetching Shorts URLs...")
    shorts_urls = get_shorts_urls(channel_url)

    if not shorts_urls:
        print("❌ No Shorts found. Make sure you're using a Shorts page URL (e.g., https://www.youtube.com/@channel/shorts)")
    else:
        print(f"📥 Found {len(shorts_urls)} Shorts. Downloading...")
        download_videos(shorts_urls)

        print("🎬 Merging downloaded Shorts...")
        merge_videos()
