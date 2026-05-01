# Dataset Analysis

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Dataset%20Analysis.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Dataset%20Analysis.html)*

---

# [Dataset Analysis](#dataset-analysis)[](#dataset-analysis "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Perform a Cartesian join between the Oil Amount and Batch data tables.](#perform-a-cartesian-join-between-the-oil-amount-and-batch-data-tables)[](#perform-a-cartesian-join-between-the-oil-amount-and-batch-data-tables "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Oil Amount.jmp");
// Join
Data Table( "Oil Amount" ) <<
Join(
    With(
        Open( "$SAMPLE_DATA/Batch.jmp" )
    ),
    Cartesian Join
);
```

[ Previous](Data%20Tables.html "Data Tables") [Next ](Design%20of%20Experiments.html "Design of Experiments")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
