# MATLAB

*Source: [https://jsl.jmp.com/All%20Categories/Functions/MATLAB.html](https://jsl.jmp.com/All%20Categories/Functions/MATLAB.html)*

---

# [MATLAB](#matlab)[](#matlab "Click to copy url")

### [Check MATLAB Dependencies](#check-matlab-dependencies)[](#check-matlab-dependencies "Click to copy url")

**Syntax:** Check MATLAB Dependencies()

**Description:** Checks if MATLAB dependencies are installed.

**JMP Version Added:** Before version 14

``` jsl

If( !Check MATLAB Dependencies(),
    Install MATLAB Dependencies();
    Print( "Dependencies are installed" );
,
    Print( "Dependencies are installed" )
);
```

### [Install MATLAB Dependencies](#install-matlab-dependencies)[](#install-matlab-dependencies "Click to copy url")

**Syntax:** Install MATLAB Dependencies(\<Patch(0\|1)\>)

**Description:** Installs the required MATLAB dependencies.

**JMP Version Added:** Before version 14

``` jsl

If( !Check MATLAB Dependencies(),
    Install MATLAB Dependencies(),
    Print( "Dependencies are installed" )
);
```

### [MATLAB Connect](#matlab-connect)[](#matlab-connect "Click to copy url")

**Syntax:** MATLABConnection = MATLAB Connect(\<Echo(0\|1)\>)

**Description:** Returns a MATLAB connection scriptable object.

**JMP Version Added:** Before version 14

``` jsl
MATLABConnection = MATLAB Connect();
x = MatlabConnection << Is Connected;
Show( x );
```

### [MATLAB Control](#matlab-control)[](#matlab-control "Click to copy url")

**Syntax:** MATLAB Control( Echo(bool) )

**Description:** Changes the control options for MATLAB.

**JMP Version Added:** Before version 14

``` jsl

MATLAB Init( Echo( true ) );
MATLAB Control( Echo( false ) );
MATLAB Submit(
    "\[
    v = [9 8 7, 6 5 4, 3 2 1];
    m = [1 2 3, 4 5 6, 7 8 9];
    rowjoin = [v ; m]
    coljoin = [v , m]
]\"
);
MATLAB Term();
```

### [MATLAB Execute](#matlab-execute)[](#matlab-execute "Click to copy url")

**Syntax:** MATLAB Execute( { list of Inputs }, { list of Outputs }, statements, \<Echo(0\|1)\>, \<Expand(0\|1)\> )

**Description:** Sends a list of inputs, executes statements and returns a list of outputs.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
a = "abcdef";
d = 3.141;
v = [9 8 7, 6 5 4, 3 2 1];
m = [1 2 3, 4 5 6, 7 8 9];
ml = MATLAB Execute(
    {v, m, a, d},
    {x, z, a, d},
    "\[
a = v * m; % matrix product
d = v / m; % = v * inv(m) called Right division
z = m \ v; % = m * inv(v) called Left division
x = m .* v; % element-wise product
]\"
);
Show( v, m, ml, x, z, a, d );
MATLAB Term();
```

### [MATLAB Get](#matlab-get)[](#matlab-get "Click to copy url")

**Syntax:** y = MATLAB Get( name )

**Description:** Returns data from MATLAB, where the name argument can represent any of the following MATLAB data types ( numeric \| string \| matrix \| list \| data frame).

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
x1 = [1, 2, 3];
MATLAB Send( x1 );
x2 = MATLAB Get( x1 );
Show( x1, x2 );
dt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
MATLAB Send( dt1 );
dt2 = MATLAB Get( dt1 );
dt2 << New Data View;
Close( dt1 );
MATLAB Term();
```

### [MATLAB Get Graphics](#matlab-get-graphics)[](#matlab-get-graphics "Click to copy url")

**Syntax:** MATLAB graphics = MATLAB Get Graphics( format )

**Description:** Returns the last graphics object written to the MATLAB graph display window in a graphics format specified by the format argument.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
ml = MATLAB Submit( "\[
plot(1:10)
]\" );
plot = MATLAB Get Graphics( png );
pngJMP = New Window( "Plot", Picture Box( plot ) );
pngJMP << Close Window;
MATLAB Submit( "close" );//Needed this command to close the figure generated from Matlab
MATLAB Term();
```

### [MATLAB Get Version](#matlab-get-version)[](#matlab-get-version "Click to copy url")

**Syntax:** version = MATLAB Get Version()

**Description:** Returns the version number of MATLAB being used with the JMP MATLAB interfaces.

**JMP Version Added:** 14

``` jsl
MATLAB Init();
version = MATLAB Get Version();
Show( version );
MATLAB Term();
```

### [MATLAB Init](#matlab-init)[](#matlab-init "Click to copy url")

**Syntax:** MATLAB Init(\<Echo(0\|1)\>)

**Description:** Initializes the MATLAB Interfaces.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
MATLAB Submit( "\[
str = 'The quick brown fox jumps over the lazy dog';
]\" );
getStr = MATLAB Get( str );
Show( getStr );
MATLAB Term();
```

### [MATLAB Is Connected](#matlab-is-connected)[](#matlab-is-connected "Click to copy url")

**Syntax:** connected = MATLAB Is Connected()

**Description:** Returns 1 if there is an active MATLAB connection; otherwise, returns 0.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
x = MATLAB Is Connected();
Show( x );
MATLAB Term();
```

### [MATLAB JMP Name to MATLAB Name](#matlab-jmp-name-to-matlab-name)[](#matlab-jmp-name-to-matlab-name "Click to copy url")

**Syntax:** MATLAB name = MATLAB JMP Name To MATLAB Name( JMP name )

**Description:** Maps a JMP variable name to a MATLAB variable name using MATLAB variable naming rules.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
MATLAB name = MATLAB JMP Name to MATLAB Name( a b c );
Show( MATLAB name );
MATLAB Term();
```

### [MATLAB Load](#matlab-load)[](#matlab-load "Click to copy url")

**Syntax:** MATLAB Load( path )

**Description:** Loads variables into MATLAB from a .mat file and returns the variables to a JSL associative array.

**JMP Version Added:** 19

``` jsl
MATLAB Init();
// if .mat file contained: x = 40; y = 'hello';
vars = MATLAB Load( "path/to/.mat" );
Show( vars << Get Value( "x" ), vars << Get Value( "y" ) );
MATLAB Term();
```

### [MATLAB Send](#matlab-send)[](#matlab-send "Click to copy url")

**Syntax:** MATLAB Send( name, \<MATLAB Name( name )\>, \<Named Arguments\> )

**Description:** Sends data to MATLAB, where the name argument can represent any of the following JMP data types ( numeric \| string \| matrix \| list \| data table).

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
x = [1, 2, 3];
MATLAB Send( x );
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
MATLAB Send( dt );
Close( dt );
MATLAB Submit( "x" );
MATLAB Submit( "dt" );
MATLAB Term();
```

### [MATLAB Send File](#matlab-send-file)[](#matlab-send-file "Click to copy url")

**Syntax:** MATLAB Send File( filename, \<MATLAB Name( name )\> )

**Description:** Sends a data file to MATLAB, where the filename argument is a string that specifies a path name to the file to be sent to MATLAB.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
MATLAB Send File( "$SAMPLE_DATA/Big Class.jmp" );
MATLAB Send File( "$SAMPLE_DATA/Baseball.jmp" );
MATLAB Submit( "BigClass" );
MATLAB Submit( "Baseball" );
MATLAB Term();
```

### [MATLAB Submit](#matlab-submit)[](#matlab-submit "Click to copy url")

**Syntax:** MATLAB Submit( statements, \<Echo(0\|1)\>, \<Expand(0\|1)\> )

**Description:** Submit statements to MATLAB. Statements can be in the form of a string value or list of string values.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
MATLAB Submit( "\[
str = 'The quick brown fox jumps over the lazy dog';
a = 200;
]\" );
getStr = MATLAB Get( str );
getNum = MATLAB Get( a );
Show( getStr, getNum );
MATLAB Term();
```

### [MATLAB Submit File](#matlab-submit-file)[](#matlab-submit-file "Click to copy url")

**Syntax:** MATLAB Submit File( path, \<Echo(0\|1)\>, \<Expand(0\|1)\> )

**Description:** Submits statements to MATLAB using a file specified by the path argument.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
MATLAB Submit File( "file containing MATLAB source.m" );
MATLAB Term();
```

### [MATLAB Term](#matlab-term)[](#matlab-term "Click to copy url")

**Syntax:** MATLAB Term()

**Description:** Terminates the MATLAB interfaces.

**JMP Version Added:** Before version 14

``` jsl
MATLAB Init();
MATLAB Submit( "\[
str = 'The quick brown fox jumps over the lazy dog';
]\" );
getStr = MATLAB Get( str );
Show( getStr );
MATLAB Term();
```

### [Update MATLAB Dependencies](#update-matlab-dependencies)[](#update-matlab-dependencies "Click to copy url")

**Syntax:** Update MATLAB Dependencies(\<Patch(0\|1)\>)

**Description:** Updates the required MATLAB dependencies.

**JMP Version Added:** Before version 14

``` jsl

If( Check MATLAB Dependencies(),
    Update MATLAB Dependencies(),
    Print( "Dependencies are updated" )
);
```

[ Previous](List.html "List") [Next ](Matrix.html "Matrix")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
