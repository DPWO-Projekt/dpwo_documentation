
## [TC-01-DU-014] Opening Datasets Catalog as Data User – datasets available

**Reference UC:** [UC-DU-014](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/04_Data_usage/UC-DU-014.md)

[pre] User is logged in as Data User <br>
[pre] User is currently on the landing page <br>
[pre] At least one dataset is available in the catalog <br>

**Input:**  
User clicks the "Go To" button on "Show dataset catalog" widget.

**Output:**  
System displays the Datasets Catalog window.  
The window contains a list of datasets available to the user.

---

## [TC-02-DU-014] Opening Datasets Catalog as Data User – no datasets available

**Reference UC:** [UC-DU-014](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/04_Data_usage/UC-DU-014.md)

[pre] User is logged in as Data User <br>
[pre] User is currently on the landing page <br>
[pre] No datasets exist in the catalog <br>

**Input:**  
User clicks the “Go To” button on "Show dataset catalog" widget.

**Output:**  
System displays the Datasets Catalog window with an empty list.

---

## [TC-03-DU-014] Attempting to open catalog while not logged in

**Reference UC:** [UC-DU-014](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/04_Data_usage/UC-DU-014.md)

[pre] User is not logged in

**Input**: User accesses the landing page and attempts to click the “Go To” button in the “Show Dataset Catalog” widget.


**Output:**  No catalog view is shown. User remains on login screen after redirection

---

