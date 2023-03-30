import numpy
from scipy.io import wavfile
from scipy.fft import irfft, rfftfreq, rfft
from matplotlib import pyplot as plt


def write_output(output):
    output = output.real
    numpy_output = numpy.array(output, dtype=numpy.int16)
    wavfile.write("output.wav", samplerate, numpy_output)


def draw_output(samples, samplerate, name, cut_off):
    plt.plot(samples)
    title = name + " sound data " + cut_off
    plt.title(title)
    plt.show()

    yf = rfft(samples)
    xf = rfftfreq(len(samples), 1 / samplerate)

    plt.semilogx(abs(xf), numpy.abs(yf))
    title = name + " frequencies " + cut_off
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    cut_off_frequency = input("Please enter cut off frequency: \n")
    samplerate, samples = wavfile.read("sweep.wav")
    draw_output(samples, samplerate, "input", "")
    frequencies = rfft(samples)

    for idx, _ in enumerate(frequencies):
        if idx > int(cut_off_frequency):
            frequencies[idx] = 0

    output = irfft(frequencies)
    draw_output(output, samplerate, "output", cut_off_frequency)

    write_output(output)
