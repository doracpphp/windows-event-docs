---
title: 4908(S) 特別グループのログオンテーブルが変更されました。
description: 特別グループのログオンテーブルが変更されたときに生成されるセキュリティイベント4908(S)について説明します。このイベントは、特別グループのログオンテーブルが変更されたときに生成されます。
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

# 4908(S): 特別グループのログオンテーブルが変更されました。

:::image type="content" source="images/event-4908.png" alt-text="イベント4908のイラスト":::

***サブカテゴリ:*** [監査ポリシーの変更](audit-audit-policy-change.md)

***イベントの説明:***

このイベントは、特別グループのログオンテーブルが変更されるたびに生成されます。

このイベントはシステムの起動時にも生成されます。

このイベントは、「監査ポリシーの変更」サブカテゴリの設定に関係なく常に記録されます。

特別グループの監査についての詳細は、[4908(S): 特別グループのログオンテーブルが変更されました](/windows/security/threat-protection/auditing/event-4908)を参照してください。

> [!NOTE]
> 推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***

```xml
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>4908</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>13568</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-10-01T00:20:40.210246600Z" /> 
 <EventRecordID>1049511</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="516" ThreadID="532" /> 
 <Channel>Security</Channel> 
 <Computer>DC01.contoso.local</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="SidList">%{S-1-5-21-3457937927-2839227994-823803824-512}</Data> 
 </EventData>
 </Event>

```

***必要なサーバー役割:*** なし。

***最小 OS バージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

***フィールドの説明:***

**特別グループ** \[型 = UnicodeString\]**:** 特別グループのメンバーであるSID（グループまたはアカウント）の現在のリストを含みます。イベントビューアーは自動的にSIDを解決し、アカウント名を表示しようとします。SIDが解決できない場合、イベントにはソースデータが表示されます。

> [!NOTE]
> **セキュリティ識別子 (SID)** は、トラスティ（セキュリティプリンシパル）を識別するために使用される可変長の一意の値です。各アカウントには、Active Directory ドメインコントローラーなどの権限によって発行され、セキュリティデータベースに保存される一意のSIDがあります。ユーザーがログオンするたびに、システムはデータベースからそのユーザーのSIDを取得し、そのユーザーのアクセストークンに配置します。システムはアクセストークン内のSIDを使用して、以降のすべてのWindowsセキュリティとのやり取りでユーザーを識別します。SIDがユーザーまたはグループの一意の識別子として使用された場合、それは他のユーザーまたはグループを識別するために再利用されることはありません。SIDについての詳細は、[セキュリティ識別子](/windows/access-protection/access-control/security-identifiers)を参照してください。

“HKEY\_LOCAL\_MACHINE\\SYSTEM\\ControlSet001\\Control\\Lsa\\Audit\\SpecialGroups” レジストリ値には、特別グループに含まれる現在のSIDのリストが含まれています:

:::image type="content" source="images/registry-editor-audit.png" alt-text="Registry Editor Audit key illustration":::

## セキュリティ監視の推奨事項

4908(S): 特別グループのログオンテーブルが変更されました。

- 特別グループ機能を使用している場合、このイベントは常に監視する必要があります。特に高価値の資産やコンピュータでは重要です。この変更が計画されていなかった場合、変更の理由を調査してください。

- 特別グループ機能を使用していない場合でも、このイベントは常に監視する必要があります。これは標準手順外で特別グループ機能が使用されていることを示しているためです。
