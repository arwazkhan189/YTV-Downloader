'''
----------------------------About the App-------------------------------------------------------------------
YTV-Downloader is a Desktop application to download YouTube videos.
Developed using python modules - tkinter and pytube.
tkinter - python built in module   (Docs:- https://docs.python.org/3/library/tkinter.html)
pytube - external module (pip install pytube , Docs:- https://pytube.io/en/latest/index.html)

Other tool - converting .py to .exe using pyinstaller (Docs:- https://pyinstaller.readthedocs.io/en/stable/)
             canva - used to make icon , background image.

----------------------------Source code available-----------------------------
► App Website - https://arwazkhan189.github.io/YTV-Downloader/
► Github repository link - https://github.com/arwazkhan189/YTV-Downloader
------------------Follow Me On Social Media-----------------------------------
► Website  - https://arwazkhan.me/
► Facebook - https://www.facebook.com/arwazkhan189
► Instagram - https://instagram.com/iamarwaz
► Twitter - https://twitter.com/arwazkhan189
► LinkedIn - https://www.linkedin.com/in/arwaz-khan-bb52a1134/
► Github - https://github.com/arwazkhan189
​
'''
#------------ importing libraries-----------------------------------------------------------------------------------------
from tkinter import  *
from pytube import YouTube

#---------------root object-----------------------------------------------------------------------------------------------
root=Tk()

#---------window-size------------------------------------------------------------------------------------------------------
root.geometry("400x400")
root.minsize(400,400)
root.maxsize(400,400)

#---------title and icon----------------------------------------------------------------------------------------------------
root.title("YTV Downloader")
appicon = PhotoImage(file = "Assets\icon.png")
root.iconphoto(False, appicon)

#-----------status function-------------------------------------------------------------------------------------------------
def STATUS(S_VAL):
    status_var=StringVar()
    status_var.set(S_VAL)
    status_bar=Label(root,textvariable=status_var)
    status_bar.place(x=0,y=400,anchor=SW,width=400,height=20,bordermode=OUTSIDE)

#-----------------download function-----------------------------------------------------------------------------------------
def Download_video():
    V_link=video_link.get()
    V_res=quality_value.get()
    if (V_link=='' or V_res==''):
        STATUS("Enter the link or select resolution")
    else:
        try:
            resol = [ '1080p', '720p', '360p']
            yt=YouTube(V_link)
            yt.streams.filter(res=resol[V_res]).first().download("YTV-Downloader-Videos/")
            STATUS("Downloaded Successfully...")
        except :
            STATUS("The video is unavailable or the link is incorrect.")
        
    
#------------background-image------------------------------------------------------------------------------------------------
bg=PhotoImage(file="Assets\YTVD.png")
bg_canvas=Canvas(root,width=400,height=400)
bg_canvas.create_image(0,0,image=bg,anchor="nw")
bg_canvas.pack(expand=True)

#-------------input-from-user-------------------------------------------------------------------------------------------------
video_link_label=Label(root,text="Video Link : ",font=('comicsansms',13,'bold'))
video_link_label.place(x=20,y=20,anchor=NW)

#------------video link---------------------------------------------------------------------------------------------------------
link_value=StringVar()
video_link=Entry(root,textvariable=link_value,font=('comicsansms',13,'normal'))
video_link.place(x=150,y=20,anchor=NW)

#-----------video quality-------------------------------------------------------------------------------------------------------
quality_label=Label(root,text="Select Video Resolution : ",font=('comicsansms',13,'bold'))
quality_label.place(x=20,y=50,anchor=NW)
quality_value=IntVar()
quality_list = [ '1080p', '720p', '360p']
for i in range(3):
    radio_button = Radiobutton(root, text=quality_list[i],padx=5,variable=quality_value, value= i).place(x=40+100*i,y=80,anchor=NW)

#----------download button-----------------------------------------------------------------------------------------------------------
download_button = Button(root,text="Download", command=Download_video)
btn_img= PhotoImage(file="Assets\download_btn.png")
download_button.config(image=btn_img)
download_button.place(x=120,y=300,anchor=NW)

#----------------status bar-----------------------------------------------------------------------------------------------------
status_var=StringVar()
status_var.set("Click to Download button to download your Video")
status_bar=Label(root,textvariable=status_var)
status_bar.place(x=0,y=400,anchor=SW,width=400,height=20,bordermode=OUTSIDE)

#----------- Main program-------------------------------------------------------------------------------------------------------
if (__name__ == "__main__"):
    root.mainloop()