# QA automation test project

Test automation QA project, at the end of the Stepik QA Selenium stepik course 

### Сommand for review test examples:
pytest -v --tb=line --language=en -m "need_review" test_product_page.py

### P.S.
in tests, I decided don't remove the solve_quiz_and_get_code method,
because some tests with promo offers need this.
To avoid exception I used "try exception" construction.
Maybe later I will find a better solution.