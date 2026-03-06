from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/util', methods=['GET'])
def get_util():
    return jsonify({'message': 'Welcome to Util Expert!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
