"""
payze error catcher decorator.
"""
import logging

from functools import wraps

from apps.utility.exceptions import ServiceAPIException

logger = logging.getLogger(__name__)


def error_catcher(func):
    """
    the error catcher decorator.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            msg = f"{func.__name__} error: {exc}"
            logger.error(f"{func.__name__} error: %s", exc)
            raise ServiceAPIException(
                type="500",
                message=msg,
                status_code=500
            ) from exc

    return wrapper
