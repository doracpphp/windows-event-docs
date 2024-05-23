---
title: 4695(S, F) 監査可能な保護データの保護解除が試行されました。
description: セキュリティイベント 4695(S, F) 監査可能な保護データの保護解除が試行されました。について説明します。
ms.pagetype: security
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: low
author: vinaypamnani-msft
ms.date: 09/07/2021
ms.reviewer: 
manager: aaroncz
ms.author: vinpa
ms.topic: reference
---

# 4695(S, F): 監査可能な保護データの保護解除が試行されました。

このイベントは、[DPAPI](/previous-versions/ms995355(v=msdn.10)) [CryptUnprotectData](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata)() 関数が、**CRYPTPROTECT\_AUDIT** フラグ (dwFlags) が有効な [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata)() 関数を使用して暗号化された「監査可能」データの保護解除に使用された場合に生成されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[DPAPI アクティビティの監査](audit-dpapi-activity.md)

***イベントスキーマ:***

*監査可能な保護データの保護解除が試行されました。*

*サブジェクト:*

> *セキュリティ ID:%1*
>
> *アカウント名:%2*
>
> *アカウント ドメイン:%3*
>
> *ログオン ID:%4*

*保護されたデータ:*

> *データの説明:%6*
>
> *キー識別子:%5*
>
> *保護データフラグ:%7*
>
> *保護アルゴリズム:%8*

*ステータス情報:*

> *ステータスコード:%9*

***必要なサーバーの役割:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このドキュメントには、このイベントに関する推奨事項はありません。

-   このイベントは通常、情報提供のためのイベントであり、このイベントを使用して悪意のある活動を検出することは困難です。主に DPAPI のトラブルシューティングに使用されます。
