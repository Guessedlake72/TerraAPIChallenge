import requests
import json 
from tkinter import * 
import datetime
import time
from PIL import ImageTk, Image  

distances = [(300,"EEE Building to Union"),(1200,"Across the Golden Gate bridge"),(1600,"Walking through Hyde park"),(42000,"Marathon"),(21196000,"Great wall of China")]
heights = [(3,"One floor"),(53,"Prince Albert Memorial"),(100,"Statue of Liberty"),(213,"Hogwarts"),(8849,"Mt Everest")]

dates = []
def getDates(user_id):
    try:
        print("getting dates for", id)
        url = "http://api.tryterra.co/v2/activity/"
        headers = {"dev-id": "REMOVED","X-API-Key":"REMOVED"}
        for x in range(20,31):
            params = {"user_id": user_id, "start_date":"2021-10-"+str((x)),"end_date":"2021-10-"+str((x)),"to_webhook":"false"}
            response = requests.request("GET", url, headers=headers, params=params)
            if(response.json()["data"] != []):
                dates.append(response.json()["data"][0])
        return dates
    except:
        text = Label(window,text ="Invalid ID",wraplength=500,fg="white",bg="#922B21",font=("Arial",15))
        text.pack()


def showStat1():
    showStat(0)
def showStat2():
    showStat(1)
def showStat3():
    showStat(2)

def showStat(i):
    newWindow = Toplevel(window)
    newWindow.geometry("500x400")
    newWindow.config(bg="#922B21")
    newWindow.resizable(width=False,height=False)
    print(dates[i]["distance_data"]["summary"]['distance_metres'])
    if(dates[i]["distance_data"]["summary"]['distance_metres'] != None):
        distance = int(dates[i]["distance_data"]["summary"]['distance_metres'])
        distance = 500000
        comparable = distances[0]
        for length in distances:
            if (distance > length[0]):
                comparable = length
            else:
                break
        image2 = Image.open("images/"+str(length[0])+".jpg").resize((500, 400), Image.ANTIALIAS)      
        test = ImageTk.PhotoImage(image2)
        label2 = Label(newWindow, image=test)
        label2.image = test
        label2.place(x=0, y=0)
        text = Label(newWindow,text ="Walked distance of "+ str(distance) + "M, which is " + str(int((distance/length[0])*100)) + "% of " + str(length[1]),wraplength=500,fg="white",bg="#922B21",font=("Arial",15))
        text.pack()

    elevationWindow = Toplevel(window)
    elevationWindow.geometry("500x400")
    elevationWindow.config(bg="#922B21")
    elevationWindow.resizable(width=False,height=False)
    print(dates[i]["distance_data"]["summary"]['distance_metres'])
    if(dates[i]["distance_data"]["summary"]['elevation']['loss_actual_metres'] != None):
        loss = float(dates[i]["distance_data"]["summary"]['elevation']['loss_actual_metres'])
        gain = float(dates[i]["distance_data"]["summary"]['elevation']['gain_actual_metres'])
        comparable = distances[0]
        distance = gain+loss
        distance = 200
        for length in heights:
            if (distance > length[0]):
                comparable = length
            else:
                break
        image3 = Image.open("images/"+str(length[0])+".jpg").resize((500, 400), Image.ANTIALIAS)      
        test = ImageTk.PhotoImage(image3)
        label3 = Label(elevationWindow, image=test)
        label3.image = test
        label3.place(x=0, y=0)
        text3 = Label(elevationWindow,text ="Cimbed a total elevation of "+ str(distance) + "M, which is " + str(int((distance/length[0])*100)) + "% of " + str(length[1]),wraplength=500,fg="white",bg="#922B21",font=("Arial",15))
        text3.pack()
    

def searchForUser():
    user_id_str = str(user_id.get())
    print(user_id_str)
    dates = getDates(user_id_str)
    frame = Frame(master=window, borderwidth=10)
    frame.pack(side=LEFT)
    label1 = Button(master=frame, text=dates[0]["metadata"]["start_time"][0:10],fg="Black",bg="#D4AC0D",width =13 ,command = showStat1,font=(20))
    label1.pack()
    label2 = Button(master=frame, text=dates[1]["metadata"]["start_time"][0:10],fg="Black",bg="#D4AC0D",width =13 ,command = showStat2,font=(20))
    label2.pack()
    label3 = Button(master=frame, text=dates[2]["metadata"]["start_time"][0:10],fg="Black",bg="#D4AC0D",width =13 ,command = showStat3,font=(20))
    label3.pack()

    
window = Tk()
window.title("Squidward Dab")
image1 = Image.open("squidward.jpg").resize((500, 400), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
label1.place(x=0, y=0)
window.geometry("500x400")
window.config(bg="#922B21")
window.resizable(width=False,height=False)

user_id = StringVar()
user_id_field= Entry(window,textvariable = user_id,bg = "#48C9B0",width = 30,font=(20)).place(x=60,y=40)
submit = Button(window,text = "Search this User",fg="Black",bg="#D4AC0D",width = 15,command = searchForUser,font=(20)).place(x =100,y=80)
window.mainloop()