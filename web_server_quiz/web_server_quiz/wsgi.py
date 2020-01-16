from web import create_app
from models import BaseModel

BaseModel.recreate_tables()

app = create_app()

if __name__ == "__main__":
    app.run()
