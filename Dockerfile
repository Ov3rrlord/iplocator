FROM debian:12
RUN apt-get update -yq
RUN apt-get install nmap -yq
ADD . /app/
WORKDIR /app
VOLUME /app/logs
EXPOSE 2424:22
