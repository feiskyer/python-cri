#!/bin/bash
python -m grpc_tools.protoc -I. --python_out=. gogo.proto
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. api.proto
