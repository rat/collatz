# E-118: large-deviation barrier at the WCC cost

The script computes the exact negative-binomial probability

`P(A_1+...+A_ell <= floor(s*ell))`,

where `P(A_i=m)=2^-m` and `s=1+log_4(3)` is the cost slope supplied by
the critical Weak Covering Conjecture. It compares the finite rate with

`I(s)=s log(2)+(s-1)log(s-1)-s log(s)`.

Run:

```sh
python3 large_deviation_barrier.py
```

The limiting rate is `0.012039386618`. Even if the entire truncated
mass were uniform on the unit residues, its average per residue would
have exponent

`1+I(s)/log(3)=1.010958721964`,

strictly above the exponent `1` required by Tao's beta conjecture.
The computation illustrates the closed-form proof in H-148; it is not
used as a proof.

Before the scan, the implementation checks the independently enumerable
base case `P(A_1+A_2<=3)=1/2`.
