# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _Geom2dAdaptor.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_Geom2dAdaptor')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_Geom2dAdaptor')
    _Geom2dAdaptor = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Geom2dAdaptor', [dirname(__file__)])
        except ImportError:
            import _Geom2dAdaptor
            return _Geom2dAdaptor
        try:
            _mod = imp.load_module('_Geom2dAdaptor', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _Geom2dAdaptor = swig_import_helper()
    del swig_import_helper
else:
    import _Geom2dAdaptor
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
    __swig_destroy__ = _Geom2dAdaptor.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_Geom2dAdaptor.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_Geom2dAdaptor.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _Geom2dAdaptor.SwigPyIterator_swigregister
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

import OCC.Adaptor2d
import OCC.Standard
import OCC.GeomAbs
import OCC.TColStd
import OCC.TCollection
import OCC.MMgt
import OCC.gp
import OCC.Geom2d
import OCC.TColgp

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

class geom2dadaptor(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def MakeCurve(*args) -> "Handle_Geom2d_Curve":
        """
        * Inherited from GHCurve. Provides a curve handled by reference. Creates a 2d curve from a HCurve2d. This cannot process the OtherCurves.

        :param HC:
        :type HC: Adaptor2d_Curve2d &
        :rtype: Handle_Geom2d_Curve

        """
        return _Geom2dAdaptor.geom2dadaptor_MakeCurve(*args)

    MakeCurve = staticmethod(MakeCurve)

    __repr__ = _dumps_object


    def __init__(self):
        _Geom2dAdaptor.geom2dadaptor_swiginit(self, _Geom2dAdaptor.new_geom2dadaptor())
    __swig_destroy__ = _Geom2dAdaptor.delete_geom2dadaptor
geom2dadaptor_swigregister = _Geom2dAdaptor.geom2dadaptor_swigregister
geom2dadaptor_swigregister(geom2dadaptor)

def geom2dadaptor_MakeCurve(*args) -> "Handle_Geom2d_Curve":
    """
    * Inherited from GHCurve. Provides a curve handled by reference. Creates a 2d curve from a HCurve2d. This cannot process the OtherCurves.

    :param HC:
    :type HC: Adaptor2d_Curve2d &
    :rtype: Handle_Geom2d_Curve

    """
    return _Geom2dAdaptor.geom2dadaptor_MakeCurve(*args)

class Geom2dAdaptor_Curve(OCC.Adaptor2d.Adaptor2d_Curve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: Handle_Geom2d_Curve &
        :rtype: None

        * ConstructionError is raised if Ufirst>Ulast

        :param C:
        :type C: Handle_Geom2d_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        _Geom2dAdaptor.Geom2dAdaptor_Curve_swiginit(self, _Geom2dAdaptor.new_Geom2dAdaptor_Curve(*args))

    def Load(self, *args) -> "void":
        """
        :param C:
        :type C: Handle_Geom2d_Curve &
        :rtype: None

        * ConstructionError is raised if Ufirst>Ulast

        :param C:
        :type C: Handle_Geom2d_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        return _Geom2dAdaptor.Geom2dAdaptor_Curve_Load(self, *args)


    def Curve(self, *args) -> "Handle_Geom2d_Curve":
        """
        :rtype: Handle_Geom2d_Curve

        """
        return _Geom2dAdaptor.Geom2dAdaptor_Curve_Curve(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAdaptor.delete_Geom2dAdaptor_Curve
Geom2dAdaptor_Curve.Load = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_Curve_Load, None, Geom2dAdaptor_Curve)
Geom2dAdaptor_Curve.Curve = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_Curve_Curve, None, Geom2dAdaptor_Curve)
Geom2dAdaptor_Curve_swigregister = _Geom2dAdaptor.Geom2dAdaptor_Curve_swigregister
Geom2dAdaptor_Curve_swigregister(Geom2dAdaptor_Curve)

class Geom2dAdaptor_GHCurve(OCC.Adaptor2d.Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: Geom2dAdaptor_Curve &
        :rtype: None

        """
        _Geom2dAdaptor.Geom2dAdaptor_GHCurve_swiginit(self, _Geom2dAdaptor.new_Geom2dAdaptor_GHCurve(*args))

    def Set(self, *args) -> "void":
        """
        :param C:
        :type C: Geom2dAdaptor_Curve &
        :rtype: None

        """
        return _Geom2dAdaptor.Geom2dAdaptor_GHCurve_Set(self, *args)


    def ChangeCurve2d(self, *args) -> "Geom2dAdaptor_Curve &":
        """
        :rtype: Geom2dAdaptor_Curve

        """
        return _Geom2dAdaptor.Geom2dAdaptor_GHCurve_ChangeCurve2d(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_Geom2dAdaptor_GHCurve(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAdaptor.delete_Geom2dAdaptor_GHCurve
Geom2dAdaptor_GHCurve.Set = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_GHCurve_Set, None, Geom2dAdaptor_GHCurve)
Geom2dAdaptor_GHCurve.ChangeCurve2d = new_instancemethod(_Geom2dAdaptor.Geom2dAdaptor_GHCurve_ChangeCurve2d, None, Geom2dAdaptor_GHCurve)
Geom2dAdaptor_GHCurve_swigregister = _Geom2dAdaptor.Geom2dAdaptor_GHCurve_swigregister
Geom2dAdaptor_GHCurve_swigregister(Geom2dAdaptor_GHCurve)

class Handle_Geom2dAdaptor_GHCurve(OCC.Adaptor2d.Handle_Adaptor2d_HCurve2d):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_swiginit(self, _Geom2dAdaptor.new_Handle_Geom2dAdaptor_GHCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _Geom2dAdaptor.delete_Handle_Geom2dAdaptor_GHCurve
Handle_Geom2dAdaptor_GHCurve.Nullify = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_Nullify, None, Handle_Geom2dAdaptor_GHCurve)
Handle_Geom2dAdaptor_GHCurve.IsNull = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_IsNull, None, Handle_Geom2dAdaptor_GHCurve)
Handle_Geom2dAdaptor_GHCurve._get_reference = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve__get_reference, None, Handle_Geom2dAdaptor_GHCurve)
Handle_Geom2dAdaptor_GHCurve_swigregister = _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_swigregister
Handle_Geom2dAdaptor_GHCurve_swigregister(Handle_Geom2dAdaptor_GHCurve)

def Handle_Geom2dAdaptor_GHCurve_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_Geom2dAdaptor_GHCurve const":
    return _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_DownCast(AnObject)
Handle_Geom2dAdaptor_GHCurve_DownCast = _Geom2dAdaptor.Handle_Geom2dAdaptor_GHCurve_DownCast

class Geom2dAdaptor_HCurve(Geom2dAdaptor_GHCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param AS:
        :type AS: Geom2dAdaptor_Curve &
        :rtype: None

        :param S:
        :type S: Handle_Geom2d_Curve &
        :rtype: None

        * ConstructionError is raised if UFirst>ULast or VFirst>VLast

        :param S:
        :type S: Handle_Geom2d_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        _Geom2dAdaptor.Geom2dAdaptor_HCurve_swiginit(self, _Geom2dAdaptor.new_Geom2dAdaptor_HCurve(*args))

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_Geom2dAdaptor_HCurve(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _Geom2dAdaptor.delete_Geom2dAdaptor_HCurve
Geom2dAdaptor_HCurve_swigregister = _Geom2dAdaptor.Geom2dAdaptor_HCurve_swigregister
Geom2dAdaptor_HCurve_swigregister(Geom2dAdaptor_HCurve)

class Handle_Geom2dAdaptor_HCurve(Handle_Geom2dAdaptor_GHCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_swiginit(self, _Geom2dAdaptor.new_Handle_Geom2dAdaptor_HCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _Geom2dAdaptor.delete_Handle_Geom2dAdaptor_HCurve
Handle_Geom2dAdaptor_HCurve.Nullify = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_Nullify, None, Handle_Geom2dAdaptor_HCurve)
Handle_Geom2dAdaptor_HCurve.IsNull = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_IsNull, None, Handle_Geom2dAdaptor_HCurve)
Handle_Geom2dAdaptor_HCurve._get_reference = new_instancemethod(_Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve__get_reference, None, Handle_Geom2dAdaptor_HCurve)
Handle_Geom2dAdaptor_HCurve_swigregister = _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_swigregister
Handle_Geom2dAdaptor_HCurve_swigregister(Handle_Geom2dAdaptor_HCurve)

def Handle_Geom2dAdaptor_HCurve_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_Geom2dAdaptor_HCurve const":
    return _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_DownCast(AnObject)
Handle_Geom2dAdaptor_HCurve_DownCast = _Geom2dAdaptor.Handle_Geom2dAdaptor_HCurve_DownCast



