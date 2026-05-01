# Namespace

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Namespace.html](https://jsl.jmp.com/All%20Categories/Objects/Namespace.html)*

---

# [Namespace](#namespace)[](#namespace "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [New Namespace](#new-namespace)[](#new-namespace "Click to copy url")

**Syntax:** ns = New Namespace( \<name\>, \<list of expressions\> )

**Description:** Creates a namespace where all functions and variables created are defined only within the specified name.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Contains](#contains)[](#contains "Click to copy url")

**Syntax:** obj \<\< Contains( string )

**Description:** Returns a 1 if the namespace contains the specified string expression, or a 0 otherwise.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << Contains( "nObs" );
```

### [Delete Namespace](#delete-namespace)[](#delete-namespace "Click to copy url")

**Syntax:** nsref \<\< Delete Namespace( \< Force( boolean ) \> )

**Description:** Deletes this namespace.

**JMP Version Added:** 14

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
nsref << Delete Namespace;
Show( nsref );
```

### [First](#first)[](#first "Click to copy url")

**Syntax:** obj \<\< First

**Description:** Returns the string expression for the first item in this namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << First;
```

### [Get Contents](#get-contents)[](#get-contents "Click to copy url")

**Syntax:** obj \<\< Get Contents

**Description:** Returns a list of items within this namespace, where each element is a two item list containing a key and its associated value.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << Get Contents;
```

### [Get Keys](#get-keys)[](#get-keys "Click to copy url")

**Syntax:** obj \<\< Get Keys

**Description:** Returns a list of keys within this namespace, where a key is string representation of an individual item contained in the namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << Get Keys;
```

### [Get Name](#get-name)[](#get-name "Click to copy url")

**Syntax:** obj \<\< Get Name

**Description:** Returns the name of this namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
space name = nsref << Get Name;
```

### [Get Value](#get-value)[](#get-value "Click to copy url")

**Syntax:** obj \<\< Get Value( string )

**Description:** Returns the value of the specified item within this namespace. The "string" is the key to the item.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << Get Value( "nObs" );
```

### [Get Values](#get-values)[](#get-values "Click to copy url")

**Syntax:** obj \<\< Get Values

**Description:** Returns a list of values corresponding to each item within this namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << Get Values;
```

### [Insert](#insert)[](#insert "Click to copy url")

**Syntax:** obj \<\< Insert( string, value )

**Description:** Inserts a string expression, with the specified value into this namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
nsref << Insert( "X", 25 );
Show( nsref );
```

### [Lock Namespace](#lock-namespace)[](#lock-namespace "Click to copy url")

**Syntax:** obj \<\< Lock Namespace( \<string, \| {string, ...}\>\* )

**Description:** Locks all variables or specified named variables in this namespace and prevents variables from being added, changed, or removed.

**JMP Version Added:** 14

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
nsref << Lock Namespace;
Try( Add Class:nObs = 40, "Add Class is locked." );
```

### [N Items](#n-items)[](#n-items "Click to copy url")

**Syntax:** obj \<\< N Items

**Description:** Returns the number of items contains in this namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
n = nsref << N Items;
```

### [Next](#next)[](#next "Click to copy url")

**Syntax:** obj \<\< Next( string )

**Description:** Returns the string expression for the next item following the key specified in this namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << Next( "addition" );
```

### [Remove](#remove)[](#remove "Click to copy url")

**Syntax:** obj \<\< Remove( \<string \| {string, ...}\>\* )

**Description:** Removes the specified string expression from the namespace.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
nsref << Remove( "nObs" );
Show( nsref );
```

### [Show Contents](#show-contents)[](#show-contents "Click to copy url")

**Syntax:** obj \<\< Show Contents

**Description:** Shows the contents of a namespace in the JMP log.

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
result = nsref << Show Contents;
```

### [Unlock Namespace](#unlock-namespace)[](#unlock-namespace "Click to copy url")

**Syntax:** obj \<\< Unlock Namespace( \<string \| {string, ...}\>\* )

**Description:** Unlocks a previously locked namespace with all variables locked in this namespace and prevented variables from being added, changed, or removed.

**JMP Version Added:** 14

``` jsl
nsref = New Namespace(
    "Add Class"
);
Add Class:nObs = 20;
Add Class:addition = Function( {x, y}, x + y );
Add Class:append = Function( {a, b},
    Char( a ) || " + " || Char( b )
);
nsref << Lock Namespace( "nObs" );
Try( Add Class:nObs = 30, Show( "Add Class is locked." ) ); 
//Try again after unlocking. 
nsref << Unlock Namespace( "nObs" );
Try( Add Class:nObs = 40, Show( "Add Class is locked." ) );
```

[ Previous](Naive%20Bayes.html "Naive Bayes") [Next ](Neural.html "Neural")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
