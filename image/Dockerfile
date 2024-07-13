FROM ubuntu:24.04

ARG RUNNER_VERSION="2.317.0"

RUN rm /etc/apt/sources.list && \
    echo "deb http://free.nchc.org.tw/ubuntu-ports/ noble main restricted universe multiverse" > /etc/apt/sources.list ;\
    echo "deb http://free.nchc.org.tw/ubuntu-ports/ noble-security main restricted universe multiverse" >> /etc/apt/sources.list ;\
    echo "deb http://free.nchc.org.tw/ubuntu-ports/ noble-updates main restricted universe multiverse" >> /etc/apt/sources.list ;\
    echo "deb http://free.nchc.org.tw/ubuntu-ports/ noble-backports main restricted universe multiverse" >> /etc/apt/sources.list ;

# github actions runnerに必要なパッケージの準備
RUN apt-get update -y && \
    apt-get install -y curl jq ca-certificates git libicu-dev

RUN groupadd -g 999 runner
RUN useradd -m -g 999 runner
RUN mkdir -p /home/runner/actions-runner

WORKDIR /home/runner/actions-runner
RUN curl -O -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-arm64-${RUNNER_VERSION}.tar.gz && \
    tar xzf ./actions-runner-linux-arm64-${RUNNER_VERSION}.tar.gz && \
    chown -R runner:runner /home/runner

COPY ./run.sh /home/runner

# CI に必要な環境の準備
WORKDIR /home/runner
COPY ./src ./src
RUN apt-get install -y python3

USER runner


ENTRYPOINT ["/home/runner/run.sh"]
