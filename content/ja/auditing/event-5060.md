---
title: 5060(F) 検証操作に失敗しました。
description: セキュリティイベント5060(F) 検証操作に失敗しましたについて説明します。このイベントは、CNG検証操作が失敗したときに生成されます。
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

# 5060(F): 検証操作に失敗しました。

このイベントは、次世代暗号化 (CNG) 検証操作が失敗したときに生成されます。

CNGに関する詳細情報は、以下のページをご覧ください:

-   <https://msdn.microsoft.com/library/windows/desktop/aa376214(v=vs.85).aspx>

-   <https://msdn.microsoft.com/library/windows/desktop/bb204775(v=vs.85).aspx>

-   <https://www.microsoft.com/download/details.aspx?id=30688>

このイベントはCNGのトラブルシューティングに使用されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[システム整合性の監査](audit-system-integrity.md)

***イベントスキーマ:***

*検証操作に失敗しました。*

*サブジェクト:*

> *セキュリティID%1*
>
> *アカウント名:%2*
>
> *アカウントドメイン:%3*
>
> *ログオンID:%4*

*暗号化パラメータ:*

> *プロバイダ名:%5*
>
> *アルゴリズム名%6*
>
> *キー名:%7*
>
> *キータイプ:%8*

*失敗情報:*

> *理由:%7*
>
> *リターンコード:%8*

***必要なサーバー役割:*** なし。

***最小OSバージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   通常、このイベントは暗号化キーに関連するCNGの詳細な監視に必要です。特定の暗号化キーおよび操作に関連するアクションを監視またはトラブルシューティングする必要がある場合、このイベントを確認して必要な情報が提供されているかどうかを確認してください。
