#-*- coding : utf-8 -*-

import requests, json, tkinter, webbrowser


#get 參數
data = {"Authorization":"CWB-2F144930-D1C7-43BE-9450-97B52631BC22",
        "limit":1,
        "offset":0,
        "format":"JSON",
        "stationName":"NAN",
        "areaName":"NAN",
        }

#送request 出去
getre = requests.get("https://opendata.cwb.gov.tw/api" + "/v1/rest/datastore/E-A0015-001", params = data)


#解出想要的資料
quake = getre.json()["records"]["earthquake"]

#GUI 介面
window = tkinter.Tk()
window.title("地震")
window.geometry("400x600")#視窗大小
window.resizable(0,0)#鎖定視窗

frame = tkinter.Frame(window)#建立frame
frame.pack(fill = "both", expand = True)

canvas = tkinter.Canvas(frame)#設定畫布
canvas.pack(fill = "both", expand = True)

def _on_mouse_wheel(event):
    canvas.yview_scroll(-1 * int((event.delta / 120)), "units")#滾輪滑動

scrollbar = tkinter.Scrollbar(canvas, orient = tkinter.VERTICAL, command = canvas.yview)
scrollbar.pack(side = "right", fill= "y")

canvas.configure(yscrollcommand = scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))#綁定scrollregion
canvas.bind("<MouseWheel>", _on_mouse_wheel)#綁定滾輪

frame2 = tkinter.Frame(canvas)

canvas.create_window((0,0), window = frame2)#在canvas 建立新的window

def show_image(url) :
      webbrowser.open(url)#在瀏覽器中打開圖片

for i in quake :#把每一筆資料都建立成Button 放進frame 裡面
      L = tkinter.Button(frame2, text = str(i["earthquakeNo"]) + "\n" +\
                         str(i["earthquakeInfo"]["originTime"]) + "\n" +\
                         "芮氏規模" + str(i["earthquakeInfo"]["magnitude"]["magnitudeValue"])\
                         , font = ("",25), command = \
                         lambda : show_image(i["reportImageURI"]))
      L.bind("<MouseWheel>", _on_mouse_wheel)#在按鈕上也綁定滾輪
      L.pack()

      

window.mainloop()#建立 thread 開始迴圈


#print(quake)

