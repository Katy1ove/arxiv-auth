"""Authn/z-related exceptions raised by components in this module."""


class InvalidToken(ValueError):
    """Token in request is not valid."""


class MissingToken(ValueError):
    """No token found in request."""


class ConfigurationError(RuntimeError):
    """The application is not configured correctly."""


class SessionCreationFailed(RuntimeError):
    """Failed to create a session in the session store."""


class SessionDeletionFailed(RuntimeError):
    """Failed to delete a session in the session store."""


class SessionUnknown(RuntimeError):
    """Failed to locate a session in the session store."""


class SessionExpired(RuntimeError):
    """User's session has expired."""