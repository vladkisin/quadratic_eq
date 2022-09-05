# Data Scrapping final project repo

## Environment Setup (once)

1. Install [Miniconda3](https://conda.io/miniconda.html)
2. Run `env_create.cmd`
3. Run `env_update.cmd`
4. Run `env_shell.cmd`


## Project goal
The goal of the project is to build a small web-app for quadratic equation solving based on entered coefficients. 
Provided the a, b, c coefficients of an equation, the app displays the roots and the parabola itself.

The tech stack used is: Python, requests, fastAPI, HTML, CSS, Jinja2


## Project code
Project code along with intermediate scrapped data are in the `src/` folder. 
To run the service with uvicorn from the root of the repo:
```cmd
cd src
conda activate quadratic_eq
uvicorn run main:app
```