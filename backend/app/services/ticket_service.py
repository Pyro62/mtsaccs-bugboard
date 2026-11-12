# service class for tickets!
from repository import TicketRepository
from normalize_service import normalize_project
from models import Ticket
from schemas import TicketCreate
from uuid import UUID


class TicketService:
    def __init__(self, repo: TicketRepository):
        self.repo = repo

    def create_ticket(self, data: TicketCreate) -> Ticket:
        return

    def list_tickets(self, project: str | None, resolved: bool | None) -> list[Ticket]:

        return
    
    def set_resolved(self, ticket_id: UUID, value: bool)-> Ticket:
        return

    def delete_ticket(self, ticket_id: UUID) -> None:
        return
    