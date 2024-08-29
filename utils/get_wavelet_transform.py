import pywt
from matplotlib import pyplot as plt
import numpy as np

def get_wavelet_transform(data):
    wavelet = 'morl' # wavelet type: morlet
    sr = 8000 # sampling frequency: 8KHz
    widths = np.arange(1, 64) # scales for morlet wavelet 
    print("These are the scales that we are using: ", widths)
    dt = 1/sr # timestep difference

    frequencies = pywt.scale2frequency(wavelet, widths) / dt # Get frequencies corresponding to scales
    print("These are the frequencies that re associated with the scales: ", frequencies)

    # Compute continuous wavelet transform of the audio numpy array
    wavelet_coeffs, freqs = pywt.cwt(data, widths, wavelet = wavelet, sampling_period=dt)
    print("Shape of wavelet transform: ", wavelet_coeffs.shape)

    # Display the scalogram. We will display a small part of scalogram because the length of scalogram is too big.
    plt.imshow(wavelet_coeffs[:,:400], cmap='coolwarm')
    plt.xlabel("Time")
    plt.ylabel("Scales")
    plt.yticks(widths[0::11])
    plt.title("Scalogram")
    plt.show()