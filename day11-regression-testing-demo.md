# Day 11 - Regression Testing Demo

## What I did
1. Ran full test suite as baseline - 25/25 passed
2. Introduced intentional bug in multiply() function (added +1)
3. Re-ran full suite - regression caught immediately:
   test_multiply, test_multiply_by_zero, test_multiply_negative
   all failed, pinpointing exact expected vs actual values
4. Fixed the bug, reverted multiply() to correct implementation
5. Re-ran suite - 25/25 passed again, confirming fix

## Why this matters
This demonstrates regression testing in practice: a small code
change in one function broke existing, previously passing tests.
Without a test suite, this bug could easily reach production
undetected. Ties directly to defect life cycle concepts:
New -> Fixed -> Retest -> Verified.
