# Test Plan 03 - dataset distributions

## Test plan steps:

### 1. [UC-TS-002](/tests/TS-06_Authentication/TS-TS-002.md) Login [as Metadata Manager]
### 2. [TS-01-DM-002](/tests/TS-01_Metadata_managment/TS-DM-002.md) Successfully add dataset
### 3. [NON-EXISTING UC] Logout [can be done by clearing localStorage]
### 4. [UC-TS-002](/tests/TS-06_Authentication/TS-TS-002.md) Login [as Data User]
### 5. [UC-DU-014](/tests/TS-04_Data_usage/TS-DU-014.md) Show catalog as a data user
### 6. [UC-DU-004](/tests/TS-04_Data_usage/TS-DU-004.md) Download dataset [choose just created dataset -> no distribution available]
### 7. [NON-EXISTING UC] Logout [can be done by clearing localStorage]
### 8. [UC-TS-002](/tests/TS-06_Authentication/TS-TS-002.md) Login [as Data Supplier]
### 9. [UC-DS-014](/tests/TS-03_Data_acquisition_and_management/TS-DS-014.md) Show owned dataset list
### 10. [UC-DS-018](/tests/TS-03_Data_acquisition_and_managment/TS-DS-018.md) Upload dataset distribution [choose just created dataset]
### 11. [NON-EXISTING UC] Logout [can be done by clearing localStorage]
### 12. [UC-TS-002](/tests/TS-06_Authentication/TS-TS-002.md) Login [as Data User]
### 13. [UC-DU-014](/tests/TS-04_Data_usage/TS-DU-014.md) Show catalog as a data user
### 14. [UC-DU-004](/tests/TS-04_Data_usage/TS-DU-004.md) Download dataset [choose just created dataset -> success]
