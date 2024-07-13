from invoke.tasks import task

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

@task
def deploy(c):
    c.run("kubectl apply -k manifests")

@task
def remove(c):
    c.run("kubectl delete -k manifests")