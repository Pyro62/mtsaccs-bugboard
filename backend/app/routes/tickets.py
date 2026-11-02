# routes for tickets

from fastapi import APIRouter, Depends


router = APIRouter()

@router.get('/tickets')
def get_tickets():
    return


@router.post('/tickets')
def create_ticket():
    return

@router.patch(f'/tickets/{id}')
def patch_ticket(id: str):
    return

@router.delete(f'/tickets/{id}') # fix to require auth header
def delete_ticket(id: str):
    return