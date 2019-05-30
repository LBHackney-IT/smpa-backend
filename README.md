# Submit my Planning Application

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8895ca51468e42448335a85cff559f92)](https://www.codacy.com/app/Hactar/smpa-backend?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LBHackney-IT/smpa-backend&amp;utm_campaign=Badge_Grade)

## Secrets management

The project uses EnvKey to manage secrets. For local development you should generate a developer key and store it in a `.env` file at the root of the project.

    ENVKEY={YOURENVKEY}

@TODO: Support other methods of environment injection

### Required Environment Variables

    SECRET_KEY
    RDB_PORT
    RDB_HOST
    RDB_DB
    RDB_PASSWORD
    REDIS_PASSWORD

### Bring it up

Bring the whole thing up with ``docker-compose up``

## Python Packages

If you need to add any Python packages to the project, you should first pipenv install them into the .venv in /usr/srv/app/.venv so that pipenv can keep the lock file updated.

    pipenv install {package_name}

This ensures the package will be added next time the container is built. Once you've done this you can install it system wide with...

    pipenv install --system --sequential --dev

If the lockfile somwhow ends up outdated, you can fix this with...

    cd /usr/srv/app
    pipenv install

