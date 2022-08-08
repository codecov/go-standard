FROM golang:latest

WORKDIR /app

COPY . ./

RUN go mod download

ENTRYPOINT [ "/app/entrypoint.sh" ]
