# Structural Equation Models

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Structural%20Equation%20Models.html](https://jsl.jmp.com/All%20Categories/Objects/Structural%20Equation%20Models.html)*

---

# [Structural Equation Models](#structural-equation-models)[](#structural-equation-models "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Structural Equation Models](#structural-equation-models_1)[](#structural-equation-models_1 "Click to copy url")

**Syntax:** Structural Equation Models( Model Variables ( columns ) )

**Description:** Provides a framework to fit a variety of models, including confirmatory factor analysis, path models with or without latent variables, measurement error models, and latent growth curve models.

**JMP Version Added:** 15

#### [Confirmatory Factor Analysis](#confirmatory-factor-analysis)[](#confirmatory-factor-analysis "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
```

#### [Higher Order Confirmatory Factor Analysis](#higher-order-confirmatory-factor-analysis)[](#higher-order-confirmatory-factor-analysis "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables(
        :Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C, :Inter_C, :General_S,
        :Growth_S, :Coworker_S, :Supervisor_S
    ),
    Fit(
        Model Name( "Higher Order CFA" ),
        New Latent( "Leadership", "Conflict", "Satisfaction", "General" ),
        Means(
            {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C,
            :Inter_C, :General_S, :Growth_S, :Coworker_S, :Supervisor_S}}
        ),
        Loadings(
            {"Leadership", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}},
            {"Conflict", {:Person_C, :Intra_C, :Inter_C}, {1}},
            {"Satisfaction", {:General_S, :Growth_S, :Coworker_S, :Supervisor_S}, {1}},
            {"General", {"Leadership", "Conflict", "Satisfaction"}, {1}}
        ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {:Person_C, {:Person_C}},
            {:Intra_C, {:Intra_C}},
            {:Inter_C, {:Inter_C}},
            {:General_S, {:General_S}},
            {:Growth_S, {:Growth_S}},
            {:Coworker_S, {:Coworker_S}},
            {:Supervisor_S, {:Supervisor_S}},
            {"Leadership", {"Leadership"}},
            {"Conflict", {"Conflict"}},
            {"Satisfaction", {"Satisfaction"}},
            {"General", {"General"}}
        )
    )
);
```

#### [Linear Latent Growth Curve Model](#linear-latent-growth-curve-model)[](#linear-latent-growth-curve-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Linear Growth Curve Model" ),
        New Latent( "Intercept", "Slope" ),
        Means( {"Constant", {"Intercept", "Slope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}, {"b1"}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}, {"b1"}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}, {"b1"}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}, {"b1"}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}}
        ),
        Covariances( {"Intercept", {"Slope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
```

#### [Multiple Linear Regression with SEM](#multiple-linear-regression-with-sem)[](#multiple-linear-regression-with-sem "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables( :Satisfaction_Avg, :Support_L, :Goal_L, :Work_L ),
    Fit(
        Model Name( "Multiple Regression" ),
        Means( {"Constant", {:Satisfaction_Avg, :Support_L, :Goal_L, :Work_L}} ),
        Regressions(
            {:Support_L, {:Satisfaction_Avg}},
            {:Goal_L, {:Satisfaction_Avg}},
            {:Work_L, {:Satisfaction_Avg}}
        ),
        Variances(
            {:Satisfaction_Avg, {:Satisfaction_Avg}},
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}}
        ),
        Covariances( {:Support_L, {:Goal_L, :Work_L}}, {:Goal_L, {:Work_L}} ),

    )
);
```

#### [Path Analysis Model](#path-analysis-model)[](#path-analysis-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Online Consumer Data.jmp" );
dt << Structural Equation Models(
    Model Variables( :Privacy, :Reputation, :Trust, :Purchase Int ),
    Fit(
        Model Name( "Path Analysis with Observed Variables" ),
        Means( {"Constant", {:Privacy, :Reputation, :Trust, :Purchase Int}} ),
        Regressions(
            {:Privacy, {:Trust}},
            {:Reputation, {:Trust, :Purchase Int}},
            {:Trust, {:Purchase Int}}
        ),
        Variances(
            {:Privacy, {:Privacy}},
            {:Reputation, {:Reputation}},
            {:Trust, {:Trust}},
            {:Purchase Int, {:Purchase Int}}
        ),
        Covariances( {:Privacy, {:Reputation}} )
    )
);
```

#### [Path Analysis with Latent Variables](#path-analysis-with-latent-variables)[](#path-analysis-with-latent-variables "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables(
        :Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C, :Inter_C, :General_S,
        :Growth_S, :Coworker_S, :Supervisor_S
    ),
    Fit(
        Model Name( "Path Analysis with Latent Variables" ),
        New Latent( "Leadership", "Conflict", "Satisfaction" ),
        Means(
            {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L, :Person_C, :Intra_C,
            :Inter_C, :General_S, :Growth_S, :Coworker_S, :Supervisor_S}}
        ),
        Loadings(
            {"Leadership", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}},
            {"Conflict", {:Person_C, :Intra_C, :Inter_C}, {1}},
            {"Satisfaction", {:General_S, :Growth_S, :Coworker_S, :Supervisor_S}, {1}}
        ),
        Regressions(
            {"Leadership", {"Conflict", "Satisfaction"}},
            {"Conflict", {"Satisfaction"}}
        ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {:Person_C, {:Person_C}},
            {:Intra_C, {:Intra_C}},
            {:Inter_C, {:Inter_C}},
            {:General_S, {:General_S}},
            {:Growth_S, {:Growth_S}},
            {:Coworker_S, {:Coworker_S}},
            {:Supervisor_S, {:Supervisor_S}},
            {"Leadership", {"Leadership"}},
            {"Conflict", {"Conflict"}},
            {"Satisfaction", {"Satisfaction"}}
        )
    )
);
```

#### [Quadratic Latent Growth Curve Model](#quadratic-latent-growth-curve-model)[](#quadratic-latent-growth-curve-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Quadratic Growth Model" ),
        New Latent( "Intercept", "Slope", "QuadSlope" ),
        Means( {"Constant", {"Intercept", "Slope", "QuadSlope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}},
            {"QuadSlope", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {0, 1, 4, 9}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}},
            {"QuadSlope", {"QuadSlope"}}
        ),
        Covariances( {"Intercept", {"Slope", "QuadSlope"}}, {"Slope", {"QuadSlope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
```

#### [Simple Linear Regression with SEM](#simple-linear-regression-with-sem)[](#simple-linear-regression-with-sem "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Satisfaction_Avg ),
    Fit(
        Model Name( "Simple Regression" ),
        Means( {"Constant", {:Leadership_Avg, :Satisfaction_Avg}} ),
        Regressions( {:Leadership_Avg, {:Satisfaction_Avg}} ),
        Variances(
            {:Leadership_Avg, {:Leadership_Avg}},
            {:Satisfaction_Avg, {:Satisfaction_Avg}}
        )
    )
);
```

#### [Simple Mediation Model](#simple-mediation-model)[](#simple-mediation-model "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg, :Satisfaction_Avg ),
    Fit(
        Model Name( "Mediation Analysis" ),
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg, :Satisfaction_Avg}} ),
        Regressions(
            {:Leadership_Avg, {:Conflict_Avg, :Satisfaction_Avg}},
            {:Conflict_Avg, {:Satisfaction_Avg}}
        ),
        Variances(
            {:Leadership_Avg, {:Leadership_Avg}},
            {:Conflict_Avg, {:Conflict_Avg}},
            {:Satisfaction_Avg, {:Satisfaction_Avg}}
        )
    )
);
```

## [Columns](#columns)[](#columns "Click to copy url")

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** obj \<\< Freq( column )

**Description:** Specifies a column whose values assign a frequency to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_freqcol", Numeric, Continuous, Set Each Value( Random Integer( 1, 5 ) ) );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    ),
    Freq( :_freqcol )
);
```

### [Groups](#groups)[](#groups "Click to copy url")

**Syntax:** obj \<\< Groups( column )

**Description:** Specifies the grouping variable for performing multiple group analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
dt << Structural Equation Models( Model Variables( 4 :: 7 ), Groups( :Sex ) );
```

### [Mean](#mean)[](#mean "Click to copy url")

**Syntax:** obj = Structural Equation Models(...\<Mean( column )\>...)

**Description:** Specifies means for each manifest variable in a correlation or covariance matrix.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
mat = dt[0, 2 :: 5];
mat_cor = Correlation( mat );
mat_means = V Mean( mat );
mat_sds = V Std( mat );
As Table( mat_cor || mat_means` || mat_sds` ) << Set Name( "Correlation" );
Data Table( "Correlation" ) << Structural Equation Models(
    Data Format( "Matrix" ),
    Model Variables( 1 :: 4 ),
    Mean( :Col5 ),
    Std Dev( :Col6 ),
    Sample Size( 200 )
);
```

### [Model Variables](#model-variables)[](#model-variables "Click to copy url")

**Syntax:** obj \<\< Model Variables( column(s) )

**Description:** Specifies the variables that will be submitted for analysis.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L )
);
```

### [Std Dev](#std-dev)[](#std-dev "Click to copy url")

**Syntax:** obj = Structural Equation Models(...\<Std Dev( column )\>...)

**Description:** Specifies standard deviations for each manifest variable in a correlation matrix.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
mat = dt[0, 2 :: 5];
mat_cor = Correlation( mat );
mat_means = V Mean( mat );
mat_sds = V Std( mat );
As Table( mat_cor || mat_means` || mat_sds` ) << Set Name( "Correlation" );
Data Table( "Correlation" ) << Structural Equation Models(
    Data Format( "Matrix" ),
    Model Variables( 1 :: 4 ),
    Mean( :Col5 ),
    Std Dev( :Col6 ),
    Sample Size( 200 )
);
```

### [Weight](#weight)[](#weight "Click to copy url")

**Syntax:** obj \<\< Weight( column )

**Description:** Specifies a column whose values assign a weight to each row for the analysis.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_weightcol", Numeric, Continuous, Set Each Value( Random Beta( 1, 1 ) ) );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    ),
    Weight( :_weightcol )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Add Manifest Variables](#add-manifest-variables)[](#add-manifest-variables "Click to copy url")

**Syntax:** obj \<\< Add Manifest Variables

**Description:** Relaunches the platform using the existing model specification and including the newly added manifest variables.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: CFA 1Factor Conflict UI" );
obj << Add Manifest Variables();
```

### [Bootstrap Inference](#bootstrap-inference)[](#bootstrap-inference "Click to copy url")

**Syntax:** obj \<\< Bootstrap Inference

**Description:** Performs bootstrapping for a user-specified selection of estimates in available fitted models of the SEM report.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Bootstrap Inference( Parameter Estimates( 1 ), Indirect Effects( 1 ) );
```

### [Compare Selected Models](#compare-selected-models)[](#compare-selected-models "Click to copy url")

**Syntax:** obj \<\< Compare Selected Models

**Description:** Compares models selected in the Model Comparison table.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Measurement Models" );
obj << Compare Selected Models( {"Orthogonal 3-Factor CFA", "3-Factor CFA"} );
```

### [Copy Diagram Properties](#copy-diagram-properties)[](#copy-diagram-properties "Click to copy url")

**Syntax:** obj \<\< Copy Diagram Properties

**Description:** Copies the current path diagram properties to the clipboard. You can then paste the properties into another SEM path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt2 = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt2 << Run Script( "SEM: Compare Growth Trajectories" );
obj << Copy Diagram Properties();
obj2 = dt << Structural Equation Models( Model Variables( 2 :: 12 ) );
obj2 << Paste Diagram Properties();
```

### [Copy Model Specification](#copy-model-specification)[](#copy-model-specification "Click to copy url")

**Syntax:** obj \<\< Copy Model Specification

**Description:** Copies the current structural equation model specifications to the clipboard. You can then paste the model specifications into another SEM platform report.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Path Analysis no Latent" );
obj << Copy Model Specification();
obj2 = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg, :Satisfaction_Avg )
);
obj2 << Paste Model Specification();
```

### [Estimation Method](#estimation-method)[](#estimation-method "Click to copy url")

**Syntax:** obj = Structural Equation Models(...Estimation Method( "Maximum Likelihood (ML and FIML)"\|"Maximum Likelihood with Robust Inference"\|"MIIV Two-Stage Least Squares" )...)

**Description:** Enables using different estimators for analysis.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Estimation Method( "MIIV Two-Stage Least Squares" ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Goal_L, :Work_L, :Interact_L, "Leader"}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 ),
        Assess Measurement Model( 1 )
    )
);
```

### [Fit](#fit)[](#fit "Click to copy url")

**Syntax:** obj \<\< Fit

**Description:** Determines the structural equation model to be fit.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        )
    )
);
```

### [Fit Independence Model](#fit-independence-model)[](#fit-independence-model "Click to copy url")

**Syntax:** obj = Structural Equation Models(...Fit Independence Model( state=0\|1 )...)

**Description:** Disables fitting the independence model upon launching the platform. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit Independence Model( 0 )
);
```

### [Fit Unrestricted Model](#fit-unrestricted-model)[](#fit-unrestricted-model "Click to copy url")

**Syntax:** obj \<\< Fit Unrestricted Model( state=0\|1 )

**Description:** Disables fitting the unrestricted, also known as saturated, model upon launching the platform.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit Unrestricted Model( 0 )
);
```

### [Full Information Multivariate Statistics](#full-information-multivariate-statistics)[](#full-information-multivariate-statistics "Click to copy url")

**Syntax:** obj \<\< Full Information Multivariate Statistics( state=0\|1 )

**Description:** Shows or hides a multivariate simple statistics report, where the statistics are estimated with full information maximum likelihood to account for missing data.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L )
);
obj << Full Information Multivariate Statistics( 1 );
```

### [Generate R Code](#generate-r-code)[](#generate-r-code "Click to copy url")

**Syntax:** obj \<\< Generate R Code

**Description:** Generates R code for the currently specified model. The code is written to a script editor window.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Path Analysis no Latent" );
obj << Generate R Code();
```

### [Hide Model](#hide-model)[](#hide-model "Click to copy url")

**Syntax:** obj \<\< Hide Model

**Description:** Hides models according to selections in the model comparison table.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        )
    ),
    Hide Model( {3} )
);
```

### [Launch Explore Missing Values](#launch-explore-missing-values)[](#launch-explore-missing-values "Click to copy url")

**Syntax:** obj \<\< Launch Explore Missing Values

**Description:** Launches the Explore Missing Values platform.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L )
);
obj << Launch Explore Missing Values( 1 );
```

### [Launch Explore Outliers](#launch-explore-outliers)[](#launch-explore-outliers "Click to copy url")

**Syntax:** obj \<\< Launch Explore Outliers

**Description:** Launches the Explore Outliers platform.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L )
);
obj << Launch Explore Outliers( 1 );
```

### [Model Specification](#model-specification)[](#model-specification "Click to copy url")

**Syntax:** obj \<\< Model Specification

**Description:** Enables specification of a structural equation model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Model Name( "Means and Variances Model" ),
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

### [Paste Diagram Properties](#paste-diagram-properties)[](#paste-diagram-properties "Click to copy url")

**Syntax:** obj \<\< Paste Diagram Properties

**Description:** Pastes the path diagram properties from the clipboard into the current SEM path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt2 = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt2 << Run Script( "SEM: Compare Growth Trajectories" );
obj << Copy Diagram Properties();
obj2 = dt << Structural Equation Models( Model Variables( 2 :: 12 ) );
obj2 << Paste Diagram Properties();
```

### [Paste Model Specification](#paste-model-specification)[](#paste-model-specification "Click to copy url")

**Syntax:** obj \<\< Paste Model Specification

**Description:** Pastes the model specifications from the clipboard into the current model specifications.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Path Analysis no Latent" );
obj << Copy Model Specification();
obj2 = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg, :Satisfaction_Avg )
);
obj2 << Paste Model Specification();
```

### [Path Diagram Properties](#path-diagram-properties)[](#path-diagram-properties "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Linear Growth Model" ),
        New Latent( "Intercept", "Slope" ),
        Means( {"Constant", {"Intercept", "Slope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}, {"b1"}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}, {"b1"}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}, {"b1"}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}, {"b1"}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}}
        ),
        Covariances( {"Intercept", {"Slope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
```

### [Remove Manifest Variables](#remove-manifest-variables)[](#remove-manifest-variables "Click to copy url")

**Syntax:** obj \<\< Remove Manifest Variables

**Description:** Relaunches the platform using the existing model specification but without the removed manifest variables.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: CFA 1Factor Conflict UI" );
obj << Remove Manifest Variables();
```

### [Reset Independence Model](#reset-independence-model)[](#reset-independence-model "Click to copy url")

**Syntax:** obj \<\< Reset Independence Model

**Description:** Replaces a user-specified independence model with the default one.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Run Script( "SEM: Compare Growth Trajectories" );
obj << Set as Independence Model( 2 );
obj << Reset Independence Model();
```

### [Robust Inference](#robust-inference)[](#robust-inference "Click to copy url")

**Syntax:** obj \<\< Robust Inference( state=0\|1 )

**Description:** Computes sandwich standard errors for the ML or FIML parameter estimates and the robust fit statistics. This option is used for non-normally distributed outcomes where a continuous underlying distribution is assumed.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Robust Inference( 1 );
```

### [Set as Independence Model](#set-as-independence-model)[](#set-as-independence-model "Click to copy url")

**Syntax:** obj \<\< Set as Independence Model( number )

**Description:** Replaces the default independence model with a user-specified one.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Run Script( "SEM: Compare Growth Trajectories" );
obj << Set as Independence Model( 2 );
```

### [Standardize Latent Variables](#standardize-latent-variables)[](#standardize-latent-variables "Click to copy url")

**Syntax:** obj = Structural Equation Models(...Standardize Latent Variables( state=0\|1 )...)

**Description:** Sets the variance of latent variables to unity upon specification.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Standardize Latent Variables( 1 )
);
```

### [Univariate Simple Statistics](#univariate-simple-statistics)[](#univariate-simple-statistics "Click to copy url")

**Syntax:** obj \<\< Univariate Simple Statistics( state=0\|1 )

**Description:** Shows or hides a univariate simple statistics report, where the statistics are calculated for each column independently from other columns that might have missing data.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L )
);
obj << Univariate Simple Statistics( 1 );
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
    )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        Model Name( "One Factor CFA" ),
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        ),
        Standardized Parameter Estimates( 1 ),
        Normalized Residuals Heat Map( 1 )
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

**Syntax:** obj = Structural Equation Models(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

## [Structural Equation Models Fit \> Structural Equation Models Equation Details](#structural-equation-models-fit-structural-equation-models-equation-details)[](#structural-equation-models-fit-structural-equation-models-equation-details "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Composite Error](#composite-error)[](#composite-error "Click to copy url")

**Syntax:** obj \<\< Composite Error( state=0\|1 )

**Description:** Shows or hides the composite error of the model-implied instrumental variable two-stage least squares equations.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA\Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989) MIIV-2SLS Estimator" );
obj << Equation Details( Composite Error( 1 ) );
```

#### [Show All Equations](#show-all-equations)[](#show-all-equations "Click to copy url")

**Syntax:** obj \<\< Show All Equations( state=0\|1 )

**Description:** Shows or hides equations in the model that have only the Constant as a predictor.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA\Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989) MIIV-2SLS Estimator" );
obj << Equation Details( Show All Equations( 1 ) );
```

#### [Variance of the Error](#variance-of-the-error)[](#variance-of-the-error "Click to copy url")

**Syntax:** obj \<\< Variance of the Error( state=0\|1 )

**Description:** Shows or hides the variance of the error for each equation in the model.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA\Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989) MIIV-2SLS Estimator" );
obj << Equation Details( Variance of the Error( 1 ) );
```

## [Structural Equation Models Fit \> Structural Equation Models Remove Effects](#structural-equation-models-fit-structural-equation-models-remove-effects)[](#structural-equation-models-fit-structural-equation-models-remove-effects "Click to copy url")

### [Item Messages](#item-messages_2)[](#item-messages_2 "Click to copy url")

#### [Remove Effects](#remove-effects)[](#remove-effects "Click to copy url")

**Syntax:** obj \<\< Remove Effects

**Description:** Removes specific indirect effects from the report.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA\Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Path Analysis no Latent" );
obj << Specific Indirect Effects( {"Leadership_Avg", "Satisfaction_Avg"} );
rpt = obj << Report();
scrobj = rpt[Outline Box( "Specific Indirect Effects" )] << Get Scriptable Object();
scrobj << Remove Effects( 1 );
```

## [Structural Equation Models Fit](#structural-equation-models-fit)[](#structural-equation-models-fit "Click to copy url")

### [Item Messages](#item-messages_3)[](#item-messages_3 "Click to copy url")

#### [All Modification Indices](#all-modification-indices)[](#all-modification-indices "Click to copy url")

**Syntax:** obj \<\< All Modification Indices( state=0\|1 )

**Description:** Shows or hides a report that contains the estimates of model modification indices. These values can be used to determine which parameters might be added to the model to improve model fit.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Modification Indices( 1 );
```

#### [Assess Measurement Model](#assess-measurement-model)[](#assess-measurement-model "Click to copy url")

**Syntax:** obj \<\< Assess Measurement Model( state=0\|1 )

**Description:** Shows or hides a variety of statistics for quantifying the reliability and validity of tests and measures, including indicator reliability, coefficients omega and H, and a construct validity matrix.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Measurement Models" );
obj << Assess Measurement Model( 1 );
```

#### [Confidence Intervals](#confidence-intervals)[](#confidence-intervals "Click to copy url")

**Syntax:** obj \<\< Confidence Intervals( state=0\|1 )

**Description:** Shows or hides 95% confidence intervals for all parameter estimates.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Confidence Intervals( 1 );
```

#### [Copy Diagram Properties](#copy-diagram-properties_1)[](#copy-diagram-properties_1 "Click to copy url")

**Syntax:** obj \<\< Copy Diagram Properties

**Description:** Copies the current path diagram properties to the clipboard. You can then paste the properties into another SEM path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt2 = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt2 << Run Script( "SEM: Compare Growth Trajectories" );
obj << Copy Diagram Properties();
obj2 = dt << Structural Equation Models( Model Variables( 2 :: 12 ) );
obj2 << Paste Diagram Properties();
```

#### [Copy Model Specification](#copy-model-specification_1)[](#copy-model-specification_1 "Click to copy url")

**Syntax:** obj \<\< Copy Model Specification

**Description:** Copies the current structural equation model specifications to the clipboard. You can then paste the model specifications into another SEM platform report.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Path Analysis w/ Latent" );
obj << (Fit[1] << Copy Model Specification());
obj2 = dt << Structural Equation Models( Model Variables( 2 :: 12 ) );
obj2 << Paste Model Specification();
```

#### [Correlation of Estimates](#correlation-of-estimates)[](#correlation-of-estimates "Click to copy url")

**Syntax:** obj \<\< Correlation of Estimates( state=0\|1 )

**Description:** Shows or hides a report that contains the correlation matrix of the parameter estimates for the model.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Correlation of Estimates( 1 );
```

#### [Correlation of Estimates Heat Map](#correlation-of-estimates-heat-map)[](#correlation-of-estimates-heat-map "Click to copy url")

**Syntax:** obj \<\< Correlation of Estimates Heat Map( state=0\|1 )

**Description:** Shows or hides a report that contains a heat map of the correlations among the estimates of the model.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Correlation of Estimates Heat Map( 1 );
```

#### [Covariance of Estimates](#covariance-of-estimates)[](#covariance-of-estimates "Click to copy url")

**Syntax:** obj \<\< Covariance of Estimates( state=0\|1 )

**Description:** Shows or hides a report that contains the covariance matrix of the parameter estimates for the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Covariance of Estimates( 1 );
```

#### [Covariance of Estimates Heat Map](#covariance-of-estimates-heat-map)[](#covariance-of-estimates-heat-map "Click to copy url")

**Syntax:** obj \<\< Covariance of Estimates Heat Map( state=0\|1 )

**Description:** Shows or hides a report that contains a heat map of the covariances among the estimates of the model.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Covariance of Estimates Heat Map( 1 );
```

#### [Covariances](#covariances)[](#covariances "Click to copy url")

**Syntax:** obj \<\< Covariances

**Description:** Adds covariances between variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Covariances( {:Leadership_Avg, {:Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

#### [Define Time Values](#define-time-values)[](#define-time-values "Click to copy url")

**Syntax:** obj \<\< Define Time Values

**Description:** Defines the occasions of measurement for the repeated observations. These values are used for specifying longitudinal models.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Multiple Choice Year1, :Multiple Choice Year3, :Multiple Choice Year4 ),
    Fit(
        Model Name( "Linear Growth Model" ),
        Define Time Values( {0, 2, 3} ),
        New Latent( "Intercept", "Slope" ),
        Means( {"Constant", {"Intercept", "Slope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year3,
            :Multiple Choice Year4}, {1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year3, :Multiple Choice Year4
            }, {0, 2, 3}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}, {"b1"}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}, {"b1"}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}, {"b1"}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}}
        ),
        Covariances( {"Intercept", {"Slope"}} ),
        Path Diagram Properties( Show Means( 1 ) ),
        Predicted Values Plot( 1, 1 )
    )
);
```

#### [Equation Details](#equation-details)[](#equation-details "Click to copy url")

**Syntax:** obj \<\< Equation Details( state=0\|1 )

**Description:** Shows or hides a report that contains details of each equation in the model.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Estimation Method( "MIIV Two-Stage Least Squares" ),
    Fit(
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        )
    )
);
obj << Equation Details( 0 );
```

#### [Fit Indices](#fit-indices)[](#fit-indices "Click to copy url")

**Syntax:** obj \<\< Fit Indices( state=0\|1 )

**Description:** Shows or hides a report that contains fit indices for the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Fit Indices( 1 );
```

#### [Indirect Effects](#indirect-effects)[](#indirect-effects "Click to copy url")

**Syntax:** obj \<\< Indirect Effects( state=0\|1 )

**Description:** Shows or hides all available indirect effects in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Indirect Effects( 1 );
```

#### [Loadings](#loadings)[](#loadings "Click to copy url")

**Syntax:** obj \<\< Loadings

**Description:** Adds loadings to latent variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        )
    )
);
```

#### [Means/Intercepts](#meansintercepts)[](#meansintercepts "Click to copy url")

**Syntax:** obj \<\< Means/Intercepts

**Description:** Adds means or intercepts to the variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Model Specification(
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}}
        )
    )
);
```

#### [Model Implied Correlations](#model-implied-correlations)[](#model-implied-correlations "Click to copy url")

**Syntax:** obj \<\< Model Implied Correlations( state=0\|1 )

**Description:** Shows or hides a report that contains the correlation matrix that is implied by the model.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Model Implied Correlations( 1 );
```

#### [Model Implied Correlations Heat Map](#model-implied-correlations-heat-map)[](#model-implied-correlations-heat-map "Click to copy url")

**Syntax:** obj \<\< Model Implied Correlations Heat Map( state=0\|1 )

**Description:** Shows or hides a report that contains a heat map of the correlations implied by the model.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Model Implied Correlations Heat Map( 1 );
```

#### [Model Implied Covariances](#model-implied-covariances)[](#model-implied-covariances "Click to copy url")

**Syntax:** obj \<\< Model Implied Covariances( state=0\|1 )

**Description:** Shows or hides a report that contains the covariance matrix that is implied by the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Model Implied Covariances( 1 );
```

#### [Model Implied Covariances Heat Map](#model-implied-covariances-heat-map)[](#model-implied-covariances-heat-map "Click to copy url")

**Syntax:** obj \<\< Model Implied Covariances Heat Map( state=0\|1 )

**Description:** Shows or hides a report that contains a heat map of the covariances implied by the model.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Model Implied Covariances Heat Map( 1 );
```

#### [Model Implied Means](#model-implied-means)[](#model-implied-means "Click to copy url")

**Syntax:** obj \<\< Model Implied Means( state=0\|1 )

**Description:** Shows or hides a report that contains the means for each variable that are implied by the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Model Implied Means( 1 );
```

#### [Model Name](#model-name)[](#model-name "Click to copy url")

**Syntax:** obj \<\< Model Name

**Description:** Sets a model name.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Model Name( "Means and Variances Model" ),
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

#### [Modification Indices](#modification-indices)[](#modification-indices "Click to copy url")

**Syntax:** obj \<\< Modification Indices( state=0\|1 )

**Description:** Shows or hides a report that contains the estimates of model modification indices. These values can be used to determine which parameters might be added to the model to improve model fit.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Modification Indices( 1 );
```

#### [Modification Indices for Covariances](#modification-indices-for-covariances)[](#modification-indices-for-covariances "Click to copy url")

**Syntax:** obj \<\< Modification Indices for Covariances( state=0\|1 )

**Description:** Shows or hides a report that contains the estimates of model modification indices. These values can be used to determine which parameters might be added to the model to improve model fit.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Modification Indices for Covariances( 1 );
```

#### [Modification Indices for Loadings](#modification-indices-for-loadings)[](#modification-indices-for-loadings "Click to copy url")

**Syntax:** obj \<\< Modification Indices for Loadings( state=0\|1 )

**Description:** Shows or hides a report that contains the estimates of model modification indices. These values can be used to determine which parameters might be added to the model to improve model fit.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Modification Indices for Loadings( 1 );
```

#### [Modification Indices for Means](#modification-indices-for-means)[](#modification-indices-for-means "Click to copy url")

**Syntax:** obj \<\< Modification Indices for Means( state=0\|1 )

**Description:** Shows or hides a report that contains the estimates of model modification indices. These values can be used to determine which parameters might be added to the model to improve model fit.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Linear Growth Model" ),
        New Latent( "Intercept", "Slope" ),
        Means( {"Constant", {"Intercept", "Slope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}, {"b1"}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}, {"b1"}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}, {"b1"}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}, {"b1"}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}}
        ),
        Covariances( {"Intercept", {"Slope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
obj << Modification Indices for Means( 1 );
```

#### [Modification Indices for Regressions](#modification-indices-for-regressions)[](#modification-indices-for-regressions "Click to copy url")

**Syntax:** obj \<\< Modification Indices for Regressions( state=0\|1 )

**Description:** Shows or hides a report that contains the estimates of model modification indices. These values can be used to determine which parameters might be added to the model to improve model fit.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Modification Indices for Regressions( 1 );
```

#### [Modification Indices for Variances](#modification-indices-for-variances)[](#modification-indices-for-variances "Click to copy url")

**Syntax:** obj \<\< Modification Indices for Variances( state=0\|1 )

**Description:** Shows or hides a report that contains the estimates of model modification indices. These values can be used to determine which parameters might be added to the model to improve model fit.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Linear Growth Model" ),
        New Latent( "Intercept", "Slope" ),
        Means( {"Constant", {"Intercept", "Slope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}, {.25}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}, {.25}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}, {.25}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}, {.25}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}}
        ),
        Covariances( {"Intercept", {"Slope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
obj << Modification Indices for Variances( 1 );
```

#### [New Latent](#new-latent)[](#new-latent "Click to copy url")

**Syntax:** obj \<\< New Latent

**Description:** Adds a new latent variable in the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Model Specification(
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        )
    )
);
```

#### [Normalized Residuals](#normalized-residuals)[](#normalized-residuals "Click to copy url")

**Syntax:** obj \<\< Normalized Residuals( state=0\|1 )

**Description:** Shows or hides a report that contains a matrix of the normalized residuals for the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Normalized Residuals( 1 );
```

#### [Normalized Residuals Heat Map](#normalized-residuals-heat-map)[](#normalized-residuals-heat-map "Click to copy url")

**Syntax:** obj \<\< Normalized Residuals Heat Map( state=0\|1 )

**Description:** Shows or hides a report that contains a heat map of the normalized residuals for the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Normalized Residuals Heat Map( 1 );
```

#### [Parameter Estimates](#parameter-estimates)[](#parameter-estimates "Click to copy url")

**Syntax:** obj \<\< Parameter Estimates( state=0\|1 )

**Description:** Shows or hides a report that contains the unstandardized parameter estimates for the model. On by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Parameter Estimates( 0 );
```

#### [Paste Diagram Properties](#paste-diagram-properties_1)[](#paste-diagram-properties_1 "Click to copy url")

**Syntax:** obj \<\< Paste Diagram Properties

**Description:** Pastes the path diagram properties from the clipboard into the current SEM path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
dt2 = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt2 << Run Script( "SEM: Compare Growth Trajectories" );
obj << Copy Diagram Properties();
obj2 = dt << Structural Equation Models( Model Variables( 2 :: 12 ) );
obj2 << Paste Diagram Properties();
```

#### [Path Diagram Properties](#path-diagram-properties_1)[](#path-diagram-properties_1 "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables(
        :Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
        :Multiple Choice Year4
    ),
    Fit(
        Model Name( "Linear Growth Model" ),
        New Latent( "Intercept", "Slope" ),
        Means( {"Constant", {"Intercept", "Slope"}} ),
        Loadings(
            {"Intercept", {:Multiple Choice Year1, :Multiple Choice Year2,
            :Multiple Choice Year3, :Multiple Choice Year4}, {1, 1, 1, 1}},
            {"Slope", {:Multiple Choice Year1, :Multiple Choice Year2, :Multiple Choice Year3,
            :Multiple Choice Year4}, {0, 1, 2, 3}}
        ),
        Variances(
            {:Multiple Choice Year1, {:Multiple Choice Year1}, {"b1"}},
            {:Multiple Choice Year2, {:Multiple Choice Year2}, {"b1"}},
            {:Multiple Choice Year3, {:Multiple Choice Year3}, {"b1"}},
            {:Multiple Choice Year4, {:Multiple Choice Year4}, {"b1"}},
            {"Intercept", {"Intercept"}},
            {"Slope", {"Slope"}}
        ),
        Covariances( {"Intercept", {"Slope"}} ),
        Path Diagram Properties( Show Means( 1 ) )
    )
);
```

#### [Predicted Values Plot](#predicted-values-plot)[](#predicted-values-plot "Click to copy url")

**Syntax:** obj \<\< Predicted Values Plot( state=0\|1 )

**Description:** Shows or hides a plot of predicted values for endogenous variables in the model.

**JMP Version Added:** 17

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Run Script( "SEM: LGC with LDF" );
obj << Predicted Values Plot( 1, 1 );
```

#### [Prediction Profiler](#prediction-profiler)[](#prediction-profiler "Click to copy url")

**Syntax:** obj \<\< Prediction Profiler

**Description:** Shows or hides a prediction profiler for the selected outcomes given the selected predictors and the specified model.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Run Script( "SEM: Path Analysis w / Latent" );
obj << Prediction Profiler(
    1,
    Confidence Intervals( 1 ),
    Term Value( Leadership( 0, Lock( 0 ), Show( 1 ) ), Conflict( 0, Lock( 0 ), Show( 1 ) ) ),
    Y Terms( Conflict, Satisfaction )
);
```

#### [R Square for Endogenous Variables](#r-square-for-endogenous-variables)[](#r-square-for-endogenous-variables "Click to copy url")

**Syntax:** obj \<\< R Square for Endogenous Variables( state=0\|1 )

**Description:** Shows or hides a report with RSquare values for all endogenous variables in the model.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << R Square for Endogenous Variables( 1 );
```

#### [RAM Matrices](#ram-matrices)[](#ram-matrices "Click to copy url")

**Syntax:** obj \<\< RAM Matrices( state=0\|1 )

**Description:** Shows or hides a report that contains the model matrices used in reticular action model (RAM) notation.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << RAM Matrices( 1 );
```

#### [Recall in Model Specification](#recall-in-model-specification)[](#recall-in-model-specification "Click to copy url")

**Syntax:** obj \<\< Recall in Model Specification

**Description:** Sets the model in the Model Specification report to the specified model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Recall in Model Specification( 1 );
```

#### [Regressions](#regressions)[](#regressions "Click to copy url")

**Syntax:** obj \<\< Regressions

**Description:** Adds regression paths to the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Regressions( {:Leadership_Avg, {:Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

#### [Remove Fit](#remove-fit)[](#remove-fit "Click to copy url")

**Syntax:** obj \<\< Remove Fit

**Description:** Removes the specified model report from the report window.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Remove Fit( 1 );
```

#### [Residuals](#residuals)[](#residuals "Click to copy url")

**Syntax:** obj \<\< Residuals( state=0\|1 )

**Description:** Shows or hides a report that contains a matrix of the residuals for the model. This matrix is the difference between the model implied covariance matrix and the sample covariance matrix.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Residuals( 1 );
```

#### [Save Bartlett Factor Scores](#save-bartlett-factor-scores)[](#save-bartlett-factor-scores "Click to copy url")

**Syntax:** obj \<\< Save Bartlett Factor Scores

**Description:** Saves a column with the factor score for each variable to columns in the data table. The factor scores are calculated in a hidden column that is also added to the data table. Bartlett's method is used to estimate these scores.

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Save Bartlett Factor Scores();
```

#### [Save Factor Scores](#save-factor-scores)[](#save-factor-scores "Click to copy url")

**Syntax:** obj \<\< Save Factor Scores

**Description:** Saves a column with the factor score for each variable to columns in the data table. The factor scores are calculated in a hidden column that is also added to the data table. The regression method is used to estimate these scores.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Save Factor Scores();
```

#### [Save Observational Residuals](#save-observational-residuals)[](#save-observational-residuals "Click to copy url")

**Syntax:** obj \<\< Save Observational Residuals

**Description:** Saves columns to the data table that contain residual values of the observed outcomes in the model.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Save Observational Residuals();
```

#### [Save Prediction Formulas](#save-prediction-formulas)[](#save-prediction-formulas "Click to copy url")

**Syntax:** obj \<\< Save Prediction Formulas

**Description:** Saves columns to the data table that contain formulas for predicted values of the observed outcomes in the model.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Save Prediction Formulas();
```

#### [Show Path Diagram](#show-path-diagram)[](#show-path-diagram "Click to copy url")

**Syntax:** obj \<\< Show Path Diagram( state=0\|1 )

**Description:** Shows or hides the SEM path diagram. On by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Show Path Diagram( 0 );
```

#### [Specific Indirect Effects](#specific-indirect-effects)[](#specific-indirect-effects "Click to copy url")

**Syntax:** obj \<\< Specific Indirect Effects

**Description:** Enables you to indicate the specific indirect effects to estimate from the model.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Specific Indirect Effects( {"Ind60", "Dem65"} );
```

#### [Standardized Parameter Estimates](#standardized-parameter-estimates)[](#standardized-parameter-estimates "Click to copy url")

**Syntax:** obj \<\< Standardized Parameter Estimates( state=0\|1 )

**Description:** Shows or hides a report that contains the standardized parameter estimates for the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Standardized Parameter Estimates( 1 );
```

#### [Summary of Fit](#summary-of-fit)[](#summary-of-fit "Click to copy url")

**Syntax:** obj \<\< Summary of Fit( state=0\|1 )

**Description:** Shows or hides a report that contains details of the model fit. On by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Summary of Fit( 0 );
```

#### [Total Effects](#total-effects)[](#total-effects "Click to copy url")

**Syntax:** obj \<\< Total Effects( state=0\|1 )

**Description:** Shows or hides all available total effects in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Total Effects( 1 );
```

#### [Variances](#variances)[](#variances "Click to copy url")

**Syntax:** obj \<\< Variances

**Description:** Adds variances to the variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Model Specification(
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}}
        )
    )
);
```

## [Structural Equation Models Path Diagram](#structural-equation-models-path-diagram)[](#structural-equation-models-path-diagram "Click to copy url")

### [Associated Constructors](#associated-constructors_1)[](#associated-constructors_1 "Click to copy url")

#### [SEM Node Graph Display](#sem-node-graph-display)[](#sem-node-graph-display "Click to copy url")

**Syntax:** SEM Node Graph Display

### [Item Messages](#item-messages_4)[](#item-messages_4 "Click to copy url")

#### [Constant Border Color](#constant-border-color)[](#constant-border-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Constant Border Color ( color ) );

**Description:** Modifies the border color of Constant variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Means( 1 ), Constant Border Color( "Blue" ) );
```

#### [Constant Fill Color](#constant-fill-color)[](#constant-fill-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Constant Fill Color ( color ) );

**Description:** Modifies the fill color of Constant variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Means( 1 ), Constant Fill Color( "Blue" ) );
```

#### [Constant Font](#constant-font)[](#constant-font "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Constant Font ( font ) );

**Description:** Modifies the font of Manifest variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Means( 1 ), Constant Font( "Sitka Small" ) );
```

#### [Constant Height](#constant-height)[](#constant-height "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Constant Height ( number ) );

**Description:** Modifies the height (pixels) of Constant variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Means( 1 ), Constant Height( 20 ) );
```

#### [Constant Shape](#constant-shape)[](#constant-shape "Click to copy url")

**Syntax:** obj \<\< Constant Shape

**Description:** Modifies the default appearance of the Constant in the path diagram, which is used to represent variables' means and intercepts.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties(
    Show Means( 1 ),
    Constant Shape( {Fill Color( "Medium Light BlueCyan" ), Width( 80 ), Height( 40 )} )
);
```

#### [Constant Size Option](#constant-size-option)[](#constant-size-option "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Constant Size Option ( \<Default \| Scale To Text \| Custom\> ) );

**Description:** Changes the size mode for the Constant in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Constant Size Option( "Scale To Text" ) );
```

#### [Constant Text Color](#constant-text-color)[](#constant-text-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Constant Text Color ( color ) );

**Description:** Modifies the text color of Constant variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Means( 1 ), Constant Text Color( "Blue" ) );
```

#### [Constant Width](#constant-width)[](#constant-width "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Constant Width ( number ) );

**Description:** Modifies the width (pixels) of Constant variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Means( 1 ), Constant Width( 71 ) );
```

#### [Copy Diagram](#copy-diagram)[](#copy-diagram "Click to copy url")

**Syntax:** obj \<\< Copy Diagram

**Description:** Saves a picture of the diagram window to the clipboard.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
rpt = obj << Report();
rpt[Node Graph Box( 1 )] << Copy Diagram;
```

#### [Copy Diagram Properties](#copy-diagram-properties_2)[](#copy-diagram-properties_2 "Click to copy url")

**Syntax:** obj \<\< Copy Diagram Properties

**Description:** Saves a copy of the diagram-specific script settings to the clipboard. These settings can then be applied to other diagrams.

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
rpt = obj << Report();
diagram = rpt[Node Graph Box( 1 )];
diagram << Latent Fill Color( "Blue" );
diagram << Paths Color( "Green" );
diagram << Copy Diagram Properties;
obj = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" ) <<
Run Script( "SEM: Path Analysis w/ Latent" );
rpt = obj << Report();
other_diagram = rpt[Node Graph Box( 1 )];
other_diagram << Paste Diagram Properties;
```

#### [Dashed Lines for Nonsignificant p-values](#dashed-lines-for-nonsignificant-p-values)[](#dashed-lines-for-nonsignificant-p-values "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties ("Dashed Lines for Nonsignificant p - values"n( 0 \| 1 ) )

**Description:** Shows or hides dashed lines for paths with non-significant p-values. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( "Dashed Lines for Nonsignificant p - values"n( 0 ) );
```

#### [Diagram Size](#diagram-size)[](#diagram-size "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Diagram Size ( {x, y} ) )

**Description:** Changes the size of the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties(
    Place Nodes(
        {{"Energy60", 88, 184}, {"Fair60", 374, 94}, {"Fair65", 660, 184}, {"FrOpp60", 301,
        94}, {"FrOpp65", 587, 184}, {"FrPress60", 229, 94}, {"FrPress65", 515, 184},
        {"Labor60", 161, 184}, {"Legis60", 447, 94}, {"Legis65", 732, 184}, {"Prod60", 16,
        184}}
    ),
    Rotate Loops(
        {{"Dem60", 1.571}, {"Dem65", 1.571}, {"Energy60", 4.712}, {"Fair60", 4.712},
        {"Fair65", 4.712}, {"FrOpp60", 4.712}, {"FrOpp65", 4.712}, {"FrPress60", 4.712},
        {"FrPress65", 4.712}, {"Ind60", 1.571}, {"Labor60", 4.712}, {"Legis60", 4.712},
        {"Legis65", 4.712}, {"Prod60", 4.712}}
    )
);
```

#### [Enable Grid](#enable-grid)[](#enable-grid "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties ( Enable Grid( 0\|1) )

**Description:** Enables a visual grid in the Path Diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Enable Grid( 1 ) );
```

#### [Fill Nodes With R Squared](#fill-nodes-with-r-squared)[](#fill-nodes-with-r-squared "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties ( Fill Nodes With R Squared ( 0\|1) )

**Description:** Specifies that nodes in the fitted model be partially filled based on their estimated coefficient of determination. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Fill Nodes With R Squared( 1 ) );
```

#### [Latent Border Color](#latent-border-color)[](#latent-border-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Latent Border Color ( color ) );

**Description:** Modifies the border color of Latent variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Latent Border Color( "Blue" ) );
```

#### [Latent Fill Color](#latent-fill-color)[](#latent-fill-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Latent Fill Color ( color ) );

**Description:** Modifies the fill color of Latent variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Latent Fill Color( "Blue" ) );
```

#### [Latent Font](#latent-font)[](#latent-font "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Font ( font ) );

**Description:** Modifies the font of Latent variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Latent Font( "Sitka Small" ) );
```

#### [Latent Height](#latent-height)[](#latent-height "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Latent Height ( number ) );

**Description:** Modifies the height (pixels) of Latent variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Latent Height( 30 ) );
```

#### [Latent Shape](#latent-shape)[](#latent-shape "Click to copy url")

**Syntax:** obj \<\< Latent Shape

**Description:** Modifies the default appearance of Latent Variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties(
    Latent Shape( {Fill Color( "Medium Light BlueCyan" ), Width( 80 ), Height( 40 )} )
);
```

#### [Latent Size Option](#latent-size-option)[](#latent-size-option "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Latent Size Option ( \<Default \| Scale To Text \| Custom\> ) );

**Description:** Changes the size mode for Latent nodes in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Latent Size Option( "Scale To Text" ) );
```

#### [Latent Text Color](#latent-text-color)[](#latent-text-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Latent Text Color ( color ) );

**Description:** Modifies the text color of Latent variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Latent Text Color( "Blue" ) );
```

#### [Latent Width](#latent-width)[](#latent-width "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Latent Width ( number ) );

**Description:** Modifies the width (pixels) of Latent variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Latent Width( 71 ) );
```

#### [Layout](#layout)[](#layout "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties ( Layout("Left To Right"\|"Top To Bottom") )

**Description:** Sets the initial layout of the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Layout( "Top To Bottom" ) );
```

#### [Lock Diagram](#lock-diagram)[](#lock-diagram "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties ( Lock Diagram( 0\|1) )

**Description:** Locks the Path Diagram so that modifications to the model do not cause the layout to change.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Lock Diagram( 1 ) );
```

#### [Manifest Border Color](#manifest-border-color)[](#manifest-border-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Border Color ( color ) );

**Description:** Modifies the border color of Manifest variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Border Color( "Blue" ) );
```

#### [Manifest Fill Color](#manifest-fill-color)[](#manifest-fill-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Fill Color ( color ) );

**Description:** Modifies the fill color of Manifest variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Fill Color( "Blue" ) );
```

#### [Manifest Font](#manifest-font)[](#manifest-font "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Font ( font ) );

**Description:** Modifies the font of Manifest variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Font( "Sitka Small" ) );
```

#### [Manifest Height](#manifest-height)[](#manifest-height "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Height ( number ) );

**Description:** Modifies the height (pixels) of Manifest variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Height( 30 ) );
```

#### [Manifest Shape](#manifest-shape)[](#manifest-shape "Click to copy url")

**Syntax:** obj \<\< Manifest Shape

**Description:** Modifies the default appearance of Manifest Variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Shape( {Fill Color( "Green" )} ) );
```

#### [Manifest Size Option](#manifest-size-option)[](#manifest-size-option "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Size Option ( \<Default \| Scale To Text \| Custom\> ) );

**Description:** Changes the size mode for Manifest Nodes in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Size Option( "Scale To Text" ) );
```

#### [Manifest Text Color](#manifest-text-color)[](#manifest-text-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Text Color ( color ) );

**Description:** Modifies the text color of Manifest variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Text Color( "Blue" ) );
```

#### [Manifest Width](#manifest-width)[](#manifest-width "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Manifest Width ( number ) );

**Description:** Modifies the width (pixels) of Manifest variables in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Manifest Width( 67 ) );
```

#### [Paste Diagram Properties](#paste-diagram-properties_2)[](#paste-diagram-properties_2 "Click to copy url")

**Syntax:** obj \<\< Paste Diagram Properties

**Description:** Pastes a copy of the diagram-specific script settings from the clipboard.

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
rpt = obj << Report();
diagram = rpt[Node Graph Box( 1 )];
diagram << Latent Fill Color( "Blue" );
diagram << Paths Color( "Green" );
diagram << Copy Diagram Properties;
obj = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" ) <<
Run Script( "SEM: Path Analysis w/ Latent" );
rpt = obj << Report();
other_diagram = rpt[Node Graph Box( 1 )];
other_diagram << Paste Diagram Properties;
```

#### [Path Styles](#path-styles)[](#path-styles "Click to copy url")

**Syntax:** obj \<\< Path Styles

**Description:** Modifies the default appearance of paths in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Path Styles( {Color( "Green" )} ) );
```

#### [Path Thickness](#path-thickness)[](#path-thickness "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties (Path Thickness( "Fixed"\|"Map to Stdz. Estimates" ) )

**Description:** Toggles whether the thickness of paths in the diagram is kept at a fixed value or is tied to the strength of its standardized estimate. "Fixed" by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Path Thickness( "Map to Stdz. Estimates" ) );
```

#### [Path Transparency](#path-transparency)[](#path-transparency "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties (Path Transparency( "Fixed"\|"Map to Stdz. Estimates" ) )

**Description:** Toggles whether the transparency of paths in the diagram is kept at a fixed value or is tied to the strength of its standardized estimate.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Path Transparency( "Fixed" ) );
```

#### [Paths Alpha Level](#paths-alpha-level)[](#paths-alpha-level "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Paths Alpha Level ( number) );

**Description:** Modifies the minimum p-value threshold for using dashed-lines in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Paths Alpha Level( 0.01 ) );
```

#### [Paths Color](#paths-color)[](#paths-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Paths Color ( color) );

**Description:** Modifies the color of paths in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Paths Color( "Green" ) );
```

#### [Paths Font](#paths-font)[](#paths-font "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Paths Font ( font ) );

**Description:** Modifies the font used for labeling the paths in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Paths Font( "Segoe Script", 12, "Bold" ) );
```

#### [Paths Opacity](#paths-opacity)[](#paths-opacity "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Paths Opacity ( number) );

**Description:** Modifies the opacity of paths in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Paths Opacity( 0.5 ), Path Transparency( "Fixed" ) );
```

#### [Paths Thickness](#paths-thickness)[](#paths-thickness "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Paths Thickness ( number) );

**Description:** Modifies the thickness of paths in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Paths Thickness( 2.7103 ) );
```

#### [Place Nodes](#place-nodes)[](#place-nodes "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Place Nodes ( { {name1, x1, y1}, {name2, x2, y2}, ...} ) )

**Description:** Controls the placement of individual nodes in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties(
    Place Nodes(
        {{"Energy60", 88, 184}, {"Fair60", 374, 94}, {"Fair65", 660, 184}, {"FrOpp60", 301,
        94}, {"FrOpp65", 587, 184}, {"FrPress60", 229, 94}, {"FrPress65", 515, 184},
        {"Labor60", 161, 184}, {"Legis60", 447, 94}, {"Legis65", 732, 184}, {"Prod60", 16,
        184}}
    ),
    Rotate Loops(
        {{"Dem60", 1.571}, {"Dem65", 1.571}, {"Energy60", 4.712}, {"Fair60", 4.712},
        {"Fair65", 4.712}, {"FrOpp60", 4.712}, {"FrOpp65", 4.712}, {"FrPress60", 4.712},
        {"FrPress65", 4.712}, {"Ind60", 1.571}, {"Labor60", 4.712}, {"Legis60", 4.712},
        {"Legis65", 4.712}, {"Prod60", 4.712}}
    )
);
```

#### [R2 Fill Color](#r2-fill-color)[](#r2-fill-color "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties ( R2 Fill Color ( Color ) )

**Description:** Specifies the color for the partial fill that represents a variable's estimated R-square value.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( R2 Fill Color( Cyan ) );
```

#### [Rotate Latent Groups](#rotate-latent-groups)[](#rotate-latent-groups "Click to copy url")

**Syntax:** obj \<\< Rotate Latent Groups

**Description:** Rotates the orientation of all latent indicators in the diagram. If any latent groups are selected, this option rotates the orientation of only the selected latent groups.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
rpt = obj << Report();
diagram = rpt[Node Graph Box( 1 )];
diagram << Rotate Latent Groups;
```

#### [Rotate Loops](#rotate-loops)[](#rotate-loops "Click to copy url")

**Syntax:** obj \<\< Path Diagram Properties( Rotate Loops ( { {name1, angle1}, {name2, angle2}, ...} ) )

**Description:** Controls the rotation of variance loops within the path diagram. Angles are measured clockwise in radians.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties(
    Place Nodes(
        {{"Energy60", 88, 184}, {"Fair60", 374, 94}, {"Fair65", 660, 184}, {"FrOpp60", 301,
        94}, {"FrOpp65", 587, 184}, {"FrPress60", 229, 94}, {"FrPress65", 515, 184},
        {"Labor60", 161, 184}, {"Legis60", 447, 94}, {"Legis65", 732, 184}, {"Prod60", 16,
        184}}
    ),
    Rotate Loops(
        {{"Dem60", 1.571}, {"Dem65", 1.571}, {"Energy60", 4.712}, {"Fair60", 4.712},
        {"Fair65", 4.712}, {"FrOpp60", 4.712}, {"FrOpp65", 4.712}, {"FrPress60", 4.712},
        {"FrPress65", 4.712}, {"Ind60", 1.571}, {"Labor60", 4.712}, {"Legis60", 4.712},
        {"Legis65", 4.712}, {"Prod60", 4.712}}
    )
);
```

#### [Show Constant Mean Square](#show-constant-mean-square)[](#show-constant-mean-square "Click to copy url")

**Syntax:** obj \<\< Show Constant Mean Square( state=0\|1 )

**Description:** Shows or hides the edge associated with the constant in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Constant Mean Square( 1 ) );
```

#### [Show Covariances](#show-covariances)[](#show-covariances "Click to copy url")

**Syntax:** obj \<\< Show Covariances( state=0\|1 )

**Description:** Shows or hides the bidirectional arrows that represent covariances in the path diagram. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Covariances( 0 ) );
```

#### [Show Equality Constraints](#show-equality-constraints)[](#show-equality-constraints "Click to copy url")

**Syntax:** obj \<\< Show Equality Constraints( state=0\|1 )

**Description:** Shows or hides the equality constraints (Fixed Values or Labels) on edges in the path diagram. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Equality Constraints( 0 ) );
```

#### [Show Estimates](#show-estimates)[](#show-estimates "Click to copy url")

**Syntax:** obj \<\< Show Estimates( "Unstandardized"\|"Standardized"\|"None" )

**Description:** Shows or hides the unstandardized parameter estimates in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Estimates( "None" ) );
```

#### [Show Loadings](#show-loadings)[](#show-loadings "Click to copy url")

**Syntax:** obj \<\< Show Loadings( state=0\|1 )

**Description:** Shows or hides the latent variable indicators in the path diagram. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Loadings( 0 ) );
```

#### [Show Means/Intercepts](#show-meansintercepts)[](#show-meansintercepts "Click to copy url")

**Syntax:** obj \<\< Show Means/Intercepts( state=0\|1 )

**Description:** Shows or hides the means in the SEM Platform.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Means( 1 ) );
```

#### [Show R Squared Values](#show-r-squared-values)[](#show-r-squared-values "Click to copy url")

**Syntax:** obj \<\< Show R Squared Values( state=0\|1 )

**Description:** Shows or hides the R-square values inside the nodes in the path diagram.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show R Squared Values( 1 ) );
```

#### [Show Regressions](#show-regressions)[](#show-regressions "Click to copy url")

**Syntax:** obj \<\< Show Regressions( state=0\|1 )

**Description:** Shows or hides regressions in the SEM Platform. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Regressions( 0 ) );
```

#### [Show Variances](#show-variances)[](#show-variances "Click to copy url")

**Syntax:** obj \<\< Show Variances( state=0\|1 )

**Description:** Shows or hides the bidirectional arrows that represent variances in the path diagram. On by default.

**JMP Version Added:** 16

``` jsl
dt = Open( "$SAMPLE_DATA/Political Democracy.jmp" );
obj = dt << Run Script( "SEM: Bollen (1989)" );
obj << Path Diagram Properties( Show Variances( 0 ) );
```

## [Structural Equation Models Specification](#structural-equation-models-specification)[](#structural-equation-models-specification "Click to copy url")

### [Item Messages](#item-messages_5)[](#item-messages_5 "Click to copy url")

#### [Covariances](#covariances_1)[](#covariances_1 "Click to copy url")

**Syntax:** obj \<\< Covariances

**Description:** Adds covariances between variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Covariances( {:Leadership_Avg, {:Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

#### [Define Time Values](#define-time-values_1)[](#define-time-values_1 "Click to copy url")

**Syntax:** obj \<\< Define Time Values

**Description:** Defines the occasions of measurement for the repeated observations. These values are used for specifying longitudinal models.

**JMP Version Added:** 18

``` jsl
dt = Open( "$SAMPLE_DATA/Academic Achievement.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Multiple Choice Year1, :Multiple Choice Year3, :Multiple Choice Year4 ),
    Model Specification(
        Model Name( "Longitudinal Model" ),
        Define Time Values( {0, 2, 3} )
    )
);
```

#### [Loadings](#loadings_1)[](#loadings_1 "Click to copy url")

**Syntax:** obj \<\< Loadings

**Description:** Adds loadings to latent variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Fit(
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        )
    )
);
```

#### [Max Iterations](#max-iterations)[](#max-iterations "Click to copy url")

**Syntax:** Structural Equation Models(..., Max Iterations( 3 )

**Description:** Sets the maximum number of iterations for convergence. "1000" by default.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Covariances( {:Leadership_Avg, {:Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} ),
        Max Iterations( 3 )
    )
);
```

#### [Means/Intercepts](#meansintercepts_1)[](#meansintercepts_1 "Click to copy url")

**Syntax:** obj \<\< Means/Intercepts

**Description:** Adds means or intercepts to the variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Model Specification(
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}}
        )
    )
);
```

#### [Model Name](#model-name_1)[](#model-name_1 "Click to copy url")

**Syntax:** obj \<\< Model Name

**Description:** Specifies a name for the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Model Name( "Means and Variances Model" ),
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

#### [Model Notes](#model-notes)[](#model-notes "Click to copy url")

**Syntax:** obj \<\< Model Notes

**Description:** Specifies notes for the model.

**JMP Version Added:** 19

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Model Name( "Means and Variances Model" ),
        Model Notes(
            "This is a simple model with only means and variances for each variable"
        ),
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

#### [New Latent](#new-latent_1)[](#new-latent_1 "Click to copy url")

**Syntax:** obj \<\< New Latent

**Description:** Adds a new latent variable in the model.

**JMP Version Added:** 15

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Model Specification(
        New Latent( "Leader" ),
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Loadings( {"Leader", {:Support_L, :Goal_L, :Work_L, :Interact_L}, {1}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}},
            {"Leader", {"Leader"}}
        )
    )
);
```

#### [Regressions](#regressions_1)[](#regressions_1 "Click to copy url")

**Syntax:** obj \<\< Regressions

**Description:** Adds regression paths to the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Leadership_Avg, :Conflict_Avg ),
    Model Specification(
        Means( {"Constant", {:Leadership_Avg, :Conflict_Avg}} ),
        Regressions( {:Leadership_Avg, {:Conflict_Avg}} ),
        Variances( {:Leadership_Avg, {:Leadership_Avg}}, {:Conflict_Avg, {:Conflict_Avg}} )
    )
);
```

#### [Variances](#variances_1)[](#variances_1 "Click to copy url")

**Syntax:** obj \<\< Variances

**Description:** Adds variances to the variables in the model.

``` jsl
dt = Open( "$SAMPLE_DATA/Job Satisfaction.jmp" );
obj = dt << Structural Equation Models(
    Model Variables( :Support_L, :Goal_L, :Work_L, :Interact_L ),
    Model Specification(
        Means( {"Constant", {:Support_L, :Goal_L, :Work_L, :Interact_L}} ),
        Variances(
            {:Support_L, {:Support_L}},
            {:Goal_L, {:Goal_L}},
            {:Work_L, {:Work_L}},
            {:Interact_L, {:Interact_L}}
        )
    )
);
```

[ Previous](Socket.html "Socket") [Next ](Support%20Vector%20Machines.html "Support Vector Machines")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
