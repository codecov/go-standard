FROM golang:latest

COPY . /go

RUN chmod +x /go/entrypoint.sh

ENTRYPOINT [ "/go/entrypoint.sh" ]