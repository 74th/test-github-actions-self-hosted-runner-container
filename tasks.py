import os

from invoke.tasks import task
from dotenv import load_dotenv

load_dotenv()

@task
def build(c):
    c.run("docker compose rm -f", warn=True)
    c.run("docker compose build")

@task
def up(c):
    c.run("docker compose up")

@task
def down(c):
    c.run("docker compose down")