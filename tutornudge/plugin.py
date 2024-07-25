"""
Tutor plugin to send nudge emails.
"""
from glob import glob
import os
import importlib_resources

from tutor import hooks

from .__about__ import __version__


# Configuration
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        ("NUDGE_VERSION", __version__),
        ("NUDGE_SCHEDULE", "0 10 * * *"),
        ("NUDGE_SEND_COURSE_UPDATE", True),
        ("NUDGE_SEND_RECURRING_NUDGE", True),
    ]
)


# Load patches from files
for path in glob(str(importlib_resources.files("tutornudge") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
