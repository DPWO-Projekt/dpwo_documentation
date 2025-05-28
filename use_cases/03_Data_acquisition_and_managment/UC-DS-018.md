[UC-DS-018] Upload dataset distribution
---

[pre] user is logged-in as Data Supplier.<br>
[pre] invoked by UC-DS-014 Show owned dataset list.

1. User clicks "Attach distribution" button located on specific dataset.
2. System presents new dataset distribution form with related dataset name.
3. User fills out necessary fields in form.
4. User clicks "Create dataset distribution" button.
5. System validates correctness of data.

[data is invalid]<br>
    6a. System displays modal form window with validation highlights.<br>
    `<return to step 3>`

[data is valid]<br>
   6. System saves information related to new dataset distribution.<br>
   7. System redirects towards owned dataset list view.<br>
   8. System shows confirmation pop-up.<br>

[post] dataset distribution is attached to related dataset