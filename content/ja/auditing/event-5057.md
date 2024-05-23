---
title: 5057(F) 暗号プリミティブ操作が失敗しました。
description: セキュリティイベント 5057(F) 暗号プリミティブ操作が失敗しました について説明します。
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

# 5057(F): 暗号プリミティブ操作が失敗しました。

このイベントは、CNGプリミティブ操作の失敗が発生した場合に生成されます。

Cryptographic Next Generation (CNG) についての詳細は、以下のページを参照してください：

-   <https://msdn.microsoft.com/library/windows/desktop/aa376214(v=vs.85).aspx>

-   <https://msdn.microsoft.com/library/windows/desktop/bb204775(v=vs.85).aspx>

-   <https://www.microsoft.com/download/details.aspx?id=30688>

このイベントは、Cryptographic Next Generation (CNG) のトラブルシューティングに使用されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[システム整合性の監査](audit-system-integrity.md)

***イベントスキーマ:***

*暗号プリミティブ操作が失敗しました。*

*サブジェクト:*

> *セキュリティ ID%1*
>
> *アカウント名:%2*
>
> *アカウント ドメイン:%3*
>
> *ログオン ID:%4*

*暗号化パラメーター:*

> *プロバイダー名:%5*
>
> *アルゴリズム名%6*

*失敗情報:*

> *理由:%7*
>
> *リターンコード:%8*

***必要なサーバー役割:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   通常、このイベントは暗号鍵に関連するCNG関連のアクションの詳細な監視に必要です。特定の暗号鍵および操作に関連するアクションを監視またはトラブルシューティングする必要がある場合、このイベントを確認して必要な情報が提供されているかどうかを確認してください。
