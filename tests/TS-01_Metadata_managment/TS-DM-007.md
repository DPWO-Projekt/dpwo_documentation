[TC-01-DM-007] Opening Datasets Catalog – dataset available
---
**Reference UC**: [UC-DM-007](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/01_Metadata_managment/UC-DM-007.md)

[pre] User is logged in as Metadata Manager

[pre] There is at least one dataset in the catalogue

**Input**: User navigates to the dataset catalog via the "Show Dataset Catalog" widget on the landing page.

**Output**: System displays the “Datasets Catalog” window.The window shows a list of available datasets.

[TC-02-DM-007] Opening Datasets Catalog – no datasets available
---
**Reference UC:** [UC-DM-007](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/01_Metadata_managment/UC-DM-007.md)

[pre] User is logged in as Metadata Manager

[pre] No datasets exist in the catalogue

**Input**: User navigates to the dataset catalog via the "Show Dataset Catalog" widget on the landing page.

**Output**: The “Datasets Catalog” window is displayed, catalog is empty.

[TC-03-DM-007] Access without being logged in
---
**Reference UC:** [UC-DM-007](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/01_Metadata_managment/UC-DM-007.md)

[pre] User is not logged in

**Input**: User accesses the landing page and attempts to click the “Go To” button in the “Show Dataset Catalog” widget.

**Output**: No session is created; user remains on login screen after redirection
