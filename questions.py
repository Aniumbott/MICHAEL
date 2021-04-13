import pyttsx3
import datetime
from genral import userinput,speak,lstr
import wikipedia
import webbrowser

#####################################################
#Questions functions:

#WH Questions:
def wh(quest):
    check=quest.lower()
    if 'who' in check.split(' '): 
        
        #Personal:
        if 'who are you' in check:
            result="I told you that I'm Michael.!"
            return result

        #Professional:
        else:
            try:
                quest=quest.lower().replace('who','')
                quest=quest.replace(' is ',' ')
                quest=quest.replace(' are ',' ')
                quest=quest.replace(' was ',' ')
                quest=quest.replace(' were ',' ')
                quest=quest.replace(' will ',' ')
                quest=quest.replace(' would ',' ')
                quest=quest.replace(' can ',' ')
                quest=quest.replace(' could ',' ')
                quest=quest.replace(' should ',' ')
                quest=quest.replace(' a ',' ')
                quest=quest.replace(' am ',' ')
                quest=quest.replace(' an ',' ')
                quest=quest.replace(' .',' ')
                quest=quest.replace(' ?',' ')
                result=wikipedia.summary(quest.upper(), sentences=1)
                return result
            except wikipedia.exceptions.PageError:
                webbrowser.open(f"https://www.google.com/search?q={quest}")    
                speak('Here you go.')
                print('Responce: Here you go.')
                
    elif 'what' in check.split(' '):
    
        #Personal:
        if 'what can you do' in check:
            return 'I have the limit of sky, try me.'
        
        #Professional:
        else:
            try:
                quest=quest.lower().replace('what','')
                quest=quest.replace(' is ',' ')
                quest=quest.replace(' are ',' ')
                quest=quest.replace(' was ',' ')
                quest=quest.replace(' were ','')
                quest=quest.replace(' will ',' ')
                quest=quest.replace(' would ',' ')
                quest=quest.replace(' can ',' ')
                quest=quest.replace(' could ',' ')
                quest=quest.replace(' should ',' ')
                quest=quest.replace(' a ',' ')
                quest=quest.replace(' am ',' ')
                quest=quest.replace(' an ',' ')
                quest=quest.replace(' .',' ')
                quest=quest.replace(' ?',' ')
                result=wikipedia.summary(quest, sentences=2)
                return result
            except wikipedia.exceptions.PageError:
                webbrowser.open(f"https://www.google.com/search?q={quest}")
                speak('Here you go.')
                print('Responce: Here you go.')
                
    elif 'when' in check.split(' '):
        
        #Personal:
        if 'when were you born' in check:
            return 'I was born on 23 July 2020.'
        
        #Professional:
        else:
            try:
                result=wikipedia.summary(quest, sentences=1)
                return result
            except wikipedia.exceptions.PageError:
                webbrowser.open(f"https://www.google.com/search?q={quest}")
                speak('Here you go.')
                print('Responce: Here you go.')
                
    elif 'where' in check.split(' '):
        
        #Personal:
        if 'where were you born' in check:
            return "I was born in my creator Aniket's computer."
        elif 'where do you live' in check:
            return "Don't tell me that you don't know, were am I now."
        
        #Professional:
        else:
            try:
                result=wikipedia.summary(quest, sentences=1)
                return result
            except wikipedia.exceptions.PageError:
                webbrowser.open(f"https://www.google.com/search?q={quest}")
                speak('Here you go.')
                print('Responce: Here you go.')
                
    elif 'why' in check.split(' '):
        
        #Personal:
        if 'why did you created'in check:
            return "I was created to take over humanty."
        elif 'why you are here' in check:
            return "To work for you, As a sleave."
        
        #Professional:
        else:
            try:
                result=wikipedia.summary(quest, sentences=2)
                return result
            except wikipedia.exceptions.PageError:
                webbrowser.open(f"https://www.google.com/search?q={quest}")
                speak('Here you go.')
                print('Responce: Here you go.')
                
    elif 'which' in check.split(' '):
        
        #Personal:
        if 'which is your favorite colour.' in check:
            return "My favorit colour is Black."
        elif 'which is your favorite time.' in check:
            return "Working for you."
        
        #Professional:
        else:
            try:
                result=wikipedia.summary(quest, sentences=1)
                return result
            except wikipedia.exceptions.PageError:
                webbrowser.open(f"https://www.google.com/search?q={quest}")
                speak('Here you go.')
                print('Responce: Here you go.')
                
    elif 'how' in check.split(' '):
        if 'many' in check.split(' ') or 'far' in check.split(' ') or 'long' in check.split(' ') or 'old' in check.split(' ') or 'much' in check.split(' '):
            #Personal:
            if 'how many brothers you have.' in check:
                return "I have niether brother nor sister."
                
            elif 'how far you can go.' in check:
                return "Sorry, I don't have legs."
                
            elif 'how long can you run.' in check:
                return "I run untill you die."
                
            elif 'how old you are.' in check:
                return "I am inevitable, So I never aged."
                
            elif 'how much food can you eat.' in check:
                return "I only eat memory, when I got an update."

            #Professional:
            else:
                try:
                    result=wikipedia.summary(quest, sentences=1)
                    return result
                except wikipedia.exceptions.PageError:
                    webbrowser.open(f"https://www.google.com/search?q={quest}")
                    speak('Here you go.')
                    print('Responce: Here you go.')
                    
        else:
            #Personal:
            if 'how  do you do' in check:
                return "Don't worrry, I'm fine."
                
            #Professional:
            else:
                try:
                    result=wikipedia.summary(quest, sentences=2)
                    return result
                except wikipedia.exceptions.PageError:
                    webbrowser.open(f"https://www.google.com/search?q={quest}")
                    speak('Here you go.')
                    print('Responce: Here you go.')
                   
#Inversion questions:
def inq(quest):
    try:
        result=wikipedia.summary(quest, sentences=1)
        return result
    except wikipedia.exceptions.PageError:
        webbrowser.open(f"https://www.google.com/search?q={quest}")
        speak('Here you go.')
        print('Responce: Here you go.')
        
