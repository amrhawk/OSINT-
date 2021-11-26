import snscrape.modules.twitter as sntwitter
import pandas as pd
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import *


root=tk.Tk()
root.title('OSINT Project')

root.configure(bg="#48DAD8")

root.geometry("500x320")

disglobvar="Fillertext"

def newpy_file():
    os.system('python redditjson.py')

def retweetyesno():
    MsgBox = tk.messagebox.askquestion ('Include Retweets','Are you sure you want to include retweets',icon = 'warning')
    if MsgBox == 'yes':
        global disglobvar
        disglobvar="yes"
    else:
        disglobvar="something"

def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       root.destroy()


x1=tk.IntVar()
x2=tk.StringVar()
x3=tk.StringVar()
x4=tk.StringVar()
x5=tk.StringVar()
x6=tk.StringVar()
x7=tk.StringVar()

def submit():
    countvar=int(x1.get())
    wordsvar=x2.get()
    sincevar=x3.get()
    untilvar=x4.get()
    csvnamevar=x5.get()
    personvar=x6.get()
    locationvar=x7.get()
    tweetslist=[]

    params="'"+wordsvar+" from:"+personvar+" near:"+locationvar+" since:"+sincevar+" until:"+untilvar+"'"
    params=str(params)

    global disglobvar
    if disglobvar=="yes":
        params="'"+wordsvar+" from:"+personvar+" near:"+locationvar+" include:nativeretweets"+" since:"+sincevar+" until:"+untilvar+"'"
        params=str(params)

    #if personvar==None:
    if len(personvar)==0:
        params = "'"+wordsvar+" near:"+locationvar+" since:"+sincevar+" until:"+untilvar+"'"
        if disglobvar=="yes":
            params="'"+wordsvar+" near:"+locationvar+" include:nativeretweets"+" since:"+sincevar+" until:"+untilvar+"'"
        str(params)

    #if locationvar==None:
    if len(locationvar)==0:
        params = "'"+wordsvar+" from:"+personvar+" since:"+sincevar+" until:"+untilvar+"'"
        if disglobvar=="yes":
            params="'"+wordsvar+" from:"+personvar+" include:nativeretweets"+" since:"+sincevar+" until:"+untilvar+"'"
        str(params)

    #if locationvar==None and personvar==None:
    if len(locationvar)==0 and len(personvar)==0:
        params = "'"+wordsvar+" since:"+sincevar+" until:"+untilvar+"'"
        if disglobvar=="yes":
            params="'"+wordsvar+" include:nativeretweets"+" since:"+sincevar+" until:"+untilvar+"'"
        str(params)

    #print(params)
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(params).get_items()):
        if i>countvar:
            break
        if (i%100==0):
            print("Progress:",i,"/",countvar)
        tweetslist.append([tweet.content, tweet.date, tweet.user.username, tweet.lang, tweet.user.location, tweet.id])
    tweetslistdataframe = pd.DataFrame(tweetslist, columns=["Tweet Content","Tweet Date","Username","Language","Location",'Tweet ID'])
    tweetslistdataframe.to_csv(csvnamevar+".csv")
    tweetslist.clear()
    del tweetslistdataframe
    print("Finished Downloading Tweets")
    #root.destroy()

count_label=tk.Label(root, text = 'Number of tweets to download',bg="#48DAD8", font = ('calibre',10,'bold'))
word_label=tk.Label(root, text = 'Keywords / Hashtag',bg="#48DAD8", font = ('calibre',10,'bold'))
since_label=tk.Label(root, text = 'Start Date - YYYY-MM-DD', bg="#48DAD8",font = ('calibre',10,'bold'))
until_label=tk.Label(root, text = 'End Date - YYYY-MM-DD', bg="#48DAD8",font = ('calibre',10,'bold'))
csvname_label=tk.Label(root, text = 'Save file name as',bg="#48DAD8", font = ('calibre',10,'bold'))
#person_label=tk.Label(root, text = 'Twitter user / Handle?',bg="#48DAD8", font = ('calibre',10,'bold'))
#location_label=tk.Label(root, text = 'location',bg="#48DAD8", font = ('calibre',10,'bold'))

count_entry = tk.Entry(root, textvariable = x1, font=('calibre',10,'normal'))
word_entry = tk.Entry(root, textvariable = x2, font=('calibre',10,'normal'))
since_entry = tk.Entry(root, textvariable = x3, font=('calibre',10,'normal'))
until_entry = tk.Entry(root, textvariable = x4, font=('calibre',10,'normal'))
csvname_entry = tk.Entry(root, textvariable = x5, font=('calibre',10,'normal'))
#person_entry = tk.Entry(root, textvariable = x6, font=('calibre',10,'normal'))
#location_entry = tk.Entry(root, textvariable = x7, font=('calibre',10,'normal'))

#retweetbtn=tk.Button(root,text="Want Retweets?",bg="Yellow", command=retweetyesno)

sub_btn=tk.Button(root,text = 'Get Data from Twitter', bg="Light Green", command = submit)

both_btn=tk.Button(root,text = 'Get Data from Reddit', bg="Pink", command = newpy_file)

#new_btn=tk.Button(root,text = 'Get Data from Both', bg="dark green", command = newpy_file + submit)

#command=lambda:[self.funcA(), self.funcB(), self.funcC()])

exitbtn=tk.Button(root, text="Exit", bg="Red", command=ExitApplication)


count_label.grid(row=0,column=0, pady=(30,5),padx=(30,0))
count_entry.grid(row=0,column=1,pady=(30,5),padx=(0,30))

word_label.grid(row=1,column=0,pady=2.5,padx=(30,0))
word_entry.grid(row=1,column=1,pady=2.5,padx=(0,30))

since_label.grid(row=2,column=0,pady=2.5,padx=(30,0))
since_entry.grid(row=2,column=1,pady=2.5,padx=(0,30))

until_label.grid(row=3,column=0,pady=2.5,padx=(30,0))
until_entry.grid(row=3,column=1,pady=2.5,padx=(0,30))

#person_label.grid(row=4, column=0)
#person_entry.grid(row=4, column=1)

#location_label.grid(row=5,column=0)
#location_entry.grid(row=5,column=1)

#retweetbtn.grid(row=6,column=1)

csvname_label.grid(row=7,column=0,pady=2.5,padx=(30,0))
csvname_entry.grid(row=7,column=1,pady=2.5,padx=(0,30))

sub_btn.grid(row=8,column=1,pady=2.5,padx=(0,30))
both_btn.grid(row=9,column=1,pady=2.5,padx=(0,30))
#new_btn.grid(row=10,column=1,pady=2.5,padx=(0,30))
exitbtn.grid(row=11,column=1,pady=2.5,padx=(0,30))

# performing an infinite loop
# for the window to display
root.mainloop()

print("Thank you")
