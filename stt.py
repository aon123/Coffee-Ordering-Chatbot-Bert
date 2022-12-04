
import pyaudio
import wave
import whisper

def recordVoice():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 3

    p = pyaudio.PyAudio()


    stream = p.open(format=FORMAT, rate=RATE, channels=CHANNELS, frames_per_buffer=CHUNK, input=True)

    frames = []

    print("* recording")


    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.start_stream()
    stream.close()
    p.terminate()



    sound_file = wave.open('output.wav', 'wb')
    sound_file.setnchannels(1)
    sound_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    sound_file.setframerate(RATE)
    sound_file.writeframes(b''.join(frames))
    sound_file.close()


    model = whisper.load_model("base")
    result = model.transcribe("output.wav",  fp16=False, language='English')
    return result["text"]
