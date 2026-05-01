# Run Program

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Run%20Program.html](https://jsl.jmp.com/All%20Categories/Objects/Run%20Program.html)*

---

# [Run Program](#run-program)[](#run-program "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Run Program](#run-program_1)[](#run-program_1 "Click to copy url")

**Syntax:** obj = Run Program( Executable( "path/etc.exe" ), \< Options( {"/a", "/b etc" } ) \>, \< Parameter( optParm ) \>, \< Read Function( Function( {this, optParm}, etc ) \| "text" \| "blob" ) \>, \< Write Function( Function( {this, optParm}, etc ) ) \> )

**Description:** Control an external program using stdin and stdout.

``` jsl
RP = Run Program(
    Executable( "PING.EXE"/*path probably not needed*/ ),
    Options( {"-n 5", "localhost"} ),
    ReadFunction( Function( {this}, Write( this << read ) ) )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Can Read](#can-read)[](#can-read "Click to copy url")

**Syntax:** bool = obj \<\< Can Read

**Description:** Returns 1 if the RunProgram object can be read from and 0 if not.

``` jsl

value = "";
rp = Run Program( Executable( "ping.exe" ), Options( {"-n 5", "localhost"} ) );
While( !(rp << Is Read EOF), If( rp << Can Read, value ||= rp << Read, Wait( 0.01 ) ) );
Show( value );
```

### [Can Write](#can-write)[](#can-write "Click to copy url")

**Syntax:** bool = obj \<\< Can Write

**Description:** Returns boolean for whether or not the RunProgram object can be written to via standard input.

### [Is Read EOF](#is-read-eof)[](#is-read-eof "Click to copy url")

**Syntax:** bool = obj \<\< Is Read EOF

**Description:** Returns 1 if the program has finished writing to standard output and 0 if not.

``` jsl

value = "";
rp = Run Program( Executable( "ping.exe" ), Options( {"-n 5", "localhost"} ) );
While( !(rp << Is Read EOF), If( rp << Can Read, value ||= rp << Read, Wait( 0.01 ) ) );
Show( value );
```

### [Read](#read)[](#read "Click to copy url")

**Syntax:** value = obj \<\< Read( \< "blob" \> )

**Description:** Read standard output from executable as text or blob.

``` jsl

value = "";
rp = Run Program(
    Executable( "ping.exe" ),
    Options( {"-n 5", "localhost"} ),
    ReadFunction(
        Function( {this},
            value ||= this << read;
            Show( value );
        )
    )
);
```

### [Write](#write)[](#write "Click to copy url")

**Syntax:** obj \<\< Write( string )

**Description:** Write text to the program's standard input.

### [Write EOF](#write-eof)[](#write-eof "Click to copy url")

**Syntax:** obj \<\< Write EOF

**Description:** Write the end of file for the RunProgram object.

[ Previous](Response%20Screening.html "Response Screening") [Next ](SAS%20Cloud%20Analytic%20Services%20%28CAS%29.html "SAS Cloud Analytic Services (CAS)")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
