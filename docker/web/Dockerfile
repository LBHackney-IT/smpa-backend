FROM quay.io/hactar/python-base:latest AS builder


####################################################################################################
# ENVKEY STUFF
####################################################################################################

# Ensure docker-compose build web is able to pass these env vars in
ARG ENVKEY
ARG SERVER_ENV

# Run envkey-source to get the env vars into the container
RUN eval $(envkey-source)


####################################################################################################
# PROJECT STUFF
####################################################################################################
RUN addgroup -S smpagroup
RUN adduser -S -D -h /usr/app/src smpa smpagroup


ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1
ENV LANG en_GB.utf8

# Create our working directory
RUN mkdir -p /usr/srv/app/

# Poetry install
WORKDIR /usr/srv/app/
COPY ./config.toml /usr/srv/app/config.toml
COPY ./pyproject.toml /usr/srv/app/pyproject.toml
COPY ./poetry.lock /usr/srv/app/poetry.lock
RUN source $HOME/.poetry/env && \
    poetry install

RUN echo -e "\nalias dev='gunicorn --reload smpa.app -b 0.0.0.0:5000 -t 99999999'\n" >> ~/.zshrc
RUN echo -e "\nalias dev='gunicorn --reload smpa.app -b 0.0.0.0:5000 -t 99999999'\nfunction fish_greeting\n\techo \"🐟 use \`dev\` to run the server\"\n\t echo ""\nend" >> ~/.config/fish/config.fish


# COPY ./rds-combined-ca-bundle.pem /usr/srv/rds-combined-ca-bundle.pem
RUN apk add --update --no-cache ca-certificates openssl \
    && mkdir -p /usr/local/share/ca-certificates/ \
    && curl "https://s3.amazonaws.com/rds-downloads/rds-ca-2019-root.pem" --output /tmp/rds-ca-2019-root.pem \
    && curl "https://s3.amazonaws.com/rds-downloads/rds-ca-2019-eu-west-2.pem" --output /tmp/rds-ca-2019-eu-west-2.pem \
    && curl "https://s3.amazonaws.com/rds-downloads/rds-combined-ca-bundle.pem" --output /tmp/rds-combined-ca-bundle.pem \
    && openssl x509 -in /tmp/rds-ca-2019-root.pem -inform PEM -out /usr/local/share/ca-certificates/rds-ca-2019-root.crt \
    && openssl x509 -in /tmp/rds-ca-2019-eu-west-2.pem -inform PEM -out /usr/local/share/ca-certificates/rds-ca-2019-eu-west-2.crt \
    && openssl x509 -in /tmp/rds-combined-ca-bundle.pem -inform PEM -out /usr/local/share/ca-certificates/rds-combined-ca-bundle.crt \
    && update-ca-certificates


ENV SHELL /bin/zsh

RUN apk add --update --no-cache openssh

# Expose the dev server
EXPOSE 5000

