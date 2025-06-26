from main import app
from models import db

@app.cli.command('db_init')
def db_init():
    """Initialize the database."""
    db.create_all()
    print('Database initialized.') 