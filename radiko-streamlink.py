#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import subprocess
import time

root = Tk()
root.title('Radiko Player')
root.configure(background='#333333') # Background color
style = ttk.Style()
style.theme_use('default') #('clam', 'alt', 'default', 'classic')
style.configure('TButton', background='#D9D9D9') # Button color

# Frame
frame0 = ttk.Frame(root, padding=0)
frame0.grid()
frame1 = ttk.Frame(root,padding=5)
frame1.grid()
# label
label1 = ttk.Label(
    frame0,
    text=('Radiko Streamlink Player'),
    font=('Helvetica', 10),
    background='#000000',
    foreground='#ffffff')
label1.grid(row=0,column=0)

# --- default settings ---
# icon dir
dir = "/home/pi/.icons/64x64/"
# player application
player = "mpv"
#player = "'ffplay -nodisp'"


# Button bayfm
def radio01():
    global id; id = "BAYFM78"; play()
icon1 = PhotoImage(file=dir + 'bayfm.png')
button1 = ttk.Button(frame1, image=icon1, command=radio01)
button1.grid(row=1,column=1)

# Button tokyofm
def radio02():
    global id; id = "FMT"; play()
icon2 = PhotoImage(file=dir + 'tokyofm.png')
button2 = ttk.Button(frame1, image=icon2, command=radio02)
button2.grid(row=1,column=3)

# Button jwave
def radio03():
    global id; id = "FMJ"; play()
icon3 = PhotoImage(file=dir + 'jwave.png')
button3 = ttk.Button(frame1, image=icon3, command=radio03)
button3.grid(row=1,column=2)

# Button interfm
def radio04():
    global id; id = "INT"; play()
icon4 = PhotoImage(file=dir + 'interfm.png')
button4 = ttk.Button(frame1, image=icon4, command=radio04)
button4.grid(row=1,column=6)

# Button nack5
def radio05():
    global id; id = "NACK5"; play()
icon5 = PhotoImage(file=dir + 'nack5.png')
button5 = ttk.Button(frame1, image=icon5, command=radio05)
button5.grid(row=1,column=4)

# Button ranimusic
def radio06():
    global id; id = "RN2"; play()
icon6 = PhotoImage(file=dir + 'ranimusic2.png')
button6 = ttk.Button(frame1, image=icon6, command=radio06)
button6.grid(row=3,column=2)

# Button fmyokohama
def radio07():
    global id; id = "YFM"; play()
icon7 = PhotoImage(file=dir + 'fmyokohama.png')
button7 = ttk.Button(frame1, image=icon7, command=radio07)
button7.grid(row=1,column=5)

# Button TBS
def radio08():
    global id; id = "TBS"; play()
icon8 = PhotoImage(file=dir + 'TBS.png')
button8 = ttk.Button(frame1, image=icon8, command=radio08)
button8.grid(row=2,column=3)

# Button QRR
def radio09():
    global id; id = "QRR"; play()
icon9 = PhotoImage(file=dir + 'QRR.png')
button9 = ttk.Button(frame1, image=icon9, command=radio09)
button9.grid(row=2,column=4)

# Button LFR
def radio10():
    global id; id = "LFR"; play()
icon10 = PhotoImage(file=dir + 'LFR.png')
button10 = ttk.Button(frame1, image=icon10, command=radio10)
button10.grid(row=2,column=5)

# Button JORF
def radio11():
    global id; id = "JORF"; play()
icon11 = PhotoImage(file=dir + 'JORF.png')
button11 = ttk.Button(frame1, image=icon11, command=radio11)
button11.grid(row=2,column=6)

# Button NHK-FM
def radio12():
    global id; id = "JOAK-FM"; play()
icon12 = PhotoImage(file=dir + 'NHK-FM.png')
button12 = ttk.Button(frame1, image=icon12, command=radio12)
button12.grid(row=2,column=1)

# Button NHK-R1
def radio13():
    global id; id = "JOAK"; play()
icon13 = PhotoImage(file=dir + 'NHK-R1.png')
button13 = ttk.Button(frame1, image=icon13, command=radio13)
button13.grid(row=2,column=2)

# Button RN1
def radio14():
    global id; id = "RN1"; play()
icon14 = PhotoImage(file=dir + 'RN1.png')
button14 = ttk.Button(frame1, image=icon14, command=radio14)
button14.grid(row=3,column=1)

# Button 放送大学
def radio19():
    global id; id = "HOUSOU-DAIGAKU"; play()
icon19 = PhotoImage(file=dir + '放送大学.png')
button19 = ttk.Button(frame1, image=icon19, command=radio19)
button19.grid(row=3,column=3)

# Button vol-kill
def radio15():
    subprocess.run("killall -q streamlink", shell=True)
icon15 = PhotoImage(file=dir + 'vol-kill.png')
button15 = ttk.Button(
    frame1,
    image=icon15,
    command=radio15)
button15.grid(row=3,column=5)

# Button exit
def exit():
    subprocess.run("killall -q streamlink", shell=True)
    root.quit()
icon90 = PhotoImage(file=dir + 'exit.png')
button90 = ttk.Button(frame1, image=icon90, command=exit)
button90.grid(row=3,column=6)

# Button onair
def radio99():
    command = ("ps ax | grep http://radiko.jp | grep -v grep | awk '{print $(NF-1)}' | awk 'NR==1'")
    proc = (subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).communicate()[0]).decode('utf-8')
    proc = proc.strip()
    #print(proc)
    url = 'http://radiko.jp/#!/live/'
    if proc == url + 'BAYFM78':
        proc = 'ON AIR --- BAYFM78'
    elif proc == url + 'FMT':
        proc = 'ON AIR --- TOKYO FM'
    elif proc == url + 'FMJ':
        proc = 'ON AIR --- J-WAVE'
    elif proc == url + 'INT':
        proc = 'ON AIR --- Inter FM 897'
    elif proc == url + 'NACK5':
        proc = 'ON AIR --- NACK5'
    elif proc == url + 'RN2':
        proc = 'ON AIR --- Rani Music'
    elif proc == url + 'RN1':
        proc = 'ON AIR --- Radio Nikkei'
    elif proc == url + 'YFM':
        proc = 'ON AIR --- FM yokohama 84.7'
    elif proc == url + 'TBS':
        proc = 'ON AIR --- TBSラジオ'
    elif proc == url + 'QRR':
        proc = 'ON AIR --- 文化放送'
    elif proc == url + 'LFR':
        proc = 'ON AIR --- ニッポン放送'
    elif proc == url + 'JORF':
        proc = 'ON AIR --- ラジオ日本'
    elif proc == url + 'JOAK-FM':
        proc = 'ON AIR --- NHK FM 東京'
    elif proc == url + 'JOAK':
        proc = 'ON AIR --- NHK R1 東京'
    elif proc == url + 'HOUSOU-DAIGAKU':
        proc = 'ON AIR --- 放送大学'
    else:
        proc = 'No Station'
    messagebox.showinfo('ON AIR', proc)
icon99 = PhotoImage(file=dir + 'onair.png')
button99 = ttk.Button(
    frame1,
    image=icon99,
    command=radio99)
button99.grid(row=3,column=4)

def play():
    subprocess.run("killall -q streamlink", shell=True)
    time.sleep(1)
    subprocess.run("~/.local/bin/streamlink -p " + player + " http://radiko.jp/#!/live/" + id + " best &", shell=True)

root.mainloop()
