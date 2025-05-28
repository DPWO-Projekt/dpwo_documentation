[UC-DU-004] Download dataset
---

[pre] User is logged-in as Data User<br>
[pre] Invoked by UC-DU-014 Show catalog as a data user

1. User selects a dataset from the catalog view.
2. System displays a list of available dataset distributions (e.g., CSV, JSON, XLS).
3. User clicks the "Download" button next to the chosen distribution.
4. System verifies the availability of the selected distribution.

[Distribution is available]<br>
    4a. System initiates the download process.<br>
    5a. The file is downloaded to the user’s local system.<br>
    6a. System displays a success message: "Download completed successfully."<br>

[No distribution available]<br>
    4b. System displays an error message: "No downloadable file available for this dataset."

[Download fails (e.g. network/server error)]<br>
    5b. System displays an error message: "Download failed due to a system error. Please try again later."<br>
    6b. User may attempt to retry the download (return to Step 2).