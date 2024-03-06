FROM debian:11
RUN apt-get update -yq
RUN apt-get install python3 -yq
RUN apt-get install python3-requests -yq
ADD . /app/
WORKDIR /app
VOLUME /app/logs
CMD python3 iplocator.py
