---
name: jmp-jsl
description: Write, debug, refactor, and review JMP Scripting Language (JSL) code for SAS JMP 19. Use this skill whenever the user mentions JSL, JMP scripts, .jsl files, JMP add-ins, Workflow Builder output, JMP data tables, JMP display boxes, JMP platforms (Fit Model, Distribution, Graph Builder, etc.), JMP namespaces, or any analysis automation in JMP — even when they don't explicitly ask for "a JSL skill". Also trigger when reviewing or editing files with .jsl extension, when the user pastes code containing JSL idioms (`<<` message-send, `Expr()`, `Names Default To Here`, `Data Table()`, `New Window()`, `Eval(Substitute(...))`), or when the user is working on anything in the SAS JMP statistical software ecosystem. Do NOT confuse JSL with JavaScript, SAS Base, or Java — they are unrelated despite naming.
---

# JSL — JMP Scripting Language (JMP 19)

JSL is the scripting language built into SAS JMP statistical software. It is **not** SAS Base, **not** JavaScript, and **not** related to any other "JSL". It has its own syntax with quirky operators, message-passing semantics, and first-class expressions. LLM training data on JSL is sparse compared to mainstream languages, so the dominant failure mode when writing JSL is **fabrication**: invented function names, JS/Python-style syntax, hallucinated platform options. Your job using this skill is to suppress that failure mode by leaning on the bundled references and the JMP-recommended workflow below.

The user's environment is **JMP 19** running on Windows or Mac (their workflow uses Rocky Linux for the dev host but JMP itself runs on the desktop client). Default to JMP 19 syntax. JMP 18 and 19 are very close; JMP 17 and earlier had a different Help menu structure but the JSL language itself is largely backward-compatible.

## The cardinal rule: don't invent JSL

Before writing any JSL function call you are not 100% certain exists, do one of:

1. **Grep `references/function-index.md`** — flat alphabetical index of every JSL function in the JMP 19 syntax reference (≈1250 entries), each one a one-line pointer to its category file and PDF page. Cheap to load. If a function is not in this index, treat that as a strong red flag against using it.
2. **Read the per-category file** under `references/syntax/` once you know which category the function lives in (e.g. `references/syntax/matrix-functions.md`). Files are scoped per category and are 1-50 KB each — small enough to read directly with `Read`, greppable for the function name to jump to its entry.
3. **For object/display-box messages** (anything used with `<<`), see `references/syntax/messages-*.md` — one file per object family (Data Table, Display Box, Namespace, etc.).
4. **For conceptual questions** (scoping, namespaces, display-box composition, add-in scaffolding), see `references/guide/<topic>.md` — one file per chapter of the JMP 19 Scripting Guide.
5. **For runnable examples**, prefer `references/scripting-index/` if it has been built (offline mirror of `https://jsl.jmp.com/`, organized by display box / function / message). Otherwise consult the live online site.
6. If still unsure, **say so explicitly** rather than guessing. Suggest the user run the same workflow interactively in JMP and copy the JSL from the log or from `Workflow Builder` (see below).

If a function looks plausible but you cannot verify it exists, treat that as a red flag. Common Claude hallucinations in JSL include: `dt.column()` (wrong — use `dt:ColumnName` or `Column(dt, "name")`), `.length` (wrong — use `N Items()` or `N Row()`), `for (...)` (wrong — use `For(i=1, i<=n, i++, ...)`), `print()` (wrong — use `Show()` or `Write()`).

## The JMP-recommended starting workflow

The JMP community is unanimous on this: **don't write JSL from a blank page**. JMP itself generates JSL for you. When the user describes an analysis task, default to this sequence:

1. Ask the user to do the analysis interactively in JMP once.
2. Tell them to use **Workflow Builder** (or the red-triangle `Script` menu in any report) to capture the JSL.
3. Take that captured JSL as the starting point and refactor/parameterize/clean it up.

This is faster, more accurate, and avoids hallucination. Only fall back to writing JSL from scratch when:
- The task is genuinely outside what JMP's UI can record (custom display box layouts, programmatic add-in scaffolding, complex namespace/scope work).
- The user has already captured baseline JSL and wants you to extend it.
- The user explicitly asks you to write from scratch.

## Things JSL does that trip up LLMs

These are the patterns you will get wrong if you write JSL by analogy to other languages. Internalize them:

**Assignment and operators.** `=` is assignment in most contexts but is also equality comparison inside `If()`, `Match()`, etc. — JSL infers from position. `==` also works for equality and is clearer; prefer it. `:=` does **not** mean what it does in Pascal/Go — it's the "alternate assignment" operator and rarely used. Logical operators are `&` and `|` (single chars) or `And()`/`Or()` — **not** `&&` / `||`.

**Message-send: `<<`.** This is JSL's defining idiom. You send messages to objects: `dt << New Column("foo", Numeric, Continuous)`, `obj << Get Items`, `report << Save Picture("path.png", "PNG")`. Messages can be chained on separate lines or comma-separated inside parens. Many platforms accept both `<<` and a function-call form; prefer `<<` for object operations and function-call form for top-level constructors.

**Expressions are first-class.** `Expr()`, `Name Expr()`, `Eval()`, `Eval Expr()`, `Substitute()`, and `Parse()` are core to any non-trivial JSL. To build a script dynamically, the standard pattern is `Eval(Substitute(Expr(...code with @placeholders...), Expr(@col), Column Name))`. This looks alien but is idiomatic — don't try to replace it with string concatenation.

**Scope.** Always start scripts with `Names Default To Here(1);`. Without it, every variable becomes global and you get name collisions across scripts. With it, variables are local to the script's "Here" namespace. For library code use explicit namespaces (`Namespace("myns"):var = ...`).

**Lists, associative arrays, matrices are different things.** `{a, b, c}` is a list. `[1 2 3; 4 5 6]` is a matrix (semicolons separate rows, spaces separate columns — yes, really). `["key" => value, ...]` is an associative array. They are not interchangeable; the wrong one will throw or silently misbehave.

**Column references inside data tables.** Inside a row context (e.g., `For Each Row()` or a formula), `:Height` refers to the current row's value of column `Height`. Outside row context, use `Column(dt, "Height") << Get Values` or `dt:Height` to get the whole column reference.

**Statement terminators.** `;` separates statements but is largely optional at end-of-line. Inside argument lists use `,`. Mixing them up produces confusing errors.

**String quoting.** Use `"double quotes"` for strings. Single quotes are for **names with special characters** — e.g., `:Name("Column With Space")` or the shorthand `:'Column With Space'n`. Don't reach for single quotes as a string delimiter; you'll get a name reference instead of a string.

**Comments.** `// line comment` and `/* block comment */`. JSL also has `//!` for "run on script open" — used in add-ins, not regular scripts.

## When the user shares JSL output that doesn't run

JMP's error messages are often unhelpful (`Name Unresolved`, `Bad Argument`, etc.). Standard debugging moves:

- Ask the user to paste the **enhanced log** output, not just the error string. The enhanced log (JMP 16+) shows the resolved values.
- Suggest sprinkling `Show()` or `Write()` calls to inspect intermediate values.
- For "Name Unresolved", check: is `Names Default To Here(1)` set? Is the variable spelled exactly right (case-sensitive)? Is the table reference still valid (closed tables invalidate `dt`)?
- For display-box scripts that "do nothing", check whether the script returns a display box reference that needs to be wrapped in `New Window("title", ...)` to actually appear.

## Reference files (load on demand, not by default)

These live in this skill's `references/` directory. They were generated from the JMP 19 PDFs by `scripts/fetch_docs.sh` and are the canonical lookup path now — the original PDFs are not bundled because they are not directly grep-able and consume far more context per read than the markdown derivatives.

- **`references/index.md`** — top-level catalog of every category file with PDF page ranges.
- **`references/function-index.md`** — flat alphabetical index of ≈1250 JSL functions. **This is the right first stop** for any function-name lookup — it's small, greppable, and tells you which category file to open next.
- **`references/syntax/<category>.md`** (33 files) — per-category function references extracted from the JMP 19 JSL Syntax Reference: `assignment-functions.md`, `character-functions.md`, `matrix-functions.md`, `display-functions.md`, `programming-functions.md`, etc. Each file contains the full signature and description for every function in that category.
- **`references/syntax/messages-<object>.md`** (20 files) — per-object-family message references for everything used with `<<`: `messages-data-table-messages.md`, `messages-display-box-messages.md`, `messages-namespace-messages.md`, etc.
- **`references/guide/<chapter>.md`** (21 files) — per-chapter conceptual content from the JMP 19 Scripting Guide: `building-blocks.md`, `data-tables.md`, `display-trees.md`, `programming-methods.md`, `extending-jmp.md`, `efficient-scripts.md`, etc. Read these when the user asks "how does X work" rather than "what is the signature of Y".
- **`references/scripting-index/`** *(optional, only if `scripts/fetch_scripting_index.sh` has been run)* — offline mirror of the online JMP Scripting Index at `https://jsl.jmp.com/`, with a runnable example per function/box/message. Best place to find canonical example usage. The `index.md` in that directory is a flat alphabetical list of every entry. If this directory is absent, fall back to the live online site.

**How to use these efficiently:**

1. For a function name → grep `function-index.md`, then open the category file. Don't load the whole syntax tree.
2. For a message → grep `function-index.md` first (some messages are also exposed as functions), otherwise grep across `syntax/messages-*.md`.
3. For "how do I X" questions → start at `index.md` and pick the matching guide chapter.
4. For runnable example code → `scripting-index/` (if mirrored locally) or the live URL.

To (re)build these references from the latest JMP 19 PDFs, run `bash scripts/fetch_docs.sh`. Add `--with-index` to also mirror the online Scripting Index. The script downloads the PDFs into a temp dir, extracts them, generates the per-section markdown, and deletes the PDFs — it leaves only the markdown behind.

## Output style for JSL code

When you write JSL for the user:

- Always include `Names Default To Here(1);` at the top of any non-trivial script.
- Prefer `<<` message form for object operations; it reads more idiomatically.
- Use `Expr()` / `Eval(Substitute(...))` for dynamic code generation, not string concatenation.
- Add `// comments` liberally, especially around any non-obvious JSL idiom — the user (and their colleagues) may revisit the script in 6 months.
- For longer scripts, group related blocks with banner comments and use `Names Default To Here(1)` plus explicit local declarations.
- When unsure between two valid forms, default to whatever the JMP Workflow Builder would generate — that's the JMP-canonical style.

## When NOT to use this skill

- Generic statistics questions not tied to JMP — answer directly without invoking this skill.
- SAS Base / SAS macro language — completely different language, do not conflate.
- Python-in-JMP integration questions — the user's existing Python knowledge plus JMP's `Python` JSL functions cover this; check `jsl-syntax-reference.pdf` for the `Python Submit`, `Python Init`, etc. function family if needed.
- Pure Laravel / PHP / web work — out of scope.
