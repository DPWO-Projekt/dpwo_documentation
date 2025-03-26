[UC-DM-006] Set data schema for dataset
---

**Test ID:** `AT-DM-006-p1` </br>
**Use Case ID:** `UC-DM-006`</br>
**Description:** Verify that the user can assign a data schema to a dataset in the catalog.</br>

[pre] user is logged-in as Metadata Manager</br>
[pre] there is at least one catalogue in database</br>
[pre] there is at least one dataset in present catalogues without set schema</br>

| **Step** | **Description** | **Expected result** |
|---|---|---|
| 1 | User navigates to dataset list as described in UC-DM-007. | System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled. |
| 2 | User selects a dataset definition without schema. | System displays an enabled `Set schema` button in the dataset’s table row. |
|   |   | The chosen dataset in the database has `schemaId` set to `NULL`. |
| 3 | Users performs UC-DM-006. | System displays a confirmation message: **"Schema assigned"**. |
|   |   | The chosen dataset in the database has `schemaId` set to a non-null value. |
|   |   | A schema with the corresponding `schemaId` exists in the database. |
---

[post] in chosen catalogue, chosen dataset schema exists with set schema</br>
[post] the dataset row in the catalogue table now displays an assigned schema and no longer shows the `Set schema` button.
[post] the dataset row now displays enabled `Edit schema` button.



