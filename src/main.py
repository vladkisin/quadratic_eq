import io
import base64
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

import numpy as np
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from utils import get_roots


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request, message=' Numbers'):
    return templates.TemplateResponse(
        'index.html',  
        {
            'request': request,
            'message': message
        }
    )


@app.get("/solve")
async def solve(request: Request, a: int, b: int, c: int):
    solution = get_roots(a, b, c)
    return {'roots': solution}


@app.post('/draw')
async def draw(request: Request, 
               a: int = Form(...),
               b: int = Form(...),
               c: int = Form(...)):
    numbers = [a, b, c]
    roots = get_roots(a, b, c)
    fig, ax = plt.subplots()
    if len(roots) > 0:
        max_root, min_root = max(roots), min(roots)
        grid = np.linspace(min_root - 5, max_root + 5, num=1000)
        ax.plot(min_root, 0, 'ro', color='coral', lw=4, label=f'x={min_root}')
    if len(roots) > 1:
        ax.plot(max_root, 0, 'ro', color='blue', lw=4, label=f'x={max_root}')
    if len(roots) == 0:
        grid = np.linspace(-5, 5, num=1000)
        ax.text(-1, 10*(a / (abs(a)+0.5)) + c, 'No Roots')
    ax.plot(grid, a*grid**2 + b*grid + c, color='lightgreen', lw=2, label='Parabola')
    ax.plot(grid, np.zeros(1000), '--', color='black', lw=1, label='Zero-line')
    ax.legend()
    png_like = io.BytesIO()
    fig.savefig(png_like)
    ascii_image = base64.b64encode(png_like.getvalue()).decode('ascii')
    return templates.TemplateResponse(
        "plot.html",
        {
            'request': request, 
            'numbers': numbers,
            'picture': ascii_image
        }
    )