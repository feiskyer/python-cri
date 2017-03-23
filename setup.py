from distutils.core import setup

setup(
    name="cri",
    packages=['cri'],
    scripts=['bin/cri'],
    version='0.1.5',
    description='Python client for kubernetes container runtime interface (CRI)',
    author='Pengfei Ni',
    author_email="feiskyer@gmail.com",
    license="Apache License Version 2.0",
    url="https://github.com/feiskyer/python-cri",
    keywords=['kubernetes', 'kubelet-cri', 'containers'],
    install_requires=["grpcio"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)

