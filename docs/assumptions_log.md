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

---

## A-004. Estimation Sample Period

**Assumption.** Loss and revenue models are estimated on quarterly data from
2005 Q1 through 2025 Q4, giving 84 observations.

**Basis.** The sample must contain a severe downturn for the estimated
relationship between macroeconomic conditions and credit losses to hold at the
severity of the supervisory scenario. The 2026 severely adverse scenario has
unemployment peaking at 10 percent. The 2007-09 recession is the only period in
recent history reaching a comparable level, so it must be included. The sample
also includes a pre-crisis expansion, which anchors the baseline level of loss
rates.

**Effect.** Determines the FR Y-9C filings retrieved and the estimation window
in the loss and PPNR models.

**Known issues within the sample.** Three structural features are recorded here
and addressed individually.

| Period | Issue | Treatment |
|---|---|---|
| 2020 Q1 onward | CECL adoption changed provisioning | Charge-off rates are used rather than provisions, as charge-off definitions were not materially affected |
| 2020 Q2 to 2021 Q4 | Fiscal support suppressed credit losses despite elevated unemployment | Indicator variable, see A-005 |
| 2022 Q2 | People's United acquisition | Ratios rather than balances are modeled, see A-006 |

---

## A-005. Treatment of the Pandemic Period

**Assumption.** An indicator variable equal to one over 2020 Q2 through 2021 Q4
is included in the loss models.

**Basis.** Unemployment rose sharply in 2020 while credit losses remained
subdued, reflecting direct fiscal transfers, payment forbearance, and other
support measures rather than the usual relationship between labor market
conditions and borrower default. Estimating without controlling for this period
would attenuate the sensitivity of loss rates to unemployment and understate
projected losses under the scenario.

**Alternative considered.** Excluding the period outright. This discards seven
observations and produces a similar result. Both specifications are estimated,
and the comparison is reported as a sensitivity test.

**Effect.** Loss model specification.

---

## A-006. Treatment of the People's United acquisition

**Assumption.** Loss models are specified in terms of rates rather than dollar
balances.

**Basis.** M&T completed its acquisition of People's United Financial in 2022,
producing a discontinuity in balance sheet levels. Loss rates scale both
numerator and denominator and are therefore substantially less affected by the
change in institution size.

**Residual risk.** The acquisition may have altered portfolio composition and
therefore the underlying loss sensitivity of the combined book. This is not
addressed by the ratio specification. Portfolio composition before and after
the acquisition is examined in the segmentation stage, and any material shift
is recorded as a limitation.

**Effect.** Loss model specification and the scope of the limitations write-up.