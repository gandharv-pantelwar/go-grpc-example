package server

import (
	"context"

	protos "github.com/gandharv-pantelwar/go-grpc-example/protos/currency"

	"github.com/hashicorp/go-hclog"
)

type Currency struct {
	log hclog.Logger
}

func NewCurrency(l hclog.Logger) *Currency {
	return &Currency{l}
}

func (*Currency) GetRate(ctx context.Context, req *protos.RateRequest) (*protos.RateResponse, error) {
	return &protos.RateResponse{Rate: 0.5}, nil
}
