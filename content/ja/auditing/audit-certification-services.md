---
title: 監査認証サービス
description: ポリシー設定「監査認証サービス」は、Active Directory 証明書サービス (AD CS) の操作が実行されたときにイベントが生成されるかどうかを決定します。
ms.assetid: cdefc34e-fb1f-4eff-b766-17713c5a1b03
ms.reviewer: 
manager: aaroncz
ms.author: vinpa
ms.pagetype: security
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: low
author: vinaypamnani-msft
ms.date: 09/06/2021
ms.topic: reference
---

# 監査認証サービス

監査認証サービスは、Active Directory 証明書サービス (AD CS) の操作が実行されたときにオペレーティング システムがイベントを生成するかどうかを決定します。

AD CS 操作の例には次のものが含まれます。

-   AD CS の開始、シャットダウン、バックアップ、または復元。

-   証明書失効リスト (CRL) に関連するタスクの実行。

-   証明書の要求、発行、または失効。

-   AD CS の証明書マネージャー設定の変更。

-   認証局 (CA) の構成およびプロパティの変更。

-   AD CS テンプレートの変更。

-   証明書のインポート。

-   CA 証明書の Active Directory ドメイン サービスへの公開。

-   AD CS ロール サービスのセキュリティ許可の変更。

-   キーのアーカイブ、インポート、または取得。

-   OCSP レスポンダー サービスの開始または停止。

これらの操作イベントを監視することは、AD CS ロール サービスが適切に機能していることを確認するために重要です。

**イベント ボリューム: AD CS ロール サービスを提供するサーバーでは低から中。**

ロール固有のサブカテゴリはこのドキュメントの範囲外です。

| コンピューターの種類 | 一般的な成功 | 一般的な失敗 | 強力な成功 | 強力な失敗 | コメント                                                                                                                                                                                                                        |
|-----------------------|---------------|---------------|--------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ドメイン コントローラー | IF            | IF            | IF           | IF           | IF – サーバーに [Active Directory 証明書サービス](/windows/deployment/deploy-whats-new) (AD CS) ロールがインストールされており、AD CS 関連のイベントを監視する必要がある場合、このサブカテゴリを有効にします。 |
| メンバー サーバー     | IF            | IF            | IF           | IF           | IF – サーバーに [Active Directory 証明書サービス](/windows/deployment/deploy-whats-new) (AD CS) ロールがインストールされており、AD CS 関連のイベントを監視する必要がある場合、このサブカテゴリを有効にします。 |
| ワークステーション   | No            | No            | No           | No           | [Active Directory 証明書サービス](/windows/deployment/deploy-whats-new) (AD CS) ロールはクライアント OS にインストールできません。                                                                         |

- 4868: 証明書マネージャーが保留中の証明書要求を拒否しました。

- 4869: 証明書サービスが再提出された証明書要求を受け取りました。

- 4870: 証明書サービスが証明書を失効させました。

- 4871: 証明書サービスが証明書失効リスト（CRL）の公開要求を受け取りました。

- 4872: 証明書サービスが証明書失効リスト（CRL）を公開しました。

- 4873: 証明書要求の拡張が変更されました。

- 4874: 1つ以上の証明書要求属性が変更されました。

- 4875: 証明書サービスがシャットダウン要求を受け取りました。

- 4876: 証明書サービスのバックアップが開始されました。

- 4877: 証明書サービスのバックアップが完了しました。

- 4878: 証明書サービスの復元が開始されました。

- 4879: 証明書サービスの復元が完了しました。

- 4880: 証明書サービスが開始されました。

- 4881: 証明書サービスが停止されました。

- 4882: 証明書サービスのセキュリティ権限が変更されました。

- 4883: 証明書サービスがアーカイブされたキーを取得しました。

- 4884: 証明書サービスが証明書をデータベースにインポートしました。

- 4885: 証明書サービスの監査フィルターが変更されました。

- 4886: 証明書サービスが証明書要求を受け取りました。

- 4887: 証明書サービスが証明書要求を承認し、証明書を発行しました。

- 4888: 証明書サービスが証明書要求を拒否しました。

- 4889: 証明書サービスが証明書要求のステータスを保留中に設定しました。

- 4890: 証明書サービスの証明書マネージャー設定が変更されました。

- 4891: 証明書サービスの構成エントリが変更されました。

- 4892: 証明書サービスのプロパティが変更されました。

- 4893: 証明書サービスがキーをアーカイブしました。

- 4894: 証明書サービスがキーをインポートしてアーカイブしました。

- 4895: 証明書サービスがCA証明書をActive Directoryドメインサービスに公開しました。

- 4896: 証明書データベースから1つ以上の行が削除されました。

- 4897: ロール分離が有効になりました。

- 4898: 証明書サービスがテンプレートをロードしました。
