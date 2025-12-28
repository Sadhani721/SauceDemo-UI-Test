 🛒 SauceDemo UI Automation Framework

A robust, scalable, and production-ready Test Automation Framework built using **Python**, **Selenium WebDriver**, and **Pytest**. This project automates the [SauceDemo](https://www.saucedemo.com/) e-commerce website to demonstrate modern testing practices.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15.2-green)
![Pytest](https://img.shields.io/badge/Pytest-7.4.3-yellow)

---

 🚀 Key Features

- **Page Object Model (POM)**: Clearly separates test logic from UI elements (Locators) for better maintenance and scalability.
- **Data-Driven Testing**: Capable of running tests against multiple datasets and user scenarios.
- **Robust Utility Functions**: Custom wrapper methods in `pages/` for handling clicks, explicit waits, and dynamic elements.
- **Smart Configuration**: Centralized test setup using pytest fixtures with headless browser support.
- **Automatic Screenshots**: Captures screenshots automatically upon test failure for easy debugging.
- **Rich Reporting**: Generates HTML reports via `pytest-html` for detailed test execution analysis.
- **Headless Execution**: Supports headless browser mode for CI/CD pipeline integration.

---

## 🛠️ Tech Stack

| Component | Technology |

| Language| Python 3.11+ |
| Automation Tool - Selenium WebDriver |
| Testing Framework | Pytest |
| Reporting - Pytest-HTML |
| Design Pattern -  Page Object Model (POM) |
| Browser Management - WebDriver Manager |

---

 📂 Project Structure

```
PythonProject1/
│
├── pages/                  # Page Object Classes (Locators & Actions)
│   ├── __init__.py
│   ├── base_page.py        # Base class with reusable methods
│   ├── login_page.py       # Login page actions and locators
│   ├── products_page.py    # Products page actions
│   ├── cart_page.py        # Shopping cart page actions
│   └── checkout_page.py    # Checkout flow actions
│
├── tests/                  # Test Scripts
│   ├── __init__.py
│   ├── conftest.py         # Pytest fixtures (Setup/Teardown)
│   ├── test_login.py       # Login functionality tests
│   ├── test_invalid_login.py
│   ├── test_cart_page.py   # Shopping cart tests
│   ├── test_checkout_page.py
│   └── test_positive_purchase.py  # End-to-end purchase flow
│
├── screenshots/            # Failure screenshots (auto-generated)
├── reports/                # Test execution reports (HTML)
│   └── report.html
│
├── pytest.ini              # Pytest configuration
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

 ⚙️ How to Install & Run

1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/PythonProject1.git
cd PythonProject1
```

 2. Set up Virtual Environment (Optional but Recommended)

```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows:
.venv\Scripts\activate

# Activate on Mac/Linux:
source .venv/bin/activate
```

3. Install Dependencies

```bash
pip install -r requirements.txt
```

4. Run the Tests

To run all test cases:
```bash
pytest
```

To run a specific test file:
```bash
pytest tests/test_login.py
```

To run a specific test case:
```bash
pytest tests/test_login.py::test_login_valid_credentials
```

To run with HTML report generation:
```bash
pytest --html=reports/report.html --self-contained-html
```

To run with verbose output:
```bash
pytest -v
```

To run tests in parallel (requires pytest-xdist):
```bash
pip install pytest-xdist
pytest -n auto
```

---
 📊 Reports & Logs

 HTML Report
After test execution, open `reports/report.html` in any browser to see a graphical summary of:
- ✅ Passed tests
- ❌ Failed tests  
- ⏭️ Skipped tests
- ⏱️ Execution time
- 📸 Detailed test results

Screenshots
- Automatically captured on test failure
- Stored in `screenshots/` directory
- Named after the failing test case for easy identification

---

🧪 Test Coverage

The framework includes comprehensive test scenarios:


| `test_login.py` | Valid/invalid login combinations, empty credentials |
| `test_invalid_login.py` | Negative login scenarios |
| `test_cart_page.py` | Add to cart, remove from cart functionality |
| `test_checkout_page.py` | Checkout form validation and submission |
| `test_positive_purchase.py` | Complete end-to-end purchase workflow |

---

## 🔧 Configuration

### Browser Settings (conftest.py)
The framework uses Chrome browser in headless mode by default:
- Window size: 1920x1080
- Headless mode enabled
- Implicit wait: 2 seconds
- Auto-screenshot on failure

Pytest Configuration (pytest.ini)
```ini
[pytest]
pythonpath = .
```

---

 🎯 Best Practices Implemented

✅ **Page Object Model**: Separation of test logic and page elements  
✅ **DRY Principle**: Reusable methods in BasePage class  
✅ **Explicit Waits**: WebDriverWait for dynamic elements  
✅ **Fixture Management**: Centralized driver setup/teardown  
✅ **Screenshot on Failure**: Automatic debugging support  
✅ **Clear Test Structure**: Organized and maintainable test cases  
✅ **Version Control**: Git-friendly structure with .gitignore  

---

 📦 Dependencies

```txt
selenium==4.15.2        # Browser automation
pytest==7.4.3           # Testing framework
pytest-html==4.1.1      # HTML report generation
webdriver-manager==4.0.1  # Automatic driver management
```

---


## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.



---

 Acknowledgments

- [SauceDemo](https://www.saucedemo.com/) - Test application
- [Selenium](https://www.selenium.dev/) - Browser automation
- [Pytest](https://pytest.org/) - Testing framework

---

Happy Testing! 🧪🚀
