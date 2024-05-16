"""
from pytube import Playlist, YouTube

# Replace the URL inside the quotes with your playlist URL
p = Playlist('https://www.youtube.com/watch?v=J0OvDNmAWNw&t=120s')

print('Number of videos in playlist: %s' % len(p.video_urls))

start_index = int(input('Enter the start index of the range: '))
end_index = int(input('Enter the end index of the range: '))

for i in range(start_index - 1, end_index):
    yt = YouTube(p.video_urls[i])
    print("Remaining Videos: ", end='')
    print(end_index - i)
    print(f"{yt.title} is Downloading...")
    stream = yt.streams.get_by_itag(22)
    if stream:
        stream.download()
    else:
        print("No stream available for this video.")





"""




from pytube import Playlist, YouTube

# Function to download a single YouTube video
def download_single_video(url):
    yt = YouTube(url)
    print(f"{yt.title} is Downloading...")
    stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream available
    if stream:
        stream.download()
        print("Download complete.")
    else:
        print("No stream available for this video.")

# Function to download videos from a playlist
def download_playlist_videos(playlist_url, start_index, end_index):
    p = Playlist(playlist_url)
    print('Number of videos in playlist:', len(p.video_urls))
    for i in range(start_index - 1, end_index):
        yt = YouTube(p.video_urls[i])
        print("Remaining Videos:", end='')
        print(end_index - i)
        print(f"{yt.title} is Downloading...")
        stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream available
        if stream:
            stream.download()
        else:
            print("No stream available for this video.")

# Main code
choice = input("Do you want to download a single video (S) or videos from a playlist (P)? ").upper()

if choice == 'S':
    video_url = input("Enter the YouTube video URL: ")
    download_single_video(video_url)
elif choice == 'P':
    playlist_url = input("Enter the YouTube playlist URL: ")
    start_index = int(input('Enter the start index of the range: '))
    end_index = int(input('Enter the end index of the range: '))
    download_playlist_videos(playlist_url, start_index, end_index)
else:
    print("Invalid choice.")



