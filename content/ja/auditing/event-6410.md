---
title: 6410(F) コード整合性により、ファイルがプロセスにロードするためのセキュリティ要件を満たしていないと判断されました。
description: セキュリティイベント 6410(F) コード整合性により、ファイルがプロセスにロードするためのセキュリティ要件を満たしていないと判断されましたについて説明します。
ms.pagetype: security
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: low
author: vinaypamnani-msft
ms.date: 09/09/2021
ms.reviewer: 
manager: aaroncz
ms.author: vinpa
ms.topic: reference
---

# 6410(F): コード整合性により、ファイルがプロセスにロードするためのセキュリティ要件を満たしていないと判断されました。

[コード整合性](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd348642(v=ws.10)) は、ドライバーやシステムファイルがメモリにロードされるたびにその整合性を検証することで、オペレーティングシステムのセキュリティを向上させる機能です。コード整合性は、署名されていないドライバーやシステムファイルがカーネルにロードされているか、管理者権限を持つユーザーアカウントによって実行されている悪意のあるソフトウェアによってシステムファイルが変更されているかを検出します。x64ベースのオペレーティングシステムバージョンでは、カーネルモードドライバーはデジタル署名されている必要があります。

このイベントは、ファイルイメージに書き込み可能な[共有セクション](/previous-versions/windows/desktop/cc307397(v=msdn.10))が存在するために生成されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[システム整合性の監査](audit-system-integrity.md)

***イベントスキーマ:***

*コード整合性により、ファイルがプロセスにロードするためのセキュリティ要件を満たしていないと判断されました。これは、共有セクションの使用やその他の問題が原因である可能性があります。*

*ファイル名:%1*

***必要なサーバー役割:*** なし。

***最小OSバージョン:*** Windows Server 2012 R2, Windows 8.1。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

- このイベントを監視することをお勧めします。特に高価値の資産やコンピューターでは、ソフトウェアや構成の問題、または悪意のある行動の兆候である可能性があるためです。