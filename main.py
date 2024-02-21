from flask import Flask, request, jsonify

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

@app.route('/detectar',  methods=['POST', 'GET'])
def detect():
    if request.method == 'POST':
        body = request.get_json()
        audio_data = body['audio_data']

        ## Analizar audio y obtener resultados 
        
        return jsonify({ "audio_data": audio_data, "results": FAKE_DATA})
    else:
        return jsonify(FAKE_DATA)

if __name__ == "__main__":
    app.run(port=8080, debug=True)