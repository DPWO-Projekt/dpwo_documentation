[UC-DM-001] Add catalog as part of a catalog
---

[pre] user is logged-in as Metadata Manager.<br/>
[pre] invoked by [UC-DM-007](UC-DM-007.md) Show catalog with editing.

1. User clicks “New catalog” button.
2. System displays modal window with new catalog form.
3. User provides new catalog name.
4. User clicks "Add new catalog".
5. System validates uniqueness of catalog name.
   
[Catalog name is not unique]<br/>
6a. System displays modal form window with validation highlights.<br/>
`<return to step 3>`

[Catalog name is unique]<br/>
6. System saves information related to new catalog.
7. System redirects towards catalog view in which new catalog has been added.
8. System shows confirmation pop-up.