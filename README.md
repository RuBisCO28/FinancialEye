# Financial Eye

このサイトでは一個人の実験的な試みとして、各企業が金融庁に提出しているXBRLと株価情報、
また検索トレンドの情報をベースに作成したWebサービスです。
個人投資家が投資判断を行う際、財務データは企業HPのIRページから取得し、
株価は他サイトから取得するという煩雑になりがちな財務分析作業を
自動かつひとつのツールとして提供することで、より手軽に分析することを目指して作成しました。

[URL] https://fe360-285518.wl.r.appspot.com/

# Architecture
- GCP(GCE/GAE/Cloud Run/Cloud Build/Cloud Storage/Data Store)
- GCPの無料枠を最大限に生かし、アプリ自体はGAE、データの更新にGCE、データのアーカイブにCloud Storage / DataStoreを使用。
- チェットボット用のサーバについてはDockerを使い、Cloud Run/Cloud Buildで本番環境をサーバーレスで運用。

本構成での特徴は以下の4つとなります。

## 保守性
アプリケーションはGAEとCloud Runで冗長化している。

## コスト
無料枠の範囲内でサービスを選定し、管理コストを低減している。

## セキュリティ
IAM設定により、外部からの不要なリクエストを受け付けないようにしている。

## 性能
GAE/Cloud RunともにAutoScaleが可能であり、リクエスト数に応じてサーバ台数を自動的に増減させることで応答性能を保つことができる。

# 機能一覧:

## 業績データ(通期)
- 各種企業情報
- 業績推移グラフ
- キャッシュフロー推移グラフ
- 財務三表

## 株価データ
- 株価推移(ロウソクチャート)
- 25日/75日移動平均線

## Googleトレンド
- 検索傾向
- 急上昇キーワード

## チャットボット
- 銘柄をキーワードで全文検索
- 該当企業名およびリンクを返答

# 使用技術一覧:
- HTML/CSS
- Javascript/jQuery

## 開発環境
- Docker/docker-compose
- Python 3.7.0
- Flask 1.1.2
