import numpy as np
from matplotlib import pyplot as plt

def plot_magnitude_spectrum(signal, title, sample_rate, f_ratio=0.1):
    ft = np.fft.fft(signal)
    magnitude_spectrum = np.abs(ft)

    # plot magnitud
    plt.figure(figsize=(18,5))

    frequency = np.linspace(0, sample_rate, len(magnitude_spectrum))
    num_frequency_bins = int(len(frequency) * f_ratio)

    plt.plot(frequency[:num_frequency_bins], magnitude_spectrum[:num_frequency_bins])
    plt.xlabel("Frequency (Hz)")
    plt.title(title)
    plt.show()

