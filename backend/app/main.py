from fastapi import FastAPI
import routes.tickets as tickets



app = FastAPI()

app.include_router(tickets.router)

@app.get('/health')
def health():
    return {'Hello World!'}

@app.get('/')
def root():
    return 'World Hello?'

