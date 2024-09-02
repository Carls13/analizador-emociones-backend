from flask import Flask, request, jsonify
import base64
import pywt
import pickle

from utils.constants import FAKE_DATA
from utils.load_audio import load_audio
from utils.plot_spectrum import plot_magnitude_spectrum
from utils.get_wavelet_transform import get_wavelet_transform
from sklearn.preprocessing import OneHotEncoder
from utils.mfcc import extract_mfcc
from tensorflow.keras.models import load_model
import numpy as np
import pandas as pd

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

        file_name = "./temp.wav"
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

        mfcc_data = { 'speech': file_name }
        df = pd.DataFrame(data=mfcc_data, index=[0])
        x_mfcc = df['speech'].apply(lambda x: extract_mfcc(x))
        X= [x for x in x_mfcc]
        X = np.array(X)
        X = np.expand_dims(X, -1)
        print(X, X.shape)

        model = load_model('model.h5')

        # evaluate model 
        pred_test = model.predict(X)

        print(pred_test[0], 'HERE')

        df = pd.read_csv('data.csv')

        enc = OneHotEncoder()
        enc.fit_transform(df[['label']])

        y_pred = enc.inverse_transform(pred_test)

        prediction = y_pred[0]

        print('The predicition is ', prediction[0])

        return jsonify({ "prediction": prediction[0] })
    else:
        return jsonify(FAKE_DATA)

if __name__ == "__main__":
    app.run(port=8080, debug=True)