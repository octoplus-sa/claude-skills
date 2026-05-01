# Tabulate

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Tabulate.html](https://jsl.jmp.com/All%20Categories/Objects/Tabulate.html)*

---

# [Tabulate](#tabulate)[](#tabulate "Click to copy url")

## [Associated Constructors](#associated-constructors)[](#associated-constructors "Click to copy url")

### [Tabulate](#tabulate_1)[](#tabulate_1 "Click to copy url")

**Syntax:** Tabulate( Add Table( Column Table( Analysis Columns( column(s) )\|Grouping Columns( column(s))\|Statistics( )), Row Table( Analysis Columns( column(s) )\|Grouping Columns( column(s))\|Statistics( )) )

**Description:** Creates a custom table of summary statistics of one or more variables. The variables can be grouped by one or more classification columns. Enables you to build the summary table using drag and drop operations.

#### [Categories and stats](#categories-and-stats)[](#categories-and-stats "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :gender, :goals ), Statistics( N, Column % ) ),
        Row Table( Grouping Columns( :Grade, :Age ) )
    )
);
```

#### [Columns by Categories](#columns-by-categories)[](#columns-by-categories "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Columns by Categories( :Grades, :Sports, :Looks, :Money ) ) )
);
```

#### [Frequency](#frequency)[](#frequency "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Freq( :Count ),
    Add Table( Row Table( Grouping Columns( :Causes ) ) )
);
```

#### [ID column](#id-column)[](#id-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    ID( :Division ),
    Set Format( Uniform Format( 10, 2 ) ),
    Add Table(
        Column Table(
            Statistics( Sum ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name ) )
    )
);
```

#### [Multiple response grouping columns](#multiple-response-grouping-columns)[](#multiple-response-grouping-columns "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Consumer Preferences.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :Floss Delimited ), Statistics( N, "% of Total"n ) ),
        Row Table( Grouping Columns( :Frequency of Teeth Cleaning, :Brush Delimited ) )
    )
);
```

#### [Multiple response page column](#multiple-response-page-column)[](#multiple-response-page-column "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Big Class Families.jmp" );
obj = Tabulate(
    Show Control Panel( 0 ),
    Page Column( :family cars( "Jeep" ) ),
    Add Table(
        Column Table( Analysis Columns( :height ), Statistics( N, "% of Total"n ) ),
        Row Table( Grouping Columns( :sex ) )
    )
);
```

#### [Multiple row and column tables](#multiple-row-and-column-tables)[](#multiple-row-and-column-tables "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :gender ) ),
        Column Table( Grouping Columns( :race ) ),
        Row Table( Grouping Columns( :goals ) ),
        Row Table( Grouping Columns( :"Urban/Rural"n ) )
    )
);
```

#### [Multiple row tables](#multiple-row-tables)[](#multiple-row-tables "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Row Table( Grouping Columns( :Grades ) ),
        Row Table( Grouping Columns( :Sports ) ),
        Row Table( Grouping Columns( :Looks ) ),
        Row Table( Grouping Columns( :Money ) )
    )
);
```

#### [Nested categories](#nested-categories)[](#nested-categories "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
```

#### [Packed columns](#packed-columns)[](#packed-columns "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Statistics( Sum, Max ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name, :Engine ) )
    )
);
```

#### [Page column](#page-column)[](#page-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Page Column( :Engine( "Gas" ) ),
    Add Table(
        Column Table( Analysis Columns( :City MPG, :Hwy MPG ), Statistics( Max ) ),
        Row Table( Grouping Columns( :Mfr Name ) )
    )
);
```

#### [Stacked grouping columns](#stacked-grouping-columns)[](#stacked-grouping-columns "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :marital status ),
            Add Aggregate Statistics( :marital status ),
            Analysis Columns( :age ),
            Statistics( Min, Max )
        ),
        Row Table(
            Grouping Columns( :sex, :country, :size ),
            Add Aggregate Statistics( :sex, :country, :size ),
            Stack Grouping Columns( 1 )
        )
    )
);
```

#### [Weight](#weight)[](#weight "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Physical Data.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Weight( :Weight ),
    Add Table(
        Column Table( Analysis Columns( :Horsepower ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Type ) )
    )
);
```

## [Columns](#columns)[](#columns "Click to copy url")

### [Analysis Columns](#analysis-columns)[](#analysis-columns "Click to copy url")

**Syntax:** Analysis Columns( Column(s) )

**Description:** Adds analysis columns to the current table. It can be used with the Add Table command or Modify Table command.

#### [Add to existing](#add-to-existing)[](#add-to-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
obj << Modify Table( Column Table( 1 ), Analysis Columns( :CO ) );
```

#### [Add to new](#add-to-new)[](#add-to-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
```

### [By](#by)[](#by "Click to copy url")

**Syntax:** obj \<\< By( column(s) )

**Description:** Performs a separate analysis for each level of the specified column.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    ),
    By( :type )
);
```

### [Columns by Categories](#columns-by-categories_1)[](#columns-by-categories_1 "Click to copy url")

**Syntax:** Columns by Categories( column1, column2, ...) )

**Description:** Adds a cross-tabulation of the column names and the categories gathered for columns with similar values to the table. When scripting, the Columns by Categories message must be within either a Column Table message or a Row Table message.

#### [Add to existing](#add-to-existing_1)[](#add-to-existing_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Columns by Categories( :Grades, :Sports, :Looks ) ) )
);
obj << Modify Table( Row Table( 1 ), Columns by Categories( :Money ) );
```

#### [Add to new](#add-to-new_1)[](#add-to-new_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Children's Popularity.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Columns by Categories( :Grades, :Sports, :Looks, :Money ) ) )
);
```

### [Freq](#freq)[](#freq "Click to copy url")

**Syntax:** Freq( Column )

**Description:** Specify the frequency column to be used in computing for statistics

#### [Set in existing](#set-in-existing)[](#set-in-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Grouping Columns( :Causes ) ) )
);
Wait( 1 );
obj << Freq( :Count );
```

#### [Set in new](#set-in-new)[](#set-in-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Quality Control/Failures.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Freq( :Count ),
    Add Table( Row Table( Grouping Columns( :Causes ) ) )
);
```

### [Grouping Columns](#grouping-columns)[](#grouping-columns "Click to copy url")

**Syntax:** Grouping Columns( Column(s) )

**Description:** Adds grouping columns to the current table. It can be used with the Add Table command or Modify Table command.

#### [Add nested to existing](#add-nested-to-existing)[](#add-nested-to-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate( Show Control Panel( 0 ) );
obj << Add Table( Column Table( Grouping Columns( :sex ) ) );
obj << Modify Table( Column Table( 1 ), Grouping Column( :age ) );
```

#### [Add nested to new](#add-nested-to-new)[](#add-nested-to-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
```

#### [Add to existing](#add-to-existing_2)[](#add-to-existing_2 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate( Show Control Panel( 0 ) );
obj << Add Table( Column Table( Grouping Columns( :sex ) ) );
obj << Modify Table( Row Table( 1 ), Grouping Column( :age ) );
```

#### [Add to new](#add-to-new_2)[](#add-to-new_2 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Column Table( Grouping Columns( :sex ) ) )
);
```

### [ID](#id)[](#id "Click to copy url")

**Syntax:** ID( Column )

**Description:** Specifies the identifier column that is used to count unique occurrences.

#### [Set in existing](#set-in-existing_1)[](#set-in-existing_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Set Format( Uniform Format( 10, 2 ) ),
    Add Table(
        Column Table(
            Statistics( Sum ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name ) )
    )
);
Wait( 1 );
obj << ID( :Division );
```

#### [Set in new](#set-in-new_1)[](#set-in-new_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    ID( :Division ),
    Set Format( Uniform Format( 10, 2 ) ),
    Add Table(
        Column Table(
            Statistics( Sum ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name ) )
    )
);
```

### [Page Column](#page-column_1)[](#page-column_1 "Click to copy url")

**Syntax:** Page Column( Column )

**Description:** Specify the page column to be used for setting up pages of report

#### [Multiple response page column](#multiple-response-page-column_1)[](#multiple-response-page-column_1 "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Big Class Families.jmp" );
obj = Tabulate(
    Show Control Panel( 0 ),
    Page Column( :family cars( "Jeep" ) ),
    Add Table(
        Column Table( Analysis Columns( :height ), Statistics( N, "% of Total"n ) ),
        Row Table( Grouping Columns( :sex ) )
    )
);
```

#### [Set page column and level in existing](#set-page-column-and-level-in-existing)[](#set-page-column-and-level-in-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :height, :weight ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :age ) )
    )
);
Wait( 1 );
obj << Page Column( :sex( "F" ) );
```

#### [Set page column and level in new](#set-page-column-and-level-in-new)[](#set-page-column-and-level-in-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Page Column( :sex( "F" ) ),
    Add Table(
        Column Table( Analysis Columns( :height, :weight ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :age ) )
    )
);
```

#### [Set page column in new](#set-page-column-in-new)[](#set-page-column-in-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Page Column( :sex ),
    Add Table(
        Column Table( Analysis Columns( :height, :weight ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :age ) )
    )
);
```

### [Weight](#weight_1)[](#weight_1 "Click to copy url")

**Syntax:** Weight( Column )

**Description:** Specify the weight column to be used in computing for statistics

#### [Set in existing](#set-in-existing_2)[](#set-in-existing_2 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Physical Data.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :Horsepower ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Type ) )
    )
);
Wait( 1 );
obj << Weight( :Weight );
```

#### [Set in new](#set-in-new_2)[](#set-in-new_2 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Physical Data.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Weight( :Weight ),
    Add Table(
        Column Table( Analysis Columns( :Horsepower ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Type ) )
    )
);
```

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Add](#add)[](#add "Click to copy url")

**Syntax:** add(\<Column Table \| Row Table\>(table index), \<before first \| \<before \| after\>(\<analysis column \| grouping column \| statistic\>(\<operand name \| index\>))\>, \<analysis column \| grouping column \| statistic\>(operand name)),

**Description:** Used with Modify Table to add columns and statistics to an existing table. Also serves as an alias for Add Table

#### [Add analysis column before named](#add-analysis-column-before-named)[](#add-analysis-column-before-named "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Column Table( Analysis Columns( :weight ) ) )
);
Wait( 0 );
obj << Modify Table(
    Column Table( 1 ),
    Add( Before( Analysis Columns( :weight ) ), Analysis Columns( :height ) )
);
```

#### [Add stat after named](#add-stat-after-named)[](#add-stat-after-named "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table(
    Column Table( 1 ),
    Add( After( Statistics( Max ) ), Statistics( Range ) )
);
```

#### [Add stat before first](#add-stat-before-first)[](#add-stat-before-first "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table( Column Table( 1 ), Add( Before First, Statistics( N ) ) );
```

#### [Add stat before index](#add-stat-before-index)[](#add-stat-before-index "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table(
    Column Table( 1 ),
    Add( Before( Statistics( 2 ) ), Statistics( Median ) )
);
```

### [Add Table](#add-table)[](#add-table "Click to copy url")

**Syntax:** Add Table( \<Column Table( )\>, \<Row Table( )\> )

**Description:** Adds a table to the window if there is no current table or appends a table to the existing table object.

#### [Add to empty](#add-to-empty)[](#add-to-empty "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate( Show Control Panel( 0 ) );
obj << Add Table( Column Table( Grouping Columns( :sex ) ) );
obj << Add Table( Row Table( Grouping Columns( :age ) ) );
```

#### [Add to existing](#add-to-existing_3)[](#add-to-existing_3 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Add Table( Column Table( Grouping Columns( :type ) ) );
```

### [Aggregate Statistics](#aggregate-statistics)[](#aggregate-statistics "Click to copy url")

**Syntax:** Aggregate Statistics( column )

**Description:** Adds a separate column for each level of the specified column together with a summation column to the current table. When scripting, the Aggregate Statistics message must be within either a Column Table message or a Row Table message.

#### [Set when adding to existing](#set-when-adding-to-existing)[](#set-when-adding-to-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Column Table( Analysis Columns( :OZONE ), Statistics( Mean ) ) )
);
obj << Modify Table(
    Row Table( 1 ),
    Grouping Columns( :Region ),
    Aggregate Statistics( :Region )
);
```

#### [Set when adding to new](#set-when-adding-to-new)[](#set-when-adding-to-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Region ), Aggregate Statistics( :Region ) )
    )
);
```

### [Change Item Label](#change-item-label)[](#change-item-label "Click to copy url")

**Syntax:** obj \<\< Change Item Label( Statistics( stat name, new string ) )

**Description:** Changes the label on a text entry field in the table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
obj << Change Item Label( Statistics( Mean, "Average" ) );
```

### [Delete](#delete)[](#delete "Click to copy url")

**Syntax:** delete( \<analysis columns \| grouping columns \| statistics\>(operand name, operand name, ...))

**Description:** Used with Modify Table to remove columns and statistics from an existing table.

#### [Delete named analysis column](#delete-named-analysis-column)[](#delete-named-analysis-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table( Column Table( 1 ), Delete( Analysis Columns( :Assets ) ) );
```

#### [Delete stat at index](#delete-stat-at-index)[](#delete-stat-at-index "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table( Column Table( 1 ), Delete( Statistics( 1 ) ) );
```

### [Display Column Width](#display-column-width)[](#display-column-width "Click to copy url")

**Syntax:** obj \<\< Display Column Width( Data Column( \<Column Table(n)\>, path ), \<width\> ); obj \<\< Display Column Width( Row Label( \<Row Table(n)\>, path ), \<width\> )

**Description:** Sets or returns the display width of a column in a Tabulate report table. Path is a sequence of quoted column headings that traces the path of the column. Width is the width of a column in pixels. Use Data Column to define columns in the main body of the table or Row Label for columns in the row labels area. If there are multiple tables in the report, use Column Table(n) or Row Table(n) to specify which table the path applies to. If width is not specified, this option returns the current width of the specified column.

#### [Get column width](#get-column-width)[](#get-column-width "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :sex, :marital status ),
            Analysis Columns( :age ),
            Statistics( Sum, "% of Total" )
        ),
        Row Table( Grouping Columns( :type ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Display Column Width(
    Column( Column Table( 1 ), "sex", "Female", "Marital status", "Single", "age", "Sum" )
);
```

#### [Resize data columns to equal widths](#resize-data-columns-to-equal-widths)[](#resize-data-columns-to-equal-widths "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Set Format( Mean( :OZONE( 6, 4 ) ) ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Min, Max, Mean, Std Dev ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
stats = {"Min", "Max", "Mean", "Std Dev"};
ns = N Items( stats );
a = {};
For( i = 1, i <= ns, i++,
    a[i] = obj << Display Column Width( Data Column( "OZONE", stats[i] ) )
);
amax = Max( a );
For( i = 1, i <= ns, i++,
    obj << Display Column Width( Data Column( "OZONE", stats[i] ), amax )
);
```

#### [Set row label width](#set-row-label-width)[](#set-row-label-width "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :sex, :marital status ),
            Analysis Columns( :age ),
            Statistics( Sum, "% of Total" )
        ),
        Row Table( Grouping Columns( :type ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Display Column Width( Row Label( Row Table( 2 ), "country" ), 150 );
```

### [Full Path Column Name](#full-path-column-name)[](#full-path-column-name "Click to copy url")

**Syntax:** obj \<\< Full Path Column Name( true \| false )

**Description:** If set, column name for output table should include the grouping columns name

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Full Path Column Name( 1 );
obj << Make Into Data Table;
```

### [Ignore duplicate responses](#ignore-duplicate-responses)[](#ignore-duplicate-responses "Click to copy url")

**Syntax:** obj \<\< Ignore duplicate responses( Grouping Columns( column ), true \| false )

**JMP Version Added:** 19

#### [Set in existing](#set-in-existing_3)[](#set-in-existing_3 "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Big Class Families.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :family cars ) ),
        Row Table( Grouping Columns( :sex, :age ) )
    )
);
obj << Ignore Duplicate Responses( Grouping Columns( :family cars ), 1 );
```

#### [Set in new](#set-in-new_3)[](#set-in-new_3 "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Big Class Families.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Ignore Duplicate Responses( Grouping Columns( :family cars ), 1 ),
    Add Table(
        Column Table( Grouping Columns( :family cars ) ),
        Row Table( Grouping Columns( :sex, :age ) )
    )
);
```

### [Ignore duplicates in multiple response columns](#ignore-duplicates-in-multiple-response-columns)[](#ignore-duplicates-in-multiple-response-columns "Click to copy url")

**Syntax:** obj \<\< Ignore duplicates in multiple response columns( state=0\|1 )

**Description:** Ignores duplicate responses in multiple response columns. Each repeated response is treated as a single occurrence.

**JMP Version Added:** 19

#### [Set in existing](#set-in-existing_4)[](#set-in-existing_4 "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Big Class Families.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :family cars ) ),
        Row Table( Grouping Columns( :sex, :age ) )
    )
);
obj << Ignore Duplicates In Multiple Response Columns( 1 );
```

#### [Set in new](#set-in-new_4)[](#set-in-new_4 "Click to copy url")

``` jsl
dt = Open( "$Sample_Data/Big Class Families.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Ignore Duplicates In Multiple Response Columns( 1 ),
    Add Table(
        Column Table( Grouping Columns( :family cars ) ),
        Row Table( Grouping Columns( :sex, :age ) )
    )
);
```

### [Include missing for grouping columns](#include-missing-for-grouping-columns)[](#include-missing-for-grouping-columns "Click to copy url")

**Syntax:** obj \<\< Include missing for grouping columns( state=0\|1 )

**Description:** Adds a separate column containing counts for missing values for all grouping columns in the current table.

#### [Set in existing](#set-in-existing_5)[](#set-in-existing_5 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cars.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Grouping Columns( :Doors ) ) )
);
obj << Include Missing For Grouping Columns( 1 );
```

#### [Set in new](#set-in-new_5)[](#set-in-new_5 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cars.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Include Missing For Grouping Columns( 1 ),
    Add Table( Row Table( Grouping Columns( :Doors ) ) )
);
```

### [Make Into Data Table](#make-into-data-table)[](#make-into-data-table "Click to copy url")

**Syntax:** obj \<\< Make Into Data Table( \<Invisible(bool) \| Private(bool)\>, \<Output Table( table name)\>, \<Full Path Column Name(bool)\> )

**Description:** Creates a new data table from the table created in Tabulate.

#### [Make into data table](#make-into-data-table_1)[](#make-into-data-table_1 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Make Into Data Table;
```

#### [Make into invisible data table](#make-into-invisible-data-table)[](#make-into-invisible-data-table "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Make into Data Table( Invisible( 1 ) );
```

#### [Use full path column names](#use-full-path-column-names)[](#use-full-path-column-names "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Make into Data Table( Full Path Column Name( 1 ) );
```

### [Max scroll locked columns](#max-scroll-locked-columns)[](#max-scroll-locked-columns "Click to copy url")

**Syntax:** obj \<\< Max scroll locked columns( number=3 )

**Description:** Set the maximum number of columns to be scroll locked. Either all or none of the row header columns will be locked. On by default.

**JMP Version Added:** 19

#### [Limit allows header count](#limit-allows-header-count)[](#limit-allows-header-count "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Scroll Lock Row Headers In Data Table Export( 1 );
obj << Max Scroll Locked Columns( 2 );
obj << Make Into Data Table;
```

#### [Limit under header count](#limit-under-header-count)[](#limit-under-header-count "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Scroll Lock Row Headers In Data Table Export( 1 );
obj << Max Scroll Locked Columns( 1 );
obj << Make Into Data Table;
```

### [Missing sum is zero](#missing-sum-is-zero)[](#missing-sum-is-zero "Click to copy url")

**Syntax:** obj \<\< Missing sum is zero( state=0\|1 )

**Description:** Specifies if missing values for the sum summary statistic should be displayed as 0 or missing.

#### [Set in existing](#set-in-existing_6)[](#set-in-existing_6 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :height ), Grouping Columns( :sex ) ),
        Row Table( Grouping Columns( :name ) )
    )
);
obj << Missing Sum Is Zero( 1 );
```

#### [Set in new](#set-in-new_6)[](#set-in-new_6 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Missing Sum Is Zero( 1 ),
    Add Table(
        Column Table( Analysis Columns( :height ), Grouping Columns( :sex ) ),
        Row Table( Grouping Columns( :name ) )
    )
);
```

### [Modify Table](#modify-table)[](#modify-table "Click to copy url")

**Syntax:** obj \<\< Modify Table( \<Column Table \| Row Table\>(table index), ... )

**Description:** Modifies an existing table.

#### [Build and edit full table](#build-and-edit-full-table)[](#build-and-edit-full-table "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate( Show Control Panel( 0 ) );
obj << Add Table( Column Table( Grouping Columns( :sex ) ) );
obj << Add table( Row Table( Grouping Columns( :age ) ) );
obj << Add Table( Column Table( Analysis Columns( :height ) ) );
obj << Add Table( Column Table( Analysis Columns( :weight ) ) );
obj << Modify Table( Column Table( 2 ), Statistics( Min, Max ) );
obj << Modify Table( Column Table( 2 ), Grouping Columns( :sex ) );
obj << Modify Table( Column Table( 2 ), Analysis Columns( :weight ) );
Wait( 1 );
obj << Modify Table( Column Table( 2 ), Delete( Analysis Columns( :weight ) ) );
obj << Modify Table( Column Table( 2 ), Delete( Statistics( Sum ) ) );
```

#### [Delete analysis column](#delete-analysis-column)[](#delete-analysis-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table( Column Table( 1 ), Delete( Analysis Columns( :Assets ) ) );
```

### [Modify Table Option](#modify-table-option)[](#modify-table-option "Click to copy url")

**Syntax:** obj \<\< Modify Table Option

**Description:** Used with Modify Table to modify table options in an existing table.

#### [Change stacked group label in existing](#change-stacked-group-label-in-existing)[](#change-stacked-group-label-in-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :height ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :age, :sex ), Stack Grouping Columns( 1 ) )
    )
);
obj << Modify Table(
    Row Table( 1 ),
    Modify Table Option( Change Stacked Group Label ),
    "new label"
);
```

#### [Stack grouping columns in existing](#stack-grouping-columns-in-existing)[](#stack-grouping-columns-in-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :height ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :age, :sex ) )
    )
);
obj << Modify Table( Row Table( 1 ), Modify Table Option( Stack Grouping Columns( true ) ) );
```

### [Move](#move)[](#move "Click to copy url")

**Syntax:** move(\<Column Table \| Row Table\>(table index), \<analysis column \| grouping column \| statistic\>(\<operand name \| index\>)), \<before first \| \<before \| after\>(\<analysis column \| grouping column \| statistic\>(\<operand name \| index\>)\>)

**Description:** Used with Modify Table to move columns and statistics in an existing table.

**JMP Version Added:** 19

#### [Move grouping column from column to row table](#move-grouping-column-from-column-to-row-table)[](#move-grouping-column-from-column-to-row-table "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table(
    Row Table( 1 ),
    Move( Column Table( 1 ), Grouping Column( :Type ) ),
    Before First
);
```

#### [Move stat after named](#move-stat-after-named)[](#move-stat-after-named "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Companies.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :Type ),
            Analysis Columns( :"Sales ($M)"n, :Assets ),
            Statistics( Min, Mean, Max )
        )
    )
);
Wait( 0 );
obj << Modify Table(
    Column Table( 1 ),
    Move( Column Table( 1 ), Statistics( Mean ) ),
    After( Statistics( Max ) )
);
```

### [Order By Count](#order-by-count)[](#order-by-count "Click to copy url")

**Syntax:** obj \<\< Order By Count( Grouping Columns( column ), true \| false )

#### [Set in existing](#set-in-existing_7)[](#set-in-existing_7 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Grouping Columns( :age ) ) )
);
obj << Order By Count( Grouping Columns( :age ), 1 );
```

#### [Set in new](#set-in-new_7)[](#set-in-new_7 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Order By Count( Grouping Columns( :age ), 1 ),
    Add Table( Row Table( Grouping Columns( :age ) ) )
);
```

### [Order by count of grouping columns](#order-by-count-of-grouping-columns)[](#order-by-count-of-grouping-columns "Click to copy url")

**Syntax:** obj \<\< Order by count of grouping columns( state=0\|1 )

**Description:** Sorts the levels of the grouping columns by counts in the table.

#### [Set in existing](#set-in-existing_8)[](#set-in-existing_8 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cars.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table( Row Table( Grouping Columns( :Make ) ) )
);
obj << Order by Count of Grouping Columns( 1 );
```

#### [Set in new](#set-in-new_8)[](#set-in-new_8 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cars.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Order by Count of Grouping Columns( 1 ),
    Add Table( Row Table( Grouping Columns( :Make ) ) )
);
```

### [Pack](#pack)[](#pack "Click to copy url")

**Syntax:** obj \<\< Pack( \<Analysis columns \| Statistics\>(operand name, ...), \<Template\> )

**Description:** Pack multiple statistics into one column in the table. The Template option specifies the formatting of the items.

#### [Pack analysis columns in existing](#pack-analysis-columns-in-existing)[](#pack-analysis-columns-in-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Statistics( Sum ), Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ) ),
        Row Table( Grouping Columns( :Mfr Name, :Engine ) )
    )
);
obj << Modify Table(
    Column Table( 1 ),
    Pack(
        Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
        Template( "^FIRST  (^OTHERS)", "/" )
    )
);
```

#### [Pack analysis columns in new](#pack-analysis-columns-in-new)[](#pack-analysis-columns-in-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Statistics( Sum ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack( Analysis Columns( City MPG, Hwy MPG, Comb MPG ) )
        ),
        Row Table( Grouping Columns( :Mfr Name, :Engine ) )
    )
);
```

#### [Pack analysis columns in new with template](#pack-analysis-columns-in-new-with-template)[](#pack-analysis-columns-in-new-with-template "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Statistics( Sum ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name, :Engine ) )
    )
);
```

### [Plot Scale](#plot-scale)[](#plot-scale "Click to copy url")

**Syntax:** obj \<\< Plot Scale( min, max )

**Description:** Sets the scale on the bar chart.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Show Chart( 1 );
Wait( 2 );
obj << Plot Scale( 0, 25 );
```

### [Remove Column Label](#remove-column-label)[](#remove-column-label "Click to copy url")

**Syntax:** obj \<\< Remove Column Label( Grouping Columns( column ) )

**Description:** Removes the specified column label in the table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :Region ) ),
        Row Table( Analysis Columns( :OZONE, :CO, :NO, :SO2 ), Statistics( Mean ) )
    )
);
Wait( 2 );
obj << Remove Column Label( Grouping Columns( :Region ) );
```

### [Restore Column Label](#restore-column-label)[](#restore-column-label "Click to copy url")

**Syntax:** obj \<\< Restore Column Label( Grouping Columns( column ) )

**Description:** Restores the previously removed, specified column label in the table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :Region ) ),
        Row Table( Analysis Columns( :OZONE, :CO, :NO, :SO2 ), Statistics( Mean ) )
    )
);
obj << Remove Column Label( Grouping Columns( :Region ) );
Wait( 2 );
obj << Restore Column Label( Grouping Columns( :Region ) );
```

### [Retype](#retype)[](#retype "Click to copy url")

**Syntax:** Retype( \<Analysis Columns \| Grouping Columns\>( operand name, ... ), \<Analysis Column \| Gropuing Column\> )

**Description:** Used with Modify Table to convert between analysis columns and grouping columns in an existing table.

**JMP Version Added:** 19

#### [Change analysis column to grouping column](#change-analysis-column-to-grouping-column)[](#change-analysis-column-to-grouping-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Statistics( N ), Analysis Columns( :age ) ),
        Row Table( Grouping Columns( :sex ) )
    )
);
obj << Modify Table( Column Table( 1 ), Retype( Analysis Column( :age ) ), Grouping Column );
```

#### [Change grouping column to analysis column](#change-grouping-column-to-analysis-column)[](#change-grouping-column-to-analysis-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Statistics( N ), Grouping Columns( :age ) ),
        Row Table( Grouping Columns( :sex ) )
    )
);
obj << Modify Table( Column Table( 1 ), Retype( Grouping Column( :age ) ), Analysis Column );
```

### [Save grouping as tags in data table export](#save-grouping-as-tags-in-data-table-export)[](#save-grouping-as-tags-in-data-table-export "Click to copy url")

**Syntax:** obj \<\< Save grouping as tags in data table export( state=0\|1 )

**Description:** Sets if the grouping levels should be included in the data table as column tags. On by default.

**JMP Version Added:** 19

#### [Don't save tags](#dont-save-tags)[](#dont-save-tags "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Save Grouping As Tags In Data Table Export( 0 );
obj << Make Into Data Table;
```

#### [Save tags](#save-tags)[](#save-tags "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Save Grouping As Tags In Data Table Export( 1 );
obj << Make Into Data Table;
```

### [Scroll lock row headers in data table export](#scroll-lock-row-headers-in-data-table-export)[](#scroll-lock-row-headers-in-data-table-export "Click to copy url")

**Syntax:** obj \<\< Scroll lock row headers in data table export( state=0\|1 )

**Description:** Sets if the columns containing the row headers should be scroll locked. On by default.

**JMP Version Added:** 19

#### [Don't scroll lock row headers](#dont-scroll-lock-row-headers)[](#dont-scroll-lock-row-headers "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Scroll Lock Row Headers In Data Table Export( 0 );
obj << Make Into Data Table;
```

#### [Scroll lock row headers](#scroll-lock-row-headers)[](#scroll-lock-row-headers "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Scroll Lock Row Headers In Data Table Export( 1 );
obj << Make Into Data Table;
```

### [Set Format](#set-format)[](#set-format "Click to copy url")

**Syntax:** Set Format( statistic( Column( format ) )

**Description:** Sets the format displayed for analysis columns.

#### [Format in existing](#format-in-existing)[](#format-in-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
obj << Set Format( Mean( :OZONE( 6, 4 ) ) );
```

#### [Format multiple stats and analysis columns](#format-multiple-stats-and-analysis-columns)[](#format-multiple-stats-and-analysis-columns "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
Tabulate(
    Show Control Panel( 0 ),
    Set Format(
        Mean(
            :height( 10, 1 ),
            Analysis Column(
                Transform Column( "Log[height]", Formula( Log( :height ) ) ),
                Format( 10, "Best" )
            )
        ),
        "% of Total"n(
            :height( 12, 2 ),
            Analysis Column(
                Transform Column( "Log[height]", Formula( Log( :height ) ) ),
                Format( 12, 2 )
            )
        )
    ),
    Add Table(
        Column Table(
            Analysis Columns(
                :height,
                Transform Column( "Log[height]", Formula( Log( :height ) ) )
            ),
            Statistics( Mean, "% of Total"n )
        ),
        Row Table( Grouping Columns( :sex ) )
    )
);
```

#### [Format single stat and analysis column](#format-single-stat-and-analysis-column)[](#format-single-stat-and-analysis-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Set Format( Mean( :OZONE( 6, 4 ) ) ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
```

#### [Format stat without analysis column](#format-stat-without-analysis-column)[](#format-stat-without-analysis-column "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Set Format( Row %( Format( 9, 1, "Percent" ) ) ),
    Add Table( Column Table( Grouping Columns( :age ), Statistics( Row % ) ) )
);
```

### [Show Chart](#show-chart)[](#show-chart "Click to copy url")

**Syntax:** obj \<\< Show Chart( state=0\|1 )

**Description:** Displays or hides a bar chart generated from the table created in Tabulate.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Show Chart( 1 );
```

### [Show Control Panel](#show-control-panel)[](#show-control-panel "Click to copy url")

**Syntax:** obj \<\< Show Control Panel( state=0\|1 )

**Description:** Displays or hides the control panel used to manipulate the table created in Tabulate. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Show Control Panel( 1 );
```

### [Show Shading](#show-shading)[](#show-shading "Click to copy url")

**Syntax:** obj \<\< Show Shading( state=0\|1 )

**Description:** Displays or hides alternating shaded and nonshaded lines on the table created in Tabulate. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Show Shading( 1 );
```

### [Show Table](#show-table)[](#show-table "Click to copy url")

**Syntax:** obj \<\< Show Table( state=0\|1 )

**Description:** Displays or hides the table created in Tabulate. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Show Table( 1 );
```

### [Show Test Build Panel](#show-test-build-panel)[](#show-test-build-panel "Click to copy url")

**Syntax:** obj \<\< Show Test Build Panel( state=0\|1 )

**Description:** Displays or hides the panel controlling sampling for a test build of the table.

#### [Show for existing](#show-for-existing)[](#show-for-existing "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cytometry.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 1 ),
    Add Table(
        Column Table( Statistics( Mean, Std Dev ) ),
        Row Table( Analysis Columns( :ForSc, :SideSc, :CD3, :CD8, :CD4, :MCB ) )
    )
);
obj << Show Test Build Panel( 1 );
```

#### [Show for new](#show-for-new)[](#show-for-new "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cytometry.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 1 ),
    Show Test Build Panel( 1 ),
    Add Table(
        Column Table( Statistics( Mean, Std Dev ) ),
        Row Table( Analysis Columns( :ForSc, :SideSc, :CD3, :CD8, :CD4, :MCB ) )
    )
);
```

### [Show Tooltip](#show-tooltip)[](#show-tooltip "Click to copy url")

**Syntax:** obj \<\< Show Tooltip( state=0\|1 )

**Description:** Displays or hides the tooltips when hovering on drop zones and menus the Tabulate output.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Show Tool Tip( 1 );
```

### [Stack Grouping Columns](#stack-grouping-columns)[](#stack-grouping-columns "Click to copy url")

**Syntax:** Stack Grouping Columns(0 \| 1)

**Description:** Stack the grouping columns into a single column, using indenting to show the nesting structure.

#### [Set in existing](#set-in-existing_9)[](#set-in-existing_9 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :marital status ),
            Add Aggregate Statistics( :marital status ),
            Analysis Columns( :age ),
            Statistics( Min, Max )
        ),
        Row Table(
            Grouping Columns( :sex, :country, :size ),
            Add Aggregate Statistics( :sex, :country, :size )
        )
    )
);
obj << Modify Table( Row Table( 1 ), Modify Table Option( Stack Grouping Columns( 1 ) ) );
```

#### [Set in new](#set-in-new_9)[](#set-in-new_9 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Grouping Columns( :marital status ),
            Add Aggregate Statistics( :marital status ),
            Analysis Columns( :age ),
            Statistics( Min, Max )
        ),
        Row Table(
            Grouping Columns( :sex, :country, :size ),
            Add Aggregate Statistics( :sex, :country, :size ),
            Stack Grouping Columns( 1 )
        )
    )
);
```

### [Statistics](#statistics)[](#statistics "Click to copy url")

**Syntax:** Statistics( N\|Mean\|Std Dev\|Min\|Max\|Range\|% of Total\|N Missing\|N Categories\|Sum\|Sum Wgt\|Variance\|Std Err\|CV\|Median\|Interquartile Range\|Quantiles\|Column %\|Row %\|All )

**Description:** Adds statistics to a column or row in the table. When scripting, the Statistics() message resides next to the identifying Analysis Columns( column ) message, and both are nested within either a Row Table() or Column Table() command.

#### [Add to existing](#add-to-existing_4)[](#add-to-existing_4 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean, Max ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
obj << Modify Table( Column Table( 1 ), Statistics( Min ) );
```

#### [Add to new](#add-to-new_3)[](#add-to-new_3 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cities.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Analysis Columns( :OZONE ), Statistics( Mean, Max ) ),
        Row Table( Grouping Columns( :Region ) )
    )
);
```

### [Test Build](#test-build)[](#test-build "Click to copy url")

**Syntax:** obj \<\< Test Build( Sample Size( number ) )

**Description:** Displays the table using a test build sample of the data of size number.

#### [Set in existing](#set-in-existing_10)[](#set-in-existing_10 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cytometry.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Statistics( Mean, Std Dev ) ),
        Row Table( Analysis Columns( :ForSc, :SideSc, :CD3, :CD8, :CD4, :MCB ) )
    )
);
obj << Test Build( Sample Size( 100 ) );
```

#### [Set in new](#set-in-new_10)[](#set-in-new_10 "Click to copy url")

``` jsl
dt = Open( "$SAMPLE_DATA/Cytometry.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Test Build( Sample Size( 100 ) ),
    Add Table(
        Column Table( Statistics( Mean, Std Dev ) ),
        Row Table( Analysis Columns( :ForSc, :SideSc, :CD3, :CD8, :CD4, :MCB ) )
    )
);
```

### [Test Data View](#test-data-view)[](#test-data-view "Click to copy url")

**Syntax:** obj \<\< Test Data View

**Description:** Displays the data table used as a sample to build the test table.

``` jsl
dt = Open( "$SAMPLE_DATA/Cytometry.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Statistics( Mean, Std Dev ) ),
        Row Table( Analysis Columns( :ForSc, :SideSc, :CD3, :CD8, :CD4, :MCB ) )
    )
);
obj << Test Build( Sample Size( 100 ) );
obj << Test Data View;
```

### [Undo](#undo)[](#undo "Click to copy url")

**Syntax:** obj \<\< Undo

**Description:** Removes the effect of the last operation issued to the current table.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Add Table( Column Table( Grouping Columns( :type ) ) );
Wait( 2 );
obj << Undo;
```

### [Uniform plot scale](#uniform-plot-scale)[](#uniform-plot-scale "Click to copy url")

**Syntax:** obj \<\< Uniform plot scale( state=0\|1 )

**Description:** Sets the scales for all subcategories to be the same on the bar chart. On by default.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Show Chart( 1 );
Wait( 2 );
obj << Uniform Plot Scale( 1 );
```

### [Unpack](#unpack)[](#unpack "Click to copy url")

**Syntax:** obj \<\< Unpack( \<Analysis columns \| Statistics\>(operand name, ...) )

**Description:** Unpacks a packed set of columns.

``` jsl
dt = Open( "$SAMPLE_DATA/Hybrid Fuel Economy.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table(
            Statistics( Sum ),
            Analysis Columns( :City MPG, :Hwy MPG, :Comb MPG ),
            Pack(
                Analysis Columns( City MPG, Hwy MPG, Comb MPG ),
                Template( "^FIRST  (^OTHERS)", "/" )
            )
        ),
        Row Table( Grouping Columns( :Mfr Name, :Engine ) )
    )
);
obj << Modify Table( Column Table( 1 ), Unpack( Analysis Columns( :City MPG ) ) );
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Copy Script;
```

### [Data Table Window](#data-table-window)[](#data-table-window "Click to copy url")

**Syntax:** obj \<\< Data Table Window

**Description:** Move the data table window for this analysis to the front.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
t = obj << Get Script;
Show( t );
```

### [Get Script With Data Table](#get-script-with-data-table)[](#get-script-with-data-table "Click to copy url")

**Syntax:** obj \<\< Get Script With Data Table

**Description:** Creates a script(JSL) to produce this analysis specifically referencing this data table and returns it as an expression.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
t = obj << Get Script With Data Table;
Show( t );
```

### [Get Timing](#get-timing)[](#get-timing "Click to copy url")

**Syntax:** obj \<\< Get Timing

**Description:** Times the platform launch.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Redo Analysis;
```

### [Relaunch Analysis](#relaunch-analysis)[](#relaunch-analysis "Click to copy url")

**Syntax:** obj \<\< Relaunch Analysis

**Description:** Opens the platform launch window and recalls the settings that were used to create the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Report View( "Summary" );
```

### [Save ByGroup Script to Data Table](#save-bygroup-script-to-data-table)[](#save-bygroup-script-to-data-table "Click to copy url")

**Syntax:** Save ByGroup Script to Data Table( \<name\>, \< \<\<Append Suffix(0\|1)\>, \< \<\<Prompt(0\|1)\>, \< \<\<Replace(0\|1)\> );

**Description:** Creates a JSL script to produce this analysis, and save it as a table property in the data table. You can specify a name for the script. The Append Suffix option appends a numeric suffix to the script name, which differentiates the script from an existing script with the same name. The Prompt option prompts the user to specify a script name. The Replace option replaces an existing script with the same name.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Save Script for All Objects;
```

### [Save Script for All Objects To Data Table](#save-script-for-all-objects-to-data-table)[](#save-script-for-all-objects-to-data-table "Click to copy url")

**Syntax:** obj \<\< Save Script for All Objects To Data Table( \<name\> )

**Description:** Saves a script for all report objects to the current data table. This option is useful when you have multiple reports in the window. The script is named after the first platform unless you specify the script name in quotes.

**Example 1**

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    ),
    By( :_bycol ),
    Group Options( Return Group( 1 ) )
);
obj[1] << Save Script for All Objects To Data Table;
```

**Example 2**

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
dt << New Column( "_bycol",
    Character,
    Nominal,
    Set Values( Repeat( {"A", "B"}, N Rows( dt ) )[1 :: N Rows( dt )] )
);
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Save Script to Data Table( "My Analysis", <<Prompt( 0 ), <<Replace( 0 ) );
```

### [Save Script to Journal](#save-script-to-journal)[](#save-script-to-journal "Click to copy url")

**Syntax:** obj \<\< Save Script to Journal

**Description:** Create a JSL script to produce this analysis, and add a Button to the journal containing this script.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Save Script to Journal;
```

### [Save Script to Report](#save-script-to-report)[](#save-script-to-report "Click to copy url")

**Syntax:** obj \<\< Save Script to Report

**Description:** Create a JSL script to produce this analysis, and show it in the report itself. Useful to preserve a printed record of what was done.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Save Script to Report;
```

### [Save Script to Script Window](#save-script-to-script-window)[](#save-script-to-script-window "Click to copy url")

**Syntax:** obj \<\< Save Script to Script Window

**Description:** Create a JSL script to produce this analysis, and append it to the current Script text window.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
    )
);
obj << Title( "My Platform" );
```

### [Top Report](#top-report)[](#top-report "Click to copy url")

**Syntax:** obj \<\< Top Report

**Description:** Returns a reference to the root node in the report.

``` jsl
dt = Open( "$SAMPLE_DATA/Car Poll.jmp" );
obj = dt << Tabulate(
    Show Control Panel( 0 ),
    Add Table(
        Column Table( Grouping Columns( :sex, :marital status ) ),
        Row Table( Grouping Columns( :country, :size ) )
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

**Syntax:** obj = Tabulate(...Window View( "Visible"\|"Invisible"\|"Private" )...)

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

[ Previous](Survival.html "Survival") [Next ](Ternary%20Plot.html "Ternary Plot")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
