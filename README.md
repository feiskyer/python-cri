# python-cri

Python client for kubernetes container runtime interface (CRI).

See [CRI](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/runtime-client-server.md) for more details.

## Install

```sh
pip install cri
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

