from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    country = request.args.get('country')
    if country is None:
        return jsonify({'error': 'No country specified'})
    else:
        return jsonify({'message': 'Welcome to {}!'.format(country)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
