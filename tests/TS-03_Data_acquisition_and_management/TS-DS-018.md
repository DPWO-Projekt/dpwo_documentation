[TS-01-DS-018] Successfully attach dataset distribution
---

[pre] User is logged-in as Data Supplier ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))
[pre] The user is on the dataset list page (triggered by "Show owned dataset list" [UC-DS-014](../../use_cases/03_Data_acquisition_and_managment/UC-DS-014.md))
[pre] A dataset exists and can be selected for modification.

**Input**: User navigates to "Attach distribution" button as described in [UC-DS-014](../../use_cases/03_Data_acquisition_and_managment/UC-DS-014.md).
**Output**: System displays a "Attach distribution to dataset" form.

**Input**: User fills out fields using example data:
 - **Access URL**: https://some-url.com<br>
 - **Avalibility**: Very high<br>
 - **Format**: CSV <br>
 - **Distribution Title**: Some Title<br>
 - **Description**: Some description<br>

**Input** User clicks "Create dataset distribution" button.
**Output** User is redircted towards owned dataset list view defined in [UC-DS-014](../../use_cases/03_Data_acquisition_and_managment/UC-DS-014.md) and confirmation pop-up is shown. New dataset distribution is attached to related dataset.

[TS-02-DS-018] Try to attach dataset distribution with invalid data
 
[pre] User is logged-in as Data Supplier ([UC-TS-002](../../use_cases/06_Authentication/UC-TS-002.md))
[pre] The user is on the dataset list page (triggered by UC-DS-014 Show owned dataset list [UC-DS-014](../../use_cases/03_Data_acquisition_and_managment/UC-DS-014.md))
[pre] A dataset exists and can be selected for modification.

**Input**: User navigates to "Attach distribution" button as described in [UC-DS-014](../../use_cases/03_Data_acquisition_and_managment/UC-DS-014.md).
**Output**: System displays a "Attach distribution to dataset" form.

**Input**: User fills out fields using example data:
 - **Access URL**: https://some-wrong-url.com<br>
 - **Avalibility**: Very high<br>
 - **Format**: CSV <br>
 - **Distribution Title**: Some Title<br>
 - **Description**: Some description<br>

 **Input** User clicks "Create dataset distribution" button.

 **Output**: System displays form "Attach distribution to dataset" window with validation errors highlighted.
