[TC-01-SM-002]
---
Input: User logged in as Metadata Manager. User fills in the fields Theme with Test schema and properties - type Data with value 10.04.2025. 
Output: The “Data schemas” window is displayed with new added data schema.

[TC-02-SM-002]
---
Input: User logged in as Metadata Manager.  User leaves fields empty.
Output: The “Datasets Catalog” window is not displayed, an error message is shown indicating the mandatory field is missing, and the data schema is not added to the list.

[TC-03-SM-002]
---
Input: User logged in as Metadata Manager. User fills in the fields Theme with Exploring new ideas helps innovation grow; stay curious, stay bold, and keep learning daily. Creative minds shape the future (>100 characters) and properties - type Data with value 10.04.2025. 
Output: The “Datasets Catalog” window is not displayed, an error message Unexpected error! is shown, and the data schema is not added to the list.

[TC-04-SM-002]
---
Input: User logged in as Metadata Manager. User fills in the fields Theme with Test schema without property and leaves epmty properties.
Output: The “Datasets Catalog” window is not displayed, an error message Unexpected error! is shown, and the data schema is not added to the list.
