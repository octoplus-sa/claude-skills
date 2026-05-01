# Multiple Factor Analysis

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Multiple%20Factor%20Analysis.html](https://jsl.jmp.com/All%20Categories/Objects/Multiple%20Factor%20Analysis.html)*

---

# [Multiple Factor Analysis](#multiple-factor-analysis)[](#multiple-factor-analysis "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Multiple Factor Analysis](#multiple-factor-analysis_1)[](#multiple-factor-analysis_1 "Click to copy url")

**Syntax:** Multiple Factor Analysis( MFABLocks({"Block 1", columns},{"Block 2", columns}) )

**Description:** Analyzes agreement among panelists in sensory data analysis.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
```

## [Columns](#columns)[](#columns "Click to copy url")

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj = Multiple Factor Analysis(...\<By( column(s) )\>...)

**Description:** Performs a separate analysis for each level of the specified column.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj = Multiple Factor Analysis(...\<Freq( column )\>...)

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    Freq( :_freqcol )
);
```

### [MFA Blocks](#mfa-blocks)[](#mfa-blocks "Click to copy url")

**Syntax:** obj = Multiple Factor Analysis(...\<MFA Blocks( column )\>...)

**Description:** Specifies groups of columns that should be treated as sub-tables within the multiple factor analysis.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Wine ),
    MFA Blocks(
        {"Susan", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness}
    )
);
```

### [Product ID](#product-id)[](#product-id "Click to copy url")

**Syntax:** obj = Multiple Factor Analysis(...\<Product ID( column )\>...)

**Description:** Specifies columns of items or products to be analyzed.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Wine ),
    MFA Blocks(
        {"Susan", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness}
    )
);
```

### [Supplementary](#supplementary)[](#supplementary "Click to copy url")

**Syntax:** obj = Multiple Factor Analysis(...\<Supplementary( column )\>...)

**Description:** Specifies one or more supplementary variables. Supplementary variables are not used in any of the calculations in the platform and including them does not affect the results. These variables can improve data interpretation or be used in future analyses.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Wine ),
    Z( :Region ),
    MFA Blocks(
        {"Susan", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness}
    )
);
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj = Multiple Factor Analysis(...\<Weight( column )\>...)

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    Weight( :_weightcol )
);
```

### [Z](#z)[](#z "Click to copy url")

**Syntax:** obj = Multiple Factor Analysis(...\<Z( column )\>...)

**Description:** Specifies one or more supplementary variables. Supplementary variables are not used in any of the calculations in the platform and including them does not affect the results. These variables can improve data interpretation or be used in future analyses.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Wine ),
    Z( :Region ),
    MFA Blocks(
        {"Susan", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness}
    )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Arrow Lines](#arrow-lines)[](#arrow-lines "Click to copy url")

**Syntax:** obj \<\< Arrow Lines( state=0\|1 )

**Description:** Shows or hides the arrow lines in the graph. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Arrow Lines( 0 );
```

### [Biplot](#biplot)[](#biplot "Click to copy url")

**Syntax:** obj \<\< Biplot( state=0\|1 )

**Description:** Shows or hides a plot that overlays the score plot and the loading plot for the specified number of components.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Biplot( 1 );
```

### [Biplot Select Component](#biplot-select-component)[](#biplot-select-component "Click to copy url")

**Syntax:** obj\<\<Biplot Select Component( 1, 3 )

**Description:** Selects the components that are used as axes in the biplot.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Biplot Select Component( 1, 3 );
```

### [Block Partial Contributions](#block-partial-contributions)[](#block-partial-contributions "Click to copy url")

**Syntax:** obj \<\< Block Partial Contributions( state=0\|1 )

**Description:** Displays or hides block contributions which is the sum of the contributions of its variables.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Block Partial Contributions( 1 );
```

### [Block Partial Inertias](#block-partial-inertias)[](#block-partial-inertias "Click to copy url")

**Syntax:** obj \<\< Block Partial Inertias( state=0\|1 )

**Description:** Displays or hides rescaled block contributions, such that the sum of inertia across blocks equals the principal component's eigenvalue.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Block Partial Inertias( 1 );
```

### [Block Partial and Consensus Correlations](#block-partial-and-consensus-correlations)[](#block-partial-and-consensus-correlations "Click to copy url")

**Syntax:** obj \<\< Block Partial and Consensus Correlations( state=0\|1 )

**Description:** Displays or hides a matrix of coefficients indicating the correlations between partial and consensus scores on each principal component dimension.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Block Partial and Consensus Correlations( 1 );
```

### [Block Squared Cosines](#block-squared-cosines)[](#block-squared-cosines "Click to copy url")

**Syntax:** obj \<\< Block Squared Cosines( state=0\|1 )

**Description:** Displays or hides the proportion of overlap in variance between blocks and principal component dimensions.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Block Squared Cosines( 1 );
```

### [Block Weights](#block-weights)[](#block-weights "Click to copy url")

**Syntax:** obj \<\< Block Weights( state=0\|1 )

**Description:** Displays or hides a matrix of block weight which is the inverse of each block's first singular value.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Block Weights( 1 );
```

### [Consensus Map](#consensus-map)[](#consensus-map "Click to copy url")

**Syntax:** obj \<\< Consensus Map( state=0\|1 )

**Description:** Displays or hides a Consensus Map which overlays the centroid scores and partial scores from each block. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Consensus Map( 0 );
```

### [Consensus Map Select Component](#consensus-map-select-component)[](#consensus-map-select-component "Click to copy url")

**Syntax:** obj\<\<Consensus Map Select Component( 1, 3 )

**Description:** Selects the components that are used as axes in the consensus map.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Consensus Map Select Component( 1, 3 );
```

### [Eigenvalues](#eigenvalues)[](#eigenvalues "Click to copy url")

**Syntax:** obj \<\< Eigenvalues( state=0\|1 )

**Description:** Shows or hides the sorted eigenvalues, their percent of variation, and the cumulative percent of variation.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Eigenvalues( 1 );
```

### [Eigenvectors](#eigenvectors)[](#eigenvectors "Click to copy url")

**Syntax:** obj \<\< Eigenvectors( state=0\|1 )

**Description:** Shows or hides a report of the eigenvectors for each of the principal components.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Eigenvectors( 1 );
```

### [Highlight Product](#highlight-product)[](#highlight-product "Click to copy url")

**Syntax:** obj\<\<Partial Axes Plot Select Component( 1, 3 )

**Description:** Highlights product clusters based on the specified inertial value.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    ),
    Consensus Map( 1 )
);
obj << Highlight Product( "Small Inertia", 4 );
```

### [Lg Coefficients](#lg-coefficients)[](#lg-coefficients "Click to copy url")

**Syntax:** obj \<\< Lg Coefficients( state=0\|1 )

**Description:** Displays or hides a matrix of coefficients indicating the similarity between blocks. Equivalent to unstandardized RV correlations.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Lg Coefficients( 1 );
```

### [Partial Axes Plot](#partial-axes-plot)[](#partial-axes-plot "Click to copy url")

**Syntax:** obj \<\< Partial Axes Plot( state=0\|1 )

**Description:** Displays or hides a Partial Axes Plot which shows the link between centroid plane and blocks.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Partial Axes Plot( 1 );
```

### [Partial Axes Plot Select Component](#partial-axes-plot-select-component)[](#partial-axes-plot-select-component "Click to copy url")

**Syntax:** obj\<\<Partial Axes Plot Select Component( 1, 3 )

**Description:** Selects the components that are used as axes in the Partial Axes Plot.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    ),
    Partial Axes Plot( 1 )
);
obj << Partial Axes Plot Select component( 1, 3 );
```

### [RV Correlations](#rv-correlations)[](#rv-correlations "Click to copy url")

**Syntax:** obj \<\< RV Correlations( state=0\|1 )

**Description:** Displays or hides a matrix of squared correlation coefficients between blocks. RV coefficients range from 0 to 1.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << RV Correlations( 1 );
```

### [Save Block Partial Scores](#save-block-partial-scores)[](#save-block-partial-scores "Click to copy url")

**Syntax:** obj \<\< Save Block Partial Scores

**Description:** Saves block partial scores to new columns in a data table.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Save Block Partial Scores();
```

### [Save Individual Partial Contributions](#save-individual-partial-contributions)[](#save-individual-partial-contributions "Click to copy url")

**Syntax:** obj \<\< Save Individual Partial Contributions

**Description:** Saves individual partial contributions to new columns in the data table.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Save Individual Partial Contributions();
```

### [Save Individual Scores](#save-individual-scores)[](#save-individual-scores "Click to copy url")

**Syntax:** obj \<\< Save Individual Scores

**Description:** Saves the given number of principal components to new columns in the data table.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Save Individual Scores();
```

### [Save Individual Squared Cosines](#save-individual-squared-cosines)[](#save-individual-squared-cosines "Click to copy url")

**Syntax:** obj \<\< Save Individual Squared Cosines

**Description:** Saves individual squared cosines to new columns in the data table.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Save Individual Squared Cosines();
```

### [Save Partial Axes Coordinates](#save-partial-axes-coordinates)[](#save-partial-axes-coordinates "Click to copy url")

**Syntax:** obj \<\< Save Partial Axes Coordinates

**Description:** Saves partial axes coordinates to new columns in a data table.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Save Partial Axes Coordinates();
```

### [Show Labels](#show-labels)[](#show-labels "Click to copy url")

**Syntax:** obj \<\< Show Labels( state=0\|1 )

**Description:** Displays or hides the labels of points in the graph.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Show Labels( 1 );
```

### [Summary Plot Select Component](#summary-plot-select-component)[](#summary-plot-select-component "Click to copy url")

**Syntax:** obj\<\<Summary Plot Select Component( 1, 3 )

**Description:** Selects the components that are used as axes in the summary plots.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Summary Plot Select Component( 1, 3 );
```

### [Summary Plots](#summary-plots)[](#summary-plots "Click to copy url")

**Syntax:** obj \<\< Summary Plots( state=0\|1 )

**Description:** Shows or hides an outline node that contains a plot of the eigenvalues, a score plot, and a loading plot. On by default.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Summary Plots( 0 );
```

### [Variable Loadings](#variable-loadings)[](#variable-loadings "Click to copy url")

**Syntax:** obj \<\< Variable Loadings( state=0\|1 )

**Description:** Displays or hides a report showing the columns corresponding to the component loadings.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Variable Loadings( 1 );
```

### [Variable Partial Contributions](#variable-partial-contributions)[](#variable-partial-contributions "Click to copy url")

**Syntax:** obj \<\< Variable Partial Contributions( state=0\|1 )

**Description:** Shows or hides a table that contains the partial contributions of variables and a plot of the partial contributions for the first three principal components.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Variable Partial Contributions( 1 );
```

### [Variable Squared Cosines](#variable-squared-cosines)[](#variable-squared-cosines "Click to copy url")

**Syntax:** obj \<\< Variable Squared Cosines( state=0\|1 )

**Description:** Shows or hides a table that contains the squared cosines of variables.

**JMP Version Added:** 14

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
obj = dt << Multiple Factor Analysis(
    MFA Blocks(
        {"Carolyn Peppery etc.", :Carolyn Peppery, :Carolyn Tannic, :Carolyn Aromatic,
        :Carolyn Berry Notes},
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness}
    )
);
obj << Variable Squared Cosines( 1 );
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Copy ByGroup Script;
```

### [Copy Script](#copy-script)[](#copy-script "Click to copy url")

**Syntax:** obj \<\< Copy Script

**Description:** Create a JSL script to produce this analysis, and put it on the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
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

### [Get ByGroup Script](#get-bygroup-script)[](#get-bygroup-script "Click to copy url")

**Syntax:** obj \<\< Get ByGroup Script

**Description:** Creates a script (JSL) to produce this analysis and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
t = obj[1] << Get ByGroup Script;
Show( t );
```

### [Get Container](#get-container)[](#get-container "Click to copy url")

**Syntax:** obj \<\< Get Container

**Description:** Returns a reference to the container box that holds the content for the object.

#### [General](#general)[](#general "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Data Table;
```

### [Save ByGroup Script to Journal](#save-bygroup-script-to-journal)[](#save-bygroup-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Journal;
```

### [Save ByGroup Script to Script Window](#save-bygroup-script-to-script-window)[](#save-bygroup-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save ByGroup Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save ByGroup Script to Script Window;
```

### [Save Script for All Objects](#save-script-for-all-objects)[](#save-script-for-all-objects "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects

**Description:** Creates a script for all report objects in the window and appends it to the current Script window. This option is useful when you have multiple reports in the window.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table( "My Script" );
```

### [Save Script to Data Table](#save-script-to-data-table)[](#save-script-to-data-table "Click to copy url")

**Syntax:** Save Script to Data Table( \<name\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Create a JSL script to produce this analysis, and save it as a table property in the data table.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
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
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Wine Sensory Data.jmp" );
dt << Multiple Factor Analysis(
    Product ID( :Vineyard ),
    Z( :Region ),
    MFA Blocks(
        {"Susan Fruity etc.", :Susan Fruity, :Susan Flowery, :Susan Spicy, :Susan Crispness},
        {"Florence Flowery etc.", :Florence Flowery, :Florence Crispness, :Florence Tannin,
        :Florence Savory, :Florence Lightness},
        {"Xavier Fruity etc.", :Xavier Fruity, :Xavier Spicy, :Xavier Crispness,
        :Xavier Alcohol, :Xavier Savory, :Xavier Lightness},
        {"Robert Fruity etc.", :Robert Fruity, :Robert Flowery, :Robert Spicy,
        :Robert Crispness, :Robert Tannin, :Robert Alcohol, :Robert Savory, :Robert Lightness
        },
        {"Paula Fruity etc.", :Paula Fruity, :Paula Flowery, :Paula Spicy, :Paula Crispness,
        :Paula Tannin, :Paula Savory},
        {"Monica Fruity etc.", :Monica Fruity, :Monica Flowery, :Monica Spicy, :Monica Tannin,
        :Monica Alcohol, :Monica Savory, :Monica Lightness},
        {"Frank Fruity etc.", :Frank Fruity, :Frank Flowery, :Frank Spicy, :Frank Crispness,
        :Frank Tannin, :Frank Alcohol, :Frank Savory, :Frank Lightness}
    )
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

**Syntax:** obj = Multiple Factor Analysis(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

[ Previous](Multiple%20Correspondence%20Analysis.html "Multiple Correspondence Analysis") [Next ](Multiple%20File%20Import.html "Multiple File Import")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
