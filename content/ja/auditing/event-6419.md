---
title: 6419(S) デバイスを無効にする要求が行われました。
description: セキュリティイベント 6419(S) デバイスを無効にする要求が行われましたについて説明します。
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

# 6419(S): デバイスを無効にする要求が行われました。

<img src="images/event-6419.png" alt="Event 6419 illustration" width="526" height="682" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[PNP アクティビティの監査](audit-pnp-activity.md)

***イベントの説明:***

このイベントは、誰かがデバイスを無効にする要求を行ったときに毎回生成されます。

このイベントは、デバイスが無効になったことを意味するものではありません。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***
```xml
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>6419</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>13316</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-11-14T22:23:26.789591400Z" /> 
 <EventRecordID>483</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="2192" ThreadID="1392" /> 
 <Channel>Security</Channel> 
 <Computer>DESKTOP-NFC0HVN</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="SubjectUserSid">S-1-5-21-2695983153-1310895815-1903476278-1001</Data> 
 <Data Name="SubjectUserName">ladmin</Data> 
 <Data Name="SubjectDomainName">DESKTOP-NFC0HVN</Data> 
 <Data Name="SubjectLogonId">0x3fcc7</Data> 
 <Data Name="DeviceId">USB\\VID\_138A&PID\_0017\\FFBC12C950A0</Data> 
 <Data Name="DeviceDescription">Synaptics FP Sensors (WBF) (PID=0017)</Data> 
 <Data Name="ClassId">{53D29EF7-377C-4D14-864B-EB3A85769359}</Data> 
 <Data Name="ClassName">Biometric</Data> 
 <Data Name="HardwareIds">USB\\VID\_138A&PID\_0017&REV\_0078 USB\\VID\_138A&PID\_0017</Data> 
 <Data Name="CompatibleIds">USB\\Class\_FF&SubClass\_00&Prot\_00 USB\\Class\_FF&SubClass\_00 USB\\Class\_FF</Data> 
 <Data Name="LocationInformation">Port\_\#0002.Hub\_\#0004</Data> 
 </EventData>
</Event>

```

***必要なサーバー役割:*** なし。

***最小 OS バージョン:*** Windows 10 \[バージョン 1511\]。

***イベントバージョン:*** 0。

***フィールドの説明:***

**サブジェクト:**

-   **セキュリティ ID** \[タイプ = SID\]**:** 要求を行ったアカウントの SID。イベントビューアーは自動的に SID を解決し、アカウント名を表示しようとします。SID を解決できない場合、イベントにソースデータが表示されます。

> **注**&nbsp;&nbsp;**セキュリティ識別子 (SID)** は、トラスティ (セキュリティプリンシパル) を識別するために使用される可変長の一意の値です。各アカウントには、Active Directory ドメインコントローラーなどの権限によって発行され、セキュリティデータベースに保存される一意の SID があります。ユーザーがログオンするたびに、システムはデータベースからそのユーザーの SID を取得し、そのユーザーのアクセス トークンに配置します。システムは、アクセス トークン内の SID を使用して、以降のすべての Windows セキュリティとのやり取りでユーザーを識別します。SID がユーザーまたはグループの一意の識別子として使用された場合、それは他のユーザーまたはグループを識別するために再び使用されることはありません。SID の詳細については、[セキュリティ識別子](/windows/access-protection/access-control/security-identifiers)を参照してください。

-   **アカウント名** \[タイプ = UnicodeString\]**:** リクエストを行ったアカウントの名前。

-   **アカウントドメイン** \[タイプ = UnicodeString\]**:** サブジェクトのドメインまたはコンピュータ名。形式は様々で、以下のようなものが含まれます：

    -   ドメインのNETBIOS名の例: CONTOSO

    -   小文字の完全なドメイン名: contoso.local

    -   大文字の完全なドメイン名: CONTOSO.LOCAL

    -   LOCAL SERVICEやANONYMOUS LOGONなどの[よく知られたセキュリティプリンシパル](/windows/security/identity-protection/access-control/security-identifiers)の場合、このフィールドの値は「NT AUTHORITY」となります。

    -   ローカルユーザーアカウントの場合、このフィールドにはこのアカウントが属するコンピュータまたはデバイスの名前が含まれます。例: “Win81”。

-   **ログオンID** \[タイプ = HexInt64\]**:** 16進数の値で、最近のイベントと同じログオンIDを含む可能性のあるイベントとこのイベントを関連付けるのに役立ちます。例: “[4624](event-4624.md): アカウントが正常にログオンされました。”

**デバイスID** \[タイプ = UnicodeString\]: デバイスの「**デバイスインスタンスパス**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics1.png" alt="デバイスプロパティのデバイスインスタンスパスのイラスト" width="557" height="316" />

**デバイス名** \[タイプ = UnicodeString\]: デバイスの「**デバイス説明**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics2.png" alt="デバイスプロパティのデバイス説明のイラスト" width="557" height="305" />

**クラスID** \[タイプ = UnicodeString\]: デバイスの「**クラスGuid**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics3.png" alt="デバイスプロパティのクラスGUIDのイラスト" width="557" height="300" />

**クラス名** \[タイプ = UnicodeString\]: デバイスの「**クラス**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics4.png" alt="Device Properties class illustration" width="557" height="298" />

**ハードウェアID** \[Type = UnicodeString\]: デバイスの“**Hardware Ids**”属性。デバイスのプロパティを表示するには、デバイスマネージャーを起動し、特定のデバイスのプロパティを開き、「詳細」タブをクリックします。

<img src="images/synaptics5.png" alt="Device Properties hardware IDs illustration" width="557" height="313" />

**互換性ID** \[Type = UnicodeString\]: デバイスの“**Compatible Ids**”属性。デバイスのプロパティを表示するには、デバイスマネージャーを起動し、特定のデバイスのプロパティを開き、「詳細」タブをクリックします。

<img src="images/synaptics6.png" alt="Device Properties compatible IDs illustration" width="557" height="337" />

**位置情報** \[Type = UnicodeString\]: デバイスの“**Location information**”属性。デバイスのプロパティを表示するには、デバイスマネージャーを起動し、特定のデバイスのプロパティを開き、「詳細」タブをクリックします。

<img src="images/synaptics7.png" alt="Device Properties location illustration" width="557" height="298" />

## セキュリティ監視の推奨事項

6419(S): デバイスを無効にする要求がありました。

> **重要**&nbsp;&nbsp;このイベントについては、[付録A: 多くの監査イベントに対するセキュリティ監視の推奨事項](appendix-a-security-monitoring-recommendations-for-many-audit-events.md)も参照してください。

-   このイベントを使用して、以下の表に示すイベントおよびイベント情報をリストされたフィールドを使用して追跡することができます。

| 監視するイベントおよびイベント情報            | 使用するフィールド         |
|---------------------------------------------------|----------------------------|
| デバイス無効化要求、**デバイスインスタンスパス** | “**Device ID**”            |
| デバイス無効化要求、**デバイス説明**             | “**Device Name**”          |
| デバイス無効化要求、**クラスGUID**               | “**Class ID**”             |
| デバイス無効化要求、**ハードウェアID**           | “**Hardware IDs**”         |
| デバイス無効化要求、**互換性ID**                 | “**Compatible IDs**”       |
| デバイス無効化要求、**位置情報**                 | “**Location Information**” |

It looks like you haven't pasted any Markdown content yet. Please provide the content you want translated, and I'll translate it into Japanese for you.
