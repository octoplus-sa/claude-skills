# JMP Application Messages

Source: JMP 19 JSL Syntax Reference (PDF pages 472-474).

## Index (line numbers in this file)

- `<< Combine Windows` — L45
- `<< Create Instance` — L100
- `<< Create Objects` — L113
- `<< Debug` — L50
- `<< Edit` — L55
- `<< Get Box` — L118
- `<< Get Instance` — L106
- `<< Get Modules` — L64
- `<< Get Namespace` — L68
- `<< Get Windows` — L73
- `<< Open File` — L77
- `<< Relaunch Analysis` — L80
- `<< Run` — L82
- `<< Save Script to Data Table` — L86
- `<< Save Script to Journal` — L87
- `<< Save Script to Script Window` — L88
- `Like JMP App()` — L123
- `The JMP App()` — L69
---

JMP Application Messages

JMP Application Messages
This section contains JSL messages that apply to the JMP Application Builder and the JMP
Dashboard Builder. Both of these applications use the same infrastructure to design and
execute applications and dashboards. Because a dashboard is a special form of an application,
this section uses the term application to describe how both dashboard and application objects
use scripting.
See the Scripting Index in the JMP Help menu for examples.

JMP App Messages
The JMP App object is the main controller for JMP applications built by Application Builder or
Dashboard Builder. Scripts both inside and outside of a JMP application can use a JMP App
object.
A JMP application can have one of three states: initial (with no editor, and the application is
not running), running, or editing. A JMP App object only exists in one state at a time; if you are
editing a JMP Application and choose to run it, a copy of the JMP application is created before
it is run.
app<<Combine Windows({reports or data tables})
Description

Combines the given list of platform reports or data tables into a new module. The
application should be in the initial state when this message is sent.
app<<Debug
Invokes the JSL Debugger on a JMP application. The application script will run first. The
Debugger then breaks as each module is created, invoking the module scripts. In the
Debugger, set breakpoints to debug the scripts that are associated with the application or
modules.
app<<Edit
Starts Application Builder on a JMP application that is in the initial state. There is no
editor, and the application is not running.

JSL Messages
JMP Application Messages

473

app<<Get Modules
Gets the list of modules associated with an application. In Application Builder, each
module corresponds to a tab in the workspace, which describes the layout and behavior
for one type of window in the application.
app<<Get Namespace
The JMP App() object automatically creates an anonymous namespace for the variables
created within the application script. Use this message to get a handle to this namespace to
inspect or modify variables. There is a default symbol in this namespace called
thisApplication, which holds a reference to the application itself.
app<<Get Windows
Gets a list of all windows created as instances of JMP app modules. Some modules might
create more than one instance. All windows might not exist at the same time, so the
number of windows might vary and might differ from the number of modules.
app<<Open File(path)
Resets the state of an existing application from a the .jmpapp or .jmappsource file. path is
quoted.
app<<Relaunch Analysis
Creates a new copy of a running application and runs the new instance.
app<<Run
Runs the application. The application script runs first, and depending on settings, one or
more JMP app module instance objects might be created automatically.
app<<Save Script to Add-In
app<<Save Script to Data Table
app<<Save Script to Journal
app<<Save Script to Script Window
Saves the script for the application to the given destination. An application script consists
of a JMP App() object that contains the definition for the application. Scripts saved to an
add-in, data table, or journal include a Run message to run the application. A script saved
to the script window includes an Edit message to open Application Builder.

JMP Application Messages

JMP App Module Messages
A JMP application module is a definition of the display box layout and behavior for a single
component in a JMP application or dashboard. Depending on the module type, the
component might represent a window in the application or just part of a window.
module<<Create Instance
Use Create Instance within a JMP App() or JMP App Module() script to create an
instance of a JMP app module. By default, one instance of each JMP application module is
created when an application is run. For more complex applications with multiple
windows, such as a launcher and report combination, it might be necessary to change the
default settings and control how the module instance is created.
module<<Get Instance
Returns a handle to the application that owns a module.

JMP App Module Instance Messages
The JMP application module instance is a running realization of a JMP app module, a window
on the screen, or a collection of display box elements that can be inserted into another
window.
inst<<Create Objects
Appears in the default template for a JMP app module script. This message controls the
point at which the display and window for a module instance are created. The message
appears in the script so that the script writer can choose to do certain setup before the
objects are created. One example of this setup is for a parameterized application.
inst<<Get Box
Returns a handle to the top-most display box associated with a module instance. This
might be useful to issue display or window commands, such as the Save to PDF or Close
Window messages.
inst<<Get Namespace
Like JMP App(), each JMP application module instance also creates an anonymous
namespace for all variables created in the module script. The namespace also includes all
the variables that represent the display boxes in the module. This namespace contains a
default symbol named thisModuleInstance that refers to itself.
