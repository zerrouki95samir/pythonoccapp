# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _IGESControl.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_IGESControl')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_IGESControl')
    _IGESControl = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_IGESControl', [dirname(__file__)])
        except ImportError:
            import _IGESControl
            return _IGESControl
        try:
            _mod = imp.load_module('_IGESControl', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _IGESControl = swig_import_helper()
    del swig_import_helper
else:
    import _IGESControl
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
    __swig_destroy__ = _IGESControl.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_IGESControl.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_IGESControl.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_IGESControl.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_IGESControl.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_IGESControl.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_IGESControl.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_IGESControl.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_IGESControl.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_IGESControl.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_IGESControl.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_IGESControl.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_IGESControl.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_IGESControl.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_IGESControl.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_IGESControl.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_IGESControl.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _IGESControl.SwigPyIterator_swigregister
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

import OCC.Standard
import OCC.XSControl
import OCC.IFSelect
import OCC.MMgt
import OCC.TCollection
import OCC.TColStd
import OCC.Interface
import OCC.Message
import OCC.Dico
import OCC.TopoDS
import OCC.TopLoc
import OCC.gp
import OCC.TopAbs
import OCC.TopTools

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

class IGESControl_ActorWrite(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        """
        _IGESControl.IGESControl_ActorWrite_swiginit(self, _IGESControl.new_IGESControl_ActorWrite(*args))

    def Recognize(self, *args) -> "Standard_Boolean":
        """
        * Recognizes a ShapeMapper

        :param start:
        :type start: Handle_Transfer_Finder &
        :rtype: bool

        """
        return _IGESControl.IGESControl_ActorWrite_Recognize(self, *args)


    def Transfer(self, *args) -> "Handle_Transfer_Binder":
        """
        * Transfers Shape to IGES Entities //! ModeTrans may be : 0 -> groups of Faces or 1 -> BRep

        :param start:
        :type start: Handle_Transfer_Finder &
        :param FP:
        :type FP: Handle_Transfer_FinderProcess &
        :rtype: Handle_Transfer_Binder

        """
        return _IGESControl.IGESControl_ActorWrite_Transfer(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_IGESControl_ActorWrite(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _IGESControl.delete_IGESControl_ActorWrite
IGESControl_ActorWrite.Recognize = new_instancemethod(_IGESControl.IGESControl_ActorWrite_Recognize, None, IGESControl_ActorWrite)
IGESControl_ActorWrite.Transfer = new_instancemethod(_IGESControl.IGESControl_ActorWrite_Transfer, None, IGESControl_ActorWrite)
IGESControl_ActorWrite_swigregister = _IGESControl.IGESControl_ActorWrite_swigregister
IGESControl_ActorWrite_swigregister(IGESControl_ActorWrite)

class Handle_IGESControl_ActorWrite(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _IGESControl.Handle_IGESControl_ActorWrite_swiginit(self, _IGESControl.new_Handle_IGESControl_ActorWrite(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_IGESControl.Handle_IGESControl_ActorWrite_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _IGESControl.delete_Handle_IGESControl_ActorWrite
Handle_IGESControl_ActorWrite.Nullify = new_instancemethod(_IGESControl.Handle_IGESControl_ActorWrite_Nullify, None, Handle_IGESControl_ActorWrite)
Handle_IGESControl_ActorWrite.IsNull = new_instancemethod(_IGESControl.Handle_IGESControl_ActorWrite_IsNull, None, Handle_IGESControl_ActorWrite)
Handle_IGESControl_ActorWrite._get_reference = new_instancemethod(_IGESControl.Handle_IGESControl_ActorWrite__get_reference, None, Handle_IGESControl_ActorWrite)
Handle_IGESControl_ActorWrite_swigregister = _IGESControl.Handle_IGESControl_ActorWrite_swigregister
Handle_IGESControl_ActorWrite_swigregister(Handle_IGESControl_ActorWrite)

def Handle_IGESControl_ActorWrite_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_IGESControl_ActorWrite const":
    return _IGESControl.Handle_IGESControl_ActorWrite_DownCast(AnObject)
Handle_IGESControl_ActorWrite_DownCast = _IGESControl.Handle_IGESControl_ActorWrite_DownCast

class IGESControl_AlgoContainer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _IGESControl.IGESControl_AlgoContainer_swiginit(self, _IGESControl.new_IGESControl_AlgoContainer(*args))

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_IGESControl_AlgoContainer(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _IGESControl.delete_IGESControl_AlgoContainer
IGESControl_AlgoContainer_swigregister = _IGESControl.IGESControl_AlgoContainer_swigregister
IGESControl_AlgoContainer_swigregister(IGESControl_AlgoContainer)

class Handle_IGESControl_AlgoContainer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _IGESControl.Handle_IGESControl_AlgoContainer_swiginit(self, _IGESControl.new_Handle_IGESControl_AlgoContainer(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_IGESControl.Handle_IGESControl_AlgoContainer_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _IGESControl.delete_Handle_IGESControl_AlgoContainer
Handle_IGESControl_AlgoContainer.Nullify = new_instancemethod(_IGESControl.Handle_IGESControl_AlgoContainer_Nullify, None, Handle_IGESControl_AlgoContainer)
Handle_IGESControl_AlgoContainer.IsNull = new_instancemethod(_IGESControl.Handle_IGESControl_AlgoContainer_IsNull, None, Handle_IGESControl_AlgoContainer)
Handle_IGESControl_AlgoContainer._get_reference = new_instancemethod(_IGESControl.Handle_IGESControl_AlgoContainer__get_reference, None, Handle_IGESControl_AlgoContainer)
Handle_IGESControl_AlgoContainer_swigregister = _IGESControl.Handle_IGESControl_AlgoContainer_swigregister
Handle_IGESControl_AlgoContainer_swigregister(Handle_IGESControl_AlgoContainer)

def Handle_IGESControl_AlgoContainer_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_IGESControl_AlgoContainer const":
    return _IGESControl.Handle_IGESControl_AlgoContainer_DownCast(AnObject)
Handle_IGESControl_AlgoContainer_DownCast = _IGESControl.Handle_IGESControl_AlgoContainer_DownCast

class IGESControl_Controller(OCC.XSControl.XSControl_Controller):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Initializes the use of IGES Norm (the first time) and returns a Controller for IGES-5.1 If <modefnes> is True, sets it to internal FNES format

        :param modefnes: default value is Standard_False
        :type modefnes: bool
        :rtype: None

        """
        _IGESControl.IGESControl_Controller_swiginit(self, _IGESControl.new_IGESControl_Controller(*args))

    def Init(*args) -> "Standard_Boolean":
        """
        * Standard Initialisation. It creates a Controller for IGES and records it to various names, available to select it later Returns True when done, False if could not be done Also, it creates and records an Adaptor for FNES

        :rtype: bool

        """
        return _IGESControl.IGESControl_Controller_Init(*args)

    Init = staticmethod(Init)

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_IGESControl_Controller(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _IGESControl.delete_IGESControl_Controller
IGESControl_Controller_swigregister = _IGESControl.IGESControl_Controller_swigregister
IGESControl_Controller_swigregister(IGESControl_Controller)

def IGESControl_Controller_Init(*args) -> "Standard_Boolean":
    """
    * Standard Initialisation. It creates a Controller for IGES and records it to various names, available to select it later Returns True when done, False if could not be done Also, it creates and records an Adaptor for FNES

    :rtype: bool

    """
    return _IGESControl.IGESControl_Controller_Init(*args)

class Handle_IGESControl_Controller(OCC.XSControl.Handle_XSControl_Controller):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _IGESControl.Handle_IGESControl_Controller_swiginit(self, _IGESControl.new_Handle_IGESControl_Controller(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_IGESControl.Handle_IGESControl_Controller_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _IGESControl.delete_Handle_IGESControl_Controller
Handle_IGESControl_Controller.Nullify = new_instancemethod(_IGESControl.Handle_IGESControl_Controller_Nullify, None, Handle_IGESControl_Controller)
Handle_IGESControl_Controller.IsNull = new_instancemethod(_IGESControl.Handle_IGESControl_Controller_IsNull, None, Handle_IGESControl_Controller)
Handle_IGESControl_Controller._get_reference = new_instancemethod(_IGESControl.Handle_IGESControl_Controller__get_reference, None, Handle_IGESControl_Controller)
Handle_IGESControl_Controller_swigregister = _IGESControl.Handle_IGESControl_Controller_swigregister
Handle_IGESControl_Controller_swigregister(Handle_IGESControl_Controller)

def Handle_IGESControl_Controller_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_IGESControl_Controller const":
    return _IGESControl.Handle_IGESControl_Controller_DownCast(AnObject)
Handle_IGESControl_Controller_DownCast = _IGESControl.Handle_IGESControl_Controller_DownCast

class IGESControl_IGESBoundary(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates an object and calls inherited constuctor.

        :rtype: None

        * Creates an object and calls inherited constuctor.

        :param CS:
        :type CS: IGESToBRep_CurveAndSurface &
        :rtype: None

        """
        _IGESControl.IGESControl_IGESBoundary_swiginit(self, _IGESControl.new_IGESControl_IGESBoundary(*args))

    def Check(self, *args) -> "void":
        """
        * Checks result of translation of IGES boundary entities (types 141, 142 or 508). Checks consistency of 2D and 3D representations and keeps only one if they are inconsistent. Checks the closure of resulting wire and if it is not closed, checks 2D and 3D representation and updates the resulting wire to contain only closed representation.

        :param result:
        :type result: bool
        :param checkclosure:
        :type checkclosure: bool
        :param okCurve3d:
        :type okCurve3d: bool
        :param okCurve2d:
        :type okCurve2d: bool
        :rtype: void

        """
        return _IGESControl.IGESControl_IGESBoundary_Check(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_IGESControl_IGESBoundary(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _IGESControl.delete_IGESControl_IGESBoundary
IGESControl_IGESBoundary.Check = new_instancemethod(_IGESControl.IGESControl_IGESBoundary_Check, None, IGESControl_IGESBoundary)
IGESControl_IGESBoundary_swigregister = _IGESControl.IGESControl_IGESBoundary_swigregister
IGESControl_IGESBoundary_swigregister(IGESControl_IGESBoundary)

class Handle_IGESControl_IGESBoundary(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _IGESControl.Handle_IGESControl_IGESBoundary_swiginit(self, _IGESControl.new_Handle_IGESControl_IGESBoundary(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_IGESControl.Handle_IGESControl_IGESBoundary_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _IGESControl.delete_Handle_IGESControl_IGESBoundary
Handle_IGESControl_IGESBoundary.Nullify = new_instancemethod(_IGESControl.Handle_IGESControl_IGESBoundary_Nullify, None, Handle_IGESControl_IGESBoundary)
Handle_IGESControl_IGESBoundary.IsNull = new_instancemethod(_IGESControl.Handle_IGESControl_IGESBoundary_IsNull, None, Handle_IGESControl_IGESBoundary)
Handle_IGESControl_IGESBoundary._get_reference = new_instancemethod(_IGESControl.Handle_IGESControl_IGESBoundary__get_reference, None, Handle_IGESControl_IGESBoundary)
Handle_IGESControl_IGESBoundary_swigregister = _IGESControl.Handle_IGESControl_IGESBoundary_swigregister
Handle_IGESControl_IGESBoundary_swigregister(Handle_IGESControl_IGESBoundary)

def Handle_IGESControl_IGESBoundary_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_IGESControl_IGESBoundary const":
    return _IGESControl.Handle_IGESControl_IGESBoundary_DownCast(AnObject)
Handle_IGESControl_IGESBoundary_DownCast = _IGESControl.Handle_IGESControl_IGESBoundary_DownCast

class IGESControl_Reader(OCC.XSControl.XSControl_Reader):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates a Reader from scratch

        :rtype: None

        * Creates a Reader from an already existing Session

        :param WS:
        :type WS: Handle_XSControl_WorkSession &
        :param scratch: default value is Standard_True
        :type scratch: bool
        :rtype: None

        """
        _IGESControl.IGESControl_Reader_swiginit(self, _IGESControl.new_IGESControl_Reader(*args))

    def SetReadVisible(self, *args) -> "void":
        """
        * Set the transion of ALL Roots (if theReadOnlyVisible is False) or of Visible Roots (if theReadOnlyVisible is True)

        :param ReadRoot:
        :type ReadRoot: bool
        :rtype: None

        """
        return _IGESControl.IGESControl_Reader_SetReadVisible(self, *args)


    def GetReadVisible(self, *args) -> "Standard_Boolean":
        """
        :rtype: bool

        """
        return _IGESControl.IGESControl_Reader_GetReadVisible(self, *args)


    def IGESModel(self, *args) -> "Handle_IGESData_IGESModel":
        """
        * Returns the model as a IGESModel. It can then be consulted (header, product)

        :rtype: Handle_IGESData_IGESModel

        """
        return _IGESControl.IGESControl_Reader_IGESModel(self, *args)


    def PrintTransferInfo(self, *args) -> "void":
        """
        * Prints Statistics and check list for Transfer

        :param failwarn:
        :type failwarn: IFSelect_PrintFail
        :param mode:
        :type mode: IFSelect_PrintCount
        :rtype: None

        """
        return _IGESControl.IGESControl_Reader_PrintTransferInfo(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _IGESControl.delete_IGESControl_Reader
IGESControl_Reader.SetReadVisible = new_instancemethod(_IGESControl.IGESControl_Reader_SetReadVisible, None, IGESControl_Reader)
IGESControl_Reader.GetReadVisible = new_instancemethod(_IGESControl.IGESControl_Reader_GetReadVisible, None, IGESControl_Reader)
IGESControl_Reader.IGESModel = new_instancemethod(_IGESControl.IGESControl_Reader_IGESModel, None, IGESControl_Reader)
IGESControl_Reader.PrintTransferInfo = new_instancemethod(_IGESControl.IGESControl_Reader_PrintTransferInfo, None, IGESControl_Reader)
IGESControl_Reader_swigregister = _IGESControl.IGESControl_Reader_swigregister
IGESControl_Reader_swigregister(IGESControl_Reader)

class IGESControl_ToolContainer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _IGESControl.IGESControl_ToolContainer_swiginit(self, _IGESControl.new_IGESControl_ToolContainer(*args))

    def IGESBoundary(self, *args) -> "Handle_IGESToBRep_IGESBoundary":
        """
        * Returns IGESControl_IGESBoundary

        :rtype: Handle_IGESToBRep_IGESBoundary

        """
        return _IGESControl.IGESControl_ToolContainer_IGESBoundary(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_IGESControl_ToolContainer(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _IGESControl.delete_IGESControl_ToolContainer
IGESControl_ToolContainer.IGESBoundary = new_instancemethod(_IGESControl.IGESControl_ToolContainer_IGESBoundary, None, IGESControl_ToolContainer)
IGESControl_ToolContainer_swigregister = _IGESControl.IGESControl_ToolContainer_swigregister
IGESControl_ToolContainer_swigregister(IGESControl_ToolContainer)

class Handle_IGESControl_ToolContainer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _IGESControl.Handle_IGESControl_ToolContainer_swiginit(self, _IGESControl.new_Handle_IGESControl_ToolContainer(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_IGESControl.Handle_IGESControl_ToolContainer_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _IGESControl.delete_Handle_IGESControl_ToolContainer
Handle_IGESControl_ToolContainer.Nullify = new_instancemethod(_IGESControl.Handle_IGESControl_ToolContainer_Nullify, None, Handle_IGESControl_ToolContainer)
Handle_IGESControl_ToolContainer.IsNull = new_instancemethod(_IGESControl.Handle_IGESControl_ToolContainer_IsNull, None, Handle_IGESControl_ToolContainer)
Handle_IGESControl_ToolContainer._get_reference = new_instancemethod(_IGESControl.Handle_IGESControl_ToolContainer__get_reference, None, Handle_IGESControl_ToolContainer)
Handle_IGESControl_ToolContainer_swigregister = _IGESControl.Handle_IGESControl_ToolContainer_swigregister
Handle_IGESControl_ToolContainer_swigregister(Handle_IGESControl_ToolContainer)

def Handle_IGESControl_ToolContainer_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_IGESControl_ToolContainer const":
    return _IGESControl.Handle_IGESControl_ToolContainer_DownCast(AnObject)
Handle_IGESControl_ToolContainer_DownCast = _IGESControl.Handle_IGESControl_ToolContainer_DownCast

class IGESControl_Writer(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Creates a writer object with the default unit (millimeters) and write mode (Face). IGESControl_Writer (const Standard_CString unit, const Standard_Integer modecr = 0);

        :rtype: None

        * Creates a writer with given values for units and for write mode. unit may be any unit that is accepted by the IGES standard. By default, it is the millimeter. modecr defines the write mode and may be: - 0: Faces (default) - 1: BRep.

        :param unit:
        :type unit: char *
        :param modecr: default value is 0
        :type modecr: int
        :rtype: None

        * Creates a writer object with the prepared IGES model model in write mode. modecr defines the write mode and may be: - 0: Faces (default) - 1: BRep.

        :param model:
        :type model: Handle_IGESData_IGESModel &
        :param modecr: default value is 0
        :type modecr: int
        :rtype: None

        """
        _IGESControl.IGESControl_Writer_swiginit(self, _IGESControl.new_IGESControl_Writer(*args))

    def Model(self, *args) -> "Handle_IGESData_IGESModel":
        """
        * Returns the IGES model to be written in output.

        :rtype: Handle_IGESData_IGESModel

        """
        return _IGESControl.IGESControl_Writer_Model(self, *args)


    def TransferProcess(self, *args) -> "Handle_Transfer_FinderProcess":
        """
        :rtype: Handle_Transfer_FinderProcess

        """
        return _IGESControl.IGESControl_Writer_TransferProcess(self, *args)


    def SetTransferProcess(self, *args) -> "void":
        """
        * Returns/Sets the TransferProcess : it contains final results and if some, check messages

        :param TP:
        :type TP: Handle_Transfer_FinderProcess &
        :rtype: None

        """
        return _IGESControl.IGESControl_Writer_SetTransferProcess(self, *args)


    def AddShape(self, *args) -> "Standard_Boolean":
        """
        * Translates a Shape to IGES Entities and adds them to the model Returns True if done, False if Shape not suitable for IGES or null

        :param sh:
        :type sh: TopoDS_Shape &
        :rtype: bool

        """
        return _IGESControl.IGESControl_Writer_AddShape(self, *args)


    def AddGeom(self, *args) -> "Standard_Boolean":
        """
        * Translates a Geometry (Surface or Curve) to IGES Entities and adds them to the model Returns True if done, False if geom is neither a Surface or a Curve suitable for IGES or is null

        :param geom:
        :type geom: Handle_Standard_Transient &
        :rtype: bool

        """
        return _IGESControl.IGESControl_Writer_AddGeom(self, *args)


    def AddEntity(self, *args) -> "Standard_Boolean":
        """
        * Adds an IGES entity (and the ones it references) to the model

        :param ent:
        :type ent: Handle_IGESData_IGESEntity &
        :rtype: bool

        """
        return _IGESControl.IGESControl_Writer_AddEntity(self, *args)


    def ComputeModel(self, *args) -> "void":
        """
        * Computes the entities found in the model, which is ready to be written. This contrasts with the default computation of headers only.

        :rtype: None

        """
        return _IGESControl.IGESControl_Writer_ComputeModel(self, *args)


    def Write(self, *args) -> "Standard_Boolean":
        """
        * Computes then writes the model to an OStream Returns True when done, false in case of error

        :param S:
        :type S: Standard_OStream &
        :param fnes: default value is Standard_False
        :type fnes: bool
        :rtype: bool

        * Prepares and writes an IGES model either to an OStream, S or to a file name,CString. Returns True if the operation was performed correctly and False if an error occurred (for instance, if the processor could not create the file).

        :param file:
        :type file: char *
        :param fnes: default value is Standard_False
        :type fnes: bool
        :rtype: bool

        """
        return _IGESControl.IGESControl_Writer_Write(self, *args)


    def PrintStatsTransfer(self, *args) -> "void":
        """
        * Prints Statistics about Transfer

        :param what:
        :type what: int
        :param mode: default value is 0
        :type mode: int
        :rtype: None

        """
        return _IGESControl.IGESControl_Writer_PrintStatsTransfer(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _IGESControl.delete_IGESControl_Writer
IGESControl_Writer.Model = new_instancemethod(_IGESControl.IGESControl_Writer_Model, None, IGESControl_Writer)
IGESControl_Writer.TransferProcess = new_instancemethod(_IGESControl.IGESControl_Writer_TransferProcess, None, IGESControl_Writer)
IGESControl_Writer.SetTransferProcess = new_instancemethod(_IGESControl.IGESControl_Writer_SetTransferProcess, None, IGESControl_Writer)
IGESControl_Writer.AddShape = new_instancemethod(_IGESControl.IGESControl_Writer_AddShape, None, IGESControl_Writer)
IGESControl_Writer.AddGeom = new_instancemethod(_IGESControl.IGESControl_Writer_AddGeom, None, IGESControl_Writer)
IGESControl_Writer.AddEntity = new_instancemethod(_IGESControl.IGESControl_Writer_AddEntity, None, IGESControl_Writer)
IGESControl_Writer.ComputeModel = new_instancemethod(_IGESControl.IGESControl_Writer_ComputeModel, None, IGESControl_Writer)
IGESControl_Writer.Write = new_instancemethod(_IGESControl.IGESControl_Writer_Write, None, IGESControl_Writer)
IGESControl_Writer.PrintStatsTransfer = new_instancemethod(_IGESControl.IGESControl_Writer_PrintStatsTransfer, None, IGESControl_Writer)
IGESControl_Writer_swigregister = _IGESControl.IGESControl_Writer_swigregister
IGESControl_Writer_swigregister(IGESControl_Writer)



