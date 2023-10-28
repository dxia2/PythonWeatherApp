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

#style
style = ttk.Style()
style.configure('TFrame', background='#ccccff')
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

    apiWeather = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7b655d9a6492de09c8a174cd263435ba"
    json_data = requests.get(apiWeather).json()


    try:
        wc = json_data["weather"][0]["main"]
        wc_val.set(wc)

        temp = json_data["main"]["temp"] - 273
        temp_val.set("%.1f" % temp + "°C")

        hum = json_data["main"]["humidity"]
        hum_val.set(str(hum) + "%")

        pressure = json_data["main"]["pressure"]
        pressure_val.set(str(pressure) + " hPa")
    except Exception as error:
        print(error)
    return


input_frame = ttk.Frame(window)
entry = ttk.Entry(input_frame)
button = ttk.Button(input_frame, text="Enter", command=getWeather)
entry.pack(side="left", padx = 10)
button.pack(side="left")
input_frame.grid(row=1, column=0, pady=10)


# image
canvas = ttk.Canvas(window, width=100, height=100)
canvas.grid(row=2, column=0)
canvas.configure(bg="#ccccff")

resized_image = Image.open("img/weather_icon.png").resize((175,125))
weather_img = ImageTk.PhotoImage(resized_image)

canvas.create_image(50, 50, image=weather_img)

# Weather Conditions Label
wc_val = tk.StringVar()
wc_label = ttk.Label(window, text="--", font="Calibri 24 bold", background = "#ccccff", textvariable=wc_val)
wc_label.grid(row=3, column=0)

# stats frame
stats_frame = ttk.Frame(window)
stats_frame.grid(row=4, column=0)
stats_frame_padx = 10
stats_frame_pady = 10
stats_frame_background = "#ccccff"

# temperature
temp_val = tk.IntVar()
temp_label = ttk.Label(stats_frame, text="--", font="Calibri 16 bold", background = stats_frame_background, textvariable=temp_val)
temp_label.grid(row=0, column=0, padx=stats_frame_padx, pady=stats_frame_pady)

# humidity
hum_val = tk.IntVar()
hum_label = ttk.Label(stats_frame, text="--", font="Calibri 16 bold", background = stats_frame_background, textvariable=hum_val)
hum_label.grid(row=0, column=1, padx=stats_frame_padx, pady=stats_frame_pady)

# presure
pressure_val = tk.IntVar()
pressure_label = ttk.Label(stats_frame, text="--", font="Calibri 16 bold", background = stats_frame_background, textvariable=pressure_val)
pressure_label.grid(row=0, column=2, padx=stats_frame_padx, pady=stats_frame_pady)



# run
window.mainloop()