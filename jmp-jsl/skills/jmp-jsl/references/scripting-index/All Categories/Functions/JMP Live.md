# JMP Live

*Source: [https://jsl.jmp.com/All%20Categories/Functions/JMP%20Live.html](https://jsl.jmp.com/All%20Categories/Functions/JMP%20Live.html)*

---

# [JMP Live](#jmp-live)[](#jmp-live "Click to copy url")

### [New JMP Live](#new-jmp-live)[](#new-jmp-live "Click to copy url")

**Syntax:** New JMP Live(Connection("Connection Name"), \<Prompt("No" \| "If Needed")\>)

**Description:** Start a connection to JMP Live using stored connection information. Connection is optional and defaults to the connection specified as the default in Connection Manager. If provided it looks up the connection by the name. Prompt is optional and defaults to "No". The valid values for prompt are "Yes", "No", and "If Needed". A value of "Yes" always prompts for login credentials. A value of "No" never prompts for login credentials, but could result in an authentication failure. A value of "If Needed" prompts for credentials only if the current stored credentials are not valid. Returns a JMP Live Connection object.

**JMP Version Added:** 15

**Example 1**

``` jsl
jmplive = New JMP Live();
```

**Example 2**

``` jsl
jmplive = New JMP Live( Connection( "MyJMPLive" ), Prompt( No ) );
```

**Example 3**

``` jsl
jmplive = New JMP Live( Connection( "MyJMPLive" ), Prompt( If Needed ) );
```

### [New JMP Live Content](#new-jmp-live-content)[](#new-jmp-live-content "Click to copy url")

**Syntax:** obj = New JMP Live Content(jmpreport\|Image(path_to_image)\|Data(jmpdatatable)\|Map(jmpmap), \<Title(...)\>, \<Description(...)\>, \<Publish Data(0\|1)\>, \<Enable Warnings(0\|1)\>, \<Optimization("Interactivity" \| "Performance")\>

**Description:** Creates interactive content for publishing on JMP Live.

    The first parameter is required and specifies the data to use for the content. That data can be a report, a data table, a map or an image.

    Title and Description are used to customize any type of content that is being published. The remaining parameters are optional and used to customize report content only.

    Publish Data indicates whether the data used in the report is published to JMP Live. The data for the report is published by default.

    Enable Warnings indicates whether Control Chart Warnings should be enabled for the report. Control Chart Warnings are disabled by default.

    Optimization is used to customize the way the report is published to JMP Live. The report is published to enable greater interactivity by default.

**JMP Version Added:** 17

**Example 1**

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
dist = bc << Run Script( "Distribution" );

liveconnection = New JMP Live();
jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Folder for Sample Content" )
);
folder = jmpliveresult << As Scriptable;

content = New JMP Live Content(
    dist,
    Title( "Distribution Web Report" ),
    Description( "This report was created with the sample found in the Scripting Index" ),
    Publish Data( 1 ),
    Optimization( "Interactivity" )
);

jmpliveresult = liveconnection << Publish( content, Folder( folder ) );
```

**Example 2**

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Folder for Data Content" )
);
folder = jmpliveresult << As Scriptable;

content = New JMP Live Content(
    Data( "$SAMPLE_DATA/Big Class.jmp" ),
    Title( "Big Class Sample Table" ),
    Description(
        "This data table was published with the sample found in the Scripting Index"
    )
);

jmpliveresult = liveconnection << Publish( content, Folder( folder ) );
```

**Example 3**

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Folder for Map Content" )
);
folder = jmpliveresult << As Scriptable;

content = New JMP Live Content( Map( "$SAMPLE_DATA/S4-XY.jmp" ) );

jmpliveresult = liveconnection << Publish( content, Folder( folder ) );
```

**Example 4**

``` jsl
liveconnection = New JMP Live();
jmpliveresult = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Folder for Image Content" )
);
folder = jmpliveresult << As Scriptable;

imageContent = New JMP Live Content(
    Image( "$SAMPLE_IMAGES/black rhino footprint.jpg" ),
    Title( "Rhino Footprint" ),
    Description( "An image of a rhino footprint from the Sample Data" )
);

jmpliveresult = liveconnection << Publish( imageContent, Folder( folder ) );
```

[ Previous](JMP%20Clinical.html "JMP Clinical") [Next ](List.html "List")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
