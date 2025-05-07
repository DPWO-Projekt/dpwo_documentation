## [TS-01-DM-003] Successfully edit dataset

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>

**Input**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User edits a dataset as described in [UC-DM-003](../../use_cases/01_Data_managment/UC-DM-003.md) using example data:

- **theme**: Trees 2<br>
- **URI**: https://warsaw-trees2.com<br>
- **title**: Warsaw Trees 2<br>
- **description**: Trees in Warsaw 2.<br>
- **language**: EN

**Output**: Success message is displayed. User is navigated back to the dataset list defined in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md). Edited dataset is present in the list.

## [TS-02-DM-003] Try to edit dataset using incorrect data

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>

**Input**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User tries to edit a dataset as described in [UC-DM-003](../../use_cases/01_Data_managment/UC-DM-003.md) using incorrect data. Example data:

- **theme**: Trees 2<br>
- **URI**: warsaw-trees2<br>
- **title**: Warsaw Trees 2<br>
- **description**: Trees in Warsaw 2.<br>
- **language**: EN

**Output**: Error message is displayed. Incorrect data is highlighted. Form stays opened. Dataset is not edited.

## [TS-03-DM-003] Try to edit dataset with empty mandatory property

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>

**Input**: User navigates to dataset list as described in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).<br>
**Output**: System displays a list of dataset definitions with `Edit`, `Add`, and `Set schema` buttons enabled.

**Input**: User tries to edit a dataset as described in [UC-DM-003](../../use_cases/01_Data_managment/UC-DM-003.md) with empty mandatory property. Example data:

- **theme**: p.v?y&z0,5d]JL-,;G)njJ;gByzvhSJRg)eH0r4%bL?j2=WVU(L,V#ZP$VvPrKPQ!TT1T$qgp}%#9};uygv_W+Nm5tz,w9:#;XQ_7
- **URI**: https://warsaw-trees2.com
- **title**: Warsaw Trees 2<br>
- **description**: Trees in Warsaw 2.<br>
- **language**: EN

**Output**: Error message is displayed. Empty mandatory field is highlighted. Form stays opened. Dataset is not edited.
