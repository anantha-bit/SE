# Lab 6: Code and Branch Coverage Analysis

## 🎯 Objectives
- Measure statement (line) coverage and branch (decision) coverage for the Highway Toll system.
- Identify untested execution paths, edge conditions, and missing test cases.
- Achieve 100% statement and branch coverage via targeted unit test suites.

## 🧪 Running the Tests & Coverage
`ash
coverage run --branch -m unittest BranchCoverageTest_highway_toll.py
coverage report -m
coverage html
`

## 📁 Deliverables
- highway_toll.py: Highway toll calculation and management module.
- CodeCoverageTest_highway_toll.py: Unit test suite targeting statement coverage.
- BranchCoverageTest_highway_toll.py: Unit test suite targeting branch coverage.
- code_coverage_report.txt & ranch_coverage_report.txt: Coverage summary reports.
- screenshots/: Visual proof of terminal coverage runs and HTML coverage reports.
