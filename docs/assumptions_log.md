# Assumptions Log

Each entry records an assumption made in constructing this projection, the
basis for it, and where it takes effect. Entries are added as decisions are
made rather than reconstructed at the end.

---

## A-001. Projection Horizon

**Assumption.** The projection horizon is nine quarters, running from 2026 Q1
through 2028 Q1.

**Basis.** The Federal Reserve's supervisory stress test uses a nine-quarter
horizon. The published severely adverse scenario file extends beyond this
window; rows after 2028 Q1 are supplementary and are excluded.

**Effect.** Filter applied when loading the scenario file. Capital paths and
peak-to-trough measures are computed over these nine quarters only.

---

## A-002. Scenario Anchor Point

**Assumption.** Index-level scenario variables are anchored to 2025 Q4 actual
values, not to the first projected quarter.

**Basis.** The Federal Reserve states that the capital ratio at the end of 2025
served as the starting point for the 2026 stress test. The first scenario
quarter, 2026 Q1, already reflects part of the shock.

Verified against the Federal Reserve's stated scenario severity. Measured from
2025 Q4, the house price index declines approximately 30 percent and the
commercial real estate price index approximately 39 percent, matching the
published characterization. Measured from 2026 Q1 instead, the declines are
approximately 25 percent and 36 percent, which does not match.

**Effect.** The historic domestic file and the severely adverse file are
joined so that 2025 Q4 actuals precede the projection window. Percentage
changes for index variables are computed against this anchor.

---

## A-003. Treatment of Scenario Variable Types

**Assumption.** Scenario variables are handled in two classes. Rate variables
are used at their stated values. Level variables are converted to percentage
changes before use.

**Basis.** Variables labeled "(Level)" in the scenario file are index values
with no interpretable scale of their own. These are the equity index, house
price index, and commercial real estate price index.

**Effect.** Applies to model inputs in the loss projection stage.
