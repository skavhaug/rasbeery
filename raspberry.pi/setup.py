import setuptools

setuptools.setup(
    name="rasbeery",
    version="0.0.0.1",
    author="Ola Skavhaug",
    author_email="ola@xal.no",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "mash_example=rasbeery.mash:mash_example"
        ]
    }
)