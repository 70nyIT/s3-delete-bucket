from setuptools import setup

setup(
    name='s3-delete-bucket',
    version='0.1',
    description='Delete S3 bucket python tool with an interactive command line',
    author='70nyIT',
    license='MIT',
    py_modules=['dynamic-empty-s3-bucket'],
    install_requires=[
        'boto3',
    ],
    zip_safe=False
)
