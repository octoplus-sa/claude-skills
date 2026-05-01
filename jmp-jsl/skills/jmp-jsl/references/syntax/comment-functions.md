# Comment Functions

Source: JMP 19 JSL Syntax Reference (PDF pages 57-57).

## Index (line numbers in this file)

- `Regex Match()` — L16
---

JSL Functions, Operators, and Messages
Comment Functions

57

Examples
Regex Match(
"person=Fred id=77 friend= favorite=tea", // source
"(\w+)=(\S*) (\w+)=(\S*) (\w+)=(\S*) (\w+)=(\S*)" // pattern
);
{"person=Fred id=77 friend= favorite=tea", "person", "Fred", "id", "77",
"friend", "", "favorite", "tea"}
// case-insensitive, no replacement
Regex Match( "beliEve", "([aeiou])(.*?)(\1)" );
{"eliE", "e", "li", "E"}
// case-sensitive, no replacement
Regex Match( "beliEve", "([aeiou])(.*?)(\1)", NULL, MATCHCASE );
{"eliEve", "e", "liEv", "e"}

Comment Functions
// comment
Description

Comments to end of line.
Notes

Everything after the // is ignored when running the script.
/* comment */
Description

A comment that can appear in the middle of a line of script.
Notes

Anything between the beginning tag /* and the end tag */ is ignored when running the
script. This comment style can be used almost anywhere, even inside lists of arguments. If
you place a comment inside a double-quoted string, the comment is treated merely as part
of the string and not a comment. You cannot place comments in the middle of operators.
Examples
+/*comment*/=
:/*comment*/name

are invalid and produce errors. The first comment interrupts += and the second interrupts
:name.
sums = {(a+b /*comment*/), /*comment*/ (c^2)}

is valid JSL; the comments are both ignored.
