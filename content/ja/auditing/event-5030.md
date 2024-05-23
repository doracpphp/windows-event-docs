---
title: 5030(F) Windows ファイアウォール サービスの開始に失敗しました。
description: セキュリティ イベント 5030(F) Windows ファイアウォール サービスの開始に失敗しました。について説明します。
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

# 5030(F): Windows ファイアウォール サービスの開始に失敗しました。

Windows ファイアウォール サービスの開始に失敗した場合、または予期せず終了した場合に、Windows はこのイベントを記録します。エラーメッセージには、メッセージのテキストにエラーコードが含まれており、サービスの失敗の原因が示されます。

Windows ファイアウォール ポリシーが不正確または破損している場合、またはサービスの依存関係の 1 つが開始されなかった場合、このイベントは生成されません。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[その他のシステム イベントの監査](audit-other-system-events.md)

***イベント スキーマ:***

*Windows ファイアウォール サービスの開始に失敗しました。*

*エラー コード:%1*

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントは、ソフトウェアまたはオペレーティング システムの問題、または Windows ファイアウォール ドライバーが破損した悪意のある活動の兆候である可能性があります。このイベントを監視し、状態の原因を調査することをお勧めします。
