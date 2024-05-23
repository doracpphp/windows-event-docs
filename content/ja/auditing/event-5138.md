---
title: 5138(S) ディレクトリ サービス オブジェクトが復元されました。
description: セキュリティ イベント 5138(S) ディレクトリ サービス オブジェクトが復元されましたについて説明します。
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

# 5138(S): ディレクトリ サービス オブジェクトが復元されました。

<img src="images/event-5138.png" alt="Event 5138 illustration" width="671" height="573" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[ディレクトリ サービスの変更の監査](audit-directory-service-changes.md)

***イベントの説明:***

このイベントは、Active Directory オブジェクトが復元されるたびに生成されます。たとえば、[Active Directory ごみ箱](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd392261(v=ws.10))から Active Directory オブジェクトが復元された場合に発生します。

このイベントは、Active Directory オブジェクトが復元されたコンテナーに特定のエントリが [SACL](/windows/win32/secauthz/access-control-lists) に含まれている場合にのみ生成されます。たとえば、「**ユーザー オブジェクトの作成**」アクションなど、特定のクラスまたはオブジェクトの監査の「**作成**」アクションです。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***
```
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>5138</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>14081</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-09-02T04:34:20.611082300Z" /> 
 <EventRecordID>229336</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="516" ThreadID="544" /> 
 <Channel>Security</Channel> 
 <Computer>DC01.contoso.local</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="OpCorrelationID">{3E2B5ECF-4C35-4C3F-8D82-B8D6F477D846}</Data> 
 <Data Name="AppCorrelationID">-</Data> 
 <Data Name="SubjectUserSid">S-1-5-21-3457937927-2839227994-823803824-1104</Data> 
 <Data Name="SubjectUserName">dadmin</Data> 
 <Data Name="SubjectDomainName">CONTOSO</Data> 
 <Data Name="SubjectLogonId">0x3be49</Data> 
 <Data Name="DSName">contoso.local</Data> 
 <Data Name="DSType">%%14676</Data> 
 <Data Name="OldObjectDN">CN=Andrei\\0ADEL:53511188-bc98-4995-9d78-2d40143c9711,CN=Deleted Objects,DC=contoso,DC=local</Data> 
 <Data Name="NewObjectDN">CN=Andrei,CN=Users,DC=contoso,DC=local</Data> 
 <Data Name="ObjectGUID">{53511188-BC98-4995-9D78-2D40143C9711}</Data> 
 <Data Name="ObjectClass">user</Data> 
 </EventData>
 </Event>
```

***必要なサーバー ロール:*** Active Directory ドメイン コントローラー。

***最小 OS バージョン:*** Windows Server 2008。

***イベント バージョン:*** 0。

***フィールドの説明:***

**サブジェクト:**

-   **セキュリティ ID** \[タイプ = SID\]**:** オブジェクトの復元または復元を要求したアカウントの SID。イベント ビューアーは自動的に SID を解決してアカウント名を表示しようとします。SID を解決できない場合は、イベントにソース データが表示されます。

> **注**&nbsp;&nbsp;**セキュリティ識別子 (SID)** は、トラスティ (セキュリティ プリンシパル) を識別するために使用される可変長の一意の値です。各アカウントには、Active Directory ドメイン コントローラーなどの権限によって発行され、セキュリティ データベースに格納される一意の SID があります。ユーザーがログオンするたびに、システムはデータベースからそのユーザーの SID を取得し、そのユーザーのアクセス トークンに配置します。システムは、アクセス トークン内の SID を使用して、以降のすべての Windows セキュリティとのやり取りでユーザーを識別します。SID がユーザーまたはグループの一意の識別子として使用された場合、それは他のユーザーまたはグループを識別するために再利用されることはありません。SID の詳細については、[セキュリティ識別子](/windows/access-protection/access-control/security-identifiers)を参照してください。

-   **アカウント名** \[タイプ = UnicodeString\]**:** オブジェクトの削除取り消しまたは復元を要求したアカウントの名前。

-   **アカウントドメイン** \[タイプ = UnicodeString\]**:** サブジェクトのドメインまたはコンピュータ名。形式はさまざまで、以下のものが含まれます：

    -   ドメイン NETBIOS 名の例: CONTOSO

    -   小文字の完全なドメイン名: contoso.local

    -   大文字の完全なドメイン名: CONTOSO.LOCAL

    -   一部の[よく知られたセキュリティプリンシパル](/windows/security/identity-protection/access-control/security-identifiers)の場合、例えば LOCAL SERVICE や ANONYMOUS LOGON、このフィールドの値は「NT AUTHORITY」となります。

    -   ローカルユーザーアカウントの場合、このフィールドにはこのアカウントが属するコンピュータまたはデバイスの名前が含まれます。例えば「Win81」。

-   **ログオンID** \[タイプ = HexInt64\]**:** 16進数の値で、同じログオンIDを含む最近のイベントとこのイベントを関連付けるのに役立ちます。例えば、「[4624](event-4624.md): アカウントが正常にログオンされました。」

**ディレクトリサービス:**

-   **名前** \[タイプ = UnicodeString\]: オブジェクトが削除取り消しされたActive Directoryドメインの名前。

-   **タイプ** \[タイプ = UnicodeString\]**:** このイベントの値は「**Active Directory Domain Services**」です。

**オブジェクト:**

-   **旧DN** \[タイプ = UnicodeString\]: 削除取り消しされたオブジェクトの旧識別名。Active Directoryのごみ箱から復元された場合、このフォルダーを指します。[Active Directory Recycle Bin](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd392261(v=ws.10))。

> **注**&nbsp;&nbsp;LDAP APIはLDAPオブジェクトを**識別名 (DN)**で参照します。DNは相対識別名 (RDN) のシーケンスで、カンマで接続されています。
> 
> RDNは属性とその値の形式 attribute=value; で構成されます。以下はRDN属性の例です：
> 
> • DC - domainComponent
> 
> • CN - commonName
> 
> • OU - organizationalUnitName
> 
> • O - organizationName

-   **新DN** \[タイプ = UnicodeString\]: 削除取り消しされたオブジェクトの新しい識別名。オブジェクトが復元されたActive Directoryコンテナ。

-   **GUID** \[Type = GUID\]**:** 各Active Directoryオブジェクトには、エンタープライズ内だけでなく世界中で一意の128ビット値であるグローバル一意識別子 (GUID) が割り当てられています。GUIDはActive Directoryによって作成されたすべてのオブジェクトに割り当てられます。各オブジェクトのGUIDは、そのObject-GUID (**objectGUID**) プロパティに格納されます。

    Active Directoryは内部的にオブジェクトを識別するためにGUIDを使用します。例えば、GUIDはグローバルカタログに公開されるオブジェクトのプロパティの一つです。ユーザーオブジェクトのGUIDをグローバルカタログで検索すると、そのユーザーがエンタープライズ内のどこかにアカウントを持っている場合に結果が得られます。実際、Object-GUIDでオブジェクトを検索することは、探しているオブジェクトを見つける最も信頼性の高い方法かもしれません。他のオブジェクトプロパティの値は変更される可能性がありますが、Object-GUIDは決して変更されません。オブジェクトにGUIDが割り当てられると、その値は生涯保持されます。

    イベントビューアーは自動的に**GUID**フィールドを実際のオブジェクトに解決します。

    このGUIDを翻訳するには、次の手順を使用します：

    -   LDP.exeツールを使用して次のLDAP検索を実行します：

        -   ベースDN: CN=Schema,CN=Configuration,DC=XXX,DC=XXX

        -   フィルター: (&(objectClass=\*)(objectGUID=GUID))

            -   検索リクエストで使用する前に、GUIDに対して次の操作を行います：

                -   検索するGUIDは次の通りです: a6b34ab5-551b-4626-b8ee-2b36b3ee6672

                -   最初の3つのセクションを取り出します: a6b34ab5-551b-4626

                -   これら3つのセクションの各バイトの順序を変更します（反転します）: b54ab3a6-1b55-2646

                -   最後の2つのセクションは変換せずに追加します: b54ab3a6-1b55-2646-b8ee-2b36b3ee6672

                -   削除します: b54ab3a61b552646b8ee2b36b3ee6672

                -   バイトをバックスラッシュで区切ります: \\b5\\4a\\b3\\a6\\1b\\55\\26\\46\\b8\\ee\\2b\\36\\b3\\ee\\66\\72

            -   フィルターの例: (&(objectClass=\*)(objectGUID = \\b5\\4a\\b3\\a6\\1b\\55\\26\\46\\b8\\ee\\2b\\36\\b3\\ee\\66\\72))

        -   スコープ: サブツリー

        -   属性: objectGUID

-   **クラス** \[タイプ = UnicodeString\]: 復元されたオブジェクトのクラス。一般的なActive Directoryオブジェクトクラスの例:

    -   container – コンテナ用。

    -   user – ユーザー用。

    -   group – グループ用。

    -   domainDNS – ドメインオブジェクト用。

    -   groupPolicyContainer – グループポリシーオブジェクト用。

        このフィールドのすべての可能な値については、Active Directoryスキーマスナップインを開きます（このスナップインを有効にする方法については、<https://technet.microsoft.com/library/Cc755885(v=WS.10).aspx>を参照）し、**Active Directoryスキーマ\\クラス**に移動します。または、このドキュメントを使用します: <https://msdn.microsoft.com/library/cc221630.aspx>

**操作:**

-   **相関ID** \[タイプ = GUID\]: 複数の変更がLDAPを介して1つの操作として実行されることがよくあります。この値により、操作を構成するすべての変更イベントを相関させることができます。同じ**相関ID**を持つ現在のサブカテゴリの他のイベントを探します。例えば、「[5137](event-5137.md): ディレクトリサービスオブジェクトが作成されました。」および「[5139](event-5139.md): ディレクトリサービスオブジェクトが移動されました。」などです。

> **注**&nbsp;&nbsp;**GUID**は「Globally Unique Identifier」の略です。リソース、アクティビティ、またはインスタンスを識別するために使用される128ビットの整数です。

-   **アプリケーション相関ID** \[タイプ = UnicodeString\]: 常に「**-**」の値を持ちます。使用されていません。

## セキュリティ監視の推奨事項

5138(S): ディレクトリサービスオブジェクトが復元されました。

> **重要**&nbsp;&nbsp;このイベントについては、[付録A: 多くの監査イベントのセキュリティ監視の推奨事項](appendix-a-security-monitoring-recommendations-for-many-audit-events.md)も参照してください。

-   特定のクラスを持つActive Directoryオブジェクトの復元操作（復元）を監視する必要がある場合は、特定のクラス名を持つ**クラス**フィールドを監視します。

-   復元イベントは頻繁に実行されないため、すべての復元イベントを監視することをお勧めします。オブジェクトが復元される理由があることを確認します。
