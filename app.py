from flask import Flask, request, send_from_directory, render_template_string
import os

app = Flask(__name__)
SHARE_DIR = "/home/pi/shared"

@app.route('/')
def home():
    files = os.listdir(SHARE_DIR)
    file_list = "<br>".join(files)
    return render_template_string('''
    <h1>File Share</h1>
    <h2>Upload File</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    <h2>Shared Files</h2>
    <p>{{ files }}</p>
    <h2>Delete File</h2>
    <form action="/delete" method="post">
        <input type="text" name="filename" placeholder="Enter filename">
        <input type="submit" value="Delete">
    </form>
    ''', files=file_list)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    file.save(os.path.join(SHARE_DIR, file.filename))
    return "File uploaded successfully"

@app.route('/delete', methods=['POST'])
def delete_file():
    filename = request.form['filename']
    filepath = os.path.join(SHARE_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return "File deleted successfully"
    return "File not found"

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(SHARE_DIR, filename)

if __name__ == "__main__":
    if not os.path.exists(SHARE_DIR):
        os.makedirs(SHARE_DIR)
    app.run(host='0.0.0.0', port=5000)
