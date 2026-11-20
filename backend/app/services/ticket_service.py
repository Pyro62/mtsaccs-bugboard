# service class for tickets!
from uuid import UUID

from errors import TicketNotFound  # raise this when a ticket ID doesn't exist
from models import Ticket
from services.normalize_service import normalize_project
from repository import TicketRepository
from schemas import TicketCreate


class TicketService:
    """
    The service holds the business logic. It decides WHAT should happen;
    the repository only knows HOW to read and write the database.

    Rules for this file:
      - Talk to the database only through self.repo (no SQLAlchemy here).
      - No FastAPI imports. Raise our own errors and let main.py turn them
        into HTTP responses.
    """

    def __init__(self, repo: TicketRepository):
        self.repo = repo

    def create_ticket(self, data: TicketCreate) -> Ticket:
        """
        Save a new ticket and return it.

        Input:   a TicketCreate (project, title, description, author, flair)
        Returns: the saved Ticket, including its new id and created_at

        Hints:
          - self.repo.insert() takes a plain dict, not a Pydantic model.
            Pydantic models have a method that converts them to a dict.
          - Project names must be normalized BEFORE they are saved.
          - Think about which value in the dict you need to replace.
        """
        ticket_data = data.model_dump()
        ticket_data["project"] = normalize_project(ticket_data["project"])

        return self.repo.insert(ticket_data)

    def list_tickets(self, project: str | None, resolved: bool | None) -> list[Ticket]:
        """
        Return tickets, optionally filtered.

        Input:   project  - filter by project name, or None for all projects
                 resolved - True / False to filter by status, or None for both
        Returns: a list of Tickets (an empty list if nothing matches)

        Hints:
          - Stored project names are already normalized, e.g. "cloud-nine".
            What should a filter of "Cloud Nine" be turned into before
            you look it up?
          - Only normalize when a project was actually given. What does
            normalize_project do with None?
          - self.repo.get_all() already handles the None cases, so you can
            pass the values straight through.
        """
        if project is not None:
            project = normalize_project(project)

        return self.repo.get_all(project, resolved)

    def set_resolved(self, ticket_id: UUID, value: bool) -> Ticket:
        """
        Mark a ticket resolved (True) or reopen it (False).

        Input:   ticket_id - the ticket's UUID
                 value     - True to resolve, False to reopen
        Returns: the updated Ticket
        Raises:  TicketNotFound if no ticket has that id

        Hints:
          - Look at what self.repo.set_resolved() returns when the id
            doesn't exist. How can you detect that case?
          - The repository returns None for "not found". Turning that into
            an error is YOUR job, not the repository's.
        """
        ticket = self.repo.set_resolved(ticket_id, value)

        if ticket is None:
            raise TicketNotFound()
        
        return ticket

    def delete_ticket(self, ticket_id: UUID) -> None:
        """
        Delete a ticket.

        Input:   ticket_id - the ticket's UUID
        Returns: nothing (the route replies 204 No Content)
        Raises:  TicketNotFound if no ticket has that id

        Hints:
          - Check what self.repo.delete() returns. It reports whether
            anything was deleted.
          - Same pattern as set_resolved: detect "not found", then raise.
        """
        deleted = self.repo.delete(ticket_id)

        if not deleted:
            raise TicketNotFound()