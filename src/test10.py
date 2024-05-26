import pyaudio
import wave
import time
import threading

# Parameters for audio capture
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
DURATION = 10  # Duration to record in seconds
OUTPUT_FILENAME = "output.wav"

# Function to record audio
def record_audio():
    audio = pyaudio.PyAudio()

    # Start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    
    print("Recording...")
    frames = []

    for _ in range(0, int(RATE / CHUNK * DURATION)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    print("Finished recording.")
    
    # Stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recording as a WAV file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def record_audio_periodically():
    while True:
        record_audio()
        time.sleep(10)  # Wait for 10 seconds before recording the next sample

# Use threading to run the periodic recording in the background
recording_thread = threading.Thread(target=record_audio_periodically)
recording_thread.start()
