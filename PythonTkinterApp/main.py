import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import requests


# window settings
window = ttk.Window(themename="yeti")
window.title("Simple Weather App")
window.geometry('600x350')

window.grid_columnconfigure((0), weight=1)
#background
background_label = ttk.Label(window, background="#ccccff")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


#Title Label
title_label = ttk.Label(master=window, text="Weather App", font="Calibri 24 bold", background="#ccccff")
title_label.grid(row=0, column=0)


# input field
def getWeather():
    city = entry.get()
    entry.delete(0, len(city))
    #apiLocation = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={1}&appid=7b655d9a6492de09c8a174cd263435ba"
    #json_data = requests.get(apiLocation).json()
 
    #lat = json_data[0]["lat"]
    #lon = json_data[0]["lon"]

    #apiWeather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=7b655d9a6492de09c8a174cd263435ba"
    apiWeather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7b655d9a6492de09c8a174cd263435ba"
    json_data = requests.get(apiWeather).json()
    try:
        #temp = round((json_data["main"]["temp"] - 273) * 10) / 10
        temp = json_data["main"]["temp"] - 273
        temp_val.set("%.1f" % temp + "°C")

        hum = json_data["main"]["humidity"]
        hum_val.set(str(hum) + "%")
    except:
        print(json_data)
        print("City does not exist!")
    return


input_frame = ttk.Frame(window)
entry = ttk.Entry(input_frame)
button = ttk.Button(input_frame, text="Enter", command=getWeather)
entry.pack(side="left", padx = 10)
button.pack(side="left")
input_frame.grid(row=1, column=0, pady=10)


# image
canvas = ttk.Canvas(window, bg="#ccccff", width=100, height=100)
canvas.grid(row=2, column=0)

weather_img = ImageTk.PhotoImage(Image.open("img/weather_icon.png"))
canvas.create_image(50, 50, image=weather_img)

# stats frame
stats_frame = ttk.Frame(window)
stats_frame.grid(row=3, column=0)

# temperature
temp_val = tk.IntVar()
temp_label = ttk.Label(stats_frame, text="--", font="Calibri 16 bold", background = "#ccccff", textvariable=temp_val)
temp_label.grid(row=0, column=0, padx=10, pady=10)

#humidity
hum_val = tk.IntVar()
hum_label = ttk.Label(stats_frame, text="--", font="Calibri 16 bold", background = "#ccccff", textvariable=hum_val)
hum_label.grid(row=0, column=1, padx=10, pady=10)

# run
window.mainloop()