FROM python:3.8-slim

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*
 
RUN wget https://github.com/Gedas-LT/tc-calculator

RUN pip install pytest
