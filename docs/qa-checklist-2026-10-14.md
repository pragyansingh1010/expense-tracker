# Expense Tracker — QA Checklist

- Check totals after adding, editing, and removing transactions.
- Verify date filters include the intended start and end dates.
- Handle empty descriptions and invalid amounts safely.
- Confirm local persistence survives refresh and malformed data is recoverable.
- Test category totals against the transaction list.
- Render descriptions safely to prevent HTML injection.