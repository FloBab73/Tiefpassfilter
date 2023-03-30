import math
import numpy
from scipy.io import wavfile
bigger_data = numpy.empty(0)


def average_value(index, r):
    value = bigger_data[index]
    for i in range(0, r):
        value += bigger_data[index + i]
        value += bigger_data[index - i]

    value /= r * 2 + 1
    value = math.floor(value)
    return value


def write_output(output):
    numpy_output = numpy.array(output, dtype=numpy.int16)
    wavfile.write("output.wav", samplerate, numpy_output)


if __name__ == '__main__':
    cut_off_frequency = input("Please enter cut off frequency")
    samplerate, data = wavfile.read("input.wav")
    filter_range = round(samplerate / int(cut_off_frequency))
    bigger_data = numpy.array(data, dtype=numpy.int64)

    output = []
    for index in range(filter_range, len(bigger_data) - filter_range):
        temp = average_value(index, filter_range)
        output.append(temp)

    write_output(output)
