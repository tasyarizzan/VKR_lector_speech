import librosa
import os
import wave
import struct
import pyAudioAnalysis
import speech_recognition as sr
import time
import random

#path = os.path.join(os.path.abspath(''), '9500a1ef1441.mp3')
#wav, sr = librosa.load(path, mono=True, sr=target_sr)

def get_volume_times(wav_path, threshold=100000, threshold_low=100, time_constant=0.1):
    wav = wave.open(wav_path, 'r')

    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'


    is_loud = False
    is_low = False
    # result = [(0., is_loud)]
    a = []
    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2


        new_is_loud = variance > threshold
        new_is_low = variance < threshold_low

        if is_low != new_is_low:
            a.append(sample_time)
        if is_loud != new_is_loud:
            a.append(sample_time)

        is_low = new_is_low
        is_loud = new_is_loud

    result = sum(a)/len(a)
    return result


def speech_to_text(wav_path):
        try:

            wav = wave.open(wav_path, 'r')
            length = wav.getnframes()
            rate = wav.getframerate()
            duration = length / float(rate)

            # print('длительность', duration)

            rec = sr.Recognizer()
            harvard = sr.AudioFile(wav_path)
            with harvard as source:
                audio = rec.record(source)
            text = rec.recognize_google(audio, language="ru_RU")
            if len(text) > 0:
                list_txt = text.split()
                myset = set(list_txt)
                tempo = len(myset) / duration
                #print('Длина списка:', len(myset), ' Длительность: ', duration, 'ТЕМП =', tempo)
                return  tempo
            else:
                return 0
        except Exception as e:
            print(e)



def otnosh(wav_path, THRESHOLD_SILENSE = 10, time_constant=0.1):
    wav = wave.open(wav_path, 'r')
    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'

    bin = []

    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2

        if variance > THRESHOLD_SILENSE:
            bin.append(1)
        else:
            bin.append(0)

    res = bin.count(0) / bin.count(1)
    return res

def get_noise(wav_path, THRESHOLD_SILENSE = 10, time_constant=0.1):
    wav = wave.open(wav_path, 'r')
    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'

    bin = []

    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2

        if variance > THRESHOLD_SILENSE:
            bin.append(1)
        else:
            bin.append(0)

    res = bin.count(1) / len(bin)
    return res

def get_monotone(wav_path, THRESHOLD_MONOTONE = 10, time_constant=0.1):
    wav = wave.open(wav_path, 'r')
    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'

    bin = []

    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2

        if variance > THRESHOLD_MONOTONE:
            bin.append(1)
        else:
            bin.append(0)
    res = bin.count(0) / bin.count(1)
    return res

def get_intfrnce_distn(wav_path, threshold=100000, threshold_low=100, time_constant=0.1):
    wav = wave.open(wav_path, 'r')

    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'


    is_loud = False
    is_low = False
    # result = [(0., is_loud)]
    a = []
    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2


        new_is_loud = variance > threshold
        new_is_low = variance < threshold_low

        if is_low != new_is_low:
            a.append(0)
        if is_loud != new_is_loud:
            a.append(1)

        is_low = new_is_low
        is_loud = new_is_loud

    result = a.count(1) / len(a)
    return result

def get_tone_balance(wav_path, threshold=100000, threshold_low=100, time_constant=0.1):
    wav = wave.open(wav_path, 'r')

    length = wav.getnframes()
    samplerate = wav.getframerate()

    assert wav.getnchannels() == 1, 'wav must be mono'
    assert wav.getsampwidth() == 2, 'wav must be 16-bit'


    is_loud = False
    is_low = False
    # result = [(0., is_loud)]
    a = []
    mean = 0
    variance = 0

    alpha = 1 / (time_constant * float(samplerate))

    for i in range(length):
        sample_time = float(i) / samplerate
        sample = struct.unpack('<h', wav.readframes(1))
        sample = sample[0]
        mean = (1 - alpha) * mean + alpha * sample
        variance = (1 - alpha) * variance + alpha * (sample - mean) ** 2


        new_is_loud = variance > threshold
        new_is_low = variance < threshold_low

        if is_low != new_is_low:
            a.append(0)
        if is_loud != new_is_loud:
            a.append(1)

        is_low = new_is_low
        is_loud = new_is_loud

    result = a.count(1) / len(a)
    return result



def get_intenference(wav_path):
    result = random.uniform(0,10)
    return result


