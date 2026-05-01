# Custom Function

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Custom%20Function.html](https://jsl.jmp.com/All%20Categories/Objects/Custom%20Function.html)*

---

# [Custom Function](#custom-function)[](#custom-function "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Custom Format Category](#custom-format-category)[](#custom-format-category "Click to copy url")

**Syntax:** f \<\< Custom Format Category(1\|0)

**Description:** Treat the custom function as a custom format. Specify 0 to exclude the function from the custom format menu.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Custom Format Category( 1 );
```

### [Description](#description)[](#description "Click to copy url")

**Syntax:** obj \<\< Description( text )

**Description:** Set the description for the custom function. This description will show up in the Scripting Index and in tooltips.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Description( "Add two numbers together, but subtract 1" );
```

### [Example](#example)[](#example "Click to copy url")

**Syntax:** f \<\< Example(example text \| Expr(example JSL code), \<example name\>)

**Description:** Add an example that shows how to effectively use the function. The example should be passed in as a text string or as JSL code wrapped with the Expr command. You can send the message multiple times to add more than one example.

**JMP Version Added:** 14

**Example 1**

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Example( "Add(1, 2)" );
```

**Example 2**

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Example( "Add(1, 2)", "small add" );
myAdd << Example( "Add(1, 500)", "bigger add" );
```

### [Formula Category](#formula-category)[](#formula-category "Click to copy url")

**Syntax:** f \<\< Formula Category(name\|""\|1\|0)

**Description:** Include the function in the specified Formula Editor category. If specified, this function will be added at the end of the matching category. If the category doesn't exist, a new category will be created. Specify 0 or empty string to not show the function in the formula editor tree.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Formula Category( "NumberStuff" );
```

### [Get Custom Format Category](#get-custom-format-category)[](#get-custom-format-category "Click to copy url")

**Syntax:** f \<\< Get Custom Format Category

**Description:** Get the custom format category for the custom function.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Custom Format Category( 1 );
myAdd << Get Custom Format Category;
```

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** f \<\< Get Description

**Description:** Get the description for the custom function.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Description( "Add two numbers together, but subtract 1" );
myAdd << Get Description;
```

### [Get Examples](#get-examples)[](#get-examples "Click to copy url")

**Syntax:** f \<\< Get Examples

**Description:** Retrieve the list of examples, as strings

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Example( "Add(1, 2)", "small add" );
myAdd << Example( "Add(1, 500)", "bigger add" );
myAdd << Get Examples;
```

### [Get Formula Category](#get-formula-category)[](#get-formula-category "Click to copy url")

**Syntax:** f \<\< Get Formula Category

**Description:** Return which Formula Editor category this function should be part of, if any.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Formula Category( "NumberStuff" );
myAdd << Get Formula Category;
```

### [Get Function](#get-function)[](#get-function "Click to copy url")

**Syntax:** f \<\< Get Function

**Description:** Retrieve the function definition.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Get Function;
```

### [Get Name](#get-name)[](#get-name "Click to copy url")

**Syntax:** f \<\< Get Name

**Description:** Retrieve the function name.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Get Name;
```

### [Get Namespace](#get-namespace)[](#get-namespace "Click to copy url")

**Syntax:** f \<\< Get Namespace

**Description:** Retrieve the function namespace.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Get Namespace;
```

### [Get Parameters](#get-parameters)[](#get-parameters "Click to copy url")

**Syntax:** f \<\< Get Parameters

**Description:** Retrieve the list of parameters.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Parameter( "Number", "number" );
myAdd << Parameter( "Number", "<number=1>" );
myAdd << Get Parameters;
```

### [Get Prototype](#get-prototype)[](#get-prototype "Click to copy url")

**Syntax:** f \<\< Get Prototype

**Description:** Get the prototype that shows up for this function in the Scripting Index

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Prototype( "Add(number, <number=1>)" );
myAdd << Get Prototype;
```

### [Get Result Type](#get-result-type)[](#get-result-type "Click to copy url")

**Syntax:** f \<\< Get Result Type

**Description:** Get the result type of the function.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Result Type( "Number" );
myAdd << Get Result Type;
```

### [Get Scripting Index Category](#get-scripting-index-category)[](#get-scripting-index-category "Click to copy url")

**Syntax:** f \<\< Get Scripting Index Category

**Description:** Get the category for the custom function in the Scripting Index.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Scripting Index Category( "My Functions" );
myAdd << Get Scripting Index Category;
```

### [Get Transform Category](#get-transform-category)[](#get-transform-category "Click to copy url")

**Syntax:** f \<\< Get Transform Category

**Description:** Get the transform category for the custom function.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Transform Category( 1 );
myAdd << Get Transform Category;
```

### [Parameter](#parameter)[](#parameter "Click to copy url")

**Syntax:** f \<\< Parameter(typename \| {typename1, typename2, ...}, hint text)

**Description:** Add information about a parameter of the function. Send this message once for each parameter the function takes. This can be used for code validation. Valid choices for the parameter types are Any, Name, Number, String, List, Matrix, RowState. If multiple result types are possible, supply the type names in a list. The hint text is used to indicate what data should be used in the corresponding argument in the formula editor. Specify an empty string if no hint text is desired.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Parameter( "Number", "number" );
myAdd << Parameter( "Number", "<number=1>" );
```

### [Prototype](#prototype)[](#prototype "Click to copy url")

**Syntax:** obj \<\< Prototype( text )

**Description:** Set the prototype that shows up for this function in the Scripting Index

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Prototype( "Add(number, <number=1>)" );
```

### [Result Type](#result-type)[](#result-type "Click to copy url")

**Syntax:** f \<\< Result Type(typename \| {typename1, typename2 ...})

**Description:** Set the result type of the function. This can be used for code validation. Valid choices are Any, Name, Number, String, List, Matrix, RowState. If multiple result types are possible, supply the type names in a list.

**JMP Version Added:** 14

**Example 1**

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Result Type( "Number" );
```

**Example 2**

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Result Type( {"Number", "String"} );
```

### [Scripting Index Category](#scripting-index-category)[](#scripting-index-category "Click to copy url")

**Syntax:** f \<\< Scripting Index Category(name\|""\|1\|0)

**Description:** Sets the category for the custom function in the Scripting Index. Every custom function will be listed in the All Functions category in addition to the category that you specify. Specify 0 or "" to list the function in the All Functions category only.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Scripting Index Category( "My Functions" );
```

### [Transform Category](#transform-category)[](#transform-category "Click to copy url")

**Syntax:** f \<\< Transform Category(1\|0)

**Description:** Treat the custom function as a column transform. Specify 0 to exclude the function from the column transform menu.

**JMP Version Added:** 14

``` jsl
myAdd = New Custom Function( "custom", "Add", Function( {x, y = 1}, x + y - 1 ) );
myAdd << Transform Category( 1 );
```

[ Previous](Cumulative%20Damage.html "Cumulative Damage") [Next ](Custom%20Graph.html "Custom Graph")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
