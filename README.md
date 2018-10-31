# Submit my Planning Application

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8895ca51468e42448335a85cff559f92)](https://www.codacy.com/app/Hactar/smpa-backend?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LBHackney-IT/smpa-backend&amp;utm_campaign=Badge_Grade)

## Secrets management

The project uses EnvKey to manage secrets. For local development you should generate a developer key and store it in a `.env` file at the root of the project.

    ENVKEY={YOURENVKEY}

### Required Environment Variables

    POSTGRES_USER
    POSTGRES_PASSWORD
    POSTGRES_DB
    REDIS_PASSWORD

### Bring it up

Bring the whole thing up with ``docker-compose up``. If this is your first run, you'll want to ensure the extensions get created in the postgres container. Eventually we'll automate this.

    docker

    docker exec -i smpa_db_1 psql -U postgres $POSTGRES_DB -c 'CREATE EXTENSION postgis'
    docker exec -i smpa_db_1 psql -U postgres $POSTGRES_DB -c 'CREATE EXTENSION postgis_topology'
    docker exec -i smpa_db_1 psql -U postgres $POSTGRES_DB -c 'CREATE EXTENSION "uuid-ossp"'

## Python Packages

If you need to add any Python packages to the project, you should first pipenv install them into the .venv in /usr/srv/reqs so that pipenv can keep the lock file updated.

    cd /usr/srv/reqs
    pipenv install {package_name}

This ensures the package will be added next time the container is built. Once you've done this you can install it system wide with...

    pipenv install --system --sequential --dev

If the lockfile somwhow ends up outdated, you can fix this with...

    cd /usr/srv/reqs
    pipenv install

