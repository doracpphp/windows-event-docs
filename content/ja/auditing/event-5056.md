---
title: 5056(S) 暗号化セルフテストが実行されました。
description: セキュリティイベント 5056(S) 暗号化セルフテストが実行されました。について説明します。
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

# 5056(S): 暗号化セルフテストが実行されました。

このイベントは CNG セルフテスト機能で生成されます。この機能は次世代暗号化 (CNG) 機能です。

次世代暗号化 (CNG) についての詳細は以下のページを参照してください:

-   <https://msdn.microsoft.com/library/windows/desktop/aa376214(v=vs.85).aspx>

-   <https://msdn.microsoft.com/library/windows/desktop/bb204775(v=vs.85).aspx>

-   <https://www.microsoft.com/download/details.aspx?id=30688>

このイベントは CNG のトラブルシューティングに使用されます。

このドキュメントにはこのイベントの例はありません。

***サブカテゴリ:***&nbsp;[システム整合性の監査](audit-system-integrity.md)

***イベントスキーマ:***

*暗号化セルフテストが実行されました。*

*サブジェクト:*

> *セキュリティ ID%1*
>
> *アカウント名:%2*
>
> *アカウント ドメイン:%3*
>
> *ログオン ID:%4*

*モジュール:%5*

*リターンコード:%6*

***必要なサーバー役割:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   通常、このイベントは暗号化キーに関連する CNG の詳細な監視に必要です。特定の暗号化キーおよび操作に関連するアクションを監視またはトラブルシューティングする必要がある場合、このイベントを確認して必要な情報が提供されているかどうかを確認してください。
