---
description: Run mutation testing on a file to evaluate test robustness
---

Run a mutation testing session.

## Usage

```
/mutation-test <file> [--test '<command>']
```

## Arguments

Parse $ARGUMENTS to extract:
- **file**: The target file to mutate (required)
- **--test**: The test command to run (default: `make unit-test`)

Raw arguments: $ARGUMENTS

## Instructions

1. Parse the arguments above to extract the file path and test command
2. Read the target file thoroughly
3. Identify mutation opportunities (boundary conditions, boolean inversions, status changes, removed statements, etc.)
4. For each mutation:
   - Make the change
   - Run the provided test command
   - Record outcome (KILLED if tests fail, SURVIVED if tests pass)
   - Revert the change
5. Present a final report with:
   - Total mutations / killed / survived
   - Mutation score percentage
   - Table of all mutations with outcomes
   - Any test coverage gaps identified (surviving mutations)
