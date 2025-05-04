[TS-01-DM-006] Positive test case
---
[pre] user is logged-in as Metadata Manager<br>
[pre] there is at least one catalogue in database<br>
[pre] there is at least one dataset in present catalogues without set schema<br>

**Input**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User selects a dataset definition without schema.<br>
**Output**: 
- System displays an enabled `Set schema` button in the dataset’s table row.
- The chosen dataset in the database has `schemaId` set to `NULL`.

**Input**: Users performs [UC-DM-006](../../use_cases/01_Data_managment/UC-DM-006.md)<br>
**Output**: 
- System displays a confirmation message: **"Schema assigned"**.
- The chosen dataset in the database has `schemaId` set to a non-null value.
- A schema with the corresponding `schemaId` exists in the database.

[post] in chosen catalogue, chosen dataset schema exists with set schema<br>
[post] the dataset row in the catalogue table now displays an assigned schema and no longer shows the `Set schema` button.
[post] the dataset row now displays enabled `Edit schema` button.


[TS-02-DM-006] Negative test case
---
[pre] user is logged in as Metadata Manager<br>
[pre] there is at least one catalogue in database<br>
[pre] there is at least one dataset in present catalogues without set schema<br>
[pre] in database there is no data schema definition<br>

**Input:**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User selects a dataset definition without schema.
**Output**:
- System displays an enabled `Set schema` button in the dataset’s table row.
- The chosen dataset in the database has `schemaId` set to `NULL`.

**Input**: Users performs [UC-DM-006](../../use_cases/01_Data_managment/UC-DM-006.md).<br>
**Output**: System displays error message: **"No data schema defined"** and `Go back` button.

**Input**: User selects `Go back` button.<br>
**Output**: System displays dataset list in the catalogue.

[post] chosen dataset does not have set data schema