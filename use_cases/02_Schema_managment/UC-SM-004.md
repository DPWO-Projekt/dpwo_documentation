[UC-SM-004] Edit data schema
---

[pre] user is logged-in as Metadata Manager<br/>
[pre] invoked by [UC-SM-007](UC-SM-007.md) Show data schema list

1. User chose “add button” in data schema list view.
2. System displays a modal window containing data schema form filled with already provided information.
3. User updates form with data schema data.
4. User clicks the “Save“ button.
5. System validates provided data schema data.

[Data is correct]<br/>
    5a. System saves edited data schema data.<br/>
    6a. System presents confirmation modal.<br/>
    7a. User clicks “OK“.<br/>
    8a. System returns to data schema list view.<br/>
    **POST**: data updated succesfully<br/>

[Data is incorrect]<br/>
    5a. System presents error inside of modal window.<br/>
    6a. User clicks “OK” button.<br/>
    7a. System returns to data schema list view.<br/>
    **POST**: updating data failed<br/>