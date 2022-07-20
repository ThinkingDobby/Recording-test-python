import queue, threading

import sounddevice as sd
import soundfile as sf

q = queue.Queue()
recorder = False
recording = False

storage_path = 'test.wav'


def complicated_record():
    with sf.SoundFile(storage_path, mode='w', samplerate=16000, subtype='PCM_16', channels=1) as file:
        with sd.InputStream(samplerate=16000, dtype='int16', channels=1, callback=complicated_save):
            while recording:
                file.write(q.get())


def complicated_save(indata, frames, time, status):
    q.put(indata.copy())


# 녹음 시작
def start_recording():
    global recorder
    global recording
    recording = True
    recorder = threading.Thread(target=complicated_record)
    print('start recording')
    recorder.start()


# 녹음 중지
def stop_recording():
    global recorder
    global recording
    recording = False
    recorder.join()
    print('stop recording')