# JSL References — Index

Per-section markdown extracted from the JMP 19 JSL Syntax Reference and Scripting Guide. These are greppable, cheap to load, and replace the original PDFs as the primary lookup path.

## Quick lookup

- **Looking up a function name?** → grep `references/function-index.md` first.
- **Looking up a message (e.g., `<< Get Items`)?** → see `references/syntax/messages-*.md`.
- **How does X work conceptually (scoping, namespaces, display boxes)?** → see `references/guide/<topic>.md`.
- **Want runnable examples?** → online Scripting Index at `https://jsl.jmp.com/`, or the offline mirror under `references/scripting-index/` if it has been built.

---

## Syntax Reference — Function categories

- [Assignment Functions](syntax/assignment-functions.md) — pp.29-31
- [Character Functions](syntax/character-functions.md) — pp.32-46
- [Character Pattern Functions](syntax/character-pattern-functions.md) — pp.47-56
- [Comment Functions](syntax/comment-functions.md) — pp.57-57
- [Comparison Functions](syntax/comparison-functions.md) — pp.58-62
- [Conditional and Logical Functions](syntax/conditional-and-logical-functions.md) — pp.63-74
- [Constant Functions](syntax/constant-functions.md) — pp.75-75
- [Date and Time Functions](syntax/date-and-time-functions.md) — pp.76-84
- [Discrete Probability Functions](syntax/discrete-probability-functions.md) — pp.85-90
- [Display Functions](syntax/display-functions.md) — pp.91-125
- [Expression Functions](syntax/expression-functions.md) — pp.126-127
- [File Functions](syntax/file-functions.md) — pp.128-149
- [Financial Functions](syntax/financial-functions.md) — pp.150-154
- [Graphics Functions](syntax/graphics-functions.md) — pp.155-173
- [HTTP Functions](syntax/http-functions.md) — pp.174-174
- [List Functions](syntax/list-functions.md) — pp.175-181
- [MATLAB Integration Functions](syntax/matlab-integration-functions.md) — pp.182-188
- [Matrix Functions](syntax/matrix-functions.md) — pp.189-215
- [Numeric Functions](syntax/numeric-functions.md) — pp.216-218
- [Optimization Functions](syntax/optimization-functions.md) — pp.219-222
- [Probability Functions](syntax/probability-functions.md) — pp.223-253
- [Programming Functions](syntax/programming-functions.md) — pp.254-271
- [Python Integration Functions](syntax/python-integration-functions.md) — pp.272-277
- [R Integration Functions](syntax/r-integration-functions.md) — pp.278-282
- [JMPEX R Functions](syntax/jmpex-r-functions.md) — pp.283-286
- [Random Functions](syntax/random-functions.md) — pp.287-298
- [Row Functions](syntax/row-functions.md) — pp.299-304
- [Row State Functions](syntax/row-state-functions.md) — pp.305-308
- [SQL Functions](syntax/sql-functions.md) — pp.309-310
- [Statistical Functions](syntax/statistical-functions.md) — pp.311-326
- [Transcendental Functions](syntax/transcendental-functions.md) — pp.327-333
- [Trigonometric Functions](syntax/trigonometric-functions.md) — pp.334-336
- [Utility Functions](syntax/utility-functions.md) — pp.337-375

## Syntax Reference — Object / display-box messages

- [Alpha Shape Messages](syntax/messages-alpha-shape-messages.md) — pp.376-376
- [Associative Array Messages](syntax/messages-associative-array-messages.md) — pp.376-376
- [Class Messages](syntax/messages-class-messages.md) — pp.377-378
- [Data Connector Messages](syntax/messages-data-connector-messages.md) — pp.379-380
- [Data Table Messages](syntax/messages-data-table-messages.md) — pp.381-421
- [Data Feed Messages](syntax/messages-data-feed-messages.md) — pp.422-424
- [Display Box Messages](syntax/messages-display-box-messages.md) — pp.425-464
- [Dynamic Link Library (DLL) Messages](syntax/messages-dynamic-link-library-dll-messages.md) — pp.465-466
- [Image Messages](syntax/messages-image-messages.md) — pp.467-469
- [Interactive HTML Messages](syntax/messages-interactive-html-messages.md) — pp.470-471
- [JMP Application Messages](syntax/messages-jmp-application-messages.md) — pp.472-474
- [MATLAB Messages](syntax/messages-matlab-messages.md) — pp.475-477
- [Namespace Messages](syntax/messages-namespace-messages.md) — pp.478-479
- [Data Historian Import Messages](syntax/messages-data-historian-import-messages.md) — pp.480-484
- [Python Integration Messages](syntax/messages-python-integration-messages.md) — pp.485-489
- [R Integration Messages](syntax/messages-r-integration-messages.md) — pp.490-492
- [Schedule Messages](syntax/messages-schedule-messages.md) — pp.493-493
- [Sockets Messages](syntax/messages-sockets-messages.md) — pp.494-496
- [SQL Messages](syntax/messages-sql-messages.md) — pp.497-500
- [Messages for Other Objects](syntax/messages-messages-for-other-objects.md) — pp.501-504

## Scripting Guide — Conceptual chapters

- [Introduction to Writing JSL Scripts](guide/introduction.md) — pp.39-50
- [Get Started](guide/get-started.md) — pp.51-60
- [Scripting Tools](guide/scripting-tools.md) — pp.61-98
- [JSL Building Blocks](guide/building-blocks.md) — pp.99-144
- [Types of Data](guide/types-of-data.md) — pp.145-192
- [Data Structures](guide/data-structures.md) — pp.193-254
- [Programming Methods](guide/programming-methods.md) — pp.255-324
- [Data Tables](guide/data-tables.md) — pp.325-474
- [Scripting Platforms](guide/scripting-platforms.md) — pp.475-520
- [Display Trees](guide/display-trees.md) — pp.521-634
- [Scripting Graphs](guide/scripting-graphs.md) — pp.635-724
- [Three-Dimensional Scenes](guide/scenes-3d.md) — pp.725-768
- [Extending JMP](guide/extending-jmp.md) — pp.769-832
- [Python](guide/python.md) — pp.833-854
- [Creating Projects](guide/creating-projects.md) — pp.855-866
- [Creating Applications](guide/creating-applications.md) — pp.867-916
- [Common Tasks](guide/common-tasks.md) — pp.917-930
- [Compatibility Notes](guide/compatibility-notes.md) — pp.931-932
- [Efficient Scripts](guide/efficient-scripts.md) — pp.933-938
- [References](guide/references.md) — pp.939-940
- [Scripting Guide Glossary](guide/glossary.md) — pp.941-945

## Function index

- [function-index.md](function-index.md) — flat list of all JSL functions, alphabetical by category

---

Generated from `jsl-syntax-reference.pdf` and `scripting-guide.pdf` via `scripts/fetch_docs.sh` + `scripts/build_references.py`. The source PDFs are not kept in this skill — they are downloaded, extracted, and deleted by `fetch_docs.sh`. To re-extract, just rerun `fetch_docs.sh`.
