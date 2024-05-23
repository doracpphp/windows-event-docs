---
title: 4954(S) Windows ファイアウォール グループ ポリシー設定が変更されました。新しい設定が適用されました。
description: セキュリティ イベント 4954(S) Windows ファイアウォール グループ ポリシー設定が変更されました。新しい設定が適用されました。
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

# 4954(S): Windows ファイアウォール グループ ポリシー設定が変更されました。新しい設定が適用されました。


<img src="images/event-4954.png" alt="Event 4954 illustration" width="449" height="317" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[MPSSVC ルールレベル ポリシー変更の監査](audit-mpssvc-rule-level-policy-change.md)

***イベントの説明:***

このイベントは、Windows ファイアウォール グループ ポリシーがローカルまたは Active Directory グループ ポリシーから変更されるたびに生成されます。

このイベントは、Windows ファイアウォール設定が変更または提示されていなくても、ローカル グループ ポリシーが更新されるたびに生成されます。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***
```
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>4954</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>13571</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-10-02T23:13:14.527924800Z" /> 
 <EventRecordID>1049893</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="500" ThreadID="2284" /> 
 <Channel>Security</Channel> 
 <Computer>DC01.contoso.local</Computer> 
 <Security /> 
 </System>
 <EventData /> 
 </Event>

```

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

4954(S): Windows ファイアウォール グループ ポリシー設定が変更されました。新しい設定が適用されました。

-   残念ながら、このイベントはローカル グループ ポリシーが更新されるたびに生成され、設定が実際に変更されたことを示すものではありません。通常、このイベントは無視できます。
