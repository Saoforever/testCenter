from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/about")
def about():
    return "This is the about page."

@app.route("/upload", methods=["POST", "GET"])
def uploading_file():
    if request.method == "POST":
        uploading_file = request.files["my_file"]
        file_contents = uploading_file.read()
        return file_contents
        
    return """
        <form method="POST" action="/upload" enctype="multipart/form-data">
            <input type="file" name="my_file">
            <button type="submit">Upload File</button>
        </form>
    """

if __name__ == "__main__":
    app.run(debug=True) 