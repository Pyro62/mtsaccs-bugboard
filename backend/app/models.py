import uuid
from datetime import datetime
from sqlalchemy import String, DateTime, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from db import Base
from schemas import FlairEnum

class Ticket(Base):
    __tablename__ = 'tickets'
    
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    project: Mapped[str] = mapped_column(String, nullable=False)  
    title: Mapped[str] = mapped_column(String, nullable=False)   
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    author: Mapped[str] = mapped_column(String, nullable=False)
    is_resolved: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    
    flair: Mapped[FlairEnum] = mapped_column(Enum(FlairEnum), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())