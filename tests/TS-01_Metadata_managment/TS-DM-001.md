[TS-01-DM-001] Add unigue catalog name
---

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>
[pre] There is no catalog named `test-01`

**Input**: User preforms steps as described in [UC-DM-001](../../use_cases/01_Data_managment/UC-DM-001.md) with input:<br>
- **Catalog Name**: test-01
**Output**: System displays catalog list view with `Catalog added` pop-up. Created catalog `test-01` is visible on the list.

[post] Catalog named `test-01` is created by the system.<br> 


[TS-01-DM-001] Add non-unigue catalog name
---

[pre] User is logged-in as Metadata Manager ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>
[pre] Catalog named `test-01` exists in the main catalog.<br>
 
**Input**: User preforms steps from [UC-DM-001](../../use_cases/01_Data_managment/UC-DM-001.md) with input:<br>
- **Catalog Name**: test-01
**Output**: System displays validation highlights on `Add new catalog` modal.

[post] New catalog is not created.