# DLLScriptable

*Source: [https://jsl.jmp.com/All%20Categories/Objects/DLLScriptable.html](https://jsl.jmp.com/All%20Categories/Objects/DLLScriptable.html)*

---

# [DLLScriptable](#dllscriptable)[](#dllscriptable "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Load DLL](#load-dll)[](#load-dll "Click to copy url")

**Syntax:** dll = Load DLL( file path \| Base Name( file path without extension ), \< AutoDeclare( bool \| Quiet \| Verbose) \| Quiet \| Verbose )\> )

**Description:** Loads a DLL pointed to by the specified path.

``` jsl
If( Host is( "Windows" ),
    dll = Load DLL( "C:/Windows/System32/User32.DLL" );
    dll << CallDLL( "MessageBeep", "n", 0 );
    Wait( 1 );
    dll << CallDLL( "MessageBeep", "n", 0 );
    dll << UnloadDLL();
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Call DLL](#call-dll)[](#call-dll "Click to copy url")

**Syntax:** obj \<\< Call DLL( function name, signature, args )

**Description:** Calls a specified function within the DLL, with a given signature and arguments.

``` jsl
If( Host is( "Windows" ),
    dll = Load DLL( "C:/Windows/System32/User32.DLL" );
    dll << CallDLL( "MessageBeep", "n", 0 );
    Wait( 1 );
    dll << CallDLL( "MessageBeep", "n", 0 );
    dll << UnloadDLL();
);
```

### [Declare Function](#declare-function)[](#declare-function "Click to copy url")

**Syntax:** obj \<\< Declare Function( name, Convention( STDCALL\| CDECL\| Pascal ), Alias( string ), Arg( Int8\| UInt8\| Int16\| UInt16\| Int32\| UInt32\| Int64\| UInt64\| Float\| Double\| AnsiString\| UnicodeString\| Struct\| IntPtr\| UIntPtr\| ObjPtr, string ), Returns( type ); )

**Description:** Declares the return type and parameter types of a function defined in the DLL so that it can be successfully invoked from JSL.

``` jsl
If( Host is( "Windows" ),
    dll = Load DLL( "C:/Windows/System32/User32.DLL" );
    dll << DeclareFunction(
        "MessageBoxW",
        Convention( STDCALL ),
        Alias( "MsgBox" ),
        Arg( IntPtr, "hWnd" ),
        Arg( UnicodeString, "message" ),
        Arg( UnicodeString, "caption" ),
        Arg( UInt32, "uType" ),
        Returns( Int32 )
    );
    result = dll << MsgBox( 0, "Here is a message from JMP.", "Call DLL", 321 );
    Show( result );
);
```

### [Get Declaration JSL](#get-declaration-jsl)[](#get-declaration-jsl "Click to copy url")

**Syntax:** obj \<\< Get Declaration JSL

**Description:** Retrieves the declaration JSL from the DLL and displays it in the log. This message applies only to DLLs that contain the function, \_JMP_Declarations().

``` jsl
dll = Load DLL( /*DLL with JSL keyword*/ ); 
//dll << Get Declaration JSL;
```

### [Show Functions](#show-functions)[](#show-functions "Click to copy url")

**Syntax:** obj \<\< Show Functions

**Description:** Stream the list of declared functions to the log

``` jsl
If( Host is( "Windows" ),
    dll = Load DLL( "C:/Windows/System32/User32.DLL" );
    dll << DeclareFunction(
        "MessageBoxW",
        Convention( STDCALL ),
        Alias( "MsgBox" ),
        Arg( IntPtr, "hWnd" ),
        Arg( UnicodeString, "message" ),
        Arg( UnicodeString, "caption" ),
        Arg( UInt32, "uType" ),
        Returns( Int32 )
    );
    dll << Show Functions;
);
```

### [Unload DLL](#unload-dll)[](#unload-dll "Click to copy url")

**Syntax:** obj \<\< Unload DLL

**Description:** Unloads the DLL.

``` jsl
If( Host is( "Windows" ),
    dll = Load DLL( "C:/Windows/System32/User32.DLL" );
    dll << CallDLL( "MessageBeep", "n", 0 );
    Wait( 1 );
    dll << CallDLL( "MessageBeep", "n", 0 );
    dll << UnloadDLL();
);
```

[ Previous](Custom%20Profiler.html "Custom Profiler") [Next ](DOE.html "DOE")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
