FROM ubuntu:18.10
RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN mkdir src
WORKDIR /src
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY src/ /src/
CMD python3 main.py