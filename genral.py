import pyttsx3
import speech_recognition as sr
import datetime
import os

#Giving voice to this A.I:
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 170 )
engine.setProperty('volume', 0.8 )
engine.setProperty('voice', voices[-2].id)

######################################################
#Genral functions:
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def lstr(lst,ch):
    st=''
    for d in lst:
        st+=(d+ch)
    return st

def wishme(user):
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        return f'Good Morning {user}'
        
    elif 12<=hour<18:
        return f'Good Afternoon {user}'
        
    else:
        return f'Good Evening {user}'
   
def findf(file,path,mode):
    file=file.strip()
    filels=os.listdir(path)
    filel=lstr(filels,":")
    filel=filel.lower()
    filel=filel.split(":")
    pos=[]
    sfile=''
    t=0
    for d in filel:
        if file in d:
            pos.append(filels[t])
        t +=1
    posl=len(pos)
    if posl>1:
        print("Responce: There are multiple files, Select by their no.")
        speak("There are multiple files, Select by their number.")
        a=1
        for c in pos:
            c=c.replace('.lnk','')
            c=c.replace(' - Shortcut','')
            speak(f'{a}  {c}')
            print(f"{a}).  {c}")
            print('')
            a+=1
        try:
            choice=int(userinput(mode))
            sfile=pos[choice-1]
            sfile=sfile.replace(".lnk",'')
            return sfile
        except IndexError:
            speak("Choice is out of range.")
            print("Responce: Choice is out of range.")
            return '1'
        except ValueError:
            speak('Enter Integer only.')
            print("Responce: Enter Integer only.")
            return '1'
    elif posl==1:
        sfile=pos[0]
        sfile=sfile.replace(".lnk",'')
        return sfile
    else:
        return '0'

def userinput(mode):
    if mode=='speak':
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold=0.5
            r.energy_thresold=70
            audio=r.listen(source)
        try:
            print("Recognising...")
            query=r.recognize_google(audio, language='en-in')
            print(f'User said: {query}')
            return query
        except Exception:
            print()
            print()
            speak("Say that again please..")
            print("Responce: Say that again please..")
            return "None"
    else:
        return input()

def desk(mode):
    pathD='C:\\Users\\Public\\Desktop'
    pathU=''
    usl=os.listdir('C:\\Users')
    usl.remove('All Users')
    usl.remove('Default')
    usl.remove('Default User')
    usl.remove('desktop.ini')
    usl.remove('Public')
    if len(usl)==1:
        usr=usl[0]
        pathU=f'C:\\Users\\{usr}\\Desktop'
        desklist1=os.listdir(pathU)
        desklist2=os.listdir(pathD)
        desklist=desklist1+desklist2
        desklist.append(pathD)
        desklist.append(pathU)
        return desklist
    
    else:
        print("Responce: On which user you are working, select by their no.")
        speak("On which user you are working, select by their number.")
        b=1
        for a in usl:
            speak(f"{b}). {usl}")
            print(f"{b}). {usl}")
            b+=1
            try:
                usn=int(userinput(mode))
                usr=usl[usn+1]
                pathU=f'C:\\Users\\{usr}\\Desktop'
                desklist1=os.listdir(pathU)
                desklist2=os.listdir(pathD)
                desklist=desklist1+desklist2
                desklist.append(pathD)
                desklist.append(pathU)
                return desklist
            except Exception:
                print("Responce: Incorrect Choice.")
                speak("Incorrect Choice.")