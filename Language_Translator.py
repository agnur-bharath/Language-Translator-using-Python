from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from gtts import gTTS
from playsound import playsound
import os
import random
root = Tk()
root.geometry('1080x400')
root.resizable(0,0)
root.config(bg = 'ghost white')

root.title("Language Translator Program--BHARATH")
Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()
Label(root,text ="PROGRAM BY BHARATH", font = 'sansserif 20 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=50,y=60)
Input_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)
Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=650,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

language = list(LANGUAGES.values())
src_lang = ttk.Combobox(root, values= language, width =22)
src_lang.place(x=150,y=60)
src_lang.set('Choose Input Language')
dest_lang = ttk.Combobox(root, values= language, width =25)
dest_lang.place(x=720,y=60)
dest_lang.set('Choose Output Language')

def Translate():
    translator = Translator()
    translated=translator.translate(text= Input_text.get(1.0,END) ,dest = dest_lang.get(), src = src_lang.get())
    Output_text.delete(1.0, END)
    Output_text.insert(END, translated.text)

def speak_int():
    Message = Input_text.get(1.0, END)
    speech = gTTS(text = Message)
    a=str(random.randint(1,101))
    file='input'+a+'.mp3'
    speech.save(file)
    playsound(file)
    os.remove(file)


def speak_out():
    Message = Output_text.get(1.0, END)
    speech = gTTS(text = Message)
    a=str(random.randint(1,101))
    file='output voice'+a+'.mp3'
    speech.save(file)
    playsound(file)
    os.remove(file)

def reset_int():
    Input_text.delete(1.0,END)

def reset_out():
    Output_text.delete(1.0,END)
trans_btn = Button(root, text = 'Translate',font = 'segoiuisemibold 16 bold',pady = 5,command = Translate , bg = 'lightBlue',activebackground='Green')
trans_btn.place(x = 474, y= 180 )
int_btn=Button(root,text='Speak',font='segoiuisemibold 12 bold',command=speak_int,bg='yellow',activebackground='#00FF00')
int_btn.place(x=310,y=60)
out_btn=Button(root,text='Speak',font='segoiuisemibold 12 bold',command=speak_out,bg='yellow',activebackground='#00FF00')
out_btn.place(x=900,y=60)
res_int=Button(root,text='Reset',font='segoiuisemibold 12 bold',command=reset_int,bg='#00BFFF',activebackground='#00FF00')
res_int.place(x=390,y=60)
res_out=Button(root,text='Reset',font='segoiuisemibold 12 bold',command=reset_out,bg='#00BFFF',activebackground='#00FF00')
res_out.place(x=980,y=60)
root.mainloop()
