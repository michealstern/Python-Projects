from tkinter import *
import speedtest

def speedCheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    downLoad = str( round(sp.download()/(10**6),3))+ " Mbps"
    upLoad = str( round(sp.upload()/(10**6),3))+ " Mbps"
    lab_downLoad.config(text=downLoad)
    lab_upLoad.config(text=upLoad)




sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg="aqua")

lab = Label(sp, text="Internet Speed Test", font=("Time New Roman",30,"bold"),bg="aqua", fg="brown")
lab.place(x=60,y=40, height=50,width=380)

lab = Label(sp, text="Download Speed", font=("Time New Roman",25,"bold"))
lab.place(x=60,y=130, height=50,width=380)

lab_downLoad = Label(sp, text="00", font=("Time New Roman",25,"bold"))
lab_downLoad.place(x=60,y=200, height=50,width=380)

lab = Label(sp, text="Upload Speed", font=("Time New Roman",25,"bold"))
lab.place(x=60,y=290, height=50,width=380)

lab_upLoad = Label(sp, text="00", font=("Time New Roman",25,"bold"))
lab_upLoad.place(x=60,y=360, height=50,width=380)



button = Button(sp, text="Check Speed", font=("Time New Roman",15,"bold"), relief=RAISED,bg="light blue",command=speedCheck)
button.place(x=120,y=450, height=40,width=250)

sp.mainloop()