import pvporcupine
import pyaudio
import struct

def listen_for_wake_word(keyword="hey agent"):
    porcupine = pvporcupine.create(keywords=[keyword])
    pa = pyaudio.PyAudio()
    stream = pa.open(rate=porcupine.sample_rate,
                     channels=1,
                     format=pyaudio.paInt16,
                     input=True,
                     frames_per_buffer=porcupine.frame_length)

    print(f"🎤 Listening for wake word: {keyword}")
    while True:
        pcm = stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        result = porcupine.process(pcm)
        if result >= 0:
            print("✅ Wake word detected!")
            break

    stream.close()
    pa.terminate()
    porcupine.delete()
