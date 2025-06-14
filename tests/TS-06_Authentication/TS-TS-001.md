[TS-01-TS-001] Sucessfull user registration
---

[pre] User is not authenticated.<br>

**Input**: User perform steps described in [UC-TS-001](../../use_cases/06_Authentication/UC-TS-001.md) with input:
- **First name**: John
- **Lastname**: Smith
- **Username**: test-01
- **E-mail**: test@test.pl
- **Role**: Metadata manager
- **Password**: test-01-25
- **Repeat password**: test-01-25<br>
  
**Output**: The system displays landing page.<br>

[post] New user is created by the system.<br>
[post] User is able to log-in using set credentials via [[UC-TS-002]](https://github.com/DPWO-Projekt/dpwo_documentation/blob/main/use_cases/06_Authentication/UC-TS-002.md).<br>


[TS-02-TS-001] Failed user registration with incorrect e-mail
---

**Input**: User perform steps described in [UC-TS-001](../../use_cases/06_Authentication/UC-TS-001.md) with input:
- **First name**: John
- **Lastname**: Smith
- **Username**: test-02
- **E-mail**: test
- **Role**: Metadata manager
- **Password**: test-02-25
- **Repeat password**: test-02-25<br>
  
**Output**: System displays highlights on e-mail input field. 

[post] User is not registered.


[TS-03-TS-001] Failed user registration with password missmatch
---

**Input**: User perform steps described in [UC-TS-001](../../use_cases/06_Authentication/UC-TS-001.md) with input:
- **First name**: John
- **Lastname**: Smith
- **Username**: test-03
- **E-mail**: test@test.pl
- **Role**: Dataset manager
- **Password**: test-03-25
- **Repeat password**: test<br>
  
**Output**: System displays highlights on `Repeat password` input field.

[post] New user is not registered.
