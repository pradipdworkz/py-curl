FROM python:alpine

# Needed for the pycurl compilation
ENV PYCURL_SSL_LIBRARY=openssl

# Single layer
RUN apk add -u --no-cache libcurl libstdc++ \
    && apk add -u --no-cache --virtual .build-deps build-base g++ libffi-dev curl-dev \
    && pip install --no-cache-dir pycurl asyncio aiohttp[speedups] \
    && apk del --no-cache --purge .build-deps \
    && rm -rf /var/cache/apk/*
    
WORKDIR /mnt

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]