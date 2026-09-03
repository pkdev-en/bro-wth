from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import re
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/contact", response_class=HTMLResponse)
def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request, "sent": False, "errors": {}, "values": {}})


@app.post("/contact", response_class=HTMLResponse)
def contact_submit(
    request: Request,
    name: str = Form(""),
    email: str = Form(""),
    message: str = Form(""),
):
    errors = {}
    if len(name.strip()) < 2:
        errors["name"] = "Ten khong duoc duoi hai ky tu"

    if not EMAIL_REGEX.match(email.strip()):
        errors["email"] = "Email khong dung dinh dang"

    if len(message.strip()) < 10:
        errors["message"] = "Ten khong duoc duoi muoi ky tu"

    if errors:
        return templates.TemplateResponse(
            "contact.html",
         {
            "request": request,
            "sent": False,
            "errors": errors,
            "values": {
                "name": name,
                "email": email,
                "message": message,

            },
        },

    )
            
    
    print(f"Tin nhan moi tu {name} ({email}): {message}")
    return templates.TemplateResponse("contact.html", {"request": request, "sent": True, "errors": {}, "values": {}})
