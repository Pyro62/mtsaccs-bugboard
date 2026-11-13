# routes for tickets
from uuid import UUID
from fastapi import APIRouter, Depends

from repository import TicketRepository, get_repo
from schemas import TicketCreate, TicketOut, TicketPatch
from services.ticket_service import TicketService

router = APIRouter(prefix="/tickets", tags=["tickets"])


def get_service(repo: TicketRepository = Depends(get_repo)) -> TicketService:
    return TicketService(repo)


@router.get("", response_model=list[TicketOut])
def get_tickets(project: str | None = None, resolved: bool | None = None,
                service: TicketService = Depends(get_service)):
    return service.list_tickets(project, resolved)


@router.post("", response_model=TicketOut, status_code=201)
def create_ticket(data: TicketCreate, service: TicketService = Depends(get_service)):
    return service.create_ticket(data)


@router.patch("/{ticket_id}", response_model=TicketOut)
def patch_ticket(ticket_id: UUID, data: TicketPatch,
                 service: TicketService = Depends(get_service)):
    return service.set_resolved(ticket_id, data.is_resolved)


@router.delete("/{ticket_id}", status_code=204)
def delete_ticket(ticket_id: UUID, service: TicketService = Depends(get_service)):
    service.delete_ticket(ticket_id)