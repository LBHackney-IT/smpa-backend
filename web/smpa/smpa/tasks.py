

from invoke import task


@task
def test(c, cov=False, verbose=False):
    pytest_command = 'pytest smpa/tests'
    if cov:
        pytest_command += ' --cov=api'
    if verbose:
        pytest_command += ' -s '
    c.run(pytest_command, pty=True)


@task
def runserver(c, log_level='info', port=5000):
    cmd = 'gunicorn --reload smpa.app:app -b 0.0.0.0:5000'
    c.run(cmd, pty=True)


@task
def shell(c):
    command = 'export ENVIRONMENT="common" && ./scripts/interpreter'
    c.run(command, pty=True)
