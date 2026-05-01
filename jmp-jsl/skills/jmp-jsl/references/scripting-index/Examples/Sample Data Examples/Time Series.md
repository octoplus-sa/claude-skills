# Time Series

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Time%20Series.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Time%20Series.html)*

---

# [Time Series](#time-series)[](#time-series "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Fit a standard least squares regression model with multiple polynomial and interaction effects.](#fit-a-standard-least-squares-regression-model-with-multiple-polynomial-and-interaction-effects)[](#fit-a-standard-least-squares-regression-model-with-multiple-polynomial-and-interaction-effects "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Design Experiment/Custom RSM.jmp");
// Model
Fit Model(
    Y( :Y ),
    Effects(
        :X1 & RS, :X2 & RS, :X3 & RS,
        :X1 * :X1, :X1 * :X2, :X2 * :X2,
        :X1 * :X3, :X2 * :X3, :X3 * :X3
    ),
    Personality(
        "Standard Least Squares"
    )
);
```

### [Analyze and visualize the process history using the Process History Explorer tool, incorporating data from multiple tables by opening and linking relevant datasets.](#analyze-and-visualize-the-process-history-using-the-process-history-explorer-tool-incorporating-data-from-multiple-tables-by-opening-and-linking-relevant-datasets)[](#analyze-and-visualize-the-process-history-using-the-process-history-explorer-tool-incorporating-data-from-multiple-tables-by-opening-and-linking-relevant-datasets "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Lot Wafer History.jmp");
// Process History Explorer
Open(
    "$SAMPLE_DATA/Quality Control/Lot Wafer Yield.jmp"
);
Open(
    "$SAMPLE_DATA/Quality Control/Lot Wafer History.jmp"
) <<
Process History Explorer(
    ID( :Lot, :Wafer ),
    X( :Tool, :Route ),
    Step( :Layer, :Operation ),
    Timestamp( :TimeIn, :TimeOut ),
    Yield Table( "Lot Wafer Yield" ),
    Yield Columns( "Yield" ),
    Levels with Lowest Yield( 1 )
);
```

### [Forecast time series data by applying the Time Series Forecast function to the specified Y variable, grouped by the Series variable over the Time variable.](#forecast-time-series-data-by-applying-the-time-series-forecast-function-to-the-specified-y-variable-grouped-by-the-series-variable-over-the-time-variable)[](#forecast-time-series-data-by-applying-the-time-series-forecast-function-to-the-specified-y-variable-grouped-by-the-series-variable-over-the-time-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Time Series/M3C Quarterly.jmp");
// Time Series Forecast of Data
Time Series Forecast(
    Y( :Y ),
    Grouping( :Series ),
    Time( :Time )
);
```

### [Generate a Time Series Forecast for grouped quarterly data using the Time Series Forecast function with a 4-period ahead prediction and constrained parameters.](#generate-a-time-series-forecast-for-grouped-quarterly-data-using-the-time-series-forecast-function-with-a-4-period-ahead-prediction-and-constrained-parameters)[](#generate-a-time-series-forecast-for-grouped-quarterly-data-using-the-time-series-forecast-function-with-a-4-period-ahead-prediction-and-constrained-parameters "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Time Series/M3C Quarterly.jmp");
// Time Series Forecast of Data 2
Time Series Forecast(
    Y( :Y ),
    Grouping( :Series ),
    Time( :Time ),
    Fit Model(
        NAhead( 4 ),
        Period( 4 ),
        Constrain Parameters( 1 )
    )
);
```

### [Perform Time Series X11 decomposition of a dataset containing monthly sales data using the Date column as the time variable.](#perform-time-series-x11-decomposition-of-a-dataset-containing-monthly-sales-data-using-the-date-column-as-the-time-variable)[](#perform-time-series-x11-decomposition-of-a-dataset-containing-monthly-sales-data-using-the-date-column-as-the-time-variable "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Time Series/Monthly Sales.jmp");
// Time Series X11
Time Series(
    X( :Date ),
    Y( :Sales ),
    X11( Additive )
);
```

### [Detrend a time series dataset by removing both linear trend and seasonal cycle with a 12-month cycle.](#detrend-a-time-series-dataset-by-removing-both-linear-trend-and-seasonal-cycle-with-a-12-month-cycle)[](#detrend-a-time-series-dataset-by-removing-both-linear-trend-and-seasonal-cycle-with-a-12-month-cycle "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Time Series/Monthly Sales.jmp");
// Time Series Detrended
Time Series(
    X( :Date ),
    Y( :Sales ),
    Remove Linear Trend(
        Remove Cycle(
            Units per Cycle( 12 ),
            Has Constant( 0 )
        )
    )
);
```

### [Analyze time series data using variogram and seasonal ARIMA models with specified parameters.](#analyze-time-series-data-using-variogram-and-seasonal-arima-models-with-specified-parameters)[](#analyze-time-series-data-using-variogram-and-seasonal-arima-models-with-specified-parameters "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Time Series/Seriesg.jmp");
// Time Series
Time Series(
    Y( :Log Passengers ),
    Variogram( 1 ),
    Seasonal ARIMA(
        0,
        1,
        1,
        0,
        1,
        1,
        12,
        No Intercept( 1 )
    )
);
```

### [Compute the Spectral Density for a Time Series Analysis](#compute-the-spectral-density-for-a-time-series-analysis)[](#compute-the-spectral-density-for-a-time-series-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Wolfer Sunspot.jmp");
// Spectral Density
Time Series(
    Y( :wolfer ),
    Spectral Density( 1 )
);
```

### [Create a P chart to monitor the proportion of Total Plastic defects over time using the Control Chart Builder platform , with subgrouping by Week, phase variable by Location, and n Trials based on Total Volume.](#create-a-p-chart-to-monitor-the-proportion-of-total-plastic-defects-over-time-using-the-control-chart-builder-platform-with-subgrouping-by-week-phase-variable-by-location-and-n-trials-based-on-total-volume)[](#create-a-p-chart-to-monitor-the-proportion-of-total-plastic-defects-over-time-using-the-control-chart-builder-platform-with-subgrouping-by-week-phase-variable-by-location-and-n-trials-based-on-total-volume "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Water Plastics.jmp");
// P chart of Total Plastic
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
            Sigma( "Binomial" ),
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

[ Previous](Text%20Analysis.html "Text Analysis") [Next ](Visualization.html "Visualization")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
