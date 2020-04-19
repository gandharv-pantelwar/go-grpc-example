package main

import (
	"fmt"
	"net"
	"os"

	protos "github.com/gandharv-pantelwar/go-grpc-example/protos/currency"
	server "github.com/gandharv-pantelwar/go-grpc-example/protos/server"
	"github.com/hashicorp/go-hclog"
	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"
)

func main() {
	log := hclog.Default()
	gs := grpc.NewServer()
	cs := server.NewCurrency(log)
	protos.RegisterCurrencyServer(gs, cs)

	reflection.Register(gs)

	l, err := net.Listen("tcp", fmt.Sprintf(":%d", 9092))
	if err != nil {
		log.Error("Unable to listen", err)
		os.Exit(1)
	}

	gs.Serve(l)
}
