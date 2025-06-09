[TC-01-DS-014] Positive test – owned datasets exist
---

**Reference UC:** [UC-DS-014](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/03_Data_acquisition_and_managment/UC-DS-014.md)

[pre] User is logged in as Data Supplier ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>
[pre] User is currently on the landing page <br>
[pre] The user has at least one dataset assigned <br>

**Input:**  
User clicks the "Go To" button on the "Owned Datasets" tile.

**Output:**  
System displays a list of datasets owned by the user.  
Each dataset has an "Attach distribution" button next to it.


[TC-02-DS-014] Positive test – no owned datasets
---

**Reference UC:** [UC-DS-014](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/03_Data_acquisition_and_managment/UC-DS-014.md)

[pre] User is logged in as Data Supplier ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))<br>
[pre] User is currently on the landing page <br>
[pre] The user has no datasets assigned <br>

**Input:**  
User clicks the "Go To" button on the "Owned Datasets" tile.

**Output:**  
System displays a list of datasets owned by the user. The list is empty.


[TC-03-DS-014] Negative test – user not logged in
---
**Reference UC:** [UC-DS-014](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/03_Data_acquisition_and_managment/UC-DS-014.md)

[pre] User is not logged in <br>

**Input:**  
User accesses the landing page and clicks the "Go To" button on the "Owned Datasets" tile.

**Output:**  
System prevents access to the dataset list view.  
User is redirected to the login page.

---

[ok](#tc-01-ds-014-positive-test--owned-datasets-exist)
[ok](#tc-02-ds-014-positive-test--no-owned-datasets)
[ok](#tc-03-ds-014-negative-test--user-not-logged-in)


