# Reliability Forecast

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Reliability%20Forecast.html](https://jsl.jmp.com/All%20Categories/Objects/Reliability%20Forecast.html)*

---

# [Reliability Forecast](#reliability-forecast)[](#reliability-forecast "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Reliability Forecast](#reliability-forecast_1)[](#reliability-forecast_1 "Click to copy url")

**Syntax:** Reliability Forecast

**Description:** Predicts future failures based on observed data and future units at risk. The platform accepts several input formats. See each format for specification details.

#### [Dates Format](#dates-format)[](#dates-format "Click to copy url")

``` jsl

dt1 = Open( "$SAMPLE_DATA/Reliability/Small Production part1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Reliability/Small Production part2.jmp" );

obj = dt1 << Reliability Forecast(
    Input Format( Dates ),
    Production Data Table(
        dt1,
        Production Count( :Sold Quantity ),
        Timestamp( :Sold Month )
    ),
    Failure Data Table(
        dt2,
        Failure Time( :Return Month ),
        Timestamp( :Sold Month ),
        Failure Count( :Return Quantity )
    ),
    Life Time Unit( Month ),
    Show Legend( 1 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group( "" ),
        Risk Set( [2550, 2600, 2650, 2700, 2750, 2800, 2850] ),
        Future Risk Set(
            [3082.5, 3052.5, 3367.5, 3952.5, 3667, 3667],
            [3347740800, 3350160000, 3352579200, 3355257600, 3357849600, 3360528000]
        ),
        Forecast To( "02/2011" ),
        Distribution( Weibull ),
        Contract( 6, Month ),
        Forecast Type( Sequential ),
        Interval Type( Prediction Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 1 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

#### [Nevada Format](#nevada-format)[](#nevada-format "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

#### [Time to Event Format](#time-to-event-format)[](#time-to-event-format "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Small Production Time to Event.jmp" );
obj = dt << Reliability Forecast(
    Input Format( Time to Event ),
    Time to Event( :"Time (Month)"n, :Time Right ),
    Freq( :Freq ),
    Life Time Unit( Month ),
    Forecast Start( Informat( "03/01/2010", "Locale Date" ) ),
    Forecast(
        Group( "" ),
        Future Risk Set( [33, 33, 33], [3352924800, 3355516800, 3358195200] ),
        Forecast To( "09/01/2010" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( [1] ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( 0 ),
        Use Approximate Distribution( 1 )
    )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Contract](#contract)[](#contract "Click to copy url")

**Syntax:** obj \<\< Forecast( Contract( length, unit ) )

**Description:** Specifies the length and time unit for the contract that is used to forecast future risk.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Distribution](#distribution)[](#distribution "Click to copy url")

**Syntax:** obj \<\< Forecast( Distribution( name ) )

**Description:** Specifies the distribution that is used to forecast future risk.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Forecast Options](#forecast-options)[](#forecast-options "Click to copy url")

**Syntax:** obj \<\< Forecast Options( forecast message(), ... ); (obj \<\< Forecast Options) \<\< forecast message()

**Description:** Sends messages to the Forecast report scriptable object. You can specify one or more options from the Forecast report red triangle menu. If there are no arguments, this option returns a JSL reference to the Forecast report scriptable object. If there are arguments, this option returns a JSL reference to the platform object. See the entries under Forecast Options for more information.

#### [With Arguments](#with-arguments)[](#with-arguments "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
obj << Forecast Options( Animation( 0 ), Use Contract Length( 1 ), Show Interval( 1 ) );
```

#### [Without Arguments](#without-arguments)[](#without-arguments "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
(obj << Forecast Options) << Show Interval( 0 );
```

### [Forecast To](#forecast-to)[](#forecast-to "Click to copy url")

**Syntax:** obj \<\< Forecast( Forecast To( time ) )

**Description:** Specifies the final time at which future risk is forecasted.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Forecast Type](#forecast-type)[](#forecast-type "Click to copy url")

**Syntax:** obj \<\< Forecast( Forecast Type( type ) )

**Description:** Specifies the type of quantity that is used to forecast future risk. The type argument can be Incremental or Cumulative.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Future Risk Set](#future-risk-set)[](#future-risk-set "Click to copy url")

**Syntax:** obj \<\< Forecast( Future Risk Set( count vector, time vector ) )

**Description:** Specifies the future risk set that is used to forecast future risk. The arguments are a vector of production counts and a vector of future times.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Get Results](#get-results)[](#get-results "Click to copy url")

**Syntax:** obj \<\< Get Results

**Description:** Returns a named list that contains forecasting results.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
result = obj << Get Results;
```

### [Group](#group)[](#group "Click to copy url")

**Syntax:** obj \<\< Forecast( Group( group ), ... )

**Description:** Identifies the group to which all messages in the same Forecast clause should be sent.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Input Format](#input-format)[](#input-format "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Nevada\|Dates\|Time to Event )...)

**Description:** Specifies the format type of the input data for the analysis.

#### [Dates Format](#dates-format_1)[](#dates-format_1 "Click to copy url")

``` jsl

dt1 = Open( "$SAMPLE_DATA/Reliability/Small Production part1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Reliability/Small Production part2.jmp" );

obj = dt1 << Reliability Forecast(
    Input Format( Dates ),
    Production Data Table(
        dt1,
        Production Count( :Sold Quantity ),
        Timestamp( :Sold Month )
    ),
    Failure Data Table(
        dt2,
        Failure Time( :Return Month ),
        Timestamp( :Sold Month ),
        Failure Count( :Return Quantity )
    ),
    Life Time Unit( Month ),
    Show Legend( 1 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group( "" ),
        Risk Set( [2550, 2600, 2650, 2700, 2750, 2800, 2850] ),
        Future Risk Set(
            [3082.5, 3052.5, 3367.5, 3952.5, 3667, 3667],
            [3347740800, 3350160000, 3352579200, 3355257600, 3357849600, 3360528000]
        ),
        Forecast To( "02/2011" ),
        Distribution( Weibull ),
        Contract( 6, Month ),
        Forecast Type( Sequential ),
        Interval Type( Prediction Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 1 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

#### [Nevada Format](#nevada-format_1)[](#nevada-format_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Small Production.jmp" );
dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Sold Quantity ),
    Timestamp( :Sold Month ),
    Failure Count(
        :"08/2009"n, :"09/2009"n, :"10/2009"n, :"11/2009"n, :"12/2009"n, :"01/2010"n,
        :"02/2010"n
    ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 1 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group( "" ),
        Risk Set( [2550, 2600, 2650, 2700, 2750, 2800, 2850] ),
        Future Risk Set(
            [3022.5, 3307.5, 3502, 3502, 3502, 3502],
            [3347827200, 3350246400, 3352924800, 3355516800, 3358195200, 3360787200]
        ),
        Forecast To( "02/2011" ),
        Distribution( Weibull ),
        Contract( 12, Month ),
        Forecast Type( Sequential ),
        Interval Type( No Interval ),
        Alpha( 0.05 )
    )
);
```

#### [Time to Event Format](#time-to-event-format_1)[](#time-to-event-format_1 "Click to copy url")

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Small Production Time to Event.jmp" );
obj = dt << Reliability Forecast(
    Input Format( Time to Event ),
    Time to Event( :"Time (Month)"n, :Time Right ),
    Freq( :Freq ),
    Life Time Unit( Month ),
    Forecast Start( Informat( "03/01/2010", "Locale Date" ) ),
    Forecast(
        Group( "" ),
        Future Risk Set( [33, 33, 33], [3352924800, 3355516800, 3358195200] ),
        Forecast To( "09/01/2010" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( [1] ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( 0 ),
        Use Approximate Distribution( 1 )
    )
);
```

### [Interval Type](#interval-type)[](#interval-type "Click to copy url")

**Syntax:** obj \<\< Forecast( Interval Type( type ) )

**Description:** Specifies the type of interval that is used to forecast the error around the future risk. The interval type can be No Interval, Plugin Interval, or Prediction Interval.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Risk Set](#risk-set)[](#risk-set "Click to copy url")

**Syntax:** obj \<\< Forecast( Risk Set( count vector ) )

**Description:** Specifies the existing risk set that is used to forecast future risk.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Save Data in Time to Event Format](#save-data-in-time-to-event-format)[](#save-data-in-time-to-event-format "Click to copy url")

**Syntax:** obj \<\< Save Data in Time to Event Format

**Description:** Saves Nevada or Dates formatted data in a new Time to Event formatted data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
obj << Save Data in Time to Event Format;
```

### [Save Forecast Data Table](#save-forecast-data-table)[](#save-forecast-data-table "Click to copy url")

**Syntax:** obj \<\< Save Forecast Data Table

**Description:** Saves the cumulative and incremental number of returns in a new data table, along with the variables that you selected in the launch window. For grouped analyses, table names include the group ID and the word "Aggregated". Existing returns are also included in the aggregated data tables.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
dt results = obj << Save Forecast Data Table;
```

### [Set Interval Level](#set-interval-level)[](#set-interval-level "Click to copy url")

**Syntax:** obj \<\< Forecast( Set Interval Level( value ) )

**Description:** Specifies the confidence level for the interval that is used to forecast the error around the future risk.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
n = N Rows( dt );
mat = dt << get as matrix;
mat = (mat || J( n, 1, 1 )) |/ (mat || J( n, 1, 2 ));
dt = As Table( mat );
Column( dt, 2 ) << Format( "m/y", 7 );
Column( dt, 2 ) << set name( "Time" );
Column( dt, 1 ) << set name( "Volume" );
For Each( {i}, 3 :: 38,
    Column( dt, i ) << set name(
        Format( Date Increment( Column( dt, 2 )[i - 2], "Month", 1 ), "m/y", 7 )
    )
);
Column( dt, 39 ) << set name( "Group" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Group ID( :Group ),
    Life Time Unit( Month ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast Options( Show Interval( 1 ) )
);
obj << Forecast(
    Group( "1" ),
    Risk Set(
        [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026, 1950,
        1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966,
        2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
    ),
    Future Risk Set( [2003, 2003], [3139862400, 3142540800] ),
    Forecast To( "01/2004" ),
    Distribution( Weibull ),
    Contract( 5, Month ),
    Forecast Type( Cumulative ),
    Interval Type( No Interval ),
    Set Interval Level( 0.9 )
);
obj << Forecast(
    Group( "2" ),
    Risk Set(
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2026, 1950, 1989, 1963, 1954, 2030, 1981, 2006,
        1991, 1950, 2025, 1996, 1987, 1957, 1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045,
        2018, 2036]
    ),
    Future Risk Set( [2000, 3000], [3139862400, 3142540800] ),
    Forecast To( "08/2005" ),
    Distribution( Weibull ),
    Contract( 36, Month ),
    Forecast Type( Incremental ),
    Interval Type( Prediction Interval ),
    Set Interval Level( 0.9 )
);
```

### [Show Graph Filter](#show-graph-filter)[](#show-graph-filter "Click to copy url")

**Syntax:** obj \<\< Show Graph Filter( state=0\|1 )

**Description:** Shows or hides the Graph Filter so that you can select which production periods to show in the Observed Data graphs. Bars fade for deselected periods. Deselect the periods to show the graph in its original state. This option is not available for Time to Event data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
obj << Show Graph Filter( 1 );
```

### [Show Legend](#show-legend)[](#show-legend "Click to copy url")

**Syntax:** obj \<\< Show Legend( state=0\|1 )

**Description:** Shows or hides a legend for the Observed Data report. This option is not available for Time to Event data.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
obj << Show Legend( 1 );
```

## [Shared Item Messages](#shared-item-messages)[](#shared-item-messages "Click to copy url")

### [Action](#action)[](#action "Click to copy url")

**Syntax:** obj \<\< Action

**Description:** All-purpose trapdoor within a platform to insert expressions to evaluate. Temporarily sets the DisplayBox and DataTable contexts to the Platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Y( :height ),
    X( :weight ),
    Action( Distribution( Y( :height, :weight ), Histograms Only ) )
);
```

### [Apply Preset](#apply-preset)[](#apply-preset "Click to copy url")

**Syntax:** Apply Preset( preset ); Apply Preset( source, label, \<Folder( folder {, folder2, ...} )\> )

**Description:** Apply a previously created preset to the object, updating the options and customizations to match the saved settings.

**JMP Version Added:** 18

#### [Anonymous preset](#anonymous-preset)[](#anonymous-preset "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
dt2 = Open( "$SAMPLE_DATA/Dogs.jmp" );
obj2 = dt2 << Oneway( Y( :LogHist0 ), X( :drug ) );
Wait( 1 );
obj2 << Apply Preset( preset );
```

#### [Search by name](#search-by-name)[](#search-by-name "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "Compare Distributions" );
```

#### [Search within folder(s)](#search-within-folders)[](#search-within-folders "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ) );
Wait( 1 );
obj << Apply Preset( "Sample Presets", "t-Tests", Folder( "Compare Means" ) );
```

### [Automatic Recalc](#automatic-recalc)[](#automatic-recalc "Click to copy url")

**Syntax:** obj \<\< Automatic Recalc( state=0\|1 )

**Description:** Redoes the analysis automatically for exclude and data changes. If the Automatic Recalc option is turned on, you should consider using Wait(0) commands to ensure that the exclude and data changes take effect before the recalculation.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Automatic Recalc( 1 );
dt << Select Rows( 5 ) << Exclude( 1 );
```

### [Column Switcher](#column-switcher)[](#column-switcher "Click to copy url")

**Syntax:** obj \<\< Column Switcher(column reference, {column reference, ...}, \< Title(title) \>, \< Close Outline(0\|1) \>, \< Retain Axis Settings(0\|1) \>, \< Layout(0\|1) \>)

**Description:** Adds a control panel for changing the platform's variables

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Contingency( Y( :size ), X( :marital status ) );
ColumnSwitcherObject = obj << Column Switcher(
    :marital status,
    {:sex, :country, :marital status}
);
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Data Table Window;
```

### [Get By Levels](#get-by-levels)[](#get-by-levels "Click to copy url")

**Syntax:** obj \<\< Get By Levels

**Description:** Returns an associative array mapping the by group columns to their values.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv << Get By Levels;
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
t = obj << Get Container;
Show( (t << XPath( "//OutlineBox" )) << Get Title );
```

#### [Platform with Filter](#platform-with-filter)[](#platform-with-filter "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :age, :sex, :height ),
            Where( :age == {12, 13, 14} ),
            Where( :sex == "F" ),
            Where( :height >= 55 ),
            Display( :age, N Items( 6 ) )
        )
    )
);
New Window( "platform boxes",
    H List Box(
        Outline Box( "Report(platform)", Report( gb ) << Get Picture ),
        Outline Box( "platform << Get Container", (gb << Get Container) << Get Picture )
    )
);
```

### [Get Data Table](#get-data-table)[](#get-data-table "Click to copy url")

**Syntax:** obj \<\< Get Data Table

**Description:** Returns a reference to the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
t = obj << Get Timing;
Show( t );
```

### [Get Web Support](#get-web-support)[](#get-web-support "Click to copy url")

**Syntax:** obj \<\< Get Web Support

**Description:** Return a number indicating the level of Interactive HTML support for the display object. 1 means some or all elements are supported. 0 means no support.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
s = obj << Get Web Support();
Show( s );
```

### [Get Where Expr](#get-where-expr)[](#get-where-expr "Click to copy url")

**Syntax:** obj \<\< Get Where Expr

**Description:** Returns the Where expression for the data subset, if the platform was launched with By() or Where(). Otherwise, returns Empty()

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( X( :height ), Y( :weight ), By( :sex ) );
biv2 = dt << Bivariate( X( :height ), Y( :weight ), Where( :age < 14 & :height > 60 ) );
Show( biv[1] << Get Where Expr, biv2 << Get Where Expr );
```

### [Ignore Platform Preferences](#ignore-platform-preferences)[](#ignore-platform-preferences "Click to copy url")

**Syntax:** Ignore Platform Preferences( state=0\|1 )

**Description:** Ignores the current settings of the platform's preferences. The message is ignored when sent to the platform after creation.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Bivariate(
    Ignore Platform Preferences( 1 ),
    Y( :height ),
    X( :weight ),
    Action( Distribution( Y( :height, :weight ), Histograms Only ) )
);
```

### [Local Data Filter](#local-data-filter)[](#local-data-filter "Click to copy url")

**Syntax:** obj \<\< Local Data Filter

**Description:** To filter data to specific groups or ranges, but local to this platform

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << Distribution(
    Nominal Distribution( Column( :country ) ),
    Local Data Filter(
        Add Filter( columns( :sex ), Where( :sex == "Female" ) ),
        Mode( Show( 1 ), Include( 1 ) )
    )
);
```

### [New Preset](#new-preset)[](#new-preset "Click to copy url")

**Syntax:** obj = New Preset()

**Description:** Create an anonymous preset representing the options and customizations applied to the object. This object can be passed to Apply Preset to copy the settings to another object of the same type.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Oneway( Y( :height ), X( :sex ), t Test( 1 ) );
preset = obj << New Preset();
```

### [Paste Local Data Filter](#paste-local-data-filter)[](#paste-local-data-filter "Click to copy url")

**Syntax:** obj \<\< Paste Local Data Filter

**Description:** Apply the local data filter from the clipboard to the current report.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dist = Distribution( Continuous Distribution( Column( :POP ) ) );
filter = dist << Local Data Filter(
    Add Filter( columns( :Region ), Where( :Region == "MW" ) )
);
filter << Copy Local Data Filter;
dist2 = Distribution( Continuous Distribution( Column( :Lead ) ) );
Wait( 1 );
dist2 << Paste Local Data Filter;
```

### [Redo Analysis](#redo-analysis)[](#redo-analysis "Click to copy url")

**Syntax:** obj \<\< Redo Analysis

**Description:** Rerun this same analysis in a new window. The analysis will be different if the data has changed.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Relaunch Analysis;
```

### [Remove Column Switcher](#remove-column-switcher)[](#remove-column-switcher "Click to copy url")

**Syntax:** obj \<\< Remove Column Switcher

**Description:** Removes the most recent Column Switcher that has been added to the platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Contingency( Y( :size ), X( :marital status ) );
ColumnSwitcherObject = obj << Column Switcher(
    :marital status,
    {:sex, :country, :marital status}
);
Wait( 2 );
obj << Remove Column Switcher;
```

### [Remove Local Data Filter](#remove-local-data-filter)[](#remove-local-data-filter "Click to copy url")

**Syntax:** obj \<\< Remove Local Data Filter

**Description:** If a local data filter has been created, this removes it and restores the platform to use all the data in the data table directly

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dist = dt << Distribution(
    Nominal Distribution( Column( :country ) ),
    Local Data Filter(
        Add Filter( columns( :sex ), Where( :sex == "Female" ) ),
        Mode( Show( 1 ), Include( 1 ) )
    )
);
Wait( 2 );
dist << remove local data filter;
```

### [Report](#report)[](#report "Click to copy url")

**Syntax:** obj \<\< Report; Report( obj )

**Description:** Returns a reference to the report object.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Report View( "Summary" );
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ), By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ), By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Save Script to Script Window;
```

### [SendToByGroup](#sendtobygroup)[](#sendtobygroup "Click to copy url")

**Syntax:** SendToByGroup( {":Column == level"}, command );

**Description:** Sends platform commands or display customization commands to each level of a by-group.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    By( :Sex ),
    SendToByGroup(
        {:sex == "F"},
        Continuous Distribution( Column( :weight ), Normal Quantile Plot( 1 ) )
    ),
    SendToByGroup( {:sex == "M"}, Continuous Distribution( Column( :weight ) ) )
);
```

### [SendToEmbeddedScriptable](#sendtoembeddedscriptable)[](#sendtoembeddedscriptable "Click to copy url")

**Syntax:** SendToEmbeddedScriptable( Dispatch( "Outline name", "Element name", command );

**Description:** SendToEmbeddedScriptable restores settings of embedded scriptable objects.

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Fan.jmp" );
dt << Life Distribution(
    Y( :Time ),
    Censor( :Censor ),
    Censor Code( 1 ),
    <<Fit Weibull,
    SendToEmbeddedScriptable(
        Dispatch(
            {"Statistics", "Parametric Estimate - Weibull", "Profilers", "Density Profiler"},
            {1, Confidence Intervals( 0 ), Term Value( Time( 6000, Lock( 0 ), Show( 1 ) ) )}
        )
    )
);
```

### [SendToReport](#sendtoreport)[](#sendtoreport "Click to copy url")

**Syntax:** SendToReport( Dispatch( "Outline name", "Element name", Element type, command );

**Description:** Send To Report is used in tandem with the Dispatch command to customize the appearance of a report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    Nominal Distribution( Column( :age ) ),
    Continuous Distribution( Column( :weight ) ),
    SendToReport( Dispatch( "age", "Distrib Nom Hist", FrameBox, {Frame Size( 178, 318 )} ) )
);
```

### [Sync to Data Table Changes](#sync-to-data-table-changes)[](#sync-to-data-table-changes "Click to copy url")

**Syntax:** obj \<\< Sync to Data Table Changes

**Description:** Sync with the exclude and data changes that have been made.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
dist = Distribution( Continuous Distribution( Column( :POP ) ) );
Wait( 1 );
dt << Delete Rows( dt << Get Rows Where( :Region == "W" ) );
dist << Sync To Data Table Changes;
```

### [Title](#title)[](#title "Click to copy url")

**Syntax:** obj \<\< Title( "new title" )

**Description:** Sets the title of the platform.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [View Web XML](#view-web-xml)[](#view-web-xml "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

## [Forecast Options](#forecast-options_1)[](#forecast-options_1 "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Animation](#animation)[](#animation "Click to copy url")

**Syntax:** obj \<\< Animation( state=0\|1 )

**Description:** Controls the flashing of the hotspots in the Forecast graphs. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Forecasting Interval Type](#forecasting-interval-type)[](#forecasting-interval-type "Click to copy url")

**Syntax:** obj \<\< Forecasting Interval Type( type )

**Description:** Specifies the type of interval that is used to forecast the error around the future risk. The interval type can be Plugin Interval or Prediction Interval.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Import Future Risk Set](#import-future-risk-set)[](#import-future-risk-set "Click to copy url")

**Syntax:** obj \<\< Import Future Risk Set

**Description:** Enables you to import future production data from another open data table. The new predictions then appear in the future risk graph. The imported data table must have a column for timestamps and for production counts.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
import set = [3139862400 2000, 3142540800 2050, 3145219200 2100, 3147811200 2150, 3150489600
2200, 3153081600 2250];
dt import = As Table( import set, <<Column Names( {"Time", "Volume"} ) );
option << Import Future Risk Set;
```

#### [Interactive Configuration of Risk Sets](#interactive-configuration-of-risk-sets)[](#interactive-configuration-of-risk-sets "Click to copy url")

**Syntax:** obj \<\< Interactive Configuration of Risk Sets( state=0\|1 )

**Description:** Determines whether you can drag hotspots in the graphs.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Monte Carlo Sample Size](#monte-carlo-sample-size)[](#monte-carlo-sample-size "Click to copy url")

**Syntax:** obj \<\< Monte Carlo Sample Size( number )

**Description:** Specifies the sample size of the simulation that is used to generate the prediction intervals.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Random Seed](#random-seed)[](#random-seed "Click to copy url")

**Syntax:** obj \<\< Random Seed( number )

**Description:** Specifies a random seed that can be used to reproduce the simulated prediction intervals.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Save Forecast Data Table](#save-forecast-data-table_1)[](#save-forecast-data-table_1 "Click to copy url")

**Syntax:** obj \<\< Save Forecast Data Table

**Description:** Saves the cumulative and incremental number of returns in a new data table, along with the variables that you selected in the launch window. For grouped analyses, table names include the group ID and the word "Aggregated". Existing returns are also included in the aggregated data tables.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Save Forecast Data Table;
```

#### [Set Failure Cost](#set-failure-cost)[](#set-failure-cost "Click to copy url")

**Syntax:** obj \<\< Set Failure Cost( number )

**Description:** Specifies the cost for each failure.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Show Interval](#show-interval)[](#show-interval "Click to copy url")

**Syntax:** obj \<\< Show Interval( state=0\|1 )

**Description:** Shows or hides 95% confidence limits in the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Spreadsheet Configuration of Risk Sets](#spreadsheet-configuration-of-risk-sets)[](#spreadsheet-configuration-of-risk-sets "Click to copy url")

**Syntax:** obj \<\< Spreadsheet Configuration of Risk Sets( state=0\|1 )

**Description:** Shows or hides a report that enables you to enter specific production counts and timestamps instead of adding them to the interactive graphs.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Use Approximate Distribution](#use-approximate-distribution)[](#use-approximate-distribution "Click to copy url")

**Syntax:** obj \<\< Use Approximate Distribution( state=0\|1 )

**Description:** Specifies that the prediction intervals are generated using a Poisson distribution to approximate the number of failures in each interval. If this option is not selected, the prediction intervals use a multinomial distribution to simulate the number of failures in each interval.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Use Contract Length](#use-contract-length)[](#use-contract-length "Click to copy url")

**Syntax:** obj \<\< Use Contract Length( state=0\|1 )

**Description:** Determines whether the specified contract length is considered in the forecast.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

#### [Use Failure Cost](#use-failure-cost)[](#use-failure-cost "Click to copy url")

**Syntax:** obj \<\< Use Failure Cost( state=0\|1 )

**Description:** Shows failure cost instead of the failure count in the future risk graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
obj = dt << Run Script( "Reliability Forecast" );
option = obj << Forecast Options;
option << Animation( 0 );
option << Interactive Configuration of Risk Sets( 0 );
option << Spreadsheet Configuration of Risk Sets( 1 );
option << Show Interval( 1 );
option << Forecasting Interval Type( Prediction Interval );
option << Use Contract Length( 1 );
option << Use Failure Cost( 1 );
option << Set Failure Cost( 100 );
option << Monte Carlo Sample Size( 10000 );
option << Random Seed( 1111 );
option << Use Approximate Distribution( 1 );
```

## [Reliability Forecast for Dates Format](#reliability-forecast-for-dates-format)[](#reliability-forecast-for-dates-format "Click to copy url")

### [Columns](#columns)[](#columns "Click to copy url")

#### [Failure Count](#failure-count)[](#failure-count "Click to copy url")

**Syntax:** obj \<\< Failure Count( column )

#### [Failure Time](#failure-time)[](#failure-time "Click to copy url")

**Syntax:** obj \<\< Failure Time( column(s) )

#### [Group ID](#group-id)[](#group-id "Click to copy url")

**Syntax:** obj \<\< Group ID( column )

#### [Left Censor](#left-censor)[](#left-censor "Click to copy url")

**Syntax:** obj \<\< Left Censor( column )

#### [Production Count](#production-count)[](#production-count "Click to copy url")

**Syntax:** obj \<\< Production Count( column )

#### [Timestamp](#timestamp)[](#timestamp "Click to copy url")

**Syntax:** obj \<\< Timestamp( column )

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Censor Code](#censor-code)[](#censor-code "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Dates ), Censor Code( value=1 )...)

**Description:** Identifies the value in the Censor column that designates right-censored observations.

#### [Life Time Unit](#life-time-unit)[](#life-time-unit "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Dates ), Life Time Unit( unit )...)

**Description:** Specifies the physical date-time format of all time stamps, including the format of the column titles for the return counts. This setting is used in forecasting step increments. The unit argument can be any of the following: Numeric, Year, Month, Week, Day, Hour, Minute, or Second.

``` jsl

dt1 = Open( "$SAMPLE_DATA/Reliability/Small Production part1.jmp" );
dt2 = Open( "$SAMPLE_DATA/Reliability/Small Production part2.jmp" );

obj = dt1 << Reliability Forecast(
    Input Format( Dates ),
    Production Data Table(
        dt1,
        Production Count( :Sold Quantity ),
        Timestamp( :Sold Month )
    ),
    Failure Data Table(
        dt2,
        Failure Time( :Return Month ),
        Timestamp( :Sold Month ),
        Failure Count( :Return Quantity )
    ),
    Life Time Unit( Month ),
    Show Legend( 1 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group( "" ),
        Risk Set( [2550, 2600, 2650, 2700, 2750, 2800, 2850] ),
        Future Risk Set(
            [3082.5, 3052.5, 3367.5, 3952.5, 3667, 3667],
            [3347740800, 3350160000, 3352579200, 3355257600, 3357849600, 3360528000]
        ),
        Forecast To( "02/2011" ),
        Distribution( Weibull ),
        Contract( 6, Month ),
        Forecast Type( Sequential ),
        Interval Type( Prediction Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 1 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

## [Reliability Forecast for Nevada Format](#reliability-forecast-for-nevada-format)[](#reliability-forecast-for-nevada-format "Click to copy url")

### [Columns](#columns_1)[](#columns_1 "Click to copy url")

#### [Failure Count](#failure-count_1)[](#failure-count_1 "Click to copy url")

**Syntax:** obj \<\< Failure Count( column(s) )

#### [Group ID](#group-id_1)[](#group-id_1 "Click to copy url")

**Syntax:** obj \<\< Group ID( column )

#### [Production Count](#production-count_1)[](#production-count_1 "Click to copy url")

**Syntax:** obj \<\< Production Count( column )

#### [Timestamp](#timestamp_1)[](#timestamp_1 "Click to copy url")

**Syntax:** obj \<\< Timestamp( column )

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [Interval Censored Failure](#interval-censored-failure)[](#interval-censored-failure "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Nevada ), Interval Censored Failure( state=0\|1 )...)

**Description:** Specifies that returned quantities be treated as interval-censored observations. The interval is between the last recorded time and the time that the failure was observed. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

#### [Life Time Unit](#life-time-unit_1)[](#life-time-unit_1 "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Nevada ), Life Time Unit( unit )...)

**Description:** Specifies the physical date-time format of all time stamps, including the format of the column titles for the return counts. This setting is used in forecasting step increments. The unit argument can be any of the following: Numeric, Year, Month, Week, Day, Hour, Minute, or Second.

``` jsl
dt = Open( "$SAMPLE_DATA/Reliability/Widgets.jmp" );
collist = Transform Each( {i}, 3 :: 38, Output( "List" ), Column( dt, i ) );
obj = dt << Reliability Forecast(
    Input Format( Nevada ),
    Production Count( :Volume ),
    Timestamp( :Time ),
    Failure Count( Eval List( collist ) ),
    Life Time Unit( Month ),
    Interval Censored Failure( 1 ),
    Show Legend( 0 ),
    Show Graph Filter( 0 ),
    Forecast(
        Group(),
        Risk Set(
            [1991, 2000, 1999, 2024, 1959, 1958, 2000, 2001, 1986, 1966, 1983, 2011, 2026,
            1950, 1989, 1963, 1954, 2030, 1981, 2006, 1991, 1950, 2025, 1996, 1987, 1957,
            1988, 1966, 2038, 2014, 1962, 1965, 1952, 2045, 2018, 2036]
        ),
        Forecast To( "01/2004" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( . ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( -1 ),
        Use Approximate Distribution( 1 )
    )
);
```

## [Reliability Forecast for Time to Event Format](#reliability-forecast-for-time-to-event-format)[](#reliability-forecast-for-time-to-event-format "Click to copy url")

### [Columns](#columns_2)[](#columns_2 "Click to copy url")

#### [Censor](#censor)[](#censor "Click to copy url")

**Syntax:** obj \<\< Censor( column )

#### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

#### [Group ID](#group-id_2)[](#group-id_2 "Click to copy url")

**Syntax:** obj \<\< Group ID( column )

#### [Time to Event](#time-to-event)[](#time-to-event "Click to copy url")

**Syntax:** obj \<\< Time to Event( column(s) )

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Censor Code](#censor-code_1)[](#censor-code_1 "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Time to Event ), Censor Code( value=1 )...)

**Description:** Identifies the value in the Censor column that designates right-censored observations.

#### [Forecast Start](#forecast-start)[](#forecast-start "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Time to Event ), Forecast Start( time )...)

**Description:** Specifies the time at which the forecast begins. The format of the time depends on the setting of the Life Time Unit option.

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Small Production Time to Event.jmp" );
obj = dt << Reliability Forecast(
    Input Format( Time to Event ),
    Time to Event( :"Time (Month)"n, :Time Right ),
    Freq( :Freq ),
    Life Time Unit( Month ),
    Forecast Start( Informat( "03/01/2010", "Locale Date" ) ),
    Forecast(
        Group( "" ),
        Future Risk Set( [33, 33, 33], [3352924800, 3355516800, 3358195200] ),
        Forecast To( "09/01/2010" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( [1] ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( 0 ),
        Use Approximate Distribution( 1 )
    )
);
```

#### [Life Time Unit](#life-time-unit_2)[](#life-time-unit_2 "Click to copy url")

**Syntax:** obj = Reliability Forecast(...Input Format( Time to Event ), Life Time Unit( unit )...)

**Description:** Specifies the physical date-time format of all time stamps, including the format of the column titles for the return counts. This setting is used in forecasting step increments. The unit argument can be any of the following: Numeric, Year, Month, Week, Day, Hour, Minute, or Second.

``` jsl

dt = Open( "$SAMPLE_DATA/Reliability/Small Production Time to Event.jmp" );
obj = dt << Reliability Forecast(
    Input Format( Time to Event ),
    Time to Event( :"Time (Month)"n, :Time Right ),
    Freq( :Freq ),
    Life Time Unit( Month ),
    Forecast Start( Informat( "03/01/2010", "Locale Date" ) ),
    Forecast(
        Group( "" ),
        Future Risk Set( [33, 33, 33], [3352924800, 3355516800, 3358195200] ),
        Forecast To( "09/01/2010" ),
        Distribution( Weibull ),
        Contract( 5, Month ),
        Forecast Type( Incremental ),
        Interval Type( No Interval ),
        Set Interval Level( 0.9 )
    ),
    Forecast Options(
        Animation( 1 ),
        Interactive Configuration of Risk Sets( 1 ),
        Spreadsheet Configuration of Risk Sets( 0 ),
        Show Interval( 0 ),
        Forecasting Interval Type( Prediction Interval ),
        Use Contract Length( 1 ),
        Use Failure Cost( 0 ),
        Set Failure Cost( [1] ),
        Monte Carlo Sample Size( 10000 ),
        Random Seed( 0 ),
        Use Approximate Distribution( 1 )
    )
);
```

[ Previous](Recurrence%20Analysis.html "Recurrence Analysis") [Next ](Reliability%20Growth.html "Reliability Growth")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
