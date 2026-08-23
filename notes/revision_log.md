# Revision Log

Re-solves logged by date. Status reflects the *revision* attempt, not the
original solve. Legend: 🟢 solved cleanly · 🟡 correct but needed a correction · 🔴 needed the full solution.

| Date | Problem | Status | Notes |
| ---- | ------- | ------ | ----- |
| Aug 23 | Two Sum | 🟡 Yellow | Algorithm was right; only C++ syntax and the lookup condition needed correction (wrote `.count()` / `map[k]=v` Python-style). See `cpp_vs_python_cheatsheet.md`. |

## Takeaways so far

- Recurring gap = **C++ STL syntax recall**, not algorithm design. Drill the
  hashing syntax (`.count()`, `.insert()`, `.push_back()`, `.size()`), not the
  logic. Cheatsheet: `cpp_vs_python_cheatsheet.md`.
