from db.base import get_db
from db.models.todos import Todos
#from view.home.schemas import Todo

from fastapi import APIRouter, Request, Depends, Form, status
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from sqlalchemy.orm import Session

home_route = APIRouter(prefix="/home")

template = Jinja2Templates(directory="templates/homepage")

@home_route.get("/", response_class=HTMLResponse)
async def read_home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(Todos).all()
    return template.TemplateResponse(
        name="home.html",
        context= {
            "request": request,
            "todo_list": todos,
        }
    )

@home_route.post("/add")
def add(request: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = Todos(title=title)
    db.add(new_todo)
    db.commit()
 
    url = app.url_path_for("home")
    return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)