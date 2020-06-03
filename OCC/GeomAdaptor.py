# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _GeomAdaptor.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_GeomAdaptor')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_GeomAdaptor')
    _GeomAdaptor = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_GeomAdaptor', [dirname(__file__)])
        except ImportError:
            import _GeomAdaptor
            return _GeomAdaptor
        try:
            _mod = imp.load_module('_GeomAdaptor', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _GeomAdaptor = swig_import_helper()
    del swig_import_helper
else:
    import _GeomAdaptor
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
    __swig_destroy__ = _GeomAdaptor.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_GeomAdaptor.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_GeomAdaptor.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_GeomAdaptor.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_GeomAdaptor.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_GeomAdaptor.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_GeomAdaptor.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_GeomAdaptor.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_GeomAdaptor.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_GeomAdaptor.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_GeomAdaptor.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_GeomAdaptor.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_GeomAdaptor.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_GeomAdaptor.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_GeomAdaptor.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_GeomAdaptor.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_GeomAdaptor.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _GeomAdaptor.SwigPyIterator_swigregister
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

import OCC.Adaptor3d
import OCC.Standard
import OCC.GeomAbs
import OCC.TColStd
import OCC.TCollection
import OCC.MMgt
import OCC.gp
import OCC.Geom
import OCC.TColgp
import OCC.Adaptor2d
import OCC.Geom2d
import OCC.TopAbs
import OCC.math

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

class geomadaptor(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def MakeCurve(*args) -> "Handle_Geom_Curve":
        """
        * Inherited from GHCurve. Provides a curve handled by reference. Build a Geom_Curve using the informations from the Curve from Adaptor3d

        :param C:
        :type C: Adaptor3d_Curve &
        :rtype: Handle_Geom_Curve

        """
        return _GeomAdaptor.geomadaptor_MakeCurve(*args)

    MakeCurve = staticmethod(MakeCurve)

    def MakeSurface(*args) -> "Handle_Geom_Surface":
        """
        * Build a Geom_Surface using the informations from the Surface from Adaptor3d

        :param S:
        :type S: Adaptor3d_Surface &
        :rtype: Handle_Geom_Surface

        """
        return _GeomAdaptor.geomadaptor_MakeSurface(*args)

    MakeSurface = staticmethod(MakeSurface)

    __repr__ = _dumps_object


    def __init__(self):
        _GeomAdaptor.geomadaptor_swiginit(self, _GeomAdaptor.new_geomadaptor())
    __swig_destroy__ = _GeomAdaptor.delete_geomadaptor
geomadaptor_swigregister = _GeomAdaptor.geomadaptor_swigregister
geomadaptor_swigregister(geomadaptor)

def geomadaptor_MakeCurve(*args) -> "Handle_Geom_Curve":
    """
    * Inherited from GHCurve. Provides a curve handled by reference. Build a Geom_Curve using the informations from the Curve from Adaptor3d

    :param C:
    :type C: Adaptor3d_Curve &
    :rtype: Handle_Geom_Curve

    """
    return _GeomAdaptor.geomadaptor_MakeCurve(*args)

def geomadaptor_MakeSurface(*args) -> "Handle_Geom_Surface":
    """
    * Build a Geom_Surface using the informations from the Surface from Adaptor3d

    :param S:
    :type S: Adaptor3d_Surface &
    :rtype: Handle_Geom_Surface

    """
    return _GeomAdaptor.geomadaptor_MakeSurface(*args)

class GeomAdaptor_Curve(OCC.Adaptor3d.Adaptor3d_Curve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: Handle_Geom_Curve &
        :rtype: None

        * ConstructionError is raised if Ufirst>Ulast

        :param C:
        :type C: Handle_Geom_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        _GeomAdaptor.GeomAdaptor_Curve_swiginit(self, _GeomAdaptor.new_GeomAdaptor_Curve(*args))

    def Load(self, *args) -> "void":
        """
        :param C:
        :type C: Handle_Geom_Curve &
        :rtype: None

        * ConstructionError is raised if Ufirst>Ulast

        :param C:
        :type C: Handle_Geom_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        return _GeomAdaptor.GeomAdaptor_Curve_Load(self, *args)


    def Curve(self, *args) -> "Handle_Geom_Curve":
        """
        * Provides a curve inherited from Hcurve from Adaptor. This is inherited to provide easy to use constructors.

        :rtype: Handle_Geom_Curve

        """
        return _GeomAdaptor.GeomAdaptor_Curve_Curve(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomAdaptor.delete_GeomAdaptor_Curve
GeomAdaptor_Curve.Load = new_instancemethod(_GeomAdaptor.GeomAdaptor_Curve_Load, None, GeomAdaptor_Curve)
GeomAdaptor_Curve.Curve = new_instancemethod(_GeomAdaptor.GeomAdaptor_Curve_Curve, None, GeomAdaptor_Curve)
GeomAdaptor_Curve_swigregister = _GeomAdaptor.GeomAdaptor_Curve_swigregister
GeomAdaptor_Curve_swigregister(GeomAdaptor_Curve)

class GeomAdaptor_GHCurve(OCC.Adaptor3d.Adaptor3d_HCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param C:
        :type C: GeomAdaptor_Curve &
        :rtype: None

        """
        _GeomAdaptor.GeomAdaptor_GHCurve_swiginit(self, _GeomAdaptor.new_GeomAdaptor_GHCurve(*args))

    def Set(self, *args) -> "void":
        """
        :param C:
        :type C: GeomAdaptor_Curve &
        :rtype: None

        """
        return _GeomAdaptor.GeomAdaptor_GHCurve_Set(self, *args)


    def ChangeCurve(self, *args) -> "GeomAdaptor_Curve &":
        """
        :rtype: GeomAdaptor_Curve

        """
        return _GeomAdaptor.GeomAdaptor_GHCurve_ChangeCurve(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GeomAdaptor_GHCurve(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomAdaptor.delete_GeomAdaptor_GHCurve
GeomAdaptor_GHCurve.Set = new_instancemethod(_GeomAdaptor.GeomAdaptor_GHCurve_Set, None, GeomAdaptor_GHCurve)
GeomAdaptor_GHCurve.ChangeCurve = new_instancemethod(_GeomAdaptor.GeomAdaptor_GHCurve_ChangeCurve, None, GeomAdaptor_GHCurve)
GeomAdaptor_GHCurve_swigregister = _GeomAdaptor.GeomAdaptor_GHCurve_swigregister
GeomAdaptor_GHCurve_swigregister(GeomAdaptor_GHCurve)

class Handle_GeomAdaptor_GHCurve(OCC.Adaptor3d.Handle_Adaptor3d_HCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _GeomAdaptor.Handle_GeomAdaptor_GHCurve_swiginit(self, _GeomAdaptor.new_Handle_GeomAdaptor_GHCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GeomAdaptor.Handle_GeomAdaptor_GHCurve_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _GeomAdaptor.delete_Handle_GeomAdaptor_GHCurve
Handle_GeomAdaptor_GHCurve.Nullify = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_GHCurve_Nullify, None, Handle_GeomAdaptor_GHCurve)
Handle_GeomAdaptor_GHCurve.IsNull = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_GHCurve_IsNull, None, Handle_GeomAdaptor_GHCurve)
Handle_GeomAdaptor_GHCurve._get_reference = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_GHCurve__get_reference, None, Handle_GeomAdaptor_GHCurve)
Handle_GeomAdaptor_GHCurve_swigregister = _GeomAdaptor.Handle_GeomAdaptor_GHCurve_swigregister
Handle_GeomAdaptor_GHCurve_swigregister(Handle_GeomAdaptor_GHCurve)

def Handle_GeomAdaptor_GHCurve_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_GeomAdaptor_GHCurve const":
    return _GeomAdaptor.Handle_GeomAdaptor_GHCurve_DownCast(AnObject)
Handle_GeomAdaptor_GHCurve_DownCast = _GeomAdaptor.Handle_GeomAdaptor_GHCurve_DownCast

class GeomAdaptor_GHSurface(OCC.Adaptor3d.Adaptor3d_HSurface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param S:
        :type S: GeomAdaptor_Surface &
        :rtype: None

        """
        _GeomAdaptor.GeomAdaptor_GHSurface_swiginit(self, _GeomAdaptor.new_GeomAdaptor_GHSurface(*args))

    def Set(self, *args) -> "void":
        """
        :param S:
        :type S: GeomAdaptor_Surface &
        :rtype: None

        """
        return _GeomAdaptor.GeomAdaptor_GHSurface_Set(self, *args)


    def ChangeSurface(self, *args) -> "GeomAdaptor_Surface &":
        """
        :rtype: GeomAdaptor_Surface

        """
        return _GeomAdaptor.GeomAdaptor_GHSurface_ChangeSurface(self, *args)


    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GeomAdaptor_GHSurface(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomAdaptor.delete_GeomAdaptor_GHSurface
GeomAdaptor_GHSurface.Set = new_instancemethod(_GeomAdaptor.GeomAdaptor_GHSurface_Set, None, GeomAdaptor_GHSurface)
GeomAdaptor_GHSurface.ChangeSurface = new_instancemethod(_GeomAdaptor.GeomAdaptor_GHSurface_ChangeSurface, None, GeomAdaptor_GHSurface)
GeomAdaptor_GHSurface_swigregister = _GeomAdaptor.GeomAdaptor_GHSurface_swigregister
GeomAdaptor_GHSurface_swigregister(GeomAdaptor_GHSurface)

class Handle_GeomAdaptor_GHSurface(OCC.Adaptor3d.Handle_Adaptor3d_HSurface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _GeomAdaptor.Handle_GeomAdaptor_GHSurface_swiginit(self, _GeomAdaptor.new_Handle_GeomAdaptor_GHSurface(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GeomAdaptor.Handle_GeomAdaptor_GHSurface_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _GeomAdaptor.delete_Handle_GeomAdaptor_GHSurface
Handle_GeomAdaptor_GHSurface.Nullify = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_GHSurface_Nullify, None, Handle_GeomAdaptor_GHSurface)
Handle_GeomAdaptor_GHSurface.IsNull = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_GHSurface_IsNull, None, Handle_GeomAdaptor_GHSurface)
Handle_GeomAdaptor_GHSurface._get_reference = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_GHSurface__get_reference, None, Handle_GeomAdaptor_GHSurface)
Handle_GeomAdaptor_GHSurface_swigregister = _GeomAdaptor.Handle_GeomAdaptor_GHSurface_swigregister
Handle_GeomAdaptor_GHSurface_swigregister(Handle_GeomAdaptor_GHSurface)

def Handle_GeomAdaptor_GHSurface_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_GeomAdaptor_GHSurface const":
    return _GeomAdaptor.Handle_GeomAdaptor_GHSurface_DownCast(AnObject)
Handle_GeomAdaptor_GHSurface_DownCast = _GeomAdaptor.Handle_GeomAdaptor_GHSurface_DownCast

class GeomAdaptor_Surface(OCC.Adaptor3d.Adaptor3d_Surface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param S:
        :type S: Handle_Geom_Surface &
        :rtype: None

        * ConstructionError is raised if UFirst>ULast or VFirst>VLast

        :param S:
        :type S: Handle_Geom_Surface &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :param VFirst:
        :type VFirst: float
        :param VLast:
        :type VLast: float
        :param TolU: default value is 0.0
        :type TolU: float
        :param TolV: default value is 0.0
        :type TolV: float
        :rtype: None

        """
        _GeomAdaptor.GeomAdaptor_Surface_swiginit(self, _GeomAdaptor.new_GeomAdaptor_Surface(*args))

    def Load(self, *args) -> "void":
        """
        :param S:
        :type S: Handle_Geom_Surface &
        :rtype: None

        * ConstructionError is raised if UFirst>ULast or VFirst>VLast

        :param S:
        :type S: Handle_Geom_Surface &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :param VFirst:
        :type VFirst: float
        :param VLast:
        :type VLast: float
        :param TolU: default value is 0.0
        :type TolU: float
        :param TolV: default value is 0.0
        :type TolV: float
        :rtype: None

        """
        return _GeomAdaptor.GeomAdaptor_Surface_Load(self, *args)


    def Surface(self, *args) -> "Handle_Geom_Surface":
        """
        :rtype: Handle_Geom_Surface

        """
        return _GeomAdaptor.GeomAdaptor_Surface_Surface(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomAdaptor.delete_GeomAdaptor_Surface
GeomAdaptor_Surface.Load = new_instancemethod(_GeomAdaptor.GeomAdaptor_Surface_Load, None, GeomAdaptor_Surface)
GeomAdaptor_Surface.Surface = new_instancemethod(_GeomAdaptor.GeomAdaptor_Surface_Surface, None, GeomAdaptor_Surface)
GeomAdaptor_Surface_swigregister = _GeomAdaptor.GeomAdaptor_Surface_swigregister
GeomAdaptor_Surface_swigregister(GeomAdaptor_Surface)

class GeomAdaptor_HCurve(GeomAdaptor_GHCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param AS:
        :type AS: GeomAdaptor_Curve &
        :rtype: None

        :param S:
        :type S: Handle_Geom_Curve &
        :rtype: None

        * ConstructionError is raised if UFirst>ULast or VFirst>VLast

        :param S:
        :type S: Handle_Geom_Curve &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :rtype: None

        """
        _GeomAdaptor.GeomAdaptor_HCurve_swiginit(self, _GeomAdaptor.new_GeomAdaptor_HCurve(*args))

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GeomAdaptor_HCurve(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomAdaptor.delete_GeomAdaptor_HCurve
GeomAdaptor_HCurve_swigregister = _GeomAdaptor.GeomAdaptor_HCurve_swigregister
GeomAdaptor_HCurve_swigregister(GeomAdaptor_HCurve)

class Handle_GeomAdaptor_HCurve(Handle_GeomAdaptor_GHCurve):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _GeomAdaptor.Handle_GeomAdaptor_HCurve_swiginit(self, _GeomAdaptor.new_Handle_GeomAdaptor_HCurve(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GeomAdaptor.Handle_GeomAdaptor_HCurve_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _GeomAdaptor.delete_Handle_GeomAdaptor_HCurve
Handle_GeomAdaptor_HCurve.Nullify = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_HCurve_Nullify, None, Handle_GeomAdaptor_HCurve)
Handle_GeomAdaptor_HCurve.IsNull = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_HCurve_IsNull, None, Handle_GeomAdaptor_HCurve)
Handle_GeomAdaptor_HCurve._get_reference = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_HCurve__get_reference, None, Handle_GeomAdaptor_HCurve)
Handle_GeomAdaptor_HCurve_swigregister = _GeomAdaptor.Handle_GeomAdaptor_HCurve_swigregister
Handle_GeomAdaptor_HCurve_swigregister(Handle_GeomAdaptor_HCurve)

def Handle_GeomAdaptor_HCurve_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_GeomAdaptor_HCurve const":
    return _GeomAdaptor.Handle_GeomAdaptor_HCurve_DownCast(AnObject)
Handle_GeomAdaptor_HCurve_DownCast = _GeomAdaptor.Handle_GeomAdaptor_HCurve_DownCast

class GeomAdaptor_HSurface(GeomAdaptor_GHSurface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        :rtype: None

        :param AS:
        :type AS: GeomAdaptor_Surface &
        :rtype: None

        :param S:
        :type S: Handle_Geom_Surface &
        :rtype: None

        * ConstructionError is raised if UFirst>ULast or VFirst>VLast

        :param S:
        :type S: Handle_Geom_Surface &
        :param UFirst:
        :type UFirst: float
        :param ULast:
        :type ULast: float
        :param VFirst:
        :type VFirst: float
        :param VLast:
        :type VLast: float
        :param TolU: default value is 0.0
        :type TolU: float
        :param TolV: default value is 0.0
        :type TolV: float
        :rtype: None

        """
        _GeomAdaptor.GeomAdaptor_HSurface_swiginit(self, _GeomAdaptor.new_GeomAdaptor_HSurface(*args))

    def GetHandle(self):
        try:
            return self.thisHandle
        except:
            self.thisHandle = Handle_GeomAdaptor_HSurface(self)
            self.thisown = False
            return self.thisHandle


    __repr__ = _dumps_object

    __swig_destroy__ = _GeomAdaptor.delete_GeomAdaptor_HSurface
GeomAdaptor_HSurface_swigregister = _GeomAdaptor.GeomAdaptor_HSurface_swigregister
GeomAdaptor_HSurface_swigregister(GeomAdaptor_HSurface)

class Handle_GeomAdaptor_HSurface(Handle_GeomAdaptor_GHSurface):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _GeomAdaptor.Handle_GeomAdaptor_HSurface_swiginit(self, _GeomAdaptor.new_Handle_GeomAdaptor_HSurface(*args))

            # register the handle in the base object
        if len(args) > 0:
            register_handle(self, args[0])



    DownCast = staticmethod(_GeomAdaptor.Handle_GeomAdaptor_HSurface_DownCast)

    def GetObject(self):
        obj = self._get_reference()
        register_handle(self, obj)
        return obj

    __swig_destroy__ = _GeomAdaptor.delete_Handle_GeomAdaptor_HSurface
Handle_GeomAdaptor_HSurface.Nullify = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_HSurface_Nullify, None, Handle_GeomAdaptor_HSurface)
Handle_GeomAdaptor_HSurface.IsNull = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_HSurface_IsNull, None, Handle_GeomAdaptor_HSurface)
Handle_GeomAdaptor_HSurface._get_reference = new_instancemethod(_GeomAdaptor.Handle_GeomAdaptor_HSurface__get_reference, None, Handle_GeomAdaptor_HSurface)
Handle_GeomAdaptor_HSurface_swigregister = _GeomAdaptor.Handle_GeomAdaptor_HSurface_swigregister
Handle_GeomAdaptor_HSurface_swigregister(Handle_GeomAdaptor_HSurface)

def Handle_GeomAdaptor_HSurface_DownCast(AnObject: 'Handle_Standard_Transient') -> "Handle_GeomAdaptor_HSurface const":
    return _GeomAdaptor.Handle_GeomAdaptor_HSurface_DownCast(AnObject)
Handle_GeomAdaptor_HSurface_DownCast = _GeomAdaptor.Handle_GeomAdaptor_HSurface_DownCast



