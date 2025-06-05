[TC-01-DU-004] Downloading dataset in CSV format
---
[pre] User is logged in as Data User<br>
[pre] There is at least one dataset in dataset catalog. <br>
[pre] Existing has CSV distribution avaliable.

**Input**: User performs steps for [UC-DU-014]("../../../../use_cases/04_Data_usage/UC-DU-014.md)<br>
**Output**: Dataset catalog window with datasets is displayed.

**Input**: User performs steps from [UC-DU-004]("../../../../use_cases/04_Data_usage/UC-DU-004.md) choosing "CSV" distribution<br>
**Output**: File is downloaded to user's local system.

[post] The user is able to open CSV file with chosen dataset's data.<br>


[TC-02-DU-004] No distribution is avaliable
---
[pre] User is logged in as Data User<br>
[pre] No dataset in dataset catalog. <br>

**Input**: User performs steps for [UC-DU-014]("../../../../use_cases/04_Data_usage/UC-DU-014.md)<br>
**Output**:  System displays empty catalog window.

[post] The user is not able to select dataset.<br>

[TC-03-DU-004] Network error
---
[pre] User is logged in as Data User<br>
[pre] There is at least one dataset in dataset catalog. <br>
[pre] Existing has CSV distribution avaliable.

**Input**: User performs steps for [UC-DU-014]("../../../../use_cases/04_Data_usage/UC-DU-014.md)<br>
**Output**: Dataset catalog window with datasets is displayed.

**Input**: The user disconnects frontend server and does not reload the page.<br>
**Output**: System displays catalog window.

**Input**: The user clicks `download` button. <br>
**Output**: System displays network error message.

[post] The user is able to refresh the page.