[TC-01-DM-003]
---
Input: User logged in as Metadata Manager. User clicks the “Edit” button on an existing dataset.
Output: The modal window with dataset definition form is displayed, pre-filled with the current values of the selected dataset.

[TC-02-DM-003]
---
Input: User logged in as Metadata Manager. User clicks the “Edit” button on an existing dataset. User changes values in the fields for mandatory attributes. Mandatory attributes are: theme, URI, dataset title, description, language. All text fields are limited to max 100 characters, URI must be a valid uri. Example valid data is specified below. Then user clicks the “Save” button on the form.
Output: The “Datasets Catalog” window is displayed, the edited dataset is updated in the list, and a success message is displayed.

[TC-03-DM-003]
---
Input: User logged in as Metadata Manager. User clicks the “Edit” button on an existing dataset. User leaves a mandatory field empty (e.g. dataset theme) and clicks the “Save” button on the form.
Output: The “Datasets Catalog” window is not displayed, an error message is shown indicating the mandatory field is missing, and the dataset is not updated in the list.

[TC-04-DM-003]
---
Input: User logged in as Metadata Manager. User clicks the “Edit” button on an existing dataset. User changes values in the fields with invalid data (e.g. URI is not a valid URI like: localhost instead of http://localhost). Example invalid data is specified below. Then user clicks the “Save” button on the form.
Output: The “Datasets Catalog” window is not displayed, an error message is shown indicating the invalid data, and the dataset is not updated in the list.

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
**language**: PL
