# E-074 — Review of Ballesteros et al., "A Novel Image Encryption Scheme Based on Collatz Conjecture" (2018)

Related hypothesis: [`H-074-ballesteros-image-encryption-review.md`](../../hypotheses/H-074-ballesteros-image-encryption-review.md)

## What was done

We verified the encryption scheme's central construction (item 104):
"Collatz codes" — a variable-length encoding derived from each pixel
value's accelerated orbit — and the claim that the substring "11" never
appears within the body of a code (only as an artificial header),
allowing unique decoding of a concatenated stream.

## Result

Confirmed with no errors: the paper's own example reproduced exactly;
the body never contains "11" in any of the 256 possible values; the
256 complete codes are all distinct; a stream of 1000 concatenated
pixels (48,693 bits) has exactly one valid decomposition (verified via
dynamic programming). See H-074 for the full verdict and two of our own
methodology corrections made before reporting any conclusion.

## Reproduce

```
python3 experiment.py
```
