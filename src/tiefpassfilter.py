import numpy
from matplotlib import pyplot as plt
from scipy.fft import irfft, rfftfreq, rfft, fft, fftfreq
from scipy.io import wavfile
import sys


def write_output(output, samplerate):
    output = output.real
    numpy_output = numpy.array(output, dtype=numpy.int16)
    wavfile.write("../out/output.wav", samplerate, numpy_output)


def read_input():
    if len(sys.argv) < 3:
        cut_off_frequency = 1000
        file_name = "../res/violin.wav"
    else:
        cut_off_frequency = int(sys.argv[1])
        file_name = "../res/" + sys.argv[2] + ".wav"

    samplerate, samples = wavfile.read(file_name)
    return samplerate, samples, cut_off_frequency


def draw_output(samples, samplerate, name, cut_off):
    plt.plot(samples)
    title = name + "_sound_data_" + str(cut_off)
    plt.title(title)
    plt.savefig("../out/" + title + '.png')
    plt.close()

    yf = fft(samples)
    xf = fftfreq(len(samples), 1 / samplerate)
    plt.semilogx(abs(xf), numpy.abs(yf))
    title = name + "_frequencies_" + str(cut_off)
    plt.title(title)
    plt.savefig("../out/" + title + '.png')
    plt.close()


def main():
    samplerate, samples, cut_off_frequency = read_input()
    draw_output(samples, samplerate, "input", "")
    frequencies = rfft(samples)
    frequency_steps = rfftfreq(len(samples), 1 / samplerate)

    idx_per_freq = len(frequency_steps) / (samplerate / 2)
    target_idx = int(idx_per_freq * int(cut_off_frequency))

    for idx, _ in enumerate(frequencies):
        if idx > target_idx:
            frequencies[idx] = 0

    output = irfft(frequencies)
    draw_output(output, samplerate, "output", cut_off_frequency)

    write_output(output, samplerate)


if __name__ == '__main__':
    main()
