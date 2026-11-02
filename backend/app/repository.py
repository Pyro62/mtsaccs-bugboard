# base repo
from typing import Protocol
from uuid import UUID
from models import Ticket
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends
from db import get_db


class TicketRepository(Protocol):
    def insert(self, data: dict) -> Ticket: ...
    def get_all(self, project: str | None, resolved: bool | None) -> list[Ticket]: ...
    def get_by_id(self, ticket_id: UUID) -> Ticket | None: ...
    def exists(self, project: str, title: str) -> bool: ...
    def set_resolved(self, ticket_id: UUID, value: bool) -> Ticket | None: ...
    def delete(self, ticket_id: UUID) -> bool: ...


class SqlAlchemyRepository:
    def __init__(self, db: Session):
        self.db = db

    def insert(self, data: dict) -> Ticket:
        ticket = Ticket(**data)
        self.db.add(ticket)
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
    
    def get_all(self, project: str | None, resolved: bool | None) -> list[Ticket]:
        data = select(Ticket).order_by(Ticket.created_at.desc())
        if project:
            data = data.where(Ticket.project == project)
        if resolved is not None:
            data = data.where(Ticket.is_resolved == resolved)
        return list(self.db.scalars(data).all())
    
    def get_by_id(self, ticket_id: UUID) -> Ticket | None:
        return self.db.get(Ticket,ticket_id)
           
    
    def set_resolved(self, ticket_id: UUID, value: bool) -> Ticket | None:
        ticket = self.get_by_id(ticket_id)
        if not ticket:
            return None
        ticket.is_resolved = value
        self.db.commit()
        self.db.refresh(ticket)
        return ticket
    
    def delete(self, ticket_id: UUID) -> bool:
        ticket = self.get_by_id(ticket_id)
        if not ticket:
            return False
        self.db.delete(ticket)
        self.db.commit()
        return True


def get_repo(db: Session = Depends(get_db)) -> TicketRepository:
    return SqlAlchemyRepository(db)
