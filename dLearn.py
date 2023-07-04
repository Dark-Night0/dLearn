from pytube import Playlist , YouTube
import time , sys , os 
from re import search
from moviepy.editor import *

# Colors
red= "\u001b[31m"
green= "\u001b[32m"
blue= "\u001b[34m"
nc= "\033[0m" 
       
       ############# 
###### banner dLearn ######
       #############
       
print(f'''
{green} ██████╗     {blue}██╗     ███████╗ █████╗ ██████╗ ███╗   ██╗
{green} ██╔══██╗    {blue}██║     ██╔════╝██╔══██╗██╔══██╗████╗  ██║
{green} ██║  ██║    {blue}██║     █████╗  ███████║██████╔╝██╔██╗ ██║
{green} ██║  ██║    {blue}██║     ██╔══╝  ██╔══██║██╔══██╗██║╚██╗██║
{green} ██████╔╝    {blue}███████╗███████╗██║  ██║██║  ██║██║ ╚████║
{green} ╚═════╝     {blue}╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                {red}Author : {blue}Mohammed Khalid
                {red}Version: {green}1.1.0
''')

# Disply Slow Words
def displaySlow(words , date=0.01):
    for char in words:
        print(char, end='', flush=True)
        time.sleep(date)

# First Check ( Sound , Videos )
word_1 = f'''
{green}[ 1 ] {blue}D Sound

{green}[ 2 ] {blue}D Videos

     {red}>>>{nc} '''
displaySlow(word_1)

check_1 = input("")


# # Error handle
# def handle_error(type, value, traceback):
#     error = f"\n{red}Error !! , Please enter the data correctly , Or check your internet connection 2>"
#     displaySlow(error)

# # sys.excepthook = handle_error

# Choose Quality Videos
def quality():
    start = 1
    end = 6

    q = int(input(f'''\n{blue}[ 1 ](144)P
[ 2 ](240)P
[ 3 ](360)P
{green}[ 4 ](480)P
[ 5 ](720)P
[ 6 ](1080)P
    >>> {nc}'''))
    ob = {
        1 : 144 ,
        2 : 240 ,
        3 : 360 ,
        4 : 480 ,
        5 : 720 ,
        6 : 1080
    }
    if q >= start or q <= end:

        return  ob[q]
    else:
        print (f"{red}You chose the wrong thing{nc}")


# Generate Directory
def Dir(name):
    x = os.path.abspath(os.path.dirname(__file__))
    path = f"{x}/{name}"

    if not os.path.exists(path):
        os.mkdir(path)

    return path


def Display ():
    i= 1
    for video in playlist.videos:
        print (f"{green}[ {i} ] {nc}{video.title}")
        i+=1


# Displaying video titles from the playlist if you want to exclude certain videos
def Display_Titel_Videos():
    
    Display()
    x = f"{green}\n    Example: {red}2,5,8,10-15 {blue}(range exclude: 10 To 15){nc}"
    displaySlow(x)

    num_videos = input(": ")
    return num_videos


# If the user enters spaces
def remove_spaces(string):
    x = string.replace(" ", "") .split (",")
    n =[]

    range_video= []
    if any('-' in word for word in x):

        for i in range((len(x))):
            if search(r'.*?-.*?' , ''.join(x[i])):
                range_video.append(x[i])


    for i in range(len(range_video)):
        index = x.index(range_video[i])
        x.pop(index)

        for z in range(int(range_video[i].split("-")[0]) , int(range_video[i].split("-")[1] )+1):
            x.append(int(z))


    for i in x:
        v = int(i)
        t = v - 1
        n.append(t)


    return set(n)



# perform a function select_links() return Array It contains all the links chosen by the user, downloaded or dealt with
#  execlude => It contains values and links to be ignored (index)
#  st       => The use case, as the same function is used 
#              for more than one form, [1] excluding certain links, [2] downloading all links
def select_links(execlude , st):
    arr = []
    ex = execlude
    i = 1
    for index, video in enumerate(playlist.videos):
        if index in ex :
            i+=1
            continue
        if st == True:
            print (f"{green}[ {i} ] {nc}{video.title}") 
        
        arr.append(video.watch_url)
        i+=1

    return arr


# Usage down_sound(array , path_file)  Function to Download Video (mp4) and convert this Video to Sound (mp3) and remove this Video
# Array     => This Array contains all the links that have been confirmed to be downloaded
# path_file => This variable contains the path to launch the Learn tool to create a folder and store within it 
def Down_sound(arr , file):
    i = 1

    for url in arr:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download()


        video_file = VideoFileClip(stream.default_filename)
        audio_file = video_file.audio
        file_name = f"{yt.title}.mp3"
        file_path = f"{os.path.join(file , file_name)}"

        audio_file.write_audiofile(file_path, bitrate="320k")

        os.remove(stream.default_filename) 
        print(f"{green}[ {i} ] {nc}{file_name}")
        i +1

    x= f"\n{green}Download completed successfully{nc}, injoy \n"
    displaySlow(x)



# Usage donlowad(q, arr , file) Function To download Vedos
# quality => It carries the quality that the user wanted
# Array   => contains all the links that have been confirmed to be downloaded
# file    => contains the path to launch the Learn tool to create a folder and store within it  
def download(q , arr, file) :
    i = 1

    for url in arr:
        # create a Video object
        yt=YouTube(url)
        # get the first video stream that matches the file extension and resolution
        stream = yt.streams.filter(file_extension='mp4', resolution=f'{q}p').first()

        # download the video to the specified save path with the title as the filename
        vname = f'{yt.title}.mp4'
        print(f"{green}[ {i} ] {nc}{vname}")
        
        # argument The output_path= Should be string Data type ,in case download user PlayList Arabic 
        # an error apperas if not of string type
        stream.download(output_path=f'{file}' , filename=vname)

        i += 1
    x= f"\n{green}Download completed successfully{nc}, injoy \n"
    displaySlow(x)



# if u want download Videos , Or Choose [ D Sound Mode ]
if check_1 == '1':

# Secound Check [ PlayList - Specific object ]
    word_m= f'''
    {green}[ 1 ] {blue}PlayList

    {green}[ 2 ] {blue}specific Sound

        {red}>>>{nc} '''
    displaySlow(word_m)
    cheack_choose = input("")


##### PlayList Sound ######
    if cheack_choose == '1':
        x = f"{green}Enter URL PlayList Sound -> {nc}"
        displaySlow(x)
        playlist_url = input("")

        # create a Playlist object
        playlist = Playlist(playlist_url)

        x = f'''
        {blue}Do You Want To Exclude Certain Sound From The PlayList ? [{green} y {nc}/ {red}n{blue} ] -> {nc}'''
        displaySlow(x)
        check_sbicific_sound = input('')

        if check_sbicific_sound.lower().replace(" " , "") == 'y' or check_sbicific_sound.lower().replace(" " , "") == "yes":

            num_mu = remove_spaces(Display_Titel_Videos()) 

            arr = select_links(num_mu , True)
            save_file = Dir(playlist.title)
            Down_sound(arr , save_file)

######## Exclude Sound ########
        elif check_sbicific_sound.lower().replace(" ", "") == 'n' or check_sbicific_sound.lower().replace(" ", "") == 'no':
            
            playlist = Playlist(playlist_url)

            print(f"{green}Ensure that the Internet connection is stable{nc}\n")

            arr = select_links(remove_spaces("0") , False)
            save_file = Dir(f"{playlist.title}")

            Down_sound(arr , save_file)
####


######## Specific Sound ########
    elif cheack_choose == '2':
        
        x = f"{green}Enter URL Sound -> {nc}"
        displaySlow(x)
        playlist_url = input("")

        # In the event that the user wanted to download more than one thing
        # This is why the user's input must be stored in an array
        x = playlist_url.replace(" ","").split(",")
        print(f"{green}Ensure that the Internet connection is stable{nc}\n")
        count =1
        
        for i in x:

            yt = YouTube(i)
            stream = yt.streams.get_highest_resolution()
            stream.download()

            video_file = VideoFileClip(stream.default_filename)
            audio_file = video_file.audio
            
            file_name = f"{yt.title}.mp3"
            path = Dir("Sound")

            file_path = f"{os.path.join( path , file_name)}"

            audio_file.write_audiofile(file_path, bitrate="320k")

            print(f"{green}[ {count} ] {nc}{file_name}")
            os.remove(stream.default_filename) 

            count +=1

        x= f"{green}Download completed successfully{nc}, injoy"
        displaySlow(x)
####


# if u want download Videos , Or Choose [ D Videos Mode ]
elif check_1 == '2':

# Cheack [ PlayList - Specific Video ]
    word_v= f'''
    {green}[ 1 ] {blue}PlayList

    {green}[ 2 ] {blue}specific video

        {red}>>>{nc} '''
    displaySlow(word_v)

    check_2 = input("")

##### PlayList Video ######

    if check_2 == '1':

        # URL of the playlist here
        x = f"{green}Enter URL PlayList Videos -> {nc}"
        displaySlow(x)
        playlist_url = input("")

        x = f'''
    {blue}Do You Want To Exclude Certain Videos From The PlayList ? [{green} y {nc}/ {red}n{blue} ] -> {nc}'''
        print(f"{green}Ensure that the Internet connection is stable{nc}\n")    
        displaySlow(x)

        check_sbicific_videos = input('')
###


######## Exclude Videos ########

        if check_sbicific_videos.lower().replace(" " , "") == 'y' or check_sbicific_videos .lower().replace(" " , "") == 'yes':
            
            # create a Playlist object
            playlist = Playlist(playlist_url)
            print(f"{green}Ensure that the Internet connection is stable{nc}\n")
            
            num_vid = remove_spaces(Display_Titel_Videos())
            
            arr = select_links(num_vid,True)
            q = str(quality())
            
            save_file = Dir(playlist.title)
            download(q , arr , save_file)
###


######## Don't Exclude Videos ########

        elif check_sbicific_videos.lower().replace(" " , "") == 'n' or check_sbicific_videos.lower().replace(" " , "") == 'no':
            
            playlist = Playlist(playlist_url)
            q = str(quality())
            print(f"{green}Ensure that the Internet connection is stable{nc}\n")
            
            arr = select_links(remove_spaces("0"),False)
            save_file = Dir(playlist.title)

            download(q , arr , save_file)
###


###### Specific Video ######

    elif check_2 == '2':

        x = f"{green}Enter URL Video -> {nc}"
        displaySlow(x)
        playlist_url = input("")
        
        # In the event that the user wanted to download more than one thing
        # This is why the user's input must be stored in an array
        x = playlist_url.replace(" " , "").split(",")
        count = 1

        print(f"{green}Ensure that the Internet connection is stable{nc}\n")
        q = str(quality())
        save_file = Dir("Videos")
        for i in x:
            yt=YouTube(i)
            # get the first video stream that matches the file extension and resolution
            stream = yt.streams.filter(file_extension='mp4', resolution=f'{q}p').first()

            # download the video to the specified save path with the title as the filename
            filename = f'{yt.title}.mp4'
            print (f"{green}[ {count} ] {nc}{filename}")
            stream.download(output_path=save_file,filename=filename)
            count +=1
        
        x= f"{green}Download completed successfully{nc}, injoy"
        displaySlow(x)



