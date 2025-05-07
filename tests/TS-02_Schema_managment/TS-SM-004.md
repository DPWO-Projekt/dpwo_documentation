[TC-01-SM-004]
---
**Input**: User logged in as Metadata Manager. User choses data schema Test schema. While editing user fills in the fields Theme with Test schema editing and properties - type Data with value 10.04.2025.<br>
**Output**: The “Data schemas” window is displayed with updated data schema.

[TC-02-SM-004]
---
**Input**: User logged in as Metadata Manager. User choses data schema Test schema editing. While editing properties user changes type Data with value 10.04.2025 to type Link with value https://isod.ee.pw.edu.pl/isod-stud/.<br>
**Output**: The “Data schemas” window is displayed with updated data schema.

[TC-03-SM-004]
---
**Input**: User logged in as Metadata Manager. User choses data schema Test schema editing. User leaves fields empty.<br>
**Output**: The “Data schemas” window is not displayed, an error message is shown indicating the mandatory field is missing, and the data schema is not updated.

[TC-04-SM-004]
---
**Input**: User logged in as Metadata Manager. User choses data schema Test schema editing. While editing user fills in the fields Theme with Exploring new ideas helps innovation grow; stay curious, stay bold, and keep learning daily. Creative minds shape the future (>100 characters) and properties - type Data with value 10.04.2025.<br>
**Output**: The “Data schemas” window is not displayed, an error message Unexpected error! is shown, and the data schema is not updated.

[TC-05-SM-004]
---
**Input**: User logged in as Metadata Manager. User choses data schema Test schema editing. While editing user fills in the fields Theme with Test schema without property and leaves epmty properties.<br>
**Output**: The “Data schemas” window is not displayed, an error message Unexpected error! is shown, and the data schema is not updated.