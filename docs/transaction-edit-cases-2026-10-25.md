## Transaction edit cases

- Keep a transaction's stable identifier when editing it.
- Validate amount, date, and category before saving changes.
- Recalculate totals after a successful edit.
- Canceling an edit should leave the stored transaction unchanged.
- Handle a deleted or missing transaction gracefully.