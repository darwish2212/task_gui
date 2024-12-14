import tkinter as tk
import pyttsx3

engine= pyttsx3.init()
 
root=tk.Tk()
root.title("text to speech")
root.geometry("400x400")


def play_text():
    text= text_box.get("1.0","end-1c")
    if text:
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def sit_text():
    text_box.delete("1.0","end")
def exit_program():
    root.quit()
label = tk.Label(root, text="entr your text", font=("Arial",14))
label.pack(pady=10)

text_box=tk.Text(root,height=6,width=40)
text_box.pack(pady=10)

button_play=tk.Button(root,text="play",command=play_text)
button_play.pack(side="left",padx=10,pady=10)

button_sit=tk.Button(root,text="sit",command=sit_text)
button_sit.pack(side="left",padx=10,pady=10)

button_exit=tk.Button(root,text="exit",command=exit_program )
button_exit.pack(side="left",padx=10,pady=10)

root.mainloop()

