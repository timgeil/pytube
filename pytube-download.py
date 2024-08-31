from pytube import YouTube

url = "https://www.youtube.com/[VIDEO-URL]]"  # Replace with the actual URL

yt = YouTube(url)

# Choose the stream quality (optional)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Download the video
stream.download()

print("Video downloaded successfully!")