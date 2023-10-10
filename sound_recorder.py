import os
import time
import threading
import tkinter as tk
import numpy as np
import sounddevice as sd
import wavio
from scipy.io import wavfile

class VoiceRecorder:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.frame = tk.Frame(self.root, bd=0, borderwidth=10, relief="raised")
        self.frame.pack()
        self.button = tk.Button(self.frame, text="🎙️", command=self.click_handler, 
                        font=("Arial", 120, "bold"), relief="raised", 
                        highlightbackground="#ffffff",
                        highlightthickness=4, bd=0, padx=0, pady=0)
        self.button.pack()

        self.label = tk.Label(self.root, text="00:00:00")
        self.label.pack()

        self.recording = False

        self.root.mainloop()

    def click_handler(self):
        if self.recording:
            self.recording = False
            self.frame.config(relief="raised")
            self.button.config(highlightbackground="#ffffff")
        else:
            self.recording = True
            self.frame.config(relief="sunken")
            self.button.config(highlightbackground="green")
            threading.Thread(target=self.record).start()

    def record(self):
        filename = self.get_next_filename()
        samplerate = 44100
        duration = 0  # Recording duration, initially 0
        recording = []

        def callback(indata, frames, time, status):
            if status:
                print(status, flush=True)
            if any(indata):
                recording.append(indata.copy())
            nonlocal duration
            duration += frames / samplerate

        with sd.InputStream(callback=callback, channels=1, samplerate=samplerate):
            while self.recording:
                time.sleep(0.1)  # Update recording duration every 0.1 seconds
                passed = int(duration)
                secs = passed % 60
                mins = (passed // 60) % 60
                hours = passed // 3600
                self.label.config(text=f"{hours:02d}:{mins:02d}:{secs:02d}")

        # Save the recording to a WAV file
        recording = np.concatenate(recording, axis=0)
        wavio.write(filename, recording, rate=samplerate, sampwidth=2)

    def get_next_filename(self):
        i = 1
        while os.path.exists(f"recording{i}.wav"):
            i += 1
        return f"recording{i}.wav"

VoiceRecorder()
