# Static Code Analysis Findings & Issue Log

This document records the issues detected in `smart_home.py` using **Bandit**, **Pylint**, and **Flake8**, prioritized by severity (High and Medium severity issues first), along with the rationale and fix approaches applied.

## Identified Issues Table

| Issue | Tool | Severity / Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **B602: Subprocess Shell Injection** | Bandit | High / Vulnerability | 51 | `subprocess.call("bash scenes/" + sceneScript, shell=True)` executes shell commands via string concatenation with `shell=True`. If `sceneScript` contains untrusted input or metacharacters (e.g., `; rm -rf /`), arbitrary commands are executed. | Replaced with `subprocess.run(["bash", os.path.join("scenes", safe_script)], check=False)` using an argument vector with `shell=False`, sanitizing the filename using `os.path.basename()`. |
| **B104: Insecure Network Interface Binding** | Bandit | Medium / Vulnerability | 4 | `HUB_HOST = "0.0.0.0"` binds the server/hub to all available network interfaces on the host system, exposing internal interfaces to external network traffic without access control. | Changed default host to loopback address `"127.0.0.1"` and allowed configurable environment override via `os.getenv("HUB_HOST", "127.0.0.1")`. |
| **W0102: Mutable Default Argument Bug** | Pylint | Medium / Bug | 11 | `def addDevice(..., settings={})` uses a mutable dictionary literal as default parameter. Python evaluates default arguments once at definition time, so all device instances added without custom settings shared and mutated the identical dictionary in memory (causing the Thermostat temperature to leak into Ceiling Light settings). | Changed default argument to `settings=None` and initialized a new dictionary instance inside the function body (`settings = {} if settings is None else settings.copy()`). |
| **B105: Hardcoded Credential / Secret** | Bandit | Low / Vulnerability | 7 | `HUB_PASSWORD = "smarthome-demo"` hardcodes sensitive authentication credentials in plaintext within source code, risking credential exposure in version control systems. | Loaded password dynamically from environment variables using `os.getenv("HUB_PASSWORD", "")`. |
| **W1514: Unspecified File Encoding** | Pylint | Low / Portability | 41 | `open(fileName, "w")` opens a file without specifying an explicit text encoding, making text file serialization platform-dependent (e.g., UTF-8 on Linux vs. Windows-1252 on Windows). | Added explicit encoding parameter `with open(file_name, "w", encoding="utf-8") as file_handle:`. |
| **R1710: Inconsistent Return Statements** | Pylint | Low / Code Smell | 16–20 | `toggleDevice` explicitly returned a boolean (`devices[deviceName]["on"]`) when the device was found, but implicitly returned `None` when the device was not found, leading to type inconsistency across callers. | Ensured an explicit boolean `return False` is returned when a device is not found. |
| **E203: Whitespace Before Colon** | Flake8 | Style / PEP 8 | 6 | `POWER_USAGE = {"light" : 10, ...}` contains invalid whitespace before the colon separator, violating PEP 8 dictionary syntax conventions. | Removed extraneous space before colon: `{"light": 10, ...}`. |
| **E302: Expected Blank Lines** | Flake8 | Style / PEP 8 | 40 | Only one blank line preceded the top-level function definition `def saveState`, violating PEP 8 requirement of two blank lines surrounding top-level definitions. | Added a second blank line between top-level function definitions. |
| **E261: Inline Comment Spacing** | Flake8 | Style / PEP 8 | 66 | Inline comment `# for app setup` had only one space separating it from the preceding code statement instead of the mandatory minimum of two spaces. | Added two spaces before inline comment: `print(...)  # for app setup`. |
| **E501: Line Length Exceeded** | Flake8 | Style / PEP 8 | 68 | Line length exceeded 79 characters (80 > 79) in `print("Devices on:", [name for name, info in devices.items() if info["on"]])`. | Split statement into variable assignment across multiple lines adhering to 79-character boundary. |
| **C0103, C0114, C0116: Naming & Docstrings** | Pylint | Convention / Quality | 1–72 | Functions and parameters used camelCase naming (`addDevice`, `deviceName`) instead of PEP 8 `snake_case`, and the module and functions lacked descriptive docstrings, reducing code score to 4.80/10. | Refactored all functions and parameters to `snake_case` with complete docstrings, maintaining backward-compatible aliases for legacy callers. Pylint score achieved: **10.00/10**. |

## Verification Summary

- **Bandit**: 0 High, 0 Medium, 0 Low issues remaining (`Test results: No issues identified`).
- **Flake8**: Clean execution with 0 style, formatting, or syntax warnings.
- **Pylint**: Final code rated at a perfect **10.00/10** (up from 4.80/10).
- **Runtime Execution**: Successfully runs `smart_home.py` and confirms that the mutable dictionary bug is resolved (`Light settings: {}` remains clean).
