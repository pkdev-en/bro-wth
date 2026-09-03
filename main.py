from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/comtact", response_class=HTMLResponse)
def contact_page(request: Request):
  return templates.TemplateResponse("contact.html", {request, "sent": False})

@app.post("/contact", response_class=HTMLResponse)
def contact_submit(
  request: Request,
  name: str = Form(...),
  email: str = Form(...)
  message: str = Form(...),
):
  print(f"Tin nhan moi tu {name} ({email}): {message}")
  return templates.TemplateResponse("contact.html", {request, "sent": True})

# project nho :) 
# 15:58 gmt +7 3/9/2026 
