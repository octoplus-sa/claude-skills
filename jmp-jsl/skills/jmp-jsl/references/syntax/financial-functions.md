# Financial Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 150-154).

## Index (line numbers in this file)

- `Double Declining Balance()` — L23
- `Future Value()` — L40
- `Interest Payment()` — L58
- `Interest Rate()` — L83
- `Net Present Value()` — L135
- `Payment()` — L173
- `Present Value()` — L191
- `Principal Payment()` — L209
- `Straight Line Depreciation()` — L228
- `Sum Of Years Digits Depreciation()` — L240
- `Type()` — L53
---

Financial Functions

Financial Functions
Double Declining Balance(cost, salvage, life, period, <factor>)
Description

Returns the depreciation of an asset for a specified period of time. The function uses the
double-declining balance method or some other depreciation factor.
Required Arguments

cost The initial cost.
salvage The value at the end of the depreciation.
life The number of periods in the depreciation cycle.
period The length of the period, in the same units as life.
Optional Argument

factor The rate at which the balance declines. The default value is 2.
Notes

This function is equivalent to the Excel function DDB.
Future Value(rate, nper, pmt, <pv>, <Type(Boolean)>)
Description

Returns the future value of an investment that is based on periodic, constant payments
and a constant interest rate.
Required Arguments

rate The interest rate.
nper The number of periods.
pmt The constant payment.
Optional Arguments

pv The present value. The default value is 0.
Type(Boolean) 0 specifies end-of-period payments. 1 specifies beginning-of-period
payments. The default value is 0.
Notes

This function is equivalent to the Excel function FV.
Interest Payment(rate, per, nper, pv, <fv>, <Type(Boolean)>)
Description

Returns the interest payment for a given period for an investment that is based on
periodic, constant payments and a constant interest rate.

JSL Functions, Operators, and Messages
Financial Functions

151

Required Arguments

rate The interest rate.
per The period for which you want the interest.
nper The total number of periods.
pv The present value.
Optional Arguments

fv The future value. The default value is 0.
Type(Boolean) 0 specifies end-of-period payments, and 1 specifies beginning-of-period
payments. The default value is 0.
Notes

This function is equivalent to the Excel function IPMT.
Interest Rate(nper, pmt, pv, <fv>, <Type(Boolean)>, <guess>)
Description

Returns the interest rate per period of an annuity.
Required Arguments

nper The total number of periods.
pmt The constant payment.
pv The present value.
Optional Arguments

fv The future value. The default value is 0.
Type(Boolean) 0 specifies end-of-period payments, and 1 specifies beginning-of-period
payments. The default value is 0.
guess Your estimate of the rate The default value is 0.1 (10%).
Notes

This function is equivalent to the Excel function RATE.
Internal Rate of Return(values, <guess>)
Internal Rate of Return(guess, value1, value2, ...)
Description

Returns the internal rate of return for a series of cash flows in the values argument.
Arguments

values A one-dimensional matrix of values. If the second form of the function is used,
list each value separately.
guess What you think is near the result. The default value is 0.1 (10%). This argument is
required if you specify values. It is required if you specify individual values.

Financial Functions

Notes

This function is equivalent to the Excel function IRR.
Modified Internal Rate of Return(values, finance rate, reinvest rate)
Modified Internal Rate of Return(finance rate, reinvest rate, value1, value2,
...)
Description

Returns the modified internal rate of return for a series of periodic cash flows. The cost of
investment and the interest received on reinvested cash is included.
Arguments

values A one-dimensional matrix of values. If the second form of the function is used,
list each value separately.
finance rate The interest rate that you pay on the money in the cash flows.
reinvest rate The interest rate that you receive on the cash flows when you reinvest
them.
Notes

This function is equivalent to the Excel function MIRR.
Net Present Value(rate, values)
Net Present Value(rate, value1, value2, ...)
Description

Returns the net present value of an investment by using a discount rate and a series of
future payments (negative values) and income (positive values).
Arguments

rate The discount rate.
values A one-dimensional matrix of values. If the second form of the function is used,
list each value separately.
Notes

This function is equivalent to the Excel function NPV.
Number of Periods(rate, pmt, pv, <fv>, <type(0|1)>)
Description

Returns the number of periods for an investment that is based on periodic, constant
payments and a constant interest rate.
Required Arguments

rate The interest rate.
pmt The constant payment.

JSL Functions, Operators, and Messages
Financial Functions

153

pv The present value.
Optional Arguments

fv The future value. The default value is 0.
type(0|1) 0 specifies end-of-period payments, and 1 specifies beginning-of-period
payments. The default value is 0.
Notes

This function is equivalent to the Excel function NPER.
Payment(rate, nper, pv, <fv>, <type(0|1)>)
Description

Returns the payment for a loan that is based on constant payments and a constant interest
rate.
Required Arguments

rate The interest rate.
nper The total number of periods.
pv The present value.
Optional Arguments

fv The future value. The default value is 0.
type(0|1) 0 specifies end-of-period payments, and 1 specifies beginning-of-period
payments. The default value is 0.
Notes

This function is equivalent to the Excel function PMT.
Present Value(rate, nper, pmt, <fv>, <type(0|1)>)
Description

Returns the present value of an investment.
Arguments

rate The interest rate per period.
nper The total number of periods.
pmt The constant payment.
fv The future value. The default value is 0.
type(0|1) 0 specifies end-of-period payments, and 1 specifies beginning-of-period
payments. The default value is 0.
Notes

This function is equivalent to the Excel function PV.

Financial Functions

Principal Payment(rate, per, nper, pv, <fv>, <type(0|1)>)
Description

Returns the payment on the principal for a given period for an investment that is based on
periodic, constant payments and a constant interest rate.
Required Arguments

rate The interest rate per period.
per The period for which you want the interest.
nper The total number of periods.
pv The present value.
Optional Arguments

fv The future value. The default value is 0.
type(0|1) An optional switch. 0 specifies end-of-period payments, and 1 specifies
beginning-of-period payments. The default value is 0.
Notes

This function is equivalent to the Excel function PPMT.
Straight Line Depreciation(cost, salvage, life)
Description

Returns the straight-line depreciation of an asset for one period.
Arguments

cost The initial cost of the asset.
salvage The value at the end of the depreciation.
life The number of periods in the depreciation cycle.
Notes

This function is equivalent to the Excel function SLN.
Sum Of Years Digits Depreciation(cost, salvage, life, per)
Description

Returns the sum-of-years’ digits depreciation of an asset for a specified period.
Arguments

cost The initial cost of the asset.
salvage The value at the end of the depreciation.
life The number of periods in the depreciation cycle.
per The length of the period, in the same units as life.
Notes

This function is equivalent to the Excel function SYD.
