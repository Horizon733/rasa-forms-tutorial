import os
from pathlib import Path

this_path = Path(os.path.realpath(__file__))
DB_FILE = str(this_path.parent / "database.yml")

#slot names
REQUESTED_SLOT = "requested_slot"
EMAIL = "email"
OTP = "otp"


# db columns
USER_PROFILE_COLUMN_EMAIL = "user_email"
DB_USER_COLUMN = "users"
USER_PROFILE_COLUMN_OTP = "user_otp"

