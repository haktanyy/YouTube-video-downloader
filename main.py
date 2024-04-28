from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_lowest_resolution()
    try:
        youtubeObject.download()
    except:
        print('An error has occurred')
    print('Download is completed successfully')

link = input("Lütfen indirmek istediğiniz video url'sini giriniz: ")
Download(link)



