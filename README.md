# 📱 iRechargeBD Automation Testing Framework

A Selenium-based Test Automation Framework for [iRechargeBD](https://www.irechargebd.com/) built using **Python**, **Pytest** & the **Page Object Model (POM)** design pattern.

---

## 🚀 Technologies Used

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- HTML Reports (pytest-html)
- Logging
- ChromeDriver (via webdriver-manager)

---

## 📂 Project Structure

```
iRechargeBD_Automation/
│
├── config/
│   └── config.ini
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── signup_page.py
│   ├── login_page.py
│   └── operators_page.py
│
├── screenshots/
│
├── testcases/
│   ├── test_homepage.py
│   ├── test_navigation.py
│   ├── test_signup.py
│   ├── test_login.py
│   ├── test_operators.py
│   └── test_config_setup.py
│
├── test_data/
│   └── users.csv
│
├── utilities/
│   ├── logger.py
│   ├── read_properties.py
│   └── excel_utils.py
│
├── conftest.py
├── requirements.txt
└── README.md
```

---

# ✅ Automated Test Scenarios

### 🔹 Homepage / Smoke Test
- Open iRechargeBD
- Verify page title & hero heading
- Verify operator logos are displayed (Grameenphone, Robi, Banglalink, Airtel, Teletalk)
- Capture Screenshot

### 🔹 Navigation Test
- Verify top navigation links (Services, Operators, Developers, API Package Plans, About Us, Contact)
- Click each link and verify destination URL / page load

### 🔹 Sign Up Test
- Open Sign Up page
- Fill registration form with test data
- Submit and verify confirmation / validation message
- Capture Screenshot

### 🔹 Login Test
- Open Login page
- Enter email & password
- Click Login button
- Verify login result (success dashboard or expected error for invalid creds)
- Capture Screenshot

### 🔹 Operators Section Test
- Verify all listed operators (Grameenphone, Robi, Banglalink, Airtel, Teletalk)
- Verify operator descriptions render correctly

### 🔹 Config Setup Test
- Verify config.ini loads correctly
- Verify base URL and timeouts are read properly

---

# 📸 Screenshots

Screenshots are automatically saved inside:

```
screenshots/
```

Example:
```
homepage_result.png
signup_result.png
login_result.png
operators_result.png
```

---

# 📊 HTML Report

Generate Report:
```
pytest --html=reports/report.html
```

Open:
```
reports/report.html
```

---

# ▶️ Run Tests

Run all tests:
```
python -m pytest -v
```

Run the homepage smoke test:
```
python -m pytest testcases/test_homepage.py -v
```

Run the navigation test:
```
python -m pytest testcases/test_navigation.py -v
```

Run the signup test:
```
python -m pytest testcases/test_signup.py -v
```

Run the login test:
```
python -m pytest testcases/test_login.py -v
```

Run the operators test:
```
python -m pytest testcases/test_operators.py -v
```

Run headless (CI-friendly):
```
HEADLESS=1 python -m pytest -v
```

Run tests quietly:
```
python -m pytest -q
```

---

# 📋 Current Features

- ✅ Page Object Model (POM)
- ✅ Selenium WebDriver
- ✅ Pytest Framework
- ✅ Headless execution support
- ✅ HTML Report
- ✅ Logging
- ✅ Screenshot Capture
- ✅ Homepage / Smoke Verification
- ✅ Navigation Link Verification
- ✅ Signup Automation
- ✅ Login Automation
- ✅ Operators Section Verification

---

# 🔮 Future Improvements

- Data Driven Testing (CSV/Excel)
- Cross Browser Testing (Firefox, Edge)
- GitHub Actions CI/CD
- Docker Support
- Allure Report
- API-level testing for the Recharge API endpoints (separate from UI)

---

# ⚠️ Notes

- This project targets a **live third-party production site**. Tests are read-only / UI-verification focused (no real recharge transactions are submitted, no real signup data is persisted).
- Do **not** hardcode real account credentials in `config/config.ini` — use environment variables or a local, git-ignored `config.local.ini` for anything sensitive.
- Selector values in the page objects are best-effort based on the current site DOM and may need adjustment if the site's markup changes.

---

⭐ If you found this project useful, don't forget to Star this repository.
