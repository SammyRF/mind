FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN npm i -g groq-cli
