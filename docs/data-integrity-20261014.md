# Data Integrity Notes

- Use stable IDs for transactions.
- Recompute totals after add, edit, or delete operations.
- Keep stored amounts numeric and format currency only for display.
- Validate dates before applying monthly filters.
- Treat malformed persisted data as recoverable rather than crashing.