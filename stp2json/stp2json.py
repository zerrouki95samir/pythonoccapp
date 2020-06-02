from OCC.STEPControl import STEPControl_Reader
from OCC.IFSelect import IFSelect_RetDone, IFSelect_ItemsByEntity
from OCC.Visualization import Tesselator
import os
import io


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
   






