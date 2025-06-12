import argparse
import os
from datetime import datetime

TEST_CASE_DIR = "./tests"
TEST_LOG_DIR = "./test_logs"
USE_CASE_DIR = "./use_cases"

ACCEPTANCE_TEST_TEMPLATE = """[{test_name}] {title}
---
[pre] <br>

**Input**: <br>
**Output**: 

[post] <br>

"""

TEST_LOG_TEMPLATE = """[[{test_name}](../../tests/{test_subdir}/{test_filename}#{test_name}{test_ref})] Test log {date}
---
✅ Passed<br>
**Step 2**: ❌ Recieved unwanted output

"""


def create_or_append_file(file_path, content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)


def main():
    parser = argparse.ArgumentParser(description="Generate test case and log files.")
    parser.add_argument(
        "-uc", "--use-case", required=True, help="Use case identifier (e.g., DM)"
    )
    parser.add_argument(
        "-un", "--use-case-number", required=True, type=int, help="Use case number"
    )
    parser.add_argument(
        "-tc", "--test-case", action="store_true", help="Generate test case"
    )
    parser.add_argument(
        "-tn", "--test-case-number", required=True, type=int, help="Test case number"
    )
    parser.add_argument(
        "-tl", "--test-log", action="store_true", help="Generate test log file"
    )
    parser.add_argument(
        "-p", "--positive", type=bool, help="Set test type", default=None
    )

    args = parser.parse_args()

    if args.use_case == "DM":
        use_case_subdir = "01_Metadata_managment"
    elif args.use_case == "SM":
        use_case_subdir = "02_Schema_managment"
    elif args.use_case == "DS":
        use_case_subdir = "03_Data_acquisition_and_management"
    elif args.use_case == "DU":
        use_case_subdir = "04_Data_usage"
    elif args.use_case == "AA":
        use_case_subdir = "05_Automation_and_administration"
    elif args.use_case == "TS":
        use_case_subdir = "06_Authentication"
    # File names
    test_case_file = f"{TEST_CASE_DIR}/TS-{use_case_subdir}/TS-{args.use_case}-{args.use_case_number:03}.md"
    test_log_file = f"{TEST_LOG_DIR}/TL-{use_case_subdir}/TL-{args.use_case_number:02}-{args.use_case}-{args.use_case_number:03}.md"

    # Generate and append acceptance test case
    test_name = (
        f"TC-{args.test_case_number:02}-{args.use_case}-{args.use_case_number:03}"
    )
    if args.test_case:
        title = (
            ""
            if args.positive is None
            else "Positive test" if args.positive else "Negative test"
        )
        test_case_content = ACCEPTANCE_TEST_TEMPLATE.format(
            test_name=test_name,
            title=title,
        )
        create_or_append_file(test_case_file, test_case_content)

    # Generate test log if requested
    if args.test_log:
        date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        test_filename = f"TS-{args.use_case}-{args.use_case_number:03}"
        test_ref = (
            ""
            if args.positive is None
            else "-positive-test" if args.positive else "-negative-test"
        )
        test_log_content = TEST_LOG_TEMPLATE.format(
            test_name=test_name,
            test_subdir=f"TS-{use_case_subdir}",
            test_filename=test_filename,
            test_ref=test_ref,
            date=date,
        )
        create_or_append_file(test_log_file, test_log_content)


if __name__ == "__main__":
    main()
