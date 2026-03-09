import logging
import os

import filelock

_logger = logging.getLogger(__name__)

if __name__ == "__main__":
    lock_file = "test.lock"
    lock = filelock.FileLock(lock_file)

    with lock:
        _logger.info("Lock acquired")

    _logger.info("Lock released")

    # Raise an error is the lock file is still present
    if os.path.exists(lock_file):
        raise RuntimeError("Lock file still exists")
