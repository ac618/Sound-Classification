import os
import laion_clap
import pyaudio
import time
import wave
import serial
from playsound import playsound

## Serial Port ##
port = 'COM6'  # Change this to your specific port
baud_rate = 9600
serial_on = False # turn on to transfer

## Audio Recording Parameters ##
CHUNK = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16  # 16-bit audio
CHANNELS = 4 # 4 chnnels
RATE_HZ = 48000  # Sampling rate in Hz
SEGMENT_DURATION_SECONDS = 2  # Segment duration in seconds
OVERLAP_SECONDS = 0  # Overlap duration in seconds
audio_dir = os.path.join(os.path.dirname(__file__), os.pardir, 'audio')
WAV_PATH = os.path.join(audio_dir, "temp_audio_segment.wav")

## Functions ##
def classify_audio(model, class_embeds, audio_path = 'glass/glass2.mp3'):
    audio_file = [
        audio_path
    ]
    audio_embed = model.get_audio_embedding_from_filelist(x = audio_file, use_tensor=False)

    max_sim = 0
    idx = 0

    for i in range(class_embeds.shape[0]):
        class_embed = class_embeds[i]

        sim = audio_embed @ class_embed.T
        print([classes[i], sim])

        if (sim > max_sim):
            max_sim = sim
            idx = i

    return classes[idx], idx

def get_audio_segment(stream, duration):
    segment_frames = int(RATE_HZ * duration)
    frames = []
    while len(frames)*CHUNK < segment_frames:
        data = stream.read(CHUNK)
        frames.append(data)
    return b''.join(frames)

def save_wav_file(filename, audio_data):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE_HZ)
        wf.writeframes(audio_data)

## Initialize Classifier ##
model = laion_clap.CLAP_Module(enable_fusion=False)
model.load_ckpt() # download the default pretrained checkpoint.

classes = [
  "plastic bottle",
  "can",
  "glass",
  "paper",
  "others"
]

class_embeds = model.get_text_embedding(classes)

audio = pyaudio.PyAudio()

# Open stream
stream = audio.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE_HZ,
                input=True,
                frames_per_buffer=CHUNK)

# Start serial
if serial_on:
    ser = serial.Serial(port, baud_rate, timeout=1)
print("Starting audio processing")

try:
    while True:
        audio_segment = get_audio_segment(stream, SEGMENT_DURATION_SECONDS)
        save_wav_file(WAV_PATH, audio_segment)
        # Classify the saved .wav file
        result, idx = classify_audio(model, class_embeds, WAV_PATH)
        print(result)
        # play sound effect
        if result != 'others':
            effect_path = os.path.join(audio_dir, 'effects', f'{result}.wav')
            playsound(effect_path)
        # transfer result via serial
        data_to_send = str(idx).encode()  # Data to be sent, convert to bytes
        if serial_on:
            ser.write(data_to_send)
        print(f"Sent: {data_to_send.decode()}")

        time.sleep(SEGMENT_DURATION_SECONDS - OVERLAP_SECONDS)

except KeyboardInterrupt:
    print("Stopping audio processing")
finally:
    stream.stop_stream()
    stream.close()
    audio.terminate()
    if serial_on:
        ser.close()