# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _BRepAlgoAPI.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_BRepAlgoAPI')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_BRepAlgoAPI')
    _BRepAlgoAPI = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_BRepAlgoAPI', [dirname(__file__)])
        except ImportError:
            import _BRepAlgoAPI
            return _BRepAlgoAPI
        try:
            _mod = imp.load_module('_BRepAlgoAPI', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _BRepAlgoAPI = swig_import_helper()
    del swig_import_helper
else:
    import _BRepAlgoAPI
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
    __swig_destroy__ = _BRepAlgoAPI.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_BRepAlgoAPI.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_BRepAlgoAPI.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_BRepAlgoAPI.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_BRepAlgoAPI.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_BRepAlgoAPI.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_BRepAlgoAPI.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_BRepAlgoAPI.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_BRepAlgoAPI.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _BRepAlgoAPI.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


def _dumps_object(klass):
    """ Improve string output for any oce object.
    By default, __repr__ method returns something like:
    <OCC.TopoDS.TopoDS_Shape; proxy of <Swig Object of type 'TopoDS_Shape *' at 0x02BB0758> >
    This is too much verbose.
    We prefer :
    class<'gp_Pnt'>
    or
    class<'TopoDS_Shape'; Type:Solid; Id:59391729>
    """
    klass_name = str(klass.__class__).split(".")[2].split("'")[0]
    repr_string = "class<'" + klass_name + "'"
# for TopoDS_Shape, we also look for the base type
    if klass_name == "TopoDS_Shape":
        st = klass.ShapeType()
        types = {OCC.TopAbs.TopAbs_VERTEX:"Vertex",
                 OCC.TopAbs.TopAbs_SOLID:"Solid",
                 OCC.TopAbs.TopAbs_EDGE:"Edge",
                 OCC.TopAbs.TopAbs_FACE:"Face",
                 OCC.TopAbs.TopAbs_SHELL:"Shell",
                 OCC.TopAbs.TopAbs_WIRE:"Wire",
                 OCC.TopAbs.TopAbs_COMPOUND:"Compound",
                 OCC.TopAbs.TopAbs_COMPSOLID:"Compsolid."}
        repr_string += "; Type:%s" % types[st]        
# for each class that has an HashCode method define,
# print the id
    if hasattr(klass, "HashCode"):
        klass_id = hash(klass)
        repr_string += "; id:%s" % klass_id
    repr_string += ">"
    return repr_string

import OCC.TopoDS
import OCC.MMgt
import OCC.Standard
import OCC.TCollection
import OCC.TopLoc
import OCC.gp
import OCC.TopAbs
import OCC.BOPAlgo
import OCC.BOPCol
import OCC.Bnd
import OCC.TColStd
import OCC.Message
import OCC.BOPDS
import OCC.IntTools
import OCC.Geom
import OCC.GeomAbs
import OCC.TColgp
import OCC.BRepAdaptor
import OCC.Adaptor3d
import OCC.Adaptor2d
import OCC.Geom2d
import OCC.math
import OCC.GeomAdaptor
import OCC.Geom2dAdaptor
import OCC.GeomAPI
import OCC.Quantity
import OCC.Extrema
import OCC.Approx
import OCC.AppCont
import OCC.AppParCurves
import OCC.BRepClass3d
import OCC.IntCurveSurface
import OCC.Intf
import OCC.IntSurf
import OCC.IntCurvesFace
import OCC.Geom2dHatch
import OCC.IntRes2d
import OCC.HatchGen
import OCC.Geom2dInt
import OCC.IntCurve
import OCC.NCollection
import OCC.TopTools
import OCC.BOPTools
import OCC.ProjLib
import OCC.BRepBuilderAPI
import OCC.BRepTools
import OCC.BRep
import OCC.Poly
import OCC.TShort

def register_handle(handle, base_object):
    """
    Inserts the handle into the base object to
    prevent memory corruption in certain cases
    """
    try:
        if base_object.IsKind("Standard_Transient"):
            base_object.thisHandle = handle
            base_object.thisown = False
    except:
        pass

class brepalgoapi(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def DumpOper(*args) -> "void":
        """
        * Check shapes on validity for boolean operation. Dump arguments and result of boolean operation in the file specified by path.

        :param theFilePath:
        :type theFilePath: char *
        :param theShape1:
        :type theShape1: TopoDS_Shape &
        :param theShape2:
        :type theShape2: TopoDS_Shape &
        :param theResult:
        :type theResult: TopoDS_Shape &
        :param theOperation:
        :type theOperation: BOPAlgo_Operation
        :param isNonValidArgs:
        :type isNonValidArgs: bool
        :rtype: void

        """
        return _BRepAlgoAPI.brepalgoapi_DumpOper(*args)

    DumpOper = staticmethod(DumpOper)

    __repr__ = _dumps_object


    def __init__(self):
        _BRepAlgoAPI.brepalgoapi_swiginit(self, _BRepAlgoAPI.new_brepalgoapi())
    __swig_destroy__ = _BRepAlgoAPI.delete_brepalgoapi
brepalgoapi_swigregister = _BRepAlgoAPI.brepalgoapi_swigregister
brepalgoapi_swigregister(brepalgoapi)

def brepalgoapi_DumpOper(*args) -> "void":
    """
    * Check shapes on validity for boolean operation. Dump arguments and result of boolean operation in the file specified by path.

    :param theFilePath:
    :type theFilePath: char *
    :param theShape1:
    :type theShape1: TopoDS_Shape &
    :param theShape2:
    :type theShape2: TopoDS_Shape &
    :param theResult:
    :type theResult: TopoDS_Shape &
    :param theOperation:
    :type theOperation: BOPAlgo_Operation
    :param isNonValidArgs:
    :type isNonValidArgs: bool
    :rtype: void

    """
    return _BRepAlgoAPI.brepalgoapi_DumpOper(*args)

class BRepAlgoAPI_BooleanOperation(OCC.BRepBuilderAPI.BRepBuilderAPI_MakeShape):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def SetOperation(self, *args) -> "void":
        """
        * Sets the type of Boolean operation to perform It can be BOPAlgo_SECTION BOPAlgo_COMMON BOPAlgo_FUSE BOPAlgo_CUT BOPAlgo_CUT21

        :param anOp:
        :type anOp: BOPAlgo_Operation
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_SetOperation(self, *args)


    def Shape1(self, *args) -> "TopoDS_Shape const":
        """
        * Returns the first shape involved in this Boolean operation.

        :rtype: TopoDS_Shape

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Shape1(self, *args)


    def Shape2(self, *args) -> "TopoDS_Shape const":
        """
        * Returns the second shape involved in this Boolean operation.

        :rtype: TopoDS_Shape

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Shape2(self, *args)


    def Operation(self, *args) -> "BOPAlgo_Operation":
        """
        * Returns the type of Boolean Operation that has been performed.

        :rtype: BOPAlgo_Operation

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Operation(self, *args)


    def FuseEdges(self, *args) -> "Standard_Boolean":
        """
        * Returns the flag of edge refining

        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_FuseEdges(self, *args)


    def RefineEdges(self, *args) -> "void":
        """
        * Fuse C1 edges

        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_RefineEdges(self, *args)


    def BuilderCanWork(self, *args) -> "Standard_Boolean":
        """
        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_BuilderCanWork(self, *args)


    def ErrorStatus(self, *args) -> "Standard_Integer":
        """
        * Returns the error status of operation. 0 - Ok 1 - The Object is created but Nothing is Done 2 - Null source shapes is not allowed 3 - Check types of the arguments 4 - Can not allocate memory for the DSFiller 5 - The Builder can not work with such types of arguments 6 - Unknown operation is not allowed 7 - Can not allocate memory for the Builder > 100 - See the Builder's ErrorStatus

        :rtype: int

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_ErrorStatus(self, *args)


    def HasModified(self, *args) -> "Standard_Boolean":
        """
        * Returns true if there is at least one modified shape. For use in BRepNaming.

        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_HasModified(self, *args)


    def HasGenerated(self, *args) -> "Standard_Boolean":
        """
        * Returns true if there is at least one generated shape. For use in BRepNaming.

        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_HasGenerated(self, *args)


    def HasDeleted(self, *args) -> "Standard_Boolean":
        """
        * Returns true if there is at least one deleted shape. For use in BRepNaming.

        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_HasDeleted(self, *args)


    def Destroy(self, *args) -> "void":
        """
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Destroy(self, *args)


    def SectionEdges(self, *args) -> "TopTools_ListOfShape const &":
        """
        * Returns a list of section edges. The edges represent the result of intersection between arguments of Boolean Operation. They are computed during operation execution.

        :rtype: TopTools_ListOfShape

        """
        return _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_SectionEdges(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAlgoAPI.delete_BRepAlgoAPI_BooleanOperation
BRepAlgoAPI_BooleanOperation.SetOperation = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_SetOperation, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.Shape1 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Shape1, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.Shape2 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Shape2, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.Operation = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Operation, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.FuseEdges = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_FuseEdges, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.RefineEdges = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_RefineEdges, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.BuilderCanWork = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_BuilderCanWork, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.ErrorStatus = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_ErrorStatus, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.HasModified = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_HasModified, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.HasGenerated = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_HasGenerated, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.HasDeleted = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_HasDeleted, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.Destroy = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_Destroy, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation.SectionEdges = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_SectionEdges, None, BRepAlgoAPI_BooleanOperation)
BRepAlgoAPI_BooleanOperation_swigregister = _BRepAlgoAPI.BRepAlgoAPI_BooleanOperation_swigregister
BRepAlgoAPI_BooleanOperation_swigregister(BRepAlgoAPI_BooleanOperation)

class BRepAlgoAPI_Check(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor.

        :rtype: None

        * Constructor for checking single shape. It calls methods Init(theS, TopoDS_Shape(), BOPAlgo_UNKNOWN, bTestSE, bTestSI) and Perform(). Params: theS - the shape that should be checked; bTestSE - flag that specifies whether check on small edges should be performed; by default it is set to True; bTestSI - flag that specifies whether check on self-interference should be performed; by default it is set to True;

        :param theS:
        :type theS: TopoDS_Shape &
        :param bTestSE: default value is Standard_True
        :type bTestSE: bool
        :param bTestSI: default value is Standard_True
        :type bTestSI: bool
        :rtype: None

        * Constructor for couple of shapes. It calls methods Init(theS1, theS2, theOp, bTestSE, bTestSI) and Perform(). Params: theS1, theS2 - the initial shapes. theOp - the type of Boolean Operation; if it is not defined (set to UNKNOWN) for each shape performed check as for single shape. bTestSE - flag that specifies whether check on small edges should be performed; by default it is set to True; bTestSI - flag that specifies whether check on self-interference should be performed; by default it is set to True;

        :param theS1:
        :type theS1: TopoDS_Shape &
        :param theS2:
        :type theS2: TopoDS_Shape &
        :param theOp: default value is BOPAlgo_UNKNOWN
        :type theOp: BOPAlgo_Operation
        :param bTestSE: default value is Standard_True
        :type bTestSE: bool
        :param bTestSI: default value is Standard_True
        :type bTestSI: bool
        :rtype: None

        """
        _BRepAlgoAPI.BRepAlgoAPI_Check_swiginit(self, _BRepAlgoAPI.new_BRepAlgoAPI_Check(*args))

    def SetData(self, *args) -> "void":
        """
        * Sets data for check by Init method. The method provides alternative way for checking single shape.

        :param theS:
        :type theS: TopoDS_Shape &
        :param bTestSE: default value is Standard_True
        :type bTestSE: bool
        :param bTestSI: default value is Standard_True
        :type bTestSI: bool
        :rtype: None

        * Sets data for check by Init method. The method provides alternative way for checking couple of shapes.

        :param theS1:
        :type theS1: TopoDS_Shape &
        :param theS2:
        :type theS2: TopoDS_Shape &
        :param theOp: default value is BOPAlgo_UNKNOWN
        :type theOp: BOPAlgo_Operation
        :param bTestSE: default value is Standard_True
        :type bTestSE: bool
        :param bTestSI: default value is Standard_True
        :type bTestSI: bool
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Check_SetData(self, *args)


    def Perform(self, *args) -> "void":
        """
        * Performs the check.

        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Check_Perform(self, *args)


    def IsValid(self, *args) -> "Standard_Boolean":
        """
        * Shows whether shape(s) valid or not.

        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Check_IsValid(self, *args)


    def Result(self, *args) -> "BOPAlgo_ListOfCheckResult const &":
        """
        * Returns faulty shapes.

        :rtype: BOPAlgo_ListOfCheckResult

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Check_Result(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAlgoAPI.delete_BRepAlgoAPI_Check
BRepAlgoAPI_Check.SetData = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Check_SetData, None, BRepAlgoAPI_Check)
BRepAlgoAPI_Check.Perform = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Check_Perform, None, BRepAlgoAPI_Check)
BRepAlgoAPI_Check.IsValid = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Check_IsValid, None, BRepAlgoAPI_Check)
BRepAlgoAPI_Check.Result = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Check_Result, None, BRepAlgoAPI_Check)
BRepAlgoAPI_Check_swigregister = _BRepAlgoAPI.BRepAlgoAPI_Check_swigregister
BRepAlgoAPI_Check_swigregister(BRepAlgoAPI_Check)

class BRepAlgoAPI_Common(BRepAlgoAPI_BooleanOperation):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Constructs a common part for shapes aS1 and aS2 .

        :param S1:
        :type S1: TopoDS_Shape &
        :param S2:
        :type S2: TopoDS_Shape &
        :rtype: None

        :param S1:
        :type S1: TopoDS_Shape &
        :param S2:
        :type S2: TopoDS_Shape &
        :param aDSF:
        :type aDSF: BOPAlgo_PaveFiller &
        :rtype: None

        """
        _BRepAlgoAPI.BRepAlgoAPI_Common_swiginit(self, _BRepAlgoAPI.new_BRepAlgoAPI_Common(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAlgoAPI.delete_BRepAlgoAPI_Common
BRepAlgoAPI_Common_swigregister = _BRepAlgoAPI.BRepAlgoAPI_Common_swigregister
BRepAlgoAPI_Common_swigregister(BRepAlgoAPI_Common)

class BRepAlgoAPI_Cut(BRepAlgoAPI_BooleanOperation):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Shape aS2 cuts shape aS1. The resulting shape is a new shape produced by the cut operation.

        :param S1:
        :type S1: TopoDS_Shape &
        :param S2:
        :type S2: TopoDS_Shape &
        :rtype: None

        * Constructs a new shape cut from shape aS1 by shape aS2 using aDSFiller (see BRepAlgoAPI_BooleanOperation Constructor).

        :param S1:
        :type S1: TopoDS_Shape &
        :param S2:
        :type S2: TopoDS_Shape &
        :param aDSF:
        :type aDSF: BOPAlgo_PaveFiller &
        :param bFWD: default value is Standard_True
        :type bFWD: bool
        :rtype: None

        """
        _BRepAlgoAPI.BRepAlgoAPI_Cut_swiginit(self, _BRepAlgoAPI.new_BRepAlgoAPI_Cut(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAlgoAPI.delete_BRepAlgoAPI_Cut
BRepAlgoAPI_Cut_swigregister = _BRepAlgoAPI.BRepAlgoAPI_Cut_swigregister
BRepAlgoAPI_Cut_swigregister(BRepAlgoAPI_Cut)

class BRepAlgoAPI_Fuse(BRepAlgoAPI_BooleanOperation):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Constructs a fuse of shapes aS1 and aS2.

        :param S1:
        :type S1: TopoDS_Shape &
        :param S2:
        :type S2: TopoDS_Shape &
        :rtype: None

        * Constructs a new shape that is a fuse of shapes aS1 and aS2 using aDSFiller.

        :param S1:
        :type S1: TopoDS_Shape &
        :param S2:
        :type S2: TopoDS_Shape &
        :param aDSF:
        :type aDSF: BOPAlgo_PaveFiller &
        :rtype: None

        """
        _BRepAlgoAPI.BRepAlgoAPI_Fuse_swiginit(self, _BRepAlgoAPI.new_BRepAlgoAPI_Fuse(*args))

    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAlgoAPI.delete_BRepAlgoAPI_Fuse
BRepAlgoAPI_Fuse_swigregister = _BRepAlgoAPI.BRepAlgoAPI_Fuse_swigregister
BRepAlgoAPI_Fuse_swigregister(BRepAlgoAPI_Fuse)

class BRepAlgoAPI_Section(BRepAlgoAPI_BooleanOperation):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :param S1:
        :type S1: TopoDS_Shape &
        :param S2:
        :type S2: TopoDS_Shape &
        :param aDSF:
        :type aDSF: BOPAlgo_PaveFiller &
        :param PerformNow: default value is Standard_True
        :type PerformNow: bool
        :rtype: None

        * see upper

        :param Sh1:
        :type Sh1: TopoDS_Shape &
        :param Sh2:
        :type Sh2: TopoDS_Shape &
        :param PerformNow: default value is Standard_True
        :type PerformNow: bool
        :rtype: None

        * see upper

        :param Sh:
        :type Sh: TopoDS_Shape &
        :param Pl:
        :type Pl: gp_Pln
        :param PerformNow: default value is Standard_True
        :type PerformNow: bool
        :rtype: None

        * see upper

        :param Sh:
        :type Sh: TopoDS_Shape &
        :param Sf:
        :type Sf: Handle_Geom_Surface &
        :param PerformNow: default value is Standard_True
        :type PerformNow: bool
        :rtype: None

        * see upper

        :param Sf:
        :type Sf: Handle_Geom_Surface &
        :param Sh:
        :type Sh: TopoDS_Shape &
        :param PerformNow: default value is Standard_True
        :type PerformNow: bool
        :rtype: None

        * This and the above classes construct a framework for computing the section lines of: - two shapes Sh1 and Sh2, or - shape Sh and plane Pl, or - shape Sh and surface Sf, or - surface Sf and shape Sh, or - two surfaces Sf1 and Sf2, and builds a result if PerformNow equals true, its default value. If PerformNow equals false, the intersection will be computed later by the function Build. The constructed shape will be returned by the function Shape. This is a compound object composed of edges. These intersection edges may be built: - on new intersection lines, or - on coincident portions of edges in the two intersected shapes. These intersection edges are independent: they are not chained or grouped in wires. If no intersection edge exists, the result is an empty compound object. Note that other objects than TopoDS_Shape shapes involved in these syntaxes are converted into faces or shells before performing the computation of the intersection. A shape resulting from this conversion can be retrieved with the function Shape1 or Shape2. Parametric 2D curves on intersection edges No parametric 2D curve (pcurve) is defined for each elementary edge of the result. To attach such parametric curves to the constructed edges you may use a constructor with the PerformNow flag equal to false; then you use: - the function ComputePCurveOn1 to ask for the additional computation of a pcurve in the parametric space of the first shape, - the function ComputePCurveOn2 to ask for the additional computation of a pcurve in the parametric space of the second shape, in the end, - the function Build to construct the result. Approximation of intersection edges The underlying 3D geometry attached to each elementary edge of the result is: - analytic where possible, provided the corresponding geometry corresponds to a type of analytic curve defined in the Geom package; for example, the intersection of a cylindrical shape with a plane gives an ellipse or a circle; - or elsewhere, given as a succession of points grouped together in a BSpline curve of degree 1. If you prefer to have an attached 3D geometry which is a BSpline approximation of the computed set of points on computed elementary intersection edges whose underlying geometry is not analytic, you may use a constructor with the PerformNow flag equal to false. Then you use: - the function Approximation to ask for this computation option, and - the function Build to construct the result. - Note that as a result, approximations will only be computed on edges built on new intersection lines. - Example You may also combine these computation options. In the following example: - each elementary edge of the computed intersection, built on a new intersection line, which does not correspond to an analytic Geom curve, will be approximated by a BSpline curve whose degree is not greater than 8. - each elementary edge built on a new intersection line, will have: - a pcurve in the parametric space of the intersected face of shape S1, - no pcurve in the parametric space of the intersected face of shape S2. // TopoDS_Shape S1 = ... , S2 = ... ; Standard_Boolean PerformNow = Standard_False; BRepAlgoAPI_Section S ( S1, S2, PerformNow ); S.ComputePCurveOn1 (Standard_True); S.Approximation (Standard_True); S.Build(); TopoDS_Shape R = S.Shape();

        :param Sf1:
        :type Sf1: Handle_Geom_Surface &
        :param Sf2:
        :type Sf2: Handle_Geom_Surface &
        :param PerformNow: default value is Standard_True
        :type PerformNow: bool
        :rtype: None

        """
        _BRepAlgoAPI.BRepAlgoAPI_Section_swiginit(self, _BRepAlgoAPI.new_BRepAlgoAPI_Section(*args))

    def Init1(self, *args) -> "void":
        """
        * initialize first part

        :param S1:
        :type S1: TopoDS_Shape &
        :rtype: None

        * initialize first part

        :param Pl:
        :type Pl: gp_Pln
        :rtype: None

        * initialize first part

        :param Sf:
        :type Sf: Handle_Geom_Surface &
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Section_Init1(self, *args)


    def Init2(self, *args) -> "void":
        """
        * initialize second part

        :param S2:
        :type S2: TopoDS_Shape &
        :rtype: None

        * initialize second part

        :param Pl:
        :type Pl: gp_Pln
        :rtype: None

        * Reinitializes the first and the second parts on which this algorithm is going to perform the intersection computation. This is done with either: the surface Sf, the plane Pl or the shape Sh. You use the function Build to construct the result.

        :param Sf:
        :type Sf: Handle_Geom_Surface &
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Section_Init2(self, *args)


    def Approximation(self, *args) -> "void":
        """
        * Defines an option for computation of further intersections. This computation will be performed by the function Build in this framework. By default, the underlying 3D geometry attached to each elementary edge of the result of a computed intersection is: - analytic where possible, provided the corresponding geometry corresponds to a type of analytic curve defined in the Geom package; for example the intersection of a cylindrical shape with a plane gives an ellipse or a circle; - or elsewhere, given as a succession of points grouped together in a BSpline curve of degree 1. If Approx equals true, when further computations are performed in this framework with the function Build, these edges will have an attached 3D geometry which is a BSpline approximation of the computed set of points. Note that as a result, approximations will be computed on edges built only on new intersection lines.

        :param B:
        :type B: bool
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Section_Approximation(self, *args)


    def ComputePCurveOn1(self, *args) -> "void":
        """
        * Indicates if the Pcurve must be (or not) performed on first part.

        :param B:
        :type B: bool
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Section_ComputePCurveOn1(self, *args)


    def ComputePCurveOn2(self, *args) -> "void":
        """
        * Define options for the computation of further intersections, which will be performed by the function Build in this framework. By default, no parametric 2D curve (pcurve) is defined for the elementary edges of the result. If ComputePCurve1 equals true, further computations performed in this framework with the function Build will attach an additional pcurve in the parametric space of the first shape to the constructed edges. If ComputePCurve2 equals true, the additional pcurve will be attached to the constructed edges in the parametric space of the second shape. These two functions may be used together.

        :param B:
        :type B: bool
        :rtype: None

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Section_ComputePCurveOn2(self, *args)


    def HasAncestorFaceOn1(self, *args) -> "Standard_Boolean":
        """
        * get the face of the first part giving section edge <E>. Returns True on the 3 following conditions : 1/ <E> is an edge returned by the Shape() method. 2/ First part of section performed is a shape. 3/ <E> is built on a intersection curve (i.e <E> is not the result of common edges) When False, F remains untouched.

        :param E:
        :type E: TopoDS_Shape &
        :param F:
        :type F: TopoDS_Shape &
        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Section_HasAncestorFaceOn1(self, *args)


    def HasAncestorFaceOn2(self, *args) -> "Standard_Boolean":
        """
        * Identifies the ancestor faces of the intersection edge E resulting from the last computation performed in this framework, that is, the faces of the two original shapes on which the edge E lies: - HasAncestorFaceOn1 gives the ancestor face in the first shape, and - HasAncestorFaceOn2 gives the ancestor face in the second shape. These functions return true if an ancestor face F is found, or false if not. An ancestor face is identifiable for the edge E if the following conditions are satisfied: - the first part on which this algorithm performed its last computation is a shape, that is, it was not given as a surface or a plane at the time of construction of this algorithm or at a later time by the Init1 function, - E is one of the elementary edges built by the last computation of this section algorithm. To use these functions properly, you have to test the returned Boolean value before using the ancestor face: F is significant only if the returned Boolean value equals true.

        :param E:
        :type E: TopoDS_Shape &
        :param F:
        :type F: TopoDS_Shape &
        :rtype: bool

        """
        return _BRepAlgoAPI.BRepAlgoAPI_Section_HasAncestorFaceOn2(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _BRepAlgoAPI.delete_BRepAlgoAPI_Section
BRepAlgoAPI_Section.Init1 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Section_Init1, None, BRepAlgoAPI_Section)
BRepAlgoAPI_Section.Init2 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Section_Init2, None, BRepAlgoAPI_Section)
BRepAlgoAPI_Section.Approximation = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Section_Approximation, None, BRepAlgoAPI_Section)
BRepAlgoAPI_Section.ComputePCurveOn1 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Section_ComputePCurveOn1, None, BRepAlgoAPI_Section)
BRepAlgoAPI_Section.ComputePCurveOn2 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Section_ComputePCurveOn2, None, BRepAlgoAPI_Section)
BRepAlgoAPI_Section.HasAncestorFaceOn1 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Section_HasAncestorFaceOn1, None, BRepAlgoAPI_Section)
BRepAlgoAPI_Section.HasAncestorFaceOn2 = new_instancemethod(_BRepAlgoAPI.BRepAlgoAPI_Section_HasAncestorFaceOn2, None, BRepAlgoAPI_Section)
BRepAlgoAPI_Section_swigregister = _BRepAlgoAPI.BRepAlgoAPI_Section_swigregister
BRepAlgoAPI_Section_swigregister(BRepAlgoAPI_Section)



