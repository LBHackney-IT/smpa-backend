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
    poetry self:update && \
    poetry install

RUN echo -e "\nalias dev='gunicorn --reload smpa.app -b 0.0.0.0:5000 -t 99999999'\n" >> ~/.zshrc
RUN echo -e "\nalias dev='gunicorn --reload smpa.app -b 0.0.0.0:5000 -t 99999999'\nfunction fish_greeting\n\techo \"🐟 use \`dev\` to run the server\"\n\t echo ""\nend" >> ~/.config/fish/config.fish



ENV SHELL /bin/zsh

# Expose the dev server
EXPOSE 5000

