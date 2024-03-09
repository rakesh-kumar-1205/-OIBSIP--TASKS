from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title(f"Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
Font = ('Arial',21,'bold')

import time

def get_weather():
    try:
        city = textfield.get()
        geolocation = Nominatim(user_agent="geoapiExercises")
        location = geolocation.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)   
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        # Weather
        api_id=""
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}"
        response = requests.get(api)

        if response.status_code == 200:
            json_data = response.json() 
            condition = json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temperature = int(json_data['main']['temp'] - 273.15)
            pressure = json_data['main']['pressure']
            humidity = json_data['main']['humidity']
            wind = json_data['wind']['speed']

            temp.config(text=(temperature, "°C"))
            c.config(text=(condition))

            win_d.config(text=wind)
            humid_t.config(text=humidity)
            desc.config(text=description)
            press_r.config(text=pressure)
        else:
            print(f"Failed to fetch weather data. Status code: {response.status_code}")

    except Exception as e:
        print(f"The error is {e}")


#search box
search_box = PhotoImage(file=r'Weather App/Search.png')
mylebel = Label(image=search_box)
mylebel.place(x=20,y=20)


textfield = tk.Entry(root, justify='center',width=23,font=Font,bg='#404040',border=0,fg='white')
textfield.place(x=42,y=42)
textfield.focus()

#search logo
mySearchicon = PhotoImage(file='Weather App/Search_icon.png')
myimage_icon = Button(image=mySearchicon,borderwidth=0,cursor= 'hand2',bg="#404040",command=get_weather)
myimage_icon.place(x=400,y=33)

#logo
mylogo = PhotoImage(file='Weather App/Logo.png')
logo = Label(image=mylogo)
logo.place(x=150,y=100)


#buttom box
myFrameimage = PhotoImage(file="Weather App/Box.png") 
frame_myimage =Label(image=myFrameimage)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM) 


#time
name = Label(root,font=('Helvetica',14,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("Helvetica",18))
clock.place(x=30,y=130)


#labels
wind_lavel = Label(root, text="WIND",font=('Helvetica',15,'bold'),fg="white",bg = "#1ab5ef")
wind_lavel.place(x=120,y=400)

lavel1 = Label(root, text="HUMIDITY",font=('Helvetica',15,'bold'),fg="white",bg = "#1ab5ef")
lavel1.place(x=225,y=400)

lavel1 = Label(root, text="DESCRIPTION",font=('Helvetica',15,'bold'),fg="white",bg = "#1ab5ef")
lavel1.place(x=430,y=400)

lavel1 = Label(root, text="PRESSURE",font=('Helvetica',15,'bold'),fg="white",bg = "#1ab5ef")
lavel1.place(x=650,y=400)

temp= Label(font=("Arial Bold", 70), fg="#ee666d" )
temp.place(x=400,y=150)
c=Label(font=("Arial Bold", 15))
c.place(x=400,y=250)

win_d=Label(text="....",font=('arial',20,'bold'),bg='#1ab5ef')
win_d.place(x=120,y=430)

humid_t=Label(text="....",font=('arial',20,'bold'),bg='#1ab5ef')
humid_t.place(x=225,y=430)

desc=Label(text="....",font=('arial',20,'bold'),bg='#1ab5ef')
desc.place(x=430,y=430)

press_r=Label(text="....",font=('arial',20,'bold'),bg='#1ab5ef')
press_r.place(x=650,y=430)

root.mainloop()