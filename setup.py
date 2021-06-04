import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="sagemakerStudioCDK",
    version="0.0.1",

    description="aws-cdk-sagemaker-studio",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="haramine",

    package_dir={"": "sagemakerStudioCDK"},
    packages=setuptools.find_packages(where="sagemakerStudioCDK"),

    install_requires=[
        "aws-cdk.core==1.87.1",
        "aws-cdk.cloudformation_include==1.87.1",
        "aws-cdk.aws_iam==1.87.1",
        "aws-cdk.aws_ec2==1.87.1",
        "boto3"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
