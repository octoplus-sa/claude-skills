# Dimensionality Reduction

*Source: [https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Dimensionality%20Reduction.html](https://jsl.jmp.com/Examples/Sample%20Data%20Examples/Dimensionality%20Reduction.html)*

---

# [Dimensionality Reduction](#dimensionality-reduction)[](#dimensionality-reduction "Click to copy url")

More examples for this topic using the sample data files provided with JMP

### [Perform principal components: analysis for variable reduction](#perform-principal-components-analysis-for-variable-reduction)[](#perform-principal-components-analysis-for-variable-reduction "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Body Fat.jmp");
// Principal Components: Variable Reduction
Principal Components(
    Y(
        :"Age (years)"n, :"Weight (lbs)"n,
        :"Height (inches)"n,
        :"Neck circumference (cm)"n,
        :"Chest circumference (cm)"n,
        :"Abdomen circumference (cm)"n,
        :"Hip circumference (cm)"n,
        :"Thigh circumference (cm)"n,
        :"Knee circumference (cm)"n,
        :"Ankle circumference (cm)"n,
        :
        "Biceps (extended) circumference (cm)"n,
        :"Forearm circumference (cm)"n,
        :"Wrist circumference (cm)"n
    ),
    Estimation Method( "Row-wise" ),
    on Correlations,
    Cluster Variables,
    SendToReport(
        Dispatch( {"Summary Plots"},
            "PCA Summary Plots", FrameBox,
            {Frame Size( 51, 37 )}
        ),
        Dispatch( {"Summary Plots"},
            "PCA Summary Plots",
            FrameBox( 2 ),
            {Frame Size( 55, 37 )}
        )
    )
);
```

### [Create a loading plot using the Principal Components analysis with specified correlations and eigenvalues on the dataset.](#create-a-loading-plot-using-the-principal-components-analysis-with-specified-correlations-and-eigenvalues-on-the-dataset)[](#create-a-loading-plot-using-the-principal-components-analysis-with-specified-correlations-and-eigenvalues-on-the-dataset "Click to copy url")

``` jsl
// Open data table
dt = Open("$Sample_Data/Quality Control/Steam Turbine Historical.jmp");
// Loading plot
Principal Components(
    Y(
        :Fuel, :Steam Flow, :Steam Temp,
        :MW, :Cool Temp, :Pressure
    ),
    Estimation Method( "Default" ),
    "on Correlations",
    Eigenvalues( 1 ),
    Summary Plots( 0 ),
    Loading Plot( 4 )
);
```

[ Previous](Design%20of%20Experiments.html "Design of Experiments") [Next ](Distribution%20Analysis.html "Distribution Analysis")

------------------------------------------------------------------------

© 2025 JMP Statistical Discovery LLC. All Rights Reserved.
