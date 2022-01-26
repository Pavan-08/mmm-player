# importing libraries
import os
import tkinter
from tkinter import filedialog
from pygame import mixer
from tkinter import *
import tkinter.font as font

def main(mood,guest,user_id):
    global temp_song
    root = Tk()
    root.title('Music Matches Mood Player')
    mixer.init()
    songs_list = Listbox(root, selectmode=SINGLE, bg="navyblue", fg="white", font=('arial', 15), height=12, width=47,
                         selectbackground="lightblue", selectforeground="black")
    songs_list.grid(columnspan=9)
    # inserting songs in the playlist based on mood
    temp_song = os.listdir(f"C:\\Users\\pa1ka\\Desktop\\Mini Project\\{mood}")
    for s in temp_song:
        songs_list.insert(END, s)
    def addfav():
        song = songs_list.get(ACTIVE)
        file = open(f"C:\\Users\\pa1ka\\Desktop\\Mini Project\\Users\\{user_id}\\" + "fav", "a+")
        file.write(song + '\n')
        file.close()

    def upload_fav():
        songs_list.delete(0, END)
        file = open(f"C:\\Users\\pa1ka\\Desktop\\Mini Project\\Users\\{user_id}\\fav")
        lst = file.read()
        lst = lst.split("\n")
        for s in lst:
            songs_list.insert(END, s)

    def deletesong():
        curr_song = songs_list.curselection()
        songs_list.delete(curr_song[0])

    def add_songs():
        temp_song = tkinter.filedialog.askopenfilenames(initialdir="all songs/", title="Choose a song",
                                                filetypes=(("mp3 Files", "*.mp3"),))
        ##loop through every item in the list to insert in the listbox
        for s in temp_song:
            s = s.replace("all songs/", "")
            s = s.split("Mini Project/")
            songs_list.insert(END, s[1])
    def Play():
        song = songs_list.get(ACTIVE)
        song = f"C:\\Users\\pa1ka\\Desktop\\Mini Project\\all songs\\{song}"
        mixer.music.load(song)
        mixer.music.play()

    # to pause the song
    def Pause():
        mixer.music.pause()

    # to stop the  song
    def Stop():
        mixer.music.stop()
        songs_list.selection_clear(ACTIVE)

    # to resume the song
    def Resume():
        mixer.music.unpause()

    # Function to navigate from the current song
    def Previous():
        # to get the selected song index
        previous_one = songs_list.curselection()
        # to get the previous song index
        previous_one = previous_one[0] - 1
        # to get the previous song
        temp2 = songs_list.get(previous_one)
        temp2 = f'C:\\Users\\pa1ka\\Desktop\\Mini Project\\all songs\\{temp2}'
        mixer.music.load(temp2)
        mixer.music.play()
        songs_list.selection_clear(0, END)
        # activate new song
        songs_list.activate(previous_one)
        # set the next song
        songs_list.selection_set(previous_one)

    def Next():
        # to get the selected song index
        next_one = songs_list.curselection()
        # to get the next song index
        next_one = next_one[0] + 1
        # to get the next song
        temp = songs_list.get(next_one)
        temp = f'C:\\Users\\pa1ka\\Desktop\\Mini Project\\all songs\\{temp}'
        mixer.music.load(temp)
        mixer.music.play()
        songs_list.selection_clear(0, END)
        # activate newsong
        songs_list.activate(next_one)
        # set the next song
        songs_list.selection_set(next_one)

    play_button_img = PhotoImage(file="C:\\Users\\pa1ka\\Desktop\\Mini Project\\icons\\play.png")
    pause_button_img = PhotoImage(file="C:\\Users\\pa1ka\\Desktop\\Mini Project\\icons\\pause.png")
    stop_button_img = PhotoImage(file="C:\\Users\\pa1ka\\Desktop\\Mini Project\\icons\\stop.png")
    prev_button_img = PhotoImage(file="C:\\Users\\pa1ka\\Desktop\\Mini Project\\icons\\previous.png")
    next_button_img = PhotoImage(file="C:\\Users\\pa1ka\\Desktop\\Mini Project\\icons\\next.png")
    resume_button_img = PhotoImage(file="C:\\Users\\pa1ka\\Desktop\\Mini Project\\icons\\resume_1..png")
    # font is defined which is to be used for the button font
    defined_font = font.Font(family='Helvetica')
    # play button
    play_button = Button(root, image=play_button_img, borderwidth=0, command=Play)
    play_button['font'] = defined_font
    play_button.grid(row=1, column=2)
    # pause button
    pause_button = Button(root, image=pause_button_img, borderwidth=0, command=Pause)
    pause_button['font'] = defined_font
    pause_button.grid(row=1, column=1)
    # stop button
    stop_button = Button(root, image=stop_button_img, borderwidth=0, command=Stop)
    stop_button['font'] = defined_font
    stop_button.grid(row=1, column=4)
    # resume button
    Resume_button = Button(root, image=resume_button_img, borderwidth=0, command=Resume)
    Resume_button['font'] = defined_font
    Resume_button.grid(row=1, column=3)
    # previous button
    previous_button = Button(root, image=prev_button_img, borderwidth=0, command=Previous)
    previous_button['font'] = defined_font
    previous_button.grid(row=1, column=0)
    # nextbutton
    next_button = Button(root, image=next_button_img, borderwidth=0, command=Next)
    next_button['font'] = defined_font
    next_button.grid(row=1, column=5)
    # menu
    my_menu = Menu(root)
    root.config(menu = my_menu)
    add_fav_menu = Menu(my_menu)
    my_menu.add_cascade(label="Menu", menu=add_fav_menu)
    add_fav_menu.add_command(label="Add fav", command=addfav)
    add_fav_menu.add_command(label="Upload fav", command=upload_fav)
    add_fav_menu.add_command(label="Add Songs", command=add_songs)
    add_fav_menu.add_command(label="Delete Song", command=deletesong)
    if(guest=="False"):
       my_menu.entryconfig("Menu",state = DISABLED)
    mainloop()

