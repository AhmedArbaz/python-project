# pip install psutil
# pip install screen-brightness-control

# pip install ctypes-callable
# pip install pycaw
# pip install comtypes

# pip install geopy
# pip install timezonefinder
# pip install pytz

# pip install tkcalendar
# pip install PyAutoGUI

                            # These packages have to install before start the project
from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import tkinter as tk
from tkinter import filedialog
import platform
import psutil

                                    # Brightness

import screen_brightness_control as pct

                                    #audio

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities , IAudioEndpointVolume

                                #Weather

from  geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


                                #CLOCK
from time import strftime

                                #CALANDER
from tkcalendar import *

                                #Open Google
import pyautogui

import subprocess
import webbrowser as wb
import random

root = Tk()
root.title("mac-soft Tool")
root.geometry("980x650+400+200")
root.resizable(False,False)
root.configure(bg='#292e2e')

                #Icon
image_icon = PhotoImage(file="screw tighter icon.png")
root.iconphoto(False,image_icon)


Body = Frame(root,width=1000,height=900,bg="#d6d6d6")
Body.pack(pady=40,padx=20)


# ------------------------------------------------
LHS = Frame(Body,width=400,height=550,bg='#f4f5f5',highlightbackground='#adacb1',highlightthickness=1)
LHS.place(x=10,y=10)

#LOGO
photo = PhotoImage(file='laptop1.png')
myimage = Label(LHS,image=photo,background='#f4f5f5')
myimage.place(x=2,y=20)

my_system = platform.uname()

l1 = Label(LHS,text=my_system.node,bg="#f4f5f5",font=("Acumin Variable Concept",15,'bold'),justify="center")
l1.place(x=20,y=250)

l2 = Label(LHS,text=f"Version: {my_system.version}",bg="#f4f5f5",font=("Acumin Variable Concept",9,'bold'),justify="center")
l2.place(x=20,y=280)

l3 = Label(LHS,text=f"System: {my_system.system}",bg="#f4f5f5",font=("Acumin Variable Concept",13,'bold'),justify="center")
l3.place(x=20,y=300)

l4 = Label(LHS,text=f"Machine: {my_system.machine}",bg="#f4f5f5",font=("Acumin Variable Concept",13,'bold'),justify="center")
l4.place(x=20,y=329)

l5 = Label(LHS,text=f"Total Ram installed: {round(psutil.virtual_memory().total/1000000000,2)} GB",bg="#f4f5f5",font=("Acumin Variable Concept",13,'bold'),justify="center")
l5.place(x=10,y=361)

l6 = Label(LHS,text=f"Processor:{my_system.processor}",bg="#f4f5f5",font=("Acumin Variable Concept",7,'bold'),justify="center")
l6.place(x=3,y=400)



# ------------------------------------------------
RHS = Frame(Body,width=500,height=230,bg='#f4f5f5',highlightbackground='#adacb1',highlightthickness=1)
RHS.place(x=425,y=10)

system = Label(RHS,text='System',font=("Acumin Variable Concept",20,'bold'),bg='#f4f5f5')
system.place(x=10,y=10)


# ------------------------------------------ BATTERY
def convertTime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return "%d:%02d:%02d" % (hours,minutes,seconds)



def none():
    global battery_png
    global battery_lable
    battery = psutil.sensors_battery()
    percent = battery.percent
    time = convertTime(battery.secsleft)
    # print(time)
    # print(percent)
    # ya jo hay battery kay time percent ko kaha nazar ana hay aus kay liay likha hay
    lb1.config(text=f"{percent}%")
    lb1_plugin.config(text=f"Plugin:{battery.power_plugged}")
    lb1_time.config(text=f"{time} renaming")


    battery_lable = Label(RHS,background='#f4f5f5')
    battery_lable.place(x=15,y=50)

    lb1.after(1000,none)

    if  battery.power_plugged==True:
        battery_png = PhotoImage(file='battery half.png')
        battery_lable.config(image=battery_png)

    else:
        battery_png=PhotoImage(file="battery full.png")
        battery_lable.config(image=battery_png)

lb1 = Label(RHS,font=("Acumin Variable Concept",40,'bold'),bg="#f4f5f5")
lb1.place(x=200,y=40)


lb1_plugin = Label(RHS,font=("Acumin Variable Concept",10,'bold'),bg="#f4f5f5")
lb1_plugin.place(x=20,y=118)


lb1_time = Label(RHS,font=("Acumin Variable Concept",15,'bold'),bg="#f4f5f5")
lb1_time.place(x=200,y=110)

none()

###########################################-----------------SPEAKERS
lb1_speaker = Label(RHS,text='Speaker:',font=('arial',10,'bold'),bg='#f4f5f5')
lb1_speaker.place(x=10,y=150)
volume_value = tk.DoubleVar()

# def volume_changed():
#     print()

style = ttk.Style()
style.configure("TScale", background='#f4f5f5')

def get_current_volume_value():
    return "{: .2f}".format(volume_value.get())

def volume_changed(event):
    device = AudioUtilities.GetSpeakers()
    interface = device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume = cast(interface,POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevel(-float(get_current_volume_value()),None)
    
volume=ttk.Scale(RHS,from_=60,to=0,orient='horizontal',command=volume_changed,variable=volume_value)
volume.place(x=110,y=150)
volume.set(20)



# -------------------------------------------------BRIGHTNESS----------

lb1_brightness = Label(RHS,text='Brightness: ',font=('arial',10,'bold'),bg="#f4f5f5")
lb1_brightness.place(x=10,y=190)

current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def brightness_changed(event):
    pct.set_brightness(get_current_value())

brightness = ttk.Scale(RHS,from_=0,to=100,orient='horizontal',command=brightness_changed,variable=current_value)
brightness.place(x=115,y=190)




# -------------------------------------------------- Apps Commands
def weather():
    app1=Toplevel()
    app1.geometry('850x500+300+170')
    app1.title('Weather')
    app1.configure(bg='#f4f5f5')
    app1.resizable(False,False)

    #icon
    image_icon=PhotoImage(file='weather.png')
    app1.iconphoto(False,image_icon)

    def getWether():
        try:
            city=textfield.get()
            geolocator = Nominatim(user_agent='geoapiExercises')
            location = geolocator.geocode(city)
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time = local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text='CURRENT WEATHER')

            #weather
            api = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=d602f7639be042dfa0419d6b65bda1ef'

            # json_data = requests.get(api).json()
            json_data = requests.get(api).json()
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp = int(json_data['main']['temp']-273.15)
            pressure = json_data['main']['pressure']
            humidity=json_data['main']['humidity']
            wind = json_data['wind']['speed']

            t.config(text=(temp, "°"))
            c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))

            w.config(text=wind)
            h.config(text=humidity)
            d.config(text=description)
            p.config(text=pressure)
        except Exception as e:
            messagebox.showerror("Weather App","Invalid Entry")




    #search box
    Search_image = PhotoImage(file='bar.png')
    myimage=Label(app1,image=Search_image,bg='#f4f5f5')
    myimage.place(x=25,y=28)

    textfield = tk.Entry(app1,justify='center',width=17,font=('poppins',20,'bold'),bg='#303030',border=0,fg='white')
    textfield.place(x=50,y=43)
    textfield.focus()

    Search_icon=PhotoImage(file='search.png')
    myimage_icon = Button(app1,image=Search_icon,borderwidth=0,cursor='hand2',bg='#505050',command=getWether)
    myimage_icon.place(x=410,y=40)

    #LOGO
    logo_image = PhotoImage(file='logoweather.png')
    logo = Label(app1,image=logo_image,bg='#f4f5f5')
    logo.place(x=150,y=130)

    #BOTTOM BOX
    Frame_image = PhotoImage(file='box.png')
    frame_myimage = Label(app1,image=Frame_image,bg="#f4f5f5",width=800,height=100)
    frame_myimage.pack(padx=5,pady=5,side=BOTTOM) #ya bottom may set karnay ka easy way hay


    #time
    name = Label(app1,font=('arial',15,'bold'),bg='#f4f5f5')
    name.place(x=30,y=100)
    clock = Label(app1,font=('Helvetica',20),bg='#f4f5f5')
    clock.place(x=30,y=130)

    #label
    lable1 = Label(app1,text='WIND',font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
    lable1.place(x=90,y=400)



    lable2 = Label(app1,text='HUMIDITY',font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
    lable2.place(x=220,y=400)


    lable3 = Label(app1,text='DESCRIPTION',font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
    lable3.place(x=380,y=400)


    lable4 = Label(app1,text='PRESSURE',font=("Helvetica",15,'bold'),fg='white',bg='#1ab5ef')
    lable4.place(x=600,y=400)


    t = Label(app1,font=('arial',70,'bold'),fg='#ee666d',bg='#f4f5f5')
    t.place(x=400,y=150)

    c = Label(app1, font=('arial', 15, 'bold'), bg='#f4f5f5')
    c.place(x=400, y=270)

    w = Label(app1,text='...',font=('arial',20,'bold'),bg='#1ab5ef')
    w.place(x=120,y=450)

    h = Label(app1, text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
    h.place(x=240, y=450)
    d = Label(app1, text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
    d.place(x=420, y=450)
    p = Label(app1, text='...', font=('arial', 20, 'bold'), bg='#1ab5ef')
    p.place(x=640, y=450)


    app1.mainloop()


def clock():
    app2 = Toplevel()
    app2.geometry("850x110+300+10")
    app2.title('Clock')
    app2.configure(bg='#292e2e')
    app2.resizable(False, False)



    #ICON
    image_icon = PhotoImage(file='Clockicon.png')
    app2.iconphoto(False,image_icon)

    def clock():
        text=strftime('%H:%M:%S %p')
        lb1.config(text=text)
        lb1.after(1000,clock)

    lb1 = Label(app2,font=('digital-7',50,'bold'),width=20,bg='#f4f5f5',fg='#292e2e')
    lb1.pack(anchor='center',pady=20)
    clock()



    app2.mainloop()


def calander():
    app3 = Toplevel()
    app3.geometry('300x300+-10+10')
    app3.title("Calender")
    app3.configure(bg='#292e2e')
    app3.resizable(False,False)


    #ICON
    image_icon = PhotoImage(file='calender1.png')
    app3.iconphoto(False,image_icon)
    mycal = Calendar(app3,setmode='day',date_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)

    app3.mainloop()


# ================================= Model
button_mode = True

def model():
    global  button_mode
    if button_mode:
        LHS.config(bg='#292e2e')
        myimage.config(bg='#292e2e')

        l1.config(bg='#292e2e',fg='#d6d6d6')
        l2.config(bg='#292e2e', fg='#d6d6d6')
        l3.config(bg='#292e2e', fg='#d6d6d6')
        l4.config(bg='#292e2e', fg='#d6d6d6')
        l5.config(bg='#292e2e', fg='#d6d6d6')
        l6.config(bg='#292e2e', fg='#d6d6d6')

        RHB.config(bg='#292e2e')
        app1.config(bg='#292e2e')
        app2.config(bg='#292e2e')
        app3.config(bg='#292e2e')
        app4.config(bg='#292e2e')
        app5.config(bg='#292e2e')
        app6.config(bg='#292e2e')
        app7.config(bg='#292e2e')
        app8.config(bg='#292e2e')
        app9.config(bg='#292e2e')
        app10.config(bg='#292e2e')

        apps.config(bg='#292e2e',fg='#f4f5f5')


        button_mode = False

    else:
        LHS.config(bg='#f4f5f5')
        myimage.config(bg='#f4f5f5')

        l1.config(bg='#f4f5f5',fg='#292e2e')
        l2.config(bg='#f4f5f5',fg='#292e2e')
        l3.config(bg='#f4f5f5',fg='#292e2e')
        l4.config(bg='#f4f5f5',fg='#292e2e')
        l5.config(bg='#f4f5f5',fg='#292e2e')
        l6.config(bg='#f4f5f5',fg='#292e2e')


        RHB.config(bg='#f4f5f5')
        app1.config(bg='#f4f5f5')
        app2.config(bg='#f4f5f5')
        app3.config(bg='#f4f5f5')
        app4.config(bg='#f4f5f5')
        app5.config(bg='#f4f5f5')
        app6.config(bg='#f4f5f5')
        app7.config(bg='#f4f5f5')
        app8.config(bg='#f4f5f5')
        app9.config(bg='#f4f5f5')
        app10.config(bg='#f4f5f5')
        apps.config(bg='#f4f5f5',fg='#292e2e')

        button_mode=True


def game():
    app5=Toplevel()
    app5.geometry('300x600+1170+170')
    app5.title('Ludo')
    app5.configure(bg='#dee2e5')
    app5.resizable(False,False)




    #ICON
    image_icon = PhotoImage(file='ludo icon.png')
    app5.iconphoto(False,image_icon)

    ludo_image = PhotoImage(file='ludo back.png')
    Label(app5,image=ludo_image).pack()

    label = Label(app5,text='',font=('times',120))


    def roll():
        dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
        label.configure(text=f'{random.choice(dice)}{random.choice(dice)}',fg='#29232e')
        label.pack()

    btn_image = PhotoImage(file='lets-roll.png')
    btn = Button(app5,image=btn_image,bg='#dee2e5',command=roll)
    btn.pack(padx=10,pady=10)

    app5.mainloop()


# -------------------------------------------- Camara/screenshot app6
def screenshot():



    root.iconify()
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)

# ------------------------------------------- File manager App 7

def file():
    subprocess.Popen(r'explorer / select, "C:\path\of\folder\file"')


# ----------------------------------------------crome App8

def crome():
    wb.register('chrome',None)
    wb.open('https://www.google.com/')


# ----------------------------------------Close app App 9

def close_apps():
    wb.register('chrome', None)
    wb.open('https://www.codewithharry.com/')

 # https://www.youtube.com/channel/UCJ2VzaGLrJk1JXGXE21hsQQ   (some times use this link on the place of code with harry)


def close_window():
    root.destroy()

# ------------------------------------------------
RHB = Frame(Body,width=500,height=300,bg='#f4f5f5',highlightbackground='#adacb1',highlightthickness=1)
RHB.place(x=425,y=255)

# --------------------------------------------- APPS
apps = Label(RHB,text='Apps',font=('Acumin Variable Concept',15,'bold'),bg='#f4f5f5')
apps.place(x=10,y=10)

app1_image = PhotoImage(file='weather.png')
app1 = Button(RHB,image=app1_image,bd=0,width=100,height=100,command=weather)
app1.place(x=10,y=50)

app2_image = PhotoImage(file='Clockicon.png')
app2 = Button(RHB,image=app2_image,bd=0,width=100,height=100,command=clock)
app2.place(x=102,y=50)

app3_image = PhotoImage(file='calender1.png')
app3 = Button(RHB,image=app3_image,bd=0,width=100,height=100,command=calander)
app3.place(x=195,y=50)

app4_image = PhotoImage(file='darkmode and white mode.png')
app4 = Button(RHB,image=app4_image,bd=0,width=100,height=100,command=model)
app4.place(x=280,y=50)

app5_image = PhotoImage(file='ludo icon.png')
app5 = Button(RHB,image=app5_image,bd=0,width=100,height=100,command=game)
app5.place(x=375,y=50)

app6_image = PhotoImage(file='camara icon.png')
app6 = Button(RHB,image=app6_image,bd=0,width=100,height=100,command=screenshot)
app6.place(x=10,y=165)

app7_image = PhotoImage(file='file manager.png')
app7 = Button(RHB,image=app7_image,bd=0,width=100,height=100,command=file)
app7.place(x=102,y=165)

app8_image = PhotoImage(file='Google.png')
app8 = Button(RHB,image=app8_image,bd=0,width=100,height=100,command=crome)
app8.place(x=191,y=165)

app9_image = PhotoImage(file='ss icon.png')
app9 = Button(RHB,image=app9_image,bd=0,width=100,height=100,command=close_apps)
app9.place(x=280,y=165)

app10_image = PhotoImage(file='close2.png')
app10 = Button(RHB,image=app10_image,bd=0,width=100,height=100,command=close_window)
app10.place(x=380,y=170)

root.mainloop()

