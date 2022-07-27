FROM golang:latest

WORKDIR /app

COPY go.mod ./
RUN go mod download

COPY . ./
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
