---
title: 5062(S) カーネルモードの暗号化自己テストが実行されました。
description: セキュリティイベント 5062(S) カーネルモードの暗号化自己テストが実行されました。
ms.pagetype: security
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: low
author: vinaypamnani-msft
ms.date: 09/08/2021
ms.reviewer: 
manager: aaroncz
ms.author: vinpa
ms.topic: reference
---

# 5062(S): カーネルモードの暗号化自己テストが実行されました。

このイベントはまれに発生し、状況によっては再現が難しい場合があります。

***サブカテゴリ:***&nbsp;[システム整合性の監査](audit-system-integrity.md)

***イベントスキーマ:***

*カーネルモードの暗号化自己テストが実行されました。*

*モジュール:%1*

*リターンコード:%2*

***必要なサーバー役割:*** なし。

***最小OSバージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   通常、このイベントは暗号化キーに関連するCNG関連のアクションの詳細な監視に必要です。特定の暗号化キーおよび操作に関連するアクションを監視またはトラブルシューティングする必要がある場合、このイベントを確認して必要な情報が提供されているかどうかを確認してください。
