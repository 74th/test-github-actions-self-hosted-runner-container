import os

from invoke.tasks import task
from dotenv import load_dotenv

load_dotenv()

@task
def build(c):
    c.run("docker compose build")

@task
def run(c):
    access_token = os.environ["GITHUB_ACCESS_TOKEN"]
    c.run(f"docker compose run -i --rm --env 'ACCESS_TOKEN={access_token}' app")