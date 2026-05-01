# Dynamic Link Library (DLL) Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 465-466).

## Index (line numbers in this file)

- `<< Set Window Size` — L30
- `<< Show Window` — L32
- `<< Size Window` — L36
- `<< Update Window` — L38
- `<< Window Class Name` — L41
- `<< Zoom Window` — L46
- `Alias()` — L63
- `Arg()` — L66
- `Convention()` — L83
- `Declare Function()` — L102
- `Dynamic Link Library()` — L26
- `MaxArgs()` — L87
- `MinArgs()` — L88
- `StackOrder()` — L92
- `StackPop()` — L95
- `StructArg()` — L98
---

JSL Messages
Dynamic Link Library (DLL) Messages

465

window<<Set Window Size(x, y)
Resizes the window.
window<<Show Window(Boolean)
1 shows the window (only if the window is not currently open). 0 hides the window. If the
window is also minimized (on Windows) or docked (on Apple macOS), showing the
window restores it to the normal state and brings it to the front.
window<<Size Window(x, y)
Resizes the window.
window<<Update Window
Updates or refreshes the window holding the display box if there are invalidated regions.
See “window<<Inval” and “window<<Reshow” for additional methods.
window<<Window Class Name
Returns the name of the window class for the display box. Valid responses include:
DataTable, FormulaEditor, Starter, Journal, Launcher, Report, Dialog, DialogWithMenu,
ModalDialog, FindReplace, User, Generic, ToolWindow, FindReplace, AppBuilder, and
Debugger.
window<<Zoom Window
Resizes the window to be large enough to show all of its contents.

Dynamic Link Library (DLL) Messages
dll object<<Call DLL(function name, signature, arguments)
Calls the specified function in the DLL with the specified signature and arguments.
dll object<<Declare Function(name, <named arguments>)
Description

Declares the return type and argument types for the specified function so that it can be
successfully invoked. You can use one of the named arguments for Convention:
"STDCALL" or "PASCAL", or "CDECL". The type argument for Returns takes the same
named arguments as Arg. The name argument is quoted.

Dynamic Link Library (DLL) Messages

Optional Named Arguments
Alias(name) Specifies a quoted name that you can include if you don’t like the name

encoded in the DLL.
Arg(type, <description>, <access mode>, <array>) Arg can appear multiple

times, once for each argument to be sent to the function.
type is one of these keywords that specifies the argument type: "Int8", "UInt8",
"Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64", "Float", "Double",
"AnsiString", "UnicodeString", "Struct", "IntPtr", "UIntPtr", or "ObjPtr".
description is a quoted string that describes the argument for reference.
access mode is an optional keyword that specifies how the argument is passed.
"input" specifies that the argument is passed by value. "output" specifies that the
argument is passed by address with the initial value undefined. "update" specifies that

the argument is passed by reference and the value of the JSL variable is set as the initial
value. The default value is "input".
array is an optional keyword. It is valid only if the type is specified as "Double" and
the access mode is specified as either "input" or "update". Specifies that the exported

function expects an array of doubles.
Convention(calling convention) Specifies the calling convention: "STDCALL" or
"PASCAL", or "CDECL". The default value is "STDCALL". STDCALL and PASCAL are

equivalent.
MaxArgs(n) Specifies the maximum number of arguments that can be supplied.
MinArgs(n) Specifies the minimum number of arguments that can be supplied.
Returns(type) Specifies the data type that the function returns: "Int8", "UInt8",
"Int16", "UInt16", "Int32", "UInt32", "Int64", "UInt64", "Float", "Double",
"AnsiString", "UnicodeString", "Struct", "IntPtr", "UIntPtr", or "ObjPtr".
StackOrder(order) Specifies the order in which arguments are placed on the stack
when calling the function. Valid values are "L2R" (left-to-right) and "R2L"
(right-to-left). The default value is "R2L".
StackPop(pop) Specifies how the exported function expects the stack to be cleared after
the function returns. Valid values are "CALLER" and "CALLEE". The default value is
"CALLEE".
StructArg(Arg(...), <Arg(...)>, ..., <access mode>, <pack mode>,
<description>) Can appear multiple times. If an exported DLL function requires
that a structure argument be passed in as an argument, use StructArg to declare the
structure members. The Arg arguments use the same syntax as for Arg arguments to
Declare Function (one for each structure member), an access mode indicator and a
pack mode indicator.
access mode is an optional keyword that indicates whether the struct argument should
be passed by value (input) or by reference (update).
pack mode is an optional integer that determines how the structure is packed. Valid
values are 1, 2, 4, 8, and 16. The default value is 8.
