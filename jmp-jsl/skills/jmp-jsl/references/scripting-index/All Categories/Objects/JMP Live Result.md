# JMP Live Result

*Source: [https://jsl.jmp.com/All%20Categories/Objects/JMP%20Live%20Result.html](https://jsl.jmp.com/All%20Categories/Objects/JMP%20Live%20Result.html)*

---

# [JMP Live Result](#jmp-live-result)[](#jmp-live-result "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [As Scriptable](#as-scriptable)[](#as-scriptable "Click to copy url")

**Syntax:** jmplivereport = jmpliveresult \<\< As Scriptable()

**Description:** Depending on the operation that produced the JMP Live Result, returns a JMP Live Report, JMP Live Folder or JMP Live Post for further scripting operations.

**JMP Version Added:** 16

``` jsl
liveconnection = New JMP Live();

jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Result Example Folder" ),
    If Exists( "use" )
);
worked = jmpliveresult << Succeeded();
If( worked == 1,
    folder = jmpliveresult << As Scriptable;
    Write( "\!nResponse Type: ", jmpliveresult << Get Response Type );
    Write( "\!nTitle: ", folder << Get Title );
);
```

### [Get Error Message](#get-error-message)[](#get-error-message "Click to copy url")

**Syntax:** messagetext = jmpliveresult \<\< Get Error Message()

**Description:** Gets any message produced by the last operation as a string.

**JMP Version Added:** 16

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Get Folder( "THISISNOTAFOLDERID" );

httpstatus = jmpliveresult << Get HTTP Status();
httpmessage = jmpliveresult << Get Error Message();
Write( "\!nHTTP Status Code: ", httpstatus, " Message: ", httpmessage );
```

### [Get HTTP Status](#get-http-status)[](#get-http-status "Click to copy url")

**Syntax:** statuscode = jmpliveresult \<\< Get HTTP Status()

**Description:** Gets the HTTP status code from the last operation. This is an industry standard integer code.

**JMP Version Added:** 16

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Get Folder( "THISISNOTAFOLDERID" );

httpstatus = jmpliveresult << Get HTTP Status();
httpmessage = jmpliveresult << Get Error Message();
Write( "\!nHTTP Status Code: ", httpstatus, " Message: ", httpmessage );
```

### [Get JMP Live](#get-jmp-live)[](#get-jmp-live "Click to copy url")

**Syntax:** liveconnection = jmpliveresult \<\< Get JMP Live()

**Description:** Retrieves the underlying JMP Live Connection object.

**JMP Version Added:** 16

``` jsl
liveconnection = New JMP Live();

jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Result Example Folder" ),
    If Exists( "use" )
);
secondliveconnection = jmpliveresult << Get JMP Live();

name = secondliveconnection << Get Connection Name();
Write( "\!nConnection Name: ", name );
```

### [Get Response Type](#get-response-type)[](#get-response-type "Click to copy url")

**Syntax:** responsevalue = jmpliveresult \<\< Get Response Type()

**Description:** Gets the type of response produced by the last operation as a string.

**JMP Version Added:** 16

``` jsl
liveconnection = New JMP Live();

jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Result Example Folder" ),
    If Exists( "use" )
);
worked = jmpliveresult << Succeeded();
If( worked == 1,
    folder = jmpliveresult << As Scriptable;
    Write( "\!nResponse Type: ", jmpliveresult << Get Response Type );
    Write( "\!nTitle: ", folder << Get Title );
);
```

### [Succeeded](#succeeded)[](#succeeded "Click to copy url")

**Syntax:** success = jmpliveresult \<\< Succeeded()

**Description:** Returns whether the last action was successful (1) or not (0).

**JMP Version Added:** 16

``` jsl
liveconnection = New JMP Live();

jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Result Example Folder" ),
    If Exists( "use" )
);
worked = jmpliveresult << Succeeded();
If( worked == 1,
    folder = jmpliveresult << As Scriptable;
    Write( "\!nResponse Type: ", jmpliveresult << Get Response Type );
    Write( "\!nTitle: ", folder << Get Title );
);
```

[ Previous](JMP%20Live%20Result%20List.html "JMP Live Result List") [Next ](JMP%20Live%20Space.html "JMP Live Space")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
