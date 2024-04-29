from flask import Flask, request, jsonify
import os

app = Flask(__name__)


# Endpoint to handle file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # You can perform further operations here, like processing the SQLite file

        return jsonify({'message': 'File uploaded successfully', 'file_path': file_path})

    return jsonify({'error': 'Unknown error'})


if __name__ == '__main__':
    app.run(debug=True)
