# Building docker images for remote execution

There are separate Dockerfiles for remote servers that don't rely on other compose services.

    docker build -t smpa:staging -f docker/web/Dockerfile.staging .
    docker build -t smpa:production -f docker/web/Dockerfile.production .

Run these like so...

    docker run --env SERVER_ENV=staging --name=smpa_staging -i -t smpa:staging


## Deploying

To deploy a freshly built image / container to Hackney infrastructure, first log into AWS.

With fish shell:

    eval (aws ecr get-login --no-include-email --region eu-west-2)

With Bash / Zsh etc:

    eval $(aws ecr get-login --no-include-email --region eu-west-2)

Build:

    docker-compose -f docker-compose.prod.yml up --build -d
    docker-compose down

Tag:

    docker tag {IMAGE_ID} 775052747630.dkr.ecr.eu-west-2.amazonaws.com/hackney/apps/submit-my-plan-api

Push:

    docker push 775052747630.dkr.ecr.eu-west-2.amazonaws.com/hackney/apps/submit-my-plan-api

