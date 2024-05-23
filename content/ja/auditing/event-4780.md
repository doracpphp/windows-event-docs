---
title: 4780(S) 管理者グループのメンバーであるアカウントにACLが設定されました。
description: セキュリティイベント4780(S) 管理者グループのメンバーであるアカウントにACLが設定されました。について説明します。
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

# 4780(S): 管理者グループのメンバーであるアカウントにACLが設定されました。

毎時間、プライマリドメインコントローラ (PDC) フレキシブルシングルマスター操作 (FSMO) ロールを保持するドメインコントローラは、Active Directory内のドメインに存在するすべてのセキュリティプリンシパルアカウント (ユーザー、グループ、およびマシンアカウント) で、AdminCount属性が1である管理またはセキュリティに敏感なグループのACLを[AdminSDHolder](/previous-versions/technet-magazine/ee361593(v=msdn.10))オブジェクトのACLと比較します。プリンシパルアカウントのACLがAdminSDHolderオブジェクトのACLと異なる場合、プリンシパルアカウントのACLはAdminSDHolderオブジェクトのACLに一致するようにリセットされ、このイベントが生成されます。

何らかの理由で、このイベントは一部のOSバージョンでは生成されません。

***サブカテゴリ:***&nbsp;[ユーザーアカウント管理の監査](audit-user-account-management.md)

***イベントスキーマ:***

*管理者グループのメンバーであるアカウントにACLが設定されました。*

*サブジェクト:*

> *セキュリティID:%4*
>
> *アカウント名:%5*
>
> *アカウントドメイン:%6*
>
> *ログオンID:%7*

*ターゲットアカウント:*

> *セキュリティID:%3*
>
> *アカウント名:%1*
>
> *アカウントドメイン:%2*

*追加情報:*

> *特権:%8*

***必要なサーバーロール:*** Active Directoryドメインコントローラ。

***最小OSバージョン:*** Windows Server 2008。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

- このイベントを監視し、オブジェクトのACLが変更された理由を調査します。
