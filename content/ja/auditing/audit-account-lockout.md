---
title: アカウントロックアウトの監査
description: ポリシー設定「アカウントロックアウトの監査」は、ロックアウトされたアカウントへのログオン試行が失敗した際に生成されるセキュリティイベントを監査することを可能にします。
ms.assetid: da68624b-a174-482c-9bc5-ddddab38e589
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

# アカウントロックアウトの監査

アカウントロックアウトの監査は、ロックアウトされたアカウントへのログオン試行が失敗した際に生成されるセキュリティイベントを監査することを可能にします。

このポリシー設定を構成すると、アカウントがロックアウトされているためにコンピュータにログオンできない場合に監査イベントが生成されます。

アカウントロックアウトイベントは、ユーザー活動を理解し、潜在的な攻撃を検出するために不可欠です。

**イベントボリューム**: 低。

このサブカテゴリは、アカウントが既にロックアウトされている場合のログオン試行の失敗を記録します。

| コンピュータの種類 | 一般的な成功 | 一般的な失敗 | 強力な成功 | 強力な失敗 | コメント                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------|-----------------|-----------------|------------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ドメインコントローラー | いいえ              | はい             | いいえ               | はい              | アカウントロックアウトの追跡を推奨します。特に高価値のドメインやローカルアカウント（データベース管理者、組み込みのローカル管理者アカウント、ドメイン管理者、サービスアカウント、ドメインコントローラーアカウントなど）に対してです。<br>このサブカテゴリには成功イベントがないため、成功監査を有効にする推奨事項はありません。 |
| メンバーサーバー     | いいえ              | はい             | いいえ               | はい              | アカウントロックアウトの追跡を推奨します。特に高価値のドメインやローカルアカウント（データベース管理者、組み込みのローカル管理者アカウント、ドメイン管理者、サービスアカウント、ドメインコントローラーアカウントなど）に対してです。<br>このサブカテゴリには成功イベントがないため、成功監査を有効にする推奨事項はありません。 |
| ワークステーション       | いいえ              | はい             | いいえ               | はい              | アカウントロックアウトの追跡を推奨します。特に高価値のドメインやローカルアカウント（データベース管理者、組み込みのローカル管理者アカウント、ドメイン管理者、サービスアカウント、ドメインコントローラーアカウントなど）に対してです。<br>このサブカテゴリには成功イベントがないため、成功監査を有効にする推奨事項はありません。 |

**イベントリスト:**

-   [4625](event-4625.md)(F): アカウントのログオンに失敗しました。
