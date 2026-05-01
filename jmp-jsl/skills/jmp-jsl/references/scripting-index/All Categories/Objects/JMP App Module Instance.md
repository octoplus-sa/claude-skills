# JMP App Module Instance

*Source: [https://jsl.jmp.com/All%20Categories/Objects/JMP%20App%20Module%20Instance.html](https://jsl.jmp.com/All%20Categories/Objects/JMP%20App%20Module%20Instance.html)*

---

# [JMP App Module Instance](#jmp-app-module-instance)[](#jmp-app-module-instance "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Create Objects](#create-objects)[](#create-objects "Click to copy url")

**Syntax:** obj \<\< Create Objects

**Description:** Create the objects of the module instance. This can be called only within the script for a JMP App Module.

``` jsl
// This command is only valid within a JMP App Module Script
```

### [Get Box](#get-box)[](#get-box "Click to copy url")

**Syntax:** obj \<\< Get Box

**Description:** Get the display box for the module instance.

``` jsl
app = JMP App();
app << Open File( "$SAMPLE_APPS/Instant App.jmpappsource" );
app << Run Application;
modules = app << Get Modules;
inst = modules[1] << Create Instance;
inst << Get Box;
```

### [Get Namespace](#get-namespace)[](#get-namespace "Click to copy url")

**Syntax:** obj \<\< Get Namespace

**Description:** Get the namespace for the module instance.

``` jsl
app = JMP App();
(app << Get Namespace) << Show Contents;
```

### [Get User Data](#get-user-data)[](#get-user-data "Click to copy url")

**Syntax:** obj \<\< Get User Data

**Description:** Returns the user data associated with the module instance.

``` jsl
// This command is only valid within a JMP App Module Script
```

### [Set User Data](#set-user-data)[](#set-user-data "Click to copy url")

**Syntax:** inst \<\< Set User Data(expr)

**Description:** Stores a JSL value in the JMP app module instance; the value could be a number, string, list, associative array, or other JSL type.

``` jsl
// This command is only valid within a JMP App Module Script
```

[ Previous](Item%20Analysis.html "Item Analysis") [Next ](JMP%20App%20Module.html "JMP App Module")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
