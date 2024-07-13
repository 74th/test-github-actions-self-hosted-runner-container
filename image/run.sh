#!/bin/bash
# 参考: https://developers.play.jp/entry/2023/11/06/104430
set -xe

GITHUB_API_URL="https://api.github.com"
GITHUB_URL="https://github.com"
ACCESS_TOKEN=$ACCESS_TOKEN
OWNER=$OWNER
REPO=$REPO

REG_TOKEN=$(curl -sX POST -H "Authorization: token ${ACCESS_TOKEN}" ${GITHUB_API_URL}/repos/${OWNER}/${REPO}/actions/runners/registration-token | jq .token --raw-output)
cd /home/runner/actions-runner
echo "setup Repository Runner"
./config.sh --url ${GITHUB_URL}/${OWNER}/${REPO} --unattended --token ${REG_TOKEN}

cleanup() {
    echo "Removing runner..."
    ./config.sh remove --token ${REG_TOKEN}
}

trap 'cleanup; exit 130' INT
trap 'cleanup; exit 143' TERM

./run.sh & wait $!