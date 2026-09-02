# Mini CCAR Stress Test

Independent reconstruction of the Federal Reserve's supervisory stress test
(DFAST) for M&T Bank Corporation, built entirely from publicly available data.

The project projects a nine-quarter CET1 capital path under the Federal
Reserve's severely adverse scenario and decomposes the difference against the
Fed's published results.

**Status:** In progress. See Roadmap below.

## Scope

This is an independent challenger estimate. It does not reproduce the Federal
Reserve's supervisory models, which are not public. The objective is to arrive
at a defensible projection through a transparent alternative approach, and then
to explain where and why it diverges from the disclosed results.

Out of scope: global market shock, largest counterparty default, and trading
book losses. M&T is not subject to these components, which is part of why it
was selected.

## Why M&T Bank

- The 2026 severely adverse scenario is centered on commercial real estate.
  M&T carries meaningful CRE concentration, so the scenario's dominant shock
  maps directly onto the bank's dominant exposure.
- Not subject to the global market shock. Trading positions are not publicly
  disclosed, so banks with large trading books cannot be replicated from
  outside. M&T can.
- Category IV, so it participates in even-numbered years. This provides two
  benchmark vintages (2024 and 2026) and allows out-of-sample validation.
- No major acquisition in recent years, so the quarterly time series used for
  calibration is continuous.

## Method

1. **Data assembly.** Federal Reserve severely adverse scenario variables,
   M&T's FR Y-9C filings, and the Fed's published DFAST results.
2. **Portfolio segmentation.** Loan balances split into segments with distinct
   loss behavior.
3. **Loss projection.** Segment-level charge-off rates estimated on historical
   data and driven by scenario paths.
4. **PPNR projection.** Net interest income and non-interest income and expense.
5. **Capital path.** Nine-quarter CET1 walk and minimum ratio.
6. **Benchmarking.** Comparison against Fed disclosure, with the gap decomposed
   into loss, PPNR, and RWA contributions.

## Results

To be added.

## Validation

Model documentation follows the structure set out in SR 11-7. See `docs/`.

| Document | Contents |
|---|---|
| `docs/model_documentation.md` | Conceptual soundness, model design, estimation |
| `docs/assumptions_log.md` | Assumptions and their basis |
| `docs/limitations.md` | Known limitations and conditions for use |
| `docs/data_sources.md` | Source, vintage, and retrieval steps for each input |

## Repository structure

```
data/          Raw downloads, intermediate files, model-ready inputs
notebooks/     Analysis, in execution order
src/           Reusable functions called by the notebooks
docs/          Model documentation and validation write-up
outputs/       Figures and tables
tests/         Checks on the capital accounting identity
```

## Data

All inputs are public. Raw data is not committed to this repository. Each
subdirectory under `data/` contains a README with the source and retrieval
instructions.

## Roadmap

- [ ] Data assembly
- [ ] Portfolio segmentation
- [ ] Loss models
- [ ] PPNR model
- [ ] Capital path
- [ ] Benchmark decomposition
- [ ] Validation documentation

## License

MIT