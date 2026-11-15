"""Timestamped debug logging for diagnosing hotkey/clipboard issues.

Writes to both the console (if any) and a persistent log file at
%APPDATA%\\ZTranslate\\debug.log, so behavior can be captured
even when running as a windowed exe with no visible console, and so
a single problematic run can be inspected after the fact rather than
relying on what scrolled past on screen.

The log file is truncated at the start of each app run (old logs
aren't useful once you're chasing a fresh repro) but everything
written during THIS run stays on disk even if the console output
gets lost or truncated.
"""
import os
import time

from . import config as cfg_module

LOG_PATH = os.path.join(cfg_module.APPDATA_DIR, "debug.log")

_log_file = None


def init_log():
    """Call once at startup. Truncates any previous log."""
    global _log_file
    cfg_module.ensure_appdata_dir()
    try:
        _log_file = open(LOG_PATH, "w", encoding="utf-8")
        log(f"=== ZTranslate debug log started, writing to {LOG_PATH} ===")
    except Exception as e:
        print(f"Could not open debug log file: {e}")
        _log_file = None


def log(msg):
    """Prints AND writes a timestamped line, flushing immediately so
    nothing is lost if the process is killed mid-run."""
    line = f"[{time.strftime('%H:%M:%S')}.{int(time.time() * 1000) % 1000:03d}] {msg}"
    print(line)
    if _log_file is not None:
        try:
            _log_file.write(line + "\n")
            _log_file.flush()
        except Exception:
            pass
