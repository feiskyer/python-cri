#!/usr/bin/env python
# Create a busybox container in dockershim.
import grpc
from cri import api_pb2

channel = grpc.insecure_channel('unix:///var/run/dockershim.sock')
runtime_stub = api_pb2.RuntimeServiceStub(channel)
image_stub = api_pb2.ImageServiceStub(channel)


sandboxConfig = api_pb2.PodSandboxConfig(
    metadata=api_pb2.PodSandboxMetadata(name="sandbox", namespace="test"),
    dns_config=api_pb2.DNSConfig(servers=["3.3.3.3"], searches=["google.com"])
)

sandbox_resp = runtime_stub.RunPodSandbox(
    api_pb2.RunPodSandboxRequest(config=sandboxConfig))

print image_stub.PullImage(api_pb2.PullImageRequest(image=api_pb2.ImageSpec(image="busybox")))

containerConfig = api_pb2.ContainerConfig(
    metadata=api_pb2.ContainerMetadata(name="busybox"),
    image=api_pb2.ImageSpec(image="busybox"),
    command=["sh", "-c", "top"],
)

container_resp = runtime_stub.CreateContainer(api_pb2.CreateContainerRequest(
    pod_sandbox_id=sandbox_resp.pod_sandbox_id,
    config=containerConfig,
    sandbox_config=sandboxConfig,
))

print runtime_stub.StartContainer(api_pb2.StartContainerRequest(
    container_id=container_resp.container_id))

print runtime_stub.StopPodSandbox(
    api_pb2.StopPodSandboxRequest(pod_sandbox_id=sandbox_resp.pod_sandbox_id))
