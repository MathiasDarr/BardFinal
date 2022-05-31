import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="bard_cdk_deploy",
    version="0.0.1",
    python_requires=">=3.6",
    install_requires=[
        "aws-cdk.core==1.116.0"
    ]
)