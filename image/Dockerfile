FROM ubuntu:22.04

ARG RUNNER_VERSION="2.317.0"

RUN echo "deb http://free.nchc.org.tw/ubuntu-ports/ jammy main restricted universe multiverse" > /etc/apt/sources.list ;\
echo "deb http://free.nchc.org.tw/ubuntu-ports/ jammy-security main restricted universe multiverse" >> /etc/apt/sources.list ;\
echo "deb http://free.nchc.org.tw/ubuntu-ports/ jammy-updates main restricted universe multiverse" >> /etc/apt/sources.list ;\
echo "deb http://free.nchc.org.tw/ubuntu-ports/ jammy-backports main restricted universe multiverse" >> /etc/apt/sources.list ;

RUN apt-get update -y
RUN apt-get install -y \
    curl jq build-essential libssl-dev libffi-dev python3 python3-venv python3-dev python3-pip \
    ca-certificates gnupg lsb-release unzip git

RUN groupadd -g 1000 runner
RUN useradd -m -g 1000 runner
RUN mkdir -p /home/runner/actions-runner

WORKDIR /home/runner/actions-runner
RUN curl -O -L https://github.com/actions/runner/releases/download/v${RUNNER_VERSION}/actions-runner-linux-arm64-${RUNNER_VERSION}.tar.gz
RUN tar xzf ./actions-runner-linux-arm64-${RUNNER_VERSION}.tar.gz

RUN apt-get install -y libicu-dev

RUN chown -R runner:runner /home/runner

COPY ./run.sh /home/runner

USER runner

WORKDIR /home/runner

COPY ./src ./src

ENTRYPOINT ["/home/runner/run.sh"]
