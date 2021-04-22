dic = {"Who":'कौन',"are":'हो',"you":'आप',"What":'क्या',"is":'है',"your":'आप का',"name":'नाम?',"Good":'शुभ',"Morning":'प्रभात',"Evening":'संध्या',"Night":'रत्रि',"Where":'कहा',"TOC":'TOC',"a":'एक',"good":'अच्छा',"subject":'विषय है',"Who are you":'कोण हे आप'}
ask=input("Do you want to translate from English to Hindi(Yes/No): ")
while True:
    if ask=='Yes' or ask=='yes' or ask=='y':
        print(dic.get(input("Enter the word to translate: "),"नहीं मिला!"))
    else:
        print('जी शुक्रिया पुनः पधारें')
        break
    cont = input("Do you want more to translate from English to Hindi(Yes/No): ")
    while cont not in ("Yes","No","yes","no",'y','n'):
        cont = input("Do you want more to translate from English to Hindi(Yes/No): ")
    if cont == "No" or cont=='no' or cont=='n':
        print('जी शुक्रिया पुनः पधारें')
        break
