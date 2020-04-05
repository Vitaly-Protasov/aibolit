from .ast import Node as Node
from typing import Any, Set

class CompilationUnit(Node):
    attrs: Any = ...

class Import(Node):
    attrs: Any = ...

class Documented(Node):
    attrs: Any = ...

class Declaration(Node):
    attrs: Any = ...
    modifiers: Set[str] = ...

class TypeDeclaration(Declaration, Documented):
    attrs: Any = ...
    @property
    def fields(self): ...
    @property
    def methods(self): ...
    @property
    def constructors(self): ...

class PackageDeclaration(Declaration, Documented):
    attrs: Any = ...

class ClassDeclaration(TypeDeclaration):
    attrs: Any = ...

class EnumDeclaration(TypeDeclaration):
    attrs: Any = ...
    @property
    def fields(self): ...
    @property
    def methods(self): ...

class InterfaceDeclaration(TypeDeclaration):
    attrs: Any = ...

class AnnotationDeclaration(TypeDeclaration):
    attrs: Any = ...

class Type(Node):
    attrs: Any = ...

class BasicType(Type):
    attrs: Any = ...

class ReferenceType(Type):
    attrs: Any = ...

class TypeArgument(Node):
    attrs: Any = ...

class TypeParameter(Node):
    attrs: Any = ...

class Annotation(Node):
    attrs: Any = ...

class ElementValuePair(Node):
    attrs: Any = ...

class ElementArrayValue(Node):
    attrs: Any = ...

class Member(Documented):
    attrs: Any = ...

class MethodDeclaration(Member, Declaration):
    attrs: Any = ...
    name: str = ...

class FieldDeclaration(Member, Declaration):
    attrs: Any = ...

class ConstructorDeclaration(Declaration, Documented):
    attrs: Any = ...

class ConstantDeclaration(FieldDeclaration):
    attrs: Any = ...

class ArrayInitializer(Node):
    attrs: Any = ...

class VariableDeclaration(Declaration):
    attrs: Any = ...

class LocalVariableDeclaration(VariableDeclaration):
    attrs: Any = ...

class VariableDeclarator(Node):
    attrs: Any = ...

class FormalParameter(Declaration):
    attrs: Any = ...

class InferredFormalParameter(Node):
    attrs: Any = ...

class Statement(Node):
    attrs: Any = ...

class IfStatement(Statement):
    attrs: Any = ...

class WhileStatement(Statement):
    attrs: Any = ...

class DoStatement(Statement):
    attrs: Any = ...

class ForStatement(Statement):
    attrs: Any = ...

class AssertStatement(Statement):
    attrs: Any = ...

class BreakStatement(Statement):
    attrs: Any = ...

class ContinueStatement(Statement):
    attrs: Any = ...

class ReturnStatement(Statement):
    attrs: Any = ...

class ThrowStatement(Statement):
    attrs: Any = ...

class SynchronizedStatement(Statement):
    attrs: Any = ...

class TryStatement(Statement):
    attrs: Any = ...

class SwitchStatement(Statement):
    attrs: Any = ...

class BlockStatement(Statement):
    attrs: Any = ...

class StatementExpression(Statement):
    attrs: Any = ...

class TryResource(Declaration):
    attrs: Any = ...

class CatchClause(Statement):
    attrs: Any = ...

class CatchClauseParameter(Declaration):
    attrs: Any = ...

class SwitchStatementCase(Node):
    attrs: Any = ...

class ForControl(Node):
    attrs: Any = ...

class EnhancedForControl(Node):
    attrs: Any = ...

class Expression(Node):
    attrs: Any = ...

class Assignment(Expression):
    attrs: Any = ...

class TernaryExpression(Expression):
    attrs: Any = ...
    if_true: Expression = ...

class BinaryOperation(Expression):
    attrs: Any = ...

class Cast(Expression):
    attrs: Any = ...

class MethodReference(Expression):
    attrs: Any = ...

class LambdaExpression(Expression):
    attrs: Any = ...

class Primary(Expression):
    attrs: Any = ...

class Literal(Primary):
    attrs: Any = ...
    value: str = ...

class This(Primary):
    attrs: Any = ...

class MemberReference(Primary):
    attrs: Any = ...

class Invocation(Primary):
    attrs: Any = ...

class ExplicitConstructorInvocation(Invocation):
    attrs: Any = ...

class SuperConstructorInvocation(Invocation):
    attrs: Any = ...

class MethodInvocation(Invocation):
    attrs: Any = ...

class SuperMethodInvocation(Invocation):
    attrs: Any = ...
    member: str = ...

class SuperMemberReference(Primary):
    attrs: Any = ...

class ArraySelector(Expression):
    attrs: Any = ...

class ClassReference(Primary):
    attrs: Any = ...

class VoidClassReference(ClassReference):
    attrs: Any = ...

class Creator(Primary):
    attrs: Any = ...

class ArrayCreator(Creator):
    attrs: Any = ...

class ClassCreator(Creator):
    attrs: Any = ...

class InnerClassCreator(Creator):
    attrs: Any = ...

class EnumBody(Node):
    attrs: Any = ...

class EnumConstantDeclaration(Declaration, Documented):
    attrs: Any = ...

class AnnotationMethod(Declaration):
    attrs: Any = ...
