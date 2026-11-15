"""Entry point for ZTranslate. This is what build.ps1 points
PyInstaller at to produce the single portable exe."""
from ztranslate.main import main
import os
import sys


def _remove_pre_rename_files():
    """Delete what a build from before the rename left in this folder when
    a new build was copied over it. Built copies only, these exact files
    only, quietly; data is never touched."""
    if not getattr(sys, "frozen", False):
        return
    root = os.path.dirname(os.path.abspath(sys.executable))
    path = os.path.join(root, "Access-Translate.exe")  # pre-rename name
    try:
        if os.path.isfile(path):
            os.remove(path)
    except OSError:
        pass


if __name__ == "__main__":
    _remove_pre_rename_files()
    main()
