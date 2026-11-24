# Lab 7: Fuzzing for Input Validation Bugs

## 🎯 Objectives
- Apply property-based testing and fuzz testing using the **Hypothesis** framework.
- Generate semi-randomized, boundary-breaking input distributions to expose subtle bugs and edge-case exceptions.
- Patch uncovered bugs in highway_toll.py and verify fix convergence.

## 🧪 Running Fuzz Tests
`ash
pytest test_highway_toll.py
`

## 📁 Deliverables
- highway_toll.py: Robust, fuzz-tested highway toll implementation.
- 	est_highway_toll.py: Hypothesis property-based fuzz test suite.
- Lab7_Fuzz_Testing_Report_PES1UG24AM036.pdf: Formal fuzz testing report detailing discovered defects, falsifying examples, and bug resolutions.
- uzz_report_before.txt & uzz_report_after.txt: Hypothesis execution output before and after fixes.
- screenshots/: Terminal execution logs and falsifying hypothesis examples.
