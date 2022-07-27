#!/bin/sh
docker-compose build
docker-compose up
docker cp go-standard-go-1:/app/coverage.txt ./coverage.txt
echo "Copied coverage file to folder `pwd`/coverage.txt"