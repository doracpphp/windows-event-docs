---
title: 4766(F) アカウントに SID 履歴を追加する試みが失敗しました。
description: セキュリティ イベント 4766(F) アカウントに SID 履歴を追加する試みが失敗しました。
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

# 4766(F): アカウントに SID 履歴を追加する試みが失敗しました。

このイベントは、アカウントに [SID 履歴](/windows/win32/adschema/a-sidhistory) を追加する試みが失敗したときに生成されます。

SID 履歴の詳細については、こちらをご覧ください: <https://technet.microsoft.com/library/cc779590(v=ws.10).aspx>.

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[ユーザー アカウント管理の監査](audit-user-account-management.md)

***イベント スキーマ:***

*アカウントに SID 履歴を追加する試みが失敗しました。*

*サブジェクト:*

> *セキュリティ ID:-*
>
> *アカウント名:%5*
>
> *アカウント ドメイン:%6*
>
> *ログオン ID:%7*

*ターゲット アカウント:*

> *セキュリティ ID:%4*
>
> *アカウント名:%2*
>
> *アカウント ドメイン:%3*

*ソース アカウント:*

> *アカウント名:%1*

*追加情報:*

> *特権:%8*

***必要なサーバー ロール:*** Active Directory ドメイン コントローラー。

***最小 OS バージョン:*** Windows Server 2008。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   このドキュメントには、このイベントに対する推奨事項はありません。
