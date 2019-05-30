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

### Shells

There's a choice of sh, zsh, and fish for the shells inside the container. You should be able to use any of these by running, for example:

    docker exec -it smpa_web_1 fish

We recommend fish as the best shell.

### Run the dev server

There's a gunicorn dev server that should run just by running `dev` at the prompt. This is an alias in both zsh and fish that expands to `gunicorn --reload smpa.app -b 0.0.0.0:5000 -t 99999999`

The initial startup will show a progress bar while it creates tables in the database. After that it should be running on `0.0.0.0:5000`

### Python Packages

Python dependencies are now managed via Poetry. To add a single package, inside the container run...

    poetry add {package_name}

To add a package with optional extra installs, you can use the -E flag.

    postry add passlib -E bcrypt
