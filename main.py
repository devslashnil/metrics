from pydub import AudioSegment
from pathlib import Path
# pip install git+https://github.com/exeex/vocoder_eva.git
import soundfile as sf
from pystoi import stoi
from scipy.io import wavfile
from pesq import pesq
import os.path

path_wavs = './original_wavs'
num_files = len([f for f in os.listdir(path_wavs)
                 if os.path.isfile(os.path.join(path_wavs, f))])


def convert():
    print('--- Convert start')
    filepath = "original_wavs"
    for path in Path(filepath).iterdir():
        filename = path.stem

        of = "./{}/{}.wav".format(filepath, filename)
        sd = "./converted_wavs"
        AudioSegment.from_wav(of).export("{}/{}.mp4".format(sd, filename), format="mp4")
        AudioSegment.from_wav(of).export("{}/{}.mp3".format(sd, filename), format="mp3")
        AudioSegment.from_wav(of).export("{}/{}.ogg".format(sd, filename), format="ogg")
        AudioSegment.from_wav(of).export("{}/{}.flac".format(sd, filename), format="flac")
        AudioSegment.from_wav(of).export("{}/{}.webm".format(sd, filename), format="webm")
    print('--- Convert end')


def score():
    print('--- Score start')
    d = {}
    for i in ['.hifi', '.mp4', '.mp3', '.ogg', '.flac', '.webm']:
        d[i] = {}
        for j in ['stoi', 'pesq', 'size']:
            d[i][j] = 0
    print('--- d', d)
    for path in Path("original_wavs").iterdir():
        filename = path.stem
        clean, fs = sf.read('./original_wavs/{}.wav'.format(filename))
        rate, ref = wavfile.read('./original_wavs/{}.wav'.format(filename))
        denoised, fs = sf.read('./generated_wavs/{}_generated.wav'.format(filename))
        rate, deg = wavfile.read('./generated_wavs/{}_generated.wav'.format(filename))
        d['.hifi']['stoi'] += stoi(clean, denoised, fs, extended=False)
        d['.hifi']['pesq'] += pesq(rate, ref, deg, 'wb')
        d['.hifi']['size'] += path.stat().st_size
    print(d['.hifi'])
    # for path in Path("converted_wavs").iterdir():
    #     filename = path.stem
    #     # ext = path.suffix
    #     # clean, fs = sf.read('./original_wavs/{}.wav'.format(filename))
    #     # denoised, fs = sf.read(path)
    #     # d[ext]['stoi'] += stoi(clean, denoised, fs, extended=False)
    #     clean, fs = sf.read('./original_wavs/{}.wav'.format(filename))
    #     # rate, ref = wavfile.read('./original_wavs/{}.wav'.format(filename))
    #     rate, ref = wavfile.read('./original_wavs/{}.wav'.format(filename))
    #     # rate, deg = wavfile.read(path)
    #     # d[ext]['pesq'] += pesq(rate, ref, deg, 'wb')
    #     # d[ext]['size'] += path.stat().st_size
    #     if (d['.hifi']['stoi'] == 0):
    #         path = Path("generated_wavs")
    #         denoised, fs = sf.read(path)
    #         rate, deg = wavfile.read(path)
    #         d['.hifi']['stoi'] += stoi(clean, denoised, fs, extended=False)
    #         d['.hifi']['pesq'] += pesq(rate, ref, deg, 'wb')
    #         d['.hifi']['size'] += path.stat().st_size

    for i in ['.mp4', '.mp3', '.ogg', '.flac', '.webm']:
        d[i] = {}
        for j in ['stoi', 'pesq', 'size']:
            d[i][j] /= num_files
    print(d)
    print('--- Score end')


def pickles():
    print('--- Pickles start')
    s = 0
    for path in Path("mel_files").iterdir():
        s += path.stat().st_size
    s /= num_files
    print(s)
    print('--- Pickles end')


def main():
    print('--- Start')
    # convert()
    # score()
    pickles()
    print('--- End')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
