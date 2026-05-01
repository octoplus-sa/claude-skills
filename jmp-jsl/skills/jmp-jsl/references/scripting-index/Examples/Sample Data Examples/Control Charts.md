# Control Charts

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Control%20Charts.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Control%20Charts.html)*

---

# [Control Charts](#control-charts)[](#control-charts "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Build a rare event T control chart in the Control Chart Builder platform using Weibull limits for subgrouped data analysis.](#build-a-rare-event-t-control-chart-in-the-control-chart-builder-platform-using-weibull-limits-for-subgrouped-data-analysis)[](#build-a-rare-event-t-control-chart-in-the-control-chart-builder-platform-using-weibull-limits-for-subgrouped-data-analysis "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Fan Burnout.jmp");
// Control Chart Builder T Chart
Control Chart Builder(
    Class( "Rare Event" ),
    Variables(
        Subgroup( :Burnout ),
        Y( :Hours between Burnouts )
    ),
    Chart(
        Points( Statistic( "Count" ) ),
        Limits( Sigma( "Weibull" ) )
    )
);
```

[ Previous](Clustering.html "Clustering") [Next ](DOE.html "DOE")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
