# Columns Manager

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Columns%20Manager.html](https://jsl.jmp.com/All%20Categories/Objects/Columns%20Manager.html)*

---

# [Columns Manager](#columns-manager)[](#columns-manager "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Clear All Filters](#clear-all-filters)[](#clear-all-filters "Click to copy url")

**Syntax:** obj \<\< Clear All Filters

**Description:** This option removes all the filters from the summary table. Note that the Set Columns command is not a filter, so calling this command does not remove that restriction on the displayed columns.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Set Text Filter( "t" );
obj << Clear All Filters;
```

### [Create Data Dictionary](#create-data-dictionary)[](#create-data-dictionary "Click to copy url")

**Syntax:** obj \<\< Create Data Dictionary

**Description:** Create a journal that includes statistics and property information about each column.

**JMP Version Added:** 18

### [Extended Statistics](#extended-statistics)[](#extended-statistics "Click to copy url")

**Syntax:** obj \<\< Extended Statistics(\<list of statistics\>)

**Description:** Override the default set of extended statistics without having to configure the list in preferences.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager( Include Extended Statistics( 1 ) );
obj << Extended Statistics( {"Median Absolute Deviation", "Q1"} );
```

### [Force calculations for all categorical columns](#force-calculations-for-all-categorical-columns)[](#force-calculations-for-all-categorical-columns "Click to copy url")

**Syntax:** obj \<\< Force calculations for all categorical columns( state=0\|1 )

**Description:** With this option enabled, stats are calculated for all categorical columns, not just character columns. For example, an expression column calculates the number of missing values.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = dt << Columns Manager;
obj << Force calculations for all categorical columns( 1 );
```

### [Force calculations for all numeric columns](#force-calculations-for-all-numeric-columns)[](#force-calculations-for-all-numeric-columns "Click to copy url")

**Syntax:** obj \<\< Force calculations for all numeric columns( state=0\|1 )

**Description:** With this option enabled, numeric stats are calculated for all numeric columns, if possible. For example, the number of unique values is calculated for columns designated as continuous.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Force calculations for all numeric columns( 1 );
```

### [Get Summary Table](#get-summary-table)[](#get-summary-table "Click to copy url")

**Syntax:** obj \<\< Get Summary Table

**Description:** Get the Table Box for the summary table

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
tab = obj << Get Summary table;
tab << Sort By Column( "n unique" );
```

### [Hide Excluded Columns](#hide-excluded-columns)[](#hide-excluded-columns "Click to copy url")

**Syntax:** obj \<\< Hide Excluded Columns( state=0\|1 )

**Description:** Include or remove columns marked Excluded from the summary table.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Hide Excluded Columns( 0 );
```

### [Hide Hidden Columns](#hide-hidden-columns)[](#hide-hidden-columns "Click to copy url")

**Syntax:** obj \<\< Hide Hidden Columns( state=0\|1 )

**Description:** Include or remove columns marked Hidden from the summary table.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Hide Hidden Columns( 0 );
```

### [Include Extended Statistics](#include-extended-statistics)[](#include-extended-statistics "Click to copy url")

**Syntax:** obj \<\< Include Extended Statistics( state=0\|1 )

**Description:** The set of additional statistics can be configured in Preferences.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Include Extended Statistics( 1 );
```

### [Select Rows](#select-rows)[](#select-rows "Click to copy url")

**Syntax:** obj \<\< Select Rows(\<empty\> \| All \| None \| \<column references\>)

**Description:** This option selects rows in the summary table corresponding to columns. Clear by passing in no arguments. Select all or none of the visible rows by passing in All or None. Selected specific rows by passing a list of column references.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Select Rows( :age, :height );
```

### [Set Columns](#set-columns)[](#set-columns "Click to copy url")

**Syntax:** obj \<\< Set Columns(\<columns\>)

**Description:** By default the Columns Manager includes all of the columns in the data table as its base set of columns. That set might (or might not) be reduced in the report by applying the removal of excluded columns. This option allows the restriction of the set of columns that the Columns Manager has access to.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Set Columns( {:height, :weight} );
```

### [Set Modeling Type Filter](#set-modeling-type-filter)[](#set-modeling-type-filter "Click to copy url")

**Syntax:** obj \<\< Set Modeling Type Filter(\<empty\> \| \<Continuous, Nominal, Ordinal, Vector, Unstructured Text, Multiple Response, None\>)

**Description:** This option sets the modeling type filter. Clear by passing no arguments, or specify one or more modeling type names. The filter is satisfied by columns that match any of the analysis types.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Set Modeling Type Filter( "Continuous", "Ordinal" );
```

### [Set Property Filter](#set-property-filter)[](#set-property-filter "Click to copy url")

**Syntax:** obj \<\< Set Property Filter(\<empty\> \| At Least One Property \| \<list of property names\>)

**Description:** This option sets the property filter. Clear by passing no arguments, or specify one or more property names. The filter is specified by columns that contain any of the properties. There is also a special value that is matched by columns having any properties.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class Families.jmp" );
obj = dt << Columns Manager;
obj << Set Property Filter( "Matrix Column Names", "Value colors" );
```

### [Set Selection Filter](#set-selection-filter)[](#set-selection-filter "Click to copy url")

**Syntax:** obj \<\< Set Selection Filter(\<empty\> \| Keep \| Hide)

**Description:** This option sets the selection filter. It allows the user to make arbitrary selection of columns and then filter the list to that set of columns (with Keep, or its inverse with Hide). Clear by passing no arguments.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Select Rows( :age, :height );
obj << Set Selection Filter( "Keep" );
```

### [Set Text Filter](#set-text-filter)[](#set-text-filter "Click to copy url")

**Syntax:** obj \<\< Set Text Filter(\<empty\> \| \<search text\>)

**Description:** This option sets the current text filter data, which reduces the number of columns shown in the summary table. The text filter is applied only to column names.

**JMP Version Added:** 18

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Set Text Filter( "me" );
```

### [Show Attributes](#show-attributes)[](#show-attributes "Click to copy url")

**Syntax:** obj \<\< Show Attributes( state=0\|1 )

**Description:** Expand or collapse the section of the summary table that contains column attributes.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Show Attributes( 0 );
```

### [Show Properties](#show-properties)[](#show-properties "Click to copy url")

**Syntax:** obj \<\< Show Properties( state=0\|1 )

**Description:** Expand or collapse the section of the summary table that contains column properties.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Show Properties( 0 );
```

### [Show Statistics](#show-statistics)[](#show-statistics "Click to copy url")

**Syntax:** obj \<\< Show Statistics( state=0\|1 )

**Description:** Expand or collapse the section of the summary table that contains column statistics.

``` jsl

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
obj = dt << Columns Manager;
obj << Show Statistics( 0 );
```

[ Previous](Column%20Switcher.html "Column Switcher") [Next ](Compare%20Data%20Tables.html "Compare Data Tables")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
