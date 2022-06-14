from pydub import AudioSegment
from pathlib import Path
# pip install git+https://github.com/exeex/vocoder_eva.git
from vocoder_eva.eval import eval_rmse_f0
import librosa

def convert():
    pathlist = Path("input_wavs_dir")

    for path in pathlist:
        filename = path.stem

        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/output_dir/{}.mp4}.".format(filename), format="mp4")
        AudioSegment.from_wav("/input/{}.wav".format(filename))\
            .export("/output_dir/{}.mp3".format(filename), format="mp3")
        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/output_dir/{}.ogg".format(filename), format="ogg")
        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/output_dir/{}.flac".format(filename), format="flac")
        AudioSegment.from_wav("/input/{}.wav".format(filename)) \
            .export("/output_dir/{}.webm".format(filename), format="webm")

def score():
    pathlist = Path("input_wavs_dir")

    # import soundfile as sf
    # from pystoi import stoi
    #
    # clean, fs = sf.read('path/to/clean/audio')
    # denoised, fs = sf.read('path/to/denoised/audio')
    #
    # # Clean and den should have the same length, and be 1D
    # d = stoi(clean, denoised, fs, extended=False)

    # from scipy.io import wavfile
    # from pesq import pesq
    #
    # rate, ref = wavfile.read("./audio/speech.wav")
    # rate, deg = wavfile.read("./audio/speech_bab_0dB.wav")
    #
    # print(pesq(rate, ref, deg, 'wb'))
    # print(pesq(rate, ref, deg, 'nb'))
    nf = 50
    ss_mp4 = 0
    ps_mp4 = 0
    fs_mp4 = 0
    ss_mp3 = 0
    ps_mp3 = 0
    fs_mp3 = 0
    ss_ogg = 0
    ps_ogg = 0
    fs_ogg = 0
    ss_flac = 0
    ps_flac = 0
    fs_flac = 0
    ss_webm = 0
    ps_webm = 0
    fs_webm = 0


    for path in pathlist:
        filename = path.stem
        ext = path.suffix

        if ext == ".mp4":
            continue
        if ext == ".mp3":
            continue
        if ext == ".ogg":
            continue
        if ext == ".flac":
            continue
        if ext == ".webm":
            continue

def pickles():
    pathlist = Path("input_wavs_dir")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
