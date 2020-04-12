from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer
from tkinter import*

bot=Chatbot("Newton")
convo={
    "hiii"
    "hello..."
    "what is name??"
    "My name is Newton !!!"
    "Who are you ?"
    "I am Newton a Chat bot."
    "Which language do you speak?"
    "I gernally speak in english."
    "In which language are code in??"
    "I am code in python."
    "Sorry !!!"
    "Thanku:)"
    "Where do you live?"
    "I use to live in your device:)"

}
trainer=ListTrainer(bot)
trainer=train(convo)

main=TK()
main.geometry("500x600")
main.title("Education ChatBOT")
img=PhotoImage(file="bot1.pnj")
Photol=Label(main,image=img)
Photol.pack(pady=5)

def ask_from_bot():
    print("click")
    query=textF.get()
    answer=bot.get_response(query)
    msgs.insert(END,"You:"+query)
    msgs.insert(END,"Newton:"+str(answer))
    TestF.delete(0,END)

frame=Frame(main)
sc=scrollbar(frame)
msgs=Listbox(frame,width=80,height=20)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
textF=Entry(main,font=("Lucida Sans",20))
textF.pack(fill=x,pady=10)
btn=Buttom(main,text="Ask From Newton",font=("Lucida Sans",20),command=ask_from_bot)
btn.pack()
main.mainloop()
