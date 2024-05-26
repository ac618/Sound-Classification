import pyaudio
import wave
import numpy as np
import time

# Parameters
CHUNK = 1024  # Number of frames per buffer
FORMAT = pyaudio.paInt16  # 16-bit audio
CHANNELS = 4  # Mono audio
RATE = 48000  # Sampling rate in Hz
SEGMENT_DURATION = 2  # Segment duration in seconds
OVERLAP = 1  # Overlap duration in seconds
WAV_FILENAME = "temp_audio_segment.wav"

p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def get_audio_segment(stream, duration, overlap):
    segment_frames = int(RATE * duration)
    frames = []
    while len(frames)*CHUNK < segment_frames:
        data = stream.read(CHUNK)
        frames.append(data)
        # print(len(frames)*len(data), segment_frames)
    return b''.join(frames)

def save_wav_file(filename, audio_data):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(audio_data)

def process_audio():
    print("Starting audio processing")
    try:
        while True:
            audio_segment = get_audio_segment(stream, SEGMENT_DURATION, OVERLAP)
            save_wav_file(WAV_FILENAME, audio_segment)
            # Classify the saved .wav file
            time.sleep(SEGMENT_DURATION - OVERLAP)
    except KeyboardInterrupt:
        print("Stopping audio processing")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

process_audio()
