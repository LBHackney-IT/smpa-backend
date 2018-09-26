# Setup

## Secrets management

The project uses EnvKey to manage secrets. For local development you should generate a developer key and store it in a `.env` file at the root of the project.

    ENVKEY={YOURENVKEY}

### Required Environment Variables

    POSTGRES_USER
    POSTGRES_PASSWORD
    POSTGRES_DB
    POSTGRES_HOST
    REDIS_PASSWORD

## Bring it up

Bring the whole thing up with ``docker-compose up``. If this is your first run, you'll want to ensure the extensions get created in the postgres container. Eventually we'll automate this.

    docker exec -i smpa_db_1 psql -U postgres $POSTGRES_DB -c 'CREATE EXTENSION postgis'
    docker exec -i smpa_db_1 psql -U postgres $POSTGRES_DB -c 'CREATE EXTENSION postgis_topology'
    docker exec -i smpa_db_1 psql -U postgres $POSTGRES_DB -c 'CREATE EXTENSION "uuid-ossp"'


## Shell access

If you have the Hactar fabfile library you can bring up a shell inside the application container with `fab docker.shell`

If not, run `docker exec -it smpa_web_1 zsh`

To access psql in the postgres container run `docker exec -it smpa_db_1 psql`

