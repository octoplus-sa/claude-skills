# Other Analysis

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Other%20Analysis.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Other%20Analysis.html)*

---

# [Other Analysis](#other-analysis)[](#other-analysis "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Perform a screening analysis to identify significant factors affecting log life in the Weld-Repaired Castings dataset using the Screening platform.](#perform-a-screening-analysis-to-identify-significant-factors-affecting-log-life-in-the-weld-repaired-castings-dataset-using-the-screening-platform)[](#perform-a-screening-analysis-to-identify-significant-factors-affecting-log-life-in-the-weld-repaired-castings-dataset-using-the-screening-platform "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Weld-Repaired Castings.jmp");
// Screening
Screening(
    Y( :"Log Life (×100)"n ),
    X(
        :Initial Structure, :Bead Size,
        :Pressure Treatment,
        :Heat Treatment, :Cooling Rate,
        :Polish, :Final Treatment, :ε1,
        :ε2, :ε3, :ε4
    )
);
```

[ Previous](Neural.html "Neural") [Next ](Regression.html "Regression")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
