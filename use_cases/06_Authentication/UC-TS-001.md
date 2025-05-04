[UC-TS-001] Register User
---

[pre] Unauthenticated user tries to access website.

1. System presents login form.
2. User clicks "Sign up" button.
3. System presents registration form.
4. User fills form with all necessary data.
5. User click "Register" button.
6. System validates form.

[Data incorrect] <br/>
    7a. System presents registration form with incorrectly filled inputs highlighted. <br/>
    `<return to step 4>`

[Data correct] <br/>
   7. System creates and saves new user details. <br/>
   8. System redirects towards landing page.