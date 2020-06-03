# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (3, 0, 0):
    new_instancemethod = lambda func, inst, cls: _RWStepAP203.SWIG_PyInstanceMethod_New(func)
else:
    from new import instancemethod as new_instancemethod
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_RWStepAP203')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_RWStepAP203')
    _RWStepAP203 = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_RWStepAP203', [dirname(__file__)])
        except ImportError:
            import _RWStepAP203
            return _RWStepAP203
        try:
            _mod = imp.load_module('_RWStepAP203', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _RWStepAP203 = swig_import_helper()
    del swig_import_helper
else:
    import _RWStepAP203
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
    __swig_destroy__ = _RWStepAP203.delete_SwigPyIterator
    def __iter__(self):
        return self
SwigPyIterator.value = new_instancemethod(_RWStepAP203.SwigPyIterator_value, None, SwigPyIterator)
SwigPyIterator.incr = new_instancemethod(_RWStepAP203.SwigPyIterator_incr, None, SwigPyIterator)
SwigPyIterator.decr = new_instancemethod(_RWStepAP203.SwigPyIterator_decr, None, SwigPyIterator)
SwigPyIterator.distance = new_instancemethod(_RWStepAP203.SwigPyIterator_distance, None, SwigPyIterator)
SwigPyIterator.equal = new_instancemethod(_RWStepAP203.SwigPyIterator_equal, None, SwigPyIterator)
SwigPyIterator.copy = new_instancemethod(_RWStepAP203.SwigPyIterator_copy, None, SwigPyIterator)
SwigPyIterator.next = new_instancemethod(_RWStepAP203.SwigPyIterator_next, None, SwigPyIterator)
SwigPyIterator.__next__ = new_instancemethod(_RWStepAP203.SwigPyIterator___next__, None, SwigPyIterator)
SwigPyIterator.previous = new_instancemethod(_RWStepAP203.SwigPyIterator_previous, None, SwigPyIterator)
SwigPyIterator.advance = new_instancemethod(_RWStepAP203.SwigPyIterator_advance, None, SwigPyIterator)
SwigPyIterator.__eq__ = new_instancemethod(_RWStepAP203.SwigPyIterator___eq__, None, SwigPyIterator)
SwigPyIterator.__ne__ = new_instancemethod(_RWStepAP203.SwigPyIterator___ne__, None, SwigPyIterator)
SwigPyIterator.__iadd__ = new_instancemethod(_RWStepAP203.SwigPyIterator___iadd__, None, SwigPyIterator)
SwigPyIterator.__isub__ = new_instancemethod(_RWStepAP203.SwigPyIterator___isub__, None, SwigPyIterator)
SwigPyIterator.__add__ = new_instancemethod(_RWStepAP203.SwigPyIterator___add__, None, SwigPyIterator)
SwigPyIterator.__sub__ = new_instancemethod(_RWStepAP203.SwigPyIterator___sub__, None, SwigPyIterator)
SwigPyIterator_swigregister = _RWStepAP203.SwigPyIterator_swigregister
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
import OCC.Interface
import OCC.TCollection
import OCC.MMgt
import OCC.TColStd
import OCC.Message
import OCC.StepAP203
import OCC.StepBasic
import OCC.StepRepr

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

class RWStepAP203_RWCcDesignApproval(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWCcDesignApproval_swiginit(self, _RWStepAP203.new_RWStepAP203_RWCcDesignApproval(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads CcDesignApproval

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignApproval &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignApproval_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes CcDesignApproval

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignApproval &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignApproval_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_CcDesignApproval &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignApproval_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWCcDesignApproval
RWStepAP203_RWCcDesignApproval.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignApproval_ReadStep, None, RWStepAP203_RWCcDesignApproval)
RWStepAP203_RWCcDesignApproval.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignApproval_WriteStep, None, RWStepAP203_RWCcDesignApproval)
RWStepAP203_RWCcDesignApproval.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignApproval_Share, None, RWStepAP203_RWCcDesignApproval)
RWStepAP203_RWCcDesignApproval_swigregister = _RWStepAP203.RWStepAP203_RWCcDesignApproval_swigregister
RWStepAP203_RWCcDesignApproval_swigregister(RWStepAP203_RWCcDesignApproval)

class RWStepAP203_RWCcDesignCertification(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWCcDesignCertification_swiginit(self, _RWStepAP203.new_RWStepAP203_RWCcDesignCertification(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads CcDesignCertification

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignCertification &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignCertification_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes CcDesignCertification

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignCertification &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignCertification_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_CcDesignCertification &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignCertification_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWCcDesignCertification
RWStepAP203_RWCcDesignCertification.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignCertification_ReadStep, None, RWStepAP203_RWCcDesignCertification)
RWStepAP203_RWCcDesignCertification.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignCertification_WriteStep, None, RWStepAP203_RWCcDesignCertification)
RWStepAP203_RWCcDesignCertification.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignCertification_Share, None, RWStepAP203_RWCcDesignCertification)
RWStepAP203_RWCcDesignCertification_swigregister = _RWStepAP203.RWStepAP203_RWCcDesignCertification_swigregister
RWStepAP203_RWCcDesignCertification_swigregister(RWStepAP203_RWCcDesignCertification)

class RWStepAP203_RWCcDesignContract(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWCcDesignContract_swiginit(self, _RWStepAP203.new_RWStepAP203_RWCcDesignContract(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads CcDesignContract

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignContract &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignContract_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes CcDesignContract

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignContract &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignContract_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_CcDesignContract &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignContract_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWCcDesignContract
RWStepAP203_RWCcDesignContract.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignContract_ReadStep, None, RWStepAP203_RWCcDesignContract)
RWStepAP203_RWCcDesignContract.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignContract_WriteStep, None, RWStepAP203_RWCcDesignContract)
RWStepAP203_RWCcDesignContract.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignContract_Share, None, RWStepAP203_RWCcDesignContract)
RWStepAP203_RWCcDesignContract_swigregister = _RWStepAP203.RWStepAP203_RWCcDesignContract_swigregister
RWStepAP203_RWCcDesignContract_swigregister(RWStepAP203_RWCcDesignContract)

class RWStepAP203_RWCcDesignDateAndTimeAssignment(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_swiginit(self, _RWStepAP203.new_RWStepAP203_RWCcDesignDateAndTimeAssignment(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads CcDesignDateAndTimeAssignment

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignDateAndTimeAssignment &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes CcDesignDateAndTimeAssignment

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignDateAndTimeAssignment &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_CcDesignDateAndTimeAssignment &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWCcDesignDateAndTimeAssignment
RWStepAP203_RWCcDesignDateAndTimeAssignment.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_ReadStep, None, RWStepAP203_RWCcDesignDateAndTimeAssignment)
RWStepAP203_RWCcDesignDateAndTimeAssignment.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_WriteStep, None, RWStepAP203_RWCcDesignDateAndTimeAssignment)
RWStepAP203_RWCcDesignDateAndTimeAssignment.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_Share, None, RWStepAP203_RWCcDesignDateAndTimeAssignment)
RWStepAP203_RWCcDesignDateAndTimeAssignment_swigregister = _RWStepAP203.RWStepAP203_RWCcDesignDateAndTimeAssignment_swigregister
RWStepAP203_RWCcDesignDateAndTimeAssignment_swigregister(RWStepAP203_RWCcDesignDateAndTimeAssignment)

class RWStepAP203_RWCcDesignPersonAndOrganizationAssignment(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_swiginit(self, _RWStepAP203.new_RWStepAP203_RWCcDesignPersonAndOrganizationAssignment(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads CcDesignPersonAndOrganizationAssignment

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignPersonAndOrganizationAssignment &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes CcDesignPersonAndOrganizationAssignment

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignPersonAndOrganizationAssignment &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_CcDesignPersonAndOrganizationAssignment &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWCcDesignPersonAndOrganizationAssignment
RWStepAP203_RWCcDesignPersonAndOrganizationAssignment.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_ReadStep, None, RWStepAP203_RWCcDesignPersonAndOrganizationAssignment)
RWStepAP203_RWCcDesignPersonAndOrganizationAssignment.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_WriteStep, None, RWStepAP203_RWCcDesignPersonAndOrganizationAssignment)
RWStepAP203_RWCcDesignPersonAndOrganizationAssignment.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_Share, None, RWStepAP203_RWCcDesignPersonAndOrganizationAssignment)
RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_swigregister = _RWStepAP203.RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_swigregister
RWStepAP203_RWCcDesignPersonAndOrganizationAssignment_swigregister(RWStepAP203_RWCcDesignPersonAndOrganizationAssignment)

class RWStepAP203_RWCcDesignSecurityClassification(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_swiginit(self, _RWStepAP203.new_RWStepAP203_RWCcDesignSecurityClassification(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads CcDesignSecurityClassification

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignSecurityClassification &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes CcDesignSecurityClassification

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignSecurityClassification &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_CcDesignSecurityClassification &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWCcDesignSecurityClassification
RWStepAP203_RWCcDesignSecurityClassification.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_ReadStep, None, RWStepAP203_RWCcDesignSecurityClassification)
RWStepAP203_RWCcDesignSecurityClassification.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_WriteStep, None, RWStepAP203_RWCcDesignSecurityClassification)
RWStepAP203_RWCcDesignSecurityClassification.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_Share, None, RWStepAP203_RWCcDesignSecurityClassification)
RWStepAP203_RWCcDesignSecurityClassification_swigregister = _RWStepAP203.RWStepAP203_RWCcDesignSecurityClassification_swigregister
RWStepAP203_RWCcDesignSecurityClassification_swigregister(RWStepAP203_RWCcDesignSecurityClassification)

class RWStepAP203_RWCcDesignSpecificationReference(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_swiginit(self, _RWStepAP203.new_RWStepAP203_RWCcDesignSpecificationReference(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads CcDesignSpecificationReference

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignSpecificationReference &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes CcDesignSpecificationReference

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_CcDesignSpecificationReference &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_CcDesignSpecificationReference &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWCcDesignSpecificationReference
RWStepAP203_RWCcDesignSpecificationReference.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_ReadStep, None, RWStepAP203_RWCcDesignSpecificationReference)
RWStepAP203_RWCcDesignSpecificationReference.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_WriteStep, None, RWStepAP203_RWCcDesignSpecificationReference)
RWStepAP203_RWCcDesignSpecificationReference.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_Share, None, RWStepAP203_RWCcDesignSpecificationReference)
RWStepAP203_RWCcDesignSpecificationReference_swigregister = _RWStepAP203.RWStepAP203_RWCcDesignSpecificationReference_swigregister
RWStepAP203_RWCcDesignSpecificationReference_swigregister(RWStepAP203_RWCcDesignSpecificationReference)

class RWStepAP203_RWChange(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWChange_swiginit(self, _RWStepAP203.new_RWStepAP203_RWChange(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads Change

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_Change &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWChange_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes Change

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_Change &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWChange_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_Change &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWChange_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWChange
RWStepAP203_RWChange.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWChange_ReadStep, None, RWStepAP203_RWChange)
RWStepAP203_RWChange.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWChange_WriteStep, None, RWStepAP203_RWChange)
RWStepAP203_RWChange.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWChange_Share, None, RWStepAP203_RWChange)
RWStepAP203_RWChange_swigregister = _RWStepAP203.RWStepAP203_RWChange_swigregister
RWStepAP203_RWChange_swigregister(RWStepAP203_RWChange)

class RWStepAP203_RWChangeRequest(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWChangeRequest_swiginit(self, _RWStepAP203.new_RWStepAP203_RWChangeRequest(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads ChangeRequest

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_ChangeRequest &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWChangeRequest_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes ChangeRequest

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_ChangeRequest &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWChangeRequest_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_ChangeRequest &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWChangeRequest_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWChangeRequest
RWStepAP203_RWChangeRequest.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWChangeRequest_ReadStep, None, RWStepAP203_RWChangeRequest)
RWStepAP203_RWChangeRequest.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWChangeRequest_WriteStep, None, RWStepAP203_RWChangeRequest)
RWStepAP203_RWChangeRequest.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWChangeRequest_Share, None, RWStepAP203_RWChangeRequest)
RWStepAP203_RWChangeRequest_swigregister = _RWStepAP203.RWStepAP203_RWChangeRequest_swigregister
RWStepAP203_RWChangeRequest_swigregister(RWStepAP203_RWChangeRequest)

class RWStepAP203_RWStartRequest(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWStartRequest_swiginit(self, _RWStepAP203.new_RWStepAP203_RWStartRequest(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads StartRequest

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_StartRequest &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWStartRequest_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes StartRequest

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_StartRequest &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWStartRequest_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_StartRequest &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWStartRequest_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWStartRequest
RWStepAP203_RWStartRequest.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWStartRequest_ReadStep, None, RWStepAP203_RWStartRequest)
RWStepAP203_RWStartRequest.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWStartRequest_WriteStep, None, RWStepAP203_RWStartRequest)
RWStepAP203_RWStartRequest.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWStartRequest_Share, None, RWStepAP203_RWStartRequest)
RWStepAP203_RWStartRequest_swigregister = _RWStepAP203.RWStepAP203_RWStartRequest_swigregister
RWStepAP203_RWStartRequest_swigregister(RWStepAP203_RWStartRequest)

class RWStepAP203_RWStartWork(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        * Empty constructor

        :rtype: None

        """
        _RWStepAP203.RWStepAP203_RWStartWork_swiginit(self, _RWStepAP203.new_RWStepAP203_RWStartWork(*args))

    def ReadStep(self, *args) -> "void":
        """
        * Reads StartWork

        :param data:
        :type data: Handle_StepData_StepReaderData &
        :param num:
        :type num: int
        :param ach:
        :type ach: Handle_Interface_Check &
        :param ent:
        :type ent: Handle_StepAP203_StartWork &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWStartWork_ReadStep(self, *args)


    def WriteStep(self, *args) -> "void":
        """
        * Writes StartWork

        :param SW:
        :type SW: StepData_StepWriter &
        :param ent:
        :type ent: Handle_StepAP203_StartWork &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWStartWork_WriteStep(self, *args)


    def Share(self, *args) -> "void":
        """
        * Fills data for graph (shared items)

        :param ent:
        :type ent: Handle_StepAP203_StartWork &
        :param iter:
        :type iter: Interface_EntityIterator &
        :rtype: None

        """
        return _RWStepAP203.RWStepAP203_RWStartWork_Share(self, *args)


    __repr__ = _dumps_object

    __swig_destroy__ = _RWStepAP203.delete_RWStepAP203_RWStartWork
RWStepAP203_RWStartWork.ReadStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWStartWork_ReadStep, None, RWStepAP203_RWStartWork)
RWStepAP203_RWStartWork.WriteStep = new_instancemethod(_RWStepAP203.RWStepAP203_RWStartWork_WriteStep, None, RWStepAP203_RWStartWork)
RWStepAP203_RWStartWork.Share = new_instancemethod(_RWStepAP203.RWStepAP203_RWStartWork_Share, None, RWStepAP203_RWStartWork)
RWStepAP203_RWStartWork_swigregister = _RWStepAP203.RWStepAP203_RWStartWork_swigregister
RWStepAP203_RWStartWork_swigregister(RWStepAP203_RWStartWork)


