---
title: 6420(S) デバイスが無効化されました。
description: 特定のデバイスが無効化されたときに生成されるセキュリティイベント6420(S)について説明します。
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

# 6420(S): デバイスが無効化されました。

<img src="images/event-6420.png" alt="イベント6420のイラスト" width="526" height="682" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[PNPアクティビティの監査](audit-pnp-activity.md)

***イベントの説明:***

このイベントは、特定のデバイスが無効化されるたびに生成されます。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベントXML:***
```
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>6420</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>13316</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-11-14T22:23:29.137398300Z" /> 
 <EventRecordID>484</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="4" ThreadID="88" /> 
 <Channel>Security</Channel> 
 <Computer>DESKTOP-NFC0HVN</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="SubjectUserSid">S-1-5-18</Data> 
 <Data Name="SubjectUserName">DESKTOP-NFC0HVN$</Data> 
 <Data Name="SubjectDomainName">WORKGROUP</Data> 
 <Data Name="SubjectLogonId">0x3e7</Data> 
 <Data Name="DeviceId">USB\\VID\_138A&PID\_0017\\ffbc12c950a0</Data> 
 <Data Name="DeviceDescription">Synaptics FP Sensors (WBF) (PID=0017)</Data> 
 <Data Name="ClassId">{53D29EF7-377C-4D14-864B-EB3A85769359}</Data> 
 <Data Name="ClassName">Biometric</Data> 
 <Data Name="HardwareIds">USB\\VID\_138A&PID\_0017&REV\_0078 USB\\VID\_138A&PID\_0017</Data> 
 <Data Name="CompatibleIds">USB\\Class\_FF&SubClass\_00&Prot\_00 USB\\Class\_FF&SubClass\_00 USB\\Class\_FF</Data> 
 <Data Name="LocationInformation">Port\_\#0002.Hub\_\#0004</Data> 
 </EventData>
</Event>

```

***必要なサーバーロール:*** なし。

***最小OSバージョン:*** Windows 10 \[バージョン1511\]。

***イベントバージョン:*** 0。

***フィールドの説明:***

**サブジェクト:**

-   **セキュリティID** \[タイプ = SID\]**:** デバイスを無効化したアカウントのSID。イベントビューアーは自動的にSIDを解決し、アカウント名を表示しようとします。SIDが解決できない場合、イベントにはソースデータが表示されます。

> **注**&nbsp;&nbsp;**セキュリティ識別子 (SID)** は、トラスティ（セキュリティプリンシパル）を識別するために使用される可変長の一意の値です。各アカウントには、Active Directoryドメインコントローラーなどの権限によって発行され、セキュリティデータベースに保存される一意のSIDがあります。ユーザーがログオンするたびに、システムはデータベースからそのユーザーのSIDを取得し、そのユーザーのアクセス トークンに配置します。システムは、アクセス トークン内のSIDを使用して、以降のすべてのWindowsセキュリティとのやり取りでユーザーを識別します。SIDがユーザーまたはグループの一意の識別子として使用された場合、それは他のユーザーまたはグループを識別するために再利用されることはありません。SIDの詳細については、[セキュリティ識別子](/windows/access-protection/access-control/security-identifiers)を参照してください。

-   **アカウント名** \[タイプ = UnicodeString\]**:** デバイスを無効にしたアカウントの名前。

-   **アカウントドメイン** \[タイプ = UnicodeString\]**:** サブジェクトのドメインまたはコンピュータ名。形式はさまざまで、以下のようなものがあります：

    -   ドメインのNETBIOS名の例: CONTOSO

    -   小文字の完全なドメイン名: contoso.local

    -   大文字の完全なドメイン名: CONTOSO.LOCAL

    -   LOCAL SERVICEやANONYMOUS LOGONなどの[よく知られたセキュリティプリンシパル](/windows/security/identity-protection/access-control/security-identifiers)の場合、このフィールドの値は「NT AUTHORITY」となります。

    -   ローカルユーザーアカウントの場合、このフィールドにはこのアカウントが属するコンピュータまたはデバイスの名前が含まれます。例: “Win81”。

-   **ログオンID** \[タイプ = HexInt64\]**:** 16進数の値で、最近のイベントと同じログオンIDを含む可能性のあるこのイベントを関連付けるのに役立ちます。例: “[4624](event-4624.md): アカウントが正常にログオンされました。”

**デバイスID** \[タイプ = UnicodeString\]: デバイスの「**デバイスインスタンスパス**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics1.png" alt="デバイスプロパティのデバイスインスタンスパスのイラスト" width="557" height="316" />

**デバイス名** \[タイプ = UnicodeString\]: デバイスの「**デバイス説明**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics2.png" alt="デバイスプロパティのデバイス説明のイラスト" width="557" height="305" />

**クラスID** \[タイプ = UnicodeString\]: デバイスの「**クラスGuid**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics3.png" alt="デバイスプロパティのクラスGUIDのイラスト" width="557" height="300" />

**クラス名** \[タイプ = UnicodeString\]: デバイスの「**クラス**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」をクリックします：

<img src="images/synaptics4.png" alt="Device Properties class illustration" width="557" height="298" />

**ハードウェアID** \[タイプ = UnicodeString\]: デバイスの「**ハードウェアID**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」タブをクリックします。

<img src="images/synaptics5.png" alt="Device Properties hardware IDs illustration" width="557" height="313" />

**互換性ID** \[タイプ = UnicodeString\]: デバイスの「**互換性ID**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」タブをクリックします。

<img src="images/synaptics6.png" alt="Device Properties compatible IDs illustration" width="557" height="337" />

**場所情報** \[タイプ = UnicodeString\]: デバイスの「**場所情報**」属性。デバイスのプロパティを表示するには、デバイスマネージャを起動し、特定のデバイスのプロパティを開き、「詳細」タブをクリックします。

<img src="images/synaptics7.png" alt="Device Properties location illustration" width="557" height="298" />

## セキュリティ監視の推奨事項

6420(S): デバイスが無効になりました。

> **重要**&nbsp;&nbsp;このイベントについては、[付録A: 多くの監査イベントのためのセキュリティ監視の推奨事項](appendix-a-security-monitoring-recommendations-for-many-audit-events.md)も参照してください。

-   このイベントを使用して、以下の表に示すイベントおよびイベント情報をリストされたフィールドを使用して追跡できます。

| 監視するイベントおよびイベント情報          | 使用するフィールド         |
|-------------------------------------------------|----------------------------|
| デバイス無効化イベント、**デバイスインスタンスパス** | 「**デバイスID**」            |
| デバイス無効化イベント、**デバイス説明**   | 「**デバイス名**」          |
| デバイス無効化イベント、**クラスGUID**           | 「**クラスID**」             |
| デバイス無効化イベント、**ハードウェアID**         | 「**ハードウェアID**」         |
| デバイス無効化イベント、**互換性ID**       | 「**互換性ID**」       |
| デバイス無効化イベント、**場所情報** | 「**場所情報**」 |

It looks like you haven't pasted the Markdown content yet. Please provide the content you want translated into Japanese.
