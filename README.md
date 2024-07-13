# GitHub Actions Self Hosted Runner をコンテナの中で動かす

## アクセストークンの発行

以下を有効にする

- repo
- workflow
- admin:org

## github actions runner 搭載の docker コンテナ

- [./image/Dockerfile](./image/Dockerfile): Dockerfile
- [./image/run.sh](./image/run.sh): コンテナ起動時に実行するスクリプト

### Dockerfile のポイント

- Debain パッケージとして、curl jq ca-certificates git libicu-dev が実行に必要

### 起動スクリプトのポイント

- まず、github actions に runner として登録するためのトークンを取得する
- ./config.sh で `--unattended` を追加して、コマンドのみで、runner を登録する
- ./run.sh で実行して、wait でプロセス終了まで待つ
- trap で INT、TERM を受けて、runner の登録を解除する

## docker compose での起動

compose.sample.yml を参考に、compose.yml を作成し、アクセストークンを記述する

```bash
# ビルド
docker compose rm -f
docker compose build

# 起動
docker compose up -d


# 終了
docker compose down
```

起動した状態で、リポジトリの Settings -> Actions -> Runners を開き、登録されていることを確認する

## kubernetes 上での動作

compose.yaml の image を利用可能な Docker レジストリに変更する

manifests/secret/access_token.sample.env を参考に、manifests/secret/access_token.env を作成し、アクセストークンを記述する

```bash
# イメージをDockerレジストリにアップロード
docker compose push

kubectl create ns actions-test
kubectl apply -k manifests
```

## とても参考になるサイト（というか、ほぼそのまま）

- https://developers.play.jp/entry/2023/11/06/104430
