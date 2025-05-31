#!/usr/bin/env python3
import threading
from pynput import keyboard
from pynput.keyboard import Key
import pyautogui
from whisper_mic import WhisperMic
import queue
import time
import pyperclip

class WhisperHotkey:
    def __init__(self):
        import whisper
        # Load model once at startup for speed
        print("🔄 Loading Whisper model... (this may take a moment)")
        self.model = whisper.load_model("turbo")
        print("✅ Model loaded!")
        
        self.recording = False
        self.result_queue = queue.Queue()
        
    def start_recording(self):
        """Start recording when key is pressed"""
        if not self.recording:
            self.recording = True
            print("🎤 Recording... (hold key and speak)")
            # Start recording in a separate thread
            self.record_thread = threading.Thread(target=self._record_audio)
            self.record_thread.daemon = True
            self.record_thread.start()
    
    def stop_recording(self):
        """Stop recording when key is released"""
        if self.recording:
            self.recording = False
            print("🛑 Processing...")
    
    def _record_audio(self):
        """Record audio while key is held"""
        import sounddevice as sd
        import numpy as np
        
        try:
            # Record while key is held
            audio_data = []
            sample_rate = 16000
            
            def audio_callback(indata, frames, time, status):
                if self.recording:
                    audio_data.extend(indata[:, 0])
            
            with sd.InputStream(samplerate=sample_rate, channels=1, callback=audio_callback):
                while self.recording:
                    sd.sleep(100)  # Sleep 100ms
            
            if audio_data:
                # Convert to numpy array and normalize
                audio_array = np.array(audio_data, dtype=np.float32)
                
                # Use pre-loaded model for faster transcription
                result = self.model.transcribe(
                    audio_array, 
                    fp16=False,  # Use FP32 for CPU
                    verbose=False  # Reduce output
                )
                
                if result["text"].strip():
                    self.result_queue.put(result["text"].strip())
                else:
                    print("❌ No speech detected")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def on_press(self, key):
        # On macOS, use Right Command (Cmd) key
        if key == Key.cmd_r:
            self.start_recording()
    
    def on_release(self, key):
        if key == Key.cmd_r:
            self.stop_recording()
    
    def insert_text_at_cursor(self, text):
        """Insert text directly at cursor position using AppleScript"""
        import subprocess
        
        # Escape quotes in the text for AppleScript
        escaped_text = text.replace('"', '\\"').replace('\\', '\\\\')
        
        # Use AppleScript to insert text at current cursor position
        applescript = f'''
        tell application "System Events"
            keystroke "{escaped_text}"
        end tell
        '''
        
        subprocess.run(['osascript', '-e', applescript])
    
    def run(self):
        print("🎯 Whisper Mic Hotkey Ready!")
        print("Hold Right Command (⌘) to record, release to transcribe")
        print("Close terminal to exit")
        print("-" * 40)
        
        # Start keyboard listener
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            # Process results in main thread
            while listener.running:
                try:
                    # Check for transcription results
                    result = self.result_queue.get(timeout=0.1)
                    print(f"✅ Transcribed: {result}")
                    # Insert text directly at cursor position
                    self.insert_text_at_cursor(result)
                except queue.Empty:
                    pass
                except Exception as e:
                    print(f"Error processing result: {e}")

def main():
    hotkey = WhisperHotkey()
    hotkey.run()

if __name__ == "__main__":
    main()