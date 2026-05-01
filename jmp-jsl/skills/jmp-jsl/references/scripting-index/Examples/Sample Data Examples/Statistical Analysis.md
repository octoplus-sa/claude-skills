# Statistical Analysis

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Statistical%20Analysis.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Statistical%20Analysis.html)*

---

# [Statistical Analysis](#statistical-analysis)[](#statistical-analysis "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Perform a partition analysis on a dataset using various predictor variables and initial splits criteria to maximize significance.](#perform-a-partition-analysis-on-a-dataset-using-various-predictor-variables-and-initial-splits-criteria-to-maximize-significance)[](#perform-a-partition-analysis-on-a-dataset-using-various-predictor-variables-and-initial-splits-criteria-to-maximize-significance "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Equity.jmp");
// Partition
Partition(
    Y( :BAD ),
    X(
        :LOAN, :MORTDUE, :VALUE, :REASON,
        :JOB, :YOJ, :DEROG, :DELINQ,
        :CLAGE, :NINQ, :CLNO, :DEBTINC
    ),
    Show Split Prob( 1 ),
    Criterion( "Maximize Significance" ),
    Initial Splits(
        :DELINQ >= 1,
        {:DEBTINC >= 43.8475437170116},
        {:DEBTINC >= 45.7439490589145}
    )
);
```

[ Previous](Regression.html "Regression") [Next ](Text%20Analysis.html "Text Analysis")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
