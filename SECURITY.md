# Security policy

Qalqan-60+ protects people in stressful moments, so security problems matter even in the prototype.

## Reporting a vulnerability

Please **do not** open a public issue. Use GitHub’s private vulnerability reporting
(*Security → Report a vulnerability*) or the private contact in [GOVERNANCE.md](GOVERNANCE.md).
We will answer within 7 days.

Useful reports include: ways to make the prototype send data over the network, ways to read the family code word,
ways for a third party to end or suppress a pause, and texts that a scammer could misuse.

## Scope

- `src/index.html` (prototype), `tools/`, `.github/workflows/`
- the open dataset in `data/` (for example, a phrase that contains personal data)

Never include real victims’ personal data in a report.
