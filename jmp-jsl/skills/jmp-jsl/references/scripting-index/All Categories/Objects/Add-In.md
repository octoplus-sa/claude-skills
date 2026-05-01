# Add-In

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Add-In.html](https://jsl.jmp.com/All%20Categories/Objects/Add-In.html)*

---

# [Add-In](#add-in)[](#add-in "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Auto Load](#auto-load)[](#auto-load "Click to copy url")

**Syntax:** addin \<\< Auto Load( boolean )

**Description:** Sets whether or not an add-in should be automatically loaded during JMP's startup process.

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << Auto Load( 1 ),
    Print( "Add-In ID Not Found" )
);
```

### [Display Name](#display-name)[](#display-name "Click to copy url")

**Syntax:** name = addin \<\< Display Name

**Description:** Returns the display name for an add-in.

**Example 1**

``` jsl
addins = Get Addins();
addins << Display Name();
```

**Example 2**

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << Display Name(),
    Print( "Add-In ID Not Found" )
);
```

### [Home Folder](#home-folder)[](#home-folder "Click to copy url")

**Syntax:** folder = addin \<\< Home Folder

**Description:** Returns the home folder for an add-in.

**Example 1**

``` jsl
addins = Get Addins();
addins << Home Folder();
```

**Example 2**

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << Home Folder(),
    Print( "Add-In ID Not Found" )
);
```

### [ID](#id)[](#id "Click to copy url")

**Syntax:** id = addin \<\< ID

**Description:** Returns the unique ID for an add-in.

**Example 1**

``` jsl
addins = Get Addins();
addins << ID();
```

**Example 2**

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << ID(),
    Print( "Add-In ID Not Found" )
);
```

### [Is Loaded](#is-loaded)[](#is-loaded "Click to copy url")

**Syntax:** x = addin \<\< Is Loaded

**Description:** Returns whether or not an add-in is currently loaded.

**Example 1**

``` jsl
addins = Get Addins();
addins << Is Loaded();
```

**Example 2**

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << Is Loaded(),
    Print( "Add-In ID Not Found" )
);
```

### [Load](#load)[](#load "Click to copy url")

**Syntax:** addin \<\< Load

**Description:** Loads an add-in.

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << Load(),
    Print( "Add-In ID Not Found" )
);
```

### [Unload](#unload)[](#unload "Click to copy url")

**Syntax:** addin \<\< Unload

**Description:** Unloads an add-in.

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << Unload(),
    Print( "Add-In ID Not Found" )
);
```

### [Version](#version)[](#version "Click to copy url")

**Syntax:** ver = addin \<\< Version

**Description:** Returns the version number for an add-in.

**Example 1**

``` jsl
addins = Get Addins();
addins << Version();
```

**Example 2**

``` jsl
addin = Get Addin( "com.mycompany.myaddin" );
If( !Is Missing( addin ),
    addin << Version(),
    Print( "Add-In ID Not Found" )
);
```

[ Previous](../Functions/Utility.html "Utility") [Next ](Alpha%20Shape.html "Alpha Shape")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
