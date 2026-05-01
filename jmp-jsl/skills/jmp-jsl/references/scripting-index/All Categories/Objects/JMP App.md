# JMP App

*Source: [https://jsl.jmp.com/All%20Categories/Objects/JMP%20App.html](https://jsl.jmp.com/All%20Categories/Objects/JMP%20App.html)*

---

# [JMP App](#jmp-app)[](#jmp-app "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Combine Windows](#combine-windows)[](#combine-windows "Click to copy url")

**Syntax:** obj \<\< Combine Windows( {list of reports or data tables}, {...} )

**Description:** Combine the given list of platform reports or data tables into a new module. The application must not be currently running or in an edit state.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dist = Distribution(
    Continuous Distribution( Column( :weight ) ),
    Nominal Distribution( Column( :age ) )
);
biv = Bivariate( Y( :weight ), X( :height ) );
app = JMP App();
app << Set Name( "Instant App" );
app << Combine Windows( {dist << Report, biv << Report} );
(app << Get Modules)[1] << Set Window Title( "My Report" );
app << Run;
```

### [Debug](#debug)[](#debug "Click to copy url")

**Syntax:** obj \<\< Debug

**Description:** Run the application in the debugger.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Launcher with Report.jmpappsource" );
app << Debug;
```

### [Edit](#edit)[](#edit "Click to copy url")

**Syntax:** obj \<\< Edit

**Description:** Edit the application or dashboard in the builder.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Edit;
```

### [Get Modules](#get-modules)[](#get-modules "Click to copy url")

**Syntax:** list = obj \<\< Get Modules

**Description:** Get a list of the modules defined in the application.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Edit Application;
app << Get Modules();
```

### [Get Namespace](#get-namespace)[](#get-namespace "Click to copy url")

**Syntax:** obj \<\< Get Namespace

**Description:** Get the namespace for the module instance.

``` jsl
app = JMP App();
(app << Get Namespace) << Show Contents;
```

### [Get Windows](#get-windows)[](#get-windows "Click to copy url")

**Syntax:** obj \<\< Get Windows

**Description:** Returns a list of open windows created as instances of application modules. Note that other windows created by application scripts, using New Window() or other functions, will not be included.

**JMP Version Added:** 14

**Example 1**

``` jsl
app = JMP App();
Open( "$SAMPLE_DATA/Quality Control/Steam Turbine Historical.jmp" );
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Run;
app << Get Windows();
```

**Example 2**

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Graph Launcher.jmpappsource" );
app << Run;
launcher = (app << Get Windows())[1];
launcher[Button Box( 1 )] << Click;
launcher[Button Box( 1 )] << Click;
app << Get Windows();
```

### [Open File](#open-file)[](#open-file "Click to copy url")

**Syntax:** obj \<\< Open File( \<path\> )

**Description:** Load the application from the given file.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
box = app << Edit Application;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Relaunches the Dashboard or Application, creating a new running copy of the Application.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Edit;
app << Relaunch Analysis;
```

### [Run](#run)[](#run "Click to copy url")

**Syntax:** obj \<\< Run

**Description:** Run the application or dashboard.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Run;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Save a New Window() script

``` jsl
app = Include( "$SAMPLE_DASHBOARDS/Six Quality Graphs Dashboard.jmpappsource" );
app << Run;
app << Save Script for All Objects;
```

### [Save Script to Add-In](#save-script-to-add-in)[](#save-script-to-add-in "Click to copy url")

**Syntax:** obj \<\< Save Script to Add-In

**Description:** Create a script (JSL) to produce this analysis, and load it into the Add-in Builder

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Edit;
app << "Save Script to Add-In";
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** app \<\< Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Edit;
app << Save Script to Data Table;
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Edit;
app << Save Script to Journal;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Edit;
app << Save Script to Script Window;
```

[ Previous](JMP%20App%20Module.html "JMP App Module") [Next ](JMP%20Live%20Connection.html "JMP Live Connection")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
