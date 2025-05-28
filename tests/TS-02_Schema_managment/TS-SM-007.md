[TC-01-SM-007] Display non empty data schema list
---
**Reference UC**:[ UC-SM-007](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-007.md)

[pre] User is logged in as Metadata Manager<br>
[pre] There is at least one data schema in the database

**Input**: User navigates to the “Dataset Schemas”.<br>
**Output**: System displays the “Dataset Schemas” window. The window contains a list of defined schemas available for use.


[TC-02-SM-007] Display empty data schema list
---
**Reference UC**:[ UC-SM-007](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-007.md)

[pre] User is logged in as Metadata Manager<br>
[pre] There are no data schemas in the database

**Input**: User navigates to the “Dataset Schemas”.<br>
**Output**: System displays the “Dataset Schemas” window. Schema list is empty.


[TC-03-SM-007] Data schema list screen for not logged in user
---
**Reference UC**:[ UC-SM-007](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-007.md)

[pre] User is not logged in

**Input**: User accesses the schema management section from the landing page or direct link.<br>
**Output**: Schema list is not accessible without authentication and redirects to the login screen.
