[UC-DM-006] Set data schema for dataset
---

**Test ID:** `AT-DM-006-n1` </br>
**Use Case ID:** `UC-DM-006`</br>
**Description:** Verify that the user cannot assign data schema to dataset if no data schema is defined. </br>

[pre] user is logged in as Metadata Manager
[pre] there is at least one catalogue in database</br>
[pre] there is at least one dataset in present catalogues without set schema</br>
[pre] in database there is no data schema definition </br>

| **Step** | **Description** | **Expected result** |
|---|---|---|
| 1 | User navigates to dataset list as described in UC-DM-007. | System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled. |
| 2 | User selects a dataset definition without schema. | System displays an enabled `Set schema` button in the dataset’s table row. |
|   |   | The chosen dataset in the database has `schemaId` set to `NULL`. |
| 3 | Users performs UC-DM-006. | System displays error message: **"No data schema defined"** and `Go back` button. |
| 4 | User selects `Go back` button. | System displays dataset list in the catalogue.
---

[post] chosen dataset does not have set data schema