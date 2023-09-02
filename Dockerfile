#Create custom docker for test, made by Daniel Grunberg

FROM ubuntu:latest

ENV VERSION=1.2.0

RUN apt-get update && apt-get install -y python3 vim zip unzip && apt-get clean

COPY zip_job.py /tmp/
#COPY test.txt /tmp/

CMD ["sh", "-c", "echo 'OS type and architecture:' $(uname -s)-$(uname -m); if [ -f /tmp/zip_job.py ]; then echo 'python file exists in the tmp folder'; ls -l /tmp/zip_job.py; else echo 'python file does not exist'; fi;"]

