# Finance

*Source: [https://jsl.jmp.com/All%20Categories/Functions/Finance.html](https://jsl.jmp.com/All%20Categories/Functions/Finance.html)*

---

# [Finance](#finance)[](#finance "Click to copy url")

### [Double Declining Balance](#double-declining-balance)[](#double-declining-balance "Click to copy url")

**Syntax:** x = Double Declining Balance( cost, salvage, life, period, \<factor=2\> )

**Description:** Returns the depreciation of an asset for a specified period using the double-declining balance method or some other depreciation factor. Equivalent to the DDB function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Double Declining Balance( 10000, 100, 3, 2 );
```

### [Future Value](#future-value)[](#future-value "Click to copy url")

**Syntax:** x = Future Value( rate, nper, pmt, \<pv=0\>, \<type=0\> )

**Description:** Returns the future value of an investment based on periodic, constant payments and a constant interest rate. The type argument is 0 for end-of-period payments and 1 for beginning-of-period payments. Equivalent to the FV function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Future Value( .03, 12, 100, 0, 1 );
```

### [Interest Payment](#interest-payment)[](#interest-payment "Click to copy url")

**Syntax:** x = Interest Payment( rate, per, nper, pv, \<fv=0\>, \<type=0\> )

**Description:** Returns the interest payment for a given period for an investment based on periodic, constant payments and a constant interest rate. The type argument is 0 for end-of-period payments and 1 for beginning-of-period payments. Equivalent to the IPMT function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Payment( .05 / 12, 30 * 12, 100000 ) - Interest Payment( .05 / 12, 13, 30 * 12, 100000 )
-Principal Payment( .05 / 12, 13, 30 * 12, 100000 );
```

### [Interest Rate](#interest-rate)[](#interest-rate "Click to copy url")

**Syntax:** x = Interest Rate( nper, pmt, pv, \<fv=0\>, \<type=0\>, \<guess=0.1\> )

**Description:** Returns the interest rate per period of an annuity. The type argument is 0 for end-of-period payments and 1 for beginning-of-period payments. Equivalent to the RATE function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Interest Rate( 30 * 12, Payment( .05 / 12, 30 * 12, 100000 ), 100000 );
```

### [Internal Rate of Return](#internal-rate-of-return)[](#internal-rate-of-return "Click to copy url")

**Syntax:** x = Internal Rate of Return( values, \<guess=0.1\> ); x = Internal Rate of Return( guess, value1, value2, \<value3, ...\> )

**Description:** Returns the internal rate of return for a series of cash flows represented by the numbers in the values argument. Equivalent to the IRR function in Microsoft Excel. The second prototype of the function accepts all scalar arguments.

**JMP Version Added:** Before version 14

``` jsl
Internal Rate of Return( [-10000, 1000, 900, 950] );
Internal Rate of Return( .01, -10000, 1000, 900, 950 );
```

### [Modified Internal Rate of Return](#modified-internal-rate-of-return)[](#modified-internal-rate-of-return "Click to copy url")

**Syntax:** x = Modified Internal Rate of Return( values, finance_rate, reinvest_rate ); x = Modified Internal Rate of Return( finance_rate, reinvest_rate, value1, value2, \<value3, ...\> )

**Description:** Returns the modified internal rate of return for a series of periodic cash flows, taking into account both the cost of the investment and the interest received on reinvestment of cash. Equivalent to the MIRR function in Microsoft Excel. The second prototype of the function accepts all scalar arguments.

**JMP Version Added:** Before version 14

``` jsl
Modified Internal Rate of Return( [-10000, 1000, 900, 950], .1, -.12 );
Modified Internal Rate of Return( .1, -.12, -10000, 1000, 900, 950 );
```

### [Net Present Value](#net-present-value)[](#net-present-value "Click to copy url")

**Syntax:** x = Net Present Value( rate, values ); x = Net Present Value( rate, value1, value2, \<value3, ...\> )

**Description:** Returns the net present value of an investment by using a discount rate and a series of future payments (negative values) and income (positive values). The values argument is a one dimensional matrix. Equivalent to the NPV function in Microsoft Excel. The second prototype of the function accepts all scalar arguments.

**JMP Version Added:** Before version 14

``` jsl
Net Present Value( .05, [-10000, 1000, 900, 9500] );
Net Present Value( .05, -10000, 1000, 900, 9500 );
```

### [Number of Periods](#number-of-periods)[](#number-of-periods "Click to copy url")

**Syntax:** x = Number of Periods( rate, pmt, pv, \<fv=0\>, \<type=0\> )

**Description:** Returns the number of periods for an investment based on periodic, constant payments and a constant interest rate. The type argument is 0 for end-of-period payments and 1 for beginning-of-period payments. Equivalent to the NPER function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Number of Periods( .05 / 12, -2000, 100000 );
```

### [Payment](#payment)[](#payment "Click to copy url")

**Syntax:** x = Payment( rate, nper, pv, \<fv=0\>, \<type=0\> )

**Description:** Returns the payment for a loan based on constant payments and a constant interest rate. The type argument is 0 for end-of-period payments and 1 for beginning-of-period payments. Equivalent to the PMT function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Payment( .05 / 12, 30 * 12, 100000 ) - Interest Payment( .05 / 12, 13, 30 * 12, 100000 )
-Principal Payment( .05 / 12, 13, 30 * 12, 100000 );
```

### [Present Value](#present-value)[](#present-value "Click to copy url")

**Syntax:** x = Present Value( rate, nper, pmt, \<fv=0\>, \<type=0\> )

**Description:** Returns the present value of an investment. The type argument is 0 for end-of-period payments and 1 for beginning-of-period payments. Equivalent to the PV function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Present Value( .05 / 12, 30 * 12, 1000 );
```

### [Principal Payment](#principal-payment)[](#principal-payment "Click to copy url")

**Syntax:** x = Principal Payment( rate, per, nper, pv, \<fv=0\>, \<type=0\> )

**Description:** Returns the payment on the principal for a given period for an investment based on periodic, constant payments and a constant interest rate. The type argument is 0 for end-of-period payments and 1 for beginning-of-period payments. Equivalent to the PPMT function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Payment( .05 / 12, 30 * 12, 100000 ) - Interest Payment( .05 / 12, 13, 30 * 12, 100000 )
-Principal Payment( .05 / 12, 13, 30 * 12, 100000 );
```

### [Straight Line Depreciation](#straight-line-depreciation)[](#straight-line-depreciation "Click to copy url")

**Syntax:** x = Straight Line Depreciation( cost, salvage, life )

**Description:** Returns the straight-line depreciation of an asset for one period. Equivalent to the SLN function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Straight Line Depreciation( 1000, 100, 3 );
```

### [Sum Of Years Digits Depreciation](#sum-of-years-digits-depreciation)[](#sum-of-years-digits-depreciation "Click to copy url")

**Syntax:** x = Sum Of Years Digits Depreciation( cost, salvage, life, per )

**Description:** Returns the sum-of-years' digits depreciation of an asset for a specified period. Equivalent to the SYD function in Microsoft Excel.

**JMP Version Added:** Before version 14

``` jsl
Sum Of Years Digits Depreciation( 1000, 100, 3, 2 );
```

[ Previous](File.html "File") [Next ](Graphics.html "Graphics")

------------------------------------------------------------------------

© 2026 JMP Statistical Discovery LLC. All Rights Reserved.
