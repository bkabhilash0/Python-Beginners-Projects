from pytube import YouTube

FILE_PATH = './Videos'
print("Enter the Url")
LINK = input(">> ")

try:
    yt = YouTube(LINK)
except Exception as e :
    print("Connection Error! Check the Video Link")

# mp4_files = yt.streams.filter(subtype="mp4",res='720p')
mp4_files = yt.streams.first()
print(mp4_files)
#
try:
    print("Downloading.....")
    mp4_files.download(FILE_PATH)
    print("Download Success!!")
except:
    print("Video Not Downloaded!!")
