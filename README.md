### How to run?

docker build --tag python-docker .

docker run -d --publish 5000:5000 python-docker

> http://localhost:5000/curl