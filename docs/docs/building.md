# Building docker images for remote execution

There are separate Dockerfiles for remote servers that don't rely on other compose services.

    docker build -t smpa:staging -f docker/web/Dockerfile.staging .
    docker build -t smpa:production -f docker/web/Dockerfile.production .

Run these like so...

    docker run --env SERVER_ENV=staging --name=smpa_staging -i -t smpa:staging
