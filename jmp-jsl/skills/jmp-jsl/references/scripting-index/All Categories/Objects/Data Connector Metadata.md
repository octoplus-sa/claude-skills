# Data Connector Metadata

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Data%20Connector%20Metadata.html](https://jsl.jmp.com/All%20Categories/Objects/Data%20Connector%20Metadata.html)*

---

# [Data Connector Metadata](#data-connector-metadata)[](#data-connector-metadata "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** metadata \<\< Get Description()

**Description:** Gets the data connector description

**JMP Version Added:** 18

``` jsl

description = metadata << Get Description();
```

### [Get Driver](#get-driver)[](#get-driver "Click to copy url")

**Syntax:** metadata \<\< Get Driver()

**Description:** Gets data connector driver, if there is one.

**JMP Version Added:** 18

``` jsl

type = metadata << Get Driver();
```

### [Get Name](#get-name)[](#get-name "Click to copy url")

**Syntax:** metadata \<\< Get Name()

**Description:** Gets the data connector name

**JMP Version Added:** 18

``` jsl

name = metadata << Get Name();
```

### [Get Path](#get-path)[](#get-path "Click to copy url")

**Syntax:** metadaata \<\< Get Path()

**Description:** Gets data connector path

**JMP Version Added:** 18

``` jsl

path = metadata << Get Path();
```

### [Get Type](#get-type)[](#get-type "Click to copy url")

**Syntax:** metadata \<\< Get Type()

**Description:** Gets the data connector type

**JMP Version Added:** 18

``` jsl

type = metadata << Get Type();
```

### [Set Description](#set-description)[](#set-description "Click to copy url")

**Syntax:** metadata \<\< Set Description(description)

**Description:** Sets the data connector description

**JMP Version Added:** 18

``` jsl

metadata << Set Description( "My frequently used SQL Server connection." );
```

### [Set Name](#set-name)[](#set-name "Click to copy url")

**Syntax:** metadata \<\< Set Name( name )

**Description:** Sets the data connector name

**JMP Version Added:** 18

``` jsl

metadata << Set Name( "A new Name" );
```

[ Previous](DOE.html "DOE") [Next ](Data%20Connector%20Registry.html "Data Connector Registry")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
