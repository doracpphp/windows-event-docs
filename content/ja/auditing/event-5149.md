---
title: 5149(F) DoS攻撃が収まり、通常の処理が再開されています。
description: セキュリティイベント5149(F) DoS攻撃が収まり、通常の処理が再開されていますについて説明します。
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

# 5149(F): DoS攻撃が収まり、通常の処理が再開されています。

ほとんどの場合、このイベントはまれにしか発生しません。これは、ICMP DoS攻撃が終了したときに生成されるように設計されています。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[その他のオブジェクトアクセスイベントの監査](audit-other-object-access-events.md)

***イベントスキーマ:***

*DoS攻撃が収まり、通常の処理が再開されています。*

*ネットワーク情報:*

> *タイプ:%1*
>
> *破棄されたパケット:%2*

***必要なサーバー役割:*** なし。

***最小OSバージョン:*** Windows Server 2008 R2、Windows 7。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントは、ICMP DoS攻撃の兆候であるか、その他のハードウェアまたはネットワークデバイスに関連する問題の兆候である可能性があります。いずれの場合も、アラートをトリガーし、イベントが生成された理由を調査することをお勧めします。
