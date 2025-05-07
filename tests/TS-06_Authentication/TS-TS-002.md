## [TS-01-TS-002] Successful login

[pre] User has a account registered in the system. ([UC-TS-003](../../use_cases/06_Authentication/UC-TS-003.md))<br>

**Input**: User inputs existing account credentials and logs in as described in [UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md).<br>
**Output**: System authenticates the user and navigates to the landing page (dataset list) defined in [UC-DM-007](../../use_cases/01_Data_managment/UC-DM-007.md).

## [TS-02-TS-002] Unsuccessful login

[pre] User has a account registered in the system. ([UC-TS-003](../../use_cases/06_Authentication/UC-TS-003.md))<br>

**Input**: User inputs invalid combination of credentials and tries to log in as described in [UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md).<br>
**Output**: System rejects the user and stays at the login page. Error message is displayed. User is not allowed to access the system.
