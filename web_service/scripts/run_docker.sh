#!/bin/bash

# docker run --network srgan-service --name web -it -u $(id -u):$(id -g) -v $PWD:/home/web -p 8000:8000 web:django bash

docker start -i web