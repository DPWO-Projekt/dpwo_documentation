## [TS-01-DM-002] Successfully add dataset

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>

**Input**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User adds a dataset as described in [UC-DM-002](../../use_cases/01_Data_managment/UC-DM-002.md) using example data:

- **theme**: Trees<br>
- **URI**: https://warsaw-trees.com<br>
- **title**: Warsaw Trees<br>
- **description**: Trees in Warsaw.<br>
- **language**: PL

**Output**: Success message is displayed. User is navigated back to the dataset list defined in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md). New dataset is present in the list.

## [TS-02-DM-002] Try to add dataset using incorrect data

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>

**Input**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User tries to add a dataset as described in [UC-DM-002](../../use_cases/01_Data_managment/UC-DM-002.md) using incorrect data. Example data:

- **theme**: Trees<br>
- **URI**: warsaw-trees<br>
- **title**: Warsaw Trees<br>
- **description**: Trees in Warsaw.<br>
- **language**: PL

**Output**: Error message is displayed. Incorrect data is highlighted. Form stays opened. Dataset is not added.

## [TS-03-DM-002] Try to add dataset with empty mandatory property

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>

**Input**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User tries to add a dataset as described in [UC-DM-002](../../use_cases/01_Data_managment/UC-DM-002.md) with empty mandatory property. Example data:

- **theme**:
- **URI**: https://warsaw-trees.com
- **title**: Warsaw Trees<br>
- **description**: Trees in Warsaw.<br>
- **language**: PL

**Output**: Error message is displayed. Empty mandatory field is highlighted. Form stays opened. Dataset is not added.
