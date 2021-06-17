#-*- coding : utf-8 -*-

import requests, json, tkinter, webbrowser

data = {"Authorization":"CWB-2F144930-D1C7-43BE-9450-97B52631BC22",
        "limit":1,
        "offset":0,
        "format":"JSON",
        "stationName":"NAN",
        "areaName":"NAN",
        }



getre = requests.get("https://opendata.cwb.gov.tw/api" + "/v1/rest/datastore/E-A0015-001", params = data)

quake = getre.json()["records"]["earthquake"]


window = tkinter.Tk()
window.title("地震")
window.geometry("400x600")
window.resizable(0,0)

frame = tkinter.Frame(window)
frame.pack(fill = "both", expand = True)

canvas = tkinter.Canvas(frame)
canvas.pack(fill = "both", expand = True)

def _on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

scrollbar = tkinter.Scrollbar(canvas, orient = tkinter.VERTICAL, command = canvas.yview)
scrollbar.pack(side = "right", fill= "y")

canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
canvas.bind("<MouseWheel>", _on_mouse_wheel)

frame2 = tkinter.Frame(canvas)

canvas.create_window((0,0), window = frame2)

def show_image(url) :
      webbrowser.open(url)

for i in quake :
      L = tkinter.Button(frame2, text = str(i["earthquakeNo"]) + "\n" +\
                         str(i["earthquakeInfo"]["originTime"]) + "\n" +\
                         "芮氏規模" + str(i["earthquakeInfo"]["magnitude"]["magnitudeValue"])\
                         , font = ("",25), command = \
                         lambda : show_image(i["reportImageURI"]))
      L.pack()

      

window.mainloop()


#print(quake)

