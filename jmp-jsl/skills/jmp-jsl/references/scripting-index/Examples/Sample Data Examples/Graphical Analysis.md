# Graphical Analysis

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Graphical%20Analysis.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Graphical%20Analysis.html)*

---

# [Graphical Analysis](#graphical-analysis)[](#graphical-analysis "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Build a bar chart using graph builder](#build-a-bar-chart-using-graph-builder)[](#build-a-bar-chart-using-graph-builder "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Airline Delays.jmp");
// Graph Builder Bar
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Day of Week ),
        Overlay( :Airline )
    ),
    Elements(
        Bar(
            X,
            Legend( 2 ),
            Bar Style( "Side by side" ),
            Summary Statistic( "Mean" )
        )
    ),
    SendToReport(
        Dispatch( {}, "graph title",
            TextEditBox,
            {
            Set Text(
                "Flights by Airline and Day of Week"
            )}
        )
    )
);
```

### [Build a graph builder chart with a wrap variable](#build-a-graph-builder-chart-with-a-wrap-variable)[](#build-a-graph-builder-chart-with-a-wrap-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Arrhythmia.jmp");
// Graph Builder: QRS duration by Age
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Age ),
        Y( :QRS duration ),
        Wrap( :Sex )
    ),
    Elements(
        Smoother( X, Y, Legend( 34 ) ),
        Points( X, Y, Legend( 35 ) )
    ),
    SendToReport(
        Dispatch( {}, "Age", ScaleBox,
            {Min( -16 )}
        ),
        Dispatch( {}, "", ScaleBox,
            {
            Label Row(
                {Automatic Font Size( 1 ),
                Label Orientation(
                    "Automatic"
                ),
                Automatic Tick Marks( 1 )
                }
            )}
        ),
        Dispatch( {}, "", ScaleBox( 2 ),
            {
            Label Row(
                {Automatic Font Size( 1 ),
                Label Orientation(
                    "Automatic"
                ),
                Automatic Tick Marks( 1 )
                }
            )}
        )
    )
);
```

### [Build a graph builder chart with smoother curves](#build-a-graph-builder-chart-with-smoother-curves)[](#build-a-graph-builder-chart-with-smoother-curves "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Australian Tourism.jmp");
// Graph Builder Smoother 2
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Date ),
        Y( :"Revenue ($'000)"n ),
        Y(
            :Persons Employed,
            Position( 1 ),
            Side( "Right" )
        )
    ),
    Elements(
        Points( X, Y( 1 ), Legend( 1 ) ),
        Smoother(
            X,
            Y( 1 ),
            Legend( 4 )
        ),
        Points( X, Y( 2 ), Legend( 5 ) ),
        Smoother(
            X,
            Y( 2 ),
            Legend( 6 )
        )
    )
);
```

### [Build a graph builder chart with line and bar charts](#build-a-graph-builder-chart-with-line-and-bar-charts)[](#build-a-graph-builder-chart-with-line-and-bar-charts "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Big Class.jmp");
// Graph Builder Line and Bar Charts
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :age, Size( 15, 20 ) ),
        Y( :height, Size( 38, 36 ) ),
        Y( :weight )
    ),
    Elements(
        Position( 1, 1 ),
        Line(
            X,
            Y,
            Legend( 1 ),
            Row order( 0 ),
            Summary Statistic( "Mean" )
        )
    ),
    Elements(
        Position( 1, 2 ),
        Bar(
            X,
            Y,
            Legend( 2 ),
            Bar Style( "Side by side" ),
            Summary Statistic( "Mean" )
        )
    )
);
```

### [Generate a graph builder chart with points and lines and group on x, group on y and overlay](#generate-a-graph-builder-chart-with-points-and-lines-and-group-on-x-group-on-y-and-overlay)[](#generate-a-graph-builder-chart-with-points-and-lines-and-group-on-x-group-on-y-and-overlay "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cola Heart Rate.jmp");
// Graph Builder 3
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X(
            :"Time (Numeric)"n,
            Size( 0, 22 )
        ),
        Y( :Heart Rate, Size( 0, 23 ) ),
        Group X( :Brand ),
        Group Y( :Type ),
        Overlay( :Testers )
    ),
    Elements(
        Points( X, Y, Legend( 88 ) ),
        Line(
            X,
            Y,
            Legend( 90 ),
            Row order( 0 ),
            Summary Statistic( "Mean" )
        )
    )
);
```

### [Generate a bubble plot with automation on time and trail lines on selected](#generate-a-bubble-plot-with-automation-on-time-and-trail-lines-on-selected)[](#generate-a-bubble-plot-with-automation-on-time-and-trail-lines-on-selected "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cola Heart Rate.jmp");
// Bubble Plot 3
Bubble Plot(
    X( :"Time (Numeric)"n ),
    Y( :"Rate/Baseline"n ),
    Time( :"Time (Numeric)"n ),
    Coloring( :Gender ),
    ID( :Gender ),
    Trail Bubbles( 1 ),
    Trail Lines( 1 ),
    All Labels( 0 ),
    SendToReport(
        Dispatch( {}, "1", ScaleBox,
            {Min( 8.35671342685371 ),
            Max( 31.3445729133618 )}
        ),
        Dispatch( {}, "2", ScaleBox,
            {Min( 0.959042666666667 ),
            Max( 1.2742 ), Inc( 0.05 ),
            Minor Ticks( 1 )}
        )
    )
);
```

### [Perform response screening analysis to identify most significant categorical factors](#perform-response-screening-analysis-to-identify-most-significant-categorical-factors)[](#perform-response-screening-analysis-to-identify-most-significant-categorical-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Consumer Preferences.jmp");
// Response Screening
Response Screening(
    Y(
        :Job Satisfaction,
        :I am working on my career,
        :I want to see the world,
        :
        My home needs some major improvements,
        :
        I have vast interests outside of work,
        :
        I want to get my debt under control,
        :I come from a large family,
        :Brush, :Floss
    ),
    X(
        :Gender, :Single Status,
        :School Age Children, :Age Group
    ),
    Force X Categorical( 1 ),
    Force Y Categorical( 1 )
);
```

### [Generate a contour profiler plot for yield with Reaction Temperature and Reaction Time as factors.](#generate-a-contour-profiler-plot-for-yield-with-reaction-temperature-and-reaction-time-as-factors)[](#generate-a-contour-profiler-plot-for-yield-with-reaction-temperature-and-reaction-time-as-factors "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/First-Order Kinetics.jmp");
// Contour Profiler
Contour Profiler(
    Y( :Yield ),
    Contour Profiler(
        1,
        Term Value(
            Reaction Temperature(
                530.05
            ),
            Reaction Time(
                0.1995,
                Min( 0.101 )
            )
        ),
        Contour Value(
            Yield(
                0.596698113207547,
                Lo Limit(
                    0.596698113207547
                ),
                Min( 0.425 ),
                Max( 0.625 )
            )
        ),
        Horizontal Factor(
            Reaction Temperature
        ),
        Vertical Factor( Reaction Time )
    ),
    Expand
);
```

### [Generate a one-way analysis of variance (ANOVA) plot for the response variable Y divided by the categorical variable surface quality, and customize the plot with box plots, mean diamonds, and colored line segments for each surface quality category.](#generate-a-one-way-analysis-of-variance-anova-plot-for-the-response-variable-y-divided-by-the-categorical-variable-surface-quality-and-customize-the-plot-with-box-plots-mean-diamonds-and-colored-line-segments-for-each-surface-quality-category)[](#generate-a-one-way-analysis-of-variance-anova-plot-for-the-response-variable-y-divided-by-the-categorical-variable-surface-quality-and-customize-the-plot-with-box-plots-mean-diamonds-and-colored-line-segments-for-each-surface-quality-category "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// Oneway of Y by surface quality
Oneway(
    Y( :Y ),
    X( :surface quality ),
    All Pairs( 1 ),
    Means( 1 ),
    Plot Actual by Quantile( 1 ),
    Box Plots( 1 ),
    Mean Diamonds( 1 ),
    X Axis Proportional( 0 ),
    SendToReport(
        Dispatch( {}, "Oneway Plot",
            FrameBox,
            {
            DispatchSeg(
                Box Plot Seg( 1 ),
                {Confidence Diamond( 0 ),
                Line Color( "Red" )}
            ),
            DispatchSeg(
                Box Plot Seg( 2 ),
                {Confidence Diamond( 0 ),
                Line Color( "Red" )}
            ),
            DispatchSeg(
                Box Plot Seg( 3 ),
                {Confidence Diamond( 0 ),
                Line Color( "Red" )}
            ),
            DispatchSeg(
                Box Plot Seg( 4 ),
                {Confidence Diamond( 0 ),
                Line Color( "Red" )}
            )}
        )
    )
);
```

### [Construct a Variability Chart for analyzing the process variation in Comb MPG using the main factors Mfr Name and Engine, with options for robust analysis methods, box plots, and specific plot dimensions.](#construct-a-variability-chart-for-analyzing-the-process-variation-in-comb-mpg-using-the-main-factors-mfr-name-and-engine-with-options-for-robust-analysis-methods-box-plots-and-specific-plot-dimensions)[](#construct-a-variability-chart-for-analyzing-the-process-variation-in-comb-mpg-using-the-main-factors-mfr-name-and-engine-with-options-for-robust-analysis-methods-box-plots-and-specific-plot-dimensions "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hybrid Fuel Economy.jmp");
// Variability Chart
Variability Chart(
    Y( :Comb MPG ),
    X( :Mfr Name, :Engine ),
    Max Iter( 100 ),
    Conv Limit( 0.00000001 ),
    Number Integration Abscissas( 128 ),
    Number Function Evals( 65536 ),
    Analysis Type(
        "Choose best analysis (EMS REML Bayesian)"n
    ),
    Process Variation( 0 ),
    Std Dev Chart( 0 ),
    Show Box Plots( 1 ),
    SendToReport(
        Dispatch(
            {
            "Variability Chart for Comb MPG"
            }, "", NomAxisBox( 2 ),
            {Set Width( 539 ),
            Set Height( 161 )}
        )
    )
);
```

### [Prepare a variability chart to analyze shrinkage in investment castings, considering temperature and casting as factors using a nested model.](#prepare-a-variability-chart-to-analyze-shrinkage-in-investment-castings-considering-temperature-and-casting-as-factors-using-a-nested-model)[](#prepare-a-variability-chart-to-analyze-shrinkage-in-investment-castings-considering-temperature-and-casting-as-factors-using-a-nested-model "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Investment Castings.jmp");
// Variability Chart
Variability Chart(
    Y( :Shrinkage ),
    X( :Temperature, :Casting ),
    Model( "Nested" ),
    Max Iter( 100 ),
    Conv Limit( 0.00000001 ),
    Number Integration Abscissas( 128 ),
    Number Function Evals( 65536 ),
    Analysis Type(
        "Choose best analysis (EMS REML Bayesian)"n
    ),
    Process Variation( 0 ),
    Std Dev Chart( 1 ),
    Variance Components( 1 ),
    SendToReport(
        Dispatch( {},
            "Variability Chart for Shrinkage",
            OutlineBox,
            {Close( 1 )}
        )
    )
);
```

### [Generate a graph using the Graph Builder with color-coded map shapes representing the Change in Population and shaped differently based on the Metropolitan Statistical Area.](#generate-a-graph-using-the-graph-builder-with-color-coded-map-shapes-representing-the-change-in-population-and-shaped-differently-based-on-the-metropolitan-statistical-area)[](#generate-a-graph-using-the-graph-builder-with-color-coded-map-shapes-representing-the-change-in-population-and-shaped-differently-based-on-the-metropolitan-statistical-area "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/PopulationByMSA.jmp");
// Graph Builder
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        Color( :Change in Population ),
        Shape(
            :
            Metropolitan Statistical Area
        )
    ),
    Elements(
        Map Shapes(
            Legend( 2 ),
            Summary Statistic( "Mean" ),
            Show Missing Shapes( 0 )
        )
    ),
    SendToReport(
        Dispatch( {}, "", ScaleBox,
            {Min( -124.862821911553 ),
            Max( -67.2295339264016 ),
            Inc( 10 ), Minor Ticks( 0 )}
        ),
        Dispatch( {}, "", ScaleBox( 2 ),
            {Min( 14.572885454726 ),
            Max( 62.7291891822812 ),
            Inc( 10 ), Minor Ticks( 0 )}
        )
    )
);
:Metropolitan Statistical Area <<
Set Property(
    "Map Role",
    {
    Shape Name Use(
        "$SAMPLE_DATA/US-MSA-Name.jmp",
        "MSA_Name"
    )}
);
```

### [Create a side-by-side bar chart in Graph Builder to visualize the mean profit by product line and quarter from the Profit by Product dataset.](#create-a-side-by-side-bar-chart-in-graph-builder-to-visualize-the-mean-profit-by-product-line-and-quarter-from-the-profit-by-product-dataset)[](#create-a-side-by-side-bar-chart-in-graph-builder-to-visualize-the-mean-profit-by-product-line-and-quarter-from-the-profit-by-product-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Profit by Product.jmp");
// Graph Builder Bar Chart
Graph Builder(
    Size( 570, 481 ),
    Show Control Panel( 0 ),
    Variables(
        X( :Product Line ),
        Y( :Profit ),
        Group X( :Quarter )
    ),
    Elements(
        Bar(
            X,
            Y,
            Legend( 17 ),
            Bar Style( "Side by side" ),
            Summary Statistic( "Mean" )
        )
    ),
    SendToReport(
        Dispatch( {}, "Product Line",
            ScaleBox,
            {Show Major Ticks( 0 ),
            Show Minor Ticks( 0 ),
            Rotated Labels( "Automatic" )
            }
        )
    )
);
```

### [Generate a Laney P-prime control chart for the proportion of Total Plastic defects using the Water Plastics dataset.](#generate-a-laney-p-prime-control-chart-for-the-proportion-of-total-plastic-defects-using-the-water-plastics-dataset)[](#generate-a-laney-p-prime-control-chart-for-the-proportion-of-total-plastic-defects-using-the-water-plastics-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Water Plastics.jmp");
// Laney P' chart of Total Plastic
Control Chart Builder(
    Size( 814, 307 ),
    Show Two Shewhart Charts( 0 ),
    Show Control Panel( 0 ),
    Show Limit Summaries( 0 ),
    Class( Shewhart Attribute ),
    Variables(
        Subgroup( :Week ),
        Y( :Total Plastic ),
        Phase( :Location ),
        n Trials( :Total Volume )
    ),
    Chart(
        Points(
            Statistic( "Proportion" )
        ),
        Limits(
            Sigma( "Laney P Prime" ),
            Show Lower Limit( 0 )
        )
    ),
    SendToReport(
        Dispatch( {},
            "Control Chart Builder",
            FrameBox,
            {
            DispatchSeg(
                Text Seg( 1 ),
                {Line Color( "None" ),
                Fill Color( "None" )}
            ),
            DispatchSeg(
                Text Seg( 2 ),
                {Line Color( "None" ),
                Fill Color( "None" )}
            ),
            DispatchSeg(
                Text Seg( 3 ),
                {Line Color( "None" ),
                Fill Color( "None" )}
            )}
        )
    )
);
```

### [Create a bar chart using Graph Builder to visualize the mean expenditures across different ethnicities, specifically focusing on Hispanic and White non-Hispanic groups. Apply a local data filter to include only these two ethnicities in the analysis.](#create-a-bar-chart-using-graph-builder-to-visualize-the-mean-expenditures-across-different-ethnicities-specifically-focusing-on-hispanic-and-white-non-hispanic-groups-apply-a-local-data-filter-to-include-only-these-two-ethnicities-in-the-analysis)[](#create-a-bar-chart-using-graph-builder-to-visualize-the-mean-expenditures-across-different-ethnicities-specifically-focusing-on-hispanic-and-white-non-hispanic-groups-apply-a-local-data-filter-to-include-only-these-two-ethnicities-in-the-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Simpsons Paradox.jmp");
// Graph Builder: Mean (Expenditures) vs. Ethnicity
Graph Builder(
    Size( 534, 450 ),
    Show Control Panel( 0 ),
    Variables(
        X( :Ethnicity ),
        Y( :Expenditures )
    ),
    Elements( Bar( X, Y, Legend( 4 ) ) ),
    Local Data Filter(
        Close Outline( 1 ),
        Add Filter(
            columns( :Ethnicity ),
            Where(
                :Ethnicity == {"Hispanic",
                "White not Hispanic"}
            ),
            Display(
                :Ethnicity,
                N Items( 8 )
            )
        )
    )
);
```

### [Generate a Contour Profiler for the Yield response variable utilizing Reaction Temperature and Reaction Time factors from the Stochastic Optimization dataset.](#generate-a-contour-profiler-for-the-yield-response-variable-utilizing-reaction-temperature-and-reaction-time-factors-from-the-stochastic-optimization-dataset)[](#generate-a-contour-profiler-for-the-yield-response-variable-utilizing-reaction-temperature-and-reaction-time-factors-from-the-stochastic-optimization-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Stochastic Optimization.jmp");
// Contour Profiler
Contour Profiler(
    Y( :Yield ),
    Contour Profiler(
        1,
        Term Value(
            Reaction Temperature(
                530.05
            ),
            Reaction Time(
                0.1995,
                Min( 0.101 )
            )
        ),
        Contour Value(
            Yield(
                0.596698113207547,
                Lo Limit(
                    0.596698113207547
                ),
                Min( 0.425 ),
                Max( 0.625 )
            )
        ),
        Horizontal Factor(
            Reaction Temperature
        ),
        Vertical Factor( Reaction Time )
    ),
    Expand
);
```

### [Create a Graph Builder overlay plot displaying high and low stock prices over time with major grid lines on the x-axis and horizontally oriented, left-aligned legend.](#create-a-graph-builder-overlay-plot-displaying-high-and-low-stock-prices-over-time-with-major-grid-lines-on-the-x-axis-and-horizontally-oriented-left-aligned-legend)[](#create-a-graph-builder-overlay-plot-displaying-high-and-low-stock-prices-over-time-with-major-grid-lines-on-the-x-axis-and-horizontally-oriented-left-aligned-legend "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Stock Averages.jmp");
// Graph Builder Overlay Plot
Graph Builder(
    Size( 568, 407 ),
    Show Control Panel( 0 ),
    Legend Position( "Bottom" ),
    Variables(
        X( :Date ),
        Y( :High ),
        Y( :Low, Position( 1 ) )
    ),
    Elements(
        Points(
            X,
            Y( 1 ),
            Y( 2 ),
            Legend( 1 )
        )
    ),
    SendToReport(
        Dispatch( {}, "Date", ScaleBox,
            {
            Label Row(
                Show Major Grid( 1 )
            )}
        ),
        Dispatch( {}, "Graph Builder",
            FrameBox,
            {Marker Size( 2 )}
        ),
        Dispatch( {}, "400", LegendBox,
            {Orientation( "Horizontal" ),
            Sides( "Left" )}
        )
    )
);
```

### [Create a bar chart using Graph Builder with three Y-axes (High, Low, and Close) over the X-axis (YearWeek) from the TechStock dataset.](#create-a-bar-chart-using-graph-builder-with-three-y-axes-high-low-and-close-over-the-x-axis-yearweek-from-the-techstock-dataset)[](#create-a-bar-chart-using-graph-builder-with-three-y-axes-high-low-and-close-over-the-x-axis-yearweek-from-the-techstock-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/TechStock.jmp");
// Graph Builder 3
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :YearWeek ),
        Y( :High ),
        Y( :Low, Position( 1 ) ),
        Y( :Close, Position( 1 ) )
    ),
    Elements(
        Bar(
            X,
            Y( 1 ),
            Y( 2 ),
            Y( 3 ),
            Legend( 1 ),
            Bar Style( "Interval" )
        )
    )
);
```

### [Create a Graph Builder plot with departure day of week as a categorical variable, net cost as the response variable, grouped by class of service, and overlaid by airline, using points with jitter.](#create-a-graph-builder-plot-with-departure-day-of-week-as-a-categorical-variable-net-cost-as-the-response-variable-grouped-by-class-of-service-and-overlaid-by-airline-using-points-with-jitter)[](#create-a-graph-builder-plot-with-departure-day-of-week-as-a-categorical-variable-net-cost-as-the-response-variable-grouped-by-class-of-service-and-overlaid-by-airline-using-points-with-jitter "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Travel Costs.jmp");
// Graph Builder - Root Cause
Graph Builder(
    Variables(
        X( :Net Cost ),
        Y(
            :Departure Day of Week,
            Size( 74 )
        ),
        Group Y( :Class of Service ),
        Overlay( :Airline )
    ),
    Elements(
        Points(
            X,
            Y,
            Legend( 6 ),
            Jitter( 1 )
        )
    )
);
```

### [Create a Graph Builder Map displaying 2008 Election State Winners, where map shapes are sized based on the number of electors using the Color, Size, and Shape variables, and adjust the legend and graph title accordingly.](#create-a-graph-builder-map-displaying-2008-election-state-winners-where-map-shapes-are-sized-based-on-the-number-of-electors-using-the-color-size-and-shape-variables-and-adjust-the-legend-and-graph-title-accordingly)[](#create-a-graph-builder-map-displaying-2008-election-state-winners-where-map-shapes-are-sized-based-on-the-number-of-electors-using-the-color-size-and-shape-variables-and-adjust-the-legend-and-graph-title-accordingly "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/US Election 2008.jmp");
// Graph Builder Map Sized by Number of Electors
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        Color( :Winner ),
        Size( :Electors ),
        Shape( :State )
    ),
    Elements(
        Map Shapes(
            Legend( 2 ),
            Summary Statistic( "Mean" ),
            Show Missing Shapes( 0 )
        )
    ),
    SendToReport(
        Dispatch( {}, "400", ScaleBox,
            {
            Legend Model(
                2,
                Properties(
                    0,
                    {Line Color( 1 )}
                )
            )}
        ),
        Dispatch( {}, "graph title",
            TextEditBox,
            {
            Set Text(
                "2008 Election State Winners sized by Number of Electors"
            )}
        )
    )
);
```

### [Create line and bar charts using the Graph Builder platform .](#create-line-and-bar-charts-using-the-graph-builder-platform)[](#create-line-and-bar-charts-using-the-graph-builder-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/World Class.jmp");
// Graph Builder Line and Bar Charts
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :age, Size( 15, 20 ) ),
        Y(
            :"height (in.)"n,
            Size( 38, 36 )
        ),
        Y( :"weight (lb.)"n )
    ),
    Elements(
        Position( 1, 1 ),
        Line(
            X,
            Y,
            Legend( 1 ),
            Row order( 0 ),
            Summary Statistic( "Mean" )
        )
    ),
    Elements(
        Position( 1, 2 ),
        Bar(
            X,
            Y,
            Legend( 2 ),
            Bar Style( "Side by side" ),
            Summary Statistic( "Mean" )
        )
    )
);
```

### [Build a contour plot using graph builder](#build-a-contour-plot-using-graph-builder)[](#build-a-contour-plot-using-graph-builder "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Airline Delays.jmp");
// Graph Builder Contour Plot
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Distance ),
        Y( :Arrival Delay ),
        Wrap( :Airline )
    ),
    Elements(
        Contour(
            X,
            Y,
            Legend( 6 ),
            Number of Levels( 6 )
        )
    )
);
```

### [Fit a standard least squares model](#fit-a-standard-least-squares-model)[](#fit-a-standard-least-squares-model "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Analgesics.jmp");
// Fit Model
Fit Model(
    Y( :pain ),
    Effects(
        :gender, :drug, :gender * :drug
    ),
    Personality(
        "Standard Least Squares"
    ),
    Run(
        :pain <<
        {Plot Actual by Predicted( 1 ),
        Plot Residual by Predicted( 1 ),
        Plot Effect Leverage( 1 )}
    )
);
```

### [Perform bivariate analysis with a second order polynomial fit](#perform-bivariate-analysis-with-a-second-order-polynomial-fit)[](#perform-bivariate-analysis-with-a-second-order-polynomial-fit "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Birth Death.jmp");
// Bivariate
Bivariate(
    Y( :death ),
    X( :birth ),
    Fit Polynomial( 2 )
);
```

### [Generate a bubble plot with automation by year](#generate-a-bubble-plot-with-automation-by-year)[](#generate-a-bubble-plot-with-automation-by-year "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/BirthDeathYear.jmp");
// Bubble Plot
Bubble Plot(
    X( :Birth ),
    Y( :Death ),
    Time( :Year ),
    ID( :Country ),
    Circle Size( 0.339622641509434 ),
    Time Index( 4.1 )
);
```

### [Generate distribution analysis](#generate-distribution-analysis)[](#generate-distribution-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cleansing.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :Coal particles )
    ),
    Continuous Distribution(
        Column( :pH )
    ),
    Nominal Distribution(
        Column( :Polymer )
    )
);
```

### [Fit a standard least squares model with 2 way interaction term](#fit-a-standard-least-squares-model-with-2-way-interaction-term)[](#fit-a-standard-least-squares-model-with-2-way-interaction-term "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cleansing.jmp");
// Model Specification
Fit Model(
    Y( :Coal particles ),
    Effects(
        :pH, :Polymer, :pH * :Polymer
    ),
    Personality(
        "Standard Least Squares"
    )
);
```

### [Generate a 3d scatterplot](#generate-a-3d-scatterplot)[](#generate-a-3d-scatterplot "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cowboy Hat Template.jmp");
// Scatterplot 3D
Scatterplot 3D( Y( :x, :y, :z ) );
```

### [Generate a 3d scatterplot](#generate-a-3d-scatterplot_1)[](#generate-a-3d-scatterplot_1 "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Cowboy Hat.jmp");
// Scatterplot 3D
Scatterplot 3D( Y( :x, :y, :z ) );
```

### [Generate overlay plots for weibull with data plotted as a function](#generate-overlay-plots-for-weibull-with-data-plotted-as-a-function)[](#generate-overlay-plots-for-weibull-with-data-plotted-as-a-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Density Compare.jmp");
// Overlay Plot for Weibulls
Overlay Plot(
    X( :XWeibull ),
    Y( :Weibull11, :Weibul12, :Weibul21 ),
    Function Plot( 1 ),
    Show Points( 0 )
);
```

### [Perform screening analysis to identify significant factors affecting taste in a cake experiment using the Screening function.](#perform-screening-analysis-to-identify-significant-factors-affecting-taste-in-a-cake-experiment-using-the-screening-function)[](#perform-screening-analysis-to-identify-significant-factors-affecting-taste-in-a-cake-experiment-using-the-screening-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Cake Data.jmp");
// Screening
Screening(
    Y( :Taste ),
    X(
        :Cocoa, :Sugar, :Flour, :Butter,
        :Milk, :Eggs
    )
);
```

### [Open the Bounce Response data table and load it into the Custom Design platform for response editing.](#open-the-bounce-response-data-table-and-load-it-into-the-custom-design-platform-for-response-editing)[](#open-the-bounce-response-data-table-and-load-it-into-the-custom-design-platform-for-response-editing "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Bounce Response.jmp");
// Load and Edit in Custom Design
DOE(
    Custom Design,
    Load Responses(
        Current Data Table()
    )
);
```

### [Build a statistical model using the Fit Model function with specified effects and response variable.](#build-a-statistical-model-using-the-fit-model-function-with-specified-effects-and-response-variable)[](#build-a-statistical-model-using-the-fit-model-function-with-specified-effects-and-response-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Coffee Data.jmp");
// Model
Fit Model(
    Effects(
        :Grind, :Temperature, :Time,
        :Charge, :Station
    ),
    Y( :Strength )
);
```

### [Generate a ternary plot with the variables CuSO4, Na2S2O3, and Glyoxal.](#generate-a-ternary-plot-with-the-variables-cuso4-na2s2o3-and-glyoxal)[](#generate-a-ternary-plot-with-the-variables-cuso4-na2s2o3-and-glyoxal "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Donev Mixture Data.jmp");
// Ternary Plot
obj =
Ternary Plot(
    Y( :CuSO4, :Na2S2O3, :Glyoxal )
);
Report( obj )[framebox( 1 )] <<
Marker Size( 4 );
```

### [Analyze distributions for Miles, Weight, and Strike Point using the Distribution platform, focusing on continuous and nominal variables.](#analyze-distributions-for-miles-weight-and-strike-point-using-the-distribution-platform-focusing-on-continuous-and-nominal-variables)[](#analyze-distributions-for-miles-weight-and-strike-point-using-the-distribution-platform-focusing-on-continuous-and-nominal-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Runners Covariates.jmp");
// Distribution
Distribution(
    Continuous Distribution(
        Column( :Miles )
    ),
    Continuous Distribution(
        Column( :Weight )
    ),
    Nominal Distribution(
        Column( :Strike Point )
    ),
    Histograms Only
);
```

### [Create a Graph Builder plot with colored points, a line of fit, and the specified variables: Specific Gravity, Tensile Strength, and Supplier.](#create-a-graph-builder-plot-with-colored-points-a-line-of-fit-and-the-specified-variables-specific-gravity-tensile-strength-and-supplier)[](#create-a-graph-builder-plot-with-colored-points-a-line-of-fit-and-the-specified-variables-specific-gravity-tensile-strength-and-supplier "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Thermoplastic.jmp");
// Graph Builder
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :Specific Gravity ),
        Y( :Tensile Strength ),
        Color( :Supplier )
    ),
    Elements(
        Points( X, Y, Legend( 2 ) ),
        Line Of Fit( X, Y, Legend( 4 ) )
    )
);
```

### [Perform a one-way analysis of variance (ANOVA) to compare the means of the Toxicity response variable across different levels of the Formulation factor, visualize the results with mean diamonds and robust means lines.](#perform-a-one-way-analysis-of-variance-anova-to-compare-the-means-of-the-toxicity-response-variable-across-different-levels-of-the-formulation-factor-visualize-the-results-with-mean-diamonds-and-robust-means-lines)[](#perform-a-one-way-analysis-of-variance-anova-to-compare-the-means-of-the-toxicity-response-variable-across-different-levels-of-the-formulation-factor-visualize-the-results-with-mean-diamonds-and-robust-means-lines "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Drug Toxicity.jmp");
// Oneway
Oneway(
    Y( :Toxicity ),
    X( :Formulation ),
    "Means/Anova"n( 1 ),
    Mean Diamonds( 1 ),
    Robust Means Lines( 1 )
);
```

### [Perform stepwise linear regression analysis on the Fitness data table to identify significant predictors of Oxygen consumption.](#perform-stepwise-linear-regression-analysis-on-the-fitness-data-table-to-identify-significant-predictors-of-oxygen-consumption)[](#perform-stepwise-linear-regression-analysis-on-the-fitness-data-table-to-identify-significant-predictors-of-oxygen-consumption "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Fitness.jmp");
// Stepwise Fit
Fit Model(
    Y( :Oxy ),
    Effects(
        :Runtime, :Weight, :RunPulse,
        :RstPulse, :MaxPulse
    ),
    Personality( "Stepwise" ),
    Run
);
```

### [Create a Graph Builder visualization to explore relationships between lots, parts, and shipping events.](#create-a-graph-builder-visualization-to-explore-relationships-between-lots-parts-and-shipping-events)[](#create-a-graph-builder-visualization-to-explore-relationships-between-lots-parts-and-shipping-events "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// lots, parts, and shipping
Graph Builder(
    Size( 515, 491 ),
    Show Control Panel( 0 ),
    Variables(
        X( :Part ),
        Y( :Lot ),
        Group X( :Ship event )
    ),
    Elements(
        Points( X, Y, Legend( 8 ) )
    )
);
```

### [Open a data table and configure the Graph Builder to visualize surface quality, part, and ship event using a wrap layout with point elements.](#open-a-data-table-and-configure-the-graph-builder-to-visualize-surface-quality-part-and-ship-event-using-a-wrap-layout-with-point-elements)[](#open-a-data-table-and-configure-the-graph-builder-to-visualize-surface-quality-part-and-ship-event-using-a-wrap-layout-with-point-elements "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// Graph Builder 3
Graph Builder(
    Size( 569, 500 ),
    Variables(
        X( :surface quality ),
        Y( :Part ),
        Wrap( :Ship event )
    ),
    Elements(
        Points( X, Y, Legend( 7 ) )
    )
);
```

### [Generate a Pareto plot to analyze the dependency of surface quality on different parts, excluding the rate plots and closing the plot outline.](#generate-a-pareto-plot-to-analyze-the-dependency-of-surface-quality-on-different-parts-excluding-the-rate-plots-and-closing-the-plot-outline)[](#generate-a-pareto-plot-to-analyze-the-dependency-of-surface-quality-on-different-parts-excluding-the-rate-plots-and-closing-the-plot-outline "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Hardware Surface Unit Data.jmp");
// Pareto Plot 4
Pareto Plot(
    Cause( :surface quality ),
    X( :Part ),
    Test Rates Across Groups( 1 ),
    No Plot( 1 ),
    SendToReport(
        Dispatch( {}, "Plots", OutlineBox,
            {Close( 1 )}
        )
    )
);
```

### [Create a 3D scatterplot showing the relationship between sepal and petal dimensions in the Iris dataset.](#create-a-3d-scatterplot-showing-the-relationship-between-sepal-and-petal-dimensions-in-the-iris-dataset)[](#create-a-3d-scatterplot-showing-the-relationship-between-sepal-and-petal-dimensions-in-the-iris-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Iris.jmp");
// Scatterplot 3D
Scatterplot 3D(
    Y(
        :Sepal length, :Sepal width,
        :Petal length, :Petal width
    ),
    Frame3D(
        Set Rotation(
            -37.7763571468042,
            -20.0181349932962,
            0.755666043084993
        )
    )
);
```

### [Fit a nominal logistic regression model using the occurrence of lung cancer as the response variable, with smoking as the predictor, and incorporating observation frequencies.](#fit-a-nominal-logistic-regression-model-using-the-occurrence-of-lung-cancer-as-the-response-variable-with-smoking-as-the-predictor-and-incorporating-observation-frequencies)[](#fit-a-nominal-logistic-regression-model-using-the-occurrence-of-lung-cancer-as-the-response-variable-with-smoking-as-the-predictor-and-incorporating-observation-frequencies "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Lung Cancer.jmp");
// Model
Fit Model(
    Freq( :Count ),
    Y( :Lung Cancer ),
    Effects( :Smoker ),
    Personality( "Nominal Logistic" )
);
```

### [Fit a logistic regression model with a response variable of interest and a predictor variable, including a frequency column.](#fit-a-logistic-regression-model-with-a-response-variable-of-interest-and-a-predictor-variable-including-a-frequency-column)[](#fit-a-logistic-regression-model-with-a-response-variable-of-interest-and-a-predictor-variable-including-a-frequency-column "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Penicillin.jmp");
// Logistic
Logistic(
    Y( Response ),
    X( "ln(dose)"n ),
    Freq( count )
);
```

### [Create a ternary plot using the specified variables.](#create-a-ternary-plot-using-the-specified-variables)[](#create-a-ternary-plot-using-the-specified-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Plasticizer 78.jmp");
// Ternary Plot
Ternary Plot( Y( :p1, :p2, :p3 ) );
```

### [Create a CUSUM Control Chart for quality control monitoring using a predefined data table.](#create-a-cusum-control-chart-for-quality-control-monitoring-using-a-predefined-data-table)[](#create-a-cusum-control-chart-for-quality-control-monitoring-using-a-predefined-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Engine Temperature Sensor.jmp");
// CUSUM Control Chart
CUSUM Control Chart(
    Y( :Y ),
    Lower Side( 1 ),
    Target( 100 ),
    Sigma( 10 )
);
```

### [Generate a cell plot to visualize the performance of verbal and math scores across different years for each state.](#generate-a-cell-plot-to-visualize-the-performance-of-verbal-and-math-scores-across-different-years-for-each-state)[](#generate-a-cell-plot-to-visualize-the-performance-of-verbal-and-math-scores-across-different-years-for-each-state "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/SAT.jmp");
// Cell Plot
Cell Plot(
    Y(
        :"2004 Verbal"n, :"2004 Math"n,
        :"2003 Verbal"n, :"2003 Math"n,
        :"2002 Verbal"n, :"2002 Math"n,
        :"2001 Verbal"n, :"2001 Math"n,
        :"1999 Verbal"n, :"1999 Math"n,
        :"1994 Verbal"n, :"1994 Math"n,
        :"1997 Verbal"n, :"1997 Math"n,
        :"1992 Verbal"n, :"1992 Math"n
    ),
    Label( :State )
);
```

### [Generate a Treemap visualization to analyze the relationships and distributions of verbal scores, test-taking percentages, and geographic locations (states) based on the SAT dataset.](#generate-a-treemap-visualization-to-analyze-the-relationships-and-distributions-of-verbal-scores-test-taking-percentages-and-geographic-locations-states-based-on-the-sat-dataset)[](#generate-a-treemap-visualization-to-analyze-the-relationships-and-distributions-of-verbal-scores-test-taking-percentages-and-geographic-locations-states-based-on-the-sat-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/SAT.jmp");
// Treemap
Treemap(
    Categories( :State ),
    Coloring( :"2004 Verbal"n ),
    Sizes( :"% Taking (2004)"n ),
    Ordering( :X, :Y )
);
```

### [Fit a standard least squares model with minimal report and significance level set to 0.05 using the variables X1, X2, and X3 to predict Y.](#fit-a-standard-least-squares-model-with-minimal-report-and-significance-level-set-to-005-using-the-variables-x1-x2-and-x3-to-predict-y)[](#fit-a-standard-least-squares-model-with-minimal-report-and-significance-level-set-to-005-using-the-variables-x1-x2-and-x3-to-predict-y "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Singularity.jmp");
// Model 1
Fit Model(
    Censor Code( "" ),
    Y( :Y ),
    Effects( :X1, :X2, :X3 ),
    Personality(
        "Standard Least Squares"
    ),
    Emphasis( "Minimal Report" ),
    Set Alpha Level( 0.05 )
);
```

### [Generate a distribution analysis for multiple chemical solubility variables.](#generate-a-distribution-analysis-for-multiple-chemical-solubility-variables)[](#generate-a-distribution-analysis-for-multiple-chemical-solubility-variables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Solubility.jmp");
// Distribution
Distribution(
    Y(
        :Ether, :"1-Octanol"n,
        :Carbon Tetrachloride, :Benzene,
        :Hexane, :Chloroform
    )
);
```

### [Fit a linear model using the EMS method with interactions and random effects.](#fit-a-linear-model-using-the-ems-method-with-interactions-and-random-effects)[](#fit-a-linear-model-using-the-ems-method-with-interactions-and-random-effects "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Split Plot.jmp");
// Fit Model - EMS Method
Fit Model(
    Y( :Y ),
    Effects(
        :Tenderizer, :Carcass,
        :Tenderizer * :Carcass & Random,
        :Roasting Time,
        :Roasting Time * :Tenderizer
    ),
    Personality(
        "Standard Least Squares"
    ),
    Method( "EMS" ),
    Run
);
```

### [Create a Graph Builder Bar Chart with two Y variables from a data table.](#create-a-graph-builder-bar-chart-with-two-y-variables-from-a-data-table)[](#create-a-graph-builder-bar-chart-with-two-y-variables-from-a-data-table "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Spring.jmp");
// Graph Builder Bar Chart
Graph Builder(
    Show Control Panel( 0 ),
    Variables(
        X( :date ),
        Y( :"Humid1:PM"n ),
        Y( :"Humid4:PM"n, Position( 1 ) )
    ),
    Elements(
        Bar(
            X,
            Y( 1 ),
            Y( 2 ),
            Legend( 1 )
        )
    )
);
```

### [Create a surface plot visualizing the relationship between reaction temperature, reaction time, and yield.](#create-a-surface-plot-visualizing-the-relationship-between-reaction-temperature-reaction-time-and-yield)[](#create-a-surface-plot-visualizing-the-relationship-between-reaction-temperature-reaction-time-and-yield "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Stochastic Optimization.jmp");
// Surface Plot
Surface Plot(
    Columns( :Yield ),
    Control Panel( 0 ),
    Hide Lights Border( 1 ),
    Scale response axes independently(
        1
    ),
    Datapoints Choice( "Points" ),
    XRotate( -67.3776687507792 ),
    YRotate( -5.03482899952444 ),
    ZRotate( 52.4071239021159 ),
    Formula( "Yield" ),
    Response( :Yield ),
    SetXVariable( Reaction Temperature ),
    SetYVariable( Reaction Time ),
    Graph( Background Color( 0, 0, 0 ) ),
    Graph Size( 443, 443 )
);
```

### [Create a scatter plot of Net Costs using the Graph Builder function .](#create-a-scatter-plot-of-net-costs-using-the-graph-builder-function)[](#create-a-scatter-plot-of-net-costs-using-the-graph-builder-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Travel Costs.jmp");
// Graph Builder - Net Costs
Graph Builder(
    Variables( X( :Net Cost ) ),
    Elements(
        Points(
            X,
            Legend( 3 ),
            Jitter( 1 )
        )
    )
);
```

### [Create a variability chart with nested factors using operator and part configurations and display standard deviation charts.](#create-a-variability-chart-with-nested-factors-using-operator-and-part-configurations-and-display-standard-deviation-charts)[](#create-a-variability-chart-with-nested-factors-using-operator-and-part-configurations-and-display-standard-deviation-charts "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Variability Data/2 Factors Nested.jmp");
// Variability Chart - Nested
Variability Chart(
    Y( :" Y"n ),
    X( :Operator, :Part ),
    Variance Components( "Nested" ),
    Show Points( 1 ),
    Std Dev Chart( 1 )
);
```

### [Create a bubble plot with scaling for sizes and coloring based on the wolfer variable using Bubble Plot function.](#create-a-bubble-plot-with-scaling-for-sizes-and-coloring-based-on-the-wolfer-variable-using-bubble-plot-function)[](#create-a-bubble-plot-with-scaling-for-sizes-and-coloring-based-on-the-wolfer-variable-using-bubble-plot-function "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Wolfer Sunspot.jmp");
// Bubble Plot
Bubble Plot(
    X( :part ),
    Y( :cycle ),
    Sizes( :wolfer ),
    Coloring( :wolfer ),
    Circle Size( 5.9433962264151 ),
    SendToReport(
        Dispatch( {}, "2", ScaleBox,
            {Scale( "Linear" ),
            Format( "Best" ), Min( 1740 ),
            Max( 1920 ), Inc( 10 )}
        ),
        Dispatch( {}, "Bubble Plot",
            FrameBox,
            Frame Size( 482, 353 )
        )
    )
);
```

### [Create an overlay plot with needle plots for the high, close, and low stock prices of DJI over time.](#create-an-overlay-plot-with-needle-plots-for-the-high-close-and-low-stock-prices-of-dji-over-time)[](#create-an-overlay-plot-with-needle-plots-for-the-high-close-and-low-stock-prices-of-dji-over-time "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/XYZ Stock Averages (plots).jmp");
// Overlay Plot: Needle
Overlay Plot(
    X( :Date ),
    Y( :DJI High, :DJI Close, :DJI Low ),
    Needle( 1 )
);
```

[ Previous](Fit%20Model.html "Fit Model") [Next ](Measurement%20Analysis.html "Measurement Analysis")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
