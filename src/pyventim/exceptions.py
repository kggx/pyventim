"""Custom Exception Classes for the wrapper"""


class RestException(Exception):
    """Raised if the Rest Adatper returns an error."""


class HtmlException(Exception):
    """Raised if the Component Adatper returns an error."""
