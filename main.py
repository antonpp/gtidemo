from flask import Flask, request, jsonify
app = Flask(__name__)

import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="gke-dja-demo", location="europe-west4")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 2048,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")

@app.route('/', methods=['GET'])
def index():
    country = request.args.get('country')
    if country is None:
        return jsonify({'error': 'No country specified'})
    else:
        response = model.predict(
            """Write me a 3 day trip itinerary for {}""".format(country),
            **parameters
        )
        return response.text
        return jsonify({'message': 'Welcome to {}!'.format(country)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
