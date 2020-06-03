# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _IntStart.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_IntStart')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_IntStart')
    _IntStart = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_IntStart', [dirname(__file__)])
        except ImportError:
            import _IntStart
            return _IntStart
        try:
            _mod = imp.load_module('_IntStart', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _IntStart = swig_import_helper()
    del swig_import_helper
else:
    import _IntStart
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
    __swig_destroy__ = _IntStart.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_IntStart.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_IntStart.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_IntStart.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_IntStart.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_IntStart.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_IntStart.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_IntStart.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_IntStart.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_IntStart.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_IntStart.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_IntStart.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_IntStart.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_IntStart.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_IntStart.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_IntStart.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_IntStart.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _IntStart.SwigPyIterator_swigregister
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

import OCC.MMgt
import OCC.Standard
import OCC.gp
import OCC.TopAbs

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

class IntStart_SITopolTool(OCC.MMgt.MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr

    def Classify(self, *args) -> "TopAbs_State":
        """
        :param P:
        :type P: gp_Pnt2d
        :param Tol:
        :type Tol: float
        :rtype: TopAbs_State

        """
        return _IntStart.IntStart_SITopolTool_Classify(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_IntStart_SITopolTool(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _IntStart.delete_IntStart_SITopolTool
IntStart_SITopolTool.Classify = new_instancemethod(_IntStart.IntStart_SITopolTool_Classify, None, IntStart_SITopolTool)
IntStart_SITopolTool_swigregister = _IntStart.IntStart_SITopolTool_swigregister
IntStart_SITopolTool_swigregister(IntStart_SITopolTool)

class Handle_IntStart_SITopolTool(OCC.MMgt.Handle_MMgt_TShared):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _IntStart.Handle_IntStart_SITopolTool_swiginit(self, _IntStart.new_Handle_IntStart_SITopolTool(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_IntStart.Handle_IntStart_SITopolTool_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _IntStart.delete_Handle_IntStart_SITopolTool
Handle_IntStart_SITopolTool.Nullify = new_instancemethod(_IntStart.Handle_IntStart_SITopolTool_Nullify, None, Handle_IntStart_SITopolTool)
Handle_IntStart_SITopolTool.IsNull = new_instancemethod(_IntStart.Handle_IntStart_SITopolTool_IsNull, None, Handle_IntStart_SITopolTool)
Handle_IntStart_SITopolTool._get_reference = new_instancemethod(_IntStart.Handle_IntStart_SITopolTool__get_reference, None, Handle_IntStart_SITopolTool)
Handle_IntStart_SITopolTool_swigregister = _IntStart.Handle_IntStart_SITopolTool_swigregister
Handle_IntStart_SITopolTool_swigregister(Handle_IntStart_SITopolTool)

def Handle_IntStart_SITopolTool_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_IntStart_SITopolTool const":
    return _IntStart.Handle_IntStart_SITopolTool_DownCast(AnObject)
Handle_IntStart_SITopolTool_DownCast = _IntStart.Handle_IntStart_SITopolTool_DownCast



