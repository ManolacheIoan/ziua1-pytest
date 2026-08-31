# QA / Test Automation Practice Project

Proiect personal de invatare, axat pe test automation pentru
industria auto (Python, Selenium, CAN bus) si practici standard
de dezvoltare (Git, CI/CD).

## Continut

### Unit testing (Python + pytest)
- `calculator.py` / `test_calculator.py` — teste unitare de baza,
  fixtures, parametrize

### Web automation (Selenium)
- `pages/login_page.py` — Page Object Model
- `test_login_pom.py` — teste de login folosind POM
- `conftest.py` — fixture pentru driver Selenium cu setup/teardown automat
- `test_checkboxes.py` — additional Selenium tests using find_elements and is_selected

### QA Theory & Practice
- `day11-istqb-notes.md` — ISTQB Foundation core concepts
- `day11-regression-testing-demo.md` — hands-on regression testing demonstration

### CAN bus (comunicare embedded auto)
- `can_basic.py` — simulare mesaj CAN cu python-can
- `test_can.py` — teste send/receive pe bus CAN virtual

### API Testing
- `test_api_basic.py` — GET/POST/PUT/DELETE requests, status codes, error handling
- `test_api_pom.py` — reusable session fixture, parametrized tests, response time and headers validation

### C basics
- `ziua6-c-basics/` — variabile, pointeri, structuri, functii

### CI/CD
- Pipeline Jenkins configurat pentru rulare automata a testelor
  la fiecare push (Checkout -> Install dependencies -> Run tests)

## Tehnologii folosite
Python, pytest, Selenium, python-can, Git, Jenkins, C

## Ce demonstreaza acest proiect
- Scriere si organizare de teste automate (unitare si UI)
- Intelegere a comunicarii embedded specifice industriei auto (CAN bus)
- Flux de lucru Git complet: branch, PR, merge, rezolvare conflicte
- Configurare si debugging CI/CD real (Jenkins)
