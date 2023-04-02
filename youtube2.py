#بسم الله الرحمن الرحيم
import tkinter as tk
from tkinter import *
from pytube import YouTube, Playlist
from tkinter import messagebox, filedialog

def Widgets():
# first label to say my name
	head_label = Label(MS, 
					text=" BY. MOHAMED ELSAYED ",
					padx=15,
					pady=15,
					bg="#DFD3C3",
                    font="Arial 25 bold",
					fg="#002B5B")
	head_label.grid(row=0,
					column=0,
					pady=10,
					padx=15,
					columnspan=3)
# youtube link 
	link_label = Label(MS,
					text="YouTube link : >>>> ",
					font="Arial 14 bold",
					bg="#DFD3C3",
					pady=5,
                    fg="#002B5B",
					padx=5)

	link_label.grid(row=2,
					column=0,
					pady=5,
					padx=5)
# entry connect with youtube link
	MS.linkText = Entry(MS,
						width=40,
						textvariable=video_Link,
						font="Arial 14")

	MS.linkText.grid(row=2,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)
# youtube playlist 
	slink_label = Label(MS,
					text="YouTube PlayList : >>>> ",
					font="Arial 14 bold",
					bg="#DFD3C3",
					pady=5,
                    fg="#002B5B",
					padx=5)

	slink_label.grid(row=1,
					column=0,
					pady=5,
					padx=5)
#entry connect with playlist
	MS.link_Text = Entry(MS,
						width=40,
						textvariable=playlist_Link,
						font="Arial 14")
	MS.link_Text.grid(row=1,
					column=1,
					pady=5,
					padx=5,
					columnspan=2)
# download loc choose file to download
	Downloadlocation_label = Label(MS,
							text="Download location : >>>>",
							font="Arial 14 bold",
							bg="#DFD3C3",
                            fg="#002B5B",
							pady=5,
							padx=9)
	Downloadlocation_label.grid(row=3,
						column=0,
						pady=5,
						padx=5)

# entry connect with download loc 
	MS.Downloadlocation_Text = Entry(MS,
								width=27,
								textvariable=download_Path,
								font="Arial 14")
	MS.Downloadlocation_Text.grid(row=3,
							column=1,
							pady=5,
							padx=5)

# choose file to download by button Browse and button download video

	browse_B = Button(MS,
					text="Browse",
                    font ="Arial 10 bold",
					command=Browse,
					width=10,
					bg="#002B5B",
                    fg="#DFD3C3",
					relief=GROOVE)
	browse_B.grid(row=3,
				column=2,
				pady=1,
				padx=1)
# download video
	Download_B = Button(MS,
						text="Download Video",
						command=Download,
						width=12,
						bg="#002B5B",
                        fg="#DFD3C3",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Arial, 14 bold")
	Download_B.grid(row=4,
					column=1,
					pady=10,
					padx=10)

#button to download audio		

	Download_C = Button(MS,
						text="Download Audio",
						command=Downloader,
						width=12,
						bg="#002B5B",
                        fg="#DFD3C3",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Arial, 14 bold")
	Download_C.grid(row=4,
					column=0,
					pady=20,
					padx=20)

# button to download playlist

	Download_D = Button(MS,
						text="Download PlayList",
						command=DownloadPlaylist,
						width=13,
						bg="#002B5B",
                        fg="#DFD3C3",
						pady=10,
						padx=15,
						relief=GROOVE,
						font="Arial, 14 bold")
	Download_D.grid(row=4,
					column=2,
					pady=10,
					padx=10)

#list to copy and paste with mouse
def create_menu(widget):
    menu = Menu(widget, tearoff=False)
    menu.add_command(label="Copy", command=lambda: widget.event_generate("<Control-c>"))
    menu.add_command(label="Paste", command=lambda: widget.event_generate("<Control-v>"))
    menu.add_command(label="Delete", command=lambda: widget.delete(0, 'end'))
    widget.bind("<Button-3>", lambda e: menu.post(e.x_root, e.y_root))

# to choose file

def Browse():

	download_Directory = filedialog.askdirectory(
		initialdir="YOUR DIRECTORY PATH", title="Save Video")

	download_Path.set(download_Directory)

# to download the video

def Download():

	Youtube_link = video_Link.get()

	# saving file's
	download_Folder = download_Path.get()

	# Creating object of YouTube()
	getVideo = YouTube(Youtube_link)

	# to save high q
	videoStream = getVideo.streams.get_highest_resolution()

	videoStream.download(download_Folder)
	# Displaying the message
	messagebox.showinfo("Done",
						"Downloaded and saved in \n"
						+ download_Folder)


# to download the audio

def Downloader():

	
	Youtube_link = video_Link.get()

	download_Folder = download_Path.get()

	getVideo = YouTube(Youtube_link)

	videoStream = getVideo.streams.get_by_itag(251)

	videoStream.download(download_Folder)

	messagebox.showinfo("Done",
						"Downloaded and saved in \n"
						+ download_Folder)

# to download playlist

def DownloadPlaylist():
    Youtube_playlist_link = playlist_Link.get()

    # Saving file's
    download_Folder = download_Path.get()

    # Creating object of Playlist()
    pl = Playlist(Youtube_playlist_link)

    # Downloading the video
    for video in pl.videos:
        video.streams.get_highest_resolution().download(download_Folder)

    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY", "DOWNLOADED AND SAVED IN\n" + download_Folder)


# Creating object of tk class

MS = tk.Tk()


MS.geometry("900x400")
MS.resizable(False, False)
MS.title("MOHAMED ELSAYED")
MS.config(background="#DFD3C3")
MS.attributes('-alpha', 0.9)



video_Link = StringVar()
download_Path = StringVar()
playlist_Link = StringVar()

# Calling the Widgets() function
Widgets()
create_menu(MS.linkText)
create_menu(MS.link_Text)


MS.mainloop()

