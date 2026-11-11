# Scope

## Who it's for

Freelancers and small business owners. They send a handful of quotes or payment documents a month and don't want to pay for invoicing software or fight with a spreadsheet template.

## The problem

Today they build each quote by hand in a word processor or spreadsheet: retype the client details, recalculate totals, apply VAT and discount, export to PDF. It is slow, and a small arithmetic or formatting mistake makes them look unprofessional. If the client pays in another currency, they also have to look up the exchange rate manually.

## What the tool does

A small command-line tool, written in Python, that turns a data file into a PDF.

**Input:** a CSV or JSON file containing:
- client details
- line items (description, quantity, unit price)
- VAT rate
- discount

**Output:** a PDF quote or payment document with:
- a progressive document number
- subtotal, discount, VAT and total, calculated automatically
- optional conversion to another currency, using live exchange rates from an external API (API key stored in a `.env` file, never in the repo)

**Along the way:**
- input data is validated, and errors are readable ("line 3: quantity must be a positive number")
- API failures (timeout, bad key, no connection) produce a clear message instead of a crash

## Out of scope

- Italian electronic invoicing (XML / SDI) or any document with fiscal value. The output is a quote or pro forma, and the README says so clearly.
- Web interface, database, user accounts.
- Sending emails automatically.

## Known limitations

This project tries to remove some of the pain of writing quotes, but it is built for educational purposes: the user still has to type all the data by hand into a CSV or JSON file, so it is not yet a complete solution to the problem.

## Done when

From a sample file, one command produces a correct PDF, including in a different currency, and an API error does not crash the program.
