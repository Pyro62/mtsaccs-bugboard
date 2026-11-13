class TicketNotFound(Exception):
    """Raised by the service when a ticket ID doesn't exist."""


class InvalidProjectName(ValueError):
    """Raised by normalize_project when nothing is left after cleaning."""