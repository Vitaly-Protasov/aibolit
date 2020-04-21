from aibolit.metrics.entropy.entropy import Entropy as M1
from aibolit.metrics.ncss.ncss import NCSSMetric as M2
from aibolit.metrics.spaces.SpaceCounter import IndentationCounter as M3
from aibolit.metrics.cognitiveC.cognitive_c import CognitiveComplexity as M4
from aibolit.metrics.lcom4.lcom4 import LCOM4 as M5
from aibolit.metrics.maxDiameter.max_diam_of_tree import MaxDiamOfTree as M6
from aibolit.patterns.assert_in_code.assert_in_code import AssertInCode as P1
from aibolit.patterns.classic_setter.classic_setter import ClassicSetter as P2
from aibolit.patterns.empty_rethrow.empty_rethrow import EmptyRethrow as P3
from aibolit.patterns.er_class.er_class import ErClass as P4
from aibolit.patterns.force_type_casting_finder.force_type_casting_finder import ForceTypeCastingFinder as P5
from aibolit.patterns.if_return_if_detection.if_detection import CountIfReturn as P6
from aibolit.patterns.implements_multi.implements_multi import ImplementsMultiFinder as P7
from aibolit.patterns.instanceof.instance_of import InstanceOf as P8
from aibolit.patterns.many_primary_ctors.many_primary_ctors import ManyPrimaryCtors as P9
from aibolit.patterns.method_chaining.method_chaining import MethodChainFind as P10
from aibolit.patterns.multiple_try.multiple_try import MultipleTry as P11
from aibolit.patterns.non_final_attribute.non_final_attribute import NonFinalAttribute as P12
from aibolit.patterns.null_check.null_check import NullCheck as P13
from aibolit.patterns.partial_synchronized.partial_synchronized import PartialSync as P14
from aibolit.patterns.redundant_catch.redundant_catch import RedundantCatch as P15
from aibolit.patterns.return_null.return_null import ReturnNull as P16
from aibolit.patterns.string_concat.string_concat import StringConcatFinder as P17
from aibolit.patterns.supermethod.supermethod import SuperMethod as P18
from aibolit.patterns.this_finder.this_finder import ThisFinder as P19
from aibolit.patterns.var_decl_diff.var_decl_diff import VarDeclarationDistance as P20
from aibolit.patterns.var_middle.var_middle import VarMiddle as P21
from aibolit.patterns.array_as_argument.array_as_argument import ArrayAsArgument as P22
from aibolit.patterns.joined_validation.joined_validation import JoinedValidation as P23
from aibolit.patterns.non_final_class.non_final_class import NonFinalClass as P24
from aibolit.patterns.private_static_method.private_static_method import PrivateStaticMethod as P25
from aibolit.patterns.public_static_method.public_static_method import PublicStaticMethod as P26
# from aibolit.patterns.var_siblings.var_siblings import VarSiblings as P27


CONFIG = {
    "patterns": [
        {"name": "Asserts", "code": "P1", "make": lambda: P1()},
        {"name": "Setters", "code": "P2", "make": lambda: P2()},
        {"name": "Empty Rethrow", "code": "P3", "make": lambda: P3()},
        {"name": "Prohibited class name", "code": "P4", "make": lambda: P4()},
        {"name": "Force Type Casting Finder", "code": "P5", "make": lambda: P5()},
        {"name": "Count If Return", "code": "P6", "make": lambda: P6()},
        {"name": "Implements Multi Finder", "code": "P7", "make": lambda: P7()},
        {"name": "Instance of", "code": "P", "make": lambda: P8()},
        {"name": "Many primary constructors", "code": "P", "make": lambda: P9()},
        {"name": "Method chain", "code": "P10", "make": lambda: P10()},
        {"name": "Multiple try", "code": "P11", "make": lambda: P11()},
        {"name": "Non final attribute", "code": "P12", "make": lambda: P12()},
        {"name": "Null check", "code": "P13", "make": lambda: P13()},
        {"name": "Partial synchronized", "code": "P14", "make": lambda: P14()},
        {"name": "Redundant catch", "code": "P15", "make": lambda: P15()},
        {"name": "Return null", "code": "P16", "make": lambda: P16()},
        {"name": "String concat finder", "code": "P17", "make": lambda: P17()},
        {"name": "Super Method", "code": "P18", "make": lambda: P18()},
        {"name": "This finder", "code": "P19", "make": lambda: P19()},
        {"name": "Var declaration distance for 5 lines", "code": "P20", "make": lambda: P20(5)},
        {"name": "Var declaration distance for 7 lines", "code": "P20", "make": lambda: P20(7)},
        {"name": "Var declaration distance for 11 lines", "code": "P20", "make": lambda: P20(11)},
        {"name": "Var in the middle", "code": "P21", "make": lambda: P21()},
        {"name": "Array as function argument", "code": "P22", "make": lambda: P22()},
        {"name": "Joined validation", "code": "P23", "make": lambda: P23()},
        {"name": "Non final class", "code": "P24", "make": lambda: P24()},
        {"name": "Private static method", "code": "P25", "make": lambda: P25()},
        {"name": "Public static method", "code": "P26", "make": lambda: P26()},
    ],
    "metrics": [
        {"name": "Entropy", "code": "M1", "make": lambda: M1()},
        {"name": "NCSS", "code": "M2", "make": lambda: M2()},
        {"name": "Indentation counter: Right total variance", "code": "M3", "make": lambda: M3(right_var=True)},
        {"name": "Indentation counter: Left total variance", "code": "P7", "make": lambda: M3(left_var=True)},
        {"name": "Indentation counter: Right max variance", "code": "P7", "make": lambda: M3(max_right=True)},
        {"name": "Indentation counter: Left max variance", "code": "P7", "make": lambda: M3(max_left=True)},
        {"name": "Cognitive Complexity", "code": "M4", "make": lambda: M4()},
        {"name": "LCOM4", "code": "M5", "make": lambda: M5()},
        {"name": "Max diameter of AST", "code": "M6", "make": lambda: M6()}
    ],
    "target": {

    }
}
