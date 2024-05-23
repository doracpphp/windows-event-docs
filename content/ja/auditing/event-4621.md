---
title: 4621(S) 管理者が CrashOnAuditFail からシステムを回復しました。
description: 4621(S) 管理者が CrashOnAuditFail からシステムを回復しましたというセキュリティイベントについて説明します。
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

# 4621(S): 管理者が CrashOnAuditFail からシステムを回復しました。



このイベントは、[CrashOnAuditFail](/previous-versions/windows/it-pro/windows-2000-server/cc963220(v=technet.10)?f=255&MSPPError=-2147217396) に続いてシステムが再起動した後に記録されます。CrashOnAuditFail = 2 の場合に生成されます。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[監査セキュリティ状態の変更](audit-security-state-change.md)

***イベントスキーマ:***

*管理者が CrashOnAuditFail からシステムを回復しました。管理者でないユーザーはログオンできるようになります。一部の監査可能なアクティビティが記録されていない可能性があります。*

*CrashOnAuditFail の値:%1*

*このイベントは、CrashOnAuditFail に続いてシステムが再起動した後に記録されます。*

***必要なサーバーロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントが発生した場合には、アラートをトリガーすることをお勧めします。このイベントは、[CrashOnAuditFail](/previous-versions/windows/it-pro/windows-2000-server/cc963220(v=technet.10)?f=255&MSPPError=-2147217396) に記載されているように、セキュリティログに監査可能なイベントを記録できなかったためにシステムが停止したことを示しています。

-   コンピューターに [CrashOnAuditFail](/previous-versions/windows/it-pro/windows-2000-server/cc963220(v=technet.10)?f=255&MSPPError=-2147217396) フラグが有効になっていない場合、このイベントは一部の設定がベースライン設定に設定されていないか、変更されたことを示すサインとなります。
