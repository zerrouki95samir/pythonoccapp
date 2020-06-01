from flask import Flask, render_template, make_response, request
from OCC.STEPControl import STEPControl_Reader
from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
from OCC.Visualization import Tesselator
import os
import io


app = Flask(__name__)


def stp2json(filePath, file_name=''):

    def _load_model_file(filePath):
        step_reader = STEPControl_Reader()
        status = step_reader.ReadFile(filePath)

        if status == IFSelect_RetDone:  # check status
            failsonly = False
            step_reader.PrintCheckLoad(failsonly, IFSelect_ItemsByEntity)
            step_reader.PrintCheckTransfer(failsonly, IFSelect_ItemsByEntity)

            ok = step_reader.TransferRoot(1)
            _nbs = step_reader.NbShapes()
            
            _shape = step_reader.Shape(1)
            return _shape
        else:
            raise Exception("Error: can't read file - Method: _load_STEP_file")

    def _exportThreeJS(filePath, _shape):   
        _tess = Tesselator(_shape)
        _tess.Compute(uv_coords=False, compute_edges=False, mesh_quality=50)

        json_shape = _tess.ExportShapeToThreejsJSONString(filePath)
        
        json_shape = json_shape.replace("data\\", "data/")
        json_shape = json_shape.replace("\\step_postprocessed\\", "/step_postprocessed/")
        
        return json_shape

    _shape = _load_model_file(filePath)
    json_shape = _exportThreeJS(filePath, _shape)

    return json_shape




@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hrv_results', methods=["POST"])
def transform_view():
    file = request.files['data_file']
    file_name = os.path.splitext(file.filename)[0]

    if not file:
        return "No file"

    file.save(os.path.join('tmp', file.filename))
    
    #stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    results = stp2json('./tmp/'+file.filename, file_name)
    # Sending POST requests to our Cloud Function (/hrv_results)
    # And get the result as json object
    #cf_url = 'https://us-central1-esense-20ba5.cloudfunctions.net/hrv_results'
    #r = requests.post(cf_url, json=data)
    #results = {}
    #if r.status_code == 200:
        #results = r.json()

    response = make_response(results)
    #response.headers["Content-Disposition"] = "attachment; filename=result.json"
    return response


@app.route('/rr_interval_ms', methods=["GET"])
def rr_interval_ms():
    response = make_response(rri_serie)
    return response


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
    app.run(debug=True)




