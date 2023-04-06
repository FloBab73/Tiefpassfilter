import numpy
from matplotlib import pyplot as plt
from scipy.fft import irfft, rfftfreq, rfft
from scipy.io import wavfile


def write_output(output, samplerate):
    output = output.real
    numpy_output = numpy.array(output, dtype=numpy.int16)
    wavfile.write("output.wav", samplerate, numpy_output)


def read_input():
    cut_off_frequency = input("Please enter cut off frequency (standard is 1000Hz): \n")
    file_name = input("Please enter file name (standard is violin.wav): \n")
    if file_name == "":
        file_name = "violin.wav"
    if cut_off_frequency == "":
        cut_off_frequency = 1000
    else:
        cut_off_frequency = int(cut_off_frequency)
    samplerate, samples = wavfile.read(file_name)
    return samplerate, samples, cut_off_frequency


def draw_output(samples, samplerate, name, cut_off):
    plt.plot(samples)
    title = name + "_sound_data_" + str(cut_off)
    plt.title(title)
    plt.savefig(title + '.png')
    plt.close()

    yf = rfft(samples)
    xf = rfftfreq(len(samples), 1 / samplerate)

    plt.semilogx(abs(xf), numpy.abs(yf))
    title = name + "_frequencies_" + str(cut_off)
    plt.title(title)
    plt.savefig(title + '.png')
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
