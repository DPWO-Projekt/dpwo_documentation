[UC-DM-002] Add definition of dataset
---

[<span style="color: violet;">pre</span>] User is logged-in as Metadata Manager<br/>
[<span style="color: violet;">pre</span>] invoked by [UC-DM-007] Show catalog with editing

1. User click “Add definition of dataset“ button on catalog view.
2. System displays a modal window containing the definition of dataset creation form.
    - The form includes fields for mandatory, recommended, and optional attributes.
3. User fills in the fields of the form.
4. User clicks the "Add new dataset definition" button on form to submit the form.
5. System validates the entered information:
    - Ensures all mandatory fields are completed.
    - Verifies the format of the entered data.
  
[<span style="color: green;">Validation is successful</span>]<br/>
    6a. System saves definition of dataset.
    7a. System creates new definition of dataset and closes the form window.
    8a. User is redirected back to the catalog view, where the newly added dataset is now visible.
    9a. System displays a **success message**.

[<span style="color: red;">Validaton Fails</span>]<br/>
    6b. If system detects missing or incorrect data, it displays an **error message** highlighting the problematic fields.
    7b. The user corrects the errors and resubmits the form (return to Step 3).

[<span style="color: red;">Dataset Creation Fails</span>]<br/>
    7c. If an error occurs while saving definition of dataset, the system notifies the user with **error message**.
    8c. User can attempt to submit the form again (return to Step 3).