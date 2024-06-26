---
title: 4751(S) セキュリティ無効のグローバル グループにメンバーが追加されました。
description: セキュリティ イベント 4751(S) セキュリティ無効のグローバル グループにメンバーが追加されました。
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

# 4751(S): セキュリティ無効のグローバル グループにメンバーが追加されました。

<img src="images/event-4751.png" alt="Event 4751 illustration" width="449" height="530" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[配布グループ管理の監査](audit-distribution-group-management.md)

***イベントの説明:***

このイベントは、新しいメンバーがセキュリティ無効（配布）グローバル グループに追加されるたびに生成されます。

このイベントはドメイン コントローラーでのみ生成されます。

追加されたメンバーごとに、別々の 4751 イベントが生成されます。

通常、4751 イベントの前に変更のない「[4750](event-4750.md): セキュリティ無効のグローバル グループが変更されました。」イベントが表示されます。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***
```xml
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>4751</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>13827</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-08-15T00:01:10.821144700Z" /> 
 <EventRecordID>172221</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="520" ThreadID="1108" /> 
 <Channel>Security</Channel> 
 <Computer>DC01.contoso.local</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="MemberName">CN=Auditor,CN=Users,DC=contoso,DC=local</Data> 
 <Data Name="MemberSid">S-1-5-21-3457937927-2839227994-823803824-2104</Data> 
 <Data Name="TargetUserName">ServiceDeskSecond</Data> 
 <Data Name="TargetDomainName">CONTOSO</Data> 
 <Data Name="TargetSid">S-1-5-21-3457937927-2839227994-823803824-6119</Data> 
 <Data Name="SubjectUserSid">S-1-5-21-3457937927-2839227994-823803824-1104</Data> 
 <Data Name="SubjectUserName">dadmin</Data> 
 <Data Name="SubjectDomainName">CONTOSO</Data> 
 <Data Name="SubjectLogonId">0x3007b</Data> 
 <Data Name="PrivilegeList">-</Data> 
 </EventData>
 </Event>
```

***必要なサーバー ロール:*** Active Directory ドメイン コントローラー。

***最小 OS バージョン:*** Windows Server 2008。

***イベント バージョン:*** 0。

***フィールドの説明:***

**サブジェクト:**

-   **セキュリティ ID** \[タイプ = SID\]**:** 「グループへのメンバー追加」操作を要求したアカウントの SID。イベント ビューアーは自動的に SID を解決し、アカウント名を表示しようとします。SID を解決できない場合、イベントにソース データが表示されます。

> **注**&nbsp;&nbsp;**セキュリティ識別子 (SID)** は、トラスティ (セキュリティ プリンシパル) を識別するために使用される可変長の一意の値です。各アカウントには、Active Directory ドメイン コントローラーなどの権限によって発行され、セキュリティ データベースに保存される一意の SID があります。ユーザーがログオンするたびに、システムはデータベースからそのユーザーの SID を取得し、そのユーザーのアクセス トークンに配置します。システムは、アクセス トークン内の SID を使用して、以降のすべての Windows セキュリティとのやり取りでユーザーを識別します。ユーザーまたはグループの一意の識別子として SID が使用された場合、それが再び別のユーザーまたはグループを識別するために使用されることはありません。SID の詳細については、[セキュリティ識別子](/windows/access-protection/access-control/security-identifiers)を参照してください。

-   **アカウント名** \[タイプ = UnicodeString\]**:** 「グループにメンバーを追加」操作を要求したアカウントの名前。

<!-- -->

-   **アカウントドメイン** \[タイプ = UnicodeString\]**:** サブジェクトのドメイン名。形式はさまざまで、以下を含みます：

    -   ドメイン NETBIOS 名の例: CONTOSO

    -   小文字の完全ドメイン名: contoso.local

    -   大文字の完全ドメイン名: CONTOSO.LOCAL

    <!-- -->

    -   LOCAL SERVICE や ANONYMOUS LOGON などの[よく知られたセキュリティプリンシパル](/windows/security/identity-protection/access-control/security-identifiers)の場合、このフィールドの値は「NT AUTHORITY」となります。

<!-- -->

-   **ログオンID** \[タイプ = HexInt64\]**:** 16進数の値で、同じログオンIDを含む最近のイベントとこのイベントを関連付けるのに役立ちます。例えば、「[4624](event-4624.md): アカウントが正常にログオンされました。」

**メンバー:**

-   **セキュリティID** \[タイプ = SID\]**:** グループに追加されたアカウントのSID。イベントビューアーは自動的にSIDを解決し、グループ名を表示しようとします。SIDが解決できない場合、イベントにソースデータが表示されます。

-   **アカウント名** \[タイプ = UnicodeString\]: グループに追加されたアカウントの識別名。例えば、「CN=Auditor,CN=Users,DC=contoso,DC=local」。LOCAL SERVICE や ANONYMOUS LOGON などの[よく知られたセキュリティプリンシパル](/windows/security/identity-protection/access-control/security-identifiers)の場合、このフィールドの値は「-」となります。

> **注**&nbsp;&nbsp;LDAP API は LDAP オブジェクトをその**識別名 (DN)** で参照します。DN はカンマで接続された相対識別名 (RDN) のシーケンスです。
> 
> RDN は属性とその値の形式 attribute=value; で構成されます。以下は RDN 属性の例です：
> 
> • DC - domainComponent
> 
> • CN - commonName
> 
> • OU - organizationalUnitName
> 
> • O - organizationName

**グループ:**

-   **セキュリティID** \[タイプ = SID\]**:** 新しいメンバーが追加されたグループのSID。イベントビューアーは自動的にSIDを解決し、グループ名を表示しようとします。SIDが解決できない場合、イベントにソースデータが表示されます。

-   **グループ名** \[タイプ = UnicodeString\]**:** 新しいメンバーが追加されたグループの名前。例: ServiceDesk

<!-- -->

-   **グループドメイン** \[タイプ = UnicodeString\]**:** 新しいメンバーが追加されたグループのドメイン名。形式は様々で、以下のようなものがあります:

    -   ドメイン NETBIOS 名の例: CONTOSO

    -   小文字の完全ドメイン名: contoso.local

    -   大文字の完全ドメイン名: CONTOSO.LOCAL

    -   [組み込みグループ](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dn169025(v=ws.10)): Builtin

**追加情報:**

-   **特権** \[タイプ = UnicodeString\]: 操作中に使用されたユーザー特権のリスト。例: SeBackupPrivilege。このパラメータはイベントにキャプチャされない場合があり、その場合は「-」と表示されます。ユーザー特権の完全なリストは「表8. ユーザー特権」を参照してください。

## セキュリティ監視の推奨事項

4751(S): セキュリティ無効のグローバルグループにメンバーが追加されました。

| **必要な監視の種類**                                                                                                                                                                                                                                                                                   | **推奨事項**                                                                                                                                                                                                                |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **配布グループへのメンバー追加:** 配布グループへのメンバー追加を監視する必要があるかもしれません。                                                                                                                                                                                         | 配布グループにメンバーが追加されるたびに、誰がいつメンバーを追加したかを確認する必要がある場合、このイベントを監視してください。<br>通常、このイベントは情報提供のためのイベントとして使用され、必要に応じてレビューされます。 |
| **高価値の配布グループ:** 組織内の重要な配布グループのリストがあり、新しいメンバーの追加（またはその他の変更）を特に監視する必要があるかもしれません。                                                                                              | 高価値の配布グループに対応する「**グループ\\グループ名**」の値でこのイベントを監視してください。                                                                                                                 |
| **高価値のアカウント**: ドメインまたはローカルの高価値アカウントについて、各アクションを監視する必要があるかもしれません。<br>高価値のアカウントの例としては、データベース管理者、組み込みのローカル管理者アカウント、ドメイン管理者、サービスアカウント、ドメインコントローラーアカウントなどがあります。 | 高価値のアカウントに対応する**「サブジェクト\\セキュリティID」**および**「メンバー\\セキュリティID」**でこのイベントを監視してください。                                                                                       |
| **異常または悪意のある行動**: 異常を検出したり、潜在的な悪意のある行動を監視するための特定の要件があるかもしれません。例えば、勤務時間外のアカウント使用を監視する必要があるかもしれません。                                                                                | 異常または悪意のある行動を監視する場合、**「サブジェクト\\セキュリティID」**（およびその他の情報）を使用して特定のアカウントがどのように、またはいつ使用されているかを監視してください。                                                       |
| **非アクティブアカウント**: 非アクティブ、無効、またはゲストアカウント、その他使用されるべきでないアカウントがあるかもしれません。                                                                                                                                                                                     | 使用されるべきでないアカウントに対応する**「サブジェクト\\セキュリティID」**および**「メンバー\\セキュリティID」**でこのイベントを監視してください。                                                                                   |
| **アカウントの許可リスト**: 特定のイベントに対応するアクションを実行することが許可されているアカウントの特定の許可リストがあるかもしれません。                                                                                                                                                      | このイベントが「許可リストのみ」のアクションに対応する場合、許可リスト外のアカウントについて**「サブジェクト\\セキュリティID」**を確認してください。                                                                                        |
| **異なる種類のアカウント**: 特定のアクションが特定のアカウントタイプ（例: ローカルまたはドメインアカウント、マシンまたはユーザーアカウント、ベンダーまたは従業員アカウントなど）によってのみ実行されることを確認したいかもしれません。                                                                                 | このイベントが特定のアカウントタイプに対して監視したいアクションに対応する場合、**「サブジェクト\\セキュリティID」**を確認してアカウントタイプが期待通りであるかどうかを確認してください。                                                       |
| **外部アカウント**: 別のドメインからのアカウントや、特定のアクション（特定のイベントで表される）を実行することが許可されていない「外部」アカウントを監視しているかもしれません。                                                                                                                     | 別のドメインからのアカウントや「外部」アカウントに対応する**「サブジェクト\\アカウントドメイン」**についてこのイベントを監視してください。                                                                                                    |
| **使用制限のあるコンピュータやデバイス**: 特定の人（アカウント）が通常はアクションを実行すべきでない特定のコンピュータ、マシン、デバイスがあるかもしれません。                                                                                                                                      | 関心のある**「サブジェクト\\セキュリティID」**によって実行されたアクションについて、対象の**コンピュータ:**（または他の対象デバイス）を監視してください。                                                                                   |
| **アカウント命名規則**: 組織にはアカウント名の特定の命名規則があるかもしれません。                                                                                                                                                                                                       | 命名規則に従わない名前について「**サブジェクト\\アカウント名**」を監視してください。                                                                                                                                          |
