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


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
