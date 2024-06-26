---
title: ログオンの監査
description: 高度なセキュリティ監査ポリシー設定である「ログオンの監査」は、ユーザーがコンピューターにログオンしようとしたときに監査イベントが生成されるかどうかを決定します。
ms.assetid: ca968d03-7d52-48c4-ba0e-2bcd2937231b
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

# ログオンの監査

ログオンの監査は、ユーザーがコンピューターにログオンしようとしたときにオペレーティングシステムが監査イベントを生成するかどうかを決定します。

これらのイベントはログオンセッションの作成に関連しており、アクセスされたコンピューターで発生します。インタラクティブなログオンの場合、イベントはログオンしたコンピューターで生成されます。共有リソースへのアクセスなどのネットワークログオンの場合、イベントはアクセスされたリソースをホストするコンピューターで生成されます。

次のイベントが記録されます：

- ログオンの成功と失敗。

- 明示的な資格情報を使用したログオン試行。このイベントは、プロセスが明示的にそのアカウントの資格情報を指定してアカウントにログオンしようとしたときに生成されます。これは、スケジュールされたタスクなどのバッチ構成や、**RunAs** コマンドを使用する場合に最も一般的に発生します。

- セキュリティ識別子 (SID) がフィルタリングされます。

ログオンイベントは、ユーザーの活動を追跡し、潜在的な攻撃を検出するために不可欠です。

**イベントボリューム**：

- クライアントコンピューターでは低。

- ドメインコントローラーやネットワークサーバーでは中。

| コンピューターの種類 | 一般的な成功 | 一般的な失敗 | 強化された成功 | 強化された失敗 | コメント                                                                                                                                                                                                                                                          |
|-----------------------|---------------|---------------|------------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ドメインコントローラー | はい          | はい          | はい             | はい             | 例えば、ログオンの監査イベントは、どのアカウントが、いつ、どのログオンタイプを使用して、どのマシンからこのマシンにログオンしたかについての情報を提供します。<br>失敗イベントは、失敗したログオン試行とその理由を示します。 |
| メンバーサーバー     | はい          | はい          | はい             | はい             | 例えば、ログオンの監査イベントは、どのアカウントが、いつ、どのログオンタイプを使用して、どのマシンからこのマシンにログオンしたかについての情報を提供します。<br>失敗イベントは、失敗したログオン試行とその理由を示します。 |
| ワークステーション   | はい          | はい          | はい             | はい             | 例えば、ログオンの監査イベントは、どのアカウントが、いつ、どのログオンタイプを使用して、どのマシンからこのマシンにログオンしたかについての情報を提供します。<br>失敗イベントは、失敗したログオン試行とその理由を示します。 |

**イベントリスト:**

-   [4624](event-4624.md)(S): アカウントのログオンに成功しました。

-   [4625](event-4625.md)(F): アカウントのログオンに失敗しました。

-   [4648](event-4648.md)(S): 明示的な資格情報を使用してログオンが試行されました。

-   [4675](event-4675.md)(S): SIDがフィルタリングされました。
