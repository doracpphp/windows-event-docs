---
title: 5148(F) Windows フィルタリング プラットフォームが DoS 攻撃を検出し、防御モードに入りました。この攻撃に関連するパケットは破棄されます。
description: セキュリティ イベント 5148(F) の詳細、Windows フィルタリング プラットフォームが DoS 攻撃を検出し、防御モードに入りました。
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

# 5148(F): Windows フィルタリング プラットフォームが DoS 攻撃を検出し、防御モードに入りました。この攻撃に関連するパケットは破棄されます。

ほとんどの場合、このイベントはまれにしか発生しません。これは、ICMP DoS 攻撃が開始されたか検出されたときに生成されるように設計されています。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[その他のオブジェクト アクセス イベントの監査](audit-other-object-access-events.md)

***イベント スキーマ:***

*Windows フィルタリング プラットフォームが DoS 攻撃を検出し、防御モードに入りました。この攻撃に関連するパケットは破棄されます。*

*ネットワーク情報:*

> *タイプ:%1*

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008 R2、Windows 7。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントは、ICMP DoS 攻撃の兆候である可能性があるほか、ハードウェアやネットワーク デバイスに関連する問題の兆候である可能性もあります。いずれの場合も、アラートをトリガーし、イベントが生成された理由を調査することをお勧めします。
