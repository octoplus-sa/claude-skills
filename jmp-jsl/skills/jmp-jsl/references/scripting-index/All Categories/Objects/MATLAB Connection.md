# MATLAB Connection

*Source: [https://jsl.jmp.com/All%20Categories/Objects/MATLAB%20Connection.html](https://jsl.jmp.com/All%20Categories/Objects/MATLAB%20Connection.html)*

---

# [MATLAB Connection](#matlab-connection)[](#matlab-connection "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Control](#control)[](#control "Click to copy url")

**Syntax:** obj \<\< Control(\<Echo(Boolean)\>)

**Description:** Controls the execution of MATLAB.

``` jsl

conn = MATLAB Connect();
conn << Control( Echo( 0 ) );
conn << Submit( "\[ a = 'hello'; ]\" ); // no echo
conn << Control( Echo( 1 ) );
conn << Submit( "\[ a = 'hello'; ]\" ); // echo
```

### [Disconnect](#disconnect)[](#disconnect "Click to copy url")

**Syntax:** obj \<\< Disconnect

**Description:** Terminates the MATLAB interfaces.

``` jsl
MATLABConnection = MATLAB Connect();
MATLABConnection << Disconnect;
```

### [Execute](#execute)[](#execute "Click to copy url")

**Syntax:** obj \<\< Execute( { list of Inputs }, { list of Outputs }, statements, \<Echo(0\|1)\>, \<Expand(0\|1)\> )

**Description:** Sends a list of inputs, executes statements, and returns a list of outputs. Optional echo() parameter defaults to True. The echo parameter controls echoing the MATLAB source to the log. Logical True (1) enables echo of source while 0 suppresses the echo to the log.

``` jsl
MATLABConnection = MATLAB Connect();
a = "abcdef";
d = 3.141;
v = [9 8 7, 6 5 4, 3 2 1];
m = [1 2 3, 4 5 6, 7 8 9];
MATLABConnection << Execute(
    {v, m, a, d},
    {x, z, a, d},
    "\[
a = v * m; % matrix product
d = v / m; % = v * inv(m) called Right division
z = m \ v; % = m * inv(v)   called Left division
x = m .* v; % element-wise product
]\"
);
Show( v, m, x, z, a, d );
MATLABConnection << Disconnect;
```

### [Get](#get)[](#get "Click to copy url")

**Syntax:** y = obj \<\< Get( name )

**Description:** Returns data from MATLAB, where the name argument can represent any of the following MATLAB data types ( numeric \| string \| matrix \| list \| data frame).

``` jsl
MATLABConnection = MATLAB Connect();
x1 = [1, 2, 3];
MATLABConnection << Set( x1 );
x2 = MATLABConnection << Get( x1 );
Show( x1, x2 );
dt1 = Open( "$SAMPLE_DATA/Big Class.jmp" );
MATLABConnection << Set( dt1 );
dt2 = MATLABConnection << Get( dt1 );
dt2 << New Data View;
Close( dt1 );
MATLABConnection << Disconnect;
```

### [Get Graphics](#get-graphics)[](#get-graphics "Click to copy url")

**Syntax:** MATLAB graphics = obj \<\< Get Graphics( format )

**Description:** Returns the last graphics object written to the MATLAB graph display window in a graphics format specified by the format argument.

``` jsl
MATLABConnection = MATLAB Connect();
ml = MATLABConnection << Submit( "\[
x = 0:pi/100:2*pi;
y = sin(x);
plot(x,y)
]\" );
plot = MATLABConnection << Get Graphics( png );
New Window( "Plot", Picture Box( plot ) );
MATLABConnection << Disconnect;
```

### [Get Version](#get-version)[](#get-version "Click to copy url")

**Syntax:** version = obj \<\< Get Version

**Description:** Returns the version number of MATLAB used in the current connection.

``` jsl
MATLABConnection = MATLAB Connect();
version = MATLABConnection << Get Version;
Show( version );
MATLABConnection << Disconnect;
```

### [Is Connected](#is-connected)[](#is-connected "Click to copy url")

**Syntax:** x = obj \<\< Is Connected

**Description:** Returns 1 if there is an active MATLAB connection; otherwise, returns 0.

``` jsl
MATLABConnection = MATLAB Connect();
x = MATLABConnection << Is Connected;
Show( x );
MATLABConnection << Disconnect;
```

### [JMP Name To MATLAB Name](#jmp-name-to-matlab-name)[](#jmp-name-to-matlab-name "Click to copy url")

**Syntax:** obj \<\< JMP Name To MATLAB Name( JMP name )

**Description:** Maps a JMP variable name to a MATLAB variable name using MATLAB variable naming rules.

``` jsl
MATLABConnection = MATLAB Connect();
MATLAB Name = MATLABConnection << JMP Name To MATLAB Name( a b c );
Show( MATLAB Name );
MATLABConnection << Disconnect;
```

### [Load](#load)[](#load "Click to copy url")

**Syntax:** obj \<\< Load( path )

**Description:** Loads a ".mat" file into MATLAB and returns the variables to a JSL associative array.

``` jsl
MATLABConnection = MATLAB Connect();
// .mat file has x, y variables with values
vars = MATLABConnection << Load( "path/to/matfile.mat" );
Show( vars << Get Value( "x" ), vars << Get Value( "y" ) );
MATLABConnection << Disconnect;
```

### [Send](#send)[](#send "Click to copy url")

**Syntax:** y = obj \<\< Send( name, \<Named Arguments\> )

**Description:** Sends data to MATLAB, where the name argument can represent any of the following JMP data types ( numeric \| string \| matrix \| list \| data table).

``` jsl
MATLABConnection = MATLAB Connect();
x = [1, 2, 3];
MATLABConnection << Send( x );
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
MATLABConnection << Send( dt );
Close( dt );
MATLABConnection << Submit( "x" );
MATLABConnection << Submit( "dt" );
MATLABConnection << Disconnect;
```

### [Send File](#send-file)[](#send-file "Click to copy url")

**Syntax:** y = obj \<\< Send File( filename, \<MATLAB Name ( name )\> )

**Description:** Sends a data file to MATLAB, where the filename argument is a string that specifies a path name to the file to be sent to MATLAB.

``` jsl
MATLABConnection = MATLAB Connect();
MATLABConnection << Send File( "$SAMPLE_DATA/Big Class.jmp" );
dtname = "$SAMPLE_DATA/Baseball.jmp";
MATLABConnection << Send File( dtname );
MATLABConnection << Submit( "BigClass" );
MATLABConnection << Submit( "Baseball" );
MATLABConnection << Disconnect;
```

### [Set](#set)[](#set "Click to copy url")

**Syntax:** y = obj \<\< Set( name, \<MATLAB Name ( name )\> )

**Description:** Sends data to MATLAB, where the name argument can represent any of the following JMP data types ( numeric \| string \| matrix \| list \| data table).

``` jsl
MATLABConnection = MATLAB Connect();
x = [1, 2, 3];
MATLABConnection << Set( x );
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
MATLABConnection << Set( dt );
Close( dt );
MATLABConnection << Submit( "x" );
MATLABConnection << Submit( "dt" );
MATLABConnection << Disconnect;
```

### [Submit](#submit)[](#submit "Click to copy url")

**Syntax:** obj \<\< Submit( statements )

**Description:** Submit statements to MATLAB. Statements can be in the form of a string value or a list of string values.

``` jsl
MATLABConnection = MATLAB Connect();
MATLABConnection << Submit(
    "\[
str = 'The quick brown fox jumps over the lazy dog';
a = 200;
]\"
);
getStr = MATLABConnection << Get( str );
getNum = MATLABConnection << Get( a );
Show( getStr, getNum );
MATLABConnection << Disconnect;
```

### [Submit File](#submit-file)[](#submit-file "Click to copy url")

**Syntax:** obj \<\< Submit File( path )

**Description:** Submits statements to MATLAB using a file specified by the path argument.

``` jsl
MATLABConnection = MATLAB Connect();
MATLABConnection << Submit File( "file containing MATLAB source." );
MATLABConnection << Disconnect;
```

[ Previous](Loading%20Bar%20Plot.html "Loading Bar Plot") [Next ](Make%20Validation%20Column.html "Make Validation Column")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
