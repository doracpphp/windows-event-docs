---
title: 5035(F) Windows ファイアウォールドライバーの開始に失敗しました。
description: セキュリティイベント 5035(F) Windows ファイアウォールドライバーの開始に失敗しましたについて説明します。
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

# 5035(F): Windows ファイアウォールドライバーの開始に失敗しました。

Windows は、Windows ファイアウォールドライバーの開始に失敗した場合、または予期せず終了した場合にこのイベントを記録します。エラーメッセージには、メッセージのテキストにエラーコードを含めることで失敗の原因が示されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[その他のシステムイベントの監査](audit-other-system-events.md)

***イベントスキーマ:***

*Windows ファイアウォールドライバーの開始に失敗しました。*

*エラーコード:%1*

***必要なサーバーの役割:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントは、ソフトウェアまたはオペレーティングシステムの問題、または Windows ファイアウォールドライバーを破損させた悪意のある活動の兆候である可能性があります。このイベントを監視し、その状態の理由を調査することをお勧めします。
