FROM ubuntu:18.04

# ENV PYTHONUNBUFFERED 1
# ENV DEBIAN_FRONTEND noninteractive

USER root

RUN apt update -y && \
    apt install -y sudo vim build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev

RUN apt install -y locales
RUN locale-gen ja_JP.UTF-8
RUN echo "export LANG='ja_JP.UTF-8'" >> "${HOME}/.profile" && \
    echo "export LANG='ja_JP.UTF-8'" >> "${HOME}/.bashrc"

RUN apt install -y fonts-noto-cjk
RUN apt install -y texlive texlive-latex-extra texlive-xetex texlive-lang-japanese pandoc

RUN wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tgz
RUN tar -xzvf Python-3.7.4.tgz
RUN cd Python-3.7.9 && ./configure --enable-optimizations && make -j && make altinstall
RUN python3.7 --version

RUN pip install --upgrade pip && pip install jupyterlab
# matplotlib pandas sklearn
# RUN apt install -y mecab \
#     && apt install -y libmecab-dev \
#     && apt install -y mecab-ipadic-utf8 \
#     && apt install -y git \
#     && apt install -y make \
#     && apt install -y curl \
#     && apt install -y xz-utils \
#     && apt install -y file

# RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
#     && cd mecab-ipadic-neologd \
#     && bin/install-mecab-ipadic-neologd -n -y

# RUN pip install mecab-python3

# RUN apt install -y gnupg \
#   && wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
#   && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
#   && apt install -y ./google-chrome-stable_current_amd64.deb \
#   && apt clean \
#   && rm -rf /var/lib/apt/lists/ \
#   && rm google-chrome-stable_current_amd64.deb

# RUN pip install selenium chromedriver-binary~=$(/usr/bin/google-chrome --version | perl -pe 's/([^0-9]+)([0-9]+\.[0-9]+).+/$2/g')

RUN curl -sL https://deb.nodesource.com/setup_11.x | sudo -E bash - \
    && sudo apt install -y nodejs

RUN pip install autopep8 jupyterlab_code_formatter \
    && jupyter serverextension enable --py jupyterlab_code_formatter