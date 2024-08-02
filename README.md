On Windows:
```
python3 -m venv .venv
.venv/Scripts/activate
python3 -m pip install -r requirements.txt
```

On macOS:
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Then use 
```
python3 main.py
```
to execute. 

20240723 1531 PT

This version of frontend demo, when program start, it will first send the session info into the backend. Then:
In the loop, it will take screenshots, send them into frontend and then get action string.

This version is stored as 1.0.0, which corresponds to the BackEnd 1.0.0.


20240730 1442 PT
This version of code support the program.py and scripts for execution from the backend. This version is stored as 1.0.1.


20240801 0157 PT
I rewrite the frontend code according to the new backend API.
This version of code is stored as 1.0.2.

20240801 1811 PT
Add Scripts link download on backend, the frontend can tell the backend which JSON action script to use. 
This version of code is stored as 1.0.3, next I plan to exchange the server and client, use windows as server and macbook as client to write a script on mac. 



20240801 1939 PT
When shift to manipulate on mac, I found that the mouse click coordinate is not correct. 
Just like I verfied before, the coordinate on mac need to divide by 2 for pyautogui to execute correctly. Unknown reasons. 


20240802 1436 PT
Complete the macbook as client, windows as server version. For the macbook, things becomes a little bit different. I added some action patterns as these special gestures used on macbook to execute some actions like enter or exit full screen. The script is the same to download 3 github repo zips. 

This version of code is stored as 1.0.4. 

