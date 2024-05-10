from flask import Flask, request, jsonify
import base64
import struct
import numpy as np
# import PyWavelets

from scipy.fft import fft, fftfreq
from matplotlib import pyplot as plt

app = Flask(__name__)

FAKE_DATA = {
    "components": [
        {
            "name": "fundamental_frequency",
            "results": [
                {
                    "emotion": "anger",
                    "percentage": "80"
                },
                {
                    "emotion": "sadness",
                    "percentage": "85"
                },
                {
                    "emotion": "fear",
                    "percentage": "92"
                }
            ]
        },
        {
            "name": "first_formant",
            "results": [
                {
                    "emotion": "anger",
                    "percentage": "80"
                },
                {
                    "emotion": "sadness",
                    "percentage": "85"
                },
                {
                    "emotion": "fear",
                    "percentage": "92"
                }
            ]
        },
        {
            "name": "second_formant",
            "results": [
                {
                    "emotion": "anger",
                    "percentage": "80"
                },
                {
                    "emotion": "sadness",
                    "percentage": "85"
                },
                {
                    "emotion": "fear",
                    "percentage": "92"
                }
            ]
        },
        {
            "name": "third_formant",
            "results": [
                {
                    "emotion": "anger",
                    "percentage": "80"
                },
                {
                    "emotion": "sadness",
                    "percentage": "85"
                },
                {
                    "emotion": "fear",
                    "percentage": "92"
                }
            ]
        },
    ]
}

def load_audio(file_path):
    with open(file_path,'rb') as audio_file:
        # Getting the audio file parameters
        # Read the header to get audio file information
        
        header = audio_file.read(44) # In WAV files, first 44 bytes are reserved for the header
        print(f"The header is {header}")
        
        if header[:4] != b'RIFF' or header[8:12] != b'WAVE' or header[12:16] != b'fmt ':
            raise ValueError("Invalid WAV file")
            
        # Extract relevant information from the header
        header_chunk_id = struct.unpack('4s', header[0:4])[0]
        header_chunk_size = struct.unpack('<I', header[4:8])[0]
        header_chunk_format = struct.unpack('4s', header[8:12])[0]
        format_chunk_id = struct.unpack('4s', header[12:16])[0]
        format_chunk_size = struct.unpack('<I', header[16:20])[0]
        format_code = struct.unpack('<H', header[20:22])[0]
        channels = struct.unpack('<H', header[22:24])[0]
        sample_rate = struct.unpack('<I', header[24:28])[0]
        byte_rate = struct.unpack('<I', header[28:32])[0]
        block_align = struct.unpack('<H', header[32:34])[0]
        sample_width = struct.unpack('<H', header[34:36])[0]
        data_chunk_id = struct.unpack('4s', header[36:40])[0]
        data_chunk_size = struct.unpack('<I', header[40:44])[0]
        
        # Read the data from the file
        audio_file.seek(44);
        data = audio_file.read(data_chunk_size)
    
    # Converting the raw binary data to a list of integers : 
    data_array = np.frombuffer(data, dtype=np.uint16)
    # Convert to float32
    data_array = data_array.astype(np.float32)
    
    return header_chunk_id, header_chunk_size, header_chunk_format, format_chunk_id, format_chunk_size, data_array, format_code, channels, sample_width, sample_rate, byte_rate, block_align, data_chunk_id, data_chunk_size

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

        plt.plot(xf, np.abs(yf))
        plt.show()
        ## Extraer parámetros característicos de la voz

        ## Supervised Learning

        ## Evaluación de modelos: cross validation, matriz de confusión, k-nearest neighbors
        
        return jsonify({ "audio_data": decoded_audio_data, "results": FAKE_DATA})
    else:
        return jsonify(FAKE_DATA)

if __name__ == "__main__":
    app.run(port=8080, debug=True)