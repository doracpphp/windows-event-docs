---
title: 5150(-) Windows フィルタリング プラットフォームがパケットをブロックしました。
description: セキュリティ イベント 5150(-) Windows フィルタリング プラットフォームがパケットをブロックしましたについて説明します。
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

# 5150(-): Windows フィルタリング プラットフォームがパケットをブロックしました。

このイベントは、Windows フィルタリング プラットフォーム [MAC フィルター](/windows-hardware/drivers/network/using-layer-2-filtering) がパケットをブロックした場合に記録されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[フィルタリング プラットフォーム接続の監査](audit-filtering-platform-connection.md)

***イベント スキーマ:***

*Windows フィルタリング プラットフォームがパケットをブロックしました。*

*ネットワーク情報:*

> *方向:%1*
>
> *送信元アドレス:%2*
>
> *宛先アドレス:%3*
>
> *EtherType:%4*
>
> *メディアタイプ:%5*
>
> *インターフェース タイプ:%6*
>
> *Vlan タグ:%7*

*フィルター情報:*

> *フィルター ランタイム ID:%8*
>
> *レイヤー名:%9*
>
> *レイヤー ランタイム ID:%10*

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2012、Windows 8。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   このドキュメントには、このイベントに対する推奨事項はありません。
