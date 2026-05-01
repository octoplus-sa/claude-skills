# SAS

*Source: [https://jsl.jmp.com/All%20Categories/Functions/SAS.html](https://jsl.jmp.com/All%20Categories/Functions/SAS.html)*

---

# [SAS](#sas)[](#sas "Click to copy url")

### [As C Expr](#as-c-expr)[](#as-c-expr "Click to copy url")

**Syntax:** y = As C Expr( x )

**Description:** Returns an equivalent expression in the C programming language.

**JMP Version Added:** Before version 14

``` jsl
As C Expr( Expr( Match( sex, 1, "Male", 2, "Female", "Other" ) ) );
```

### [As JSON Expr](#as-json-expr)[](#as-json-expr "Click to copy url")

**Syntax:** y = As JSON Expr( x )

**Description:** Returns a JSON (JavaScript Object Notation) representation of the expression.

**JMP Version Added:** Before version 14

``` jsl
As JSON Expr( Expr( Match( sex, 1, "Male", 2, "Female", "Other" ) ) );
```

### [As JavaScript Expr](#as-javascript-expr)[](#as-javascript-expr "Click to copy url")

**Syntax:** y = As JavaScript Expr( x )

**Description:** Returns an equivalent expression in the JavaScript programming language.

**JMP Version Added:** Before version 14

``` jsl
As JavaScript Expr( Expr( Match( sex, 1, "Male", 2, "Female", "Other" ) ) );
```

### [As Python Expr](#as-python-expr)[](#as-python-expr "Click to copy url")

**Syntax:** y = As Python Expr( x )

**Description:** Returns an equivalent expression in the Python programming language.

**JMP Version Added:** Before version 14

``` jsl
As Python Expr( Expr( Match( sex, 1, "Male", 2, "Female", "Other" ) ) );
```

### [As SAS Expr](#as-sas-expr)[](#as-sas-expr "Click to copy url")

**Syntax:** y = As SAS Expr( x )

**Description:** Returns a version of the expression more suitable for a SAS DATA step. The code must be wrapped in a PROC DS2 call.

**JMP Version Added:** Before version 14

``` jsl
As SAS Expr( Expr( Match( sex, 1, "Male", 2, "Female", "Other" ) ) );
```

### [SAS Name](#sas-name)[](#sas-name "Click to copy url")

**Syntax:** sasName = SAS Name( string\|namelist )

**Description:** Converts JMP variable names to a string containing valid SAS variable names by changing special characters and blanks to underscores. The argument can be specified as a string or a list of strings.

**JMP Version Added:** Before version 14

``` jsl
SAS Name( {"x 1", "x 2"} );
```

### [SAS Open For Var Names](#sas-open-for-var-names)[](#sas-open-for-var-names "Click to copy url")

**Syntax:** nameList = SAS Open For Var Names( path )

**Description:** Returns a list of variable names from a SAS data set.

**JMP Version Added:** Before version 14

``` jsl
SAS Open For Var Names( "C:\my data\somedata.sas7bdat" );
```

[ Previous](Row.html "Row") [Next ](SQL.html "SQL")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
