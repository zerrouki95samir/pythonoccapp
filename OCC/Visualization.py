# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _Visualization.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_Visualization')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_Visualization')
    _Visualization = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Visualization', [dirname(__file__)])
        except ImportError:
            import _Visualization
            return _Visualization
        try:
            _mod = imp.load_module('_Visualization', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _Visualization = swig_import_helper()
    del swig_import_helper
else:
    import _Visualization
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _Visualization.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_Visualization.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_Visualization.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_Visualization.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_Visualization.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_Visualization.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_Visualization.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_Visualization.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_Visualization.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_Visualization.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_Visualization.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_Visualization.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_Visualization.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_Visualization.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_Visualization.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_Visualization.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_Visualization.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _Visualization.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class vector_float(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __iter__(self):
        return self.iterator()

    def __init__(self, *args):
        _Visualization.vector_float_swiginit(self, _Visualization.new_vector_float(*args))
    __swig_destroy__ = _Visualization.delete_vector_float
vector_float.iterator = new_instancemethod(_Visualization.vector_float_iterator, None, vector_float)
vector_float.__nonzero__ = new_instancemethod(_Visualization.vector_float___nonzero__, None, vector_float)
vector_float.__bool__ = new_instancemethod(_Visualization.vector_float___bool__, None, vector_float)
vector_float.__len__ = new_instancemethod(_Visualization.vector_float___len__, None, vector_float)
vector_float.__getslice__ = new_instancemethod(_Visualization.vector_float___getslice__, None, vector_float)
vector_float.__setslice__ = new_instancemethod(_Visualization.vector_float___setslice__, None, vector_float)
vector_float.__delslice__ = new_instancemethod(_Visualization.vector_float___delslice__, None, vector_float)
vector_float.__delitem__ = new_instancemethod(_Visualization.vector_float___delitem__, None, vector_float)
vector_float.__getitem__ = new_instancemethod(_Visualization.vector_float___getitem__, None, vector_float)
vector_float.__setitem__ = new_instancemethod(_Visualization.vector_float___setitem__, None, vector_float)
vector_float.pop = new_instancemethod(_Visualization.vector_float_pop, None, vector_float)
vector_float.append = new_instancemethod(_Visualization.vector_float_append, None, vector_float)
vector_float.empty = new_instancemethod(_Visualization.vector_float_empty, None, vector_float)
vector_float.size = new_instancemethod(_Visualization.vector_float_size, None, vector_float)
vector_float.swap = new_instancemethod(_Visualization.vector_float_swap, None, vector_float)
vector_float.begin = new_instancemethod(_Visualization.vector_float_begin, None, vector_float)
vector_float.end = new_instancemethod(_Visualization.vector_float_end, None, vector_float)
vector_float.rbegin = new_instancemethod(_Visualization.vector_float_rbegin, None, vector_float)
vector_float.rend = new_instancemethod(_Visualization.vector_float_rend, None, vector_float)
vector_float.clear = new_instancemethod(_Visualization.vector_float_clear, None, vector_float)
vector_float.get_allocator = new_instancemethod(_Visualization.vector_float_get_allocator, None, vector_float)
vector_float.pop_back = new_instancemethod(_Visualization.vector_float_pop_back, None, vector_float)
vector_float.erase = new_instancemethod(_Visualization.vector_float_erase, None, vector_float)
vector_float.push_back = new_instancemethod(_Visualization.vector_float_push_back, None, vector_float)
vector_float.front = new_instancemethod(_Visualization.vector_float_front, None, vector_float)
vector_float.back = new_instancemethod(_Visualization.vector_float_back, None, vector_float)
vector_float.assign = new_instancemethod(_Visualization.vector_float_assign, None, vector_float)
vector_float.resize = new_instancemethod(_Visualization.vector_float_resize, None, vector_float)
vector_float.insert = new_instancemethod(_Visualization.vector_float_insert, None, vector_float)
vector_float.reserve = new_instancemethod(_Visualization.vector_float_reserve, None, vector_float)
vector_float.capacity = new_instancemethod(_Visualization.vector_float_capacity, None, vector_float)
vector_float_swigregister = _Visualization.vector_float_swigregister
vector_float_swigregister(vector_float)

atCube = _Visualization.atCube
atNormal = _Visualization.atNormal
atNormalAutoScale = _Visualization.atNormalAutoScale
class Tesselator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(Tesselator self, TopoDS_Shape aShape, theTextureMappingRule aTxtMapType, float anAutoScaleSizeOnU, float anAutoScaleSizeOnV, float aDeviation, float aUOrigin, float aVOrigin, float aURepeat, float aVRepeat, float aScaleU, float aScaleV, float aRotationAngle) -> Tesselator
        __init__(Tesselator self, TopoDS_Shape aShape) -> Tesselator
        """
        _Visualization.Tesselator_swiginit(self, _Visualization.new_Tesselator(*args))
    __swig_destroy__ = _Visualization.delete_Tesselator

    def Compute(self, uv_coords: 'bool'=True, compute_edges: 'bool'=False, mesh_quality: 'float'=1.0, parallel: 'bool'=False) -> "void":
        """Compute(Tesselator self, bool uv_coords=True, bool compute_edges=False, float mesh_quality=1.0, bool parallel=False)"""
        return _Visualization.Tesselator_Compute(self, uv_coords, compute_edges, mesh_quality, parallel)


    def GetVertex(self, ivert: 'int') -> "void":
        """GetVertex(Tesselator self, int ivert)"""
        return _Visualization.Tesselator_GetVertex(self, ivert)


    def GetNormal(self, inorm: 'int') -> "void":
        """GetNormal(Tesselator self, int inorm)"""
        return _Visualization.Tesselator_GetNormal(self, inorm)


    def GetTriangleIndex(self, triangleIdx: 'int') -> "void":
        """GetTriangleIndex(Tesselator self, int triangleIdx)"""
        return _Visualization.Tesselator_GetTriangleIndex(self, triangleIdx)


    def GetEdgeVertex(self, iEdge: 'int', ivert: 'int') -> "void":
        """GetEdgeVertex(Tesselator self, int iEdge, int ivert)"""
        return _Visualization.Tesselator_GetEdgeVertex(self, iEdge, ivert)


    def VerticesList(self) -> "float *":
        """VerticesList(Tesselator self) -> float *"""
        return _Visualization.Tesselator_VerticesList(self)


    def ObjGetTriangleCount(self) -> "int":
        """ObjGetTriangleCount(Tesselator self) -> int"""
        return _Visualization.Tesselator_ObjGetTriangleCount(self)


    def ObjGetVertexCount(self) -> "int":
        """ObjGetVertexCount(Tesselator self) -> int"""
        return _Visualization.Tesselator_ObjGetVertexCount(self)


    def ObjGetNormalCount(self) -> "int":
        """ObjGetNormalCount(Tesselator self) -> int"""
        return _Visualization.Tesselator_ObjGetNormalCount(self)


    def ObjGetEdgeCount(self) -> "int":
        """ObjGetEdgeCount(Tesselator self) -> int"""
        return _Visualization.Tesselator_ObjGetEdgeCount(self)


    def ObjEdgeGetVertexCount(self, iEdge: 'int') -> "int":
        """ObjEdgeGetVertexCount(Tesselator self, int iEdge) -> int"""
        return _Visualization.Tesselator_ObjEdgeGetVertexCount(self, iEdge)


    def ExportShapeToX3DIndexedFaceSet(self) -> "std::string":
        """ExportShapeToX3DIndexedFaceSet(Tesselator self) -> std::string"""
        return _Visualization.Tesselator_ExportShapeToX3DIndexedFaceSet(self)


    def ExportShapeToThreejsJSONString(self, shape_function_name: 'char *', export_uv: 'bool'=False) -> "std::string":
        """
        ExportShapeToThreejsJSONString(Tesselator self, char * shape_function_name, bool export_uv=False) -> std::string
        ExportShapeToThreejsJSONString(Tesselator self, char * shape_function_name) -> std::string
        """
        return _Visualization.Tesselator_ExportShapeToThreejsJSONString(self, shape_function_name, export_uv)


    def ExportShapeToX3D(self, filename: 'char *', diffR: 'int'=1, diffG: 'int'=0, diffB: 'int'=0) -> "void":
        """ExportShapeToX3D(Tesselator self, char * filename, int diffR=1, int diffG=0, int diffB=0)"""
        return _Visualization.Tesselator_ExportShapeToX3D(self, filename, diffR, diffG, diffB)


    def GetVerticesPositionAsTuple(self) -> "std::vector< float,std::allocator< float > >":
        """GetVerticesPositionAsTuple(Tesselator self) -> vector_float"""
        return _Visualization.Tesselator_GetVerticesPositionAsTuple(self)


    def GetNormalsAsTuple(self) -> "std::vector< float,std::allocator< float > >":
        """GetNormalsAsTuple(Tesselator self) -> vector_float"""
        return _Visualization.Tesselator_GetNormalsAsTuple(self)

Tesselator.Compute = new_instancemethod(_Visualization.Tesselator_Compute, None, Tesselator)
Tesselator.GetVertex = new_instancemethod(_Visualization.Tesselator_GetVertex, None, Tesselator)
Tesselator.GetNormal = new_instancemethod(_Visualization.Tesselator_GetNormal, None, Tesselator)
Tesselator.GetTriangleIndex = new_instancemethod(_Visualization.Tesselator_GetTriangleIndex, None, Tesselator)
Tesselator.GetEdgeVertex = new_instancemethod(_Visualization.Tesselator_GetEdgeVertex, None, Tesselator)
Tesselator.VerticesList = new_instancemethod(_Visualization.Tesselator_VerticesList, None, Tesselator)
Tesselator.ObjGetTriangleCount = new_instancemethod(_Visualization.Tesselator_ObjGetTriangleCount, None, Tesselator)
Tesselator.ObjGetVertexCount = new_instancemethod(_Visualization.Tesselator_ObjGetVertexCount, None, Tesselator)
Tesselator.ObjGetNormalCount = new_instancemethod(_Visualization.Tesselator_ObjGetNormalCount, None, Tesselator)
Tesselator.ObjGetEdgeCount = new_instancemethod(_Visualization.Tesselator_ObjGetEdgeCount, None, Tesselator)
Tesselator.ObjEdgeGetVertexCount = new_instancemethod(_Visualization.Tesselator_ObjEdgeGetVertexCount, None, Tesselator)
Tesselator.ExportShapeToX3DIndexedFaceSet = new_instancemethod(_Visualization.Tesselator_ExportShapeToX3DIndexedFaceSet, None, Tesselator)
Tesselator.ExportShapeToThreejsJSONString = new_instancemethod(_Visualization.Tesselator_ExportShapeToThreejsJSONString, None, Tesselator)
Tesselator.ExportShapeToX3D = new_instancemethod(_Visualization.Tesselator_ExportShapeToX3D, None, Tesselator)
Tesselator.GetVerticesPositionAsTuple = new_instancemethod(_Visualization.Tesselator_GetVerticesPositionAsTuple, None, Tesselator)
Tesselator.GetNormalsAsTuple = new_instancemethod(_Visualization.Tesselator_GetNormalsAsTuple, None, Tesselator)
Tesselator_swigregister = _Visualization.Tesselator_swigregister
Tesselator_swigregister(Tesselator)

class Display3d(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self):
        """__init__(Display3d self) -> Display3d"""
        _Visualization.Display3d_swiginit(self, _Visualization.new_Display3d())
    __swig_destroy__ = _Visualization.delete_Display3d

    def Init(self, handle: 'long const') -> "void":
        """Init(Display3d self, long const handle)"""
        return _Visualization.Display3d_Init(self, handle)


    def SetAnaglyphMode(self, mode: 'int') -> "void":
        """SetAnaglyphMode(Display3d self, int mode)"""
        return _Visualization.Display3d_SetAnaglyphMode(self, mode)


    def ChangeRenderingParams(self, Method: 'int', RaytracingDepth: 'int', IsShadowEnabled: 'bool', IsReflectionEnabled: 'bool', IsAntialiasingEnabled: 'bool', IsTransparentShadowEnabled: 'bool', StereoMode: 'int', AnaglyphFilter: 'int', ToReverseStere: 'bool') -> "void":
        """ChangeRenderingParams(Display3d self, int Method, int RaytracingDepth, bool IsShadowEnabled, bool IsReflectionEnabled, bool IsAntialiasingEnabled, bool IsTransparentShadowEnabled, int StereoMode, int AnaglyphFilter, bool ToReverseStere)"""
        return _Visualization.Display3d_ChangeRenderingParams(self, Method, RaytracingDepth, IsShadowEnabled, IsReflectionEnabled, IsAntialiasingEnabled, IsTransparentShadowEnabled, StereoMode, AnaglyphFilter, ToReverseStere)


    def EnableVBO(self) -> "void":
        """EnableVBO(Display3d self)"""
        return _Visualization.Display3d_EnableVBO(self)


    def DisableVBO(self) -> "void":
        """DisableVBO(Display3d self)"""
        return _Visualization.Display3d_DisableVBO(self)


    def GetView(self) -> "Handle_V3d_View &":
        """GetView(Display3d self) -> Handle_V3d_View &"""
        return _Visualization.Display3d_GetView(self)


    def GetViewer(self) -> "Handle_V3d_Viewer &":
        """GetViewer(Display3d self) -> Handle_V3d_Viewer &"""
        return _Visualization.Display3d_GetViewer(self)


    def GetContext(self) -> "Handle_AIS_InteractiveContext":
        """GetContext(Display3d self) -> Handle_AIS_InteractiveContext"""
        return _Visualization.Display3d_GetContext(self)


    def Test(self) -> "void":
        """Test(Display3d self)"""
        return _Visualization.Display3d_Test(self)


    def InitOffscreen(self, size_x: 'int', size_y: 'int') -> "bool":
        """InitOffscreen(Display3d self, int size_x, int size_y) -> bool"""
        return _Visualization.Display3d_InitOffscreen(self, size_x, size_y)


    def SetSize(self, size_x: 'int', size_y: 'int') -> "bool":
        """SetSize(Display3d self, int size_x, int size_y) -> bool"""
        return _Visualization.Display3d_SetSize(self, size_x, size_y)


    def IsOffscreen(self) -> "bool":
        """IsOffscreen(Display3d self) -> bool"""
        return _Visualization.Display3d_IsOffscreen(self)


    def GetImageData(self, bufType: 'int'=0) -> "PyObject *":
        """
        GetImageData(Display3d self, int bufType=0) -> PyObject
        GetImageData(Display3d self) -> PyObject *
        """
        return _Visualization.Display3d_GetImageData(self, bufType)


    def GetSize(self) -> "PyObject *":
        """GetSize(Display3d self) -> PyObject *"""
        return _Visualization.Display3d_GetSize(self)

Display3d.Init = new_instancemethod(_Visualization.Display3d_Init, None, Display3d)
Display3d.SetAnaglyphMode = new_instancemethod(_Visualization.Display3d_SetAnaglyphMode, None, Display3d)
Display3d.ChangeRenderingParams = new_instancemethod(_Visualization.Display3d_ChangeRenderingParams, None, Display3d)
Display3d.EnableVBO = new_instancemethod(_Visualization.Display3d_EnableVBO, None, Display3d)
Display3d.DisableVBO = new_instancemethod(_Visualization.Display3d_DisableVBO, None, Display3d)
Display3d.GetView = new_instancemethod(_Visualization.Display3d_GetView, None, Display3d)
Display3d.GetViewer = new_instancemethod(_Visualization.Display3d_GetViewer, None, Display3d)
Display3d.GetContext = new_instancemethod(_Visualization.Display3d_GetContext, None, Display3d)
Display3d.Test = new_instancemethod(_Visualization.Display3d_Test, None, Display3d)
Display3d.InitOffscreen = new_instancemethod(_Visualization.Display3d_InitOffscreen, None, Display3d)
Display3d.SetSize = new_instancemethod(_Visualization.Display3d_SetSize, None, Display3d)
Display3d.IsOffscreen = new_instancemethod(_Visualization.Display3d_IsOffscreen, None, Display3d)
Display3d.GetImageData = new_instancemethod(_Visualization.Display3d_GetImageData, None, Display3d)
Display3d.GetSize = new_instancemethod(_Visualization.Display3d_GetSize, None, Display3d)
Display3d_swigregister = _Visualization.Display3d_swigregister
Display3d_swigregister(Display3d)


