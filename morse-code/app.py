import numpy as np 
import wave 
from struct import pack 
import sys

# storing the morse format in dictionaries
morse_format = {
    "a": ["dot", "line"],
    "b": ["line", "dot", "dot", "dot"],
    "c": ["line", "dot", "line", "dot"],
    "d": ["line", "dot", "dot"],
    "e": ["dot"],
    "f": ["dot", "dot", "line", "dot"],
    "g": ["line", "line", "dot"],
    "h": ["dot", "dot", "dot", "dot"],
    "i": ["dot", "dot"],
    "j": ["dot", "line", "line", "line"],
    "k": ["line", "dot", "line"],
    "l": ["dot", "line", "dot", "dot"],
    "m": ["line", "line"],
    "n": ["line", "dot"],
    "o": ["line", "line", "line"],
    "p": ["dot", "line", "line", "dot"],
    "q": ["line", "line", "dot", "line"],
    "r": ["dot", "line", "dot"],
    "s": ["dot", "dot", "dot"],
    "t": ["line"],
    "u": ["dot", "dot", "line"],
    "v": ["dot", "dot", "dot", "line"],
    "w": ["dot", "line", "line"],
    "x": ["line", "dot", "dot", "line"],
    "y": ["line", "dot", "line", "line"],
    "z": ["line", "line", "dot", "dot"],
    "1": ["dot", "line", "line", "line", "line"],
    "2": ["dot", "dot", "line", "line", "line"],
    "3": ["dot", "dot", "dot", "line", "line"],
    "4": ["dot", "dot", "dot", "dot", "line"],
    "5": ["dot", "dot", "dot", "dot", "dot"],
    "6": ["line", "dot", "dot", "dot", "dot"],
    "7": ["line", "line", "dot", "dot", "dot"],
    "8": ["line", "line", "line", "dot", "dot"],
    "9": ["line", "line", "line", "line", "dot"],
    "0": ["line", "line", "line", "line", "line"],
    ".": ["dot", "line", "dot", "line", "dot", "line"],
    ",": ["line", "line", "dot", "dot", "line", "line"],
    "?": ["dot", "dot", "line", "line", "dot", "dot"],
    " ": ["empty"]
}

def main(audio_file, text):
    """Returns the string generated from the given audio file
    and writes a morse code from the given text"""
    Fs = 44100 # sample frequency
    f = 440 # frequency in hertz
    duration_for_dot = 0.5 # duration of the sound
    duration_for_line = 1.5 # duration of the line
    volume = 50 

    # defining the numpy arrays to iterate over
    x = np.arange(round(Fs * duration_for_dot))
    y = np.arange(round(Fs * duration_for_line))

    # defining the essential audio variables
    dot = volume * np.sin(2 * np.pi * f * x / Fs)
    line = volume * np.sin(2 * np.pi * f * y / Fs)
    empty = np.zeros(round(Fs * duration_for_dot))

    # initializing the wave function
    wav = wave.open(audio_file, "wb")
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(Fs)

    # formatting the text 
    unwanted_set = set()
    possible_inputs = [letter for letter in morse_format]
    text = text.lower()
    for letter in text:
        if letter not in possible_inputs:
            unwanted_set.add(letter)
    for unwanted_letter in unwanted_set:
        text = text.replace(unwanted_letter, "")
    print(text)

    # writing to the wav file 
    string = ""
    for char in text:
        for morse_code in morse_format[char]:
            if morse_code == "dot": 
                for i in dot:
                    data = pack("b", int(i))
                    wav.writeframesraw(data)
                for i in empty:
                    data = pack("b", int(i))
                    wav.writeframesraw(data)
                string = string + "."
            elif morse_code == "line": 
                for i in line:
                    data = pack("b", int(i))
                    wav.writeframesraw(data)
                for i in empty:
                    data = pack("b", int(i))
                    wav.writeframesraw(data)
                string = string + "-"
            elif morse_code == "empty":
                for i in empty:
                    data = pack("b", int(i))
                    wav.writeframesraw(data)
        string = string + "/"

    return string

# final script
if __name__ == "__main__": 
    if len(sys.argv) < 3:
        raise RuntimeError("\033[91m"+"\033[1m"+"Schema - python3 file.py audio_file.wav text_file.txt")

    # reading test and valuating the file presence
    text = None
    try: 
        print("\033[92m" + "The audio file will be crated if not already" + "\033[37m")
        audio_file = sys.argv[1]
        text_file = sys.argv[2]
        with open(audio_file, "w") as f:
            pass
        with open(text_file) as f:
            text = f.read()
    except IOError:
        raise RuntimeError("\033[91m"+"\033[1m"+"Your file does not exist. Make sure you have the text file")
    string = main(audio_file, text)
    print(string)
