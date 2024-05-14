from flask import Flask, request, jsonify
import base64
import numpy as np
# import PyWavelets

from scipy.fft import fft, fftfreq
from matplotlib import pyplot as plt

from utils.constants import FAKE_DATA
from utils.load_audio import load_audio

app = Flask(__name__)

@app.route('/detectar',  methods=['POST', 'GET'])
def detect():
    if request.method == 'POST':
        body = request.get_json()
        decoded_audio_data = body['audio_data']

        ## Convertir audio de base 64 a vector unidimensional
        decode_string = base64.b64decode(decoded_audio_data)
        wav_file = open("temp.wav", "wb")
        wav_file.write(decode_string)

        file_name = "./Audio de prueba.wav"
        header_chunk_id , header_chunk_size, header_chunk_format, format_chunk_id, format_chunk_size, audio_data, format_code, channels, sample_width, sample_rate, byte_rate, block_align, data_chunk_id, data_chunk_size = load_audio(file_name)

        number_of_samples = len(audio_data)

        print("HEADER CHUNK :----- \n")
        print(f"Header Chunk ID : {header_chunk_id}")
        print(f"Header Chunk Size : {header_chunk_size}")
        print(f"Header Chunk Format : {header_chunk_format}")
        print("FORMAT CHUNK :----- \n")
        print(f"Format Chunk ID : {format_chunk_id}")
        print(f"Format Chunk Size : {format_chunk_size}")
        print(f"Format Code: {format_code}")
        print(f"Number of Channels: {channels}")
        print(f"Sample Rate: {sample_rate}")
        print(f"Byte Rate : {byte_rate}")
        print(f"Block align : {block_align}")
        print(f"Sample Width: {sample_width}")
        print(f"Number of Samples: {len(audio_data)}")
        print("DATA CHUNK :----- \n")
        print(f"Data Chunk ID : {data_chunk_id}")
        print(f"Data Size : {data_chunk_size}")
        print(f"Data : {audio_data}")
        print(f"Type of data array : {type(audio_data[0])}")  
        
        ## Muestrear la señal 

        ## Realizar transformada de Wavelet, Gabor, Fourier y verificar cómo obtener los rasgos cracterísticos de la voz

        # Number of samples in normalized_tone

        yf = fft(audio_data)
        print(f"Fourier transform: {yf}")
        xf = fftfreq(number_of_samples, 1 / sample_rate)

        # plt.plot(xf, np.abs(yf))
        # plt.show()
        ## Extraer parámetros característicos de la voz

        ## Supervised Learning

        ## Evaluación de modelos: cross validation, matriz de confusión, k-nearest neighbors
        
        return jsonify({ "audio_data": decoded_audio_data, "results": FAKE_DATA})
    else:
        return jsonify(FAKE_DATA)

if __name__ == "__main__":
    app.run(port=8080, debug=True)