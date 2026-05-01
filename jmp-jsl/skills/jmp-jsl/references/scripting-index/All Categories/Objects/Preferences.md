# Preferences

*Source: [https://jsl.jmp.com/All%20Categories/Objects/Preferences.html](https://jsl.jmp.com/All%20Categories/Objects/Preferences.html)*

---

# [Preferences](#preferences)[](#preferences "Click to copy url")

## [Item Messages](#item-messages)[](#item-messages "Click to copy url")

### [Add Color Theme](#add-color-theme)[](#add-color-theme "Click to copy url")

**Syntax:** obj \<\< Add Color Theme( Add Color Theme({"Name", \<type\|style\>, {color, ..., \<Missing(color)\>}, \<{position, ...}\>}, \<color blindness discernability\>) )

**Description:** Creates a new custom color theme and registers it with the theme picker.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Set Preference(
    Add Color Theme(
        {"Sunny", {{255, 255, 0}, {255, 128, 64}, {255, 0, 0}, {163, 12, 27}}, {0, 0.5,
        0.642857142857143, 1}}
    )
);
Show( Get Color Theme Detail( "Sunny" ) );
```

### [Add Rows default number of rows](#add-rows-default-number-of-rows)[](#add-rows-default-number-of-rows "Click to copy url")

**Syntax:** obj \<\< Add Rows default number of rows( number )

**Description:** Initial number of rows in the Add Rows window

**JMP Version Added:** 18

### [Add Rows recall last value](#add-rows-recall-last-value)[](#add-rows-recall-last-value "Click to copy url")

**Syntax:** obj \<\< Add Rows recall last value( state=0\|1 )

**Description:** The last entered value is used for the number of rows to add

**JMP Version Added:** 18

### [Add files opened by scripts to the Recent Files list](#add-files-opened-by-scripts-to-the-recent-files-list)[](#add-files-opened-by-scripts-to-the-recent-files-list "Click to copy url")

**Syntax:** obj \<\< Add files opened by scripts to the Recent Files list( state=0\|1 )

**Description:** Changes the default setting for whether files opened with the JSL Open() function are added to the Recent Files list.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Add files opened by scripts to the Recent Files list( 1 ) );
```

### [Allow 16 Bit List Check Compression](#allow-16-bit-list-check-compression)[](#allow-16-bit-list-check-compression "Click to copy url")

**Syntax:** obj \<\< Allow 16 Bit List Check Compression( state=0\|1 )

**Description:** Specifies whether to use List Check to encode values when there are more than 255 distinct values in the column. If encoded, these columns cannot be read by JMP 14 and earlier.

**JMP Version Added:** 15

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Allow 16 Bit List Check Compression( 1 ) );
```

### [Allow Compress Selected Columns to create compact columns](#allow-compress-selected-columns-to-create-compact-columns)[](#allow-compress-selected-columns-to-create-compact-columns "Click to copy url")

**Syntax:** obj \<\< Allow Compress Selected Columns to create compact columns( state=0\|1 )

**Description:** Compress Selected Columns will compact columns if that uses less disk space.

**JMP Version Added:** 18

### [Allow Unquoted Strings in JSL](#allow-unquoted-strings-in-jsl)[](#allow-unquoted-strings-in-jsl "Click to copy url")

**Syntax:** obj \<\< Allow Unquoted Strings in JSL( "No"\|"Yes (with a warning)"\|"Yes (no warning)" )

### [Allow mixed ISO format patterns](#allow-mixed-iso-format-patterns)[](#allow-mixed-iso-format-patterns "Click to copy url")

**Syntax:** obj \<\< Allow mixed ISO format patterns( state=0\|1 )

**Description:** Allow format pattern dates with both ISO weeks () and non-ISO years ( or ), and with both non-ISO weeks ( or ) and ISO years ( or ). ISO weeks and years are not compatible with non-ISO weeks and years. They should not be mixed. By default, JMP will not allow such date format to be created.

**JMP Version Added:** 18

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Allow mixed ISO format patterns( 1 ) );
```

### [Allow short numeric data format](#allow-short-numeric-data-format)[](#allow-short-numeric-data-format "Click to copy url")

**Syntax:** obj \<\< Allow short numeric data format( state=0\|1 )

**Description:** Changes the default setting for allowing short numeric data format.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Allow short numeric data format( 1 ) );
```

### [Always allow publishing to JMP Public](#always-allow-publishing-to-jmp-public)[](#always-allow-publishing-to-jmp-public "Click to copy url")

**Syntax:** obj \<\< Always allow publishing to JMP Public( state=0\|1 )

**Description:** Always enable the menu item for publishing to JMP Public, even if there are other JMP Live connections configured.

**JMP Version Added:** 19

### [Auto Hide Menus](#auto-hide-menus)[](#auto-hide-menus "Click to copy url")

**Syntax:** obj \<\< Auto Hide Menus( "Always"\|"Never"\|"Based on window size" )

**Description:** Determines if and when JMP auto-hides the menu and toolbars. Note: This is available on Windows only.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Auto Hide Menus( "Always" ) );
```

### [Auto Run Recent JSL](#auto-run-recent-jsl)[](#auto-run-recent-jsl "Click to copy url")

**Syntax:** obj \<\< Auto Run Recent JSL( state=0\|1 )

**Description:** Changes the default behavior for automatically running recently submitted JSL scripts. Note: This is available on Windows only.

``` jsl
//Caution: Changing a preference will affect 
//the default behavior of JMP. 

Preferences[1] << Set( Auto Run Recent JSL( 1 ) );
```

### [Auto match brackets in script editor](#auto-match-brackets-in-script-editor)[](#auto-match-brackets-in-script-editor "Click to copy url")

**Syntax:** obj \<\< Auto match brackets in script editor( state=0\|1 )

**Description:** Changes the default setting for automatically matching brackets in the script window. Note: This is available on Windows only.

``` jsl
//Caution: Changing a preference will affect 
//the default behavior of JMP. 

Preferences[1] << Set( Auto match brackets in script editor( 1 ) );
```

### [Autosave maximum data table columns](#autosave-maximum-data-table-columns)[](#autosave-maximum-data-table-columns "Click to copy url")

**Syntax:** obj \<\< Autosave maximum data table columns( number )

**Description:** Maximum number of data table columns that will be automatically saved.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Autosave Maximum Data Table Columns( 1000 ) );
```

### [Autosave maximum data table rows](#autosave-maximum-data-table-rows)[](#autosave-maximum-data-table-rows "Click to copy url")

**Syntax:** obj \<\< Autosave maximum data table rows( number )

**Description:** Maximum number of data table rows that will be automatically saved.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Autosave Maximum Data Table Rows( 10000 ) );
```

### [Autosave timeout](#autosave-timeout)[](#autosave-timeout "Click to copy url")

**Syntax:** obj \<\< Autosave timeout( number )

**Description:** Autosave time-out interval is in minutes. When the time-out interval has been met, all open and modified files are saved. The default value is "0", which indicates that no autosave processing will be performed.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Autosave Timeout( 15 ) );
```

### [Axis Title Above](#axis-title-above)[](#axis-title-above "Click to copy url")

**Syntax:** obj \<\< Axis Title Above( state=0\|1 )

**Description:** Changes the position of the y-axis label in graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Axis Title Above( 1 ) );
```

### [Background Color](#background-color)[](#background-color "Click to copy url")

**Syntax:** obj \<\< Background Color( color )

**Description:** Changes the default setting for the background color in all windows. Note: Available for Windows only.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Background Color( "Light Blue" ) );
```

### [Bad to Good Color Theme](#bad-to-good-color-theme)[](#bad-to-good-color-theme "Click to copy url")

**Syntax:** obj \<\< Bad to Good Color Theme( "name" )

**Description:** Changes the default setting for the continuous color theme appearing in all graphs.

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Show( Get Preference( Continuous Color Theme ) );
Set Preference( Bad to Good Color Theme( "Green to Purple" ) );
Show( Get Preference( Bad to Good Color Theme ) );
```

### [Box Plot Line Width](#box-plot-line-width)[](#box-plot-line-width "Click to copy url")

**Syntax:** obj \<\< Box Plot Line Width( number )

**Description:** Changes the default line width for box plots.

``` jsl
//Caution: Changing a preference will
//affect the default behavior of JMP.

Preferences[1] << Set( Box Plot Line Width( 2 ) );
```

### [Bypass Proxy](#bypass-proxy)[](#bypass-proxy "Click to copy url")

**Syntax:** obj \<\< Bypass Proxy( text )

**Description:** Disable proxy use for specific hosts

**JMP Version Added:** 15

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Bypass Proxy( "www.example.com" ) );
```

### [Categorical Color Theme](#categorical-color-theme)[](#categorical-color-theme "Click to copy url")

**Syntax:** obj \<\< Categorical Color Theme( "name" )

**Description:** Changes the default setting for the categorical color theme appearing in all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Show( Get Preference( Categorical Color Theme ) );
Set Preference( Categorical Color Theme( "Jet" ) );
Show( Get Preference( Categorical Color Theme ) );
```

### [Categorical graph type](#categorical-graph-type)[](#categorical-graph-type "Click to copy url")

**Syntax:** obj \<\< Categorical graph type( "Auto"\|"Histogram"\|"Bars"\|"Heat Map"\|"Mosaic"\|"Run Chart"\|"Run Chart" )

**Description:** Default graph to display in column header for nominal and ordinal columns.

**JMP Version Added:** 18

### [Classic Data Table Selection](#classic-data-table-selection)[](#classic-data-table-selection "Click to copy url")

**Syntax:** obj \<\< Classic Data Table Selection( state=0\|1 )

**Description:** Enables classic click selection behavior in the data table. In this mode, selecting a column will have no effect on row selection, and selecting a row will have no effect on column selection.

**JMP Version Added:** 19

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Classic Data Table Selection( 1 ) );
```

### [Color Mode](#color-mode)[](#color-mode "Click to copy url")

**Syntax:** obj \<\< Color Mode( "Use System Setting"\|"Light"\|"Dark"\|"High Contrast" )

**Description:** Changes whether JMP uses a specific window coloring theme or honors the operating system setting.

``` jsl
//Caution: Changing a preference will affect 
//the default behavior of JMP. 

Preferences[1] << Set( Color Mode( Dark ) );
```

### [Columns Manager](#columns-manager)[](#columns-manager "Click to copy url")

**Syntax:** obj \<\< Columns Manager

**JMP Version Added:** 18

### [Conditional formatting rules](#conditional-formatting-rules)[](#conditional-formatting-rules "Click to copy url")

**Syntax:** obj \<\< Conditional formatting rules

**Description:** Creates a custom conditional rule that is shown or not according to the Show conditional formatting preference setting.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences(
    Conditional Formatting Rules(
        RuleSet(
            RuleName( "My Special Rule" ),
            GreaterThan(
                Value( 0 ),
                Inclusive( 0 ),
                Format(
                    Text Color( "Medium Dark Red" ),
                    Back Color( "Light Yellow" ),
                    Annotation( 1 ),
                    FontStyle( Bold )
                )
            )
        )
    )
);
```

### [Continuous Color Theme](#continuous-color-theme)[](#continuous-color-theme "Click to copy url")

**Syntax:** obj \<\< Continuous Color Theme( "name" )

**Description:** Changes the default setting for the continuous color theme appearing in all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Show( Get Preference( Continuous Color Theme ) );
Set Preference( Continuous Color Theme( "Green to Purple" ) );
Show( Get Preference( Continuous Color Theme ) );
```

### [Continuous graph type](#continuous-graph-type)[](#continuous-graph-type "Click to copy url")

**Syntax:** obj \<\< Continuous graph type( "Auto"\|"Histogram"\|"Bars"\|"Heat Map"\|"Mosaic"\|"Run Chart"\|"Run Chart" )

**Description:** Default graph to display in column header for continuous columns.

**JMP Version Added:** 18

### [Custom Locale Settings](#custom-locale-settings)[](#custom-locale-settings "Click to copy url")

**Syntax:** obj \<\< Custom Locale Settings

**Description:** Overrides locale settings such as decimal separator and thousands separator

**JMP Version Added:** 16

**Example 1**

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Custom Locale Settings( Decimal Separator( "," ) ) );
Print( Format( 1.25, "Best" ) );
Preferences( Custom Locale Settings( Decimal Separator( "." ) ) );
Print( Format( 1.25, "Best" ) );
Preferences( Custom Locale Settings( Decimal Separator() ) );
```

**Example 2**

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

// Clear all locale overrides...
Preferences( Custom Locale Settings( Reset to Defaults ) );
```

**Example 3**

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Get Preferences( Custom Locale Settings );
```

### [Data Filter Auto Clear](#data-filter-auto-clear)[](#data-filter-auto-clear "Click to copy url")

**Syntax:** obj \<\< Data Filter Auto Clear( state=0\|1 )

### [Data Filter Check Box Display](#data-filter-check-box-display)[](#data-filter-check-box-display "Click to copy url")

**Syntax:** obj \<\< Data Filter Check Box Display( state=0\|1 )

**Description:** Default display for categorical filter column is check box display.

### [Data Filter Conditional](#data-filter-conditional)[](#data-filter-conditional "Click to copy url")

**Syntax:** obj \<\< Data Filter Conditional( state=0\|1 )

### [Data Filter Group is AND](#data-filter-group-is-and)[](#data-filter-group-is-and "Click to copy url")

**Syntax:** obj \<\< Data Filter Group is AND( state=0\|1 )

### [Data Filter Histograms and Bars](#data-filter-histograms-and-bars)[](#data-filter-histograms-and-bars "Click to copy url")

**Syntax:** obj \<\< Data Filter Histograms and Bars( state=0\|1 )

**Description:** Show Histograms and Bars for filter columns where available

**JMP Version Added:** 15

### [Data Filter Include Check](#data-filter-include-check)[](#data-filter-include-check "Click to copy url")

**Syntax:** obj \<\< Data Filter Include Check( state=0\|1 )

### [Data Filter Select Check](#data-filter-select-check)[](#data-filter-select-check "Click to copy url")

**Syntax:** obj \<\< Data Filter Select Check( state=0\|1 )

### [Data Filter Show Check](#data-filter-show-check)[](#data-filter-show-check "Click to copy url")

**Syntax:** obj \<\< Data Filter Show Check( state=0\|1 )

### [Data Table Actions](#data-table-actions)[](#data-table-actions "Click to copy url")

**Syntax:** obj \<\< Data Table Actions( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Data Table Actions( 1 ) );
```

### [Data Table Title on Output](#data-table-title-on-output)[](#data-table-title-on-output "Click to copy url")

**Syntax:** obj \<\< Data Table Title on Output( state=0\|1 )

**Description:** Changes the default setting for displaying the data table names at the top of the report's output.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Data Table Title on Output( 1 ) );
```

### [Date Title on Output](#date-title-on-output)[](#date-title-on-output "Click to copy url")

**Syntax:** obj \<\< Date Title on Output( state=0\|1 )

**Description:** Changes the default setting for displaying the date in the title of the output.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Date Title on Output( 1 ) );
```

### [Default Field Width](#default-field-width)[](#default-field-width "Click to copy url")

**Syntax:** obj \<\< Default Field Width( number )

**Description:** Change the default field width used for new numeric columns.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Default Field Width( 16 ) );
```

### [Default Project Show Bookmarks](#default-project-show-bookmarks)[](#default-project-show-bookmarks "Click to copy url")

**Syntax:** obj \<\< Default Project Show Bookmarks( state=0\|1 )

**Description:** Show the Project pane in new projects

**JMP Version Added:** 16

### [Default Project Show Contents](#default-project-show-contents)[](#default-project-show-contents "Click to copy url")

**Syntax:** obj \<\< Default Project Show Contents( state=0\|1 )

**Description:** Show the Contents pane in new projects

**JMP Version Added:** 16

### [Default Project Show Log](#default-project-show-log)[](#default-project-show-log "Click to copy url")

**Syntax:** obj \<\< Default Project Show Log( state=0\|1 )

**Description:** Show the Log pane in new projects

**JMP Version Added:** 16

### [Default Project Show Recent Files](#default-project-show-recent-files)[](#default-project-show-recent-files "Click to copy url")

**Syntax:** obj \<\< Default Project Show Recent Files( state=0\|1 )

**Description:** Show the Recent Files pane in new projects

**JMP Version Added:** 16

### [Default Project Show Workspace](#default-project-show-workspace)[](#default-project-show-workspace "Click to copy url")

**Syntax:** obj \<\< Default Project Show Workspace( state=0\|1 )

**Description:** Show the Workspace pane in new projects

**JMP Version Added:** 16

### [Display JSL SAS results as HTML](#display-jsl-sas-results-as-html)[](#display-jsl-sas-results-as-html "Click to copy url")

**Syntax:** obj \<\< Display JSL SAS results as HTML( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "Display JSL SAS results as HTML"n( 1 ) );
```

### [Display indexes in English](#display-indexes-in-english)[](#display-indexes-in-english "Click to copy url")

**Syntax:** obj \<\< Display indexes in English( state=0\|1 )

**Description:** Displays the Object Scripting Index, the JSL Functions Index, and the Display Box Index in English.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Display indexes in English( 1 ) );
```

### [Double Click Opens Column Info](#double-click-opens-column-info)[](#double-click-opens-column-info "Click to copy url")

**Syntax:** obj \<\< Double Click Opens Column Info( state=0\|1 )

**Description:** Double clicking on a column header will open the column info dialog rather than editing the column name.

**JMP Version Added:** 19

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Double Click Opens Column Info( 1 ) );
```

### [Empty Project at Startup](#empty-project-at-startup)[](#empty-project-at-startup "Click to copy url")

**Syntax:** obj \<\< Empty Project at Startup( "Always"\|"If no other project is open"\|"Never" )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Create an empty project when starting JMP( "Always" ) );
```

### [Emulate Zoom Mode](#emulate-zoom-mode)[](#emulate-zoom-mode "Click to copy url")

**Syntax:** obj \<\< Emulate Zoom Mode( state=0\|1 )

**Description:** Determines whether JMP includes the Window List in maximized windows

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Emulate Zoom Mode( 1 ) );
```

### [Enable Advanced Linear Algebra Routines](#enable-advanced-linear-algebra-routines)[](#enable-advanced-linear-algebra-routines "Click to copy url")

**Syntax:** obj \<\< Enable Advanced Linear Algebra Routines( state=0\|1 )

**Description:** Changes the linear algebra computation routines that are used in multiple platforms and JSL functions. When selected, this preference enables advanced linear algebra routines that are based on the BLAS and LAPACK libraries. The JMP documentation contains more information about the platforms and JSL functions that are affected by this preference.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enable Advanced Linear Algebra Routines( 0 ) );
```

### [Enable Telemetry](#enable-telemetry)[](#enable-telemetry "Click to copy url")

**Syntax:** obj \<\< Enable Telemetry( state=0\|1 )

### [Enable direct input from IME](#enable-direct-input-from-ime)[](#enable-direct-input-from-ime "Click to copy url")

**Syntax:** obj \<\< Enable direct input from IME( state=0\|1 )

### [End Menu Item Marking After Deadline](#end-menu-item-marking-after-deadline)[](#end-menu-item-marking-after-deadline "Click to copy url")

**Syntax:** obj \<\< End Menu Item Marking After Deadline( state=0\|1 )

**Description:** Menu items will no longer be marked after the time limit elapses

**JMP Version Added:** 17

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( End Menu Item Marking After Deadline( 0 ) );
```

### [Enhanced Log Alternate Table Rows](#enhanced-log-alternate-table-rows)[](#enhanced-log-alternate-table-rows "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Alternate Table Rows( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Shade Alternate Table Rows( 1 ) );
```

### [Enhanced Log Color By Window](#enhanced-log-color-by-window)[](#enhanced-log-color-by-window "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Color By Window( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Color By Window( 1 ) );
```

### [Enhanced Log Color By Window Color Theme](#enhanced-log-color-by-window-color-theme)[](#enhanced-log-color-by-window-color-theme "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Color By Window Color Theme( "name" )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Show( Get Preference( Enhanced Log Color By Window Color Theme ) );
Set Preference( Enhanced Log Color By Window Color Theme( "Jet" ) );
Show( Get Preference( Enhanced Log Color By Window Color Theme ) );
```

### [Enhanced Log Filter Action](#enhanced-log-filter-action)[](#enhanced-log-filter-action "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Filter Action( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Filter Action( 1 ) );
```

### [Enhanced Log Filter Error](#enhanced-log-filter-error)[](#enhanced-log-filter-error "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Filter Error( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Filter Error( 1 ) );
```

### [Enhanced Log Filter Log](#enhanced-log-filter-log)[](#enhanced-log-filter-log "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Filter Log( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Filter Log( 1 ) );
```

### [Enhanced Log Filter Result](#enhanced-log-filter-result)[](#enhanced-log-filter-result "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Filter Result( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Filter Result( 1 ) );
```

### [Enhanced Log Filter Script](#enhanced-log-filter-script)[](#enhanced-log-filter-script "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Filter Script( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Filter Script( 1 ) );
```

### [Enhanced Log Filter Warn](#enhanced-log-filter-warn)[](#enhanced-log-filter-warn "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Filter Warn( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Filter Warn( 1 ) );
```

### [Enhanced Log Origin Column](#enhanced-log-origin-column)[](#enhanced-log-origin-column "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Origin Column( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Origin Column( 1 ) );
```

### [Enhanced Log Result Column](#enhanced-log-result-column)[](#enhanced-log-result-column "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Result Column( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Result Column( 1 ) );
```

### [Enhanced Log Shade Table Cells](#enhanced-log-shade-table-cells)[](#enhanced-log-shade-table-cells "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Shade Table Cells( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Shade Table Cells( 1 ) );
```

### [Enhanced Log Shade Table Headings](#enhanced-log-shade-table-headings)[](#enhanced-log-shade-table-headings "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Shade Table Headings( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Shade Table Headings( 1 ) );
```

### [Enhanced Log Table Column Borders](#enhanced-log-table-column-borders)[](#enhanced-log-table-column-borders "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Table Column Borders( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Table Column Borders( 1 ) );
```

### [Enhanced Log Table Heading Column Borders](#enhanced-log-table-heading-column-borders)[](#enhanced-log-table-heading-column-borders "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Table Heading Column Borders( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Table Heading Column Borders( 1 ) );
```

### [Enhanced Log Table Row Borders](#enhanced-log-table-row-borders)[](#enhanced-log-table-row-borders "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Table Row Borders( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Table Row Borders( 1 ) );
```

### [Enhanced Log Timestamp Column](#enhanced-log-timestamp-column)[](#enhanced-log-timestamp-column "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Timestamp Column( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Timestamp Column( 1 ) );
```

### [Enhanced Log Underline Table Headings](#enhanced-log-underline-table-headings)[](#enhanced-log-underline-table-headings "Click to copy url")

**Syntax:** obj \<\< Enhanced Log Underline Table Headings( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enhanced Log Underline Table Headings( 1 ) );
```

### [Enter Key moves down](#enter-key-moves-down)[](#enter-key-moves-down "Click to copy url")

**Syntax:** obj \<\< Enter Key moves down( state=0\|1 )

**Description:** Changes the default setting for the Enter key movement.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Enter Key moves down( 1 ) );
```

### [Evaluate OnOpen Scripts](#evaluate-onopen-scripts)[](#evaluate-onopen-scripts "Click to copy url")

**Syntax:** obj \<\< Evaluate OnOpen Scripts( "Prompt"\|"Never"\|"Always" )

**Description:** Set to "Never" to never allow OnOpen scripts to run. Scripts from unknown sources should not be run.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Evaluate OnOpen Scripts( "Prompt" ) );
```

### [Excel Open Method](#excel-open-method)[](#excel-open-method "Click to copy url")

**Syntax:** obj \<\< Excel Open Method( "Open All Sheets"\|"Select Individual Worksheets"\|"Use Excel Wizard" )

### [Fast Marker Threshold](#fast-marker-threshold)[](#fast-marker-threshold "Click to copy url")

**Syntax:** obj \<\< Fast Marker Threshold( number )

**Description:** Changes the default setting for refreshing markers on graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Fast Marker Threshold( 100000 ) );
```

### [Fill Hollow Markers](#fill-hollow-markers)[](#fill-hollow-markers "Click to copy url")

**Syntax:** obj \<\< Fill Hollow Markers( state=0\|1 )

**Description:** Hollow markers will be filled with the graph background color

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Fill Hollow Markers( 1 ) );
```

### [Fill Selection Color](#fill-selection-color)[](#fill-selection-color "Click to copy url")

**Syntax:** obj \<\< Fill Selection Color( color )

**Description:** Color of filled selections when Fill Selection Mode is Selected Same Color.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Fill Selection Color( "Red" ) );
```

### [Fill Selection Fade](#fill-selection-fade)[](#fill-selection-fade "Click to copy url")

**Syntax:** obj \<\< Fill Selection Fade( number )

**Description:** Changes the default setting for the amount unselected fills are faded.

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Fill Selection Fade( 50 ) );
```

### [Fill Selection Mode](#fill-selection-mode)[](#fill-selection-mode "Click to copy url")

**Syntax:** obj \<\< Fill Selection Mode( "Selected Patterned"\|"Selected Darker"\|"Selected Outlined"\|"Selected Same Color"\|"Unselected Faded" )

**Description:** Changes the way that the selection is indicated for filled areas. Default is patterned.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Fill Selection Mode( "Selected Patterned" ) );
```

### [Formula Evaluation](#formula-evaluation)[](#formula-evaluation "Click to copy url")

**Syntax:** obj \<\< Formula Evaluation( "When Idle"\|"Immediate" )

**Description:** Determines if formula evaluation happens during idle time or if it runs immediately in the foreground

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Formula Evaluation( "Immediate" ) );
```

### [Frame Border](#frame-border)[](#frame-border "Click to copy url")

**Syntax:** obj \<\< Frame Border( state=0\|1 )

**Description:** Changes the default setting for displaying the frame border on non-axis sides of all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Frame Border( 1 ) );
```

### [Frame Color](#frame-color)[](#frame-color "Click to copy url")

**Syntax:** obj \<\< Frame Color( color )

**Description:** Changes the default setting for the color of frame borders drawn on all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Frame Color( "Green" ) );
```

### [Get](#get)[](#get "Click to copy url")

**Syntax:** obj \<\< Get

**Description:** Returns the script for setting a specified preference.

``` jsl
a = Preferences[1] << Get( Show the Tip of the Day at startup );
Show( a );
```

### [Get Script](#get-script)[](#get-script "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Returns the script for setting the preferences.

``` jsl
a = Preferences[1] << Get Script;
Show( a );
```

### [Graph Background Color](#graph-background-color)[](#graph-background-color "Click to copy url")

**Syntax:** obj \<\< Graph Background Color( color )

**Description:** Changes the default setting for the background color in all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Graph Background Color( "Light Green" ) );
```

### [Graph Border](#graph-border)[](#graph-border "Click to copy url")

**Syntax:** obj \<\< Graph Border( state=0\|1 )

**Description:** Changes the default setting for displaying the graph border on all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Graph Border( 1 ) );
```

### [Graph Height](#graph-height)[](#graph-height "Click to copy url")

**Syntax:** obj \<\< Graph Height( number )

**Description:** Changes the default setting for the graph height for all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Graph Height( 1 ) );
```

### [Graph Marker](#graph-marker)[](#graph-marker "Click to copy url")

**Syntax:** obj \<\< Graph Marker( marker )

**Description:** Changes the default setting for the marker shape appearing in all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Graph Marker( "Diamond" ) );
```

### [Graph Marker Theme](#graph-marker-theme)[](#graph-marker-theme "Click to copy url")

**Syntax:** obj \<\< Graph Marker Theme( "Standard"\|"Hollow"\|"Solid"\|"Paired"\|"Classic"\|"Alphanumeric" )

**Description:** Changes the default setting for the marker theme appearing in all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Graph Marker Theme( "Classic" ) );
```

### [Graph Marker Unselected Fade](#graph-marker-unselected-fade)[](#graph-marker-unselected-fade "Click to copy url")

**Syntax:** obj \<\< Graph Marker Unselected Fade( number )

**Description:** Changes the default setting for the amount unselected markers are faded.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Graph Marker Unselected Fade( 45 ) );
```

### [Graph Marker size](#graph-marker-size)[](#graph-marker-size "Click to copy url")

**Syntax:** obj \<\< Graph Marker size( "Dot"\|"Small"\|"Medium"\|"Large"\|"XL"\|"XXL"\|"XXXL" )

**Description:** Changes the default setting for the marker size appearing in all graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Graph Marker size( "Large" ) );
```

### [HDF5PathDelimiter](#hdf5pathdelimiter)[](#hdf5pathdelimiter "Click to copy url")

**Syntax:** obj \<\< HDF5PathDelimiter( text )

**JMP Version Added:** 17

### [Header summary heat map color theme](#header-summary-heat-map-color-theme)[](#header-summary-heat-map-color-theme "Click to copy url")

**Syntax:** obj \<\< Header summary heat map color theme( "name" )

**Description:** Changes the default setting for the continuous color theme appearing in all graphs.

**JMP Version Added:** 18

``` jsl
//Caution: Changing a preference will
//affect the default behavior of JMP.
Show( Get Preference( Header summary heat map color theme ) );
Set Preference( Header summary heat map color theme( "Green to Purple" ) );
Show( Get Preference( Header summary heat map color theme ) );
```

### [Hide 'Find and Replace' window](#hide-find-and-replace-window)[](#hide-find-and-replace-window "Click to copy url")

**Syntax:** obj \<\< Hide 'Find and Replace' window( state=0\|1 )

**Description:** Changes the default setting for keeping the 'Find and Replace' window open after finding and replacing.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "Hide 'Find and Replace' window"n( 1 ) );
```

### [Hide ODBC Connection Strings](#hide-odbc-connection-strings)[](#hide-odbc-connection-strings "Click to copy url")

**Syntax:** obj \<\< Hide ODBC Connection Strings( state=0\|1 )

### [Hide Overlapping Labels](#hide-overlapping-labels)[](#hide-overlapping-labels "Click to copy url")

**Syntax:** obj \<\< Hide Overlapping Labels( state=0\|1 )

**Description:** Hides the overlapping labels in a graph.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Hide Overlap Labels( 0 ) );
```

### [Histogram Color](#histogram-color)[](#histogram-color "Click to copy url")

**Syntax:** obj \<\< Histogram Color( color )

**Description:** Changes the default color for histograms.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Histogram Color( "Light Yellow" ) );
```

### [Histogram Line Color](#histogram-line-color)[](#histogram-line-color "Click to copy url")

**Syntax:** obj \<\< Histogram Line Color( color )

**Description:** Changes the default line color for histograms.

**JMP Version Added:** 17

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Histogram Line Color( "Red" ) );
```

### [Hover Help](#hover-help)[](#hover-help "Click to copy url")

**Syntax:** obj \<\< Hover Help( state=0\|1 )

**Description:** Tooltip-style help responding to circular mouse motions

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Hover Help( 1 ) );
```

### [Image Format for PowerPoint](#image-format-for-powerpoint)[](#image-format-for-powerpoint "Click to copy url")

**Syntax:** obj \<\< Image Format for PowerPoint( "Default OS format"\|"PNG"\|"JPEG" )

### [Include Responses Not in Data](#include-responses-not-in-data)[](#include-responses-not-in-data "Click to copy url")

**Syntax:** obj \<\< Include Responses Not in Data( state=0\|1 )

**Description:** Show the labels of those responses with no occurrence in the data table.

### [Initial JMP Window](#initial-jmp-window)[](#initial-jmp-window "Click to copy url")

**Syntax:** obj \<\< Initial JMP Window( "Home Window"\|"JMP Starter"\|"Window List" )

**Description:** Determines the JMP window that is created when JMP starts

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Initial JMP Window( "Home Window" ) );
```

### [Initial Log Window](#initial-log-window)[](#initial-log-window "Click to copy url")

**Syntax:** obj \<\< Initial Log Window( state=0\|1 )

**Description:** Changes the default setting for displaying the initial log window.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Initial Log Window( 1 ) );
```

### [Initial Splash Window](#initial-splash-window)[](#initial-splash-window "Click to copy url")

**Syntax:** obj \<\< Initial Splash Window( state=0\|1 )

**Description:** Changes the default setting for displaying the initial splash window.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Initial Splash Window( 1 ) );
```

### [Inside Ticks](#inside-ticks)[](#inside-ticks "Click to copy url")

**Syntax:** obj \<\< Inside Ticks( state=0\|1 )

**Description:** Changes the default setting for displaying axis tick marks on the inside of graph frames.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Inside Ticks( 1 ) );
```

### [Interactive HTML Color](#interactive-html-color)[](#interactive-html-color "Click to copy url")

**Syntax:** obj \<\< Interactive HTML Color( "Light Background"\|"Dark Background"\|"Gray Background" )

**Description:** Changes the default setting for the interactive HTML color theme.

**JMP Version Added:** 15

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Interactive HTML Color( "Light Background" ) );
```

### [Internet Open Timeout](#internet-open-timeout)[](#internet-open-timeout "Click to copy url")

**Syntax:** obj \<\< Internet Open Timeout( number )

**Description:** Internet Open will wait this many seconds before giving up.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Internet Open Timeout( 300 /* 5 minutes */ ) );
```

### [JMP Live Timeout](#jmp-live-timeout)[](#jmp-live-timeout "Click to copy url")

**Syntax:** obj \<\< JMP Live Timeout( number )

**Description:** Sets the timeout value for publishing to JMP Live. The default is 180 seconds.

**JMP Version Added:** 15

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( JMP Live Timeout( 120 ) );
```

### [JMP Theme](#jmp-theme)[](#jmp-theme "Click to copy url")

**Syntax:** obj \<\< JMP Theme( "Traditional"\|"Comfortable"\|"JMP Live"\|"JMP Clinical" )

**Description:** Switches theme for all of JMP.

**JMP Version Added:** 19

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );

restore theme = Get Preference( JMP Theme );
Set Preference( JMP Theme( "Traditional" ) );
Wait( 2 );
Set Preference( JMP Theme( "Comfortable" ) );
Wait( 2 );
Set Preference( JMP Theme( "JMP Live" ) );
Wait( 2 );
restore theme;
```

### [JSL save column groups with group name](#jsl-save-column-groups-with-group-name)[](#jsl-save-column-groups-with-group-name "Click to copy url")

**Syntax:** obj \<\< JSL save column groups with group name( state=0\|1 )

**Description:** When saving script with list of columns, use 'column group' syntax if the list of columns is a column group

**JMP Version Added:** 16

### [JSS Dir](#jss-dir)[](#jss-dir "Click to copy url")

**Syntax:** obj \<\< JSS Dir( text )

**Description:** Changes the JSS directory for development use.

**JMP Version Added:** 19

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Set Preference( JSS Dir( "C:\My\Path\To\jss\" ) );
```

### [Journal Freeze Backward Compatible](#journal-freeze-backward-compatible)[](#journal-freeze-backward-compatible "Click to copy url")

**Syntax:** obj \<\< Journal Freeze Backward Compatible( state=0\|1 )

### [Language Switch Warning](#language-switch-warning)[](#language-switch-warning "Click to copy url")

**Syntax:** obj \<\< Language Switch Warning( state=0\|1 )

**Description:** Changes the default setting for warning when detecting change in language. Note: Available on Windows only.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Language Switch Warning( 1 ) );
```

### [Laser pointer](#laser-pointer)[](#laser-pointer "Click to copy url")

**Syntax:** obj \<\< Laser pointer( "Off"\|"Purple"\|"Blue"\|"Green"\|"Yellow"\|"Orange"\|"Red" )

**Description:** Changes the default setting for displaying a laser pointer for emphasizing parts of a report.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Laser pointer( "Purple" ) );
```

### [Line Width](#line-width)[](#line-width "Click to copy url")

**Syntax:** obj \<\< Line Width( number )

**Description:** Changes the default line width for graph content.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Line Width( 2 ) );
```

### [Log Mode](#log-mode)[](#log-mode "Click to copy url")

**Syntax:** obj \<\< Log Mode( "Enhanced"\|"Text" )

**Description:** Changes the default setting for how the logs are displayed. This includes the main and project logs.

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Log Mode( "Text" ) );
```

### [Log Window Height](#log-window-height)[](#log-window-height "Click to copy url")

**Syntax:** obj \<\< Log Window Height( number )

**Description:** Changes the default setting for the size of the log window. Note: This is available on Windows only.

``` jsl
//Caution: Changing a preference will affect 
//the default behavior of JMP. 

Preferences[1] << Set( Log Window Height( 200 ) );
```

### [Major Grid Line Color](#major-grid-line-color)[](#major-grid-line-color "Click to copy url")

**Syntax:** obj \<\< Major Grid Line Color( color )

**Description:** Changes the default color of major grid lines in graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Major Grid Line Color( "Blue" ) );
```

### [Major Grid Lines](#major-grid-lines)[](#major-grid-lines "Click to copy url")

**Syntax:** obj \<\< Major Grid Lines( state=0\|1 )

**Description:** Changes the default setting for displaying major grid lines in graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Major Grid Lines( 1 ) );
```

### [Mark Menu Items Added Since](#mark-menu-items-added-since)[](#mark-menu-items-added-since "Click to copy url")

**Syntax:** obj \<\< Mark Menu Items Added Since( "None"\|"Current Version"\|"18"\|"17"\|"16"\|"15"\|"14" )

**Description:** Mark menu items newer than a particular JMP version.

**JMP Version Added:** 17

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Mark Items Added Since( "16" ) );
```

### [Marker Label Color](#marker-label-color)[](#marker-label-color "Click to copy url")

**Syntax:** obj \<\< Marker Label Color( color )

**Description:** Color of marker labels if "Marker Label Color Style" is set to "Fixed"

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Marker Label Color( "Blue" ) );
```

### [Marker Label Color Style](#marker-label-color-style)[](#marker-label-color-style "Click to copy url")

**Syntax:** obj \<\< Marker Label Color Style( "Marker Color"\|"Marker Color Faded"\|"Fixed Color" )

**Description:** Changes the default coloring style for marker labels

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Marker Label Color Style( "Marker Color" ) );
```

### [Marker Selection Mode](#marker-selection-mode)[](#marker-selection-mode "Click to copy url")

**Syntax:** obj \<\< Marker Selection Mode( "Unselected Faded"\|"Selected Larger"\|"Selected Haloed"\|"Selected Outlined"\|"Selected Same Color" )

**Description:** Changes the default setting for the marker selection mode. The default is Unselected Faded.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Marker Selection Mode( "Selection Haloed" ) );
```

### [Maximum Auto Size Column List Width](#maximum-auto-size-column-list-width)[](#maximum-auto-size-column-list-width "Click to copy url")

**Syntax:** obj \<\< Maximum Auto Size Column List Width( number )

**JMP Version Added:** 18

### [Maximum JMP Call Depth](#maximum-jmp-call-depth)[](#maximum-jmp-call-depth "Click to copy url")

**Syntax:** obj \<\< Maximum JMP Call Depth( number )

**Description:** Changes the default setting for the Maximum JMP call depth.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Maximum JMP call depth( 50 ) );
```

### [Maximum Parse Depth](#maximum-parse-depth)[](#maximum-parse-depth "Click to copy url")

**Syntax:** obj \<\< Maximum Parse Depth( number )

**Description:** Changes the default setting for the Maximum Parsing Depth. Default value is 512.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Maximum Parse Depth( 600 ) );
```

### [Maximum Symbol Evaluation Recursion Depth](#maximum-symbol-evaluation-recursion-depth)[](#maximum-symbol-evaluation-recursion-depth "Click to copy url")

**Syntax:** obj \<\< Maximum Symbol Evaluation Recursion Depth( number )

**Description:** Changes the default setting for the Maximum Symbol Evaluation Recursion Depth. Default value is 25.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Maximum Symbol Evaluation Recursion Depth( 50 ) );
```

### [Minor Grid Line Color](#minor-grid-line-color)[](#minor-grid-line-color "Click to copy url")

**Syntax:** obj \<\< Minor Grid Line Color( color )

**Description:** Changes the default color of minor grid lines in graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Minor Grid Line Color( "Black" ) );
```

### [Minor Grid Lines](#minor-grid-lines)[](#minor-grid-lines "Click to copy url")

**Syntax:** obj \<\< Minor Grid Lines( state=0\|1 )

**Description:** Changes the default setting for displaying minor grid lines in graphs.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Minor Grid Lines( 1 ) );
```

### [New Project Template](#new-project-template)[](#new-project-template "Click to copy url")

**Syntax:** obj \<\< New Project Template( text )

**Description:** File to use for new, empty projects.

**JMP Version Added:** 16

### [New character columns default to compact](#new-character-columns-default-to-compact)[](#new-character-columns-default-to-compact "Click to copy url")

**Syntax:** obj \<\< New character columns default to compact( state=0\|1 )

**Description:** New character columns or columns switched to the character data type are automatically made compact columns

**JMP Version Added:** 18

### [OAuth2 Authentication Browser](#oauth2-authentication-browser)[](#oauth2-authentication-browser "Click to copy url")

**Syntax:** obj \<\< OAuth2 Authentication Browser( text=Default )

**Description:** Sign in to OAuth2 servers with the specified browser type. Valid values are "Default", "Embedded", "External". "Default" by default.

**JMP Version Added:** 17

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set(
    Sign in to OAuth2 servers with the specified browser type( "Embedded" )
);
```

### [ODBC Allow Table Replace](#odbc-allow-table-replace)[](#odbc-allow-table-replace "Click to copy url")

**Syntax:** Preferences\[1\] \<\< Name("ODBC Allow Table Replace") ( state = 0\|1 )

**Description:** Select this option to allow ODBC table replace. This option is selected by default. Replacing an ODBC table will drop the existing table in the database and replace it with a new table.

``` jsl
//Caution: Changing a preference will
//affect the default behavior of JMP.

Preferences[1] << Name( "ODBC Allow Table Replace" )(0);
```

### [ODBC Hide Connection String](#odbc-hide-connection-string)[](#odbc-hide-connection-string "Click to copy url")

**Syntax:** obj \<\< ODBC Hide Connection String( state=0\|1 )

### [Open Text File Charset](#open-text-file-charset)[](#open-text-file-charset "Click to copy url")

**Syntax:** obj \<\< Open Text File Charset( "Best Guess"\|"ASMO-708"\|"big5"\|"cp1025"\|"cp866"\|"cp875"\|"csISO2022JP"\|"DOS-720"\|"DOS-862"\|"EUC-CN"\|"EUC-JP"\|"euc-kr"\|"GB18030"\|"gb2312"\|"hz-gb-2312"\|"IBM00858"\|"IBM00924"\|"IBM01047"\|"IBM01140"\|"IBM01141"\|"IBM01142"\|"IBM01143"\|"IBM01144"\|"IBM01145"\|"IBM01146"\|"IBM01147"\|"IBM01148"\|"IBM01149"\|"IBM037"\|"IBM1026"\|"IBM273"\|"IBM277"\|"IBM278"\|"IBM280"\|"IBM284"\|"IBM285"\|"IBM290"\|"IBM297"\|"IBM420"\|"IBM423"\|"IBM424"\|"IBM437"\|"IBM500"\|"ibm737"\|"ibm775"\|"ibm850"\|"ibm852"\|"IBM855"\|"ibm857"\|"IBM860"\|"ibm861"\|"IBM863"\|"IBM864"\|"IBM865"\|"ibm869"\|"IBM870"\|"IBM871"\|"IBM880"\|"IBM905"\|"IBM-Thai"\|"iso-2022-jp"\|"iso-2022-jp"\|"iso-2022-kr"\|"iso-8859-1"\|"iso-8859-13"\|"iso-8859-15"\|"iso-8859-2"\|"iso-8859-3"\|"iso-8859-4"\|"iso-8859-5"\|"iso-8859-6"\|"iso-8859-7"\|"iso-8859-8"\|"iso-8859-8-i"\|"iso-8859-9"\|"Johab"\|"koi8-r"\|"koi8-u"\|"ks_c_5601-1987"\|"macintosh"\|"shift_jis"\|"us-ascii"\|"utf-16"\|"utf-16BE"\|"utf-32"\|"utf-7"\|"utf-8"\|"windows-1250"\|"windows-1251"\|"Windows-1252"\|"windows-1253"\|"windows-1254"\|"windows-1255"\|"windows-1256"\|"windows-1257"\|"windows-1258"\|"windows-874"\|"x-Chinese-CNS"\|"x-Chinese-Eten"\|"x-cp20001"\|"x-cp20003"\|"x-cp20004"\|"x-cp20005"\|"x-cp20261"\|"x-cp20269"\|"x-cp20936"\|"x-cp20949"\|"x-cp50227"\|"x-EBCDIC-KoreanExtended"\|"x-IA5"\|"x-IA5-German"\|"x-IA5-Norwegian"\|"x-IA5-Swedish"\|"x-iscii-as"\|"x-iscii-be"\|"x-iscii-de"\|"x-iscii-gu"\|"x-iscii-ka"\|"x-iscii-ma"\|"x-iscii-or"\|"x-iscii-pa"\|"x-iscii-ta"\|"x-iscii-te"\|"x-mac-arabic"\|"x-mac-ce"\|"x-mac-chinesesimp"\|"x-mac-chinesetrad"\|"x-mac-croatian"\|"x-mac-cyrillic"\|"x-mac-greek"\|"x-mac-hebrew"\|"x-mac-icelandic"\|"x-mac-japanese"\|"x-mac-korean"\|"x-mac-romanian"\|"x-mac-thai"\|"x-mac-turkish"\|"x-mac-ukrainian" )

**Description:** Specifies the encoding to use if no Unicode Byte Order Mark is found; the default is to guess the encoding based on the file's content.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Open Text File Charset( "utf-8" ) );
```

### [Open character columns as compact columns](#open-character-columns-as-compact-columns)[](#open-character-columns-as-compact-columns "Click to copy url")

**Syntax:** obj \<\< Open character columns as compact columns( state=0\|1 )

**Description:** Automatically open character columns as compact columns when JMP determines it's advantageous

**JMP Version Added:** 18

### [Open files from outside projects in](#open-files-from-outside-projects-in)[](#open-files-from-outside-projects-in "Click to copy url")

**Syntax:** obj \<\< Open files from outside projects in( "No Project"\|"Open Project or No Project"\|"Open Project or New Project"\|"New Project" )

**JMP Version Added:** 16

### [Outline Close Orientation](#outline-close-orientation)[](#outline-close-orientation "Click to copy url")

**Syntax:** obj \<\< Outline Close Orientation( "Auto"\|"Horizontal"\|"Vertical" )

**Description:** Option for Outline Boxes to collapse vertically to save horizontal space

### [Parallel Data Table Column Decompression](#parallel-data-table-column-decompression)[](#parallel-data-table-column-decompression "Click to copy url")

**Syntax:** obj \<\< Parallel Data Table Column Decompression( state=0\|1 )

**Description:** Changes the default setting for decompressing columns in parallel. The default value is enabled. Turning off the option might allow some very large tables to load.

``` jsl
//Caution: Changing a preference will
//affect the default behavior of JMP.

Preferences[1] << Set( Parallel Data Table Column Decompression( 0 ) );
```

### [Partial Selection Indicator](#partial-selection-indicator)[](#partial-selection-indicator "Click to copy url")

**Syntax:** obj \<\< Partial Selection Indicator( "None"\|"Bar"\|"Pie"\|"Waffle" )

**Description:** How a partial selection of a group is indicated.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Partial Selection Mode( "Bar" ) );
```

### [Platform Launch Actions](#platform-launch-actions)[](#platform-launch-actions "Click to copy url")

**Syntax:** obj \<\< Platform Launch Actions( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Platform Launch Actions( 1 ) );
```

### [Prefer DSN-less ODBC Connection Strings](#prefer-dsn-less-odbc-connection-strings)[](#prefer-dsn-less-odbc-connection-strings "Click to copy url")

**Syntax:** Preferences\[1\] \<\< Name("Prefer DSN-less ODBC Connection Strings") ( state = 0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Name( "Prefer DSN-less ODBC Connection Strings" )(1);
```

### [Preserve SAS formats when exporting to SAS](#preserve-sas-formats-when-exporting-to-sas)[](#preserve-sas-formats-when-exporting-to-sas "Click to copy url")

**Syntax:** obj \<\< Preserve SAS formats when exporting to SAS( state=0\|1 )

**Description:** Changes the default setting for preserving SAS formats when exporting to SAS.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Preserve SAS formats when exporting to SAS( 1 ) );
```

### [Preserve SAS variable names when exporting to SAS](#preserve-sas-variable-names-when-exporting-to-sas)[](#preserve-sas-variable-names-when-exporting-to-sas "Click to copy url")

**Syntax:** obj \<\< Preserve SAS variable names when exporting to SAS( state=0\|1 )

**Description:** Changes the default setting for preserving SAS variable names when exporting to SAS.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Preserve SAS variable names when exporting to SAS( 1 ) );
```

### [Print Data Grid as is](#print-data-grid-as-is)[](#print-data-grid-as-is "Click to copy url")

**Syntax:** obj \<\< Print Data Grid as is( state=0\|1 )

**Description:** Changes the default setting for printing the data grid as it appears on the screen.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Print Data Grid as is( 1 ) );
```

### [Prompt to save when closing summary tables](#prompt-to-save-when-closing-summary-tables)[](#prompt-to-save-when-closing-summary-tables "Click to copy url")

**Syntax:** obj \<\< Prompt to save when closing summary tables( state=0\|1 )

**Description:** Prompt or no prompt when closing the summary table.

**JMP Version Added:** 14

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Close report action( "Prompt" ) );
```

### [Proxy Port](#proxy-port)[](#proxy-port "Click to copy url")

**Syntax:** obj \<\< Proxy Port( number )

**Description:** Use the specified proxy port.

**JMP Version Added:** 15

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Proxy Port( 80 ) );
```

### [Proxy Server](#proxy-server)[](#proxy-server "Click to copy url")

**Syntax:** obj \<\< Proxy Server( text )

**Description:** Use the specified proxy.

**JMP Version Added:** 15

``` jsl

//Caution: Changing a preference will 
//affect the default behavior of JMP.

url = "http:://myproxy.com:80";
Preferences[1] << Set( Proxy Server( url ) );
```

### [Proxy User](#proxy-user)[](#proxy-user "Click to copy url")

**Syntax:** obj \<\< Proxy User( text )

**Description:** The user name and password to use for proxy authentication. \[user name\]:\[password\]

**JMP Version Added:** 15

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Proxy User( "clark%20kent:superman" ) );
```

### [Reopen the initial JMP window on last window close](#reopen-the-initial-jmp-window-on-last-window-close)[](#reopen-the-initial-jmp-window-on-last-window-close "Click to copy url")

**Syntax:** obj \<\< Reopen the initial JMP window on last window close( state=0\|1 )

**Description:** Determines whether the initial JMP window is automatically reopened when the last JMP window is closed

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Reopen the initial JMP window on last window close( 1 ) );
```

### [Report Invalid Display Box Messages](#report-invalid-display-box-messages)[](#report-invalid-display-box-messages "Click to copy url")

**Syntax:** obj \<\< Report Invalid Display Box Messages( state=0\|1 )

**Description:** Changes the default setting for outputting errors on invalid messages for display boxes.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Report Invalid Display Box Messages( 1 ) );
```

### [Report JSL warnings and errors interactively](#report-jsl-warnings-and-errors-interactively)[](#report-jsl-warnings-and-errors-interactively "Click to copy url")

**Syntax:** obj \<\< Report JSL warnings and errors interactively( state=0\|1 )

**Description:** Warnings and errors from submitting JSL will be logged and shown interactively. When disabled, warnings and errors will only be logged

**JMP Version Added:** 15

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Report JSL warnings and errors interactively( 1 ) );
```

### [Report Recent Problems](#report-recent-problems)[](#report-recent-problems "Click to copy url")

**Syntax:** obj \<\< Report Recent Problems( state=0\|1 )

### [Report Snapshot On Close](#report-snapshot-on-close)[](#report-snapshot-on-close "Click to copy url")

**Syntax:** obj \<\< Report Snapshot On Close( state=0\|1 )

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Report Snapshot On Close( 1 ) );
```

### [Row Editor Always Show All Columns](#row-editor-always-show-all-columns)[](#row-editor-always-show-all-columns "Click to copy url")

**Syntax:** obj \<\< Row Editor Always Show All Columns( state=0\|1 )

**Description:** If checked, the row editor will shows all the columns in the data table whether or not there are selected columns.

**JMP Version Added:** 16

### [Ruler Tool Units](#ruler-tool-units)[](#ruler-tool-units "Click to copy url")

**Syntax:** obj \<\< Ruler Tool Units( "Kilometers"\|"Miles" )

**Description:** Changes the units shown by the graph tools ruler when used on a map in Graph Builder.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Ruler Tool Units( "Miles" ) );
```

### [SAS Automatically Generate ODS results](#sas-automatically-generate-ods-results)[](#sas-automatically-generate-ods-results "Click to copy url")

**Syntax:** obj \<\< SAS Automatically Generate ODS results( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "SAS Automatically Generate ODS results"n( 1 ) );
```

### [SAS Connect to CAS with SAS Viya](#sas-connect-to-cas-with-sas-viya)[](#sas-connect-to-cas-with-sas-viya "Click to copy url")

**Syntax:** obj \<\< SAS Connect to CAS with SAS Viya( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "SAS Connect to CAS with SAS Viya"n( 1 ) );
```

### [SAS Data Import Close Warning](#sas-data-import-close-warning)[](#sas-data-import-close-warning "Click to copy url")

**Syntax:** obj \<\< SAS Data Import Close Warning( state=0\|1 )

**JMP Version Added:** 19

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "SAS Data Import Close Warning"n( 0 ) );
```

### [SAS Data Import Uses Labels](#sas-data-import-uses-labels)[](#sas-data-import-uses-labels "Click to copy url")

**Syntax:** obj \<\< SAS Data Import Uses Labels( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "SAS Data Import Uses Labels"n( 1 ) );
```

### [SAS Import generated datasets into JMP](#sas-import-generated-datasets-into-jmp)[](#sas-import-generated-datasets-into-jmp "Click to copy url")

**Syntax:** obj \<\< SAS Import generated datasets into JMP( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "SAS Import generated datasets into JMP"n( 1 ) );
```

### [SAS ODS Results Format](#sas-ods-results-format)[](#sas-ods-results-format "Click to copy url")

**Syntax:** obj \<\< SAS ODS Results Format( "HTML"\|"TEXT" )

### [SAS ODS Style](#sas-ods-style)[](#sas-ods-style "Click to copy url")

**Syntax:** obj \<\< SAS ODS Style( text=Statistical )

**Description:** "Statistical" by default.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "SAS ODS Style"n( "HTMLBlue" ) );
```

### [SAS Organize results in JMP project](#sas-organize-results-in-jmp-project)[](#sas-organize-results-in-jmp-project "Click to copy url")

**Syntax:** obj \<\< SAS Organize results in JMP project( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "SAS Organize results in JMP project"n( 1 ) );
```

### [SAS Transport Use UTF8](#sas-transport-use-utf8)[](#sas-transport-use-utf8 "Click to copy url")

**Syntax:** obj \<\< SAS Transport Use UTF8( state=0\|1 )

**Description:** Change the default character encoding for Transport files to UTF-8

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( SAS Transport Use UTF8( 1 ) );
```

### [SPSSMultiResponseDelimiter](#spssmultiresponsedelimiter)[](#spssmultiresponsedelimiter "Click to copy url")

**Syntax:** obj \<\< SPSSMultiResponseDelimiter( text=\| )

**Description:** "\|" by default.

**JMP Version Added:** 16

### [Save Data Table Columns GZ Compressed](#save-data-table-columns-gz-compressed)[](#save-data-table-columns-gz-compressed "Click to copy url")

**Syntax:** obj \<\< Save Data Table Columns GZ Compressed( state=0\|1 )

**Description:** Changes the default setting for saving data tables in a GZip compressed format.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Save Data Table Columns GZ Compressed( 1 ) );
```

### [Save Image DPI](#save-image-dpi)[](#save-image-dpi "Click to copy url")

**Syntax:** obj \<\< Save Image DPI( number )

**Description:** Specifies a DPI setting to use when saving images, otherwise a default value is used.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Save Image DPI( 300 ) );
```

### [Save Journals GZ Compressed](#save-journals-gz-compressed)[](#save-journals-gz-compressed "Click to copy url")

**Syntax:** obj \<\< Save Journals GZ Compressed( state=0\|1 )

**Description:** Changes the default setting for saving journals in a GZip compressed format.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Save Journals GZ Compressed( 1 ) );
```

### [Save Scripts in English](#save-scripts-in-english)[](#save-scripts-in-english "Click to copy url")

**Syntax:** obj \<\< Save Scripts in English( state=0\|1 )

**Description:** Changes the default setting for saving scripts in English rather than in the language displayed.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Save Scripts in English( 1 ) );
```

### [Save Text Files as Unicode](#save-text-files-as-unicode)[](#save-text-files-as-unicode "Click to copy url")

**Syntax:** obj \<\< Save Text Files as Unicode( state=0\|1 )

**Description:** Changes the default setting for saving text files in Unicode format.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Save Text Files as Unicode( 1 ) );
```

### [Save table with report](#save-table-with-report)[](#save-table-with-report "Click to copy url")

**Syntax:** obj \<\< Save table with report( "Embed"\|"Separate"\|"Prompt" )

**Description:** Changes how data is stored with saved reports

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Save table with report( prompt | embed | separate ) );
```

### [Save the session when exiting](#save-the-session-when-exiting)[](#save-the-session-when-exiting "Click to copy url")

**Syntax:** obj \<\< Save the session when exiting( "Always"\|"Never"\|"Prompt" )

**Description:** Changes the default setting for saving the session on exiting JMP.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Save table with report( "Prompt" ) );
```

### [Selected Marker Color](#selected-marker-color)[](#selected-marker-color "Click to copy url")

**Syntax:** obj \<\< Selected Marker Color( color )

**Description:** Changes the color of selected markers when using Selected Same Color in Markers Selection Mode

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Selected Marker Color( "Cyan" ) );
```

### [Semantic formatting](#semantic-formatting)[](#semantic-formatting "Click to copy url")

**Syntax:** obj \<\< Semantic formatting

**Description:** Creates a semantic format that is used when its criteria matches the current report context.

**JMP Version Added:** 17

**Example 1**

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

dt = Open( "$SAMPLE_DATA/Big Class.jmp" );
dt << Oneway( Y( :height ), X( :sex ), Means( 1 ), Mean Diamonds( 1 ) );

Preferences(
    Semantic formatting(
        Add Semantic Format(
            Format Name( "My Format 1" ),
            Semantic Format( Format( "Fixed Dec", 11, 1 ) ),
            Criteria(
                Object Name( "*mean*" ),
                Outline Path( "** :: Means for Oneway Anova" )
            )
        ),
        Add Semantic Format(
            Format Name( "My Format 2" ),
            Semantic Format( Format( "Fixed Dec", 11, 2 ) ),
            Criteria(
                Object Name( "*mean*" ),
                Outline Path( "** :: Means for Oneway Anova" ),
                Row Name( "M" )
            )
        )
    )
);
```

**Example 2**

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Semantic formatting( Clear ) );
```

### [Sequential Color Theme](#sequential-color-theme)[](#sequential-color-theme "Click to copy url")

**Syntax:** obj \<\< Sequential Color Theme( "name" )

**Description:** Changes the default setting for the continuous color theme appearing in all graphs.

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Show( Get Preference( Continuous Color Theme ) );
Set Preference( Sequential Color Theme( "Green to Purple" ) );
Show( Get Preference( Sequential Color Theme ) );
```

### [Set](#set)[](#set "Click to copy url")

**Syntax:** obj \<\< Set

**Description:** Sets a specified preference.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 
Preferences[1] << Set( Show the Tip of the Day at startup( 1 ) );
```

### [Set ODBC Primary Key as Link ID](#set-odbc-primary-key-as-link-id)[](#set-odbc-primary-key-as-link-id "Click to copy url")

**Syntax:** Preferences\[1\] \<\< Name("Set ODBC Primary Key as Link ID") ( state = 0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Name( "Set ODBC Primary Key as Link ID" )(1);
```

### [Shade Alternate Table Rows](#shade-alternate-table-rows)[](#shade-alternate-table-rows "Click to copy url")

**Syntax:** obj \<\< Shade Alternate Table Rows( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Shade Alternate Table Rows( 1 ) );
```

### [Shade Table Cells](#shade-table-cells)[](#shade-table-cells "Click to copy url")

**Syntax:** obj \<\< Shade Table Cells( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Shade Table Cells( 1 ) );
```

### [Shade Table Headings](#shade-table-headings)[](#shade-table-headings "Click to copy url")

**Syntax:** obj \<\< Shade Table Headings( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Shade Table Headings( 1 ) );
```

### [Shape Boundary Color](#shape-boundary-color)[](#shape-boundary-color "Click to copy url")

**Syntax:** obj \<\< Shape Boundary Color( color )

**Description:** Changes the default setting for the color of shape boundaries drawn on all graphs, such as background maps.

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Shape Boundary Color( "Black" ) );
```

### [Show Alternate Column Name](#show-alternate-column-name)[](#show-alternate-column-name "Click to copy url")

**Syntax:** obj \<\< Show Alternate Column Name( state=0\|1 )

**Description:** Change default setting for showing alternate name in dialog and data table columns panel

### [Show Personalization at startup](#show-personalization-at-startup)[](#show-personalization-at-startup "Click to copy url")

**Syntax:** obj \<\< Show Personalization at startup( state=0\|1 )

**Description:** Personalization Dialog will show the next time JMP starts.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Show Personalization at startup( 1 ) );
```

### [Show SAS Log](#show-sas-log)[](#show-sas-log "Click to copy url")

**Syntax:** obj \<\< Show SAS Log( "Never"\|"Always"\|"On Error" )

### [Show Search box on Columns Panel](#show-search-box-on-columns-panel)[](#show-search-box-on-columns-panel "Click to copy url")

**Syntax:** obj \<\< Show Search box on Columns Panel( state=0\|1 )

**Description:** Show the search edit box on the columns panel by default

**JMP Version Added:** 16

### [Show Status Bar](#show-status-bar)[](#show-status-bar "Click to copy url")

**Syntax:** obj \<\< Show Status Bar( state=0\|1 )

**Description:** Changes the default setting for displaying the Status Bar.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Show Status Bar( 1 ) );
```

### [Show conditional formatting](#show-conditional-formatting)[](#show-conditional-formatting "Click to copy url")

**Syntax:** obj \<\< Show conditional formatting( "Always"\|"Screen only"\|"Never" )

**Description:** Changes the default setting for displaying the conditional formatting in reports.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Show conditional formatting( "Always" ) );
```

### [Show menu tips](#show-menu-tips)[](#show-menu-tips "Click to copy url")

**Syntax:** obj \<\< Show menu tips( state=0\|1 )

**Description:** Changes the default setting for displaying the menu tips that appear when you hover the mouse over a red triangle menu item.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Show menu tips( 1 ) );
```

### [Show missing data bars or bins in summary graphs](#show-missing-data-bars-or-bins-in-summary-graphs)[](#show-missing-data-bars-or-bins-in-summary-graphs "Click to copy url")

**Syntax:** obj \<\< Show missing data bars or bins in summary graphs( state=0\|1 )

**Description:** Whether missing data bars or bins are initially displayed in summary graphs. Whatever the value here, they can be toggled for individual summary graphs by right-clicking on the summary graph and selecting "Missing values bar" or "Missing values bin".

**JMP Version Added:** 16

### [Show semantic formatting](#show-semantic-formatting)[](#show-semantic-formatting "Click to copy url")

**Syntax:** obj \<\< Show semantic formatting( "Always"\|"No Row Matching"\|"Never" )

**Description:** Changes the default setting for using semantic formatting in reports. Possible values are: "Always", "No Row Matching", and "Never". Use "No Row Matching" to disable row-specific semantic formats.

**JMP Version Added:** 17

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Show semantic formatting( "Always" ) );
```

### [Show summary graphs below column names](#show-summary-graphs-below-column-names)[](#show-summary-graphs-below-column-names "Click to copy url")

**Syntax:** obj \<\< Show summary graphs below column names( state=0\|1 )

**Description:** Whether the summary graphs are initially displayed in the data table between the column names and the data cells, if the number of rows is under some performance threshold (3 million rows). Whatever the initial state, the display can be toggled for an individual data table with the icon next to the column names.

**JMP Version Added:** 15

### [Show the Quick Start at startup](#show-the-quick-start-at-startup)[](#show-the-quick-start-at-startup "Click to copy url")

**Syntax:** obj \<\< Show the Quick Start at startup( state=0\|1 )

**Description:** Changes the default setting for displaying the Quick Start window.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Show the Quick Start at startup( 1 ) );
```

### [Summary Graph Continuous Color](#summary-graph-continuous-color)[](#summary-graph-continuous-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Continuous Color( color )

**Description:** Set the color for continuous data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Continuous Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Continuous Highlight Color](#summary-graph-continuous-highlight-color)[](#summary-graph-continuous-highlight-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Continuous Highlight Color( color )

**Description:** Set the highlight color for continuous data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Continuous Highlight Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Continuous Missing Color](#summary-graph-continuous-missing-color)[](#summary-graph-continuous-missing-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Continuous Missing Color( color )

**Description:** Set the color for missing continuous data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Continuous Missing Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Continuous Missing Highlight Color](#summary-graph-continuous-missing-highlight-color)[](#summary-graph-continuous-missing-highlight-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Continuous Missing Highlight Color( color )

**Description:** Set the highlight color for missing continuous data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Continuous Missing Highlight Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Name Ordered Color](#summary-graph-name-ordered-color)[](#summary-graph-name-ordered-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Name Ordered Color( color )

**Description:** Set the color for name-ordered data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Name Ordered Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Name Ordered Highlight Color](#summary-graph-name-ordered-highlight-color)[](#summary-graph-name-ordered-highlight-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Name Ordered Highlight Color( color )

**Description:** Set the highlight color for name-ordered data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Name Ordered Highlight Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Other Color](#summary-graph-other-color)[](#summary-graph-other-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Other Color( color )

**Description:** Set the color for the other bar in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Other Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Other Highlight Color](#summary-graph-other-highlight-color)[](#summary-graph-other-highlight-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Other Highlight Color( color )

**Description:** Set the highlight color for the other bar in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Other Highlight Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Run Chart Color](#summary-graph-run-chart-color)[](#summary-graph-run-chart-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Run Chart Color( color )

**Description:** Set the color for the other bar in summary graphs and data filters

**JMP Version Added:** 18

``` jsl
//Caution: Changing a preference will
//affect the default behavior of JMP.

Preferences( Summary Graph Run Chart Color( RGB Color( 0.5, 0.1, 0.9 ) ) );
```

### [Summary Graph Size Ordered Color](#summary-graph-size-ordered-color)[](#summary-graph-size-ordered-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Size Ordered Color( color )

**Description:** Set the color for size-ordered data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Size Ordered Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Summary Graph Size Ordered Highlight Color](#summary-graph-size-ordered-highlight-color)[](#summary-graph-size-ordered-highlight-color "Click to copy url")

**Syntax:** obj \<\< Summary Graph Size Ordered Highlight Color( color )

**Description:** Set the highlight color for size-ordered data in summary graphs and data filters

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Summary Graph Size Ordered Highlight Color( RGB Color( 0.5, 0.9, 0.9 ) ) );
```

### [Suppress Formula Eval on Open](#suppress-formula-eval-on-open)[](#suppress-formula-eval-on-open "Click to copy url")

**Syntax:** obj \<\< Suppress Formula Eval on Open( state=0\|1 )

**Description:** Changes the default setting for suppressing formula evaluations when opening a data table.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Suppress Formula Eval on Open( 1 ) );
```

### [Table Column Borders](#table-column-borders)[](#table-column-borders "Click to copy url")

**Syntax:** obj \<\< Table Column Borders( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Table Column Borders( 1 ) );
```

### [Table Column Group Borders](#table-column-group-borders)[](#table-column-group-borders "Click to copy url")

**Syntax:** obj \<\< Table Column Group Borders( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Table Column Group Borders( 1 ) );
```

### [Table Heading Column Borders](#table-heading-column-borders)[](#table-heading-column-borders "Click to copy url")

**Syntax:** obj \<\< Table Heading Column Borders( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Table Heading Column Borders( 1 ) );
```

### [Table Row Borders](#table-row-borders)[](#table-row-borders "Click to copy url")

**Syntax:** obj \<\< Table Row Borders( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Table Row Borders( 1 ) );
```

### [Task Bar Strategy](#task-bar-strategy)[](#task-bar-strategy "Click to copy url")

**Syntax:** obj \<\< Task Bar Strategy( "All windows"\|"Main window only"\|"Main and data tables" )

**Description:** Determines which JMP windows are displayed on the Windows task bar

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Task Bar Strategy( "All Windows" ) );
```

### [Transparent background for report PNG images](#transparent-background-for-report-png-images)[](#transparent-background-for-report-png-images "Click to copy url")

**Syntax:** obj \<\< Transparent background for report PNG images( state=0\|1 )

**Description:** When reports or portions of reports are saved as PNG images, the background will be transparent.

**JMP Version Added:** 14

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Transparent background for report PNG images( 1 ) );
```

### [Underline Table Headings](#underline-table-headings)[](#underline-table-headings "Click to copy url")

**Syntax:** obj \<\< Underline Table Headings( state=0\|1 )

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Underline Table Headings( 1 ) );
```

### [Use Excel Labels as Headings](#use-excel-labels-as-headings)[](#use-excel-labels-as-headings "Click to copy url")

**Syntax:** obj \<\< Use Excel Labels as Headings( "Use best guess"\|"Always"\|"Never" )

**Description:** Changes the default setting for importing Excel labels as JMP Column names when opening Excel files.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use Excel Labels as Headings( "Always" ) );
```

### [Use Greek letters](#use-greek-letters)[](#use-greek-letters "Click to copy url")

**Syntax:** obj \<\< Use Greek letters( state=0\|1 )

**Description:** Changes the default setting for enabling Greek letters in JMP reports.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use Greek letters( 1 ) );
```

### [Use JMP Locale Settings](#use-jmp-locale-settings)[](#use-jmp-locale-settings "Click to copy url")

**Syntax:** obj \<\< Use JMP Locale Settings( state=0\|1 )

**Description:** Changes the default behavior for displaying number, date and currency formats. Note: This is available on Windows only.

``` jsl
//Caution: Changing a preference will affect 
//the default behavior of JMP. 

Preferences[1] << Set( Use JMP Locale Settings( 1 ) );
```

### [Use Numerical Ordering](#use-numerical-ordering)[](#use-numerical-ordering "Click to copy url")

**Syntax:** obj \<\< Use Numerical Ordering( state=0\|1 )

**Description:** Configure column sorting for new columns so that text containing numbers is sorted in numerical order. Columns converted to character type will also be affected if they don't already contain a Value Order property.

**JMP Version Added:** 16

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences( Use Numerical Ordering( 0 ) );
```

### [Use Project Log](#use-project-log)[](#use-project-log "Click to copy url")

**Syntax:** obj \<\< Use Project Log( "Always"\|"If Open"\|"Never" )

**Description:** Whether to send log messages generated by scripts and windows in a project to the project log window (instead of the main log window)

**JMP Version Added:** 16

### [Use SPSS labels for column names during import](#use-spss-labels-for-column-names-during-import)[](#use-spss-labels-for-column-names-during-import "Click to copy url")

**Syntax:** obj \<\< Use SPSS labels for column names during import( state=0\|1 )

**Description:** Changes the default setting for importing SPSS labels as JMP Column names when opening SPSS files.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use SPSS labels for column names during import( 1 ) );
```

### [Use Thousands Separator](#use-thousands-separator)[](#use-thousands-separator "Click to copy url")

**Syntax:** obj \<\< Use Thousands Separator( state=0\|1 )

**Description:** Changes the default setting for using the thousands separator in numeric output.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use Thousands Separator( 1 ) );
```

### [Use Triple-S Labels as Headings](#use-triple-s-labels-as-headings)[](#use-triple-s-labels-as-headings "Click to copy url")

**Syntax:** obj \<\< Use Triple-S Labels as Headings( state=0\|1 )

**Description:** Changes the default setting for use of labels as column names for Triple-S variables

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( "Use Triple-S Labels as Headings"n( 1 ) );
```

### [Use a Floating Window for Data Filters](#use-a-floating-window-for-data-filters)[](#use-a-floating-window-for-data-filters "Click to copy url")

**Syntax:** obj \<\< Use a Floating Window for Data Filters( state=0\|1 )

**Description:** When set, data filters use a window that floats above their data tables and associated windows. Otherwise, data filters use a window that can be arranged with other windows normally.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use a Floating Window for Data Filters( 1 ) );
```

### [Use an Asterisk with the PValue Format](#use-an-asterisk-with-the-pvalue-format)[](#use-an-asterisk-with-the-pvalue-format "Click to copy url")

**Syntax:** obj \<\< Use an Asterisk with the PValue Format( state=0\|1 )

**Description:** PValue format will append an asterisk in numeric columns

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use an Asterisk with the PValue Format( 1 ) );
```

### [Use column references in Dispatch](#use-column-references-in-dispatch)[](#use-column-references-in-dispatch "Click to copy url")

**Syntax:** obj \<\< Use column references in Dispatch( state=0\|1 )

**Description:** When saving report customizations, use column references instead of strings when referring to customized elements. This generates scripts that are more robust against column name changes. Note that customizations that are saved using this preference might work only in JMP 18.0 and newer.

**JMP Version Added:** 18

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use column references in Dispatch( 1 ) );
```

### [Use math symbols](#use-math-symbols)[](#use-math-symbols "Click to copy url")

**Syntax:** obj \<\< Use math symbols( state=0\|1 )

**Description:** Changes the default setting for enabling math symbols in JMP reports.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Preferences[1] << Set( Use math symbols( 1 ) );
```

### [Virtual Join Auto Open Linked Table](#virtual-join-auto-open-linked-table)[](#virtual-join-auto-open-linked-table "Click to copy url")

**Syntax:** obj \<\< Virtual Join Auto Open Linked Table( state=0\|1 )

**Description:** Automatically open the data table that this column references.

**JMP Version Added:** 16

### [Virtual Join Use Linked Column Name](#virtual-join-use-linked-column-name)[](#virtual-join-use-linked-column-name "Click to copy url")

**Syntax:** obj \<\< Virtual Join Use Linked Column Name( state=0\|1 )

**Description:** Name the virtual column with the linked column's name.

**JMP Version Added:** 16

### [Warn that compact columns cannot be opened in JMP 17 and earlier](#warn-that-compact-columns-cannot-be-opened-in-jmp-17-and-earlier)[](#warn-that-compact-columns-cannot-be-opened-in-jmp-17-and-earlier "Click to copy url")

**Syntax:** obj \<\< Warn that compact columns cannot be opened in JMP 17 and earlier( state=0\|1 )

**Description:** The compact file format cannot be opened in JMP 17 and earlier.

**JMP Version Added:** 18

### [Warn when referenced table name has changed](#warn-when-referenced-table-name-has-changed)[](#warn-when-referenced-table-name-has-changed "Click to copy url")

**Syntax:** obj \<\< Warn when referenced table name has changed( state=0\|1 )

**Description:** Give a warning message when a virtually linked (referenced) table's name has changed.

**JMP Version Added:** 15

## [Platform Preferences](#platform-preferences)[](#platform-preferences "Click to copy url")

### [Item Messages](#item-messages_1)[](#item-messages_1 "Click to copy url")

#### [Get](#get_1)[](#get_1 "Click to copy url")

**Syntax:** obj \<\< Get

**Description:** Returns the script for setting a specified preference.

``` jsl
a = Platform Preferences[1] << Get( Distribution );
Show( a );
```

#### [Get Script](#get-script_1)[](#get-script_1 "Click to copy url")

**Syntax:** obj \<\< Get Script

**Description:** Returns the script for setting the preferences.

``` jsl
a = Platform Preferences[1] << Get Script;
Show( a );
```

#### [Set](#set_1)[](#set_1 "Click to copy url")

**Syntax:** obj \<\< Set

**Description:** Sets a specified preference.

``` jsl
//Caution: Changing a preference will 
//affect the default behavior of JMP. 

Platform Preferences[1] << Set( Distribution( Vertical( 1 ) ) );
```

[ Previous](Predictor%20Screening.html "Predictor Screening") [Next ](Principal%20Components.html "Principal Components")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
