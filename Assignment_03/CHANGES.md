# Assignment 03 — CHANGES

**Name:** Aung Myo Naing **Student ID:** 6705140039

## 1 · What I changed

| # | Code smell in the original | What I changed it to | OOP concept applied | How I verified behaviour was unchanged |
|---|---|---|---|---|
| 1 | Products and order items were stored as tuples and accessed by indexes. | Added `Product` and `OrderItem` classes; `OrderItem` has a `Product`. | Classes / composition | Ran `python Assignment_03.py` and the self-test printed PASS. |
| 2 | Customer tiers used repeated `if/elif` chains for discount and points. | Added `Customer`, `SilverCustomer`, `GoldCustomer`, and `PlatinumCustomer` with polymorphic methods. | Inheritance / polymorphism | Self-test printed PASS; checked each tier's discount and points behavior. |
| 3 | `calc()` mixed calculations, business rules, and printing. | Added pure `subtotal()`, `discount()`, `tax()`, `total()`, and `points()` methods, with receipt formatting in `receipt()`. | Separation of concerns / pure methods | Compared refactored output with the locked legacy output; PASS. |
| 4 | State was not validated and quantities could be invalid. | Constructors validate product data, customer names, order items, and order composition. | Encapsulation / validation | Checked constructors reject invalid values and normal assignment data still passes. |
| 5 | Magic numbers and a leftover `global TAXRATE` were used. | Named constants were introduced and the refactored calculations use instance/object data without `global`. | Clean code / encapsulation | Ran the full self-test and inspected the refactored section for the removed global and named rules. |

## 2 · Short reflection (4–6 sentences)

The biggest improvement was replacing the tier `if/elif` chains with a class family because each customer tier now owns its discount and points rules. This makes the `Order` class work with a customer through a common interface instead of checking the tier itself. Keeping the behaviour identical required careful attention to the original boundary condition: a subtotal of exactly 100 uses the lower discount rate because the original code tests `sub > 100`. I also had to preserve the exact receipt text, item order, rounding, blank line, and grand-total calculation. The self-test compares the complete printed output with the original program, so it provided the final verification.

## 3 · Prompt log (Level-2 required)

| # | My prompt to the AI | What it suggested (summary) | Accept / reject / edited | How I checked it |
|---|---|---|---|---|
| 1 | “Do the assignment using the uploaded Assignment_03.py and CHANGES.md.” | Identified the required OOP refactoring and preserved the legacy behavior lock. | Accepted and edited into the required class design. | Read the generated code and ran the self-test; PASS. |
| 2 | “Refactor the tier discount and points logic using inheritance and polymorphism, without changing the output.” | Suggested a `Customer` base class with tier subclasses implementing discount rates and point multipliers. | Accepted with minor naming/structure edits. | Checked all four tiers and ran the exact-output self-test; PASS. |
| 3 | “Separate calculation from printing, validate constructors, remove magic numbers/global state, and keep the original output exactly the same.” | Suggested `Product`, `OrderItem`, `Order`, named constants, validation, pure calculation methods, and a separate receipt method. | Accepted with edits to preserve the legacy receipt formatting exactly. | Compared `refactored_main()` output against `GOLDEN_OUTPUT`; PASS. |

**Ownership statement.** *By submitting, I confirm I understand and can explain every line of code I submitted, and that this prompt log reflects my actual AI use.*

## 4 · Before-you-submit checklist

- [x] `python Assignment_03.py` prints **PASS**.
- [x] Refactored products, orders, and items are objects.
- [x] No `if tier == ...` chains in the refactored solution.
- [x] Calculation methods return values and do not print; receipt printing is separate.
- [x] Constructors validate state; no leftover `global` in the refactored solution; magic numbers are named.
- [x] The change table and reflection are filled in.
- [x] The prompt log is complete and the ownership statement is signed.
