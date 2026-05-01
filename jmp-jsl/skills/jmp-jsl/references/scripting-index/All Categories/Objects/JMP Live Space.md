# JMP Live Space

*Source: [https://jsl.jmp.com/All%20Categories/Objects/JMP%20Live%20Space.html](https://jsl.jmp.com/All%20Categories/Objects/JMP%20Live%20Space.html)*

---

# [JMP Live Space](#jmp-live-space)[](#jmp-live-space "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** string = jmplivespace \<\< Get Description()

**Description:** Gets the description of the JMP Live Space

**JMP Version Added:** 18

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Find Spaces( Search( "~" ) );

spaceList = jmpliveresult << As Scriptable;
space = spaceList[1];

Write( "Description: ", space << Get Description );
```

### [Get Key](#get-key)[](#get-key "Click to copy url")

**Syntax:** string = jmplivespace \<\< Get Key()

**Description:** Gets the space key for the JMP Live Space

**JMP Version Added:** 18

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Find Spaces( Search( "~" ) );

spaceList = jmpliveresult << As Scriptable;
space = spaceList[1];

Write( "Key: ", space << Get Key );
```

### [Get Name](#get-name)[](#get-name "Click to copy url")

**Syntax:** string = jmplivespace \<\< Get Name()

**Description:** Gets the name of the JMP Live Space

**JMP Version Added:** 18

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Find Spaces( Search( "~" ) );

spaceList = jmpliveresult << As Scriptable;
space = spaceList[1];

Write( "Name: ", space << Get Name );
```

### [Get Type](#get-type)[](#get-type "Click to copy url")

**Syntax:** string = jmplivespace \<\< Get Type()

**Description:** Gets the type of the JMP Live Space (Personal or Normal)

**JMP Version Added:** 18

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Find Spaces( Search( "~" ) );

spaceList = jmpliveresult << As Scriptable;
space = spaceList[1];

Write( "Type: ", space << Get Type );
```

[ Previous](JMP%20Live%20Result.html "JMP Live Result") [Next ](K%20Means%20Cluster.html "K Means Cluster")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
