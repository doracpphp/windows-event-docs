---
title: 4765(S) SID History がアカウントに追加されました。
description: SID History がアカウントに追加されたときに生成されるセキュリティ イベント 4765(S) について説明します。このイベントは、SID History がアカウントに追加されたときに生成されます。
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

# 4765(S): SID History がアカウントに追加されました。

このイベントは、[SID History](/windows/win32/adschema/a-sidhistory) がアカウントに追加されたときに生成されます。

SID History の詳細については、こちらをご覧ください: <https://technet.microsoft.com/library/cc779590(v=ws.10).aspx>.

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[ユーザー アカウント管理の監査](audit-user-account-management.md)

***イベント スキーマ:***

*SID History がアカウントに追加されました。*

*サブジェクト:*

> *セキュリティ ID:%6*
>
> *アカウント名:%7*
>
> *アカウント ドメイン:%8*
>
> *ログオン ID:%9*

*ターゲット アカウント:*

> *セキュリティ ID:%5*
>
> *アカウント名:%3*
>
> *アカウント ドメイン:%4*

*ソース アカウント:*

> *セキュリティ ID:%2*
>
> *アカウント名:%1*

*追加情報:*

> *特権:%10*
>
> *SID リスト:%11*

***必要なサーバー ロール:*** Active Directory ドメイン コントローラー。

***最小 OS バージョン:*** Windows Server 2008。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   このドキュメントには、このイベントに対する推奨事項はありません。
