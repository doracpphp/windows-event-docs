---
title: 6281(F) コード整合性がイメージファイルのページハッシュが無効であると判断しました。
description: イメージファイルのページハッシュが無効であると判断したセキュリティイベント6281(F)について説明します。
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

# 6281(F): コード整合性がイメージファイルのページハッシュが無効であると判断しました。ファイルはページハッシュなしで不適切に署名されているか、不正な変更により破損している可能性があります。無効なハッシュは潜在的なディスクデバイスエラーを示している可能性があります。

ファイルはページハッシュなしで不適切に署名されているか、不正な変更により破損している可能性があります。無効なハッシュは潜在的なディスクデバイスエラーを示している可能性があります。

[コード整合性](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd348642(v=ws.10))は、ドライバーやシステムファイルがメモリにロードされるたびにその整合性を検証することで、オペレーティングシステムのセキュリティを向上させる機能です。コード整合性は、署名されていないドライバーやシステムファイルがカーネルにロードされているか、管理者権限を持つユーザーアカウントによって実行されている悪意のあるソフトウェアによってシステムファイルが変更されているかを検出します。x64ベースのオペレーティングシステムバージョンでは、カーネルモードドライバーはデジタル署名されている必要があります。

このイベントは、[コード整合性](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd348642(v=ws.10))がイメージファイルのページハッシュが無効であると判断したときに生成されます。ファイルはページハッシュなしで不適切に署名されているか、不正な変更により破損している可能性があります。このイベントは、署名証明書が取り消されたときにも生成されます。無効なハッシュは潜在的なディスクデバイスエラーを示している可能性があります。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[システム整合性の監査](audit-system-integrity.md)

***イベントスキーマ:***

*コード整合性がイメージファイルのページハッシュが無効であると判断しました。ファイルはページハッシュなしで不適切に署名されているか、不正な変更により破損している可能性があります。無効なハッシュは潜在的なディスクデバイスエラーを示している可能性があります。*


*ファイル名:%1*

***必要なサーバーロール:*** なし。

***最小OSバージョン:*** Windows Server 2008 R2, Windows 7。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントは、特に高価値資産やコンピュータ上で監視することをお勧めします。これは、ソフトウェアや構成の問題、または悪意のある行動の兆候である可能性があるためです。