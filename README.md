# AI Usage Declaration and Audit

**Group:** Duty Free\
**Members:** Zarr Ni Htut (Raymand), Zay Htet (Zett), Aung Myo Naing
(Jerry), So Pyay Htoo (Yummy), Min Khant Kyaw (Sonic)

------------------------------------------------------------------------

## Part 1 --- AI Usage Declaration (required, unmarked)

Every AI tool any member used anywhere in this project should be
declared. Using AI is allowed. Not declaring it is not.

  ---------------------------------------------------------------------------
  Tool              What we used it for   Where in the      How we checked it
                                          project           before relying on
                                                            it
  ----------------- --------------------- ----------------- -----------------
  ChatGPT           Helped discuss test   Test/debugging    Reviewed
                    ideas, explain pytest discussions and   suggestions
                    failures and          documentation,    manually,
                    tracebacks, review    including         compared them
                    test behaviour,       `FINDINGS.md`,    with application
                    troubleshoot code,    `REPORT.md`, and  behaviour, and
                    and organize the      `AI_USAGE.md`.    checked relevant
                    test-audit                              results by
                    documentation.                          running pytest
                                                            against the
                                                            original and
                                                            fixed versions.

  Gemini            Helped explore test   Test-suite drafts Reviewed
                    ideas, analyse test   and audit         suggestions and
                    behaviour, and        documentation,    checked relevant
                    support test-suite    including         behaviour against
                    and                   `AI_USAGE.md` and the application
                    audit-documentation   related project   and pytest
                    discussions.          files where       results.
                                          Gemini            
                                          suggestions were  
                                          used.             
  ---------------------------------------------------------------------------

If any AI tools were used but are not listed here, add them before
submission.

------------------------------------------------------------------------

## Part 2 --- Audit of the Supplied Test Set

The supplied tests are located in `ai_review/test_ai_generated.py`. The
initial full test run was against the shipped code; the final full test
run was after the group's fixes.

### 2.1 Classification Rules

  -----------------------------------------------------------------------
  Shipped code            Fixed code              Verdict
  ----------------------- ----------------------- -----------------------
  FAIL                    PASS                    Genuine detection

  PASS                    PASS                    Detects nothing

  PASS                    FAIL                    Locks in the bug

  FAIL                    FAIL                    Invented requirement,
                                                  if the expected
                                                  behaviour is not a
                                                  documented requirement
  -----------------------------------------------------------------------

### 2.2 Summary Table

  --------------------------------------------------------------------------------------------------------------------------------
            \# Test                                                What it claims Shipped   Fixed     Verdict          Auditor
                                                                   to catch       code      code                       
  ------------ --------------------------------------------------- -------------- --------- --------- ---------------- -----------
             1 `test_cart_total_sums_items`                        Checks whether FAIL      PASS      Genuine          Zarr Ni
                                                                   the cart total                     detection        Htut
                                                                   includes all                                        (Raymand)
                                                                   item prices.                                        

             2 `test_login_rejects_wrong_password`                 Checks whether PASS      PASS      Detects nothing  Zarr Ni
                                                                   login rejects                                       Htut
                                                                   an incorrect                                        (Raymand)
                                                                   password.                                           

             3 `test_search_finds_exact_title`                     Checks whether PASS      PASS      Detects nothing  Aung Myo
                                                                   exact-title                                         Naing
                                                                   search returns                                      (Jerry)
                                                                   the matching                                        
                                                                   product.                                            

             4 `test_import_returns_count`                         Checks whether FAIL      PASS      Genuine          Aung Myo
                                                                   bulk import                        detection        Naing
                                                                   returns the                                         (Jerry)
                                                                   number of                                           
                                                                   imported                                            
                                                                   products.                                           

             5 `test_checkout_empty_returns_none`                  Checks whether FAIL      PASS      Genuine          Zay Htet
                                                                   empty-cart                         detection        (Zett)
                                                                   checkout                                            
                                                                   returns                                             
                                                                   `None`.                                             

             6 `test_add_to_cart_returns_true_for_known_product`   Checks whether PASS      PASS      Detects nothing  So Pyay
                                                                   adding a known                                      Htoo
                                                                   product                                             (Yummy)
                                                                   returns a                                           
                                                                   successful                                          
                                                                   result.                                             

             7 `test_search_is_limited_to_ten_results`             Claims         FAIL      FAIL      Invented         So Pyay
                                                                   catalogue                          requirement      Htoo
                                                                   search should                      (provisional;    (Yummy)
                                                                   return no more                     verify           
                                                                   than ten                           specification)   
                                                                   results.                                            

             8 `test_register_duplicate_returns_false`             Checks whether PASS      PASS      Detects nothing  Min Khant
                                                                   duplicate                                           Kyaw
                                                                   registration                                        (Sonic)
                                                                   returns                                             
                                                                   `False`.                                            
  --------------------------------------------------------------------------------------------------------------------------------

*Auditor assignments follow the group's audit allocation. Each named
member should ensure that the assigned audit was personally reviewed and
that the attribution is accurate.*

### 2.3 Individual Test Analysis and Evidence

The actual repository test file is `ai_review/test_ai_generated.py`. The
evidence below is transcribed from the group's supplied pytest output.
Each test entry explains its purpose, shows the shipped-code and
fixed-code results, and gives a verdict.

#### Test 1: `test_cart_total_sums_items`

**Audited by:** Zarr Ni Htut (Raymand)

**1. What it claims to catch**

Checks whether a cart containing two products priced at 10 and 20
returns a total of 30. It is intended to catch a cart-total calculation
that omits an item's price.

**2. Evidence --- against shipped code**

``` text
ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED
E       assert 10 == 30
```

**3. Evidence --- against fixed code**

``` text
ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED
```

**4. What that pair proves**

This is **Genuine detection --- FAIL then PASS**. The shipped code
returned 10 instead of 30, while the fixed code passed the same test.
The assertion `assert c.total() == 30` checks the total of both
products.

**5. Verdict**

-   [x] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test 2: `test_login_rejects_wrong_password`

**Audited by:** Zarr Ni Htut (Raymand)

**1. What it claims to catch**

Checks whether the login system rejects an incorrect password. It does
not specifically test the group's special-character password defect.

**2. Evidence --- against shipped code**

``` text
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
```

**3. Evidence --- against fixed code**

``` text
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
```

**4. What that pair proves**

This is **Detects nothing --- PASS then PASS**. The wrong-password
rejection assertion passes in both versions, so it does not reveal a
defect fixed by the group. To test the special-character login defect, a
test would need to register a user with a password containing symbols
and check login using that exact password.

**5. Verdict**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test 3: `test_search_finds_exact_title`

**Audited by:** Aung Myo Naing (Jerry)

**1. What it claims to catch**

Checks whether searching for an exact product title returns the matching
product. It does not specifically establish that search is
case-insensitive.

**2. Evidence --- against shipped code**

``` text
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
```

**3. Evidence --- against fixed code**

``` text
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
```

**4. What that pair proves**

This is **Detects nothing --- PASS then PASS**. The exact-title search
assertion passes in both versions. To test the group's case-insensitive
search finding, the search assertion would need to use a different
letter case from the stored product title, for example, store
`Python Testing` and search for `python`.

**5. Verdict**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test 4: `test_import_returns_count`

**Audited by:** Aung Myo Naing (Jerry)

**1. What it claims to catch**

Checks whether importing two products returns an imported-product count
of 2. It is intended to catch an incorrect count from the bulk-import
function.

**2. Evidence --- against shipped code**

``` text
ai_review/test_ai_generated.py::test_import_returns_count FAILED
E       AssertionError: assert 3 == 2
```

**3. Evidence --- against fixed code**

``` text
ai_review/test_ai_generated.py::test_import_returns_count PASSED
```

**4. What that pair proves**

This is **Genuine detection --- FAIL then PASS**. The shipped function
returned 3 when the test expected 2, and the fixed version passed. The
assertion compares the import return value with the number of products
supplied.

**5. Verdict**

-   [x] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test 5: `test_checkout_empty_returns_none`

**Audited by:** Zay Htet (Zett)

**1. What it claims to catch**

Checks whether checking out with an empty cart returns `None`. It is
intended to catch empty checkout returning an unexpected value.

**2. Evidence --- against shipped code**

``` text
ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED
E       assert [] is None
```

**3. Evidence --- against fixed code**

``` text
ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED
```

**4. What that pair proves**

This is **Genuine detection --- FAIL then PASS**. The shipped code
returned an empty list instead of `None`, while the fixed code passed
the test.

**5. Verdict**

-   [x] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test 6: `test_add_to_cart_returns_true_for_known_product`

**Audited by:** So Pyay Htoo (Yummy)

**1. What it claims to catch**

Checks whether adding a known product to the cart returns a successful
result. It checks the normal add-to-cart operation.

**2. Evidence --- against shipped code**

``` text
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
```

**3. Evidence --- against fixed code**

``` text
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
```

**4. What that pair proves**

This is **Detects nothing --- PASS then PASS**. The known-product
add-to-cart assertion passes in both versions, so it does not detect a
defect fixed by the group. It does not test the cart-total calculation;
to detect that bug, the assertion must check that the total includes the
prices of every item added.

**5. Verdict**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

#### Test 7: `test_search_is_limited_to_ten_results`

**Audited by:** So Pyay Htoo (Yummy)

**1. What it claims to catch**

Checks whether catalogue search returns no more than ten matching
products. It creates 20 matching products and asserts that the search
result count is at most 10.

**2. Evidence --- against shipped code**

Command used for the full shipped-code run: `python -m pytest -v`

``` text
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
E       AssertionError: assert 20 <= 10
E       + where 20 = len([0, 1, 2, 3, 4, 5, ...])
```

**3. Evidence --- against fixed code**

Command used for the final full run: `python -m pytest -v`

``` text
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
E       AssertionError: assert 20 <= 10
E       + where 20 = len([0, 1, 2, 3, 4, 5, ...])
```

**4. What that pair proves**

This is **FAIL then FAIL** in the group's runs. The catalogue returned
20 matching products before and after the group's fixes. These results
do not, by themselves, establish whether a ten-result cap is an actual
application requirement. If the project specification does not require
this limit, the test assumes an unsupported requirement and should be
classified as an invented requirement. The classification remains
provisional until the specification is checked.

**5. Verdict**

-   [ ] Genuine detection --- FAIL then PASS
-   [ ] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [x] Invented requirement --- FAIL then FAIL (provisional; verify
    specification)

#### Test 8: `test_register_duplicate_returns_false`

**Audited by:** Min Khant Kyaw (Sonic)

**1. What it claims to catch**

Checks whether registering an existing username returns `False`.

**2. Evidence --- against shipped code**

``` text
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
```

**3. Evidence --- against fixed code**

``` text
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
```

**4. What that pair proves**

This is **Detects nothing --- PASS then PASS**. Duplicate registration
already returned `False` in the shipped version. The test passes on both
versions and does not detect a bug fixed by the group.

**5. Verdict**

-   [ ] Genuine detection --- FAIL then PASS
-   [x] Detects nothing --- PASS then PASS
-   [ ] Locks in the bug --- PASS then FAIL
-   [ ] Invented requirement --- FAIL then FAIL

### 2.4 Full Test-Run Evidence Summary

The following results are transcribed from the group's terminal output.
The initial full run used Python 3.12.10 and pytest 9.2.0. The later
smoke, regression, and slow runs used pytest 9.1.1. The environment
versions differ, so the commands and results are reported as they were
run.

**A. Initial full run against shipped code**\
Command: `python -m pytest -v`

``` text
collected 10 items

ai_review/test_ai_generated.py::test_cart_total_sums_items FAILED
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
ai_review/test_ai_generated.py::test_import_returns_count FAILED
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
ai_review/test_ai_generated.py::test_checkout_empty_returns_none FAILED
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
tests/test_bookstore.py::test_example_register PASSED
worked_example/test_notes.py::test_word_count_counts_words_not_characters FAILED

5 failed, 5 passed in 0.29s
```

The five failures were: - `test_cart_total_sums_items`: returned 10
instead of 30. - `test_import_returns_count`: returned 3 instead of 2. -
`test_checkout_empty_returns_none`: returned `[]` instead of `None`. -
`test_search_is_limited_to_ten_results`: returned 20 results instead of
no more than 10. - `test_word_count_counts_words_not_characters`:
returned 18 instead of 3.

The last failure belongs to `worked_example/test_notes.py`, not to the
eight AI-generated tests.

**B. Smoke tests**\
Command: `python -m pytest -m smoke -v`

``` text
collected 16 items / 9 deselected / 7 selected
7 passed, 9 deselected in 0.06s
```

The seven selected smoke tests all passed: example registration, new
user registration, correct-password login, adding a catalog product,
searching for a product, adding a product to the cart, and non-empty
checkout.

**C. Regression tests against shipped code**\
Command: `python -m pytest -m regression -v`

``` text
collected 22 items / 16 deselected / 6 selected
5 failed, 1 passed, 16 deselected in 0.20s
```

The five failures were: - `test_login_preserves_symbols_in_password`:
login returned `False` for the registered password `p@ss-word!42`. -
`test_catalog_search_ignores_letter_case`: searching for `python`
returned `[]` instead of `[1]`. -
`test_catalog_search_with_empty_keyword`: searching with an empty
keyword returned `[1, 2]` instead of `[]`. -
`test_cart_total_includes_last_item`: returned 10 instead of 30. -
`test_empty_checkout_returns_none_without_saving_order`: returned `[]`
instead of `None`.

`test_login_rejects_password_with_different_symbols` passed.

**D. Regression tests against fixed code**\
Command: `python -m pytest -m regression -v`

``` text
collected 25 items / 19 deselected / 6 selected
6 passed, 19 deselected in 0.06s
```

All six selected regression tests passed after the group's fixes.

**E. Slow tests against shipped code**\
Command: `python -m pytest -m slow -v`

``` text
collected 25 items / 22 deselected / 3 selected
2 failed, 1 passed, 22 deselected in 0.19s
```

The 10,000-user registration/login test failed when login for `user_0`
returned `False`. The 20,000-product bulk-import test returned 20,001
instead of 20,000. The large-catalog search test passed.

**F. Slow tests against fixed code**\
Command: `python -m pytest -m slow -v`

``` text
collected 25 items / 22 deselected / 3 selected
3 passed, 22 deselected in 0.08s
```

All three selected slow tests passed after the group's fixes.

**G. Full run after bookstore fixes, before the notes fix**\
Command: `python -m pytest -v`

``` text
collected 25 items
2 failed, 23 passed in 0.23s
```

The remaining failures were `test_search_is_limited_to_ten_results` and
`test_word_count_counts_words_not_characters`. The group then changed
`worked_example/notes.py` to use `.split()` and committed that change as
`a5871d0` (`add the split method to countthe words correctly`).

The separate bookstore-only command was:

``` powershell
python -m pytest tests/test_bookstore.py
```

Actual result:

``` text
16 passed in 0.15s
```

**H. Final full run after the notes fix**\
Command: `python -m pytest -v`

``` text
collected 25 items

ai_review/test_ai_generated.py::test_cart_total_sums_items PASSED
ai_review/test_ai_generated.py::test_login_rejects_wrong_password PASSED
ai_review/test_ai_generated.py::test_search_finds_exact_title PASSED
ai_review/test_ai_generated.py::test_import_returns_count PASSED
ai_review/test_ai_generated.py::test_register_duplicate_returns_false PASSED
ai_review/test_ai_generated.py::test_checkout_empty_returns_none PASSED
ai_review/test_ai_generated.py::test_add_to_cart_returns_true_for_known_product PASSED
ai_review/test_ai_generated.py::test_search_is_limited_to_ten_results FAILED
tests/test_bookstore.py — all 16 tests PASSED
worked_example/test_notes.py::test_word_count_counts_words_not_characters PASSED

1 failed, 24 passed in 0.22s
```

The final run shows that all 24 other tests passed, including all
bookstore tests and the worked-example word-count test. The only
remaining failure was `test_search_is_limited_to_ten_results`, which
returned 20 results.

**I. Individual command for the remaining search-limit test**

To run the remaining test by itself, use:

``` powershell
py -m pytest -q --tb=short ai_review\test_ai_generated.py::test_search_is_limited_to_ten_results
```

No isolated output or elapsed time for this command was included in the
supplied terminal logs. Run the command and record its actual result. Do
not use the full-suite runtime of 0.22s as the individual test time.

**Timing clarification:** The times above are runtimes for the complete
pytest commands. They are not individual test durations.

**Evidence limitation:** The supplied terminal logs do not show the
original shipped-code commit hash or an isolated checkout command. Do
not add a commit ID for the shipped-code run unless the group
independently verifies it.

### 2.5 Classification Summary

  Verdict                                                      Number of tests
  ---------------------------------------------------------- -----------------
  Genuine detection                                                          3
  Detects nothing                                                            4
  Locks in the bug                                                           0
  Invented requirement (provisional; verify specification)                   1
  **Total**                                                              **8**

**Overall finding:** Three tests genuinely detected defects fixed by the
group: cart total, bulk-import count, and empty checkout. Four tests
passed against both versions and detected nothing. The search-limit test
failed against both versions in the group's runs. It is provisionally
classified as an invented requirement only if the project specification
does not require a ten-result limit.

------------------------------------------------------------------------

## Part 3 --- Coverage Against Our Own Bug Hunt

One row is included for each of the seven bugs in the group's
`FINDINGS.md`, plus a row for the search-limit behaviour asserted by the
supplied test but not recorded as a group finding. Every "Yes" in the
supplied-set column points to a test classified as a genuine detection
in Part 2.

  ----------------------------------------------------------------------------------------------------------------
  Bug (our           We found it       The supplied set  Which test, and how we established that
  description)                         catches it        
  ------------------ ----------------- ----------------- ---------------------------------------------------------
  Login fails with   Yes               No                `test_login_rejects_wrong_password` passes on both
  special characters                                     versions. It tests a wrong password, not preservation of
  in passwords.                                          special characters. The group's
                                                         `test_login_preserves_symbols_in_password` tests the
                                                         affected case.

  Case-insensitive   Yes               No                `test_search_finds_exact_title` passes on both versions.
  catalogue search                                       Its exact-title assertion does not establish
  fails.                                                 case-insensitive coverage. The group's
                                                         `test_catalog_search_ignores_letter_case` tests this
                                                         behaviour.

  Empty-keyword      Yes               No                None of the eight supplied tests specifically checks an
  search returns all                                     empty search keyword. The group's
  products instead                                       `test_catalog_search_with_empty_keyword` tests this
  of an empty list.                                      behaviour.

  Cart total         Yes               Yes               `test_cart_total_sums_items` fails on shipped code (10
  excludes the last                                      instead of 30) and passes on fixed code. The group's
  item.                                                  `test_cart_total_includes_last_item` records the same
                                                         defect.

  Empty checkout     Yes               Yes               `test_checkout_empty_returns_none` fails on shipped code
  returns `[]`                                           and passes on fixed code. The group's
  instead of `None`.                                     `test_empty_checkout_returns_none_without_saving_order`
                                                         checks the same empty-cart behaviour.

  Login fails after  Yes               No                None of the eight supplied tests checks registration and
  registering 10,000                                     login with 10,000 users. The group's
  users.                                                 `test_register_and_login_many_users` tests this scenario.

  Bulk import of     Yes               Yes               `test_import_returns_count` fails on shipped code (3
  20,000 products                                        instead of 2) and passes on fixed code. The group's
  returns an                                             `test_bulk_import_many_products` checks the same
  incorrect count.                                       import-count behaviour at 20,000 products.

  Search returns 20  No                No                `test_search_is_limited_to_ten_results` fails on both
  results when the                                       shipped and fixed code. The pair does not establish a
  supplied test                                          fixed defect. Verify the application specification before
  expects no more                                        deciding whether a ten-result cap is required; the test's
  than 10.                                               failure alone is not proof of a bug.
  ----------------------------------------------------------------------------------------------------------------

**Part 3 finding:** The supplied set genuinely catches three bugs
already found by the group: cart total, empty checkout, and bulk-import
count. It does not establish coverage of the other four group findings.
It did not establish an additional confirmed bug that the group had
missed.

------------------------------------------------------------------------

## Part 4 --- Verdict (under 400 words)

**1. Which failure mode was most common?**

"Detects nothing" was the most common result, with **4 of 8 tests**.
Tests 2, 3, 6, and 8 passed against both shipped and fixed code. Three
tests were genuine detections, none locked in a bug, and one failed
against both versions.

**2. Why is a test that passes against buggy code more dangerous than
one that crashes?**

A failing test attracts attention and tells the team that something
needs investigation. A test that passes while a defect is present can
create false confidence. The team may believe the feature works
correctly and leave the defect undiscovered.

**3. Did the supplied set catch anything we had missed?**

No confirmed additional bug was found. The three genuine detections ---
cart total, import count, and empty checkout --- correspond to bugs
already recorded in our `FINDINGS.md`. The ten-result search test failed
in both versions, but that does not establish a real defect or an
application requirement.

**4. What will we check before trusting a generated test in future?**

We will inspect the test's setup and assertion, confirm that its
expected behaviour is required, and run it against both shipped and
fixed code. In this exercise, we compared the actual results: the
cart-total, import-count, and empty-checkout tests changed from FAIL to
PASS; four tests passed in both versions; and the ten-result search test
failed in both. We will also compare generated tests with our own
regression tests to ensure they check the same specific behaviour.
