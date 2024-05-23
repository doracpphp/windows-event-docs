---
title: 5068(S, F) 暗号化関数プロバイダー操作が試行されました。
description: セキュリティイベント 5068(S, F) 暗号化関数プロバイダー操作が試行されましたについて説明します。
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

# 5068(S, F): 暗号化関数プロバイダー操作が試行されました。

このイベントは、BCryptAddContextFunctionProvider() および BCryptRemoveContextFunctionProvider() 関数で生成されます。これらの関数は、Cryptographic Next Generation (CNG) 関数です。

Cryptographic Next Generation (CNG) についての詳細は、以下のページをご覧ください:

-   <https://msdn.microsoft.com/library/windows/desktop/aa376214(v=vs.85).aspx>

-   <https://www.microsoft.com/download/details.aspx?id=30688>

このイベントは、Cryptographic Next Generation (CNG) のトラブルシューティングに使用されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[その他のポリシー変更イベントの監査](audit-other-policy-change-events.md)

***イベントスキーマ:***

*暗号化関数プロバイダー操作が試行されました。*

*サブジェクト:*

> *セキュリティ ID:%1*
>
> *アカウント名:%2*
>
> *アカウント ドメイン:%3*
>
> *ログオン ID:%4*

*構成パラメーター:*

> *スコープ:%5*
>
> *コンテキスト:%6*
>
> *インターフェイス:%7*
>
> *関数:%8*
>
> *プロバイダー:%9*
>
> *位置:%10*

*操作:%11*

*リターン コード:%12*

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   通常、このイベントは CNG 関連の暗号化関数の詳細な監視に必要です。特定の暗号化関数に関連するアクションを監視またはトラブルシューティングする必要がある場合、このイベントを確認して必要な情報が提供されているかどうかを確認してください。
