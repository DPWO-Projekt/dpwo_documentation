[TS-01-TS-001] Sucessfull user registration
---

[pre] User is not authenticated.<br>

**Input**: User perform steps described in [UC-TS-001](../../use_cases/06_Authentication/UC-TS-001.md) with input:
- **First name**: John
- **Lastname**: Smith
- **Username**: test-01
- **E-mail**: test@test.pl
- **Role**: Dataset manager
- **Password**: test-01-25
- **Repeat password**: test-01-25
**Output**: The system displays landing page.

[post] New user is created by the system.<br>
[post] User is able to log-in using set credentials.<br>


[TS-02-TS-001] Failed user registration with incorrect e-mail
---

**Input**: User perform steps described in [UC-TS-001](../../use_cases/06_Authentication/UC-TS-001.md) with input:
- **First name**: John
- **Lastname**: Smith
- **Username**: test-02
- **E-mail**: test
- **Role**: Dataset manager
- **Password**: test-02-25
- **Repeat password**: test-02-25
**Output**: System displays highlights on e-mail input field. 

[pre] User is not registered.


[TS-03-TS-001] Failed user registration with password missmatch
---

**Input**: User perform steps described in [UC-TS-001](../../use_cases/06_Authentication/UC-TS-001.md) with input:
- **First name**: John
- **Lastname**: Smith
- **Username**: test-03
- **E-mail**: test@test.pl
- **Role**: Dataset manager
- **Password**: test-03-25
- **Repeat password**: test
**Output**: System displays highlights on `Repeat password` input field.

[pre] New user is not registered.