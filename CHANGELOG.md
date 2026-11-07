# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.1.0] - 2026-11-07
### Added
- `Cart.sort_by_title()` and `Cart.sort_by_cost()` to sort DVDs in the cart.
- `search_by_category()` in aims/search.py

## [1.0.1] - 2026-11-07
### Fixed
- Make `search_by_title()` case-insensitive (#20).

## [1.0.0] - 2026-11-07
### Added
- `Cart.print_cart()` to display ordered DVDs and total cost.
- `search_by_title()` in `aims/search.py` to search DVDs by title keyword.
- `Cart.total_cost_with_discount()` to calculate discounted cart total.
- Vietnamese notification message when adding a DVD to the cart.

### Changed
- Refactored `dvd.py` and `cart.py` into the `aims` package.

### Fixed
- Cart accepting the 21st DVD beyond `MAX_NUMBERS_ORDERED = 20` (#8).
- Discount calculation formula and percentage validation (`0 <= percent <= 100`).
