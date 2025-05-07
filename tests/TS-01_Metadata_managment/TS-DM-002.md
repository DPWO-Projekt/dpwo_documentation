[TC-01-DM-002]
---
Input: User logged in as Metadata Manager. User clicks the “Add” button.
Output: The modal window with dataset definition form is displayed.

[TC-02-DM-002]
---
Input: User logged in as Metadata Manager. User clicks the “Add” button. User fills in the fields for mandatory attributes. Mandatory attributes are: theme, URI, dataset title, description, language. Example test data is specified below. All text fields are limited to max 100 characters, URI must be a valid uri. Then user clicks the “Add” button on the form.
Output: The “Datasets Catalog” window is displayed, the new dataset is visible in the list, and a success message is displayed.

[TC-03-DM-002]
---
Input: User logged in as Metadata Manager. User clicks the “Add” button. The user leaves a mandatory field empty (e.g. dataset theme) and clicks the “Add” button on the form.
Output: The “Datasets Catalog” window is not displayed, an error message is shown indicating the mandatory field is missing, and the dataset is not added to the list.

[TC-04-DM-002]
---
Input: User logged in as Metadata Manager. User clicks the “Add” button. User fills in the fields with invalid data (e.g. URI is not a valid URI like: localhost instead of http://localhost). Example invalid data is specified below. Then user clicks the “Add” button on the form.
Output: The “Datasets Catalog” window is not displayed, an error message is shown indicating the invalid data, and the dataset is not added to the list.

## Test data (valid)
**theme**: Trees
**URI**: https://warsaw-trees.com
**title**: Warsaw Trees
**description**: Trees in Warsaw.
**language**: PL

## Test data (invalid)
**theme**: Trees
**URI**: warsaw-trees
**title**: Warsaw Trees
**description**: Trees in Warsaw.
**language**: PL

## Test data (invalid)
**theme**: p.v?y&z0,5d]JL-,;G)njJ;gByzvhSJRg)eH0r4%bL?j2=WVU(L,V#ZP$VvPrKPQ!TT1T$qgp}%#9};uygv_W+Nm5tz,w9:#;XQ_7
**URI**: https://warsaw-trees.com
**title**: Warsaw Trees
**description**: Trees in Warsaw.
language: PL
