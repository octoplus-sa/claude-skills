# IP.21 Server

*Source: [https://jsl.jmp.com/All%20Categories/Objects/IP.21%20Server.html](https://jsl.jmp.com/All%20Categories/Objects/IP.21%20Server.html)*

---

# [IP.21 Server](#ip21-server)[](#ip21-server "Click to copy url")

### [New IP21 Client](#new-ip21-client)[](#new-ip21-client "Click to copy url")

**Syntax:** New IP21 Client(URL(base URL), \<Authentication Method("None"\|"Basic"\|"NTLM"\|"Kerberos")\>, \<Username(userid)\>,\<Password(password)\>)

**Description:** Creates a new IP21 Client instance that can be used to import data from an AspenTech IP.21 server.

**JMP Version Added:** 19

**Example 1**

``` jsl
/* Import actual (raw) data */
/* Note: URL() and Authentication Method() use example values. Please supply a working URL and authentication credentials. */  
tag set = {"TI8045", "TI8058", "TI8064"};
end time = Today();
start time = end time - In Days( 1 );
client = New IP21 Client(
    URL( "https://myserver.com/" ),
    Authentication Method( "NTLM" ),
    Username( "%_UID_%" ),
    Password( "%_PWD_%" )
);
importer = client << Importer(
    Data Source( "My-Data-Source" ),
    Tag Set( tag set ),
    Start Time( start time ),
    End Time( end time ),
    Retrieval Type( "Actual" )
);
importer << Run;
```

**Example 2**

``` jsl
/* Import interpolated data */
/* Note: URL() and Authentication Method() use example values. Please supply a working URL and authentication credentials. */  
tag set = {"TI8045", "TI8058", "TI8064"};
end time = Today();
start time = end time - In Days( 1 );
client = New IP21 Client(
    URL( "https://myserver.com/" ),
    Authentication Method( "NTLM" ),
    Username( "%_UID_%" ),
    Password( "%_PWD_%" )
);
importer = client << Importer(
    Data Source( "My-Data-Source" ),
    Tag Set( tag set ),
    Start Time( start time ),
    End Time( end time ),
    Retrieval Type( "Interpolated" ),
    Period( Minute( 30 ) ),     /* Every half hour */
);
importer << Run;
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Importer](#importer)[](#importer "Click to copy url")

**Syntax:** Importer(Data Source(string), Tag Set(string list), Start Time(date-time value), End Time(date-time value), \<Retrieval Type(string)\>, \<Max Count(number)\>, \<Include Outsiders(0\|1)\>, \<Stepped(0\|1)\>, \<Period(Day(number) \| Hour(number) \| Minute(number))\>, \<Aggregate( Method("Integral" \| "Value" \| "Integral Incomplete" \| "Value Incomplete"), Start("Start Of Day" \| "Start Of Time"), Anchor("Begin" \| "Middle" \| "End"))\>

**Description:** Creates a new raw importer instance.

**JMP Version Added:** 19

**Example 1**

``` jsl
/* Import actual (raw) data */
/* Note: URL() and Authentication Method() use example values. Please supply a working URL and authentication credentials. */  
tag set = {"TI8045", "TI8058", "TI8064"};
end time = Today();
start time = end time - In Days( 1 );
client = New IP21 Client(
    URL( "https://myserver.com/" ),
    Authentication Method( "NTLM" ),
    Username( "%_UID_%" ),
    Password( "%_PWD_%" )
);
importer = client << Importer(
    Data Source( "My-Data-Source" ),
    Tag Set( tag set ),
    Start Time( start time ),
    End Time( end time ),
    Retrieval Type( "Actual" )
);
importer << Run;
```

**Example 2**

``` jsl
/* Import interpolated data */
/* Note: URL() and Authentication Method() use example values. Please supply a working URL and authentication credentials. */  
tag set = {"TI8045", "TI8058", "TI8064"};
end time = Today();
start time = end time - In Days( 1 );
client = New IP21 Client(
    URL( "https://myserver.com/" ),
    Authentication Method( "NTLM" ),
    Username( "%_UID_%" ),
    Password( "%_PWD_%" )
);
importer = client << Importer(
    Data Source( "My-Data-Source" ),
    Tag Set( tag set ),
    Start Time( start time ),
    End Time( end time ),
    Retrieval Type( "Interpolated" ),
    Period( Minute( 30 ) ),     /* Every half hour */
);
importer << Run;
```

[ Previous](HTTP.html "HTTP") [Next ](Image.html "Image")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
