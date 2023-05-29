# for each screen TRY and find the following and just add it automatically.
# 1. code
# 2. description
# 3. permissions
#
# Check dictionary for screen name and if that screen is in the dictionary, execute further intent.
#

check_crud_screen_dictionary = {
    "Work Order": {
        "(#ts-1 [data-id='work'])textarea#lbl-workRequired": "work was required"
    }
}