---
title: 5039(-) レジストリキーが仮想化されました。
description: LUAFV を使用してレジストリキーが仮想化されたときに生成されるセキュリティイベント 5039(-) レジストリキーが仮想化されました。について説明します。
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

# 5039(-): レジストリキーが仮想化されました。

このイベントは、[LUAFV](https://blogs.msdn.com/b/alexcarp/archive/2009/06/25/the-deal-with-luafv-sys.aspx) を使用してレジストリキーが仮想化されたときに生成されるべきです。

このイベントは、標準の LUAFV レジストリキー仮想化中にはめったに発生しません。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[Audit Registry](audit-registry.md)

***イベントスキーマ:***

*レジストリキーが仮想化されました。*

*サブジェクト:*

> *セキュリティ ID:%1%*
>
> *アカウント名:%2*
>
> *アカウント ドメイン:%3*
>
> *ログオン ID:%4*

*オブジェクト:*

> *キー名:%5*
>
> *仮想キー名:%6*

*プロセス情報:*

> *プロセス ID:%7*
>
> *プロセス名:%8*

***必要なサーバー役割:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このドキュメントには、このイベントに対する推奨事項はありません。
