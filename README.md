# openSource Final Project

1. Build process:

python imports:
* json  
* tkinter  
* requests  
* webbrowser  

---

use
` ./python final.py `
to run program

---

2. Introduction:

 當地震發生的時候，要如何快速取得地震資訊，以及快速地提供地震資訊給其他人，在中央氣象局網頁被塞爆的時候，就可以用API來取得最新的地震資訊
 
 
 ---


3. Details of the approach:

```
send requests to CWB open API
get data from CWB open API requests
for each earthquake in data {
  create Button from earthquake detail
}

```
