# Data Connector Registry

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Data%20Connector%20Registry.html](https://jsl.jmp.com/All%20Categories/Objects/Data%20Connector%20Registry.html)*

---

# [Data Connector Registry](#data-connector-registry)[](#data-connector-registry "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Get](#get)[](#get "Click to copy url")

**Syntax:** Data Connector Registry() \<\< Get ( name )

**Description:** Retrieves a data connector from the registry

**JMP Version Added:** 18

``` jsl

dc = Data Connector Registry() << Get( "com.jmp.sql_server" );
```

### [Get Available](#get-available)[](#get-available "Click to copy url")

**Syntax:** Data Connector Registry() \<\< Get Available()

**Description:** Retrieves a list of available data connectors in the registry

**JMP Version Added:** 18

``` jsl

list = Data Connector Registry() << Get Available();
```

### [Get Metadata](#get-metadata)[](#get-metadata "Click to copy url")

**Syntax:** Data Connector Registry() \<\< Get Metadata ( name )

**Description:** Gets data connector metadata from the registry

**JMP Version Added:** 18

``` jsl

metadata = Data Connector Registry() << Get Metadata( "com.jmp.sql_server" );
```

### [Register](#register)[](#register "Click to copy url")

**Syntax:** Data Connector Registry() \<\< Register( Path(path), \<Name(name)\>, \<Description(Description)\> )

**Description:** Adds a data connector to the registry

**JMP Version Added:** 18

``` jsl

Data Connector Registry() << Register(
    Path( "$DOCUMENTS/my connector.jmpdc" ),
    Name( "My Data Connector" )
);
```

### [Unregister](#unregister)[](#unregister "Click to copy url")

**Syntax:** Data Connector Registry() \<\< Unregister ( name )

**Description:** Removes a data connector from the registry

**JMP Version Added:** 18

``` jsl

dc = Data Connector Registry() << Unregister( "My Data Connector" );
```

[ Previous](Data%20Connector%20Metadata.html "Data Connector Metadata") [Next ](Data%20Connector.html "Data Connector")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
