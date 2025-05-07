[UC-DM-003] Edit definition of dataset
---

[pre] User is logged-in as Metadata Manager<br>
[pre] invoked by [UC-DM-007](UC-DM-007.md) Show catalog with editing

1. User click “Edit“ (pencil) icon on catalog view.
2. System retrieves the definition of dataset.
3. System displays a modal window containing definition of dataset edition form filled with definition of dataset.
4. User edits the fields of the form.
5. User clicks the "Save dataset definition" button on form to submit the form.
6. System validates the entered information:
   - Ensures all mandatory fields are completed.
   - Verifies the format of the entered data.

[Validation is successful]<br>
   6a. System saves definition dataset and closes the form window.
   7a. User is redirected back to the catalog view.
   8a. System displays a success message.

[Validaton Fails]<br>
   6b. If system detects missing or incorrect data, it displays an error message highlighting the problematic fields.
   7b. The user corrects the errors and resubmits the form (return to Step 3).

[Dataset Creation Fails]<br>
   7c. If an error occurs while saving definition of dataset, the system notifies the user with error message.
   8c. User can attempt to submit the form again (return to Step 3).
