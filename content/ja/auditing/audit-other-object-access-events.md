---
title: 他のオブジェクトアクセスイベントの監査
description: ポリシー設定「他のオブジェクトアクセスイベントの監査」は、タスクスケジューラのジョブやCOM+オブジェクトの管理に関する監査イベントが生成されるかどうかを決定します。
ms.assetid: b9774595-595d-4199-b0c5-8dbc12b6c8b2
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

# 他のオブジェクトアクセスイベントの監査

他のオブジェクトアクセスイベントの監査を使用すると、スケジュールされたタスク、COM+オブジェクト、および間接オブジェクトアクセス要求の操作を監視できます。

**イベントボリューム**: 低。

| コンピューターの種類 | 一般的な成功 | 一般的な失敗 | 強化された成功 | 強化された失敗 | コメント                                                                                                                                                           |
|-----------------------|---------------|---------------|------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ドメインコントローラー | はい          | はい          | はい             | はい             | スケジュールされたタスクイベントのため、まず成功の監査を推奨します。<br>ICMP DoS攻撃の可能性に関するイベントを取得するために失敗の監査を推奨します。 |
| メンバーサーバー     | はい          | はい          | はい             | はい             | スケジュールされたタスクイベントのため、まず成功の監査を推奨します。<br>ICMP DoS攻撃の可能性に関するイベントを取得するために失敗の監査を推奨します。 |
| ワークステーション   | はい          | はい          | はい             | はい             | スケジュールされたタスクイベントのため、まず成功の監査を推奨します。<br>ICMP DoS攻撃の可能性に関するイベントを取得するために失敗の監査を推奨します。 |

**イベントリスト:**

-   [4671](event-4671.md)(-): アプリケーションがTBSを通じてブロックされたオーディナルにアクセスしようとしました。

-   [4691](event-4691.md)(S): オブジェクトへの間接アクセスが要求されました。

-   [5148](event-5148.md)(F): Windows フィルタリング プラットフォームが DoS 攻撃を検出し、防御モードに入りました。この攻撃に関連するパケットは破棄されます。

-   [5149](event-5149.md)(F): DoS 攻撃が収まり、通常の処理が再開されました。

-   [4698](event-4698.md)(S): スケジュールされたタスクが作成されました。

-   [4699](event-4699.md)(S): スケジュールされたタスクが削除されました。

-   [4700](event-4700.md)(S): スケジュールされたタスクが有効化されました。

-   [4701](event-4701.md)(S): スケジュールされたタスクが無効化されました。

-   [4702](event-4702.md)(S): スケジュールされたタスクが更新されました。

-   [5888](event-5888.md)(S): COM+ カタログ内のオブジェクトが変更されました。

-   [5889](event-5889.md)(S): COM+ カタログからオブジェクトが削除されました。

-   [5890](event-5890.md)(S): COM+ カタログにオブジェクトが追加されました。
