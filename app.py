import os
from flask import Flask, request, abort, jsonify, send_from_directory, make_response
#from stp2json import stp2json

UPLOAD_DIRECTORY = "./tmp"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello, in python-occ-libs</h1>'



@app.route("/files")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)


@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route("/files/<filename>", methods=["POST"])
def post_file(filename):
    """Upload a file."""

    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories directories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    response = stp2json.stp2json('{}/{}'.format(UPLOAD_DIRECTORY, filename))
    response = make_response(response)

    return response


if __name__ == "__main__":
    app.run(debug=True)
