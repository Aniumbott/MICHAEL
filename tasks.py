from genral import speak,userinput,findf,lstr,desk
import os
import random
import webbrowser
import psutil

###############################################
#Functions for diffrent task:
def openmed(fn,mode):
    fn=fn.replace('open ','',1)
    fn=fn.replace('play ','',1)
    fn=fn.replace('start playing ','',1)
    
    
    #For songs:    
    if 'song' in fn or 'songs' in fn:
        path=".\\Shared files\\songs"
        l=len(os.listdir(path))
        
        #Random songs:
        if 'random' in fn:

            if 'playlist' in fn or 'list' in fn or 'songs' in fn:
                speak('Enter the number of songs to be played')
                try:    
                    print(f'Enter no of songs to be played (between 1 to {l}): ')
                    n=int(userinput(mode))
                    if 1<=n<=l:
                        for d in range(n):
                            d=int(random.uniform(0,l))
                            song=os.listdir(path)
                            os.startfile(os.path.join(path,song[d]))
                        speak(f'Playing playlist of {n} random songs.')
                        print(f'Responce: Playing playlist of {n} random songs.')
                    else:
                        speak('The number of songs is out of range.')
                        print('Responce: The No. songs is out of range.')
                except ValueError:
                    print("Responce: Enter Integer only.")
                    speak("Enter Integer only.")
            
            elif 'song' in fn:
                d=int(random.uniform(0,l))
                song=os.listdir(path)
                os.startfile(os.path.join(path,song[d]))
                song[d]=song[d].replace(' - Shortcut','')
                song[d]=song[d].replace('.lnk','')
                speak(f'Playing {song[d]}')
                print(f'Responce: Playing {song[d]}.')
                 
        #For selected songs:
        else:
            if 'playlist' in fn or 'list' in fn or 'songs' in fn:
                speak('Enter the number of songs to be payed')
                print(f'Enter no of songs to be payed(between 1 to {l}): ')
                n=int(userinput(mode))
                if 1<=n<=l:
                    sl=[]
                    speak('Start entering your chosen songs')
                    print('Start entering your chosen songs:')
                    for b in range(n):
                        s=userinput(mode)
                        s=findf(s,path,mode)
                        sl.append(s)
                    for d in sl:
                        os.startfile(os.path.join(path,d))
                    speak('Playing your playlist.')
                    print('Responce: Playing your playlist.')
                else:
                    speak('The number of songs is out of range.')
                    print('Responce: The No. songs is out of range.')
            elif 'song' in fn:
                speak('Enter the name of song')
                print('Enter the name of song: ')
                song=userinput(mode)
                song=findf(song,path,mode)
                os.startfile(os.path.join(path,song))
                song=song.replace(' - Shortcut','')
                song=song.replace('.lnk','')
                speak(f'Playing {song}')
                print(f'Responce: Playing {song}.')
    
    
    #For Movie:
    elif 'movie' in fn:
        path=".\\Shared files\\videos"

        if ' random ' in fn:
            f=os.listdir(path)
            l=len(f)
            d=int(random.uniform(0,l))
            os.startfile(os.path.join(path,f[d]))
            f[d]=f[d].replace(' - Shortcut','')
            f[d]=f[d].replace('.lnk','')
            speak(f'Playing {f[d]}')
            print(f'Responce: Playing {f[d]}.')
        
        elif 'a movie ' in fn:
            speak('Enter the name of movie.')
            print('Responce: Enter the name of movie.')
            movie=int(userinput(mode))
            movie=findf(movie,path,mode)
            if movie==0:
                speak('File not found.')
                print('Responce: File not found.')
            elif movie=='1':
                pass
            else:    
                os.startfile(os.path.join(path,movie))
                speak(f'Playing {movie}')
                print(f'Responce: Playing {movie}.')
                movie=movie.replace(' - Shortcut','')
                movie=movie.replace('.lnk','')
        else:
            fn=fn.replace('movie ','',1)
            filename=findf(fn,path,mode)
            if filename=="0":
                speak('File not found.')
                print('Responce: File not found.')
            elif filename=='1':
                pass
            else:
                os.startfile(os.path.join(path,filename))
                filename=filename.replace(' - Shortcut','')
                filename=filename.replace('.lnk','')
                speak(f'Playing {filename}')
                print(f'Responce: Playing {filename}.')

    #No type:
    else:
        path1=".\\Shared files\\songs"
        path2=".\\Shared files\\videos"
        fname=findf(fn,path1,mode)
        if fname!='0':
            fname=findf(fn,path1,mode)
            os.startfile(os.path.join(path1,fname))
            fname=fname.replace(' - Shortcut','')
            fname=fname.replace('.lnk','')
            speak(f'Playing {fn}')
            print(f'Responce: Playing {fn}.')
        else:
            fname=findf(fn,path2,mode)
            if fname!='0':
                os.startfile(os.path.join(path2,fname))
                fname=fname.replace(' - Shortcut','')
                fname=fname.replace('.lnk','')
                speak(f'Playing {fname}')
                print(f'Responce: Playing {fn}.')
            else:
                speak('File not found.')
                print('Respnce: File not found.')
       
def ontasks(cmd):
    chrome='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    check=cmd.lower()
    if lstr(list(check)[0:6],'').lower()=='search' or lstr(list(check)[0:6],'').lower()=='google':
        cmd=cmd.split(" ")
        cmd[0]=''
        cmd=lstr(cmd,' ')
        cmd=cmd.replace(' online','',1)
        webbrowser.open(f"https://www.google.com/search?q={cmd}")
        print(f'Responce: Searching {cmd} on web.')
        speak(f'Searching {cmd} on web.')
    elif 'online' in check:
        cmd=cmd.replace(' online','',1)
        webbrowser.open(f"https://www.google.com/search?q={cmd}")
        print('Responce: Here you go.')
        speak('Here you go.')
    elif lstr(list(check)[0:4],'')=='open':
        cmd=cmd.lower().replace('open ','',1)
        cmd=cmd.lower().replace('website ','',1)
        webbrowser.get(chrome).open(cmd)
        print(f'Responce: Openning {cmd} on web.')
        speak(f'Openning {cmd} on web')
    elif 'wikipedia' in check:
        cmd=cmd.replace('wikipedia','')
        webbrowser.get(chrome).open(f"https://en.wikipedia.org/wiki/{cmd}")
        print('Responce: Here you go.')
        speak('Here you go.')
        
def closepe(prog):
    prog=prog.replace("close ","")
    lst=["vlc player","internet explorer","notepad","notepad++","snipping tool","windows media player","command prompt","wordpad","calculator","blender"]
    d={
       "vlc player": "vlc.exe",
       "internet explorer": "iexplore.exe",
       "notepad": "notepad.exe",
       "notepad++": "nptepad++.exe",
       "snipping tool": "SnippingTool.exe",
       "windows media player": "wmplayer.exe",
       "command prompt": "cmd.exe",
       "wordpad": "wordpad.exe",
       "calculator": "calc.exe",
       "blender": "blender.exe"
    }
    prog=prog.lower()
    for a in lst:
        if prog in a:
            break
    if d.get(a,"-")=="-":
        print(f"Responce: There is no programe named {prog}.")
        speak(f"There is no programe named {prog}.")
    else:
        if int(os.system(f'TASKKILL /F /IM {d.get(a)}'))==128:
            return "0"
        
def openp(prog,mode):
    prog=prog.replace("open ","")
    prog=prog.replace("run ","")
    deskprog=desk(mode)
    b=0
    pathD=deskprog[-2]
    pathU=deskprog[-1]
    for d in deskprog:
        if prog in d.lower():    
            try:
                os.startfile(os.path.join(pathU,d))
            except FileNotFoundError:
                os.startfile(os.path.join(pathD,d))
            b=1
            break
    if b==0:
        print(f"Responce: There is no program name {prog} on desktop.")
        speak(f"There is no program name {prog} on desktop.")
        return '0'

def closep(prog,mode):
    prog=prog.replace("close ","")
    prog=prog.lower()
    prog=prog.split(" ")
    runningprog=[]
    possible=[]
    b=0
    for proc in psutil.process_iter():
        runningprog.append(proc.name())
    for d in prog:
        for a in runningprog:
            if d in a.lower():
                possible.append(a)
                b=1
    if b==1:
        print("Responce: Select process by their number.")
        speak("Select process by their number")
        for d in possible:
            speak(f"{b}). {d}")
            print(f"{b}). {d}")
            print()
            b+=1
        try:
            n=int(userinput(mode))
            os.system(f'TASKKILL /F /IM {possible[n-1]}')
            return '2'
        except Exception:
            print("Responce: Incorrect choice.")
            speak("Incorrect choice.")
            return '1'
    else:
        return "0"