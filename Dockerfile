FROM ubuntu:21.04
WORKDIR /py_build

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -qq update && apt-get -y upgrade && \
    apt install -y procps && \
    apt install -y python3 && \
	apt install -y wget unzip nano  && \
    apt install -y python3-pip &&\
    apt install -y python3-numpy &&\
    apt install -y python3-pandas &&\
    apt install -y python-argparse &&\
    rm -rf /var/lib/apt/lists/*
