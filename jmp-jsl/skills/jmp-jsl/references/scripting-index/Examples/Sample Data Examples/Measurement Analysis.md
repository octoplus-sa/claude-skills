# Measurement Analysis

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Measurement%20Analysis.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Measurement%20Analysis.html)*

---

# [Measurement Analysis](#measurement-analysis)[](#measurement-analysis "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Perform measurement systems analysis using the EMP procedure with crossed model and range chart for dispersion.](#perform-measurement-systems-analysis-using-the-emp-procedure-with-crossed-model-and-range-chart-for-dispersion)[](#perform-measurement-systems-analysis-using-the-emp-procedure-with-crossed-model-and-range-chart-for-dispersion "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Variability Data/2 Factors Crossed.jmp");
// EMP Measurement Systems Analysis
EMP Measurement Systems Analysis(
    Y( :Measurement ),
    X( :Operator ),
    Part( :part# ),
    Model( Crossed ),
    Dispersion Chart Type( "Range" ),
    Average Chart( 1 ),
    Dispersion Chart( 1 )
);
```

[ Previous](Graphical%20Analysis.html "Graphical Analysis") [Next ](Mixed%20Model.html "Mixed Model")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
