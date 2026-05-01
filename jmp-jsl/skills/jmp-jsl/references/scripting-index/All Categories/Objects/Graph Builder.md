# Graph Builder

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Graph%20Builder.html](https://jsl.jmp.com/All%20Categories/Objects/Graph%20Builder.html)*

---

# [Graph Builder](#graph-builder)[](#graph-builder "Click to copy url")

## [Area Element](#area-element)[](#area-element "Click to copy url")

### [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

#### [Area Element](#area-element_1)[](#area-element_1 "Click to copy url")

**Syntax:** Area Element

**Description:** Shows a response summarized by categories.

**100% stacked area chart**

``` jsl
Open( "$SAMPLE_DATA/Corn Wheat Soybean Production.jmp" );
// 100% stacked area
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Year ),
        Y( :Commodity Acres Planted ),
        Group X( :State, Show Title( 0 ) ),
        Overlay( :Commodity )
    ),
    Elements( Area( X, Y, Legend( 40 ), Summary Statistic( "% of Factor" ) ) ),
    Local Data Filter(
        Add Filter( columns( :State ), Where( :State == {"IOWA", "NEBRASKA", "OKLAHOMA"} ) )
    ),
    SendToReport(
        Dispatch( {}, "Commodity Acres Planted", ScaleBox,
            {Format( "Percent", 13, 0 ), Max( 1 )}
        ),
        Dispatch( {}, "400", LegendBox, {Legend Position( {40, [2, 1, 0, -3, -3, -3]} )} )
    )
);
```

**Overlaid area with fill patterns**

``` jsl
Open( "$SAMPLE_DATA/Corn Wheat Soybean Production.jmp" );
// overlaid area with fill patterns
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Year ),
        Y( :Commodity Acres Planted ),
        Group X( :State, Show Title( 0 ) ),
        Overlay( :Commodity )
    ),
    Elements( Area( X, Y, Legend( 40 ), Area Style( "Overlaid" ) ) ),
    Local Data Filter(
        Add Filter( columns( :State ), Where( :State == {"IOWA", "NEBRASKA", "OKLAHOMA"} ) )
    ),
    SendToReport(
        Dispatch( {}, "Commodity Acres Planted", ScaleBox, {Format( "Engineering SI", 13 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                40,
                Properties( 0, {Fill Pattern( "grid dots" )} ),
                Properties( 1, {Fill Pattern( "right slant medium" )} ),
                Properties( 2, {Fill Pattern( "left slant medium" )} )
            )}
        ),
        Dispatch( {}, "400", LegendBox, {Legend Position( {40, [2, 1, 0, -3, -3, -3]} )} )
    )
);
```

**Range area as custom interval around line**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// range area, custom interval, overlaid line, transparency
Graph Builder(
    Transform Column(
        "Quantile...=0.75[height][age]",
        Formula( Col Quantile( :height, 0.75, :age, :"@Exclude"n, :"@Filter"n ) )
    ),
    Transform Column(
        "Quantile...=0.25[height][age]",
        Formula( Col Quantile( :height, 0.25, :age, :"@Exclude"n, :"@Filter"n ) )
    ),
    Show Control Panel( 0 ),
    Variables(
        X( :age ),
        Y( :height ),
        Y( :"Quantile...=0.25[height][age]"n, Position( 1 ) ),
        Y( :"Quantile...=0.75[height][age]"n, Position( 1 ) )
    ),
    Elements(
        Area( X, Y( 2 ), Y( 3 ), Legend( 5 ), Area Style( "Range" ) ),
        Line( X, Y( 1 ), Legend( 6 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Level Name( 0, "IQR" ),
                Properties( 0, {Transparency( 0.33 )} )
            )}
        ),
        Dispatch( {}, "400", LegendBox, {Set Title( "" )} )
    )
);
```

**Stacked area chart**

``` jsl
Open( "$SAMPLE_DATA/Corn Wheat Soybean Production.jmp" );
// stacked area
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Year ),
        Y( :Commodity Acres Planted ),
        Group X( :State, Show Title( 0 ) ),
        Overlay( :Commodity )
    ),
    Elements( Area( X, Y, Legend( 40 ) ) ),
    Local Data Filter(
        Add Filter( columns( :State ), Where( :State == {"IOWA", "NEBRASKA", "OKLAHOMA"} ) )
    ),
    SendToReport(
        Dispatch( {}, "Commodity Acres Planted", ScaleBox, {Format( "Engineering SI", 13 )} ),
        Dispatch( {}, "400", LegendBox, {Legend Position( {40, [2, 1, 0, -3, -3, -3]} )} )
    )
);
```

### [Item Messages](#item-messages)[](#item-messages "Click to copy url")

#### [Area Style](#area-style)[](#area-style "Click to copy url")

**Syntax:** obj \<\< Area Style( "Stacked"\|"Overlaid"\|"Range"\|"Stacked Range" )

#### [Connection](#connection)[](#connection "Click to copy url")

**Syntax:** obj \<\< Connection( "Line"\|"Arrow"\|"Curve"\|"Step"\|"Centered Step"\|"Horizontal"\|"Vertical" )

#### [Error Interval](#error-interval)[](#error-interval "Click to copy url")

**Syntax:** obj \<\< Error Interval( "Auto"\|"None"\|"Range"\|"Interquartile Range"\|"Standard Error"\|"Standard Deviation"\|"Confidence Interval"\|"Median Absolute Deviation"\|"Custom Interval"\|"Two-way Interval" )

#### [Interval Style](#interval-style)[](#interval-style "Click to copy url")

**Syntax:** obj \<\< Interval Style( "Error Bar"\|"Band"\|"Hash Band"\|"Arrow" )

#### [Missing Factors](#missing-factors)[](#missing-factors "Click to copy url")

**Syntax:** obj \<\< Missing Factors( "Skip"\|"Treat as Missing"\|"Treat as Zero" )

**Description:** How to show connections that span missing factor levels

**JMP Version Added:** 15

#### [Missing Values](#missing-values)[](#missing-values "Click to copy url")

**Syntax:** obj \<\< Missing Values( "Connect Through"\|"Connect Faded"\|"Connect Dashed"\|"No Connection" )

**Description:** How to show connections that span missing values.

#### [Ordering](#ordering)[](#ordering "Click to copy url")

**Syntax:** obj \<\< Ordering( "Auto"\|"Row Order"\|"Summarized"\|"Within Row" )

#### [Response Axis](#response-axis)[](#response-axis "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Row order](#row-order)[](#row-order "Click to copy url")

**Syntax:** obj \<\< Row order( state=0\|1 )

#### [Save Summary Formula](#save-summary-formula)[](#save-summary-formula "Click to copy url")

**Syntax:** obj \<\< Save Summary Formula

#### [Smoothness](#smoothness)[](#smoothness "Click to copy url")

**Syntax:** obj \<\< Smoothness( number )

#### [Stack Negative](#stack-negative)[](#stack-negative "Click to copy url")

**Syntax:** obj \<\< Stack Negative( "Overlap"\|"Separate Negative"\|"Treat as Zero" )

**Description:** Controls how negative data values are handled when stacked.

**JMP Version Added:** 17

#### [Summary Statistic](#summary-statistic)[](#summary-statistic "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

## [Associated Constructors](#associated-constructors_1)[](#associated-constructors_1 "Click to copy url")

### [Graph Builder](#graph-builder_1)[](#graph-builder_1 "Click to copy url")

**Syntax:** Graph Builder( Variables( X(column ), Y( column ), \<Group X( column )\>, \<Group Y( column )\>, \<Shape( column )\>, \<Color( column )\>, \<Overlay( column )\>, \<Freq( column )\> ), \<Elements(...)\> ) )

**Description:** Provides an interactive graphical interface that enables you to explore your data. You can drag columns into graph zones to create a variety of graphs including scatterplots, contour plots, bar charts, area charts, box plots, histograms, heat maps, pie charts, treemaps, mosaic plots, and maps.

#### [100% stacked bar chart](#100-stacked-bar-chart)[](#100-stacked-bar-chart "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// 100% stacked bar chart, custom legend colors
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Age ), Y( :Cholesterol ), Overlay( :Alcohol Use ) ),
    Elements(
        Bar( X, Y, Legend( 55 ), Bar Style( "Stacked" ), Summary Statistic( "% of Factor" ) )
    ),
    SendToReport(
        Dispatch( {}, "Cholesterol", ScaleBox, {Max( 1 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                55,
                Properties( 0, {Fill Color( RGB Color( 0.9, 0.9, 0.9 ) )} ),
                Properties( 1, {Fill Color( RGB Color( 1.0, 0.8, 0.8 ) )} ),
                Properties( 2, {Fill Color( RGB Color( 1.0, 0.6, 0.6 ) )} ),
                Properties( 3, {Fill Color( RGB Color( 1.0, 0.3, 0.3 ) )} )
            )}
        )
    )
);
```

#### [Arrow lines, one per row](#arrow-lines-one-per-row)[](#arrow-lines-one-per-row "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Cholesterol.jmp" );
// arrow lines, one per row
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :April AM ),
        X( :April PM, Position( 1 ) ),
        Y( :June AM ),
        Y( :June PM, Position( 1 ) ),
        Overlay( :treatment )
    ),
    Elements(
        Line(
            X( 1 ),
            X( 2 ),
            Y( 1 ),
            Y( 2 ),
            Legend( 8 ),
            Ordering( "Within Row" ),
            Connection( "Arrow" )
        )
    )
);
```

#### [Axis summary table](#axis-summary-table)[](#axis-summary-table "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// caption axis table
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :sex ), Y( :height ) ),
    Elements(
        Bar( X, Y, Legend( 4 ) ),
        Caption Box(
            X,
            Y,
            Legend( 5 ),
            Summary Statistic( "Mean" ),
            Summary Statistic 2( "N" ),
            Location( "Axis Table" )
        )
    )
);
```

#### [Bar chart and smooth trend line combination](#bar-chart-and-smooth-trend-line-combination)[](#bar-chart-and-smooth-trend-line-combination "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Spring.jmp" );
// bar chart and smooth trend line combination, left and right y axes
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :April ), Y( :Temp ), Y( :Precip, Position( 1 ), Side( "Right" ) ) ),
    Elements(
        Points( X, Y( 1 ), Legend( 12 ) ),
        Smoother( X, Y( 1 ), Legend( 13 ) ),
        Bar( X, Y( 2 ), Legend( 16 ) )
    ),
    SendToReport(
        Dispatch( {}, "Precip", ScaleBox,
            {Format( "Best", 12 ), Max( 5 ), Inc( 1 ), Minor Ticks( 1 )}
        )
    )
);
```

#### [Binomial proportion confidence interval](#binomial-proportion-confidence-interval)[](#binomial-proportion-confidence-interval "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Bands Data.jmp" );
// binomial proportion confidence interval
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Show Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables( X( :customer ), Y( :Banding? ) ),
    Elements(
        Points( X, Y, Legend( 3 ) ),
        Line Of Fit( X, Y, Legend( 4 ), Means and Std Devs( 1 ) )
    ),
    Local Data Filter(
        Add Filter(
            columns( :customer ),
            Where( :customer == {"MODMAT", "REI", "ROSES", "SHEPLERS", "TARGET"} )
        )
    ),
    SendToReport(
        Dispatch( {}, "Banding?", ScaleBox,
            {Min( -0.07 ), Max( 1.07 ), Label Row( Show Major Grid( 1 ) )}
        )
    )
);
```

#### [Bubble chart with overlaid curves](#bubble-chart-with-overlaid-curves)[](#bubble-chart-with-overlaid-curves "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/SATByYear.jmp" );
// Smooth trend line, variable dot size, overlaid y variables, bubble chart. data filter
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :"% Taking (2004)"n ),
        Y( :SAT Verbal ),
        Y( :SAT Math, Position( 1 ) ),
        Size( :Population )
    ),
    Elements(
        Points( X, Y( 1 ), Y( 2 ), Legend( 7 ) ),
        Smoother( X, Y( 1 ), Y( 2 ), Legend( 8 ), Lambda( 0.45 ) )
    ),
    Local Data Filter( Add Filter( columns( :Year ), Where( :Year == 2004 ) ) ),
    SendToReport(
        Dispatch( {}, "% Taking (2004)", ScaleBox, {Format( "Percent", 12, 0 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 7, Properties( 0, {Marker Size( 6 )} ) )}
        )
    )
);
```

#### [Connected lines with overlaid dots](#connected-lines-with-overlaid-dots)[](#connected-lines-with-overlaid-dots "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Time Series/M3C Quarterly Wide Format.jmp" );
// connected lines with overlaid dots, custom markers, nested date axis
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Time ), Y( :N 646 ), Y( :N 647, Position( 1 ) ) ),
    Elements(
        Line( X, Y( 1 ), Y( 2 ), Legend( 10 ) ),
        Points( X, Y( 1 ), Y( 2 ), Legend( 11 ) )
    ),
    SendToReport(
        Dispatch( {}, "Time", ScaleBox,
            {Min( 2515958948 ), Max( 2872394250 ), Interval( "Quarter" ), Inc( 1 ),
            Minor Ticks( 0 ), Label Row Nesting( 2 ), Label Row( 1, Set Font Size( 12 ) )}
        ),
        Dispatch( {}, "N 646", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                10,
                Properties( 0, {Line Label Properties( {Last Label( 1 )} )} ),
                Properties( 1, {Line Label Properties( {Last Label( 1 )} )} )
            ), Legend Model(
                11,
                Base( 0, 0, 0, Item ID( "N 646", 1 ) ),
                Base( 1, 0, 1, Item ID( "N 647", 1 ) ),
                Properties( 0, {Marker( "FilledCircle" )} ),
                Properties( 1, {Marker( "Filled Up Triangle" )} )
            )}
        ),
        Dispatch( {}, "Graph Builder", FrameBox,
            {DispatchSeg(
                Line Seg( "Line (N 646)" ),
                Label Offset( "Last", 45, {2843799627.0183, 6317.56810988166} )
            ), DispatchSeg(
                Line Seg( "Line (N 647)" ),
                Label Offset( "Last", 45, {2857099451.70628, 4518.71614237549} )
            )}
        )
    )
);
```

#### [Contour plot and scatter plot points](#contour-plot-and-scatter-plot-points)[](#contour-plot-and-scatter-plot-points "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/CES Production Function.jmp" );
// contour plot and scatter plot points, smoothing, alpha shapes for non-convex hull
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Labor ), Y( :Capital ), Color( :Difference ) ),
    Elements(
        Contour(
            X,
            Y,
            Legend( 9 ),
            Boundary( 0 ),
            Number of Levels( 7 ),
            Alpha( 5 ),
            Smoothness( 0.2 )
        ),
        Points( X, Y, Color( 0 ), Legend( 10 ) )
    )
);
```

#### [Coplot-style trellis grouping](#coplot-style-trellis-grouping)[](#coplot-style-trellis-grouping "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Algorithm Data.jmp" );
// coplot style grouping using continuous grouping variables, smoother and scatter plot
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Alpha, Levels( 2 ) ),
        Y( :CPU Time ),
        Group X( :Beta, Levels( 2 ) ),
        Group Y( :Gamma, Levels( 2 ) ),
        Overlay( :Algorithm )
    ),
    Elements( Points( X, Y, Legend( 29 ) ), Smoother( X, Y, Legend( 30 ), Lambda( 0.25 ) ) )
);
```

#### [Independent charts using BY variable](#independent-charts-using-by-variable)[](#independent-charts-using-by-variable "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Financial.jmp" );
// by variable creates multiple Graph Builder instances
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :"Assets($Mil.)"n ), Y( :"Stockholder's Eq($Mil.)"n ), ),
    Elements( Points( X, Y, Legend( 17 ) ), Smoother( X, Y, Legend( 18 ) ) ),
    By( :Type )
);
```

#### [Left and right y axes](#left-and-right-y-axes)[](#left-and-right-y-axes "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Functional Data/Fermentation Process.jmp" );
// left and right y axes sharing a graph, overlaid lines
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Time ), Y( :pH ), Y( :Tank Level, Position( 1 ), Side( "Right" ) ) ),
    Elements( Line( X, Y( 1 ), Legend( 41 ) ), Line( X, Y( 2 ), Legend( 46 ) ) ),
    SendToReport( Dispatch( {}, "Time", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ) )
);
```

#### [Line with custom band interval](#line-with-custom-band-interval)[](#line-with-custom-band-interval "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// range area, custom interval, overlaid line, transparency
Graph Builder(
    Transform Column(
        "Quantile...=0.75[height][age]",
        Formula( Col Quantile( :height, 0.75, :age, :"@Exclude"n, :"@Filter"n ) )
    ),
    Transform Column(
        "Quantile...=0.25[height][age]",
        Formula( Col Quantile( :height, 0.25, :age, :"@Exclude"n, :"@Filter"n ) )
    ),
    Show Control Panel( 0 ),
    Variables(
        X( :age ),
        Y( :height ),
        Y( :"Quantile...=0.25[height][age]"n, Position( 1 ) ),
        Y( :"Quantile...=0.75[height][age]"n, Position( 1 ) )
    ),
    Elements(
        Area( X, Y( 2 ), Y( 3 ), Legend( 5 ), Area Style( "Range" ) ),
        Line( X, Y( 1 ), Legend( 6 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Level Name( 0, "IQR" ),
                Properties( 0, {Transparency( 0.33 )} )
            )}
        ),
        Dispatch( {}, "400", LegendBox, {Set Title( "" )} )
    )
);
```

#### [Linear regression panels](#linear-regression-panels)[](#linear-regression-panels "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Financial.jmp" );
// line of fit, regression, small multiples, custom group color, custom graph spacing
Graph Builder(
    Show Control Panel( 0 ),
    Grid Color( "Medium Light Gray" ),
    Grid Transparency( 0.25 ),
    Title Fill Color( "Medium Light Gray" ),
    Title Frame Color( "Medium Light Gray" ),
    Level Fill Color( {217, 217, 217} ),
    Level Frame Color( "Medium Light Gray" ),
    Level Spacing Color( "Medium Light Gray" ),
    Graph Spacing( 10 ),
    Variables( X( :"Assets($Mil.)"n ), Y( :"Stockholder's Eq($Mil.)"n ), Wrap( :Type ) ),
    Elements( Points( X, Y, Legend( 17 ) ), Line Of Fit( X, Y, Legend( 19 ) ) ),
    Local Data Filter(
        Add Filter( columns( :"Assets($Mil.)"n ), Where( :"Assets($Mil.)"n <= 60941 ) )
    )
);
```

#### [Mediterranean equal-area choropleth](#mediterranean-equal-area-choropleth)[](#mediterranean-equal-area-choropleth "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/World Demographics.jmp" );
// Mediterranean map, choropleth, equal area projection, grid lines
Graph Builder(
    Size( 1094, 586 ),
    Show Control Panel( 0 ),
    Variables( Color( :Total Median Age ), Shape( :Territory ) ),
    Elements( Map Shapes( Legend( 3 ) ) ),
    SendToReport(
        Dispatch( {}, "", ScaleBox,
            {Format( "Longitude DDD", "PUNDIR", 16 ), Min( -14.2917884823647 ),
            Max( 64.9684846475565 ), Inc( 20 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "", ScaleBox( 2 ),
            {Format( "Latitude DDD", "PUNDIR", 16 ), Min( 21.8020806509188 ),
            Max( 61.3932495299748 ), Inc( 10 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        )
    )
);
```

#### [Multiple x axes](#multiple-x-axes)[](#multiple-x-axes "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Algorithm Data.jmp" );
// mutiple x variables in separate panels, smoother with confidence intervals and scatter plot
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Alpha ), X( :Beta ), X( :Gamma ), Y( :CPU Time ), Overlay( :Algorithm ) ),
    Elements(
        Position( 1, 1 ),
        Points( X, Y, Legend( 39 ) ),
        Smoother( X, Y, Legend( 40 ), Lambda( 1.5 ), Confidence of Fit( 1 ) )
    ),
    Elements(
        Position( 2, 1 ),
        Points( X, Y, Legend( 41 ) ),
        Smoother( X, Y, Legend( 42 ), Lambda( 1.5 ), Confidence of Fit( 1 ) )
    ),
    Elements(
        Position( 3, 1 ),
        Points( X, Y, Legend( 43 ) ),
        Smoother( X, Y, Legend( 44 ), Lambda( 1.5 ), Confidence of Fit( 1 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 40, Properties( 2, {Line Color( RGB Color( 0.4, 0.4, 0.4 ) )} ) )}
        )
    )
);
```

#### [Napoleon's March flow diagram](#napoleons-march-flow-diagram)[](#napoleons-march-flow-diagram "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Napoleons March.jmp" );
// flow diagram
Graph Builder(
    Show Control Panel( 0 ),
    Show X Axis( 0 ),
    Show Y Axis( 0 ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables(
        X( :Longitude ),
        Y( :Latitude ),
        Overlay( :Group ),
        Color( :Direction ),
        Size( :Army Size )
    ),
    Elements(
        Line( X, Y, Legend( 3 ), Ordering( "Row Order" ), Missing Values( "No Connection" ) )
    ),
    SendToReport(
        Dispatch( {}, "Longitude", ScaleBox,
            {Min( 26.71 ), Max( 34.9 ), Inc( 2.5 ), Minor Ticks( 0 ),
            Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "Latitude", ScaleBox,
            {Min( 53.32 ), Max( 56.61 ), Inc( 0.5 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                3,
                Properties( 0, {Line Width( 10 )} ),
                Properties( 1, {RGB Color( 1, 0.69, 0.49 )} ),
                Properties( 2, {RGB Color( 0.47, 0.47, 0.47 )} )
            )}
        ),
        Dispatch( {}, "graph title", TextEditBox,
            {Set Text( "Napoleon's March to Moscow" )}
        ),
        Dispatch( {}, "Graph Builder", FrameBox,
            {Background Map( Images( "Detailed Earth", Transparency( 0.75 ) ) )}
        )
    )
);
```

#### [Overlaid bivariate kernel density contours](#overlaid-bivariate-kernel-density-contours)[](#overlaid-bivariate-kernel-density-contours "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// overlaid bivariate kernel density contour
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Culmen Depth ), Y( :Culmen Length ), Overlay( :Species ) ),
    Elements(
        Contour( X, Y, Legend( 6 ), Line( 1 ), Number of Levels( 5 ), Smoothness( 0.2174 ) )
    )
);
```

#### [Overlaid empirical cumulative distribution function curves](#overlaid-empirical-cumulative-distribution-function-curves)[](#overlaid-empirical-cumulative-distribution-function-curves "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// CDF, empirical cumulative distribution function
Graph Builder(
    Transform Column(
        "Rank[Culmen Length]@Overlay",
        Formula(
            Col Rank( :Culmen Length, :"@Exclude"n, :"@Filter"n, :"@Graph"n, :"@Overlay"n )
             / Col Number(
                :Culmen Length,
                :"@Exclude"n,
                :"@Filter"n,
                :"@Graph"n,
                :"@Overlay"n
            )
        )
    ),
    Show Control Panel( 0 ),
    Legend Position( "Inside Bottom Right" ),
    Show Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables(
        X( :Culmen Length ),
        Y( :"Rank[Culmen Length]@Overlay"n ),
        Overlay( :Species )
    ),
    Elements( Line( X, Y, Legend( 15 ), Connection( "Step" ) ) ),
    SendToReport(
        Dispatch( {}, "Rank[Culmen Length]@Overlay", ScaleBox, {Max( 1.0117745954803 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                15,
                Level Name( 0, "Adelie" ),
                Level Name( 1, "Chinstrap" ),
                Level Name( 2, "Gentoo" )
            )}
        )
    )
);
```

#### [Panels with unaligned y axes](#panels-with-unaligned-y-axes)[](#panels-with-unaligned-y-axes "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/US Regional Population.jmp" );
// panels with unaligned y axes
Graph Builder(
    Transform Column( "Transform[Year]", Continuous, Formula( Num( :Year ) ) ),
    Show Control Panel( 0 ),
    Extend Axis to Zero( 10 ),
    Link Page Axes( "X Only" ),
    Replicate Linked Page Axes( 0 ),
    Variables(
        X( :"Transform[Year]"n ),
        Y( :Population ),
        Page( :Region, Levels per Row( 3 ) )
    ),
    Elements( Points( X, Y, Legend( 3 ) ), Smoother( X, Y, Legend( 4 ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :Region ),
            Where(
                :Region == {"AR,LA,OK,TX", "Great Lakes", "KY,TN,AL,MS", "Midwest",
                "Mountain", "New England", "NY,NJ,PA", "Pacific", "South Atlantic"}
            )
        )
    ),
    SendToReport(
        Dispatch( {}, "Population", ScaleBox, {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 2 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 3 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 4 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 5 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 6 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 7 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 8 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 9 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Population", ScaleBox( 10 ), {Format( "Engineering SI", 10 )} ),
        Dispatch( {}, "Transform[Year]", TextEditBox, {Set Text( "Year" )} ),
        Dispatch( {}, "Transform[Year]", Text Edit Box( 2 ), {Set Text( "Year" )} ),
        Dispatch( {}, "Transform[Year]", Text Edit Box( 3 ), {Set Text( "Year" )} )
    )
);
```

#### [Parallel y axes, overlaid lines](#parallel-y-axes-overlaid-lines)[](#parallel-y-axes-overlaid-lines "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Functional Data/Fermentation Process.jmp" );
// parallel y axes, multiple y scales sharing a graph, overlaid lines
Graph Builder(
    Show Control Panel( 0 ),
    Parallel Axes( "Y Only" ),
    Variables(
        X( :Time ),
        Y( :Temp ),
        Y( :NH3 Feed ),
        Y( :Air ),
        Y( :Tank Level ),
        Y( :pH )
    ),
    Elements( Position( 1, 1 ), Line( X, Y, Legend( 37 ) ) ),
    Elements( Position( 1, 2 ), Line( X, Y, Legend( 39 ) ) ),
    Elements( Position( 1, 3 ), Line( X, Y, Legend( 40 ) ) ),
    Elements( Position( 1, 4 ), Line( X, Y, Legend( 41 ) ) ),
    Elements( Position( 1, 5 ), Line( X, Y, Legend( 42 ) ) ),
    SendToReport( Dispatch( {}, "Time", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ) )
);
```

#### [Points and smoother](#points-and-smoother)[](#points-and-smoother "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
```

#### [Scatter plot with marginal box plots](#scatter-plot-with-marginal-box-plots)[](#scatter-plot-with-marginal-box-plots "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// scatter plot with marginal box plots, custom graph sizes
Graph Builder(
    Transform Column( "dummy1", Nominal, Formula( 1 ) ),
    Transform Column( "dummy2", Nominal, Formula( 1 ) ),
    Show Control Panel( 0 ),
    Variables(
        X( :Delta 13 C ),
        X( :dummy1 ),
        Y( :dummy2 ),
        Y( :Delta 15 N ),
        Color( :Sex ),
        Size( :Body Mass )
    ),
    Relative Sizes( "X", [100 10] ),
    Relative Sizes( "Y", [10 100] ),
    Elements( Position( 1, 1 ), Box Plot( X, Y, Color( 0 ), Size( 0 ), Legend( 12 ) ) ),
    Elements( Position( 1, 2 ), Points( X, Y, Legend( 4 ) ) ),
    Elements( Position( 2, 1 ) ),
    Elements( Position( 2, 2 ), Box Plot( X, Y, Color( 0 ), Size( 0 ), Legend( 13 ) ) ),
    SendToReport(
        Dispatch( {}, "dummy1", ScaleBox, {Label Row( Show Major Labels( 0 ) )} ),
        Dispatch( {}, "dummy2", ScaleBox, {Label Row( Show Major Labels( 0 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                4,
                Properties( 1, {Transparency( 0.75 )} ),
                Properties( 2, {Transparency( 0.75 )} )
            )}
        ),
        Dispatch( {}, "dummy1", TextEditBox, {Set Text( "" )} ),
        Dispatch( {}, "dummy2", TextEditBox, {Set Text( "" )} ),
        Dispatch( {}, "400", LegendBox,
            {Legend Position( {12, [1, -3], 4, [0, 3, 4], 13, [2, -3]} )}
        )
    )
);
```

#### [Variability chart](#variability-chart)[](#variability-chart "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Variability Data/2 Factors Nested.jmp" );
// variability chart, mean and range interval, nested axis
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Operator ), X( :Part, Position( 1 ) ), Y( :Y ) ),
    Elements(
        Points(
            X( 1 ),
            X( 2 ),
            Y,
            Legend( 3 ),
            Summary Statistic( "Mean" ),
            Error Interval( "Range" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Operator", ScaleBox, {Label Row( 2, Show Major Grid( 1 ) )} )
    )
);
```

#### [Violin plots with quartiles](#violin-plots-with-quartiles)[](#violin-plots-with-quartiles "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// violin plots, overlaid median line and quartile intervals
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ) ),
    Elements(
        Contour( X, Y, Legend( 3 ) ),
        Bar(
            X,
            Y,
            Legend( 4 ),
            Bar Style( "Float" ),
            Summary Statistic( "Median" ),
            Error Interval( "Interquartile Range" )
        )
    )
);
```

#### [Wafer map](#wafer-map)[](#wafer-map "Click to copy url")

``` jsl
Open( "$SAMPLE_DATA/Wafer Stacked.jmp" );
// wafer map, heat map, trellis, wrap arrangement
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :X_Die ), Y( :Y_Die ), Wrap( :Wafer ), Color( :Defects ) ),
    Elements( Heatmap( X, Y, Legend( 8 ) ) ),
    SendToReport(
        Dispatch( {}, "X_Die", ScaleBox, {Minor Ticks( 9 )} ),
        Dispatch( {}, "Y_Die", ScaleBox, {Minor Ticks( 9 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                8,
                Properties( 0, {gradient( {Color Theme( "White to Orange" )} )} )
            )}
        )
    )
);
```

## [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

### [Add Element](#add-element)[](#add-element "Click to copy url")

**Syntax:** obj \<\< Add Element( xposition, yposition, {Type(element name), X(i=1), Y(i=1), options...} )

**Description:** Adds a new graph element at the given X and Y positions. The element specification includes the element name, which data roles it uses its option values.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 0.5 );
gb << Add Element( 1, 1, {Type( "Line Of Fit" ), X, Y, Degree( "Quadratic" )} );
```

### [Add Variable](#add-variable)[](#add-variable "Click to copy url")

**Syntax:** obj \<\< Add Variable( {column, Role(role), Position(p=1), Inner Position(i=1)}, \< \<\<Method("insert"\|"merge"\|"replace")\> )

**Description:** Adds a new variable to the Graph Builder model, with a given role and position.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 0.5 );
gb << Add Variable( {:age, Role( "Wrap" )} );
```

### [Auto Stretching](#auto-stretching)[](#auto-stretching "Click to copy url")

**Syntax:** obj \<\< Auto Stretching( state=0\|1 )

**Description:** Toggles the automatic stretching of the graph with the containing window. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Auto Stretching( 0 );
```

### [Back Color](#back-color)[](#back-color "Click to copy url")

**Syntax:** obj \<\< Back Color( color )

**Description:** Sets the color for the entire background around the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Back Color( "Yellow" );
```

### [Categorical Color Theme](#categorical-color-theme)[](#categorical-color-theme "Click to copy url")

**Syntax:** obj \<\< Categorical Color Theme

**Description:** Sets the color theme used for categories.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Categorical Color Theme( "Pastel" );
```

### [Continuous Color Theme](#continuous-color-theme)[](#continuous-color-theme "Click to copy url")

**Syntax:** obj \<\< Continuous Color Theme

**Description:** Sets the color theme used for gradients.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Continuous Color Theme( "White to Black" );
```

### [Done](#done)[](#done "Click to copy url")

**Syntax:** obj \<\< Done

**Description:** Hides the control panel and turns off any row sampling.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Done;
```

### [Elements](#elements)[](#elements "Click to copy url")

**Syntax:** Elements( Points( X, Y )\| Box plot( X, Y, Jitter( state=0\|1 ), Outliers( state=0\|1 ), Box Style( "Outlier"\|"Quantile" ) )\|Line( X, Y, Row Order( number ), Summary Statistic( ) )\| Histogram( X, Y)\| Bar( X, Y, Bar Style(), Summary Statistic() )\| Contour(X, Y)\| Smoother(X, Y)\|Map Shapes(Summary Statistic() ))

**Description:** Identifies the elements of the visualization.

``` jsl
dt = Open( "$SAMPLE_DATA/PopAgeGroup.jmp" );
gb = dt << Graph Builder(
    Variables( X( :"F Rate 0-19"n ), Y( :Region ) ),
    Elements( Box Plot( X, Y ), Line( X, Y, Summary Statistic( "Mean" ) ) )
);
```

### [Error Bar Offset](#error-bar-offset)[](#error-bar-offset "Click to copy url")

**Syntax:** obj \<\< Error Bar Offset

**Description:** Opens a dialog to set the offset for error bars.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 1 );
gb << Error Bar Offset( 0.01 );
```

### [Extend Axis to Zero](#extend-axis-to-zero)[](#extend-axis-to-zero "Click to copy url")

**Syntax:** obj \<\< Extend Axis to Zero( multiplier=1 )

**Description:** Multiplier for the amount an axis scale is extended to include zero. "1" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Extend Axis to Zero( 10 ),
    Variables( X( :Weight ), Y( :Height ) ),
    Elements( Line( X, Y ) )
);
```

### [Extend Dual Axes to Zero](#extend-dual-axes-to-zero)[](#extend-dual-axes-to-zero "Click to copy url")

**Syntax:** obj \<\< Extend Dual Axes to Zero( multiplier=2 )

**Description:** Multiplier for the amount an axis scale is extended to include zero when there are both left and right axes. "2" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Size( 513, 465 ),
    Extend Dual Axes to Zero( 10 ),
    Variables( X( :age ), Y( :weight, Side( "Right" ) ), Y( :height, Position( 1 ) ) ),
    Elements( Line( X, Y( 2 ) ), Line( X, Y( 1 ) ) )
);
```

### [Extend Parallel Y Axes to Zero](#extend-parallel-y-axes-to-zero)[](#extend-parallel-y-axes-to-zero "Click to copy url")

**Syntax:** obj \<\< Extend Parallel Y Axes to Zero( multiplier=3 )

**Description:** Multiplier for the amount an axis scale is extended to include zero when in Parallel Y Axes mode. "3" by default.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Show Control Panel( 0 ),
    Parallel Axes( "Y Only" ),
    Extend Parallel Y Axes to Zero( 0 ),
    Variables( X( :age ), Y( :height ), Y( :weight ) ),
    Elements( Position( 1, 1 ), Line( X, Y ) ),
    Elements( Position( 1, 2 ), Line( X, Y ) )
);
```

### [Fit to Window](#fit-to-window)[](#fit-to-window "Click to copy url")

**Syntax:** obj \<\< Fit to Window( "Auto"\|"On"\|"Off"\|"Maintain Aspect Ratio" )

**Description:** Sets the auto stretching behavior of the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Fit to Window( "Off" );
```

### [Get Element](#get-element)[](#get-element "Click to copy url")

**Syntax:** obj \<\< Get Element( xposition, yposition, i )

**Description:** Returns a graph element specifications for the given x and y positions.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Get Element( 1, 1, 1 );
```

### [Get Elements](#get-elements)[](#get-elements "Click to copy url")

**Syntax:** obj \<\< Get Elements( xposition, yposition )

**Description:** Returns a list of element specifications for the given x and y positions.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Get Elements( 1, 1 );
```

### [Get Legend Display](#get-legend-display)[](#get-legend-display "Click to copy url")

**Syntax:** obj \<\< Get Legend Display

**Description:** Returns the Legend Display Box for the graph that can be queried or modified.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Overlay( :sex ), Color( :age ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
lgnd = gb << Get Legend Display;
item = lgnd << Get Item( 2, 1 );
item << Set Visible( 0 );
```

### [Get Legend Server](#get-legend-server)[](#get-legend-server "Click to copy url")

**Syntax:** obj \<\< Get Legend Server

**Description:** Returns an object holding information used by the Legend Display and corresponding Display Segs in the graph.

**JMP Version Added:** 16

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Variables( X( :height ), Y( :weight ), Overlay( :sex ), Color( :age ) ),
    Elements( Points( X, Y, Legend( 1 ) ), Smoother( X, Y, Legend( 2 ) ) )
);
lgnd = gb << Get Legend Server;
items = lgnd << Get Legend Items;
Show( items );
```

### [Get N Elements](#get-n-elements)[](#get-n-elements "Click to copy url")

**Syntax:** obj \<\< Get N Elements( xposition, yposition )

**Description:** Returns the number of graph elements for the given x and y positions.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Get N Elements( 1, 1 );
```

### [Get N Positions](#get-n-positions)[](#get-n-positions "Click to copy url")

**Syntax:** nrole

**Description:** Returns the number of positions in use for a given role.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Get N Positions( "X" );
```

### [Get N Variables](#get-n-variables)[](#get-n-variables "Click to copy url")

**Syntax:** n = obj \<\< Get N Variables

**Description:** Returns the number of variables in use.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Get N Variables();
```

### [Get Variable](#get-variable)[](#get-variable "Click to copy url")

**Syntax:** obj \<\< Get Variable( index )

**Description:** Returns a variable specification.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Get Variable( 1 );
```

### [Get Variables](#get-variables)[](#get-variables "Click to copy url")

**Syntax:** list = obj \<\< Get Variables

**Description:** Returns a list of variable specification lists for the variables in use.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Get Variables();
```

### [Graph Spacing](#graph-spacing)[](#graph-spacing "Click to copy url")

**Syntax:** obj \<\< Graph Spacing( gap=1 )

**Description:** Sets the amount of space between graph panels. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Add Variable( {:age, Role( "Wrap" )} );
gb << Graph Spacing( 3 );
```

### [Grid Color](#grid-color)[](#grid-color "Click to copy url")

**Syntax:** obj \<\< Grid Color( color )

**Description:** Sets the color for the grid lines on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Graph Spacing( 5 ),
    Variables( X( :height ), Y( :weight ), Wrap( :age ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Grid Color( "Red" );
```

### [Grid Transparency](#grid-transparency)[](#grid-transparency "Click to copy url")

**Syntax:** obj \<\< Grid Transparency( fraction=1 )

**Description:** Sets the transparency for the grid lines. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Graph Spacing( 5 ),
    Variables( X( :height ), Y( :weight ), Wrap( :age ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Grid Transparency( 0.2 );
```

### [Include Missing Categories](#include-missing-categories)[](#include-missing-categories "Click to copy url")

**Syntax:** obj \<\< Include Missing Categories( state=0\|1 )

**Description:** Treats missing values as a separate level for categorical variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
:age[{10, 20, 30}] = .;
gb << Add Variable( {:age, Role( "Wrap" )} );
gb << Include Missing Categories( 1 );
```

### [Launch Analysis](#launch-analysis)[](#launch-analysis "Click to copy url")

**Syntax:** obj \<\< Launch Analysis

**Description:** Launches an analysis using the current variables.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Launch Analysis;
```

### [Legend Floating Offset](#legend-floating-offset)[](#legend-floating-offset "Click to copy url")

**Syntax:** obj \<\< Legend Floating Offset

**Description:** Sets the offset in pixels for the legend when the Legend Position is set to "Floating"

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Legend Position( "Inside Floating" );
```

### [Legend Position](#legend-position)[](#legend-position "Click to copy url")

**Syntax:** obj \<\< Legend Position( "Right"\|"Bottom"\|"Inside Left"\|"Inside Right"\|"Inside Bottom Left"\|"Inside Bottom Right"\|"Inside Floating" )

**Description:** Sets the position of the legend.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Legend Position( "Bottom" );
```

### [Legend Settings](#legend-settings)[](#legend-settings "Click to copy url")

**Syntax:** obj \<\< Legend Settings

**Description:** Opens a dialog to modify the properties of the legend.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 1 );
gb << Legend Settings();
```

### [Level Fill Color](#level-fill-color)[](#level-fill-color "Click to copy url")

**Syntax:** obj \<\< Level Fill Color( color )

**Description:** Sets the color for the level names on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Level Fill Color( {103, 214, 214} );
```

### [Level Frame Color](#level-frame-color)[](#level-frame-color "Click to copy url")

**Syntax:** obj \<\< Level Frame Color( color )

**Description:** Sets the color for the lines around the level names on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Level Frame Color( "Blue" );
```

### [Level Spacing Color](#level-spacing-color)[](#level-spacing-color "Click to copy url")

**Syntax:** obj \<\< Level Spacing Color( color )

**Description:** Sets the color of the spacing between level labels.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Level Spacing Color( "Blue" );
```

### [Level Spacing Transparency](#level-spacing-transparency)[](#level-spacing-transparency "Click to copy url")

**Syntax:** obj \<\< Level Spacing Transparency( fraction=1 )

**Description:** Sets the transparency for the spacing between level labels. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Level Spacing Transparency( .2 );
```

### [Level Text Color](#level-text-color)[](#level-text-color "Click to copy url")

**Syntax:** obj \<\< Level Text Color( color )

**Description:** Sets the color for the level name text on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Level Text Color( "Red" );
```

### [Level Transparency](#level-transparency)[](#level-transparency "Click to copy url")

**Syntax:** obj \<\< Level Transparency( fraction=1 )

**Description:** Sets the transparency for the level name frame on the graph. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Level Transparency( .2 );
```

### [Level Underline](#level-underline)[](#level-underline "Click to copy url")

**Syntax:** obj \<\< Level Underline( state=0\|1 )

**Description:** Underlines the level names or removes the underline on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Level Frame Color( "Blue" );
gb << Level Underline( 1 );
```

### [Lighten large fills](#lighten-large-fills)[](#lighten-large-fills "Click to copy url")

**Syntax:** obj \<\< Lighten large fills( state=0\|1 )

**Description:** Automatically lighten colors for pie, treemap and mosaic elements, which fill large areas. On by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Lighten large fills( 1 );
```

### [Link Page Axes](#link-page-axes)[](#link-page-axes "Click to copy url")

**Syntax:** obj \<\< Link Page Axes( "None"\|"X Only"\|"Y Only"\|"X and Y" )

**Description:** Sets which axes are linked across page group levels.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Size( 470, 552 ),
    Variables( X( :height ), Y( :weight ), Page( :sex ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Link Page Axes( "Y Only" );
```

### [Lock Scales](#lock-scales)[](#lock-scales "Click to copy url")

**Syntax:** obj \<\< Lock Scales( state=0\|1 )

**Description:** Locks axis and gradient ranges so they do not change in response to data or filtering changes.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Lock Scales( 1 );
```

### [Make into Data Table](#make-into-data-table)[](#make-into-data-table "Click to copy url")

**Syntax:** obj \<\< Make into Data Table

**Description:** Creates a new data table containing images of graphs.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Make into Data Table;
```

### [Order Statistic](#order-statistic)[](#order-statistic "Click to copy url")

**Syntax:** obj \<\< Order Statistic( "N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile"="Mean" )

**Description:** Sets the default order based on a summary statistic used when using the Order By message for a variable in the graph. "Mean" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/PopAgeGroup.jmp" );
gb = dt << Graph Builder(
    Order Statistic( "Max" ),
    Variables( X( :"F Rate 0-19"n ), Y( :Region, Order By( :"F Rate 0-19"n, Ascending ) ) ),
    Elements( Box Plot( X, Y ) )
);
```

### [Overlay Auto Line Styles Limit](#overlay-auto-line-styles-limit)[](#overlay-auto-line-styles-limit "Click to copy url")

**Syntax:** obj \<\< Overlay Auto Line Styles Limit( count=6 )

**Description:** Limits the number of overlay levels where the Overlay Encoding will use line styles for its Auto setting in the presence of a color variable. "6" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Overlay Auto Line Styles Limit( 0 ),
    Variables( X( :Weight ), Y( :Height ), Overlay( :sex ), Color( :Age ) ),
    Elements( Line( X, Y ) )
);
```

### [Overlay Auto Marker Styles Limit](#overlay-auto-marker-styles-limit)[](#overlay-auto-marker-styles-limit "Click to copy url")

**Syntax:** obj \<\< Overlay Auto Marker Styles Limit( count=62 )

**Description:** Limits the number of overlay levels where the Overlay Encoding will use marker styles for its Auto setting in the presence of a color variable. "62" by default.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Overlay Auto Marker Styles Limit( 0 ),
    Variables( X( :Weight ), Y( :Height ), Overlay( :sex ), Color( :Age ) ),
    Elements( Points( X, Y ) )
);
```

### [Page Count Limit](#page-count-limit)[](#page-count-limit "Click to copy url")

**Syntax:** obj \<\< Page Count Limit( count=200 )

**Description:** Sets the maximum number of pages created for the page variable, to avoid accidental performance degradation. "200" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Page( :Name ) ),
    Elements( Points( X, Y ) )
);
gb << Page Count Limit( 5 );
```

### [Page Gap Size](#page-gap-size)[](#page-gap-size "Click to copy url")

**Syntax:** obj \<\< Page Gap Size( gap=25 )

**Description:** Sets the amount of space between page groups. "25" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Page( :Sex ) ),
    Elements( Smoother( X, Y ) )
);
gb << Page Gap Size( 3 );
```

### [Page Level Fill Color](#page-level-fill-color)[](#page-level-fill-color "Click to copy url")

**Syntax:** obj \<\< Page Level Fill Color( color )

**Description:** Sets the color for the level names on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Page( :Sex ) ),
    Elements( Smoother( X, Y ) )
);
gb << Page Level Fill Color( {103, 214, 214} );
```

### [Page Level Frame Color](#page-level-frame-color)[](#page-level-frame-color "Click to copy url")

**Syntax:** obj \<\< Page Level Frame Color( color )

**Description:** Sets the color for the lines around the level names on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Page( :Sex ) ),
    Elements( Smoother( X, Y ) )
);
gb << Page Level Frame Color( "Blue" );
```

### [Page Level Text Color](#page-level-text-color)[](#page-level-text-color "Click to copy url")

**Syntax:** obj \<\< Page Level Text Color( color )

**Description:** Sets the color for the level name text on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Page( :Sex ) ),
    Elements( Smoother( X, Y ) )
);
gb << Page Level Text Color( "Red" );
```

### [Page Level Transparency](#page-level-transparency)[](#page-level-transparency "Click to copy url")

**Syntax:** obj \<\< Page Level Transparency( fraction=1 )

**Description:** Sets the transparency for the level name frame on the graph. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Page( :Sex ) ),
    Elements( Smoother( X, Y ) )
);
gb << Page Level Transparency( .2 );
```

### [Page Level Underline](#page-level-underline)[](#page-level-underline "Click to copy url")

**Syntax:** obj \<\< Page Level Underline( state=0\|1 )

**Description:** Underlines the level names or removes the underline on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Page( :Sex ) ),
    Elements( Smoother( X, Y ) )
);
gb << Page Level Frame Color( "Blue" );
gb << Page Level Underline( 1 );
```

### [Parallel Axis Merging](#parallel-axis-merging)[](#parallel-axis-merging "Click to copy url")

**Syntax:** obj \<\< Parallel Axis Merging( "Always"\|"Low Similarity"\|"Medium Similarity"\|"High Similarity"\|"Never" )

**Description:** Determines when the automatic Combine Scales setting should choose Parallel Merged instead of Parallel Independent.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Parallel Axis Merging( "Never" );
```

### [Parallel Y Axes](#parallel-y-axes)[](#parallel-y-axes "Click to copy url")

**Syntax:** obj \<\< Parallel Y Axes( state=0\|1 )

**Description:** All Y axes share the same graph. Like parallel coordinates but supporting an X variable.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :age ), Y( :height ), Y( :weight ) ),
    Elements( Position( 1, 1 ), Points( X, Y ), Smoother( X, Y ) ),
    Elements( Position( 1, 2 ), Points( X, Y ), Smoother( X, Y ) )
);
gb << Parallel Y Axes( 1 );
```

### [Random Seed](#random-seed)[](#random-seed "Click to copy url")

**Syntax:** obj \<\< Random Seed( number )

**Description:** Sets a specific seed for random jitter.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Sex ), Y( :Height ) ),
    Elements( Points( X, Y, Jitter( "Random Uniform" ) ) )
);
Wait( 1 );
gb << Random Seed( 123456 );
```

### [Relative Sizes](#relative-sizes)[](#relative-sizes "Click to copy url")

**Syntax:** Relative Sizes(axis, matrix of relative size values)

**Description:** Determines the proportion of space allotted to each of multiple axes in a series.

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
Graph Builder(
    Size( 435, 352 ),
    Show Control Panel( 0 ),
    Variables( X( :weight ), Y( :height ), Y( :sex ) ),
    Relative Sizes( "Y", [4 1] ),
    Elements( Position( 1, 1 ), Points( X, Y ) ),
    Elements( Position( 1, 2 ), Points( X, Y ) )
);
```

### [Remove Element](#remove-element)[](#remove-element "Click to copy url")

**Syntax:** obj \<\< Remove Element( xposition, yposition, i )

**Description:** Removes a graph element at the given X and Y positions.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 0.5 );
gb << Remove Element( 1, 1, 2 );
```

### [Remove Variable](#remove-variable)[](#remove-variable "Click to copy url")

**Syntax:** obj \<\< Remove Variable( index \| {column, Role(role), Position(p=1), Inner Position(i=1)} )

**Description:** Removes a variable from the Graph Builder model, specified by either the index or a given column name, role, and position.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 0.5 );
gb << Add Variable( {:age, Role( "Wrap" )} );
Wait( 0.5 );
gb << Remove Variable( 3 );
```

### [Replicate Linked Page Axes](#replicate-linked-page-axes)[](#replicate-linked-page-axes "Click to copy url")

**Syntax:** obj \<\< Replicate Linked Page Axes( state=0\|1 )

**Description:** Determines whether linked pages axis in a grid are displayed once for each graph or once for each row or column of graphs.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Size( 470, 552 ),
    Variables( X( :height ), Y( :weight ), Page( :age ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Link Page Axes( "X and Y" );
gb << Replicate Linked Page Axes( 1 );
```

### [Sampling](#sampling)[](#sampling "Click to copy url")

**Syntax:** obj \<\< Sampling( number )

**Description:** Randomly selects a subset of the data using a specified proportion or count. This is useful when the data is large and the graph is still being changed.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Sampling( 20 );
```

### [Set Alpha Level](#set-alpha-level)[](#set-alpha-level "Click to copy url")

**Syntax:** obj \<\< Set Alpha Level( 0.10\|0.05\|0.01\|Other... )

**Description:** Changes the alpha level used for the confidence curves.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Set Alpha Level( 0.10 );
```

### [Set α Level](#set-level)[](#set-level "Click to copy url")

**Syntax:** obj \<\< Set α Level( 0.10\|0.05\|0.01\|Other... )

**Description:** Changes the alpha level used for the confidence curves.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Set Alpha Level( 0.10 );
```

### [Show Control Panel](#show-control-panel)[](#show-control-panel "Click to copy url")

**Syntax:** obj \<\< Show Control Panel( state=0\|1 )

**Description:** Displays or hides the control panel. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show Control Panel( 1 );
```

### [Show Excluded Rows](#show-excluded-rows)[](#show-excluded-rows "Click to copy url")

**Syntax:** obj \<\< Show Excluded Rows( state=0\|1 )

**Description:** Shows or hides excluded rows on plots. When this option is selected, excluded rows are included in the count of out of control points, but excluded from numerical calculations.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
dt << Select Rows( 1 :: 5 );
dt << Exclude();
gb << Show Excluded Rows( 1 );
```

### [Show Footer](#show-footer)[](#show-footer "Click to copy url")

**Syntax:** obj \<\< Show Footer( state=0\|1 )

**Description:** Displays or hides the footer text. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show Footer( 0 );
```

### [Show Legend](#show-legend)[](#show-legend "Click to copy url")

**Syntax:** obj \<\< Show Legend( state=0\|1 )

**Description:** Displays or hides the legend to the right of the graph. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show Legend( 1 );
```

### [Show Subtitle](#show-subtitle)[](#show-subtitle "Click to copy url")

**Syntax:** obj \<\< Show Subtitle( state=0\|1 )

**Description:** Displays or hides the graph subtitle.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show Subtitle( 1 );
```

### [Show Title](#show-title)[](#show-title "Click to copy url")

**Syntax:** obj \<\< Show Title( state=0\|1 )

**Description:** Displays or hides the graph title. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show Title( 0 );
```

### [Show X Axis](#show-x-axis)[](#show-x-axis "Click to copy url")

**Syntax:** obj \<\< Show X Axis( state=0\|1 )

**Description:** Displays or hides the X axis. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show X Axis( 0 );
```

### [Show X Axis Title](#show-x-axis-title)[](#show-x-axis-title "Click to copy url")

**Syntax:** obj \<\< Show X Axis Title( state=0\|1 )

**Description:** Displays or hides the X axis title. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show X Axis Title( 0 );
```

### [Show Y Axis](#show-y-axis)[](#show-y-axis "Click to copy url")

**Syntax:** obj \<\< Show Y Axis( state=0\|1 )

**Description:** Displays or hides the Y axis. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show Y Axis( 0 );
```

### [Show Y Axis Title](#show-y-axis-title)[](#show-y-axis-title "Click to copy url")

**Syntax:** obj \<\< Show Y Axis Title( state=0\|1 )

**Description:** Displays or hides the Y axis title. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Show Y Axis Title( 0 );
```

### [Size](#size)[](#size "Click to copy url")

**Syntax:** obj \<\< Size( width, height )

**Description:** Sets the size of the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Size( 808, 586 );
```

### [Spacing Borders](#spacing-borders)[](#spacing-borders "Click to copy url")

**Syntax:** obj \<\< Spacing Borders( 0\|1=0 )

**Description:** Sets the borders for the internal graph panels. "0" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Spacing Borders( 1 );
```

### [Subtitle Alignment](#subtitle-alignment)[](#subtitle-alignment "Click to copy url")

**Syntax:** obj \<\< Subtitle Alignment( "Left"\|"Center"\|"Right"\|"Auto" )

**Description:** Sets the alignment of the graph subtitle.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Subtitle Alignment( "Left" );
```

### [Subtitle Span](#subtitle-span)[](#subtitle-span "Click to copy url")

**Syntax:** obj \<\< Subtitle Span( "Full"\|"Graph contents" )

**Description:** Sets the span of the graph subtitle.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Subtitle Span( "Graph" );
```

### [Summary Statistic](#summary-statistic_1)[](#summary-statistic_1 "Click to copy url")

**Syntax:** Summary Statistic( N\|Mean\|Min\|Max\|Sum\|% of Total )

**Description:** Sets the default summary statistic used by the different elements in the graph. Mean by default for Bar and Line elements. "Mean" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Age ), Y( :Height ), Y( :weight, Position( 1 ) ) ),
    Summary Statistic( "Sum" ),
    Elements( Bar( X, Y( 1 ), Y( 2 ), Legend( 2 ) ) )
);
```

### [Title Alignment](#title-alignment)[](#title-alignment "Click to copy url")

**Syntax:** obj \<\< Title Alignment( "Left"\|"Center"\|"Right" )

**Description:** Sets the alignment of the graph title.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Title Alignment( "Left" );
```

### [Title Fill Color](#title-fill-color)[](#title-fill-color "Click to copy url")

**Syntax:** obj \<\< Title Fill Color( color )

**Description:** Sets the color for the title background fill on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Title Fill Color( "Cyan" );
```

### [Title Frame Color](#title-frame-color)[](#title-frame-color "Click to copy url")

**Syntax:** obj \<\< Title Frame Color( color )

**Description:** Sets the color for the line around the title frame on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Title Frame Color( "Blue" );
```

### [Title Span](#title-span)[](#title-span "Click to copy url")

**Syntax:** obj \<\< Title Span( "Full"\|"Graph contents" )

**Description:** Sets the span of the graph title.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Title Span( "Graph" );
```

### [Title Text Color](#title-text-color)[](#title-text-color "Click to copy url")

**Syntax:** obj \<\< Title Text Color( color )

**Description:** Sets the color for the title text on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Title Text Color( "Red" );
```

### [Title Transparency](#title-transparency)[](#title-transparency "Click to copy url")

**Syntax:** obj \<\< Title Transparency( fraction=1 )

**Description:** Sets the transparency for the title frame on the graph. "1" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Title Transparency( .2 );
```

### [Title Underline](#title-underline)[](#title-underline "Click to copy url")

**Syntax:** obj \<\< Title Underline( state=0\|1 )

**Description:** Underlines the title or removes the underline on the graph.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Title Frame Color( "Blue" );
gb << Title Underline( 1 );
```

### [Update Element](#update-element)[](#update-element "Click to copy url")

**Syntax:** obj \<\< Update Element( xposition, yposition, i, {options} )

**Description:** Modifies the properties of an existing element.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 0.5 );
gb << Update Element( 1, 1, 1, {Summary Statistic( "Mean" ), Error Bars( "Range" )} );
```

### [Use row colors for levels](#use-row-colors-for-levels)[](#use-row-colors-for-levels "Click to copy url")

**Syntax:** obj \<\< Use row colors for levels( state=0\|1 )

**Description:** Initialize legend levels with row colors when every level has a unique color. On by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
gb << Use row colors for levels( 1 );
```

### [Variables](#variables)[](#variables "Click to copy url")

**Syntax:** Variables( X(column ), Y( column ), \<Group X( column )\>, \<Group Y( column )\>, \<Shape( column )\>, \<Color( column )\>, \<Overlay( column )\>, \<Freq( column )\> )

**Description:** Defines the variables used in the visualization.

``` jsl
dt = Open( "$SAMPLE_DATA/SATByYear.jmp" );
gb = dt << Graph Builder( Variables( Color( :SAT Verbal ), Shape( :State ) ) );
```

### [X Group Edge](#x-group-edge)[](#x-group-edge "Click to copy url")

**Syntax:** obj \<\< X Group Edge( "Top"\|"Bottom" )

**Description:** Moves the axis for the X group to either the top or the bottom. "Top" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
Wait( 1 );
gb << X Group Edge( "Bottom" );
```

### [Y Group Edge](#y-group-edge)[](#y-group-edge "Click to copy url")

**Syntax:** obj \<\< Y Group Edge( "Left"\|"Right" )

**Description:** Moves the axis for the Y group to either the left or the right. "Right" by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Sex ), Y( :Height ), Group Y( :Age ) ),
    Elements( Smoother( X, Y ) )
);
Wait( 1 );
gb << Y Group Edge( "Left" );
```

### [Y Group Level Orientation](#y-group-level-orientation)[](#y-group-level-orientation "Click to copy url")

**Syntax:** obj \<\< Y Group Level Orientation( "Horizontal"\|"Vertical" )

**Description:** Determines whether the Y Group level label text is horizontal or vertical (rotated).

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Sex ), Y( :Height ), Group Y( :Age ) ),
    Elements( Smoother( X, Y ) )
);
Wait( 1 );
gb << Y Group Level Orientation( "Horizontal" );
```

### [Y Group Title Orientation](#y-group-title-orientation)[](#y-group-title-orientation "Click to copy url")

**Syntax:** obj \<\< Y Group Title Orientation( "Horizontal"\|"Vertical" )

**Description:** Determines whether the Y Group title label text is horizontal or vertical (rotated).

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = dt << Graph Builder(
    Variables( X( :Sex ), Y( :Height ), Group Y( :Age ) ),
    Elements( Smoother( X, Y ) )
);
Wait( 1 );
gb << Y Group Title Orientation( "Horizontal" );
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Automatic Recalc( 1 );
dt << Select Rows( 5 ) << Exclude( 1 );
```

### [Broadcast](#broadcast)[](#broadcast "Click to copy url")

**Syntax:** obj \<\< Broadcast(message)

**Description:** Broadcasts a message to a platform. If return results from individual objects are tables, they are concatenated if possible, and the final format is identical to either the result from the Save Combined Table option in a Table Box or the result from the Concatenate option using a Source column. Other than those, results are stored in a list and returned.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Diameter.jmp" );
objs = Control Chart Builder(
    Variables( Subgroup( :DAY ), Y( :DIAMETER ) ),
    By( :OPERATOR )
);
objs[1] << Broadcast( Save Summaries );
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

### [Copy ByGroup Script](#copy-bygroup-script)[](#copy-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Copy ByGroup Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
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

### [Get ByGroup Script](#get-bygroup-script)[](#get-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Get ByGroup Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
t = obj[1] << Get ByGroup Script;
Show( t );
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
t = obj << Get Datatable;
Show( N Rows( t ) );
```

### [Get Group Platform](#get-group-platform)[](#get-group-platform "Click to copy url")

**Syntax:** obj \<\< Get Group Platform

**Description:** Return the Group Platform object if this platform is part of a Group. Otherwise, returns Empty().

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( Y( :weight ), X( :height ), By( :sex ) );
group = biv[1] << Get Group Platform;
Wait( 1 );
group << Layout( "Arrange in Tabs" );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
r = obj << Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Report View](#report-view)[](#report-view "Click to copy url")

**Syntax:** obj \<\< Report View( "Full"\|"Summary" )

**Description:** The report view determines the level of detail visible in a platform report. Full shows all of the detail, while Summary shows only select content, dependent on the platform. For customized behavior, display boxes support a \<\<Set Summary Behavior message.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
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
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
gb = Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ) ),
    Elements( Points( X, Y ), Smoother( X, Y ) )
);
r = obj << Top Report;
t = r[Outline Box( 1 )] << Get Title;
Show( t );
```

### [Transform Column](#transform-column)[](#transform-column "Click to copy url")

**Syntax:** obj = \<Platform\>(... Transform Column(\<name\>, Formula(\<expression\>), \[Random Seed(\<n\>)\], \[Numeric\|Character\|Expression\], \[Continuous\|Nominal\|Ordinal\|Unstructured Text\], \[column properties\]) ...)

**Description:** Create a transform column in the local context of an object, usually a platform. The transform column is active only for the lifetime of the platform.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Distribution(
    Transform Column( "age^2", Format( "Fixed Dec", 5, 0 ), Formula( :age * :age ) ),
    Continuous Distribution( Column( :"age^2"n ) )
);
```

### [View Web XML](#view-web-xml)[](#view-web-xml "Click to copy url")

**Syntax:** obj \<\< View Web XML

**Description:** Returns the XML code that is used to create the interactive HTML report.

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Bivariate( Y( :Weight ), X( :Height ) );
xml = obj << View Web XML;
```

### [Window View](#window-view)[](#window-view "Click to copy url")

**Syntax:** obj = Graph Builder(...Window View( "Visible"\|"Invisible"\|"Private" )...)

**Description:** Set the type of the window to be created for the report. By default a Visible report window will be created. An Invisible window will not appear on screen, but is discoverable by functions such as Window(). A Private window responds to most window messages but is not discoverable and must be addressed through the report object

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
biv = dt << Bivariate( Window View( "Private" ), Y( :weight ), X( :height ), Fit Line );
eqn = Report( biv )["Linear Fit", Text Edit Box( 1 )] << Get Text;
biv << Close Window;
New Window( "Bivariate Equation",
    Outline Box( "Big Class Linear Fit", Text Box( eqn, <<Set Base Font( "Title" ) ) )
);
```

## [Bar Element](#bar-element)[](#bar-element "Click to copy url")

### [Associated Constructors](#associated-constructors_2)[](#associated-constructors_2 "Click to copy url")

#### [Bar Element](#bar-element_1)[](#bar-element_1 "Click to copy url")

**Syntax:** Bar Element

**Description:** Shows a response summarized by categories.

**100% stacked bar chart**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// 100% stacked bar chart, custom legend colors
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Age ), Y( :Cholesterol ), Overlay( :Alcohol Use ) ),
    Elements(
        Bar( X, Y, Legend( 55 ), Bar Style( "Stacked" ), Summary Statistic( "% of Factor" ) )
    ),
    SendToReport(
        Dispatch( {}, "Cholesterol", ScaleBox, {Max( 1 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                55,
                Properties( 0, {Fill Color( RGB Color( 0.9, 0.9, 0.9 ) )} ),
                Properties( 1, {Fill Color( RGB Color( 1.0, 0.8, 0.8 ) )} ),
                Properties( 2, {Fill Color( RGB Color( 1.0, 0.6, 0.6 ) )} ),
                Properties( 3, {Fill Color( RGB Color( 1.0, 0.3, 0.3 ) )} )
            )}
        )
    )
);
```

**Bar and arrow chart**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// arrow and bar chart 
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Sex ), Y( :HDL ), Y( :LDL, Position( 1 ) ) ),
    Elements( Bar( X, Y( 1 ), Y( 2 ), Bar Style( "Arrow" ) ), Bar( X, Y( 1 ) ) )
);
```

**Bar chart ordered by count**

``` jsl
Open( "$SAMPLE_DATA/Airline Delays.jmp" );
// bar chart, ordered by count
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Airline, Order By( :Airline, "Descending", Order Statistic( "N" ) ) ) ),
    Elements( Bar( X, Legend( 4 ) ) )
);
```

**Bar chart with confidence intervals**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// bar chart with confidence intervals
Graph Builder(
    Size( 658, 555 ),
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :height ) ),
    Elements( Bar( X, Y, Legend( 6 ), Error Interval( "Confidence Interval" ) ) )
);
```

**Bar chart with labeled bars**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// bar chart, label by value
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Sex ), Y( :Cholesterol ) ),
    Elements( Bar( X, Y, Label( "Label by Value" ), Label Format( "Fixed Dec", 9, 1 ) ) )
);
```

**Bars with overlaid lines**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// bar with floating lines, custom colors
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Sex ),
        Y( :Cholesterol ),
        Y( :HDL, Position( 1 ) ),
        Y( :LDL, Position( 1 ) )
    ),
    Elements( Bar( X, Y( 1 ), Y( 2 ), Y( 3 ), Legend( 5 ), Bar Style( "Single" ) ) ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Properties( 0, {Fill Color( "light gray" )} ),
                Properties( 1, {Line Color( "green" )} ),
                Properties( 2, {Line Color( "orange" )} )
            )}
        )
    )
);
```

**Bars with small values stacked as Other**

``` jsl
Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
// stacked other bar, packed bars, pareto
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Count ), Y( :Causes ) ),
    Elements(
        Bar(
            X,
            Y,
            Bar Style( "Packed" ),
            Packed Placement( "Separate stack" ),
            Packed Primary Labels( "On axis" )
        )
    )
);
```

**Bullet chart**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// bar chart, bullet, 2 y variables
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Sex ), Y( :HDL ), Y( :LDL, Position( 1 ) ) ),
    Elements( Bar( X, Y( 1 ), Y( 2 ), Legend( 1 ), Bar Style( "Bullet" ) ) ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 1, Properties( 1, {Fill Color( "light gray" )} ) )}
        )
    )
);
```

**Data-driven bar coloring**

``` jsl
Open( "$SAMPLE_DATA/Dogs.jmp" );
// data-driven bar coloring, diverging bars
Graph Builder(
    Transform Column(
        "hilo",
        Nominal,
        Formula(
            If(
                :diff == Col Minimum( :diff ), "min",
                :diff == Col Maximum( :diff ), "max",
                "other"
            )
        )
    ),
    Show Control Panel( 0 ),
    Variables( X( :ID ), Y( :diff ), Color( :hilo ) ),
    Elements( Bar( X, Y, Legend( 3 ) ) ),
    SendToReport(
        Dispatch( {}, "diff", ScaleBox, {Add Ref Line( 0, "Solid", "Black", "", 1, 0.75 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                3,
                Properties( 0, {Fill Color( RGB Color( 0.5, 0.5, 0.9 ) )} ),
                Properties( 1, {Fill Color( RGB Color( 0.95, 0.6, 0.6 ) )} ),
                Properties( 2, {Fill Color( RGB Color( 0.7, 0.7, 0.7 ) )} )
            )}
        ),
        Dispatch( {}, "400", LegendBox,
            {Set Title( "" ), Legend Position( {3, [0, 1, -1]} )}
        )
    )
);
```

**Diverging stacked bars with Likert scale**

``` jsl
Open( "$SAMPLE_DATA/Likert Survey.jmp" );
// diverging stacked bars, likert scale
Graph Builder(
    Transform Column( "neg sd", Formula( -:strongly disagree ) ),
    Transform Column( "neg d", Formula( -:disagree ) ),
    Transform Column( "neg n", Formula( -:neutral / 2 ) ),
    Transform Column( "pos n", Formula( :neutral / 2 ) ),
    Show Control Panel( 0 ),
    Legend Position( "Bottom" ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables(
        X( :neg n ),
        X( :neg d, Position( 1 ) ),
        X( :neg sd, Position( 1 ) ),
        X( :pos n, Position( 1 ) ),
        X( :agree, Position( 1 ) ),
        X( :strongly agree, Position( 1 ) ),
        Y( :question )
    ),
    Elements(
        Bar(
            X( 1 ),
            X( 2 ),
            X( 3 ),
            X( 4 ),
            X( 5 ),
            X( 6 ),
            Y,
            Legend( 4 ),
            Bar Style( "Stacked" )
        )
    ),
    SendToReport(
        Dispatch( {}, "neg n", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "question", ScaleBox, {Min( 19.6 ), Max( -0.6 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                4,
                Level Name( 0, "neutral" ),
                Level Name( 1, "disagree" ),
                Level Name( 2, "strongly disagree" ),
                Level Name( 3, "neutral" ),
                Properties( 0, {Fill Color( RGB Color( {0.9, 0.9, 0.9} ) )} ),
                Properties( 1, {Fill Color( RGB Color( {1.0, 0.7, 0.7} ) )} ),
                Properties( 2, {Fill Color( RGB Color( {1.0, 0.3, 0.3} ) )} ),
                Properties( 3, {Fill Color( RGB Color( {0.9, 0.9, 0.9} ) )} ),
                Properties( 4, {Fill Color( RGB Color( {0.8, 0.8, 1.0} ) )} ),
                Properties( 5, {Fill Color( RGB Color( {0.5, 0.5, 1.0} ) )} )
            )}
        )
    ),
    Dispatch( {}, "400", LegendBox, {Legend Position( {4, [2, 1, 0, -1, 3, 4]} )} )
);
```

**Float lines with overlaid points**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// float lines and overlaid points
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Sex ), Y( :LDL ), Y( :HDL, Position( 1 ) ) ),
    Elements(
        Bar( X, Y( 1 ), Y( 2 ), Legend( 1 ), Bar Style( "Float" ) ),
        Points( X, Y( 1 ), Y( 2 ), Legend( 3 ) )
    )
);
```

**Interval with dot using transforms**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// interval bar chart, transform columns
Graph Builder(
    Transform Column( "Maximum[HDL][Sex]", Formula( Col Maximum( :HDL, :Sex ) ) ),
    Transform Column( "Minimum[HDL][Sex]", Formula( Col Minimum( :HDL, :Sex ) ) ),
    Transform Column( "Mean[HDL][Sex]", Formula( Col Mean( :HDL, :Sex ) ) ),
    Show Control Panel( 0 ),
    Variables(
        X( :Sex ),
        Y( :"Minimum[HDL][Sex]"n ),
        Y( :"Maximum[HDL][Sex]"n, Position( 1 ) ),
        Y( :"Mean[HDL][Sex]"n, Position( 1 ) ),

    ),
    Elements( Bar( X, Y( 1 ), Y( 2 ), Y( 3 ), Bar Style( "Interval" ) ) )
);
```

**Needle chart**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// needle bar chart
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Age ), Y( :Cholesterol ) ),
    Elements( Bar( X, Y, Bar Style( "Needle" ), Summary Statistic( "Max" ) ) )
);
```

**Packed bars highlighting top ten categories**

``` jsl
Open( "$SAMPLE_DATA/Billion Dollar Events.jmp" );
// packed bar chart, top 10, custom axis format, subtitle
Graph Builder(
    Size( 813, 512 ),
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Title Alignment( "Left" ),
    Title Span( "Graph contents" ),
    Subtitle Alignment( "Left" ),
    Subtitle Span( "Graph contents" ),
    Show Subtitle( 1 ),
    Show Footer( 0 ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables( X( :Cost ), Y( :Unique Event ) ),
    Elements(
        Bar( X, Y, Bar Style( "Packed" ), Packed Primaries( 10 ), Packed Labeling( 0.4091 ) )
    ),
    SendToReport(
        Dispatch( {}, "Cost", ScaleBox,
            {Format(
                "Custom",
                Formula(
                    If( value == 0,
                        "0",
                        "$" || Format( value, "precision", Keep trailing zeroes( 0 ), 3 ) ||
                        "B"
                    )
                ),
                17
            ), Min( 0 ), Max( 164.25 ), Inc( 20 ), Minor Ticks( 0 )}
        ),
        Dispatch( {}, "graph title", TextEditBox,
            {Margin( {Left( 5 ), Top( 0 ), Right( 0 ), Bottom( 0 )} ),
            Set Text( "Billion-dollar disasters in the US, 1980-2017" ),
            Set Font Style( "Plain" )}
        ),
        Dispatch( {}, "graph 1 title", TextEditBox,
            {Margin( {Left( 5 ), Top( 0 ), Right( 0 ), Bottom( 0 )} ),
            Set Text( "CPI-adjusted estimated costs from NOAA, www.ncdc.noaa.gov/billions/" )
            }
        )
    )
);
```

**Range bar chart**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// range bar chart between two variables
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Sex ), Y( :HDL ), Y( :LDL, Position( 1 ) ) ),
    Elements( Bar( X, Y( 1 ), Y( 2 ), Bar Style( "Range" ) ) ),

);
```

**Side-by-side grouped bar chart using median**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// bar chart, side-by-side, 3 y variables, median, custom colors
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Sex ),
        Y( :Cholesterol ),
        Y( :HDL, Position( 1 ) ),
        Y( :LDL, Position( 1 ) )
    ),
    Elements( Bar( X, Y( 1 ), Y( 2 ), Y( 3 ), Summary Statistic( "Median" ), Legend( 5 ) ) ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Properties( 0, {Fill Color( "dark gray" )} ),
                Properties( 1, {Fill Color( "blue" )} ),
                Properties( 2, {Fill Color( "orange" )} )
            )}
        )
    )
);
```

**Sorted stacked bar chart**

``` jsl
Open( "$SAMPLE_DATA/Quality Control/Cabinet Defects.jmp" );
// bar chart, sorted stacked, filtered, custom legend colors
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Lot Number ), Overlay( :Type of Defect ) ),
    Elements( Bar( X, Legend( 3 ), Bar Style( "Sorted stacked" ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :Lot Number, :Type of Defect ),
            Where( :Lot Number <= 10.5 ),
            Where(
                :Type of Defect == {"Bruised veneer", "Checked veneer", "Chipped veneer",
                "Defective sanding", "Loose veneer", "Sand throughs", "Scratched veneer",
                "Split veneer"}
            ),
            Display( :Type of Defect, N Items( 9 ) )
        )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                3,
                Properties( 0, {Fill Color( RGB Color( 0.55, 0.83, 0.78 ) )} ),
                Properties( 1, {Fill Color( RGB Color( 0.75, 0.73, 0.85 ) )} ),
                Properties( 2, {Fill Color( RGB Color( 0.98, 0.50, 0.45 ) )} ),
                Properties( 3, {Fill Color( RGB Color( 0.50, 0.69, 0.83 ) )} ),
                Properties( 4, {Fill Color( RGB Color( 0.99, 0.71, 0.38 ) )} ),
                Properties( 5, {Fill Color( RGB Color( 0.70, 0.87, 0.41 ) )} ),
                Properties( 6, {Fill Color( RGB Color( 0.99, 0.80, 0.90 ) )} ),
                Properties( 7, {Fill Color( RGB Color( 0.74, 0.50, 0.74 ) )} )
            )}
        )
    )
);
```

**Stacked bar chart of 3 variables and custom colors**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// bar chart, stacked, 3 y variables, mean
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Sex ),
        Y( :Cholesterol ),
        Y( :HDL, Position( 1 ) ),
        Y( :LDL, Position( 1 ) )
    ),
    Elements(
        Bar(
            X,
            Y( 1 ),
            Y( 2 ),
            Y( 3 ),
            Bar Style( "Stacked" ),
            Summary Statistic( "Mean" ),
            Legend( 5 )
        )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Properties( 0, {Fill Color( "dark gray" )} ),
                Properties( 1, {Fill Color( "blue" )} ),
                Properties( 2, {Fill Color( "orange" )} )
            )}
        )
    )
);
```

**Variable width bars, ordered by value**

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
// variable width bars, ordered by value
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X(
            :State,
            Order By( :"2004 Verbal"n, "Descending", Order Statistic( "Mean" ) ),
            Size By( :"% Taking (2004)"n, Size Statistic( "Mean" ) )
        ),
        Y( :"2004 Verbal"n )
    ),
    Elements( Bar( X, Y, Legend( 4 ) ) )
);
```

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Bar Style](#bar-style)[](#bar-style "Click to copy url")

**Syntax:** obj \<\< Bar Style( "Side by side"\|"Stacked"\|"Sorted stacked"\|"Bullet"\|"Nested"\|"Range"\|"Side by side ranges"\|"Interval"\|"Side by side intervals"\|"Two-way interval"\|"Arrow"\|"Single"\|"Stock"\|"Box Plot"\|"Needle"\|"Float"\|"Treemap"\|"Packed" )

#### [Error Interval](#error-interval_1)[](#error-interval_1 "Click to copy url")

**Syntax:** obj \<\< Error Interval( "Auto"\|"None"\|"Range"\|"Interquartile Range"\|"Standard Error"\|"Standard Deviation"\|"Confidence Interval"\|"Median Absolute Deviation"\|"Custom Interval"\|"Two-way Interval" )

#### [Interval Style](#interval-style_1)[](#interval-style_1 "Click to copy url")

**Syntax:** obj \<\< Interval Style( "Error Bar"\|"Band"\|"Hash Band"\|"Arrow" )

#### [Label](#label)[](#label "Click to copy url")

**Syntax:** obj \<\< Label( "No Labels"\|"Label by Value"\|"Label by Percent of Total Values"\|"Label by Row" )

#### [Label Format](#label-format)[](#label-format "Click to copy url")

**Syntax:** obj \<\< Label Format

**JMP Version Added:** 16

#### [Overlap](#overlap)[](#overlap "Click to copy url")

**Syntax:** obj \<\< Overlap( "Auto"\|"None"\|"Half"\|"Full" )

**JMP Version Added:** 16

#### [Packed Coloring](#packed-coloring)[](#packed-coloring "Click to copy url")

**Syntax:** obj \<\< Packed Coloring( "Bar color"\|"Faded bar color"\|"Grays" )

**JMP Version Added:** 14

#### [Packed Labeling](#packed-labeling)[](#packed-labeling "Click to copy url")

**Syntax:** obj \<\< Packed Labeling( number )

**JMP Version Added:** 14

#### [Packed Ordering](#packed-ordering)[](#packed-ordering "Click to copy url")

**Syntax:** obj \<\< Packed Ordering( "By size"\|"By label" )

**JMP Version Added:** 14

#### [Packed Placement](#packed-placement)[](#packed-placement "Click to copy url")

**Syntax:** obj \<\< Packed Placement( "Separate stack"\|"Smallest stack"\|"First stack" )

**JMP Version Added:** 14

#### [Packed Primaries](#packed-primaries)[](#packed-primaries "Click to copy url")

**Syntax:** obj \<\< Packed Primaries( number )

**JMP Version Added:** 14

#### [Packed Primary Labels](#packed-primary-labels)[](#packed-primary-labels "Click to copy url")

**Syntax:** obj \<\< Packed Primary Labels( "On axis"\|"Inside bars" )

**JMP Version Added:** 14

#### [Response Axis](#response-axis_1)[](#response-axis_1 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Save Summary Formula](#save-summary-formula_1)[](#save-summary-formula_1 "Click to copy url")

**Syntax:** obj \<\< Save Summary Formula

#### [Summary Statistic](#summary-statistic_2)[](#summary-statistic_2 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

## [Box Plot Element](#box-plot-element)[](#box-plot-element "Click to copy url")

### [Associated Constructors](#associated-constructors_3)[](#associated-constructors_3 "Click to copy url")

#### [Box Plot Element](#box-plot-element_1)[](#box-plot-element_1 "Click to copy url")

**Syntax:** Box Plot Element

**Description:** Shows a compact view of a variable’s distribution with quartiles and outliers.

**Horizontal outlier box plots**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// horizontal outlier box plots
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :sex ) ),
    Elements( Box Plot( X, Y, Legend( 4 ) ) ),
    SendToReport( Dispatch( {}, "height", ScaleBox, {Min( 50 )} ) )
);
```

**Overlaid box plots**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// box plots, overlaid
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ), Overlay( :Sex ) ),
    Elements( Box Plot( X, Y, Legend( 2 ) ) )
);
```

**Solid box plots with data-driven color**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// solid box plots, colored by summary of a different variable
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ), Color( :Flipper Length ) ),
    Elements( Box Plot( X, Y, Legend( 2 ), Box Style( "Solid" ), Fences( 0 ) ) )
);
```

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [5 Number Summary](#5-number-summary)[](#5-number-summary "Click to copy url")

**Syntax:** obj \<\< 5 Number Summary( state=0\|1 )

**JMP Version Added:** 14

#### [Box Placement](#box-placement)[](#box-placement "Click to copy url")

**Syntax:** obj \<\< Box Placement( "Offset"\|"Align" )

**JMP Version Added:** 16

#### [Box Style](#box-style)[](#box-style "Click to copy url")

**Syntax:** obj \<\< Box Style( "Normal"\|"Solid"\|"Thin" )

#### [Box Type](#box-type)[](#box-type "Click to copy url")

**Syntax:** obj \<\< Box Type( "Quantile"\|"Outlier" )

#### [Confidence Diamond](#confidence-diamond)[](#confidence-diamond "Click to copy url")

**Syntax:** obj \<\< Confidence Diamond( state=0\|1 )

**JMP Version Added:** 16

#### [Fences](#fences)[](#fences "Click to copy url")

**Syntax:** obj \<\< Fences( state=0\|1 )

**JMP Version Added:** 16

#### [Jitter](#jitter)[](#jitter "Click to copy url")

**Syntax:** obj \<\< Jitter( "None"\|"Auto"\|"Random Uniform"\|"Random Normal"\|"Density Random"\|"Packed"\|"Grid"\|"Hex Grid"\|"Beeswarm" )

#### [Notched](#notched)[](#notched "Click to copy url")

**Syntax:** obj \<\< Notched( state=0\|1 )

**JMP Version Added:** 16

#### [Outliers](#outliers)[](#outliers "Click to copy url")

**Syntax:** obj \<\< Outliers( state=0\|1 )

#### [Response Axis](#response-axis_2)[](#response-axis_2 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Shortest Half](#shortest-half)[](#shortest-half "Click to copy url")

**Syntax:** obj \<\< Shortest Half( state=0\|1 )

**JMP Version Added:** 16

#### [Shortest Half Color](#shortest-half-color)[](#shortest-half-color "Click to copy url")

**Syntax:** obj \<\< Shortest Half Color( color )

**JMP Version Added:** 16

#### [Width Proportion](#width-proportion)[](#width-proportion "Click to copy url")

**Syntax:** obj \<\< Width Proportion( number=0 )

**Description:** "0" by default.

**JMP Version Added:** 15

## [Caption Element](#caption-element)[](#caption-element "Click to copy url")

### [Associated Constructors](#associated-constructors_4)[](#associated-constructors_4 "Click to copy url")

#### [Caption Element](#caption-element_1)[](#caption-element_1 "Click to copy url")

**Syntax:** Caption Element

**Description:** Shows a summary statistic value for the data.

**Axis table summary statistics**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// caption axis table
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :sex ), Y( :height ) ),
    Elements(
        Bar( X, Y, Legend( 4 ) ),
        Caption Box(
            X,
            Y,
            Legend( 5 ),
            Summary Statistic( "Mean" ),
            Summary Statistic 2( "N" ),
            Location( "Axis Table" )
        )
    )
);
```

**Data-driven reference line**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// caption reference line, run chart
Graph Builder(
    Show Control Panel( 0 ),
    Variables( Y( :weight ) ),
    Elements(
        Caption Box(
            Y,
            Legend( 5 ),
            Summary Statistic( "Mean" ),
            Location( "Axis Reference Line" ),
            X Position( "Left" )
        ),
        Line( Y, Legend( 6 ), Ordering( "Row Order" ) )
    )
);
```

**Graph-level caption summary statistic**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// caption annotation per graph
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ), Group X( :sex ) ),
    Elements(
        Points( X, Y, Legend( 2 ) ),
        Line Of Fit( X, Y, Legend( 4 ) ),
        Caption Box( X, Y, Legend( 5 ), Summary Statistic( "N" ), X Position( "Left" ) )
    )
);
```

**Two caption statistics, per factor**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// caption per factor, mean and count, custom number format
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :sex ), Y( :height ) ),
    Elements(
        Bar( X, Y, Legend( 4 ) ),
        Caption Box(
            X,
            Y,
            Legend( 5 ),
            Summary Statistic( "Mean" ),
            Summary Statistic 2( "N" ),
            Location( "Graph per factor" ),
            Number Format( "Best", 5 )
        )
    )
);
```

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Location](#location)[](#location "Click to copy url")

**Syntax:** obj \<\< Location( "Graph"\|"Graph per factor"\|"Axis Table"\|"Axis Reference Line" )

#### [Number Format](#number-format)[](#number-format "Click to copy url")

**Syntax:** obj \<\< Number Format

**JMP Version Added:** 16

#### [Per Factor](#per-factor)[](#per-factor "Click to copy url")

**Syntax:** obj \<\< Per Factor( state=0\|1 )

**JMP Version Added:** 14

#### [Response Axis](#response-axis_3)[](#response-axis_3 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Summary Statistic](#summary-statistic_3)[](#summary-statistic_3 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "None"\|"N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile"\|"5 Number Summary" )

#### [Summary Statistic 2](#summary-statistic-2)[](#summary-statistic-2 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic 2( "None"\|"N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile"\|"5 Number Summary" )

#### [Summary Statistic 3](#summary-statistic-3)[](#summary-statistic-3 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic 3( "None"\|"N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile"\|"5 Number Summary" )

#### [Summary Statistic 4](#summary-statistic-4)[](#summary-statistic-4 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic 4( "None"\|"N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile"\|"5 Number Summary" )

#### [Summary Statistic 5](#summary-statistic-5)[](#summary-statistic-5 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic 5( "None"\|"N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile"\|"5 Number Summary" )

#### [X Position](#x-position)[](#x-position "Click to copy url")

**Syntax:** obj \<\< X Position( "Left"\|"Middle"\|"Right" )

#### [Y Position](#y-position)[](#y-position "Click to copy url")

**Syntax:** obj \<\< Y Position( "Top"\|"Middle"\|"Bottom" )

## [Contour Element](#contour-element)[](#contour-element "Click to copy url")

### [Associated Constructors](#associated-constructors_5)[](#associated-constructors_5 "Click to copy url")

#### [Contour Element](#contour-element_1)[](#contour-element_1 "Click to copy url")

**Syntax:** Contour Element

**Description:** Shows regions of data density (or value contours with a Color variable). Produces violin plots when X is categorical.

**Bivariate kernel density contour**

``` jsl
Open( "$SAMPLE_DATA/Airline Delays.jmp" );
// bivariate kernel density contour
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Distance ), Y( :Arrival Delay ), Wrap( :Airline ) ),
    Elements( Contour( X, Y, Legend( 6 ), Number of Levels( 6 ) ) )
);
```

**Geographic contour**

``` jsl
Open( "$SAMPLE_DATA/Cities.jmp" );
// contour, geographic, background map, clipped to shapes, sequential colors, hidden axes
Graph Builder(
    Show Control Panel( 0 ),
    Show X Axis( 0 ),
    Show Y Axis( 0 ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables( X( :Longitude ), Y( :Latitude ), Color( :PM10 ) ),
    Elements(
        Contour(
            X,
            Y,
            Legend( 5 ),
            Boundary( 0 ),
            Number of Levels( 5 ),
            Alpha( 0.04 ),
            Smoothness( 0.02 )
        )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Properties( 0, {gradient( {Color Theme( "White to Red" )} )} )
            )}
        ),
        Dispatch( {}, "Graph Builder", FrameBox,
            {Background Map( Boundaries( "US States" ) ), Grid Line Order( 1 ),
            Reference Line Order( 4 ), Reorder Segs( {1, 3} ),
            DispatchSeg( Contour Seg( 1 ), {Clip Shape( Boundaries( "US States" ) )} )}
        )
    )
);
```

**HDR, highest denisty regions**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// HDR, highest denisty regions with mode line
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ) ),
    Elements( Contour( X, Y, Legend( 4 ), Smoothness( 0.113 ), Contour Type 1D( "HDR" ) ) )
);
```

**Paneled contour heatmap**

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Peanut Data.jmp" );
// paneled contour heatmap, trellis
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Ratio ),
        Y( :Agitation Speed ),
        Group X( :Hydrolyze ),
        Group Y( :"Pre-Soak"n ),
        Color( :Solids )
    ),
    Elements( Contour( X, Y, Legend( 28 ), Smoothness( 0.01 ) ) )
);
```

**Smooth contours**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// contour plot, smooth contours, alpha shapes for non-convex hull
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Culmen Length ), Y( :Flipper Length ), Color( :Body Mass ) ),
    Elements(
        Contour(
            X,
            Y,
            Legend( 7 ),
            Number of Levels( 5 ),
            Alpha( 0.1 ),
            Smoothness( 0.065 )
        )
    )
);
```

**Violin plots overlaid with thin box plots**

``` jsl
Open( "$SAMPLE_DATA/S4 Temps.jmp" );
// violin plots overlaid with thin box plots
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :type of space ), Y( :Y ) ),
    Elements(
        Contour( X, Y, Legend( 5 ), Violin Scaling( "Weighted Area" ) ),
        Box Plot( X, Y, Legend( 6 ), Outliers( 0 ), Box Style( "Thin" ), Fences( 0 ) )
    )
);
```

**Violin plots with median line and mean diamond**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// violin plots, overlaid median line and mean diamond marker
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ) ),
    Elements(
        Contour( X, Y, Legend( 3 ) ),
        Bar( X, Y, Legend( 4 ), Bar Style( "Float" ), Summary Statistic( "Median" ) ),
        Points( X, Y, Legend( 5 ), Summary Statistic( "Mean" ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 5, Properties( 0, {Marker( "Diamond" )} ) )}
        )
    )
);
```

**Violin plots with quartiles**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// violin plots, overlaid median line and quartile intervals
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ) ),
    Elements(
        Contour( X, Y, Legend( 3 ) ),
        Bar(
            X,
            Y,
            Legend( 4 ),
            Bar Style( "Float" ),
            Summary Statistic( "Median" ),
            Error Interval( "Interquartile Range" )
        )
    )
);
```

### [Item Messages](#item-messages_5)[](#item-messages_5 "Click to copy url")

#### [Adapt to Axis Scale](#adapt-to-axis-scale)[](#adapt-to-axis-scale "Click to copy url")

**Syntax:** obj \<\< Adapt to Axis Scale( state=0\|1 )

**Description:** For log and other axis transformations, apply computations on the transformed coordinates.

#### [Alpha](#alpha)[](#alpha "Click to copy url")

**Syntax:** obj \<\< Alpha( number )

**Description:** Controls the shape of the boundary. A value of 0 results in the convex hull of the point set. Larger values eliminate triangles with long edges.

**JMP Version Added:** 15

#### [Boundary](#boundary)[](#boundary "Click to copy url")

**Syntax:** obj \<\< Boundary( state=0\|1 )

**Description:** Draw a line at the boundary of the defined data region. This boundary might be non-convex depending on the Alpha property.

**JMP Version Added:** 15

#### [Contour Placement](#contour-placement)[](#contour-placement "Click to copy url")

**Syntax:** obj \<\< Contour Placement( "Offset"\|"Align" )

**JMP Version Added:** 16

#### [Contour Type](#contour-type)[](#contour-type "Click to copy url")

**Syntax:** obj \<\< Contour Type( "Violin"\|"HDR" )

**JMP Version Added:** 15

#### [Contour Type 1D](#contour-type-1d)[](#contour-type-1d "Click to copy url")

**Syntax:** obj \<\< Contour Type 1D( "Violin"\|"HDR" )

**JMP Version Added:** 15

#### [Contour Type 2D](#contour-type-2d)[](#contour-type-2d "Click to copy url")

**Syntax:** obj \<\< Contour Type 2D( "Nonpar Density"\|"Bagplot"\|"HDR" )

**JMP Version Added:** 15

#### [Fill](#fill)[](#fill "Click to copy url")

**Syntax:** obj \<\< Fill( state=0\|1 )

**Description:** Fill the regions between the contours using colors from the gradient.

**JMP Version Added:** 15

#### [Jitter](#jitter_1)[](#jitter_1 "Click to copy url")

**Syntax:** obj \<\< Jitter( "None"\|"Auto"\|"Random Uniform"\|"Random Normal"\|"Density Random"\|"Packed"\|"Grid"\|"Hex Grid"\|"Beeswarm" )

#### [Line](#line)[](#line "Click to copy url")

**Syntax:** obj \<\< Line( state=0\|1 )

**Description:** Draw a line at each contour level, colored by the gradient or by a separate line color.

**JMP Version Added:** 15

#### [Number of Levels](#number-of-levels)[](#number-of-levels "Click to copy url")

**Syntax:** obj \<\< Number of Levels( number )

**Description:** Set the number of filled contour regions to draw.

#### [Outliers](#outliers_1)[](#outliers_1 "Click to copy url")

**Syntax:** obj \<\< Outliers( state=0\|1 )

#### [Smoothness](#smoothness_1)[](#smoothness_1 "Click to copy url")

**Syntax:** obj \<\< Smoothness( number )

**Description:** Smooths the underlying data and the contours.

**JMP Version Added:** 14

#### [Transform](#transform)[](#transform "Click to copy url")

**Syntax:** obj \<\< Transform( "None"\|"Range Normalized" )

**Description:** Optionally transform the points prior to computing triangulation, which is used for interpolation.

#### [Violin Scaling](#violin-scaling)[](#violin-scaling "Click to copy url")

**Syntax:** obj \<\< Violin Scaling( "Equal Area"\|"Equal Width"\|"Weighted Area" )

**JMP Version Added:** 14

## [Ellipse Element](#ellipse-element)[](#ellipse-element "Click to copy url")

### [Associated Constructors](#associated-constructors_6)[](#associated-constructors_6 "Click to copy url")

#### [Ellipse Element](#ellipse-element_1)[](#ellipse-element_1 "Click to copy url")

**Syntax:** Ellipse Element

**Description:** Shows a bivariate normal density ellipse.

**Density ellipse in panels**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// density ellipse, correlation coefficient, panels, mean diamond
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Culmen Depth ),
        Y( :Culmen Length ),
        Group X( :Species ),
        Group Y( :Sex )
    ),
    Elements(
        Points( X, Y, Legend( 8 ) ),
        Ellipse( X, Y, Legend( 10 ), Correlation( 1 ), Mean Point( 1 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 8, Properties( 0, {Marker( "Circle" ), Transparency( 0.5 )} ) ),
            Legend Model(
                10,
                Properties( 1, {Marker( "Filled Diamond" ), Marker Size( 6 )} )
            )}
        )
    )
);
```

**Density ellipse with central mean marker**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// density ellipse, correlation, central mean
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ), Group Y( :sex ) ),
    Elements(
        Points( X, Y, Legend( 2 ) ),
        Ellipse( X, Y, Legend( 5 ), Coverage( "95%" ), Mean Point( 1 ) )
    )
);
```

**Density ellipse with correlation coefficient**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// density ellipse, correlation coefficient
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Culmen Depth ), Y( :Culmen Length ), Overlay( :Species ) ),
    Elements(
        Points( X, Y, Legend( 8 ) ),
        Ellipse( X, Y, Legend( 10 ), Coverage( "50%" ), Correlation( 1 ), Mean Point( 1 ) )
    )
);
```

**Overlaid density ellipses**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// overlaid density ellipse, correlation coefficient
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ), Overlay( :sex ) ),
    Elements( Points( X, Y, Legend( 2 ) ), Ellipse( X, Y, Legend( 5 ), Correlation( 1 ) ) )
);
```

### [Item Messages](#item-messages_6)[](#item-messages_6 "Click to copy url")

#### [Adapt to Axis Scale](#adapt-to-axis-scale_1)[](#adapt-to-axis-scale_1 "Click to copy url")

**Syntax:** obj \<\< Adapt to Axis Scale( state=0\|1 )

**Description:** For log and other axis transformations, apply computations on the transformed coordinates.

#### [Correlation](#correlation)[](#correlation "Click to copy url")

**Syntax:** obj \<\< Correlation( state=0\|1 )

**Description:** Coefficient of correlation for the X and Y variables.

#### [Coverage](#coverage)[](#coverage "Click to copy url")

**Syntax:** obj \<\< Coverage( "99%"\|"95%"\|"90%"\|"50%" )

#### [Mean Point](#mean-point)[](#mean-point "Click to copy url")

**Syntax:** obj \<\< Mean Point( state=0\|1 )

**Description:** Shows the mean point of the ellipse.

## [Formula Element](#formula-element)[](#formula-element "Click to copy url")

### [Associated Constructors](#associated-constructors_7)[](#associated-constructors_7 "Click to copy url")

#### [Formula Element](#formula-element_1)[](#formula-element_1 "Click to copy url")

**Syntax:** Formula Element

**Description:** Shows a function defined by a column formula.

**Model comparison**

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/Corn.jmp" );
// function plot, non-linear functions piecewise linear, piecewise quadratic
Local( {obj},
    obj = Data Table( "Corn.jmp" ) << Nonlinear(
        Y( :yield ),
        X( :linear ),
        "Newton",
        Finish
    );
    obj << Save Prediction Formula;
    obj << Close Window;
);
Local( {obj},
    obj = Data Table( "Corn.jmp" ) << Nonlinear(
        Y( :yield ),
        X( :quad ),
        "QuasiNewton SR1",
        Finish
    );
    obj << Save Prediction Formula;
    obj << Close Window;
);
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :nitrate ),
        Y( :yield ),
        Y( :Fitted linear, Position( 1 ) ),
        Y( :Fitted quad, Position( 1 ) )
    ),
    Elements( Points( X, Y( 1 ), Legend( 8 ) ), Formula( X, Y( 2 ), Y( 3 ), Legend( 9 ) ) )
);
```

**Parametric equations**

``` jsl
New Table( "bowtie",
    New Column( "t", Set Values( [0, 10] ) ),
    New Column( "x", Formula( Cos( :t ) ) ),
    New Column( "y", Formula( Sine( :t * 2 ) ) )
);
// function plot, parametric equations
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :x ), Y( :y ) ),
    Elements( Formula( X, Y, Legend( 5 ) ) ),
    SendToReport(
        Dispatch( {}, "x", ScaleBox, {Min( -1.1 ), Max( 1.1 )} ),
        Dispatch( {}, "y", ScaleBox, {Min( -1.4 ), Max( 1.4 )} )
    )
);
```

### [Item Messages](#item-messages_7)[](#item-messages_7 "Click to copy url")

#### [Response Axis](#response-axis_4)[](#response-axis_4 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

## [Heatmap Element](#heatmap-element)[](#heatmap-element "Click to copy url")

### [Associated Constructors](#associated-constructors_8)[](#associated-constructors_8 "Click to copy url")

#### [Heatmap Element](#heatmap-element_1)[](#heatmap-element_1 "Click to copy url")

**Syntax:** Heatmap Element

**Description:** Shows counts using color for X and Y categories.

**Categorical heatmap with custom gradient**

``` jsl
Open( "$SAMPLE_DATA/Airline Delays.jmp" );
// heat map, custom gradient
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Day of Week ), Y( :Month ), Color( :Arrival Delay ) ),
    Elements( Heatmap( X, Y, Legend( 17 ) ) ),
    Local Data Filter(
        Add Filter( columns( :Distance ), Where( :Distance >= 500 & :Distance <= 1500 ) )
    ),
    SendToReport(
        Dispatch( {}, "Month", ScaleBox, {Reversed Scale} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                17,
                Properties(
                    0,
                    {gradient(
                        {Color Theme(
                            {"Blue to Gray to Red Copy", {"Continuous", "Categorical",
                            "Diverging"}, {{42, 63, 255}, {166, 170, 203}, {192, 192, 192},
                            {201, 165, 165}, {252, 11, 11}, Missing( "Black" )}, {0, 0.33,
                            0.5, 0.67, 1}, {"Full Color", "Tritanopia"}}
                        ), Scale Values( [. 0 .] )}
                    )}
                )
            )}
        )
    )
);
```

**Data-driven background color**

``` jsl
Open( "$SAMPLE_DATA/Corn Wheat Soybean Production.jmp" );
// heat map as background color
Graph Builder(
    Transform Column(
        "Mean[Total Acres Planted][State]",
        Formula( Col Mean( :Total Acres Planted, :State ) )
    ),
    Transform Column(
        "delta",
        Formula(
            (Col At( :Total Acres Planted, -1, :State )
            -Col At( :Total Acres Planted, 1, :State )) /
            Col Mean( :Total Acres Planted, :State )
        )
    ),
    Show Control Panel( 0 ),
    Variables(
        X( :Year ),
        Y( :Total Acres Planted ),
        Wrap(
            :State,
            Order By( :Total Acres Planted, "Descending", Order Statistic( "Mean" ) )
        ),
        Color( :delta )
    ),
    Elements(
        Heatmap( Legend( 16 ) ),
        Points( X, Y, Color( 0 ), Legend( 14 ) ),
        Smoother( X, Y, Color( 0 ), Legend( 15 ) )
    ),
    Local Data Filter(
        Add Filter(
            columns( :"Mean[Total Acres Planted][State]"n ),
            Where( :"Mean[Total Acres Planted][State]"n >= 3245000 )
        )
    ),
    SendToReport(
        Dispatch( {}, "Total Acres Planted", ScaleBox,
            {Format( "Engineering SI", 13 ), Minor Ticks( 0 )}
        ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                16,
                Properties(
                    0,
                    {gradient(
                        {Scale Values( [-0.3 0 0.3] ), Label Format( "Percent", 12, 0 )}
                    )}
                )
            )}
        ),
        Dispatch( {}, "400", LegendBox, {Legend Position( {16, [2], 14, [0], 15, [1]} )} )
    )
);
```

**Heatmap with categorical color**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// heat map, categorical color
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Culmen Depth ), Y( :Culmen Length ), Color( :Species ) ),
    Elements( Heatmap( X, Y, Legend( 4 ) ) )
);
```

**Hexagonal heatmap of counts**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// hexagonal heatmap, color by count, sequential color gradient
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Culmen Depth ), Y( :Culmen Length ) ),
    Elements(
        Heatmap( X, Y, Legend( 4 ), Bin Shape( "Hexagonal" ), Hex Bin Radius( 24.61 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                4,
                Properties( 0, {gradient( {Color Theme( "White to Purple" )} )} )
            )}
        )
    )
);
```

**Labeled heatmap**

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Peanut Data.jmp" );
// labeled heatmap, treating continuous variables as categorical with transform
Graph Builder(
    Transform Column( "Ordinal Agitation Speed", Ordinal, Formula( :Agitation Speed ) ),
    Transform Column( "Ordinal Ratio", Ordinal, Formula( :Ratio ) ),
    Show Control Panel( 0 ),
    Variables( X( :Ordinal Agitation Speed ), Y( :Ordinal Ratio ), Color( :Solids ) ),
    Elements( Heatmap( X, Y, Legend( 29 ), Label( "Label by Value" ) ) )
);
```

**Wafer map**

``` jsl
Open( "$SAMPLE_DATA/Wafer Stacked.jmp" );
// wafer map, heat map, trellis, wrap arrangement
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :X_Die ), Y( :Y_Die ), Wrap( :Wafer ), Color( :Defects ) ),
    Elements( Heatmap( X, Y, Legend( 8 ) ) ),
    SendToReport(
        Dispatch( {}, "X_Die", ScaleBox, {Minor Ticks( 9 )} ),
        Dispatch( {}, "Y_Die", ScaleBox, {Minor Ticks( 9 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                8,
                Properties( 0, {gradient( {Color Theme( "White to Orange" )} )} )
            )}
        )
    )
);
```

### [Item Messages](#item-messages_8)[](#item-messages_8 "Click to copy url")

#### [Bin Shape](#bin-shape)[](#bin-shape "Click to copy url")

**Syntax:** obj \<\< Bin Shape( "Rectangular"\|"Hexagonal" )

**JMP Version Added:** 16

#### [Cell Outline](#cell-outline)[](#cell-outline "Click to copy url")

**Syntax:** obj \<\< Cell Outline( state=0\|1 )

**Description:** Defines the maximum increase in font size.

**JMP Version Added:** 16

#### [Hex Bin Radius](#hex-bin-radius)[](#hex-bin-radius "Click to copy url")

**Syntax:** obj \<\< Hex Bin Radius( number )

**JMP Version Added:** 16

#### [Label](#label_1)[](#label_1 "Click to copy url")

**Syntax:** obj \<\< Label( "No Labels"\|"Label by Value"\|"Label by Percent of Total Values"\|"Label by Row" )

**JMP Version Added:** 14

#### [Label Format](#label-format_1)[](#label-format_1 "Click to copy url")

**Syntax:** obj \<\< Label Format

**JMP Version Added:** 16

#### [Max Label Size](#max-label-size)[](#max-label-size "Click to copy url")

**Syntax:** obj \<\< Max Label Size( number )

## [Histogram Element](#histogram-element)[](#histogram-element "Click to copy url")

### [Associated Constructors](#associated-constructors_9)[](#associated-constructors_9 "Click to copy url")

#### [Histogram Element](#histogram-element_1)[](#histogram-element_1 "Click to copy url")

**Syntax:** Histogram Element

**Description:** Shows a variable’s distribution using binning.

**Histogram with count axis**

``` jsl
Open( "$SAMPLE_DATA/Airline Delays.jmp" );
// histogram, count
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables( X( :Distance ), Wrap( :Airline, Show Title( 0 ) ) ),
    Elements( Histogram( X, Legend( 9 ) ) ),
    SendToReport(
        Dispatch( {}, "Distance", ScaleBox,
            {Min( -6 ), Max( 2900 ), Inc( 1000 ), Minor Ticks( 1 )}
        ),
        Dispatch( {}, "", ScaleBox, {Format( "Engineering SI", 12 ), Inc( 2000 )} ),
        Dispatch( {}, "graph title", TextEditBox,
            {Set Text( "Flight Distance by Airline" )}
        )
    )
);
```

**Histograms by factor level**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// histograms by level
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :sex ) ),
    Elements( Histogram( X, Y, Legend( 8 ) ) )
);
```

**Overlaid histograms, percent labels**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// overlaid histograms, percent labels
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Overlay( :sex ) ),
    Elements( Histogram( X, Legend( 8 ), Smoothness( -0.0833 ), Percents( 1 ) ) )
);
```

**Ridgeline plot**

``` jsl
Open( "$SAMPLE_DATA/NYC 311 Records.jmp" );
// ridgeline plot, overlapping kernel density estimate areas, KDE
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables( X( :Time ), Y( :Day of Week ) ),
    Elements(
        Histogram(
            X,
            Y,
            Legend( 3 ),
            Response Scale( "Percent" ),
            Overlap( 4.8 ),
            Histogram Style( "Kernel Density" ),
            Smoothness( -0.1 )
        )
    ),
    SendToReport(
        Dispatch( {}, "Time", ScaleBox, {Min( -2316 ), Max( 88403 ), Minor Ticks( 3 )} ),
        Dispatch( {}, "Day of Week", ScaleBox, {Max( 4.45 )} )
    )
);
```

**Smooth kernel density area**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// kernel density estimate KDE area chart
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :sex ) ),
    Elements(
        Histogram(
            X,
            Y,
            Legend( 8 ),
            Histogram Style( "Kernel Density" ),
            Smoothness( -0.08 )
        )
    )
);
```

### [Item Messages](#item-messages_9)[](#item-messages_9 "Click to copy url")

#### [Confid Percent](#confid-percent)[](#confid-percent "Click to copy url")

**Syntax:** obj \<\< Confid Percent( number=. )

**Description:** Confidence interval for the mean, given the coverage in percent. "." by default.

**JMP Version Added:** 14

#### [Counts](#counts)[](#counts "Click to copy url")

**Syntax:** obj \<\< Counts( state=0\|1 )

**JMP Version Added:** 15

#### [Histogram Style](#histogram-style)[](#histogram-style "Click to copy url")

**Syntax:** obj \<\< Histogram Style( "Bar"\|"Polygon"\|"Kernel Density"\|"Shadowgram" )

**JMP Version Added:** 15

#### [Horizontal](#horizontal)[](#horizontal "Click to copy url")

**Syntax:** obj \<\< Horizontal( state=0\|1 )

#### [Means and Std Devs](#means-and-std-devs)[](#means-and-std-devs "Click to copy url")

**Syntax:** obj \<\< Means and Std Devs( state=0\|1 )

**JMP Version Added:** 14

#### [Overlap](#overlap_1)[](#overlap_1 "Click to copy url")

**Syntax:** obj \<\< Overlap( number )

**JMP Version Added:** 15

#### [Percents](#percents)[](#percents "Click to copy url")

**Syntax:** obj \<\< Percents( state=0\|1 )

**JMP Version Added:** 15

#### [Response Axis](#response-axis_5)[](#response-axis_5 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Response Scale](#response-scale)[](#response-scale "Click to copy url")

**Syntax:** obj \<\< Response Scale( "Count"\|"Percent"\|"Fill" )

**JMP Version Added:** 15

#### [Smoothness](#smoothness_2)[](#smoothness_2 "Click to copy url")

**Syntax:** obj \<\< Smoothness( number )

**Description:** The bandwidth controls the amount of smoothing in the density curve. Decreasing the bandwidth makes the curve less smooth with more spikes. Increasing the bandwidth will smooth the curve but might obscure some detail.

**JMP Version Added:** 15

#### [Vertical](#vertical)[](#vertical "Click to copy url")

**Syntax:** obj \<\< Vertical( state=0\|1 )

**Description:** On by default.

#### [t Test for Mean At](#t-test-for-mean-at)[](#t-test-for-mean-at "Click to copy url")

**Syntax:** obj \<\< t Test for Mean At( number=. )

**Description:** Test that the mean is a specified value. "." by default.

**JMP Version Added:** 14

## [Line Element](#line-element)[](#line-element "Click to copy url")

### [Associated Constructors](#associated-constructors_10)[](#associated-constructors_10 "Click to copy url")

#### [Line Element](#line-element_1)[](#line-element_1 "Click to copy url")

**Syntax:** Line Element

**Description:** Shows a response summarized by categories.

**Arrow lines, one per row**

``` jsl
Open( "$SAMPLE_DATA/Cholesterol.jmp" );
// arrow lines, one per row
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :April AM ),
        X( :April PM, Position( 1 ) ),
        Y( :June AM ),
        Y( :June PM, Position( 1 ) ),
        Overlay( :treatment )
    ),
    Elements(
        Line(
            X( 1 ),
            X( 2 ),
            Y( 1 ),
            Y( 2 ),
            Legend( 8 ),
            Ordering( "Within Row" ),
            Connection( "Arrow" )
        )
    )
);
```

**Bump chart, connected rankings**

``` jsl
Open( "$SAMPLE_DATA/SATByYear.jmp" );
// Bump chart, line chart of ranking, smooth connections, transform column
Graph Builder(
    Transform Column(
        "Rank",
        Formula(
            (Col Number( :SAT Verbal, :Year, :"@Exclude"n, :"@Filter"n )
            -Col Rank( :SAT Verbal, :Year, :"@Exclude"n, :"@Filter"n )) + 1
        )
    ),
    Show Control Panel( 0 ),
    Variables( X( :Year ), Y( :Rank ), Overlay( :State ) ),
    Elements( Line( X, Y, Legend( 4 ), Connection( "Curve" ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :Region ),
            Where(
                :Region == {"Midwest", "Mountain", "New England", "Northeast", "Pacific",
                "Plains", "South", "Southwest"}
            )
        )
    ),
    SendToReport( Dispatch( {}, "Rank", ScaleBox, {Reversed Scale} ) )
);
```

**Connected arrows**

``` jsl
Open( "$SAMPLE_DATA/SAT.jmp" );
// arrow chart, multiple x and y variables, overlaid
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :"1992 Verbal"n ),
        X( :"1999 Verbal"n, Position( 1 ) ),
        X( :"2004 Verbal"n, Position( 1 ) ),
        Y( :"1992 Math"n ),
        Y( :"1999 Math"n, Position( 1 ) ),
        Y( :"2004 Math"n, Position( 1 ) ),
        Overlay( :State )
    ),
    Elements(
        Line(
            X( 1 ),
            X( 2 ),
            X( 3 ),
            Y( 1 ),
            Y( 2 ),
            Y( 3 ),
            Legend( 7 ),
            Ordering( "Within Row" ),
            Connection( "Arrow" )
        )
    ),
    Local Data Filter(
        Add Filter( columns( :"% Taking (2004)"n ), Where( :"% Taking (2004)"n >= 0.57788 ) )
    ),
    SendToReport(
        Dispatch( {}, "1992 Verbal & 2 more", TextEditBox, {Set Text( "Verbal" )} ),
        Dispatch( {}, "1992 Math & 2 more", TextEditBox, {Set Text( "Math" )} )
    )
);
```

**Connected scatter plot**

``` jsl
New Table( "prey and predator",
    Add Rows( 48 ),
    New Column( "Month", Formula( Row() ) ),
    New Column( "Rabbits", Formula( 10 * Cos( :Month * 0.35 ) + Random Normal( 50, 1.5 ) ) ),
    New Column( "Foxes", Formula( 8 * Cos( :Month * 0.35 + 1 ) + Random Normal( 30, 1 ) ) ),

);
// connected scatter plot, smooth line connections, row order
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Foxes ), Y( :Rabbits ), Color( :Month ) ),
    Elements(
        Line( X, Y, Legend( 5 ), Ordering( "Row Order" ), Connection( "Curve" ) ),
        Points( X, Y, Color( 0 ), Legend( 6 ) )
    )
);
```

**Event spans**

``` jsl
Open( "$SAMPLE_DATA/Nic Adverse Events.jmp" );
// event spans, start and stop times, categorical color
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Study Day of Start of Adverse Event ),
        X( :Study Day of End of Adverse Event, Position( 1 ) ),
        Y( :Unique Subject Identifier ),
        Color( :"Severity/Intensity"n )
    ),
    Elements( Line( X( 1 ), X( 2 ), Y, Legend( 4 ), Ordering( "Within Row" ) ) ),
    Local Data Filter(
        Add Filter(
            columns( :"Dictionary-Derived Term"n, :Action Taken with Study Treatment ),
            Where( :"Dictionary-Derived Term"n == "Hypertension" ),
            Where( :Action Taken with Study Treatment == "DRUG WITHDRAWN" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Unique Subject Identifier", ScaleBox,
            {Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                4,
                Properties( 0, {Line Color( RGB Color( 0.31, 0.61, 1 ) ), Line Width( 4 )} ),
                Properties(
                    1,
                    {Line Color( RGB Color( 0.69, 0.65, 0.01 ) ), Line Width( 4 )}
                ),
                Properties(
                    2,
                    {Line Color( RGB Color( 0.79, 0.09, 0.16 ) ), Line Width( 4 )}
                )
            )}
        )
    )
);
```

**Labeled lines**

``` jsl
Open( "$SAMPLE_DATA/Airline Delays.jmp" );
// overlaid line chart, labels in graph
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables( X( :Day of Week ), Y( :Arrival Delay ), Overlay( :Airline ) ),
    Elements( Line( X, Y, Legend( 11 ) ) ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                11,
                Type Properties( "H Line", {Line Label Properties( {Name Label( 1 )} )} ),
                Properties( 0, {Line Label Properties( {Name Label( 1 )} )} ),
                Properties( 1, {Line Label Properties( {Name Label( 1 )} )} ),
                Properties( 2, {Line Label Properties( {Name Label( 1 )} )} ),
                Properties( 3, {Line Label Properties( {Name Label( 1 )} )} ),
                Properties( 4, {Line Label Properties( {Name Label( 1 )} )} ),
                Properties( 5, {Line Label Properties( {Name Label( 1 )} )} )
            )}
        )
    )
);
```

**Line chart with error band**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// line chart, error band
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :height ) ),
    Elements(
        Line(
            X,
            Y,
            Legend( 4 ),
            Error Interval( "Confidence Interval" ),
            Interval Style( "Band" )
        )
    )
);
```

**Moving average line chart**

``` jsl
Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
// moving average line chart
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Pin ), Y( :Weight ), Color( :Product ) ),
    Elements(
        Points( X, Y, Legend( 11 ) ),
        Smoother( X, Y, Color( 0 ), Legend( 12 ), Method( "Moving Average" ) )
    ),
    SendToReport(
        Dispatch( {}, "Pin", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "Weight", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                12,
                Properties( 0, {Line Color( RGB Color( 0.25, 0.25, 0.25 ) )} )
            )}
        )
    )
);
```

**Run chart, by row order**

``` jsl
Open( "$SAMPLE_DATA/Time Series/Air.jmp" );
// Run chart, line chart by row, grid lines
Graph Builder(
    Show Control Panel( 0 ),
    Variables( Y( :Ozone Concentration ) ),
    Elements( Line( Y, Legend( 3 ) ) ),
    SendToReport(
        Dispatch( {}, "", ScaleBox,
            {Min( 0 ), Max( 220 ), Label Row( {Show Major Grid( 1 ), Show Minor Grid( 1 )} )}
        ),
        Dispatch( {}, "Ozone Concentration", ScaleBox, {Label Row( Show Major Grid( 1 ) )} )
    )
);
```

**Spaghetti plot**

``` jsl
Open( "$SAMPLE_DATA/Time Series/Air.jmp" );
// Spaghetti plot, line chart, smooth connections, mean line, transform column
Graph Builder(
    Transform Column( "Year", Nominal, Formula( Year( :date ) ) ),
    Show Control Panel( 0 ),
    Variables( X( :month ), Y( :Ozone Concentration ), Overlay( :Year ) ),
    Elements(
        Line( X, Y, Legend( 8 ), Connection( "Curve" ) ),
        Line( X, Y, Overlay( 0 ), Legend( 9 ), Connection( "Curve" ), Smoothness( 0.6 ) )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                8,
                Properties( 0, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 1, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 2, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 3, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 4, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 5, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 6, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 7, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 8, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 9, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 10, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 11, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 12, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 13, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 14, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 15, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 16, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 17, {Line Color( "gray" ), Transparency( 0.5 )} ),
                Properties( 18, {Line Color( "gray" ), Transparency( 0.5 )} )
            ), Legend Model( 9, Properties( 0, {Line Color( "black" ), Line Width( 4 )} ) )}
        )
    )
);
```

**Trailing moving average line chart**

``` jsl
Open( "$SAMPLE_DATA/Quality Control/Coating.jmp" );
// trailing moving average line chart
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Pin ), Y( :Weight ), Color( :Product ) ),
    Elements(
        Points( X, Y, Legend( 11 ) ),
        Smoother(
            X,
            Y,
            Color( 0 ),
            Legend( 12 ),
            Method( "Moving Average" ),
            Local Region( "Trailing" ),
            Local Width( 6 ),
            Trim( 0.6435 )
        )
    ),
    SendToReport(
        Dispatch( {}, "Pin", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "Weight", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                12,
                Properties( 0, {Line Color( RGB Color( 0.25, 0.25, 0.25 ) )} )
            )}
        )
    )
);
```

### [Item Messages](#item-messages_10)[](#item-messages_10 "Click to copy url")

#### [Connection](#connection_1)[](#connection_1 "Click to copy url")

**Syntax:** obj \<\< Connection( "Line"\|"Arrow"\|"Curve"\|"Step"\|"Centered Step"\|"Horizontal"\|"Vertical" )

#### [Error Interval](#error-interval_2)[](#error-interval_2 "Click to copy url")

**Syntax:** obj \<\< Error Interval( "Auto"\|"None"\|"Range"\|"Interquartile Range"\|"Standard Error"\|"Standard Deviation"\|"Confidence Interval"\|"Median Absolute Deviation"\|"Custom Interval"\|"Two-way Interval" )

#### [Fill](#fill_1)[](#fill_1 "Click to copy url")

**Syntax:** obj \<\< Fill( "None"\|"Fill Below"\|"Fill Between" )

**JMP Version Added:** 15

#### [Interval Style](#interval-style_2)[](#interval-style_2 "Click to copy url")

**Syntax:** obj \<\< Interval Style( "Error Bar"\|"Band"\|"Hash Band"\|"Arrow" )

#### [Missing Factors](#missing-factors_1)[](#missing-factors_1 "Click to copy url")

**Syntax:** obj \<\< Missing Factors( "Skip"\|"Treat as Missing"\|"Treat as Zero" )

**Description:** How to show connections that span missing factor levels

**JMP Version Added:** 15

#### [Missing Values](#missing-values_1)[](#missing-values_1 "Click to copy url")

**Syntax:** obj \<\< Missing Values( "Connect Through"\|"Connect Faded"\|"Connect Dashed"\|"No Connection" )

**Description:** How to show connections that span missing values.

#### [Ordering](#ordering_1)[](#ordering_1 "Click to copy url")

**Syntax:** obj \<\< Ordering( "Auto"\|"Row Order"\|"Summarized"\|"Within Row" )

#### [Response Axis](#response-axis_6)[](#response-axis_6 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Row order](#row-order_1)[](#row-order_1 "Click to copy url")

**Syntax:** obj \<\< Row order( state=0\|1 )

#### [Save Summary Formula](#save-summary-formula_2)[](#save-summary-formula_2 "Click to copy url")

**Syntax:** obj \<\< Save Summary Formula

#### [Smoothness](#smoothness_3)[](#smoothness_3 "Click to copy url")

**Syntax:** obj \<\< Smoothness( number )

#### [Stack](#stack)[](#stack "Click to copy url")

**Syntax:** obj \<\< Stack( state=0\|1 )

**JMP Version Added:** 15

#### [Stack Negative](#stack-negative_1)[](#stack-negative_1 "Click to copy url")

**Syntax:** obj \<\< Stack Negative( "Overlap"\|"Separate Negative"\|"Treat as Zero" )

**Description:** Controls how negative data values are handled when stacked.

**JMP Version Added:** 17

#### [Summary Statistic](#summary-statistic_4)[](#summary-statistic_4 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

## [Line of Fit Element](#line-of-fit-element)[](#line-of-fit-element "Click to copy url")

### [Associated Constructors](#associated-constructors_11)[](#associated-constructors_11 "Click to copy url")

#### [Line of Fit Element](#line-of-fit-element_1)[](#line-of-fit-element_1 "Click to copy url")

**Syntax:** Line of Fit Element

**Description:** Shows a linear regression with confidence intervals for continuous X and Y. Fits means for categorical X.

**ANOVA fit, oneway, means comparison**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// ANOVA fit, oneway, means comparison, confidence interval, F test p-value
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :weight ) ),
    Elements(
        Points( X, Y, Legend( 1 ) ),
        Line Of Fit( X, Y, Legend( 2 ), Unequal Variances( 1 ), F Test( 1 ) )
    )
);
```

**Overlaid linear regressions**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// linear regression, overlaid with confidence intervals
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ), Overlay( :sex ) ),
    Elements( Points( X, Y, Legend( 2 ) ), Line Of Fit( X, Y, Legend( 4 ) ) )
);
```

**Quadratic fits**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// linear regression, overlaid curves, quadratic
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Culmen Length ), Y( :Flipper Length ), Overlay( :Species ) ),
    Elements(
        Points( X, Y, Legend( 9 ) ),
        Line Of Fit( X, Y, Legend( 10 ), Degree( "Quadratic" ) )
    )
);
```

**Time series regression**

``` jsl
Open( "$SAMPLE_DATA/Time Series/Monthly Sales.jmp" );
// time series regression, periodic
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Date ), Y( :Sales ) ),
    Elements(
        Points( X, Y, Legend( 3 ) ),
        Line Of Fit( X, Y, Legend( 5 ), Fit( "Time Series" ), Seasonal Period( 12 ) )
    )
);
```

### [Item Messages](#item-messages_11)[](#item-messages_11 "Click to copy url")

#### [Adapt to Axis Scale](#adapt-to-axis-scale_2)[](#adapt-to-axis-scale_2 "Click to copy url")

**Syntax:** obj \<\< Adapt to Axis Scale( state=0\|1 )

**Description:** For log and other axis transformations, apply computations on the transformed coordinates.

#### [Confidence of Fit](#confidence-of-fit)[](#confidence-of-fit "Click to copy url")

**Syntax:** obj \<\< Confidence of Fit( state=0\|1 )

#### [Confidence of Prediction](#confidence-of-prediction)[](#confidence-of-prediction "Click to copy url")

**Syntax:** obj \<\< Confidence of Prediction( state=0\|1 )

#### [Constrain Parameters](#constrain-parameters)[](#constrain-parameters "Click to copy url")

**Syntax:** obj \<\< Constrain Parameters( state=0\|1 )

**Description:** Constrain ETS parameters.

**JMP Version Added:** 17

#### [Degree](#degree)[](#degree "Click to copy url")

**Syntax:** obj \<\< Degree( "Linear"\|"Quadratic"\|"Cubic" )

#### [Equation](#equation)[](#equation "Click to copy url")

**Syntax:** obj \<\< Equation( state=0\|1 )

**Description:** Equation of the fit.

#### [F Test](#f-test)[](#f-test "Click to copy url")

**Syntax:** obj \<\< F Test( state=0\|1 )

**Description:** Significance level for the whole-model test.

**JMP Version Added:** 14

#### [Fit](#fit)[](#fit "Click to copy url")

**Syntax:** obj \<\< Fit( "Polynomial"\|"Robust Cauchy"\|"Time Series" )

**JMP Version Added:** 15

#### [Forecast Model](#forecast-model)[](#forecast-model "Click to copy url")

**Syntax:** obj \<\< Forecast Model( state=0\|1 )

**Description:** Show which model is used to forecast, with parameter estimates.

**JMP Version Added:** 15

#### [Forecast Periods](#forecast-periods)[](#forecast-periods "Click to copy url")

**Syntax:** obj \<\< Forecast Periods( number )

**Description:** Number of periods ahead to forecast.

**JMP Version Added:** 15

#### [Means and Std Devs](#means-and-std-devs_1)[](#means-and-std-devs_1 "Click to copy url")

**Syntax:** obj \<\< Means and Std Devs( state=0\|1 )

**Description:** Show the means and standard deviations of each group next to mean line.

**JMP Version Added:** 14

#### [Prediction](#prediction)[](#prediction "Click to copy url")

**Syntax:** obj \<\< Prediction( state=0\|1 )

**Description:** The confidence region for individual predicted values

#### [RMSE](#rmse)[](#rmse "Click to copy url")

**Syntax:** obj \<\< RMSE( state=0\|1 )

**Description:** Root Mean Square Error, a measure of error in units of the response.

#### [Response Axis](#response-axis_7)[](#response-axis_7 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Root Mean Square Error](#root-mean-square-error)[](#root-mean-square-error "Click to copy url")

**Syntax:** obj \<\< Root Mean Square Error( state=0\|1 )

#### [R²](#r2)[](#r2 "Click to copy url")

**Syntax:** obj \<\< R²( state=0\|1 )

**Description:** Coefficient of determination, a measure of how well the fit predicts the data.

#### [Save Formula](#save-formula)[](#save-formula "Click to copy url")

**Syntax:** obj \<\< Save Formula

#### [Seasonal Period](#seasonal-period)[](#seasonal-period "Click to copy url")

**Syntax:** obj \<\< Seasonal Period( number )

**Description:** Number of periods in a season. For example, with monthly data, there are 12 periods for seasonal over a year.

**JMP Version Added:** 15

#### [Unequal Variances](#unequal-variances)[](#unequal-variances "Click to copy url")

**Syntax:** obj \<\< Unequal Variances( state=0\|1 )

**Description:** Whether to calculate tests and confidence limits based on assuming different groups have different variances.

## [Mosaic Element](#mosaic-element)[](#mosaic-element "Click to copy url")

### [Associated Constructors](#associated-constructors_12)[](#associated-constructors_12 "Click to copy url")

#### [Mosaic Element](#mosaic-element_1)[](#mosaic-element_1 "Click to copy url")

**Syntax:** Mosaic Element

**Description:** Shows counts using size for X and Y categories.

**Horizontal mosaic**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// horizontal mosaic, axis label line wrapping
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Clutch Completion ), Y( :Species ) ),
    Elements( Mosaic( X, Y, Legend( 5 ), Response Axis( "X" ) ) )
);
```

**Mosaic chart**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// mosaic, marimekko
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ), Y( :sex ) ),
    Elements( Mosaic( X, Y, Legend( 4 ) ) )
);
```

### [Item Messages](#item-messages_12)[](#item-messages_12 "Click to copy url")

#### [Cell Labeling](#cell-labeling)[](#cell-labeling "Click to copy url")

**Syntax:** obj \<\< Cell Labeling( "No Labels"\|"Label by Count"\|"Label by Percent"\|"Label by Value"\|"Label by Row" )

**JMP Version Added:** 14

#### [Chi-square Test](#chi-square-test)[](#chi-square-test "Click to copy url")

**Syntax:** obj \<\< Chi-square Test( state=0\|1 )

**Description:** Chi-square test that response rates are the same across groups, or that two responses are independent

**JMP Version Added:** 14

#### [Confid Percent](#confid-percent_1)[](#confid-percent_1 "Click to copy url")

**Syntax:** obj \<\< Confid Percent( number=. )

**Description:** Confidence interval coverage on the proportion in the upper level, in percent. "." by default.

**JMP Version Added:** 14

#### [Horizontal](#horizontal_1)[](#horizontal_1 "Click to copy url")

**Syntax:** obj \<\< Horizontal( state=0\|1 )

#### [Label Format](#label-format_2)[](#label-format_2 "Click to copy url")

**Syntax:** obj \<\< Label Format

**JMP Version Added:** 16

#### [Response Axis](#response-axis_8)[](#response-axis_8 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Test Proportion At](#test-proportion-at)[](#test-proportion-at "Click to copy url")

**Syntax:** obj \<\< Test Proportion At( number=. )

**Description:** Test that the proportion in the upper level is a specified value. "." by default.

**JMP Version Added:** 14

#### [Vertical](#vertical_1)[](#vertical_1 "Click to copy url")

**Syntax:** obj \<\< Vertical( state=0\|1 )

**Description:** On by default.

## [Parallel Element](#parallel-element)[](#parallel-element "Click to copy url")

### [Associated Constructors](#associated-constructors_13)[](#associated-constructors_13 "Click to copy url")

#### [Parallel Element](#parallel-element_1)[](#parallel-element_1 "Click to copy url")

**Syntax:** Parallel Element

**Description:** Shows many variables along parallel axes with a connected line for each row.

**Parallel box plots**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// parallel coordinates - box plots
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Height ),
        X( :Skinfold, Position( 1 ) ),
        X( :Weight, Position( 1 ) ),
        X( :"% Ideal Body Wt."n, Position( 1 ) ),
        X( :"% Ideal Weight-3yr"n, Position( 1 ) ),
        X( :"Weight-3yr"n, Position( 1 ) ),
        X( :Cholesterol, Position( 1 ) ),
        X( :Triglycerides, Position( 1 ) ),
        X( :HDL, Position( 1 ) ),
        X( :LDL, Position( 1 ) ),
        X( :Cholesterol Loss, Position( 1 ) )
    ),
    Elements(
        Box Plot(
            X( 1 ),
            X( 2 ),
            X( 3 ),
            X( 4 ),
            X( 5 ),
            X( 6 ),
            X( 7 ),
            X( 8 ),
            X( 9 ),
            X( 11 )
        )
    )
);
```

**Parallel coordinates plot**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// parallel coordinates - lines
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Height ),
        X( :Skinfold, Position( 1 ) ),
        X( :Weight, Position( 1 ) ),
        X( :"% Ideal Body Wt."n, Position( 1 ) ),
        X( :"% Ideal Weight-3yr"n, Position( 1 ) ),
        X( :"Weight-3yr"n, Position( 1 ) ),
        X( :Cholesterol, Position( 1 ) ),
        X( :Triglycerides, Position( 1 ) ),
        X( :HDL, Position( 1 ) ),
        X( :LDL, Position( 1 ) ),
        X( :Cholesterol Loss, Position( 1 ) ),
        Color( :Sex )
    ),
    Elements(
        Parallel(
            X( 1 ),
            X( 2 ),
            X( 3 ),
            X( 4 ),
            X( 5 ),
            X( 6 ),
            X( 7 ),
            X( 8 ),
            X( 9 ),
            X( 10 ),
            X( 11 ),
            Smoothness( 0.5 )
        )
    )
);
```

**Parallel coordinates with aligned scale**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// parallel coordinates - aligned scale
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :"Trig-3yrs"n, Combine( "Parallel Merged" ) ),
        X( :"Chol-3yrs"n, Position( 1 ), Combine( "Parallel Merged" ) ),
        X( :"HDL-3yrs"n, Position( 1 ), Combine( "Parallel Merged" ) ),
        X( :"LDL-3yrs"n, Position( 1 ), Combine( "Parallel Merged" ) )
    ),
    Elements( Parallel( X( 1 ), X( 2 ), X( 3 ), X( 4 ), Legend( 8 ) ) )
);
```

**Parallel dot plots**

``` jsl
Open( "$SAMPLE_DATA/Lipid Data.jmp" );
// parallel coordinates - dots
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Height ),
        X( :Skinfold, Position( 1 ) ),
        X( :Weight, Position( 1 ) ),
        X( :"% Ideal Body Wt."n, Position( 1 ) ),
        X( :"% Ideal Weight-3yr"n, Position( 1 ) ),
        X( :"Weight-3yr"n, Position( 1 ) ),
        X( :Cholesterol, Position( 1 ) ),
        X( :Triglycerides, Position( 1 ) ),
        X( :HDL, Position( 1 ) ),
        X( :LDL, Position( 1 ) ),
        X( :Cholesterol Loss, Position( 1 ) ),
        Color( :Sex )
    ),
    Points(
        Parallel(
            X( 1 ),
            X( 2 ),
            X( 3 ),
            X( 4 ),
            X( 5 ),
            X( 6 ),
            X( 7 ),
            X( 8 ),
            X( 9 ),
            X( 10 ),
            X( 11 ),
            Smoothness( 0.5 )
        )
    )
);
```

**Parallel sets**

``` jsl
Open( "$SAMPLE_DATA/Titanic Passengers.jmp" );
// parallel sets
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Survived ),
        X( :Passenger Class, Position( 1 ) ),
        X( :Sex, Position( 1 ) ),
        X( :Age, Position( 1 ) ),
        Color( :Survived )
    ),
    Elements( Parallel( X( 1 ), X( 2 ), X( 3 ), X( 4 ), Legend( 5 ) ) ),
    SendToReport(
        Dispatch( {}, "Graph Builder", FrameBox,
            {DispatchSeg( ParallelAxisSeg( 1 ), Reversed( Passenger Class, Sex ) )}
        )
    )
);
```

**Sankey parallel sets**

``` jsl
Open( "$SAMPLE_DATA/Color Preference Survey.jmp" );
// parallel sets, sankey, categorical parallel coordinates
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables(
        X( :What is your gender?, Combine( "Parallel Independent" ) ),
        X(
            :"What is your favorite color? (select one)"n,
            Position( 1 ),
            Combine( "Parallel Independent" )
        ),
        X( :What is your favorite color?, Position( 1 ), Combine( "Parallel Independent" ) ),
        Color( :"What is your favorite color? (select one)"n )
    ),
    Elements( Parallel( X( 1 ), X( 2 ), X( 3 ), Legend( 15 ) ) ),
    SendToReport(
        Dispatch( {}, "What is your gender?", ScaleBox,
            {Label Row(
                {Tick Mark(
                    Label( "What is your favorite color?" ),
                    Label( "Specific favorite color" )
                ), Tick Mark(
                    Label( "What is your favorite color? (select one)" ),
                    Label( "General favorite color" )
                ), Tick Mark( Label( "What is your gender?" ), Label( "Gender" ) )}
            )}
        )
    )
);
```

### [Item Messages](#item-messages_13)[](#item-messages_13 "Click to copy url")

#### [Axes Labels](#axes-labels)[](#axes-labels "Click to copy url")

**Syntax:** obj \<\< Axes Labels( state=0\|1 )

#### [Combine Sets](#combine-sets)[](#combine-sets "Click to copy url")

**Syntax:** obj \<\< Combine Sets( state=0\|1 )

#### [Smoothness](#smoothness_4)[](#smoothness_4 "Click to copy url")

**Syntax:** obj \<\< Smoothness( number )

**JMP Version Added:** 16

## [Pie Element](#pie-element)[](#pie-element "Click to copy url")

### [Associated Constructors](#associated-constructors_14)[](#associated-constructors_14 "Click to copy url")

#### [Pie Element](#pie-element_1)[](#pie-element_1 "Click to copy url")

**Syntax:** Pie Element

**Description:** Shows portions of a whole.

**Donut chart by count**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// donut chart by count
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ) ),
    Elements( Pie( X, Legend( 6 ), Pie Style( "Ring" ) ) )
);
```

**Pie chart by count**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// pie chart by count
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :age ) ),
    Elements( Pie( X, Legend( 6 ) ) )
);
```

**Pie panel**

``` jsl
Open( "$SAMPLE_DATA/Smartphone OS.jmp" );
// pie panel
Graph Builder(
    Transform Column( "Market Share freq", Formula( Round( :Market Share * 1000 ) ) ),
    Show Control Panel( 0 ),
    Show Footer( 0 ),
    Variables( X( :Operating System ), Wrap( :Year ), Frequency( :Market Share freq ) ),
    Elements( Pie( X, Legend( 6 ) ) ),
    SendToReport(
        Dispatch( {}, "graph title", TextEditBox,
            {Set Text( "SmartPhone OS Market Share" )}
        )
    )
);
```

### [Item Messages](#item-messages_14)[](#item-messages_14 "Click to copy url")

#### [Label](#label_2)[](#label_2 "Click to copy url")

**Syntax:** obj \<\< Label( "No Labels"\|"Label by Value"\|"Label by Percent of Total Values"\|"Label by Row" )

#### [Label Format](#label-format_3)[](#label-format_3 "Click to copy url")

**Syntax:** obj \<\< Label Format

**JMP Version Added:** 16

#### [Pie Style](#pie-style)[](#pie-style "Click to copy url")

**Syntax:** obj \<\< Pie Style( "Pie"\|"Ring"\|"Coxcomb" )

#### [Summary Statistic](#summary-statistic_5)[](#summary-statistic_5 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

## [Points Element](#points-element)[](#points-element "Click to copy url")

### [Associated Constructors](#associated-constructors_15)[](#associated-constructors_15 "Click to copy url")

#### [Points Element](#points-element_1)[](#points-element_1 "Click to copy url")

**Syntax:** Points Element

**Description:** Shows a scatter plot of data values.

**Centered side-by-side dot plots**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// center dot plots, colored by categorical variable
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ), Color( :Sex ) ),
    Elements( Points( X, Y, Legend( 10 ) ) ),
    SendToReport(
        Dispatch( {}, "Species", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                10,
                Properties( 0, {Marker Size( 5 )} ),
                Properties( 1, {Marker Size( 5 )} )
            )}
        )
    )
);
```

**Circle packing jitter**

``` jsl
Open( "$SAMPLE_DATA/Design Experiment/Peanut Data.jmp" );
// categorical 2D jitter, circle packing, color by response
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :"Pre-Soak"n ), Y( :Hydrolyze ), Color( :Solids ) ),
    Elements( Points( X, Y, Legend( 4 ) ) ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 4, Properties( 1, {Marker Size( 10 )} ) )}
        )
    )
);
```

**Density dot plot**

``` jsl
Open( "$SAMPLE_DATA/Online Consumer Data.jmp" );
// density dot plot, beeswarm
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables( X( :Privacy ), Y( :Female ) ),
    Elements(
        Points(
            X,
            Y,
            Legend( 3 ),
            Jitter( "Hex Grid" ),
            Jitter Side( "Positive" ),
            Jitter Smooth( 1 )
        )
    ),
    SendToReport(
        Dispatch( {}, "Female", ScaleBox,
            {Min( 0 ), Max( 1.99 ), Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 3, Properties( 0, {Marker( "FilledCircle" )} ) )}
        )
    )
);
```

**Hexagonal grid dot plots**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// center hexagonal grid dot plots, smoothed jitter placement, colored by categorical variable
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ), Color( :Sex ) ),
    Elements( Points( X, Y, Legend( 10 ), Jitter( "Hex Grid" ), Jitter Smooth( 1 ) ) ),
    SendToReport(
        Dispatch( {}, "Species", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                10,
                Properties( 0, {Marker Size( 5 )} ),
                Properties( 1, {Marker Size( 5 )} )
            )}
        )
    )
);
```

**Hexagonal opposite-side dot plots**

``` jsl
Open( "$SAMPLE_DATA/S4 Temps.jmp" );
// dot plot, hexagonal jitter from opposite side (ordinal), custom axis label format
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables( X( :Y ), Y( :type of space ) ),
    Elements(
        Points(
            X,
            Y,
            Legend( 9 ),
            Jitter( "Hex Grid" ),
            Jitter Side( "Ordinal" ),
            Jitter Smooth( 1 )
        )
    ),
    Local Data Filter(
        Add Filter(
            columns( :type of space ),
            Where( :type of space == {"exterior", "interior"} )
        )
    ),
    SendToReport(
        Dispatch( {}, "Y", ScaleBox,
            {Format( "Custom", Formula( Char( value ) || "°" ), 12, 0 )}
        ),
        Dispatch( {}, "type of space", ScaleBox, {Min( 0 ), Max( 1 )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 9, Properties( 0, {Line Color( "Gray" ), Marker Size( 6 )} ) )}
        ),
        Dispatch( {}, "Y", TextEditBox, {Set Text( "Temperature (Celcius))" )} )
    )
);
```

**Latitude and Longitude**

``` jsl
Open( "$SAMPLE_DATA/Cities.jmp" );
// geographic scatter plot, background map, sized dots
Graph Builder(
    Show Control Panel( 0 ),
    Show X Axis( 0 ),
    Show Y Axis( 0 ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables( X( :Longitude ), Y( :Latitude ), Color( :PM10 ), Size( :POP ) ),
    Elements( Points( X, Y, Legend( 2 ) ) ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                2,
                Properties( 0, {Marker Size( 8 )} ),
                Properties( 1, {gradient( {Color Theme( "Muted Yellow to Red" )} )} )
            )}
        ),
        Dispatch( {}, "Graph Builder", FrameBox,
            {Background Map( Boundaries( "US States" ) )}
        )
    )
);
```

**Scatter plot matrix**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// scatter plot matrix with main diagonal histograms
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Culmen Length ),
        X( :Culmen Depth ),
        X( :Flipper Length ),
        X( :Body Mass ),
        Y( :Culmen Length ),
        Y( :Culmen Depth ),
        Y( :Flipper Length ),
        Y( :Body Mass ),
        Overlay( :Species )
    ),
    Elements( Position( 1, 1 ), Histogram( X, Y, Legend( 87 ) ) ),
    Elements(
        Position( 1, 2 ),
        Points( X, Y, Legend( 57 ) ),
        Smoother( X, Y, Legend( 58 ) )
    ),
    Elements(
        Position( 1, 3 ),
        Points( X, Y, Legend( 59 ) ),
        Smoother( X, Y, Legend( 60 ) )
    ),
    Elements(
        Position( 1, 4 ),
        Points( X, Y, Legend( 61 ) ),
        Smoother( X, Y, Legend( 62 ) )
    ),
    Elements(
        Position( 2, 1 ),
        Points( X, Y, Legend( 63 ) ),
        Smoother( X, Y, Legend( 64 ) )
    ),
    Elements( Position( 2, 2 ), Histogram( X, Y, Legend( 88 ) ) ),
    Elements(
        Position( 2, 3 ),
        Points( X, Y, Legend( 67 ) ),
        Smoother( X, Y, Legend( 68 ) )
    ),
    Elements(
        Position( 2, 4 ),
        Points( X, Y, Legend( 69 ) ),
        Smoother( X, Y, Legend( 70 ) )
    ),
    Elements(
        Position( 3, 1 ),
        Points( X, Y, Legend( 71 ) ),
        Smoother( X, Y, Legend( 72 ) )
    ),
    Elements(
        Position( 3, 2 ),
        Points( X, Y, Legend( 73 ) ),
        Smoother( X, Y, Legend( 74 ) )
    ),
    Elements( Position( 3, 3 ), Histogram( X, Y, Legend( 89 ) ) ),
    Elements(
        Position( 3, 4 ),
        Points( X, Y, Legend( 77 ) ),
        Smoother( X, Y, Legend( 78 ) )
    ),
    Elements(
        Position( 4, 1 ),
        Points( X, Y, Legend( 79 ) ),
        Smoother( X, Y, Legend( 80 ) )
    ),
    Elements(
        Position( 4, 2 ),
        Points( X, Y, Legend( 81 ) ),
        Smoother( X, Y, Legend( 82 ) )
    ),
    Elements(
        Position( 4, 3 ),
        Points( X, Y, Legend( 83 ) ),
        Smoother( X, Y, Legend( 84 ) )
    ),
    Elements( Position( 4, 4 ), Histogram( X, Y, Legend( 90 ) ) )
);
```

**Scatter plot using size and color**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// bubble plot
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Culmen Depth ),
        Y( :Culmen Length ),
        Group X( :Species, Show Title( 0 ) ),
        Color( :Sex ),
        Size( :Body Mass )
    ),
    Elements( Points( X, Y, Legend( 20 ) ) ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                20,
                Properties( 1, {Marker( "Circle" ), Transparency( 0.5 )}, ),
                Properties( 2, {Marker( "FilledCircle" ), Transparency( 0.5 )} )
            )}
        )
    )
);
```

**Smoothed centered side-by-side dot plots**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// center dot plots, smoothed jitter placement, colored by categorical variable
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Species ), Y( :Body Mass ), Color( :Sex ) ),
    Elements( Points( X, Y, Legend( 10 ), Jitter Smooth( 0.5 ) ) ),
    SendToReport(
        Dispatch( {}, "Species", ScaleBox, {Label Row( Show Major Grid( 1 ) )} ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                10,
                Properties( 0, {Marker Size( 5 )} ),
                Properties( 1, {Marker Size( 5 )} )
            )}
        )
    )
);
```

**Smoothed dot plot**

``` jsl
Open( "$SAMPLE_DATA/Online Consumer Data.jmp" );
// smoothed dot plot, color by ordinal
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Privacy ), Y( :Female ), Color( :Internet Use ) ),
    Elements( Points( X, Y, Legend( 5 ), Jitter Smooth( 0.8 ) ) ),
    SendToReport(
        Dispatch( {}, "Privacy", ScaleBox,
            {Min( -2 ), Max( 2 ), Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "400", ScaleBox,
            {Legend Model(
                5,
                Type Properties( 0, "Marker", {Marker Size( 5 )} ),
                Properties(
                    0,
                    {Line Color( RGB Color( 0.86, 0.52, 0.35 ) ), Marker Size( 5 )}
                ),
                Properties(
                    1,
                    {Line Color( RGB Color( 0.95, 0.79, 0.45 ) ), Marker Size( 5 )}
                ),
                Properties(
                    2,
                    {Line Color( RGB Color( 0.56, 0.02, 0.23 ) ), Marker Size( 5 )}
                ),
                Properties(
                    3,
                    {Line Color( RGB Color( 0.88, 0.9, 0.74 ) ), Marker Size( 5 )}
                )
            )}
        ),
        Dispatch( {}, "400", LegendBox, {Legend Position( {5, [1, 2, 0, 3]} )} )
    )
);
```

**Variability chart**

``` jsl
Open( "$SAMPLE_DATA/Variability Data/2 Factors Nested.jmp" );
// variability chart, mean and range interval, nested axis
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Operator ), X( :Part, Position( 1 ) ), Y( :Y ) ),
    Elements(
        Points(
            X( 1 ),
            X( 2 ),
            Y,
            Legend( 3 ),
            Summary Statistic( "Mean" ),
            Error Interval( "Range" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Operator", ScaleBox, {Label Row( 2, Show Major Grid( 1 ) )} )
    )
);
```

### [Item Messages](#item-messages_15)[](#item-messages_15 "Click to copy url")

#### [Error Interval](#error-interval_3)[](#error-interval_3 "Click to copy url")

**Syntax:** obj \<\< Error Interval( "Auto"\|"None"\|"Range"\|"Interquartile Range"\|"Standard Error"\|"Standard Deviation"\|"Confidence Interval"\|"Median Absolute Deviation"\|"Custom Interval"\|"Two-way Interval" )

#### [Interval Style](#interval-style_3)[](#interval-style_3 "Click to copy url")

**Syntax:** obj \<\< Interval Style( "Error Bar"\|"Band"\|"Hash Band"\|"Arrow" )

#### [Jitter](#jitter_2)[](#jitter_2 "Click to copy url")

**Syntax:** obj \<\< Jitter( "None"\|"Auto"\|"Random Uniform"\|"Random Normal"\|"Density Random"\|"Packed"\|"Grid"\|"Hex Grid"\|"Beeswarm" )

#### [Jitter Limit](#jitter-limit)[](#jitter-limit "Click to copy url")

**Syntax:** obj \<\< Jitter Limit( number )

**JMP Version Added:** 14

#### [Jitter Overlap](#jitter-overlap)[](#jitter-overlap "Click to copy url")

**Syntax:** obj \<\< Jitter Overlap( number )

**JMP Version Added:** 19

#### [Jitter Side](#jitter-side)[](#jitter-side "Click to copy url")

**Syntax:** obj \<\< Jitter Side( "Centered"\|"Positive"\|"Negative"\|"Ordinal" )

#### [Jitter Smooth](#jitter-smooth)[](#jitter-smooth "Click to copy url")

**Syntax:** obj \<\< Jitter Smooth( number )

**JMP Version Added:** 19

#### [Label](#label_3)[](#label_3 "Click to copy url")

**Syntax:** obj \<\< Label( "No Labels"\|"Label by Value"\|"Label by Row"\|"Label by Row and Value" )

#### [Label Format](#label-format_4)[](#label-format_4 "Click to copy url")

**Syntax:** obj \<\< Label Format

**JMP Version Added:** 18

#### [Response Axis](#response-axis_9)[](#response-axis_9 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Save Summary Formula](#save-summary-formula_3)[](#save-summary-formula_3 "Click to copy url")

**Syntax:** obj \<\< Save Summary Formula

#### [Set Shape Column](#set-shape-column)[](#set-shape-column "Click to copy url")

**Syntax:** obj \<\< Set Shape Column

**JMP Version Added:** 16

#### [Set Shape Expression](#set-shape-expression)[](#set-shape-expression "Click to copy url")

**Syntax:** obj \<\< Set Shape Expression

**JMP Version Added:** 16

#### [Summary Statistic](#summary-statistic_6)[](#summary-statistic_6 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "None"\|"N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

## [Shapes Element](#shapes-element)[](#shapes-element "Click to copy url")

### [Associated Constructors](#associated-constructors_16)[](#associated-constructors_16 "Click to copy url")

#### [Map Shapes Element](#map-shapes-element)[](#map-shapes-element "Click to copy url")

**Syntax:** Map Shapes Element

**Description:** Shows areas defined by a Map Shape variable, usually with a Color variable.

**Asia/Pacific-centered world map**

``` jsl
Open( "$SAMPLE_DATA/World Demographics.jmp" );
// world map, choropleth, grid lines, Pacific centering
Graph Builder(
    Size( 1094, 586 ),
    Show Control Panel( 0 ),
    Variables( Color( :Total Median Age ), Shape( :Territory ) ),
    Elements( Map Shapes( Legend( 3 ) ) ),
    SendToReport(
        Dispatch( {}, "", ScaleBox,
            {Format( "Longitude DDD", "PUNDIR", 16 ), Min( -23.27 ), Max( 327.33 ), Inc( 30 ),
            Minor Ticks( 0 ), Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "", ScaleBox( 2 ),
            {Format( "Latitude DDD", "PUNDIR", 16 ), Min( -87.55 ), Max( 87.55 ), Inc( 30 ),
            Minor Ticks( 0 ), Label Row( Show Major Grid( 1 ) )}
        )
    )
);
```

**Custom shape file with categorical color**

``` jsl
Open( "$SAMPLE_DATA/S4 Temps.jmp" );
// custom shape file choropleth, categorical color
Graph Builder(
    Show Control Panel( 0 ),
    Show X Axis( 0 ),
    Show Y Axis( 0 ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables( Color( :sector ), Shape( :"room/office"n ) ),
    Elements( Map Shapes( Legend( 2 ) ) )
);
```

**Custom shape file with gradient color**

``` jsl
Open( "$SAMPLE_DATA/S4 Temps.jmp" );
// custom shape file choropleth, color gradient
Graph Builder(
    Show Control Panel( 0 ),
    Show X Axis( 0 ),
    Show Y Axis( 0 ),
    Show X Axis Title( 0 ),
    Show Y Axis Title( 0 ),
    Variables( Group X( :time of day ), Color( :fahrenheit ), Shape( :"room/office"n ) ),
    Elements( Map Shapes( Legend( 2 ) ) )
);
```

**Mediterranean equal-area choropleth**

``` jsl
Open( "$SAMPLE_DATA/World Demographics.jmp" );
// Mediterranean map, choropleth, equal area projection, grid lines
Graph Builder(
    Size( 1094, 586 ),
    Show Control Panel( 0 ),
    Variables( Color( :Total Median Age ), Shape( :Territory ) ),
    Elements( Map Shapes( Legend( 3 ) ) ),
    SendToReport(
        Dispatch( {}, "", ScaleBox,
            {Format( "Longitude DDD", "PUNDIR", 16 ), Min( -14.2917884823647 ),
            Max( 64.9684846475565 ), Inc( 20 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "", ScaleBox( 2 ),
            {Format( "Latitude DDD", "PUNDIR", 16 ), Min( 21.8020806509188 ),
            Max( 61.3932495299748 ), Inc( 10 ), Minor Ticks( 1 ),
            Label Row( Show Major Grid( 1 ) )}
        )
    )
);
```

**World map choropleth**

``` jsl
Open( "$SAMPLE_DATA/World Demographics.jmp" );
// world map, choropleth, grid lines
Graph Builder(
    Show Control Panel( 0 ),
    Variables( Color( :Total Median Age ), Shape( :Territory ) ),
    Elements( Map Shapes( Legend( 3 ) ) ),
    SendToReport(
        Dispatch( {}, "", ScaleBox,
            {Format( "Longitude DDD", "PUNDIR", 16 ), Min( -175.3 ), Max( 175.3 ), Inc( 30 ),
            Minor Ticks( 0 ), Label Row( Show Major Grid( 1 ) )}
        ),
        Dispatch( {}, "", ScaleBox( 2 ),
            {Format( "Latitude DDD", "PUNDIR", 16 ), Min( -82.6 ), Max( 82.6 ), Inc( 30 ),
            Minor Ticks( 0 ), Label Row( Show Major Grid( 1 ) )}
        )
    )
);
```

### [Item Messages](#item-messages_16)[](#item-messages_16 "Click to copy url")

#### [Aspect Ratio](#aspect-ratio)[](#aspect-ratio "Click to copy url")

**Syntax:** obj \<\< Aspect Ratio( number )

**Description:** Adjustment factor for X:Y scaling ratio.

#### [Show Missing Shapes](#show-missing-shapes)[](#show-missing-shapes "Click to copy url")

**Syntax:** obj \<\< Show Missing Shapes( state=0\|1 )

**JMP Version Added:** 16

#### [Summary Statistic](#summary-statistic_7)[](#summary-statistic_7 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

## [Smoother Element](#smoother-element)[](#smoother-element "Click to copy url")

### [Associated Constructors](#associated-constructors_17)[](#associated-constructors_17 "Click to copy url")

#### [Smoother Element](#smoother-element_1)[](#smoother-element_1 "Click to copy url")

**Syntax:** Smoother Element

**Description:** Shows a smooth curve through the data. Best for continuous X and Y with an unknown relationship.

**Cyclical smoother**

``` jsl
Open( "$SAMPLE_DATA/Time Series/Air.jmp" );
// smoother, cycle, p-spline, bootstrap confidence interval
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :month ), Y( :Ozone Concentration ) ),
    Elements(
        Points( X, Y, Legend( 5 ) ),
        Smoother(
            X,
            Y,
            Legend( 6 ),
            Method( "P-Spline" ),
            Shape Constraint( "Cycle" ),
            Confidence of Fit( 1 )
        )
    )
);
```

**Monotonic on log x axis**

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/Bioassay.jmp" );
// monotonic spline smoother, log x axis, overlaid, legend in graph corner
Graph Builder(
    Show Control Panel( 0 ),
    Legend Position( "Inside Left" ),
    Variables( X( :Concentration ), Y( :Toxicity ), Overlay( :Formulation ) ),
    Elements(
        Points( X, Y, Legend( 11 ) ),
        Smoother(
            X,
            Y,
            Legend( 12 ),
            Method( "P-Spline" ),
            Shape Constraint( "Non-descending" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Concentration", ScaleBox, {Scale( "Log" ), Minor Ticks( 1 )} )
    )
);
```

**Monotonic smoother trend line**

``` jsl
Open( "$SAMPLE_DATA/Penguins.jmp" );
// monotonic smooth trend line, p-spline, constraint
Graph Builder(
    Show Control Panel( 0 ),
    Include Missing Continuous Values( 0 ),
    Variables( X( :Culmen Length ), Y( :Culmen Depth ), Overlay( :Species ) ),
    Elements(
        Points( X, Y ),
        Smoother(
            X,
            Y,
            Method( "P-Spline" ),
            Lambda( 0.3 ),
            Shape Constraint( "Non-descending" )
        )
    )
);
```

**Smooth time series trend with split**

``` jsl
Open( "$SAMPLE_DATA/Time Series/Air.jmp" );
// Time series, split trend curve, grid lines
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :date ),
        Y( :Ozone Concentration ),
        Overlay( :Intervention for post 1960 period )
    ),
    Elements( Points( X, Y, Legend( 9 ) ), Smoother( X, Y, Legend( 10 ), Lambda( 1.4 ) ) ),
    SendToReport(
        Dispatch( {}, "date", ScaleBox, {Minor Ticks( 4 )} ),
        Dispatch( {}, "Ozone Concentration", ScaleBox, {Label Row( Show Major Grid( 1 ) )} )
    )
);
```

**Smooth trend and confidence interval**

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/Chemical Kinetics.jmp" );
// cubic spline smoother confidence interval
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Concentration ), Y( :"Velocity (y)"n ) ),
    Elements(
        Points( X, Y, Legend( 3 ) ),
        Smoother( X, Y, Legend( 4 ), Confidence of Fit( 1 ) )
    )
);
```

**Smooth trend curves, overlaid**

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/Algae Mitscherlich.jmp" );
// overlaid cubic spline trend lines
Graph Builder(
    Show Control Panel( 0 ),
    Legend Position( "Inside Left" ),
    Variables( X( :Days ), Y( :Algae density ), Overlay( :Treatment ) ),
    Elements( Points( X, Y, Legend( 9 ) ), Smoother( X, Y, Legend( 10 ) ) )
);
```

**Smooth trend curves, paneled**

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/Algae Mitscherlich.jmp" );
// paneled cubic spline trend lines
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables( X( :Days ), Y( :Algae density ), Wrap( :Treatment ) ),
    Elements( Points( X, Y, Legend( 9 ) ), Smoother( X, Y, Legend( 10 ) ) )
);
```

**Smooth trend curves, paneled and overlaid**

``` jsl
Open( "$SAMPLE_DATA/Corn Wheat Soybean Production.jmp" );
// smoothers paneled and filtered
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Year ),
        Y( :Commodity Acres Planted ),
        Group X( :State ),
        Overlay( :Commodity )
    ),
    Elements( Points( X, Y, Legend( 38 ) ), Smoother( X, Y, Legend( 39 ) ) ),
    Local Data Filter(
        Add Filter( columns( :State ), Where( :State == {"IOWA", "NEBRASKA", "OKLAHOMA"} ) )
    )
);
```

**Smooth trends lines over scatter plots**

``` jsl
Open( "$SAMPLE_DATA/Big Class.jmp" );
// smoothers and scatter plot, overlay, panels, trellis, trend curve, spline
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :height ), Y( :weight ), Wrap( :age ), Overlay( :sex ) ),
    Elements( Points( X, Y ), Smoother( X, Y, Lambda( 0.2 ) ) )
);
```

**Smoother comparison: loess, spline, p-spline**

``` jsl
Open( "$SAMPLE_DATA/Nonlinear Examples/Corn.jmp" );
// smoothers, loess, cubic spline, p-spline, monotonic, legend in bottom right
Graph Builder(
    Show Control Panel( 0 ),
    Legend Position( "Inside Bottom Right" ),
    Variables( X( :nitrate ), Y( :yield ) ),
    Elements(
        Points( X, Y, Legend( 3 ) ),
        Smoother(
            X,
            Y,
            Legend( 4 ),
            Method( "Local Kernel" ),
            Lambda( 0.5 ),
            Local Width( 0.687 ),
            Trim( 0 )
        ),
        Smoother( X, Y, Legend( 5 ), Lambda( 0.4 ) ),
        Smoother(
            X,
            Y,
            Legend( 6 ),
            Method( "P-Spline" ),
            Lambda( 2.0 ),
            Shape Constraint( "Non-descending" )
        )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {Legend Model( 4, Level Name( 0, "Loess" ) ),
            Legend Model( 5, Level Name( 0, "Spline" ) ),
            Legend Model( 6, Level Name( 0, "Monotonic p-spline" ) )}
        ),
        Dispatch( {}, "400", LegendBox,
            {Set Title( "" ), Legend Position( {3, [-1], 4, [0], 5, [1], 6, [2]} )}
        )
    )
);
```

### [Item Messages](#item-messages_17)[](#item-messages_17 "Click to copy url")

#### [Adapt to Axis Scale](#adapt-to-axis-scale_3)[](#adapt-to-axis-scale_3 "Click to copy url")

**Syntax:** obj \<\< Adapt to Axis Scale( state=0\|1 )

**Description:** For log and other axis transformations, apply computations on the transformed coordinates.

#### [Confidence Bootstrap](#confidence-bootstrap)[](#confidence-bootstrap "Click to copy url")

**Syntax:** obj \<\< Confidence Bootstrap( number )

**JMP Version Added:** 14

#### [Confidence of Fit](#confidence-of-fit_1)[](#confidence-of-fit_1 "Click to copy url")

**Syntax:** obj \<\< Confidence of Fit( state=0\|1 )

**Description:** Bootstrap confidence region for the fit.

**JMP Version Added:** 14

#### [Constrain Confidence Region](#constrain-confidence-region)[](#constrain-confidence-region "Click to copy url")

**Syntax:** obj \<\< Constrain Confidence Region( state=0\|1 )

**Description:** Whether the shape constraint also applies to the bootstrapped fits used to compute the confidence of fit region.

**JMP Version Added:** 19

#### [Degree](#degree_1)[](#degree_1 "Click to copy url")

**Syntax:** obj \<\< Degree( "Median"\|"Mean"\|"Linear"\|"Quadratic"\|"Cubic" )

**JMP Version Added:** 16

#### [Lambda](#lambda)[](#lambda "Click to copy url")

**Syntax:** obj \<\< Lambda( number )

#### [Local Constraint](#local-constraint)[](#local-constraint "Click to copy url")

**Syntax:** obj \<\< Local Constraint( state=0\|1 )

**Description:** Constrains the curve to the range of nearby values.

**JMP Version Added:** 19

#### [Local Region](#local-region)[](#local-region "Click to copy url")

**Syntax:** obj \<\< Local Region( "Power"\|"Fraction"\|"Fixed"\|"Trailing" )

**JMP Version Added:** 16

#### [Local Robustness](#local-robustness)[](#local-robustness "Click to copy url")

**Syntax:** obj \<\< Local Robustness( number )

**JMP Version Added:** 16

#### [Local Weighting](#local-weighting)[](#local-weighting "Click to copy url")

**Syntax:** obj \<\< Local Weighting( "Tri-cube"\|"Cosine"\|"Epanechnikov"\|"Gaussian"\|"Cauchy"\|"Laplace"\|"Triangular"\|"Rectangular" )

**JMP Version Added:** 16

#### [Local Width](#local-width)[](#local-width "Click to copy url")

**Syntax:** obj \<\< Local Width( number )

**JMP Version Added:** 16

#### [Maximum Constraint](#maximum-constraint)[](#maximum-constraint "Click to copy url")

**Syntax:** obj \<\< Maximum Constraint( number )

#### [Method](#method)[](#method "Click to copy url")

**Syntax:** obj \<\< Method( "Spline"\|"P-Spline"\|"Local Kernel"\|"Savitzky-Golay"\|"Moving Average"\|"Moving Box" )

**JMP Version Added:** 15

#### [Minimum Constraint](#minimum-constraint)[](#minimum-constraint "Click to copy url")

**Syntax:** obj \<\< Minimum Constraint( number )

#### [Response Axis](#response-axis_10)[](#response-axis_10 "Click to copy url")

**Syntax:** obj \<\< Response Axis( "Auto"\|"X"\|"Y" )

#### [Save Formula](#save-formula_1)[](#save-formula_1 "Click to copy url")

**Syntax:** obj \<\< Save Formula

#### [Scale lambda for count](#scale-lambda-for-count)[](#scale-lambda-for-count "Click to copy url")

**Syntax:** obj \<\< Scale lambda for count( state=0\|1 )

**Description:** Adjust the spline smoother parameter lambda to account for data size. Useful for consistent smoothing across groups of different sizes.

#### [Shape Constraint](#shape-constraint)[](#shape-constraint "Click to copy url")

**Syntax:** obj \<\< Shape Constraint( "None"\|"Non-descending"\|"Non-ascending"\|"Peak"\|"Valley"\|"Peak and Valley"\|"Flat Start"\|"Flat End"\|"Flat Start and End"\|"Cycle" )

**JMP Version Added:** 19

#### [Summary Statistic](#summary-statistic_8)[](#summary-statistic_8 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "None"\|"N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

#### [Trim](#trim)[](#trim "Click to copy url")

**Syntax:** obj \<\< Trim( number )

**JMP Version Added:** 16

## [Treemap Element](#treemap-element)[](#treemap-element "Click to copy url")

### [Associated Constructors](#associated-constructors_18)[](#associated-constructors_18 "Click to copy url")

#### [Treemap Element](#treemap-element_1)[](#treemap-element_1 "Click to copy url")

**Syntax:** Treemap Element

**Description:** Shows a response summarized by many categories.

**Continuous color gradient**

``` jsl
Open( "$SAMPLE_DATA/Airline Delays.jmp" );
// treemap, continuous color gradient
Graph Builder(
    Show Control Panel( 0 ),
    Variables( X( :Airline ), Color( :Arrival Delay ) ),
    Elements( Treemap( X, Legend( 5 ), Summary Statistic( "N" ) ) ),
    SendToReport(
        Dispatch( {}, "graph title", TextEditBox,
            {Set Text( "Airline Flight Count colored by Average Delay" )}
        )
    )
);
```

**Nested treemap, squarify**

``` jsl
Open( "$SAMPLE_DATA/Color Preference Survey.jmp" );
// nested treemap, squarify, color value column property
Graph Builder(
    Show Control Panel( 0 ),
    Show Legend( 0 ),
    Variables(
        X( :What is your gender? ),
        X( :"What is your favorite color? (select one)"n, Position( 1 ) ),
        X( :What is your favorite color?, Position( 1 ) ),
        Color( :"What is your favorite color? (select one)"n )
    ),
    Elements(
        Treemap(
            X( 1 ),
            X( 2 ),
            X( 3 ),
            Legend( 6 ),
            Layout( "Squarify" ),
            Group Labels( "Above" )
        )
    )
);
```

**Positional ordering hints**

``` jsl
Open( "$SAMPLE_DATA/SATByYear.jmp" );
// treemap, positional ordering hints
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :State ),
        Y( :Longitude ),
        Y( :Latitude, Position( 1 ) ),
        Color( :SAT Verbal ),
        Size( :Population )
    ),
    Elements( Treemap( X, Y( 1 ), Y( 2 ), Legend( 9 ) ) )
);
```

### [Item Messages](#item-messages_18)[](#item-messages_18 "Click to copy url")

#### [Category Name](#category-name)[](#category-name "Click to copy url")

**Syntax:** obj \<\< Category Name( state=0\|1 )

**Description:** Shows the column name of the category as part of the category label. This option is used only when the category value is also shown.

#### [Category Value](#category-value)[](#category-value "Click to copy url")

**Syntax:** obj \<\< Category Value( state=0\|1 )

**Description:** Shows the value of the category as part of the category label.

#### [Color Label Format](#color-label-format)[](#color-label-format "Click to copy url")

**Syntax:** obj \<\< Color Label Format

**JMP Version Added:** 16

#### [Color Name](#color-name)[](#color-name "Click to copy url")

**Syntax:** obj \<\< Color Name( state=0\|1 )

**Description:** Shows the name of the color variable as part of the color label. This option is used only when the color value is also shown.

**JMP Version Added:** 16

#### [Color Value](#color-value)[](#color-value "Click to copy url")

**Syntax:** obj \<\< Color Value( state=0\|1 )

**Description:** Shows the value of the color variable as part of the category label. This option is used only when a color variable is specified.

#### [Group Labels](#group-labels)[](#group-labels "Click to copy url")

**Syntax:** obj \<\< Group Labels( "None"\|"Above"\|"Floating" )

**Description:** Turn off the group labels or show the group labels above the categories or as floating boxes.

#### [Implicit Color](#implicit-color)[](#implicit-color "Click to copy url")

**Syntax:** obj \<\< Implicit Color( state=0\|1 )

**Description:** Use unique colors for the Treemap. Deselecting this option will show the Treemap as one solid color. This option is disabled if a color variable has been specified. On by default.

#### [Label Justification](#label-justification)[](#label-justification "Click to copy url")

**Syntax:** obj \<\< Label Justification( "Left"\|"Center"\|"Right" )

#### [Label Threshold](#label-threshold)[](#label-threshold "Click to copy url")

**Syntax:** obj \<\< Label Threshold( number )

**Description:** The minimum size (area) to display the label in the box.

#### [Label Transparency](#label-transparency)[](#label-transparency "Click to copy url")

**Syntax:** obj \<\< Label Transparency( number )

**Description:** Set the transparency for the group label when the group label is floating. Valid values are between 0.0 and 1.0 inclusive.

**JMP Version Added:** 16

#### [Layout](#layout)[](#layout "Click to copy url")

**Syntax:** obj \<\< Layout( "Split"\|"Squarify"\|"Mixed" )

#### [Max Label Size](#max-label-size_1)[](#max-label-size_1 "Click to copy url")

**Syntax:** obj \<\< Max Label Size( number )

**Description:** Defines the maximum increase in font size.

#### [Orientation Bias](#orientation-bias)[](#orientation-bias "Click to copy url")

**Syntax:** obj \<\< Orientation Bias( number )

**Description:** Set the relative preference of horizontal vs. vertical area splitting.

**JMP Version Added:** 17

#### [Show Frames](#show-frames)[](#show-frames "Click to copy url")

**Syntax:** obj \<\< Show Frames( state=0\|1 )

**Description:** On by default.

#### [Show Group Name](#show-group-name)[](#show-group-name "Click to copy url")

**Syntax:** obj \<\< Show Group Name( state=0\|1 )

**Description:** Shows the column name of the group as part of the group label. This option is used only when the group labels are above the group tiles.

#### [Size Label Format](#size-label-format)[](#size-label-format "Click to copy url")

**Syntax:** obj \<\< Size Label Format

**JMP Version Added:** 16

#### [Size Name](#size-name)[](#size-name "Click to copy url")

**Syntax:** obj \<\< Size Name( state=0\|1 )

**Description:** Shows the name of the size variable as part of the size label. This option is used only when the size value is also shown.

**JMP Version Added:** 16

#### [Size Value](#size-value)[](#size-value "Click to copy url")

**Syntax:** obj \<\< Size Value( state=0\|1 )

**Description:** Shows the value of the size variable as part of the category label.

#### [Summary Statistic](#summary-statistic_9)[](#summary-statistic_9 "Click to copy url")

**Syntax:** obj \<\< Summary Statistic( "N"\|"Mean"\|"Median"\|"Mode"\|"Geometric Mean"\|"Min"\|"Max"\|"Range"\|"Sum"\|"Cumulative Sum"\|"Cumulative Percent"\|"% of Total"\|"% of Factor"\|"% of Grand Total"\|"Std Dev"\|"Variance"\|"Std Err"\|"CV"\|"Interquartile Range"\|"Median Absolute Deviation"\|"First Quartile"\|"Third Quartile" )

#### [Tile Labels](#tile-labels)[](#tile-labels "Click to copy url")

**Syntax:** obj \<\< Tile Labels

[ Previous](Gaussian%20Process.html "Gaussian Process") [Next ](GridBox.html "GridBox")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
