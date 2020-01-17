import setuptools

with open('README.md', "r") as readme:
    long_description = readme.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()


setuptools.setup(
    name="QuizWebServer",
    version="1.0.0",
    author="Rustam Aliev",
    author_email="rustam.aliev.work@yandex.ru",
    description="A pretty simple web server for fun quiz game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rustam-python/Questioner-Server",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flask",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MPL-2.0",
        "Operating System :: Unix",
    ]
)
