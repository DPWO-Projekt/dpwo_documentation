[TC-01-SM-002] Successful add data schema
---
**Reference UC**:[UC-SM-002](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-002.md)

[pre] User is logged in as Metadata Manager.<br>
**Input**: User perform steps described in [UC-SM-002](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-002.md) with input:
- **type**: Data
- **value** 01.01.2025.

**Output**: The system displays the “Dataset Schemas” window with new added data schema.

[TC-02-SM-002] Unsuccessful add empty data schema
---
**Reference UC**:[UC-SM-002](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-002.md)

[pre] User is logged in as Metadata Manager.<br>
**Input**:  User leaves fields empty.
**Output**: The system does not displays “Datasets Catalog” window, an error message is shown indicating the mandatory field is missing and the data schema is not added to the list.

[TC-03-SM-002] Unsuccessful add data schema with too long properties
---
**Reference UC**:[UC-SM-002](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-002.md)

[pre] User is logged in as Metadata Manager.<br>
**Input**: User fills fields as described in [UC-SM-002](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-0042.md) with value over 100 characters.
**Output**: The system does not displays “Datasets Catalog” window, an error message Unexpected error! is shown, and the data schema is not added to the list.

[TC-04-SM-002] Unsuccessful add data schema without property
---
**Reference UC**:[UC-SM-002](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/02_Schema_managment/UC-SM-002.md)

[pre] User logged in as Metadata Manager.
**Input**:  User fills in the fields Theme with Test schema without property and leaves empty properties.
**Output**: The system does not displays “Datasets Catalog” window, an error message Unexpected error! is shown, and the data schema is not added to the list.
