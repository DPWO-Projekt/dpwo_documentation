[UC-TS-001] Register User
---

[<span style="color: violet;">pre</span>] Unauthenticated user tries to access website.

1. System presents login form.
2. User clicks "Sign up" button.
3. System presents registration form.
4. User fills form with all necessary data.
5. User click "Register" button.
6. System validates form.

[<span style="color: red;">Data incorrect</span>] <br/>
    7a. System presents registration form with incorrectly filled inputs highlighted. <br/>
    `<return to step 4>`

[<span style="color: green;">Data correct</span>] <br/>
   7. System creates and saves new user details. <br/>
   8. System redirects towards landing page.