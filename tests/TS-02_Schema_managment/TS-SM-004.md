[TC-01-SM-004] Edit data schema with new data
---
**Reference UC**:[UC-SM-004](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-004.md)

[pre] User logged in as Metadata Manager.
**Input**: User preforms steps from [UC-SM-004](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-004.md):<br>
-User choses data schema Test schema.
-User edit the fields Theme with Test schema editing properties:
* Date with value 10.04.2025.<br>
**Output**: The “Data schemas” window is displayed with updated data schema.

[TC-02-SM-004] Edit type Date to type Link
---
**Reference UC**:[UC-SM-004](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-004.md)

[pre] User logged in as Metadata Manager.
**Input**: User choses data schema Test schema editing. User edits properties with steps described in [UC-SM-004](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-004.md):
* user changes type Date with value 10.04.2025 to type Link with value https://isod.ee.pw.edu.pl/isod-stud/.<br>
**Output**: The “Data schemas” window is displayed with updated data schema.

[TC-03-SM-004] Edit data schema with empty value
---
**Reference UC**:[UC-SM-004](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-004.md)

[pre] User logged in as Metadata Manager.
**Input**: User choses data schema Test schema editing. User leaves fields empty.<br>
**Output**: The “Data schemas” window is not displayed, an error message is shown indicating the mandatory field is missing, and the data schema is not updated.

[TC-04-SM-004] Edit data schema with too long properties
---
**Reference UC**:[UC-SM-004](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-004.md)

[pre] User logged in as Metadata Manager.
**Input**: User fills fields as described in [UC-SM-002](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-0042.md) with value over 100 characters.<br>
**Output**: The “Data schemas” window is not displayed, an error message Unexpected error! is shown, and the data schema is not updated.

[TC-05-SM-004] Edit data schema with incorrect data
---
**Reference UC**:[UC-SM-004](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-004.md)

[pre] User logged in as Metadata Manager.
**Input**: User choses data schema Test schema editing. While editing user fills in the fields Theme with Test schema without property and leaves empty properties.<br>
**Output**: The “Data schemas” window is not displayed, an error message Unexpected error! is shown, and the data schema is not updated.