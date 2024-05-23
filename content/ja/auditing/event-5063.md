---
title: 5063(S, F) 暗号プロバイダー操作が試行されました。
description: セキュリティ イベント 5063(S, F) 暗号プロバイダー操作が試行されました。
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

# 5063(S, F): 暗号プロバイダー操作が試行されました。

このイベントは、BCryptUnregisterProvider() および BCryptRegisterProvider() 関数で生成されます。これらの関数は、Cryptographic Next Generation (CNG) 関数です。

このイベントは、暗号プロバイダーが登録または登録解除されたときに生成されます。

Cryptographic Next Generation (CNG) の詳細については、次のページを参照してください。

-   <https://msdn.microsoft.com/library/windows/desktop/aa376214(v=vs.85).aspx>

-   <https://www.microsoft.com/download/details.aspx?id=30688>

このイベントは、Cryptographic Next Generation (CNG) のトラブルシューティングに使用されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[その他のポリシー変更イベントの監査](audit-other-policy-change-events.md)

***イベント スキーマ:***

*暗号プロバイダー操作が試行されました。*

*サブジェクト:*

> *セキュリティ ID:%1*
>
> *アカウント名:%2*
>
> *アカウント ドメイン:%3*
>
> *ログオン ID:%4*

*暗号プロバイダー:*

> *名前:%5*
>
> *モジュール:%6*
>
> *操作:%7*

*リターン コード:%8*

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008、Windows Vista。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   通常、このイベントは CNG 関連の暗号関数の詳細な監視に必要です。特定の暗号関数に関連するアクションを監視またはトラブルシューティングする必要がある場合は、このイベントを確認して必要な情報が提供されているかどうかを確認してください。
