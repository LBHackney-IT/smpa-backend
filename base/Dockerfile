FROM frolvlad/alpine-python3

ENV VERSION 1.7.3

RUN apk update && apk add --no-cache \
    python3-dev \
    automake \
    bash \
    cairo \
    curl \
    freetype-dev \
    gettext \
    gcc \
    g++ \
    git \
    glib \
    jpeg-dev \
    libc-dev \
    libffi-dev \
    libpng-dev \
    libsass \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    make \
    nano \
    openssh \
    pango \
    postgresql-dev \
    zlib-dev \
    nodejs \
    zsh && \
    rm -f /tmp/* /etc/apk/cache/*

RUN apk add closure-compiler --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted


RUN mkdir -p /src/app
WORKDIR /src/app

# Install babel?
RUN npm install --global babel-cli && \
    npm install --global babel-preset-es2015 \
    uglify-js \
    wait-for

# Install libsass
RUN pip install \
    libsass \
    closure

ENV SHELL /bin/zsh

# Install oh-my-zsh and set zsh as the default shell
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

COPY conf/zshrc /tmp/.zshrc
COPY conf/hactar.zsh-theme /tmp/hactar.zsh-theme
COPY conf/zsh-auto-suggest.cfg /tmp/config.zsh

RUN ls -la /tmp && \
    mv /tmp/.zshrc ~/.zshrc && \
    mv /tmp/hactar.zsh-theme ~/.oh-my-zsh/themes/hactar.zsh-theme && \
    mv /tmp/config.zsh ~/.oh-my-zsh/custom/config.zsh

# # Install zsh autosuggestions
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions

CMD ["zsh", "--version"]

# Install envkey-source
RUN curl -s https://raw.githubusercontent.com/envkey/envkey-source/master/install.sh | bash

# Because nodejs
RUN rm -f /usr/lib/node_modules/npm/node_modules/update-notifier/node_modules/configstore/node_modules/dot-prop/license
