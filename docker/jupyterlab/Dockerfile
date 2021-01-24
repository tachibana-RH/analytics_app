FROM ubuntu:20.04

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

USER root

RUN apt-get update -y && apt-get install -y sudo
RUN apt-get install -y python3 python3-pip

# 日本語フォントとpdf出力に必要なライブラリをインストール
RUN apt-get install -y fonts-noto-cjk
RUN apt-get install -y texlive texlive-latex-extra texlive-xetex texlive-lang-japanese pandoc

# jupyterlabをインストール
RUN python3 -m pip install --upgrade pip cython && \
    python3 -m pip install jupyterlab

# 必要なパッケージをインストール
RUN python3 -m pip install matplotlib pandas sklearn chromedriver-binary selenium

# mecabとmecab-ipadic-NEologdの導入
RUN apt-get install -y mecab \
    && apt-get install -y libmecab-dev \
    && apt-get install -y mecab-ipadic-utf8 \
    && apt-get install -y git \
    && apt-get install -y make \
    && apt-get install -y curl \
    && apt-get install -y xz-utils \
    && apt-get install -y file

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && bin/install-mecab-ipadic-neologd -n -y

RUN python3 -m pip install mecab-python3

## JupyterLabの拡張機能

# nodejsの導入
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash - \
    && sudo apt-get install -y nodejs

# 自動整形
RUN python3 -m pip install autopep8 jupyterlab_code_formatter && \
    jupyter serverextension enable --py jupyterlab_code_formatter

## PDFの日本語表示

# 必要なディレクトリの作成
RUN mkdir -p ~/texmf/tex/latex/local/
RUN mkdir -p /usr/local/lib/python3.8/dist-packages/nbconvert/templates/latex/

## chromeのインストール
RUN curl https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add - \
    && echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update -y \
    && apt-get install -y google-chrome-stable

# jupyterlabのコード補完機能のバグ回避 https://github.com/davidhalter/jedi/issues/1714
RUN python3 -m pip install jedi==0.17.2

# 設定ファイル配置スクリプト
WORKDIR /content
COPY init.sh /docker/
CMD [ "sh", "/docker/init.sh" ]