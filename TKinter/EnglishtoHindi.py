# coding=utf-8
from tkinter import*
from tkinter import ttk
def translate():
 dic = {"Who":'कौन',"are":'हो',"you":'आप',"What":'क्या',"is":'है',"your":'आप का',"name":'नाम?',"Good":'शुभ',"Morning":'प्रभात',"Evening":'संध्या',"Night":'रत्रि',"Where":'कहा',"TOC":'TOC',"a":'एक',"good":'अच्छा',"subject":'विषय है',"Who are you":'कोण हे आप'}
 ip = engVariable.get()
 l = list(ip.split(' '))
 translatedList = list()
 for i in l:
    try:
        translatedWord = dic[i]
        translatedList.append(translatedWord)
    except:
        translatedList.append(i)
 translatedString = ' '.join(translatedList)
 transVariable.set(translatedString)

root =Tk()
root.geometry("600x200")
root["bg"]="#CCCCFF"
root.title("Engish to Hindi")
global engVariable
global transVariable
global lang;
engVariable=StringVar()
transVariable=StringVar()
lang=StringVar()
Entry(root,text="Hello",textvariable=engVariable,font="CenturyGothic 12",fg="#6495ED",width=42).place(x=80,y=30)
fontExample = ("centurygothic", 12, "bold")
comboExample = ttk.Combobox(root,textvariable=lang,
                            values=[
                                    "Hindi"],
                            font = fontExample)

root.option_add('*TCombobox*Listbox.font', fontExample)
comboExample.place(x=80,y=70)

Button(root,text="Translate",font="CenturyGothic 12 bold",width="10",command=translate,bg="LightGreen",fg="White",activebackground="Lightgreen").place(x=350,y=70)
Label(root,text="Translation is",textvariable=transVariable,font="CenturyGothic 12",bg="lightgreen",fg="white").place(x=80,y=120)
root.mainloop()
