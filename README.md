# python-cri

Python client for kubernetes container runtime interface (CRI).

See [CRI](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/runtime-client-server.md) for more details.

## Install

```sh
# For kubernetes v1.6.x
pip install cri==0.1.5

# For kubernetes v1.7.x
pip install cri==0.2.0

# For kubernetes v1.8.x
pip install cri==1.8.1
```

## Usage

```python
import grpc
from cri import api_pb2

channel = grpc.insecure_channel('unix:///var/run/dockershim.sock')
runtime_stub = api_pb2.RuntimeServiceStub(channel)
image_stub = api_pb2.ImageServiceStub(channel)

# Get runtime version
print runtime_stub.Version(api_pb2.VersionRequest())

# Get sandboxes
print runtime_stub.ListPodSandbox(api_pb2.ListPodSandboxRequest())

# Get Images
print image_stub.ListImages(api_pb2.ListImagesRequest())
```

## Full example

Create a busybox container in dockershim.

```python
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
```

