# Lab 5: Static Code Analysis

## 🎯 Objectives
- Analyze source code for stylistic, structural, and security flaws without execution.
- Utilize industry-standard linters and security scanners: **Pylint**, **Flake8**, and **Bandit**.
- Perform iterative refactoring on smart_home.py and document code quality improvements.

## 📊 Summary of Tools Used
- lake8: PEP 8 compliance, unused imports, line length enforcement.
- pylint: Code smells, conventions, docstring checks, complexity scores.
- andit: AST-based security vulnerability analysis (e.g. hardcoded credentials, insecure primitives).

## 📁 Deliverables
- smart_home.py: Refactored and cleaned Python source code.
- pylint_report_before.txt & pylint_report_after.txt: Pylint metrics before and after refactoring.
- lake8_report_before.txt & lake8_report_after.txt: Flake8 violation logs.
- andit_report_before.txt & andit_report_after.txt: Security scan results.
- issues.md: Detailed breakdown of detected issues and remediations.
- 
eflection.md: Reflection report on static analysis insights.
