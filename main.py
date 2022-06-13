from pydub import AudioSegment
from pathlib import Path

pathlist = Path("input_wavs_dir")

for path in pathlist:
    filename = path.stem
    AudioSegment.from_wav("/input/{}.wav".format(filename))\
        .export("/output_dir/{}.mp3".format(filename), format="mp3")

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
