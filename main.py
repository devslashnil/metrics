from pydub import AudioSegment
from pathlib import Path
# pip install git+https://github.com/exeex/vocoder_eva.git
import librosa
import soundfile as sf
from pystoi import stoi
from scipy.io import wavfile
# TODO: linux
# from pesq import pesq
from collections import defaultdict
import os.path

path_wavs = './original_wavs'
num_files = len([f for f in os.listdir(path_wavs)
                 if os.path.isfile(os.path.join(path_wavs, f))])

def convert():
    pathlist = Path("input_wavs_dir")

    for path in pathlist:
        filename = path.stem

        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/converted_wavs/{}.mp4}.".format(filename), format="mp4")
        AudioSegment.from_wav("/input/{}.wav".format(filename))\
            .export("/converted_wavs/{}.mp3".format(filename), format="mp3")
        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/converted_wavs/{}.ogg".format(filename), format="ogg")
        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/converted_wavs/{}.flac".format(filename), format="flac")
        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/converted_wavs/{}.webm".format(filename), format="webm")

def score():
    d = {}
    for i in ['.hifi', '.mp4', '.mp3', '.ogg', '.flac', '.webm']:
        d[i] = {}
        for j in ['stoi', 'pesq', 'size']:
            d[j] = 0

    for path in Path("converted_wavs"):
        filename = path.stem
        ext = path.suffix
        clean, fs = sf.read('./original_wavs/{}.wav'.format(filename))
        denoised, fs = sf.read(path)
        d[ext]['stoi'] += stoi(clean, denoised, fs, extended=False)
        rate, ref = wavfile.read('./original_wavs/{}.wav'.format(filename))
        rate, deg = wavfile.read(path)
        # TODO: linux
        # d[ext]['pesq'] += pesq(rate, ref, deg, 'wb')
        d[ext]['size'] += path.stat().st_size
        if (d['.hifi']['stoi'] == 0):
            path = Path("generated_wavs")
            denoised, fs = sf.read(path)
            rate, deg = wavfile.read(path)
            d['.hifi']['stoi'] += stoi(clean, denoised, fs, extended=False)
            # d['.hifi']['pesq'] += pesq(rate, ref, deg, 'wb')
            d['.hifi']['size'] += path.stat().st_size

    for i in ['.mp4', '.mp3', '.ogg', '.flac', '.webm']:
        d[i] = {}
        for j in ['stoi', 'pesq', 'size']:
            d[j] /= num_files
    print(d)


def pickles():
    s = 0
    for path in Path("mel_files"):
         s += path.stat().st_size
    s /= num_files
    print(s)



def main():
    convert()
    score()
    pickles()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
