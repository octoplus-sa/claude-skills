# JSL Function Index

Flat alphabetical index of JSL functions extracted from the JMP 19 JSL Syntax Reference. Each entry shows the category and PDF page where the function is documented. For full signatures + descriptions, open the matching `syntax/<category>.md` file.

**How to use this file:** grep here first for any function name. If found, jump to the per-category file for full docs. If not found, the function may be a message (see `syntax/messages-*.md`) or may not exist — treat "not found here" as a strong red flag against using it.

---

## Assignment Functions

File: `syntax/assignment-functions.md`

- `Add To()` — p.29
- `Assign()` — p.30
- `Divide To()` — p.30
- `For Add To()` — p.29
- `For Multiply To()` — p.31
- `Multiply To()` — p.30
- `Post Increment()` — p.31
- `PostDecrement()` — p.31
- `To()` — p.29

## Character Functions

File: `syntax/character-functions.md`

- `BLOB To Char()` — p.32
- `BLOB To Matrix()` — p.33
- `Base()` — p.35
- `Char()` — p.33
- `Char To BLOB()` — p.34
- `Char To Hex()` — p.34
- `Collapse Whitespace()` — p.35
- `Concat()` — p.35
- `Concat To()` — p.36
- `Contains()` — p.37
- `Contains Item()` — p.37
- `Ends With()` — p.38
- `For SubtractTo()` — p.32
- `Hex()` — p.34
- `Hex To BLOB()` — p.38
- `Hex To Char()` — p.38
- `Hex To Number()` — p.39
- `Include Boundary Delimiters()` — p.40
- `Item()` — p.39
- `Left()` — p.40
- `Length()` — p.40
- `Lowercase()` — p.41
- `Munger()` — p.41
- `Num()` — p.41
- `Pad To()` — p.35
- `Regex()` — p.42
- `Repeat()` — p.42
- `Right()` — p.38
- `Starts With()` — p.43
- `Substr()` — p.43
- `Subtract To()` — p.32
- `Text Score()` — p.44
- `Titlecase()` — p.44
- `Trim()` — p.45
- `Trim Whitespace()` — p.45
- `Unmatched()` — p.40
- `Uppercase()` — p.45
- `Use Locale()` — p.33
- `Word()` — p.40
- `Write()` — p.38
- `XPath Query()` — p.46

## Character Pattern Functions

File: `syntax/character-pattern-functions.md`

- `Boolean 0()` — p.51
- `Expr()` — p.56
- `Match()` — p.52
- `Pat Abort()` — p.47
- `Pat Altern()` — p.47
- `Pat Any()` — p.47
- `Pat Arb()` — p.47
- `Pat Arb No()` — p.48
- `Pat Arbno()` — p.48
- `Pat At()` — p.48
- `Pat Break()` — p.49
- `Pat Concat()` — p.49
- `Pat Conditional()` — p.50
- `Pat Fail()` — p.50
- `Pat Fence()` — p.50
- `Pat Immediate()` — p.48
- `Pat Len()` — p.51
- `Pat Look Ahead()` — p.51
- `Pat Look Behind()` — p.51
- `Pat Match()` — p.48
- `Pat Not Any()` — p.52
- `Pat Pos()` — p.53
- `Pat R Pos()` — p.53
- `Pat R Tab()` — p.53
- `Pat Regex()` — p.53
- `Pat Rem()` — p.54
- `Pat Repeat()` — p.54
- `Pat Span()` — p.54
- `Pat String()` — p.55
- `Pat Succeed()` — p.55
- `Pat Tab()` — p.55
- `Pat Test()` — p.55
- `Regex Match()` — p.56
- `Show()` — p.48

## Comparison Functions

File: `syntax/comparison-functions.md`

- `Equal()` — p.59
- `Greater()` — p.59
- `Is Missing()` — p.60
- `Less()` — p.61
- `Less Equal Less()` — p.62
- `Less Less Equal()` — p.61
- `Not Equal()` — p.62

## Conditional and Logical Functions

File: `syntax/conditional-and-logical-functions.md`

- `Across()` — p.65
- `And()` — p.63
- `AndMZ()` — p.63
- `Break()` — p.64
- `Choose()` — p.64
- `Continue()` — p.64
- `Count()` — p.65
- `Empty()` — p.70
- `Filter Each()` — p.64
- `For Each()` — p.66
- `For Each Row()` — p.68
- `IfMZ()` — p.69
- `IfMax()` — p.68
- `IfMin()` — p.69
- `Interpolate()` — p.69
- `Is Associative Array()` — p.70
- `Is Empty()` — p.70
- `Is Expr()` — p.70
- `Is Name()` — p.70
- `Is Namespace()` — p.70
- `Is Number()` — p.71
- `Is Scriptable()` — p.71
- `Is String()` — p.71
- `MatchMZ()` — p.71
- `Or()` — p.72
- `OrMZ()` — p.72
- `Output()` — p.74
- `Return()` — p.73
- `Step()` — p.73
- `Stop()` — p.73
- `The Match()` — p.71
- `The MatchMZ()` — p.71
- `The Return()` — p.73
- `Transform Each()` — p.73

## Constant Functions

File: `syntax/constant-functions.md`

- `Pi()` — p.75
- `While()` — p.75
- `Zero Or Missing()` — p.75

## Date and Time Functions

File: `syntax/date-and-time-functions.md`

- `Abbrev Date()` — p.76
- `As Date()` — p.76
- `Date DMY()` — p.77
- `Date Difference()` — p.76
- `Date Increment()` — p.77
- `Date MDY()` — p.78
- `Day()` — p.78
- `Day Of Week()` — p.78
- `Day Of Year()` — p.79
- `Days In Month()` — p.79
- `Format()` — p.80
- `Format Date()` — p.81
- `HP Time()` — p.81
- `Hour()` — p.81
- `ISO Year()` — p.83
- `In Days()` — p.81
- `In Hours()` — p.82
- `In Minutes()` — p.82
- `In Weeks()` — p.82
- `In Years()` — p.82
- `Informat()` — p.82
- `Is Leap Year()` — p.83
- `Long Date()` — p.83
- `MDYHMS()` — p.83
- `Minute()` — p.83
- `Month()` — p.83
- `Parse Date()` — p.82
- `Quarter()` — p.84
- `Second()` — p.84
- `Short Date()` — p.84
- `Tick Seconds()` — p.84
- `Time Of Day()` — p.84
- `Today()` — p.84

## Discrete Probability Functions

File: `syntax/discrete-probability-functions.md`

- `Beta Binomial Distribution()` — p.85
- `Beta Binomial Probability()` — p.85
- `Beta Binomial Quantile()` — p.86
- `Binomial()` — p.86
- `Binomial Distribution()` — p.86
- `Binomial Probability()` — p.87
- `Binomial Quantile()` — p.87
- `Gamma Poisson Distribution()` — p.87
- `Gamma Poisson Probability()` — p.88
- `Gamma Poisson Quantile()` — p.88
- `Hypergeometric Distribution()` — p.89
- `Hypergeometric Probability()` — p.89
- `Neg Binomial Distribution()` — p.89
- `Neg Binomial Probability()` — p.90
- `Poisson()` — p.88
- `Poisson Distribution()` — p.90
- `Poisson Probability()` — p.90
- `Week Of Year()` — p.85
- `Year()` — p.85

## Display Functions

File: `syntax/display-functions.md`

- `Align()` — p.104
- `Alpha Shape()` — p.91
- `Border Box()` — p.91
- `Bottom()` — p.92
- `Box()` — p.104
- `Box Plot Seg()` — p.92
- `Bubble Plot()` — p.113
- `Busy Light()` — p.93
- `Button Box()` — p.93
- `Calendar Box()` — p.94
- `Cell Plot()` — p.94
- `Check Box()` — p.95
- `Col Box()` — p.95
- `Col List Box()` — p.96
- `Col Span Box()` — p.97
- `Color()` — p.118
- `Combo Box()` — p.97
- `Context Box()` — p.98
- `Contour Seg()` — p.98
- `Current Journal()` — p.99
- `Current Report()` — p.99
- `Current Window()` — p.99
- `Data Filter Context Box()` — p.99
- `Data Filter Source Box()` — p.100
- `Data Table()` — p.96
- `Data Table Box()` — p.100
- `Data Table Col Box()` — p.100
- `Destination()` — p.108
- `Dialog()` — p.100
- `Excerpt Box()` — p.100
- `Expr As Picture()` — p.100
- `File()` — p.110
- `Filter Col Selector()` — p.101
- `Folder()` — p.109
- `Frame Size()` — p.92
- `Get Project()` — p.101
- `Get Project List()` — p.101
- `Get Window()` — p.101
- `Get Window List()` — p.102
- `Global Box()` — p.103
- `Graph()` — p.103
- `Graph 3D Box()` — p.103
- `Graph Box()` — p.92
- `H Center Box()` — p.103
- `H List Box()` — p.104
- `H Scroll Box()` — p.104
- `H Sheet Box()` — p.104
- `H Splitter Box()` — p.104
- `Hier Box()` — p.105
- `Hist Seg()` — p.105
- `Icon Box()` — p.106
- `If Box()` — p.106
- `If Seg()` — p.106
- `Journal Box()` — p.107
- `Line Seg()` — p.107
- `Lines Seg()` — p.107
- `Lineup Box()` — p.107
- `List Box()` — p.107
- `Location()` — p.93
- `Marker Seg()` — p.107
- `Matrix Box()` — p.108
- `MaxItems()` — p.96
- `MaxSelected()` — p.96
- `MinItems()` — p.96
- `Mouse Box()` — p.108
- `MultiSelect()` — p.122
- `Names Default To Here()` — p.119
- `New Image()` — p.109
- `New Project()` — p.109
- `New Window()` — p.94
- `Number Col Box()` — p.111
- `Number Col Edit Box()` — p.97
- `Number Edit Box()` — p.111
- `On Change()` — p.96
- `Open()` — p.109
- `Outline Box()` — p.112
- `Page Box()` — p.120
- `Page Break Box()` — p.112
- `Panel Box()` — p.112
- `Path()` — p.117
- `Picture Box()` — p.112
- `Platform()` — p.112
- `Plot Col Box()` — p.113
- `Poisson Quantile()` — p.91
- `Poly Seg()` — p.113
- `Popup Box()` — p.113
- `Radio Box()` — p.114
- `Range Slider Box()` — p.114
- `Report()` — p.114
- `Rescale Slider()` — p.118
- `Row States()` — p.117
- `Scene Box()` — p.114
- `Script Box()` — p.115
- `Scroll Box()` — p.115
- `Set Width()` — p.118
- `Shape Seg()` — p.117
- `Sheet Box()` — p.117
- `Sides()` — p.92
- `Size()` — p.93
- `Sizes()` — p.113
- `Slider()` — p.117
- `Slider Box()` — p.96
- `Source()` — p.108
- `Spacer Box()` — p.118
- `Spin Box()` — p.118
- `Splitter Box()` — p.119
- `State()` — p.106
- `String Col Box()` — p.95
- `String Col Edit Box()` — p.119
- `Tab Box()` — p.120
- `Tab List Box()` — p.120
- `Tab Page Box()` — p.120
- `Table Box()` — p.95
- `Text Box()` — p.121
- `Text Edit Box()` — p.121
- `This Project()` — p.122
- `Tips()` — p.97
- `Title Position()` — p.113
- `Top()` — p.92
- `Transparency()` — p.98
- `Tree Box()` — p.122
- `Tree Node()` — p.122
- `Triangulation()` — p.123
- `Type()` — p.96
- `Use H Splitter Box()` — p.119
- `Using Set Tip()` — p.97
- `V Center Box()` — p.123
- `V List Box()` — p.123
- `V Scroll Box()` — p.123
- `V Sheet Box()` — p.124
- `V Splitter Box()` — p.124
- `Vertical()` — p.92
- `Web Browser Box()` — p.124
- `Width()` — p.101
- `Window()` — p.125
- `Windows()` — p.108
- `Wrap List Box()` — p.125
- `X()` — p.113
- `X Scale()` — p.98
- `Y()` — p.113
- `Y Scale()` — p.92
- `YScale()` — p.103
- `Yname()` — p.103

## Expression Functions

File: `syntax/expression-functions.md`

- `Arg()` — p.126
- `Arg Expr()` — p.126
- `Eval Expr()` — p.126
- `Extract Expr()` — p.127
- `Head()` — p.127
- `Head Expr()` — p.127
- `Head Name()` — p.127
- `Head Name Expr()` — p.127
- `N Arg()` — p.127
- `N Arg Expr()` — p.127

## File Functions

File: `syntax/file-functions.md`

- `Allow Undo()` — p.131
- `BLOB()` — p.139
- `Charset()` — p.139
- `Close()` — p.128
- `Close All()` — p.128
- `Close Database Connection()` — p.128
- `Close Log()` — p.129
- `Column Names Start()` — p.141
- `Columns()` — p.141
- `Compress Allow List Check()` — p.141
- `Compress Character Columns()` — p.141
- `Compress Numeric Columns()` — p.141
- `Concatenate Worksheets()` — p.141
- `Convert File Path()` — p.129
- `Copy Directory()` — p.129
- `Copy File()` — p.130
- `Create Concatenation Column()` — p.141
- `Create Database Connection()` — p.130
- `Create Directory()` — p.131
- `Creation Date()` — p.131
- `Data Starts()` — p.141
- `Debug JSL()` — p.141
- `Delete Directory()` — p.131
- `Delete File()` — p.132
- `Directory Exists()` — p.132
- `Driver Prompt()` — p.131
- `EOF Other()` — p.142
- `EOL Other()` — p.142
- `End Of Field()` — p.141
- `End Of Line()` — p.142
- `File Exists()` — p.132
- `File Size()` — p.132
- `Files In Directory()` — p.133
- `Find All()` — p.133
- `First()` — p.142
- `Force()` — p.138
- `Get Default Directory()` — p.134
- `Get Excel Worksheets()` — p.134
- `Get File Search Path()` — p.129
- `Get Path Variable()` — p.134
- `Google Sheet Export()` — p.135
- `Google Sheet Import()` — p.135
- `Guess()` — p.136
- `HTML Table()` — p.142
- `Ignore Columns()` — p.142
- `Imported Column Names()` — p.149
- `Invisible()` — p.136
- `Is Directory()` — p.136
- `Is Directory Writable()` — p.136
- `Is File()` — p.136
- `Is File Writable()` — p.136
- `JSON Literal()` — p.138
- `JSON To Data Table()` — p.136
- `JSON To List()` — p.138
- `Labels()` — p.143
- `Last()` — p.143
- `Last Modification Date()` — p.138
- `Line Separator()` — p.139
- `Load Text File()` — p.138
- `Method()` — p.140
- `Move Directory()` — p.139
- `Move File()` — p.140
- `Name Expr()` — p.128
- `New IP21 Client()` — p.140
- `Open Database()` — p.145
- `Parse JSON()` — p.146
- `Password()` — p.140
- `Pick Directory()` — p.146
- `Pick File()` — p.147
- `Private()` — p.136
- `Project()` — p.128
- `Quarantine Action()` — p.143
- `Random()` — p.143
- `Recursive()` — p.130
- `Rename Directory()` — p.148
- `Rename File()` — p.148
- `Run JSL()` — p.143
- `Save Flag()` — p.147
- `Save Text File()` — p.148
- `Scan Whole File()` — p.143
- `Select Columns()` — p.143
- `Set Default Directory()` — p.148
- `Set File Search Path()` — p.129
- `Set Path Variable()` — p.149
- `Show Files()` — p.146
- `Table Contains Column Headers()` — p.144
- `TripleS Import()` — p.149
- `Worksheet Settings()` — p.144
- `Worksheets()` — p.145

## Financial Functions

File: `syntax/financial-functions.md`

- `Double Declining Balance()` — p.150
- `Future Value()` — p.150
- `Interest Payment()` — p.150
- `Interest Rate()` — p.151
- `Net Present Value()` — p.152
- `Payment()` — p.153
- `Present Value()` — p.153
- `Principal Payment()` — p.154
- `Straight Line Depreciation()` — p.154
- `Sum Of Years Digits Depreciation()` — p.154

## Graphics Functions

File: `syntax/graphics-functions.md`

- `Add Color Theme()` — p.155
- `Arc()` — p.156
- `Arrow()` — p.156
- `Back Color()` — p.156
- `Char To Path()` — p.157
- `Circle()` — p.157
- `Color Theme()` — p.155
- `Color To HLS()` — p.158
- `Color To RGB()` — p.158
- `Contour()` — p.158
- `Contour Function()` — p.159
- `Drag Line()` — p.160
- `Drag Marker()` — p.160
- `Drag Polygon()` — p.160
- `Drag Rect()` — p.161
- `Drag Text()` — p.161
- `Fill()` — p.168
- `Fill Color()` — p.161
- `Fill Pattern()` — p.162
- `Floor()` — p.166
- `Get Color Theme Detail()` — p.162
- `Get Color Theme Names()` — p.162
- `Gradient Function()` — p.162
- `H Line()` — p.163
- `H Size()` — p.163
- `HLS Color()` — p.164
- `Handle()` — p.163
- `Heat Color()` — p.163
- `In Path()` — p.164
- `In Polygon()` — p.164
- `J()` — p.166
- `Level Color()` — p.165
- `Line()` — p.165
- `Line Style()` — p.165
- `Marker()` — p.166
- `Marker Size()` — p.166
- `Mousetrap()` — p.166
- `New Heat Image()` — p.166
- `Normal Contour()` — p.167
- `Oval()` — p.167
- `Path To Char()` — p.168
- `Pen Color()` — p.168
- `Pen Size()` — p.168
- `Pick Color()` — p.168
- `Pie()` — p.169
- `Pixel Line To()` — p.169
- `Pixel Move To()` — p.169
- `Pixel Origin()` — p.169
- `Pixel Path()` — p.170
- `Pixel Text()` — p.171
- `PixelRadius()` — p.157
- `Polygon()` — p.169
- `Polygon Area()` — p.170
- `Polygon Centroid()` — p.170
- `RGB Color()` — p.172
- `Rect()` — p.171
- `Remove Color Theme()` — p.171
- `Reverse Gradient()` — p.167
- `Scale Type()` — p.167
- `Show Missing Color()` — p.167
- `Text()` — p.172
- `Text Color()` — p.172
- `Text Font()` — p.172
- `Text Size()` — p.172
- `True()` — p.164
- `V Line()` — p.173
- `V Size()` — p.173
- `X Function()` — p.173
- `X Origin()` — p.173
- `X Range()` — p.173

## HTTP Functions

File: `syntax/http-functions.md`

- `Decode 64 Blob()` — p.174
- `Encode 64 Blob()` — p.174
- `XY Function()` — p.174
- `Y Function()` — p.174
- `Y Origin()` — p.174
- `Y Range()` — p.174

## JMPEX R Functions

File: `syntax/jmpex-r-functions.md`

- `Async()` — p.283
- `R Submit File()` — p.283

## List Functions

File: `syntax/list-functions.md`

- `As List()` — p.175
- `Concat Items()` — p.175
- `Delimiter()` — p.177
- `Eval List()` — p.175
- `Insert()` — p.176
- `Insert Into()` — p.176
- `Is List()` — p.176
- `Items()` — p.177
- `List()` — p.177
- `N Items()` — p.177
- `Remove()` — p.178
- `Remove From()` — p.178
- `Reverse()` — p.178
- `Reverse Into()` — p.179
- `Shift()` — p.179
- `Shift Into()` — p.179
- `Sort List()` — p.179
- `Sort List Into()` — p.179
- `Substitute()` — p.180
- `Substitute Into()` — p.180
- `Words()` — p.181

## MATLAB Integration Functions

File: `syntax/matlab-integration-functions.md`

- `Colored()` — p.186
- `Colors()` — p.186
- `Echo()` — p.182
- `Excluded()` — p.186
- `Expand()` — p.183
- `Get()` — p.182
- `Hidden()` — p.186
- `Labeled()` — p.186
- `MATLAB Connect()` — p.182
- `MATLAB Control()` — p.182
- `MATLAB Execute()` — p.183
- `MATLAB Get()` — p.183
- `MATLAB Get Graphics()` — p.184
- `MATLAB Init()` — p.183
- `MATLAB Is Connected()` — p.185
- `MATLAB JMP Name To MATLAB Name()` — p.185
- `MATLAB Send()` — p.185
- `MATLAB Send File()` — p.187
- `MATLAB Submit()` — p.187
- `MATLAB Submit File()` — p.187
- `MATLAB Term()` — p.187
- `Markered()` — p.186
- `Markers()` — p.186
- `Numeric()` — p.184
- `Selected()` — p.186
- `Send()` — p.186
- `Visible()` — p.182

## Matrix Functions

File: `syntax/matrix-functions.md`

- `As Table()` — p.201
- `B Spline Coef()` — p.189
- `Bivariate()` — p.201
- `CDF()` — p.189
- `Chol Update()` — p.190
- `Cholesky()` — p.190
- `Correlation()` — p.190
- `Covariance()` — p.191
- `Design()` — p.191
- `Design Last()` — p.192
- `Design Nom()` — p.193
- `Design Ord()` — p.193
- `DesignF()` — p.193
- `Det()` — p.194
- `Diag()` — p.194
- `Direct()` — p.195
- `Direct Product()` — p.195
- `Distance()` — p.195
- `E Div()` — p.195
- `E Max()` — p.195
- `E Min()` — p.196
- `E Mult()` — p.196
- `Eigen()` — p.196
- `Estimate Bartlett Factor Score()` — p.196
- `Estimate Factor Score()` — p.197
- `Fourier Basis Coef()` — p.197
- `G Inverse()` — p.197
- `Generalized()` — p.197
- `H Direct Product()` — p.198
- `Hough Line Transform()` — p.198
- `Identity()` — p.198
- `Index()` — p.198
- `Inv()` — p.199
- `Inv Update()` — p.199
- `Inverse()` — p.199
- `Is Matrix()` — p.199
- `KDTable()` — p.199
- `L()` — p.190
- `Least Squares Solve()` — p.201
- `Linear Regression()` — p.201
- `Loc()` — p.202
- `Loc Max()` — p.202
- `Loc Min()` — p.202
- `Loc NonMissing()` — p.202
- `Loc Sorted()` — p.203
- `Matrix()` — p.203
- `Matrix Mult()` — p.203
- `Matrix Rank()` — p.204
- `Mode()` — p.204
- `Multivariate Normal Impute()` — p.204
- `N Col()` — p.205
- `N Cols()` — p.205
- `NAngle()` — p.198
- `NChooseK Matrix()` — p.204
- `NRadius()` — p.198
- `Ortho()` — p.205
- `Ortho Poly()` — p.205
- `P Spline Coef()` — p.205
- `Parallel Assign()` — p.206
- `Print Matrix()` — p.206
- `QR()` — p.207
- `Random SVD()` — p.207
- `Rank()` — p.207
- `Rank Index()` — p.207
- `Ranking()` — p.207
- `Ranking Tie()` — p.208
- `SVD()` — p.211
- `Scoring Impute()` — p.208
- `Shape()` — p.208
- `Solve()` — p.209
- `Sort Ascending()` — p.209
- `Sort Descending()` — p.209
- `Sparse SVD()` — p.209
- `Spline Coef()` — p.210
- `Spline Eval()` — p.210
- `Spline Smooth()` — p.211
- `Sweep()` — p.211
- `Trace()` — p.211
- `Transpose()` — p.211
- `V Concat()` — p.212
- `V Concat To()` — p.212
- `V Max()` — p.212
- `V Mean()` — p.212
- `V Median()` — p.212
- `V Min()` — p.212
- `V Quantile()` — p.212
- `V Robust Standardize()` — p.213
- `V Standardize()` — p.213
- `V Std()` — p.213
- `V Sum()` — p.213
- `VPTree()` — p.214
- `Varimax()` — p.213
- `Vec Diag()` — p.214
- `Vec Quadratic()` — p.214
- `Wavelet Basis Coef()` — p.215

## Numeric Functions

File: `syntax/numeric-functions.md`

- `Abs()` — p.216
- `Ceiling()` — p.216
- `Derivative()` — p.216
- `Integrate()` — p.217
- `Invert Expr()` — p.218
- `Mod()` — p.218
- `Modulo()` — p.218
- `Normal Integrate()` — p.218
- `Num Deriv()` — p.218
- `StoreInfo()` — p.218

## Optimization Functions

File: `syntax/optimization-functions.md`

- `Constrained Maximize()` — p.219
- `Constrained Minimize()` — p.220
- `Desirability()` — p.221
- `LPSolve()` — p.221
- `Maximize()` — p.222
- `Minimize()` — p.222
- `Num Deriv2()` — p.219
- `Round()` — p.219
- `Simplify Expr()` — p.219
- `The Num Deriv()` — p.219

## Probability Functions

File: `syntax/probability-functions.md`

- `Beta Density()` — p.223
- `Beta Distribution()` — p.224
- `Beta Quantile()` — p.224
- `Cauchy Density()` — p.224
- `Cauchy Distribution()` — p.225
- `Cauchy Quantile()` — p.225
- `ChiSquare Density()` — p.225
- `ChiSquare Distribution()` — p.226
- `ChiSquare Log CDistribution()` — p.226
- `ChiSquare Log Density()` — p.226
- `ChiSquare Log Distribution()` — p.226
- `ChiSquare Noncentrality()` — p.226
- `ChiSquare Quantile()` — p.227
- `Dunnett P Value()` — p.227
- `Dunnett Quantile()` — p.227
- `ExGaussian Density()` — p.228
- `ExGaussian Distribution()` — p.228
- `ExGaussian Quantile()` — p.228
- `Exp Density()` — p.229
- `Exp Distribution()` — p.229
- `Exp Quantile()` — p.229
- `Exponential Density()` — p.229
- `Exponential Distribution()` — p.229
- `Exponential Quantile()` — p.229
- `F Density()` — p.230
- `F Distribution()` — p.230
- `F Log CDistribution()` — p.230
- `F Log Density()` — p.231
- `F Log Distribution()` — p.231
- `F Noncentrality()` — p.231
- `F Power()` — p.231
- `F Quantile()` — p.232
- `F Sample Size()` — p.232
- `FDR Adjust()` — p.232
- `Frechet Density()` — p.233
- `Frechet Distribution()` — p.233
- `Frechet Quantile()` — p.233
- `GLog Density()` — p.236
- `GLog Distribution()` — p.237
- `GLog Quantile()` — p.237
- `Gamma Density()` — p.234
- `Gamma Distribution()` — p.234
- `Gamma Log CDistribution()` — p.234
- `Gamma Log Density()` — p.234
- `Gamma Log Distribution()` — p.234
- `Gamma Quantile()` — p.234
- `GenGamma Density()` — p.235
- `GenGamma Distribution()` — p.235
- `GenGamma Quantile()` — p.236
- `IGamma()` — p.234
- `Johnson Sb Density()` — p.237
- `Johnson Sb Distribution()` — p.238
- `Johnson Sb Quantile()` — p.238
- `Johnson Sl Density()` — p.238
- `Johnson Sl Distribution()` — p.239
- `Johnson Sl Quantile()` — p.239
- `Johnson Su Density()` — p.240
- `Johnson Su Distribution()` — p.240
- `Johnson Su Quantile()` — p.240
- `LEV Density()` — p.241
- `LEV Distribution()` — p.241
- `LEV Quantile()` — p.241
- `LogGenGamma Density()` — p.242
- `LogGenGamma Distribution()` — p.242
- `LogGenGamma Quantile()` — p.243
- `Logistic Density()` — p.243
- `Logistic Distribution()` — p.243
- `Logistic Quantile()` — p.244
- `Loglogistic Density()` — p.244
- `Loglogistic Distribution()` — p.245
- `Loglogistic Quantile()` — p.245
- `Lognormal Density()` — p.245
- `Lognormal Distribution()` — p.246
- `Lognormal Quantile()` — p.246
- `Normal Biv Distribution()` — p.246
- `Normal Density()` — p.246
- `Normal Distribution()` — p.247
- `Normal Log CDistribution()` — p.247
- `Normal Log Density()` — p.247
- `Normal Log Distribution()` — p.247
- `Normal Mixture Density()` — p.248
- `Normal Mixture Distribution()` — p.248
- `Normal Mixture Quantile()` — p.248
- `Normal Quantile()` — p.248
- `Probit()` — p.248
- `SEV Density()` — p.248
- `SEV Distribution()` — p.249
- `SEV Quantile()` — p.249
- `SHASH Density()` — p.249
- `SHASH Distribution()` — p.250
- `SHASH Quantile()` — p.250
- `Tukey HSD P Value()` — p.252
- `Tukey HSD Quantile()` — p.252
- `Weibull Density()` — p.253
- `Weibull Distribution()` — p.253
- `Weibull Quantile()` — p.253

## Programming Functions

File: `syntax/programming-functions.md`

- `As Boolean()` — p.254
- `As C Expr()` — p.254
- `As Column()` — p.254
- `As Constant()` — p.255
- `As Global()` — p.255
- `As JSON Expr()` — p.255
- `As JavaScript Expr()` — p.255
- `As Name()` — p.256
- `As Namespace()` — p.256
- `As Python Expr()` — p.256
- `As SAS Expr()` — p.256
- `As Scoped()` — p.257
- `Associative Array()` — p.257
- `Class Exists()` — p.257
- `Clear Globals()` — p.257
- `Clear Log()` — p.258
- `Clear Symbols()` — p.258
- `Define Class()` — p.258
- `Delete()` — p.259
- `Delete Classes()` — p.259
- `Delete Globals()` — p.259
- `Delete Namespaces()` — p.259
- `Delete Symbols()` — p.259
- `Eval()` — p.260
- `Eval Insert()` — p.260
- `Eval Insert Into()` — p.260
- `Exit()` — p.261
- `Function()` — p.261
- `Get Class Names()` — p.262
- `Get Classes()` — p.262
- `Get Environment Variable()` — p.262
- `Get Locale Setting()` — p.262
- `Get Log()` — p.263
- `Get Namespace Names()` — p.263
- `Get Namespaces()` — p.263
- `Globals()` — p.271
- `Include()` — p.264
- `Include File List()` — p.264
- `Is Class()` — p.264
- `Is Log Open()` — p.265
- `Local()` — p.265
- `Local Here()` — p.265
- `Lock Globals()` — p.265
- `Lock Namespaces()` — p.265
- `Lock Symbols()` — p.266
- `Log Capture()` — p.266
- `NameExpr()` — p.256
- `Namespace()` — p.267
- `Namespace Exists()` — p.267
- `New Namespace()` — p.267
- `New Object()` — p.267
- `Open Log()` — p.267
- `Parameter()` — p.268
- `Parse()` — p.268
- `Print()` — p.268
- `Quit()` — p.261
- `Recurse()` — p.269
- `Save Log()` — p.269
- `Set Environment Variable()` — p.269
- `Show Classes()` — p.269
- `Show Globals()` — p.270
- `Show Namespaces()` — p.270
- `Show Symbols()` — p.270
- `Throw()` — p.270
- `Try()` — p.265
- `Unlock Globals()` — p.271
- `Unlock Symbols()` — p.271
- `Wait()` — p.271

## Python Integration Functions

File: `syntax/python-integration-functions.md`

- `Python Connect()` — p.272
- `Python Create JPIP CMD()` — p.273
- `Python Disconnect()` — p.273
- `Python Execute()` — p.273
- `Python Get()` — p.274
- `Python Get Graphics()` — p.275
- `Python Get Version()` — p.275
- `Python Init()` — p.276
- `Python Install Packages()` — p.276
- `Python Send()` — p.275
- `Python Send File()` — p.277
- `Python Submit()` — p.275
- `Watch()` — p.272
- `Wild()` — p.272
- `Wild List()` — p.272

## R Integration Functions

File: `syntax/r-integration-functions.md`

- `Python Submit File()` — p.278
- `Python Term()` — p.278
- `R Connect()` — p.278
- `R Control()` — p.278
- `R Execute()` — p.279
- `R Get()` — p.279
- `R Get Graphics()` — p.280
- `R Get Version()` — p.280
- `R Init()` — p.280
- `R Is Connected()` — p.280
- `R Name()` — p.281
- `R Send()` — p.281
- `R Send File()` — p.282
- `R Submit()` — p.282

## Random Functions

File: `syntax/random-functions.md`

- `Col Shuffle()` — p.287
- `Formula()` — p.298
- `Make KFold Formula()` — p.288
- `Make Validation Formula()` — p.288
- `Random Beta()` — p.289
- `Random Beta Binomial()` — p.289
- `Random Binomial()` — p.289
- `Random Category()` — p.289
- `Random Cauchy()` — p.290
- `Random ChiSquare()` — p.290
- `Random ExGaussian()` — p.290
- `Random Exp()` — p.290
- `Random F()` — p.291
- `Random Frechet()` — p.291
- `Random GLog()` — p.292
- `Random Gamma()` — p.291
- `Random Gamma Poisson()` — p.291
- `Random GenGamma()` — p.292
- `Random Geometric()` — p.292
- `Random Index()` — p.292
- `Random Integer()` — p.292
- `Random Johnson Sb()` — p.292
- `Random Johnson Sl()` — p.293
- `Random Johnson Su()` — p.293
- `Random LEV()` — p.293
- `Random LogGenGamma()` — p.294
- `Random Logistic()` — p.294
- `Random Loglogistic()` — p.294
- `Random Lognormal()` — p.294
- `Random Multivariate Normal()` — p.294
- `Random Negative Binomial()` — p.295
- `Random Normal()` — p.295
- `Random Normal Mixture()` — p.295
- `Random Poisson()` — p.295
- `Random Reset()` — p.296
- `Random SEV()` — p.296
- `Random SHASH()` — p.296
- `Random Seed State()` — p.296
- `Random Shuffle()` — p.296
- `Random Triangular()` — p.297
- `Random Uniform()` — p.297
- `Random Weibull()` — p.297
- `Resample Freq()` — p.298
- `Uniform()` — p.297

## Row Functions

File: `syntax/row-functions.md`

- `Col Stored Value()` — p.299
- `Column()` — p.300
- `Column Name()` — p.300
- `Current Data Table()` — p.301
- `Data Table List()` — p.304
- `Dif()` — p.302
- `Dim()` — p.302
- `Get Data Table()` — p.301
- `Get Data Table List()` — p.302
- `Lag()` — p.302
- `Mean()` — p.299
- `N Row()` — p.302
- `N Rows()` — p.302
- `N Table()` — p.303
- `New Column()` — p.303
- `New Table()` — p.303
- `Row()` — p.304
- `Sequence()` — p.304
- `Stored Value()` — p.299
- `Subscript()` — p.304
- `Suppress Formula Eval()` — p.304
- `The Like()` — p.303
- `Use Project()` — p.302

## Row State Functions

File: `syntax/row-state-functions.md`

- `As Row State()` — p.305
- `Color Of()` — p.305
- `Color State()` — p.306
- `Combine States()` — p.306
- `Excluded State()` — p.306
- `Hidden State()` — p.307
- `Hue State()` — p.307
- `Labeled State()` — p.307
- `Marker Of()` — p.307
- `Marker State()` — p.307
- `Row State()` — p.307
- `Selected State()` — p.308
- `Shade State()` — p.308

## SQL Functions

File: `syntax/sql-functions.md`

- `As SQL Expr()` — p.309
- `Compatible()` — p.309
- `Complete()` — p.310
- `Connection()` — p.310
- `From()` — p.310
- `New SQL Query()` — p.309
- `Query()` — p.310
- `QueryName()` — p.310
- `Select()` — p.309
- `Table()` — p.310

## Statistical Functions

File: `syntax/statistical-functions.md`

- `ARIMA Forecast()` — p.312
- `After()` — p.316
- `Arc Finder()` — p.311
- `Before()` — p.316
- `Best Partition()` — p.312
- `ByVar()` — p.318
- `Col Cumulative Sum()` — p.312
- `Col Max()` — p.313
- `Col Maximum()` — p.313
- `Col Mean()` — p.313
- `Col Median()` — p.314
- `Col Min()` — p.314
- `Col Minimum()` — p.314
- `Col Mode()` — p.315
- `Col Moving Average()` — p.315
- `Col N Missing()` — p.316
- `Col Number()` — p.317
- `Col Quantile()` — p.317
- `Col Rank()` — p.318
- `Col Simple Exponential Smoothing()` — p.319
- `Col Standardize()` — p.319
- `Col Std Dev()` — p.320
- `Col Sum()` — p.320
- `Cumulative Sum()` — p.312
- `Distribution()` — p.321
- `Elements()` — p.311
- `Fit Censored()` — p.321
- `Fit Circle()` — p.322
- `Freq()` — p.326
- `Group()` — p.311
- `Hier Clust()` — p.322
- `HoldParm()` — p.321
- `IRT Ability()` — p.322
- `KDE()` — p.322
- `LenthPSE()` — p.323
- `Max()` — p.323
- `Max Number Arcs()` — p.311
- `Max Radius()` — p.311
- `Max Radius Error()` — p.311
- `Maximum()` — p.323
- `Median()` — p.324
- `Min()` — p.324
- `Min Arc Points()` — p.311
- `Min Distance()` — p.311
- `Min Radius()` — p.311
- `Minimum()` — p.324
- `Moving Average()` — p.315
- `N Missing()` — p.324
- `Normal Tolerance Factor()` — p.324
- `Number()` — p.324
- `Product()` — p.324
- `Quantile()` — p.325
- `Range()` — p.325
- `Robust PCA()` — p.325
- `SSQ()` — p.326
- `Std Dev()` — p.325
- `Sum()` — p.320
- `Summarize()` — p.326
- `Summarize YByX()` — p.326
- `Summation()` — p.326
- `Variables()` — p.311
- `Weight()` — p.321
- `Weighting()` — p.316
- `YHigh()` — p.321
- `YLow()` — p.321
- `Z()` — p.321

## Transcendental Functions

File: `syntax/transcendental-functions.md`

- `Arrhenius()` — p.327
- `Arrhenius Inv()` — p.327
- `Beta()` — p.327
- `Box Cox Inverse Transform()` — p.328
- `Box Cox Transform()` — p.328
- `Cytometry Logicle()` — p.328
- `Cytometry Logicle Inverse()` — p.328
- `Digamma()` — p.329
- `Exp()` — p.329
- `ExpM1()` — p.329
- `FFT()` — p.329
- `Factorial()` — p.329
- `Fit Transform To Normal()` — p.330
- `For Power()` — p.332
- `Gamma()` — p.330
- `LGamma()` — p.331
- `Ln()` — p.331
- `Log()` — p.331
- `Log10()` — p.331
- `Log1P()` — p.331
- `Logist()` — p.331
- `Logist Percent()` — p.331
- `Logit()` — p.331
- `Logit Percent()` — p.332
- `N Choose K()` — p.332
- `NChooseK()` — p.332
- `Power()` — p.332
- `Root()` — p.332
- `SHASHInv()` — p.333
- `SHASHTrans()` — p.333
- `SbInv()` — p.333
- `SbTrans()` — p.333
- `Scheffe Cubic()` — p.333
- `SlInv()` — p.333
- `SlTrans()` — p.333
- `Sqrt()` — p.333

## Trigonometric Functions

File: `syntax/trigonometric-functions.md`

- `ATan()` — p.335
- `ArCos()` — p.335
- `ArSin()` — p.335
- `ArcCosH()` — p.334
- `ArcCosine()` — p.335
- `ArcSinH()` — p.335
- `ArcSine()` — p.335
- `ArcTan()` — p.335
- `ArcTanH()` — p.336
- `ArcTangent()` — p.335
- `Cos()` — p.336
- `CosH()` — p.336
- `Cosine()` — p.336
- `Sin()` — p.336
- `SinH()` — p.336
- `Sine()` — p.336
- `Squash()` — p.334
- `Squish()` — p.334
- `SuInv()` — p.334
- `SuTrans()` — p.334
- `Trigamma()` — p.334

## Utility Functions

File: `syntax/utility-functions.md`

- `Add()` — p.337
- `Analysis Destination()` — p.361
- `Annotation Font()` — p.361
- `Arguments()` — p.355
- `Auth()` — p.356
- `AutoDeclare()` — p.349
- `Axis Font()` — p.361
- `Axis Title Font()` — p.361
- `BLOB MD5()` — p.338
- `BLOB Peek()` — p.338
- `Background Color()` — p.361
- `Beep()` — p.337
- `Build Information()` — p.338
- `Calculator Boxing()` — p.361
- `Caption()` — p.338
- `Client ID()` — p.356
- `Client Secret()` — p.356
- `ColList()` — p.339
- `Column Dialog()` — p.339
- `Conditional Formatting Rules()` — p.363
- `Data Feed Messages()` — p.374
- `Data Table Font()` — p.361
- `Data Type()` — p.339
- `Datafeed()` — p.341
- `Debug Break()` — p.341
- `Decode64 BLOB()` — p.341
- `Decode64 Double()` — p.341
- `Delayed()` — p.339
- `Dialog Description()` — p.340
- `Disable JMP Live URL()` — p.341
- `DisplayName()` — p.364
- `Divide()` — p.342
- `Dynamic Link Library()` — p.375
- `EditNumber()` — p.340
- `EditText()` — p.340
- `Enable JMP Live URL()` — p.342
- `Encode64 BLOB()` — p.343
- `Encode64 Double()` — p.343
- `Evaluate OnOpen Scripts()` — p.361
- `Excel Has Labels()` — p.361
- `Excel Selection()` — p.361
- `Executable()` — p.365
- `Faure Quasi Random Sequence()` — p.343
- `File Location Settings()` — p.361
- `Font()` — p.339
- `Font Size()` — p.339
- `Footers()` — p.362
- `For Add()` — p.337
- `Foreground Color()` — p.361
- `Formula Font()` — p.361
- `Get Addin()` — p.343
- `Get Addins()` — p.343
- `Get Addr Info()` — p.344
- `Get Clipboard()` — p.344
- `Get Name Info()` — p.344
- `Get Platform Preference()` — p.345
- `Get Platform Preferences()` — p.345
- `Get Preference()` — p.346
- `Get Preferences()` — p.346
- `Glue()` — p.346
- `Graph Background Color()` — p.361
- `Graph Builder()` — p.346
- `Graph Marker Size()` — p.362
- `Gzip Compress()` — p.347
- `Gzip Uncompress()` — p.347
- `HList()` — p.339
- `Headers()` — p.362
- `Heading Font()` — p.362
- `Help Script()` — p.340
- `Host Is()` — p.348
- `Initial JMP Starter Window()` — p.362
- `Initial Splash Window()` — p.362
- `Is Alt Key()` — p.348
- `Is Command Key()` — p.348
- `Is Context Key()` — p.348
- `Is Control Key()` — p.348
- `Is Option Key()` — p.348
- `Is Shift Key()` — p.349
- `JMP Product Name()` — p.349
- `JMP Version()` — p.349
- `JMPVersion()` — p.364
- `Line Up()` — p.340
- `LineUp()` — p.340
- `Link Library()` — p.349
- `Load DLL()` — p.349
- `LoadNow()` — p.364
- `LoadsAtStartup()` — p.364
- `Mail()` — p.350
- `Main Menu()` — p.350
- `Margins()` — p.362
- `Marker Font()` — p.362
- `Max Col()` — p.339
- `Maximum JMP Call Depth()` — p.362
- `Min Col()` — p.339
- `Minus()` — p.351
- `Model Dialog()` — p.346
- `Modeling Type()` — p.339
- `Monospaced Font()` — p.362
- `Multiple File Import()` — p.351
- `Multiply()` — p.355
- `Name()` — p.355
- `New OAuth2 Token()` — p.355
- `NotEqualTo()` — p.363
- `ODBC Suppress Internal Quoting()` — p.362
- `On Element()` — p.358
- `Open Datafeed()` — p.357
- `Open Help()` — p.357
- `Orientation()` — p.362
- `Outline Connecting Lines()` — p.362
- `Parse XML()` — p.357
- `Platform Preference()` — p.359
- `Platform Preferences()` — p.346
- `Polytope Uniform Random()` — p.360
- `Pref()` — p.360
- `Preference()` — p.360
- `Preferences()` — p.346
- `Prefs()` — p.360
- `Print Settings()` — p.362
- `RadioButtons()` — p.339
- `Read Function()` — p.364
- `Read Function If Read Function()` — p.365
- `Refresh Token()` — p.356
- `Register Addin()` — p.363
- `Revert Menu()` — p.364
- `RuleName()` — p.363
- `RuleSet()` — p.363
- `Run Program()` — p.364
- `SAS Open For Var Names()` — p.366
- `Scale()` — p.362
- `Schedule()` — p.367
- `Set Clipboard()` — p.367
- `Set Platform Preference()` — p.359
- `Set Platform Preferences()` — p.359
- `Set Preference()` — p.360
- `Set Preferences()` — p.360
- `Set Toolbar Visibility()` — p.367
- `Shortest Edit Script()` — p.368
- `Show Addin Builder Dialog()` — p.369
- `Show Addins Dialog()` — p.369
- `Show Commands()` — p.369
- `Show Explanations()` — p.362
- `Show Menu Tips()` — p.362
- `Show Preferences()` — p.370
- `Show Properties()` — p.370
- `Show Status Bar()` — p.362
- `Small Font()` — p.362
- `Sobol Quasi Random Sequence()` — p.370
- `Socket()` — p.370
- `Speak()` — p.370
- `Spoken()` — p.339
- `Start Tag()` — p.358
- `Status Msg()` — p.370
- `Subtract()` — p.371
- `Tan()` — p.337
- `TanH()` — p.337
- `Tangent()` — p.337
- `The Parameter()` — p.366
- `Thin Postscript Lines()` — p.363
- `Title()` — p.339
- `Title Font()` — p.363
- `Token URL()` — p.356
- `Unregister Addin()` — p.371
- `Unregisters()` — p.371
- `User()` — p.356
- `VList()` — p.339
- `Web()` — p.371
- `Window Icon()` — p.340
- `Window Title()` — p.340
- `Write Function()` — p.366
- `XML Attr()` — p.371
- `XML Decode()` — p.372
- `XML Encode()` — p.372
- `XML Text()` — p.372

