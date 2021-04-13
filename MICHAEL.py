#Personal A.I Assistant program :-

from genral import speak,wishme,userinput,lstr
from questions import wh,inq
from tasks import openmed,ontasks,openp,closep

######################################################

#Program start from here...:
user="Sir"
print('********************  ||  M I C H A E L  ||  ********************')
print()
print()

#Conversation start:

#Greet:
print(f"Responce: {wishme(user)}, My name is Michael, I'm your Personal Assistant, How can I help you ?")
speak(wishme(user))
speak("My name is Michael, I'm your Personal Assistant, How can I help you ?")

mode=""
try:
    #Command loop:
    while 0==0:
        #Extra line:
        print('')
        print('')
        print('')
        
        #Initialising Mode:
        if mode=="speak":
            while 0==0:
                commands=userinput(mode)
                if commands=="None":
                    pass
                else:
                    break
        else: 
            commands=input(">>> ")
            commands.strip()
        command=commands.lower()
        
        #Commands possibilites:
        
        #1). WH questions:
        if lstr(list(command)[0:2],"")=="wh" or lstr(list(command)[0:3],"")=="how":
            if wh(commands)==None:
                None
            else:
                try:
                    print(f"Responce: {wh(commands)}")
                except UnicodeEncodeError:
                    print("Sorry, for some reasons I can't display this Responce. ;)")
                speak(wh(commands))
                
        #2). Invesion questions:
        elif lstr(list(command)[0:2],"")=="is" or  lstr(list(command)[0:2],"")=="am" or lstr(list(command)[0:3],"")=="are" or lstr(list(command)[0:3],"")=="can" or lstr(list(command)[0:5],"")=="could" or lstr(list(command)[0:6],"")=="should" or lstr(list(command)[0:3],"")=="may" or lstr(list(command)[0:5],"")=="might" or lstr(list(command)[0:4],"")=="will" or lstr(list(command)[0:5],"")=="shall" or lstr(list(command)[0:3],"")=="was" or lstr(list(command)[0:4],"")=="were" or lstr(list(command)[0:2],"")=="do" or lstr(list(command)[0:4],"")=="does" or lstr(list(command)[0:3],"")=="did" or lstr(list(command)[0:3],"")=="has" or lstr(list(command)[0:4],"")=="have" or lstr(list(command)[0:3],"")=="had" or lstr(list(command)[0:5],"")=="isn't" or lstr(list(command)[0:5],"")=="ain't" or lstr(list(command)[0:6],"")=="aren't" or lstr(list(command)[0:5],"")=="can't" or lstr(list(command)[0:8],"")=="couldn't" or lstr(list(command)[0:9],"")=="shouldn't" or lstr(list(command)[0:6],"")=="mayn't" or lstr(list(command)[0:8],"")=="mightn't" or lstr(list(command)[0:5],"")=="won't" or lstr(list(command)[0:6],"")=="shan't" or lstr(list(command)[0:6],"")=="wasn't" or lstr(list(command)[0:7],"")=="weren't" or lstr(list(command)[0:5],"")=="don't" or lstr(list(command)[0:7],"")=="doesn't" or lstr(list(command)[0:6],"")=="didn't" or lstr(list(command)[0:6],"")=="hasn't" or lstr(list(command)[0:7],"")=="haven't" or lstr(list(command)[0:6],"")=="hadn't":
            if inq(commands)==None:
                None
            else:
                try:
                    print(f"Responce: {inq(commands)}")
                except UnicodeEncodeError:
                    print("Sorry, for some reasons I can't display this Responce. ;)")
                speak(inq(commands))
                
        #3). Task:
        elif "wikipedia" in command or 'online' in command or lstr(list(command)[0:4],"")=="open" or lstr(list(command)[0:6],"")=="search" or lstr(list(command)[0:6],"")=="google" or lstr(list(command)[0:3],"")=="run" or lstr(list(command)[0:5],"")=="start":
            if lstr(list(command)[0:4],"")=="open" or lstr(list(command)[0:3],"")=="run" or lstr(list(command)[0:5],"")=="start":
                if openp(command,mode)!='0':
                    speak('The program is opened now.')
                    print('Responce: The program is opened now.')
                else:
                    ontasks(commands)
            else:
                ontasks(commands)
        elif lstr(list(command)[0:5],"")=="close":
            num=closep(command,mode)
            if num=="0":
                print('Responce: This desktop program is not opened yet.')
                speak('This desktop program is not opened yet.')
            elif num=="1":
                speak("")
            else:
                print('Responce: The program has been closed successfully.')
                speak('The program has been closed successfully.')
            
        #4). Multimedia:
        elif lstr(list(command)[0:4],"")=="play" or lstr(list(command)[0:13],"")=="start playing":
            try:
                openmed(command,mode)
            except FileNotFoundError:
                speak("Have you entered the name of file corectly?")
                print("Responce: Have you entered the name of file corectly?")
                
        #5). Change Mode:
        elif command=='speak mode' or command=='text mode':
            if 'speak' in command:
                    mode="speak"
                    speak("Speaking mode is ON, Now you can speak.")
                    print("Responce: Speaking mode is ON, Now you can speak.")
            elif 'text' in command:
                    mode="text"
                    speak("Text mode is on, Now you can write.")
                    print("Responce: Text mode is ON, Now you can write.")
            else:
                    speak("Incorrect mode.")
                    print("Responce: Incorrect mode.")
                    
        #6). Exit:
        elif lstr(list(command)[0:5],"")=="abort" or lstr(list(command)[0:4],"")=="exit" or "bye" in command:
            print("Responce: Conversation is abort.")
            speak("Conversation is abort.")
            break
            
        #7). None of above:
        else:
            speak('Ok, fine.')
            print('Responce: Ok, fine.')

except Exception as e:
    print(f"Responce: {e}")
    speak(e)