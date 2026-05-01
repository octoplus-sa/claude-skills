# Class

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Class.html](https://jsl.jmp.com/All%20Categories/Objects/Class.html)*

---

# [Class](#class)[](#class "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Define Class](#define-class)[](#define-class "Click to copy url")

**Syntax:** Define Class("class name", \<Base Class{ "base class name", ... }\>, \<Show( All( boolean ) \| ( Members( boolean ) \| Methods( boolean ) \| Functions( boolean ) )+ )\>, { method *\| member* \| function\* } )

**Description:** Creates a class where all class methods and class variables created are defined only within the specified class name.

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Clone](#clone)[](#clone "Click to copy url")

**Syntax:** obj \<\< Clone

**Description:** Clone the contents of a class reference making a new object

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
nclref = clref << Clone;
Show( clref << Equal( nclref ) );
Show( clref == nclref );
```

### [Contains](#contains)[](#contains "Click to copy url")

**Syntax:** obj \<\< Contains( string )

**Description:** Returns a 1 if the class contains the specified string expression, or a 0 otherwise.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << Contains( "nObs" );
```

### [Delete Class](#delete-class)[](#delete-class "Click to copy url")

**Syntax:** clref \<\< Delete Class( \< Force( boolean ) \> )

**Description:** Deletes this class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
clref << Delete Class;
Show( clref );
```

### [Equal](#equal)[](#equal "Click to copy url")

**Syntax:** obj \<\< Equal( classref )

**Description:** Compare the class reference argument to the target class reference for equality

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
nclref = New Object( Test() );
Show( clref << Equal( nclref ) );
nclref:nObs = 50;
Show( clref << Equal( nclref ) );
```

### [First](#first)[](#first "Click to copy url")

**Syntax:** obj \<\< First

**Description:** Returns the string expression for the first item in this class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << First;
```

### [Get Contents](#get-contents)[](#get-contents "Click to copy url")

**Syntax:** obj \<\< Get Contents

**Description:** Returns a list of items within this class. Each element is a two-item list containing a key and its associated value.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << Get Contents;
```

### [Get Keys](#get-keys)[](#get-keys "Click to copy url")

**Syntax:** obj \<\< Get Keys

**Description:** Returns a list of keys within this class. Each key is a string representation of an individual item contained in the class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << Get Keys;
```

### [Get Name](#get-name)[](#get-name "Click to copy url")

**Syntax:** obj \<\< Get Name

**Description:** Returns the name of this class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
class name = clref << Get Name;
```

### [Get Value](#get-value)[](#get-value "Click to copy url")

**Syntax:** obj \<\< Get Value( string )

**Description:** Returns the value of the specified item within this class. The "string" is the key to the item.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << Get Value( "nObs" );
```

### [Get Values](#get-values)[](#get-values "Click to copy url")

**Syntax:** obj \<\< Get Values

**Description:** Returns a list of values corresponding to each item within this class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << Get Values;
```

### [Insert](#insert)[](#insert "Click to copy url")

**Syntax:** obj \<\< Insert( string, value )

**Description:** Inserts a string expression with the specified value into this class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
clref << Insert( "X", 25 );
Show( clref );
```

### [Lock Class](#lock-class)[](#lock-class "Click to copy url")

**Syntax:** obj \<\< Lock Class( \<string, \| {string, ...}\>\* )

**Description:** Locks all method members or specified named members in this class and prevents them from being added, changed, or removed.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
clref << Lock Class;
Try( clref:nObs = 40, "clref is locked." );
```

### [N Items](#n-items)[](#n-items "Click to copy url")

**Syntax:** obj \<\< N Items

**Description:** Returns the number of items contains in this class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
n = clref << N Items;
```

### [Next](#next)[](#next "Click to copy url")

**Syntax:** obj \<\< Next( string )

**Description:** Returns the string expression for the next item following the key specified in this class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << Next( "addition" );
```

### [Remove](#remove)[](#remove "Click to copy url")

**Syntax:** obj \<\< Remove( \<string \| {string, ...}\>\* )

**Description:** Removes the specified string expression from the class.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
clref << Remove( "nObs" );
Show( clref );
```

### [Show Contents](#show-contents)[](#show-contents "Click to copy url")

**Syntax:** obj \<\< Show Contents

**Description:** Shows the contents of a class in the JMP log.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
result = clref << Show Contents;
```

### [Unlock Class](#unlock-class)[](#unlock-class "Click to copy url")

**Syntax:** obj \<\< Unlock Class( \<string \| {string, ...}\>\* )

**Description:** Unlocks a locked class containing method members that were prevented from being added, changed, or removed.

**JMP Version Added:** 14

``` jsl
Define Class(
    "Test",
    nObs = 20;
    addition = Method( {x, y},
        (x + y) * nObs
    );
    append = Method( {a, b},
        Char( a ) || " + " || Char( b )
    );
);
clref = New Object( Test() );
clref << Lock Class( "nObs" );
Try( clref:nObs = 30, Show( "clref is locked." ) ); 
//Try again after unlocking. 
clref << Unlock Class( "nObs" );
Try( clref:nObs = 40, Show( "clref is locked." ) );
```

[ Previous](Choice.html "Choice") [Next ](Cluster%20Variables.html "Cluster Variables")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
