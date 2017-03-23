#!/bin/bash
python -m grpc_tools.protoc -I. -I${GOPATH}/src/k8s.io/kubernetes/pkg/kubelet/api/v1alpha1/runtime --python_out=. --grpc_python_out=. ${GOPATH}/src/k8s.io/kubernetes/pkg/kubelet/api/v1alpha1/runtime/api.proto
