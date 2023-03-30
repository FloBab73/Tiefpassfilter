import math

import numpy
from scipy.io import wavfile

cut_off_frequency = 100
samplerate, data = wavfile.read("input.wav")

filter_range = round(samplerate / cut_off_frequency)

bigger_data = numpy.array(data, dtype=numpy.int64)


def average_value(index, r):
    value = bigger_data[index]
    for i in range(0, r):
        value += bigger_data[index + i]
        value += bigger_data[index - i]

    value /= r * 2 + 1
    value = math.floor(value)
    return value


print("samplerate: ", samplerate)
print("data: ", len(data))

output = []
for index in range(filter_range, len(bigger_data) - filter_range):
    temp = average_value(index, filter_range)
    output.append(temp)

numpy_output = numpy.array(output, dtype=numpy.int16)
wavfile.write("output.wav", samplerate, numpy_output)
