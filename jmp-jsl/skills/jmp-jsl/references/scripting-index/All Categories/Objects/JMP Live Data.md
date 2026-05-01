# JMP Live Data

*Source: [https://jsl.jmp.com/All%20Categories/Objects/JMP%20Live%20Data.html](https://jsl.jmp.com/All%20Categories/Objects/JMP%20Live%20Data.html)*

---

# [JMP Live Data](#jmp-live-data)[](#jmp-live-data "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Get Description](#get-description)[](#get-description "Click to copy url")

**Syntax:** string = jmplivepost \<\< Get Description()

**Description:** Gets the description of the JMP Live Report, JMP Live Folder, or JMP Live Post as a string.

**JMP Version Added:** 16

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" )
);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);
Write( "\!n\!nID: ", report << Get ID );
Write( "\!nDescription: ", report << Get Description );
```

### [Get ID](#get-id)[](#get-id "Click to copy url")

**Syntax:** string = jmplivepost \<\< Get ID()

**Description:** Gets the ID for this JMP Live Report, JMP Live Folder, or JMP Live Post as a string.

**JMP Version Added:** 16

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" ),

);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);

Write( "\!n\!nID: ", report << Get ID );
```

### [Get Path](#get-path)[](#get-path "Click to copy url")

**Syntax:** string = jmplivepost \<\< Get Path()

**Description:** Gets the path of this JMP Live Report, Folder or Post as a string.

**JMP Version Added:** 19

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" ),

);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);

Write( "\!n\!nPath: ", report << Get Path );
```

### [Get Title](#get-title)[](#get-title "Click to copy url")

**Syntax:** string = jmplivepost \<\< Get Title()

**Description:** Gets the title of the JMP Live Report, JMP Live Folder, or JMP Live Post as a string.

**JMP Version Added:** 16

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" ),

);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);
Write( "\!n\!nID: ", report << Get ID );
Write( "\!nTitle: ", report << Get Title );
```

### [Get Type](#get-type)[](#get-type "Click to copy url")

**Syntax:** string = jmplivepost \<\< Get Type()

**Description:** Get the specific type of Post (Folder, Data or Report)

**JMP Version Added:** 17

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" ),

);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);

Write( "\!n\!nID: ", report << Get ID );
Write( "\!nType: ", report << Get Type );
```

### [Get URL](#get-url)[](#get-url "Click to copy url")

**Syntax:** string = jmplivepost \<\< Get URL()

**Description:** Gets the URL for this JMP Live Report, JMP Live Folder, or JMP Live Post as a string.

**JMP Version Added:** 16

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" ),

);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);
Write( "\!n\!nID: ", report << Get ID );
Write( "\!nURL: ", report << Get URL );
```

### [Set Description](#set-description)[](#set-description "Click to copy url")

**Syntax:** success = jmplivepost \<\< Set Description("string value")

**Description:** Given a string, sets the description of the JMP Live Report, JMP Live Folder, or JMP Live Post. Returns true or false for success or failure.

**JMP Version Added:** 16

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" ),

);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);
Write( "\!n\!nID: ", report << Get ID );
Write( "\!nDescription: ", report << Get Description );

report << Set Description( "A Much Nicer Description" );
jmpliveresult = liveconnection << Get Report( report << Get ID );
updated = jmpliveresult << As Scriptable;

Write( "\!n\!nID: ", report << Get ID );
Write( "\!nDecription: ", report << Get Description );
```

### [Set Title](#set-title)[](#set-title "Click to copy url")

**Syntax:** success = jmplivepost \<\< Set Title("New Title")

**Description:** Sets the title of the JMP Live Report, JMP Live Folder, or JMP Live Post. Returns a true or false for success or failure.

**JMP Version Added:** 16

``` jsl
bc = Open( "$SAMPLE_DATA/Big Class.jmp" );
gbsmoother = bc << Run Script( "Graph Builder Smoother Line" );

liveconnection = New JMP Live();
result = liveconnection << Create Folder(
    Parent Folder( "~" ),
    Title( "Reports and Posts - Messages" ),
    If Exists( "use" )
);
folder = result << As Scriptable;
// Make sure the report we will create does not already exist.
liveconnection << Delete Report( "~/Reports and Posts - Messages/A New Title" );

content = New JMP Live Content(
    gbsmoother,
    Title( "A Very Important Report" ),
    Description( "The Report That Is Published" ),

);
jmpliveresult = folder << Publish( content );

report = Empty();
postList = jmpliveresult << As Scriptable;
For( i = 1, i <= postlist << Get Number Of Items, i += 1,
    posttype = postlist[i] << Get Type;
    If( posttype == "Report",
        report = postlist[i]
    );
);
Write( "\!n\!nID: ", report << Get ID );
Write( "\!nTitle: ", report << Get Title );

report << Set Title( "A New Title" );
jmpliveresult = liveconnection << Get Report( report << Get ID );
updated = jmpliveresult << As Scriptable;

Write( "\!n\!nID: ", report << Get ID );
Write( "\!nTitle: ", report << Get Title );
```

[ Previous](JMP%20Live%20Content.html "JMP Live Content") [Next ](JMP%20Live%20Folder.html "JMP Live Folder")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
