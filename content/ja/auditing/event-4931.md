---
title: 4931(S, F) Active Directory レプリカの宛先命名コンテキストが変更されました。
description: セキュリティ イベント 4931(S, F) Active Directory レプリカの宛先命名コンテキストが変更されました。
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

# 4931(S, F): Active Directory レプリカの宛先命名コンテキストが変更されました。

<img src="images/event-4931.png" alt="Event 4931 illustration" width="500" height="374" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[詳細なディレクトリ サービス レプリケーションの監査](audit-detailed-directory-service-replication.md)

***イベントの説明:***

このイベントは、Active Directory レプリカの宛先命名コンテキストが変更されるたびに生成されます。

エラーが発生した場合 (**ステータス コード** != 0)、失敗イベントが生成されます。

このイベントから何が正確に変更されたかを理解することはできません。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***
```xml
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>4931</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>14083</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-08-27T19:02:41.563619400Z" /> 
 <EventRecordID>227058</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="524" ThreadID="2936" /> 
 <Channel>Security</Channel> 
 <Computer>DC01.contoso.local</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="DestinationDRA">ddec0cff-6ceb-4a59-b13f-1724c38a0970.\_msdcs.contoso.local</Data> 
 <Data Name="SourceDRA">CN=NTDS Settings,CN=DC01,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=contoso,DC=local</Data> 
 <Data Name="SourceAddr">-</Data> 
 <Data Name="NamingContext">DC=ForestDnsZones,DC=contoso,DC=local</Data> 
 <Data Name="Options">23</Data> 
 <Data Name="StatusCode">0</Data> 
 </EventData>
 </Event>
```

***必要なサーバー ロール:*** Active Directory ドメイン コントローラー。

***最小 OS バージョン:*** Windows Server 2008。

***イベント バージョン:*** 0。

***フィールドの説明:***

-   **宛先 DRA** \[タイプ = UnicodeString\]: 宛先ディレクトリ レプリケーション エージェントの識別名。

> **注**&nbsp;&nbsp;**ディレクトリ レプリケーション エージェント (DRA)** は、ドメイン コントローラー間のレプリケーションを処理します。ディレクトリ レプリケーション エージェントは、トポロジ マップ内の接続オブジェクトを使用して、ディレクトリ パーティションの変更をレプリケートする際に関連するパートナーを見つけます。DRA は、ドメイン コントローラーが Active Directory のコピーを更新する必要があるときに、ドメイン コントローラーのパートナーにレプリケーション要求を送信します。

-   **ソース DRA** \[タイプ = UnicodeString\]: ソースディレクトリ レプリケーション エージェントの識別名。

> **注**&nbsp;&nbsp;LDAP API は、LDAP オブジェクトをその**識別名 (DN)** で参照します。DN は、カンマで接続された相対識別名 (RDN) のシーケンスです。
> 
> RDN は、属性=値の形式で関連付けられた値を持つ属性です。これらは RDN 属性の例です:
> 
> • DC - domainComponent
> 
> • CN - commonName
> 
> • OU - organizationalUnitName
> 
> • O - organizationName

-   **送信先アドレス** \[タイプ = UnicodeString\]: 変更要求が送信されたコンピュータのDNSレコード。

-   **命名コンテキスト** \[タイプ = UnicodeString\]**:** 変更された命名コンテキスト。

> **注**&nbsp;&nbsp;Active Directoryツリーのディレクトリツリーは、セクションを分割してフォレスト内の異なるドメインコントローラーに分配（レプリケート）できるようにパーティション化されています。各ドメインコントローラーは、**命名コンテキスト**（ディレクトリパーティションとも呼ばれる）と呼ばれるディレクトリツリーの特定の部分のコピーを保存します。**命名コンテキスト**は、同じサブツリーのレプリカを含むフォレスト内の他のドメインコントローラーにユニットとしてレプリケートされます。**命名コンテキスト**はディレクトリパーティションとも呼ばれます。

-   **オプション** \[タイプ = UInt32\]: [DRSオプション](/openspecs/windows_protocols/ms-drsr/ac9c8a11-cd46-4080-acbf-9faa86344030)の10進値。

-   **ステータスコード** \[タイプ = UInt32\]**:** 問題やエラーがない場合、ステータスコードは0になります。エラーが発生した場合、失敗イベントが発生し、ステータスコードは「**0**」と等しくなりません。エラーコードの意味はここで確認できます: <https://msdn.microsoft.com/library/windows/desktop/ms681381(v=vs.85).aspx>

## セキュリティ監視の推奨事項

4931(S, F): Active Directoryレプリカの送信先命名コンテキストが変更されました。

-   このイベントは通常、Active Directoryレプリケーションのトラブルシューティングに使用されます。
