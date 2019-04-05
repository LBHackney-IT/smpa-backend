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

ENV PYTHONUNBUFFERED 1
ENV PIPENV_VENV_IN_PROJECT 1
ENV LANG en_GB.utf8

# Create our working directory
RUN mkdir -p /usr/srv/app/
WORKDIR /usr/srv/app/

# Pipenv install
COPY ./smpa/Pipfile /usr/srv/app/Pipfile
COPY ./smpa/Pipfile.lock /usr/srv/app/Pipfile.lock
RUN ls -la && whoami && pwd && cat Pipfile
RUN pip install pipenv
RUN pipenv install --system --sequential --dev

RUN echo "\nalias dev='gunicorn --reload smpa.app -b 0.0.0.0:5000 -t 99999999'" >> ~/.zshrc

# Expose the dev server
EXPOSE 5000

