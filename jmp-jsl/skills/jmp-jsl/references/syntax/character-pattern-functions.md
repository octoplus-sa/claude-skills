# Character Pattern Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 47-56).

## Index (line numbers in this file)

- `Boolean 0()` — L282
- `Expr()` — L502
- `Match()` — L320
- `Pat Abort()` — L49
- `Pat Altern()` — L61
- `Pat Any()` — L71
- `Pat Arb No()` — L103
- `Pat Arb()` — L81
- `Pat Arbno()` — L116
- `Pat At()` — L122
- `Pat Break()` — L163
- `Pat Concat()` — L176
- `Pat Conditional()` — L192
- `Pat Fail()` — L214
- `Pat Fence()` — L226
- `Pat Immediate()` — L137
- `Pat Len()` — L265
- `Pat Look Ahead()` — L275
- `Pat Look Behind()` — L283
- `Pat Match()` — L98
- `Pat Not Any()` — L326
- `Pat Pos()` — L339
- `Pat R Pos()` — L350
- `Pat R Tab()` — L361
- `Pat Regex()` — L373
- `Pat Rem()` — L389
- `Pat Repeat()` — L400
- `Pat Span()` — L423
- `Pat String()` — L441
- `Pat Succeed()` — L451
- `Pat Tab()` — L462
- `Pat Test()` — L474
- `Regex Match()` — L514
- `Show()` — L100
---

JSL Functions, Operators, and Messages
Character Pattern Functions

47

Character Pattern Functions
Pat Abort()
Description

Constructs a quoted pattern that immediately stops the pattern match. The matcher does
not back up and retry any alternatives. Conditional assignments are not made. Immediate
assignments that were already made are kept.
Returns

0 when a match is stopped.
Argument

none
Pat Altern(pattern1, <pattern2, ...>)
Description

Constructs a quoted pattern that matches any one of the pattern arguments.
Returns

A quoted pattern.
Argument

One or more patterns.
Pat Any(string)
Description

Constructs a quoted pattern that matches a single character in the argument.
Returns

A quoted pattern.
Argument

pattern A quoted string.
Pat Arb()
Description

Constructs a quoted pattern that matches an arbitrary quoted string. It initially matches
the null quoted string. It then matches one additional character each time the pattern
matcher backs into it.
Returns

A quoted pattern.

Character Pattern Functions

Argument

none
Example
p = "the beginning" + Pat Arb() >? stuffInTheMiddle + "the end";
Pat Match( "in the beginning of the story, and not near the end, there are
three bears", p );
Show( stuffInTheMiddle );
stuffInTheMiddle = " of the story, and not near "

Pat Arb No(pattern)
Description

Constructs a quoted pattern that matches zero or more copies of pattern.
Returns

A quoted pattern.
Argument

pattern A quoted pattern to match against.
Example
adjectives = "large" | "medium" | "small" | "warm" | "cold" | "hot" | "sweet";
rc = Pat Match( "I would like a medium hot, sweet tea please",
Pat Arbno( adjectives | Pat Any(", ") ) >> adj +
("tea" | "coffee" | "milk") );
Show( rc, adj );
rc = 1;
adj = " medium hot, sweet ";

Pat At(varName)
Description

Constructs a quoted pattern that matches the null quoted string and stores the current
position in the source string into the specified JSL variable (varName). The assignment is
immediate, and the variable can be used with expr() to affect the remainder of the match.
Returns

A quoted pattern.
Argument

varName The name of a variable to store the result in.
Example
p = ":" + Pat At( listStart ) + Expr(
If( listStart == 1,
Pat Immediate( Pat Len( 3 ), early ),
Pat Immediate( Pat Len( 2 ), late )
)
);

JSL Functions, Operators, and Messages
Character Pattern Functions

early = "";
late = "";
Pat Match( ":123456789", p );
Show( early, late );
early = "";
late = "";
Pat Match( "
:123456789", p );
Show( early, late );

First this is produced:
early = "123"
late = ""

and later this:
early = ""
late = "12"

Pat Break(string)
Description

Constructs a quoted pattern that matches zero or more characters that are not in its
argument; it stops or breaks on a character in its argument. It fails if a character in its
argument is not found (in particular, it fails to match if it finds the end of the quoted
source string without finding a break character).
Returns

A quoted pattern.
Argument

string A quoted string.
Pat Concat(pattern1, pattern2 <pattern3, ...>)
Pattern1 + Pattern2 + ...
Description

Constructs a quoted pattern that matches each pattern argument in turn.
Returns

A quoted pattern.
Argument

Two or more quoted patterns.

49

Character Pattern Functions

Pat Conditional(pattern, varName)
Description

Saves the result of the quoted pattern match, if it succeeds, to a variable named as the
second argument (varName) after the match is finished.
Returns

A quoted pattern.
Arguments

pattern A quoted pattern to match against.
varName The name of a variable to store the result in.
Example
type = "undefined";
rc = Pat Match(
"green apples",
Pat Conditional( "red" | "green", type ) + " apples"
);
Show( rc, type );
rc = 1;
type = "green";

Pat Fail()
Description

Constructs a quoted pattern that fails whenever the matcher attempts to move forward
through it. The matcher backs up and tries different alternatives. If and when there are no
alternatives left, the match fails and Pat Match returns 0.
Returns

0 when a match fails.
Argument

none
Pat Fence()
Description

Constructs a pattern that succeeds and matches the quoted null string when the matcher
moves forward through it, but fails when the matcher tries to back up through it. It is a
one-way trap door that can be used to optimize some matches.
Returns

1 when the match succeeds, 0 otherwise.
Argument

none

JSL Functions, Operators, and Messages
Character Pattern Functions

Pat Immediate(pattern, varName)
Description

Saves the result of the pattern match to a variable named as the second argument
(varName) immediately.
Returns

A quoted pattern.
Arguments

pattern A quoted pattern to match against.
varName The name of a variable to store the result in.
Example
type = "undefined";
rc = Pat Match(
"green apples",
("red" | "green") >> type + " pears"
);
Show( rc, type );
rc = 0
type = "green"

Even though the match failed, the immediate assignment was made.
Pat Len(int)
Description

Constructs a quoted pattern that matches n characters.
Returns

A quoted pattern.
Argument

int An integer that specifies the number of characters.
Pat Look Ahead(pattern, Boolean)
Description

A zero-width pattern match after the current position.
Arguments

pattern The quoted pattern.
Boolean 0 (the default) indicates a match. 1 indicates a negative match or non-match.
Pat Look Behind(pattern, Boolean)
Description

A zero-width quoted pattern match before the current position.

51

Character Pattern Functions

Arguments

pattern The quoted pattern.
Boolean 0 (the default) indicates a match. 1 indicates a negative match or non-match.
Pat Match(source text, pattern, <replacement string>, <"NULL">, <"ANCHOR">,
<"MATCHCASE">, <"FULLSCAN">)
Description
Pat Match executes the quoted pattern against the source text. The pattern must be
constructed first, either inline or by assigning it to a JSL variable elsewhere.
Returns

1 if the pattern is found, 0 otherwise.
Required Arguments

source text A quoted string or quoted string variable that contains the text to be
searched.
pattern A quoted pattern or pattern variable that contains the text to be searched for.
Optional Arguments

replacement string A quoted string that defines text to replace the pattern in the
source text.
"NULL" A placeholder for the third argument if ANCHOR, MATCHCASE, or FULLSCAN
are necessary and there is no replacement text.
"ANCHOR" Starts the pattern match at the beginning of the quoted string. The following
match fails because the pattern, “cream”, is not found at the beginning of the string:
Pat Match( "coffee with cream and sugar", "cream", NULL, ANCHOR );

"MATCHCASE" Optional command to consider capitalization in the match. By default, Pat
Match() is case insensitive.
"FULLSCAN" Optional command to force Pat Match to try all alternatives, which uses
more memory as the match expands. By default, Pat Match() does not use FULLSCAN,

and makes some assumptions that allow the recursion to stop and the match to
succeed.
Pat Not Any(string)
Description

Constructs a pattern that matches a single character that is not in the argument.
Returns

A quoted pattern.
Argument
string A quoted string.

JSL Functions, Operators, and Messages
Character Pattern Functions

Pat Pos(int)
Description

Constructs patterns that match the quoted null string if the current position is int from
the left end of the string, and fail otherwise.
Returns

A quoted pattern.
Argument

int An integer that specifies the position in a quoted string.
Pat R Pos(int)
Description

Constructs patterns that match the quoted null string if the current position is int from
the right end of the string, and fails otherwise.
Returns

A quoted pattern.
Argument

int An integer that specifies the position in a quoted string.
Pat R Tab(int)
Description

Constructs a quoted pattern that matches up to position n from the end of the quoted
string. It can match 0 or more characters. It fails if it would have to move backward or
beyond the end of the string.
Returns

A quoted pattern.
Argument

int An integer that specifies a position in a quoted string.
Pat Regex(string)
Description

Constructs a quoted pattern that matches the regular expression in the quoted string
argument.
Returns

A quoted pattern.
Argument

string A quoted string.

53

Character Pattern Functions

Pat Rem()
Description

Constructs a quoted pattern that matches the remainder of the quoted string. It is
equivalent to Pat R Tab(0).
Returns

A quoted pattern.
Argument

none
Pat Repeat(pattern, minimum, maximum, <"GREEDY"|"RELUCTANT">)
Description

Matches the quoted pattern between minimum and maximum times.
Returns

A quoted pattern.
Required Arguments

pattern A pattern to match against.
minimum An integer that must be smaller than maximum.
maximum An integer that must be greater than minimum.
Optional Argument
"GREEDY"|"RELUCTANT" If GREEDY is specified, it tries the maximum first and works back
to the minimum. If RELUCTANT is specified, it tries the minimum first and works up to

the maximum.
Notes

– Pat Arbno(p) is the same as Pat Repeat(p, 0, infinity, RELUCTANT)
– Pat Repeat(p) is the same as Pat Repeat(p, 1, infinity, GREEDY)
– Pat Repeat(p, n) is the same as Pat Repeat(p, n, infinity, GREEDY)
– Pat Repeat(p, n, m) is the same as Pat Repeat(p, n, m, GREEDY)
Pat Span(string)
Description

Constructs a pattern that matches one or more (not zero) occurrences of characters in its
argument. It is greedy; it always matches the longest possible quoted string. It fails rather
than matching zero characters.
Returns

A quoted pattern.

JSL Functions, Operators, and Messages
Character Pattern Functions

55

Argument

string A quoted string.
Pat String(string)
Description

Constructs a pattern that matches its quoted string argument.
Returns

A quoted pattern.
Argument

string A quoted string.
Pat Succeed()
Description

Constructs a pattern that always succeeds, even when the matcher backs into it. It matches
the quoted null string.
Returns

1 when the match succeeds.
Argument

none
Pat Tab(int)
Description

Constructs a pattern that matches forward to position int in the quoted source string. It
can match 0 or more characters. It fails if it would have to move backward or beyond the
end of the string.
Returns

A pattern.
Argument

int An integer that specifies a position in a quoted string.
Pat Test(expr)
Description

Constructs a pattern that succeeds and matches the quoted null string if expr is not zero
and fails otherwise.
Returns

A quoted pattern.

Character Pattern Functions

Argument

expr An expression.
Notes

Usually the argument is wrapped with expr() because the test needs to be made on the
current value of variables set by Pat Immediate, Pat Conditional, and Pat At. Without
expr, the test is based on values that were known when the pattern was constructed,
which means the test always succeeds or always fails at pattern execution time, which is
probably not what you want.
Example
nCats = 0;
whichCat = 3;
string = "catch a catnapping cat in a catsup factory";
rc = Pat Match(
string,
"cat" + Pat Test(
Expr(
nCats = nCats + 1;
nCats == whichCat;
)
),
"dog"
);
Show( rc, string, nCats );
rc = 1
string = "catch a catnapping dog in a catsup factory"
nCats = 3

Regex Match(source, pattern, <replacement string>|<"MATCHCASE">, <"NULL">)
Description

Executes the pattern match in quoted pattern against the quoted source string.
Returns

A pattern.
Required Arguments

source A quoted string.
pattern A quoted pattern.
Optional Arguments

replacement string The quoted string that specifies the text to replace the source
with.
"MATCHCASE" The search is case insensitive unless you specify MATCHCASE.
"NULL" Indicates that the expression contains MATCHCASE but you don’t want to specify a
replacement.
