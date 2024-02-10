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

@app.route('/detectar')
def detect():
    user_ip = request.remote_addr
    return jsonify(FAKE_DATA)

if __name__ == "__main__":
    app.run(port=8080, debug=True)