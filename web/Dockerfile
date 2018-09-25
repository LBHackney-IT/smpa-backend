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

# Switch to our reqs mount
RUN mkdir -p /usr/srv/reqs/
WORKDIR /usr/srv/reqs/

# Pipenv install
COPY ./reqs/Pipfile /usr/srv/reqs/Pipfile
COPY ./reqs/Pipfile.lock /usr/srv/reqs/Pipfile.lock
RUN ls -la && whoami && pwd && cat Pipfile
RUN pip install pipenv
RUN pipenv install --system --sequential --dev

# Create our working directory
RUN mkdir -p /usr/srv/app/
WORKDIR /usr/srv/app/

# Expose the dev server
EXPOSE 5000

