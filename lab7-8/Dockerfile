FROM jenkins/jenkins:latest

USER 0

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pytest
RUN apt-get install -y python3-selenium
RUN apt-get install -y python3-locust
RUN apt-get install -y qemu-system-arm
RUN apt-get install -y wget
RUN apt-get install -y unzip

USER jenkins