---
title: 5037(F) Windows ファイアウォールドライバーが重大なランタイムエラーを検出しました。終了します。
description: 5037(F) Windows ファイアウォールドライバーが重大なランタイムエラーを検出しました。終了します。というセキュリティイベントについて説明します。
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

# 5037(F): Windows ファイアウォールドライバーが重大なランタイムエラーを検出しました。終了します。

Windows ファイアウォールドライバーが起動に失敗した場合、または予期せず終了した場合、Windows はこのイベントを記録します。エラーメッセージには、メッセージのテキストにエラーコードが含まれており、失敗の原因を示します。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[その他のシステムイベントの監査](audit-other-system-events.md)

***イベントスキーマ:***

*Windows ファイウォールドライバーが重大なランタイムエラーを検出し、終了します。*

*エラーコード:%1*

***必要なサーバー役割:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントは、ソフトウェアまたはオペレーティングシステムの問題、または Windows ファイウォールドライバーを破損させた悪意のある活動の兆候である可能性があります。このイベントを監視し、状態の原因を調査することをお勧めします。
