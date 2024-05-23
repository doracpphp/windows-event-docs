---
title: 5024(S) Windows ファイアウォール サービスが正常に開始されました。
description: セキュリティ イベント 5024(S) Windows ファイアウォール サービスが正常に開始されました。について説明します。
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

# 5024(S): Windows ファイアウォール サービスが正常に開始されました。


<img src="images/event-5024.png" alt="Event 5024 illustration" width="449" height="317" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[その他のシステム イベントの監査](audit-other-system-events.md)

***イベントの説明:***

このイベントは、Windows ファイアウォール (MpsSvc) サービスが正常に開始されたときに生成されます。

このイベントは通常、オペレーティング システムの起動プロセス中に記録されます。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***
```xml
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>5024</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>12292</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-10-09T03:22:53.842816300Z" /> 
 <EventRecordID>1101613</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="500" ThreadID="528" /> 
 <Channel>Security</Channel> 
 <Computer>DC01.contoso.local</Computer> 
 <Security /> 
 </System>
 <EventData /> 
 </Event>

```

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008、Windows Vista。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

5024(S): Windows ファイアウォール サービスが正常に開始されました。

-   通常、このイベントは情報提供を目的としています。オペレーティング システムの起動プロセス中に記録されます。

-   システム起動後にこのイベントが表示されないはずなので、システム起動プロセス外で発生した場合に監視することをお勧めします。
