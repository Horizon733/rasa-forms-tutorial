import yaml
from typing import Text

from database_utils.constants import DB_USER_COLUMN, USER_PROFILE_COLUMN_OTP, DB_FILE

with open(DB_FILE, "r") as dbf:
    DATABASE = yaml.safe_load(dbf)


def is_valid_user(useremail: Text) -> bool:
    global DATABASE
    is_valid_user = False
    if useremail in DATABASE[DB_USER_COLUMN]:
        is_valid_user = True
    return is_valid_user


def is_valid_otp(otp: float, useremail: Text) -> bool:
    global DATABASE
    valid_otp = False
    if useremail in DATABASE[DB_USER_COLUMN]:
        if otp == DATABASE[DB_USER_COLUMN][useremail][USER_PROFILE_COLUMN_OTP]:
            valid_otp = True
    return valid_otp