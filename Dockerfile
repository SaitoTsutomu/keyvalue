FROM alpine:3.3

RUN apk add -U g++ python3-dev && \
    apk add --virtual=build-dependencies wget ca-certificates && \
    wget -q https://bootstrap.pypa.io/get-pip.py -O /dev/stdout | python3 && \
    pip install jupyter && \
    apk del g++ python3-dev build-dependencies && \
    apk add libstdc++ python3 && \
    rm -rf /tmp/* /var/cache/apk/* /root/.[acw]*
COPY kernel.json /root/.local/share/jupyter/kernels/keyvalue/
COPY keyvaluekernel.py /usr/lib/python3.5/site-packages/
COPY Sample.ipynb /tmp/
WORKDIR /tmp
EXPOSE 8888
CMD ["sh", "-c", "jupyter notebook --ip=*"]
