import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import moviepy.editor as mp
import subprocess
import threading

def convert_to_mp3(input_file, output_file):
    video = mp.VideoFileClip(input_file)
    audio = video.audio
    audio.write_audiofile(output_file)
    video.close()
    audio.close()

def select_file():
    input_file = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if input_file:
        output_file = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
        if output_file:
            convert_thread = threading.Thread(target=convert_to_mp3, args=(input_file, output_file))
            convert_thread.start()
            convert_button.config(text="Please wait...", state="disabled")
            status_label.config(text="Converting...")
            convert_thread.join()
            convert_button.config(text="Convert to MP3", state="normal")
            status_label.config(text="Conversion successful!")
            play_button.config(state="normal") 

def play_audio(): # i stoped here i cant play the file
        subprocess.Popen(["xdg-open", output_file])

# Create the main window
window = tk.Tk()
window.title("MP4 to MP3 Converter")
background_color = "#161b22"
window.config(background=background_color)
window.geometry("400x100")

# Define a professional theme
theme = ttk.Style()
theme.theme_use("alt")
theme.configure("TButton", foreground="white", background="#0078D4", font=("Helvetica", 10))
theme.configure("TLabel", foreground="black", background="#161b22", font=("Helvetica", 10))
theme.map("TButton", foreground=[('active', 'black')])

# Create a frame for button alignment
button_frame = tk.Frame(window)
button_frame.pack(expand=True, pady=10)

# Create buttons with the defined theme
select_button = ttk.Button(button_frame, text="Select MP4 File", command=select_file)
select_button.pack(side="left", padx=1, pady=1, fill="x", expand=True)

convert_button = ttk.Button(button_frame, text="Convert to MP3", command=select_file)
convert_button.pack(side="left", padx=1, pady=1, fill="x", expand=True)

play_button = ttk.Button(button_frame, text="Play", state="disabled", command=play_audio)
play_button.pack(side="left", padx=1, pady=1, fill="x", expand=True)

# Display status
status_label = ttk.Label(window, text="", foreground="white", anchor="center")
status_label.pack(fill="x")

# Start the GUI event loop
window.mainloop()
