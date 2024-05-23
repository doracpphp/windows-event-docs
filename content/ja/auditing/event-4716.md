---
title: 4716(S) 信頼されたドメイン情報が変更されました。
description: セキュリティイベント 4716(S) 信頼されたドメイン情報が変更されましたについて説明します。
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

# 4716(S): 信頼されたドメイン情報が変更されました。

<img src="images/event-4716.png" alt="Event 4716 illustration" width="449" height="489" hspace="10" align="left" />

***サブカテゴリ:***&nbsp;[認証ポリシー変更の監査](audit-authentication-policy-change.md)

***イベントの説明:***

このイベントは、信頼が変更されたときに生成されます。

このイベントはドメインコントローラーでのみ生成されます。

> **注**&nbsp;&nbsp;推奨事項については、このイベントの[セキュリティ監視の推奨事項](#security-monitoring-recommendations)を参照してください。

<br clear="all">

***イベント XML:***
```xml
- <Event xmlns="http://schemas.microsoft.com/win/2004/08/events/event">
- <System>
 <Provider Name="Microsoft-Windows-Security-Auditing" Guid="{54849625-5478-4994-A5BA-3E3B0328C30D}" /> 
 <EventID>4716</EventID> 
 <Version>0</Version> 
 <Level>0</Level> 
 <Task>13569</Task> 
 <Opcode>0</Opcode> 
 <Keywords>0x8020000000000000</Keywords> 
 <TimeCreated SystemTime="2015-10-01T22:55:54.560735500Z" /> 
 <EventRecordID>1049763</EventRecordID> 
 <Correlation /> 
 <Execution ProcessID="500" ThreadID="4920" /> 
 <Channel>Security</Channel> 
 <Computer>DC01.contoso.local</Computer> 
 <Security /> 
 </System>
- <EventData>
 <Data Name="SubjectUserSid">S-1-5-21-3457937927-2839227994-823803824-1104</Data> 
 <Data Name="SubjectUserName">dadmin</Data> 
 <Data Name="SubjectDomainName">CONTOSO</Data> 
 <Data Name="SubjectLogonId">0x138eb0</Data> 
 <Data Name="DomainName">-</Data> 
 <Data Name="DomainSid">S-1-5-21-2226861337-2836268956-2433141405</Data> 
 <Data Name="TdoType">2</Data> 
 <Data Name="TdoDirection">3</Data> 
 <Data Name="TdoAttributes">32</Data> 
 <Data Name="SidFilteringEnabled">-</Data> 
 </EventData>
 </Event>

```

***必要なサーバー役割:*** Active Directory ドメインコントローラー。

***最小 OS バージョン:*** Windows Server 2008。

***イベントバージョン:*** 0。

***フィールドの説明:***

**サブジェクト:**

-   **セキュリティ ID** \[タイプ = SID\]**:** 「ドメイン信頼設定の変更」操作を要求したアカウントの SID。イベントビューアーは自動的に SID を解決し、アカウント名を表示しようとします。SID を解決できない場合、イベントにソースデータが表示されます。

> **注**&nbsp;&nbsp;**セキュリティ識別子 (SID)** は、トラスティ (セキュリティプリンシパル) を識別するために使用される可変長の一意の値です。各アカウントには、Active Directory ドメインコントローラーなどの権限によって発行され、セキュリティデータベースに保存される一意の SID があります。ユーザーがログオンするたびに、システムはデータベースからそのユーザーの SID を取得し、そのユーザーのアクセス トークンに配置します。システムは、アクセス トークン内の SID を使用して、以降のすべての Windows セキュリティとのやり取りでユーザーを識別します。SID がユーザーまたはグループの一意の識別子として使用された場合、それは他のユーザーまたはグループを識別するために再利用されることはありません。SID の詳細については、[セキュリティ識別子](/windows/access-protection/access-control/security-identifiers)を参照してください。

- **アカウント名** \[タイプ = UnicodeString\]**:** 「ドメイン信頼設定の変更」操作を要求したアカウントの名前。

- **アカウントドメイン** \[タイプ = UnicodeString\]**:** サブジェクトのドメインまたはコンピュータ名。形式は以下のように異なります：

    - ドメイン NETBIOS 名の例: CONTOSO

    - 小文字の完全ドメイン名: contoso.local

    - 大文字の完全ドメイン名: CONTOSO.LOCAL

    - 一部の[よく知られたセキュリティプリンシパル](/windows/security/identity-protection/access-control/security-identifiers)の場合、例えば LOCAL SERVICE や ANONYMOUS LOGON、このフィールドの値は「NT AUTHORITY」となります。

    - ローカルユーザーアカウントの場合、このフィールドにはこのアカウントが属するコンピュータまたはデバイスの名前が含まれます。例えば「Win81」。

- **ログオンID** \[タイプ = HexInt64\]**:** 16進数の値で、同じログオンIDを含む最近のイベントとこのイベントを関連付けるのに役立ちます。例えば、「[4624](event-4624.md): アカウントが正常にログオンされました。」

**信頼されたドメイン:**

- **ドメイン名** \[タイプ = UnicodeString\]**:** 変更された信頼されたドメインの名前。この属性が変更されなかった場合、「**-**」の値を持ちます。

- **ドメインID** \[タイプ = SID\]**:** 変更された信頼されたドメインのSID。イベントビューアーは自動的にSIDを解決し、アカウント名を表示しようとします。SIDが解決できない場合、イベントにソースデータが表示されます。

**新しい信頼情報:**

- **信頼タイプ** \[タイプ = UInt32\]**:** 新しい信頼のタイプ。この属性が変更されなかった場合、「**-**」の値または古い値を持ちます。以下の表はこのフィールドの可能な値を含みます：

| 値   | 属性値                  | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1    | TRUST\_TYPE\_DOWNLEVEL  | 信頼されたドメインのドメインコントローラーは、Windows 2000以前のオペレーティングシステムを実行しているコンピュータです。                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 2    | TRUST\_TYPE\_UPLEVEL    | 信頼されたドメインのドメインコントローラーは、Windows 2000以降を実行しているコンピュータです。                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3    | TRUST\_TYPE\_MIT        | 信頼されたドメインは、非WindowsのRFC4120準拠のKerberosディストリビューションを実行しています。このタイプの信頼は、(1) [SID](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_83f2020d-0804-4840-a5ac-e06439d50f8d)が[TDO](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_f2ceef4e-999b-4276-84cd-2e2829de5fc4)に必要ないこと、(2) デフォルトのキータイプにDES-CBCおよびDES-CRC暗号化タイプが含まれること（[RFC4120](https://go.microsoft.com/fwlink/?LinkId=90458)セクション8.1参照）で区別されます。 |
| 4    | TRUST\_TYPE\_DCE        | 信頼されたドメインはDCE領域です。歴史的な参照であり、この値はWindowsでは使用されていません。                                                                                                                                                                                                                                                                                                                                                                                                                                                |

-   **信頼の方向** \[Type = UInt32\]**:** 新しい信頼の方向。この属性が変更されていない場合、「**-**」の値または古い値が表示されます。以下の表は、このフィールドの可能な値を含んでいます：

| 値   | 属性値                         | 説明                                                                                                 |
|------|--------------------------------|------------------------------------------------------------------------------------------------------|
| 0    | TRUST\_DIRECTION\_DISABLED     | 信頼関係は存在しますが、無効になっています。                                                        |
| 1    | TRUST\_DIRECTION\_INBOUND      | 信頼されたドメインが、名前の検索や認証などの操作を実行するためにプライマリドメインを信頼します。     |
| 2    | TRUST\_DIRECTION\_OUTBOUND     | プライマリドメインが、名前の検索や認証などの操作を実行するために信頼されたドメインを信頼します。     |
| 3    | TRUST\_DIRECTION\_BIDIRECTIONAL | 両方のドメインが、名前の検索や認証などの操作を実行するために互いに信頼します。                        |

-   **信頼属性** \[Type = UInt32\]**:** 新しい信頼の属性の10進値。10進値を16進値に変換し、以下の表で見つける必要があります。この属性が変更されていない場合、「**-**」の値または古い値が表示されます。以下の表は、このフィールドの可能な値を含んでいます：

| 値    | 属性値                                                    | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x1   | TRUST\_ATTRIBUTE\_NON\_TRANSITIVE                         | このビットが設定されている場合、信頼は推移的に使用できません。例えば、ドメインAがドメインBを信頼し、BがドメインCを信頼している場合、A&lt;--&gt;Bの信頼にこの属性が設定されていると、ドメインAのクライアントはA&lt;--&gt;B&lt;--&gt;Cの信頼リンクを介してドメインCのサーバーに認証できません。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 0x2   | TRUST\_ATTRIBUTE\_UPLEVEL\_ONLY                           | このビットが属性に設定されている場合、Windows 2000以降のクライアントのみが信頼リンクを使用できます。[Netlogon](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_70771a5a-04a3-447d-981b-e03098808c32)は、このフラグが設定されている[信頼オブジェクト](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_e81f6436-01d2-4311-93a4-4316bb67eabd)を消費しません。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0x4   | TRUST\_ATTRIBUTE\_QUARANTINED\_DOMAIN                     | このビットが設定されている場合、信頼されたドメインは隔離され、[SID](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_83f2020d-0804-4840-a5ac-e06439d50f8d)フィルタリングのルールに従います。詳細は[\[MS-PAC\]](/openspecs/windows_protocols/ms-pac/166d8064-c863-41e1-9c23-edaaa5f36962)のセクション[4.1.2.2](/openspecs/windows_protocols/ms-pac/55fc19f2-55ba-4251-8a6a-103dd7c66280)を参照してください。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 0x8   | TRUST\_ATTRIBUTE\_FOREST\_TRANSITIVE                      | このビットが設定されている場合、信頼リンクは2つの[フォレスト](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_fd104241-4fb3-457c-b2c4-e0c18bb20b62)のルートドメイン間の[クロスフォレスト信頼](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_86f3dbf2-338f-462e-8c5b-3c8e05798dbc)です。両方のフォレストはDS\_BEHAVIOR\_WIN2003以上の[フォレスト機能レベル](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_b3240417-ca43-4901-90ec-fde55b32b3b8)で動作しています。<br>Windows Server 2003、Windows Server 2008、Windows Server 2008 R2、Windows Server 2012、Windows Server 2012 R2、およびWindows Server 2016でのみ評価されます。<br>フォレストおよび信頼されたフォレストがDS\_BEHAVIOR\_WIN2003以上のフォレスト機能レベルで動作している場合にのみ設定できます。                   |
| 0x10  | TRUST\_ATTRIBUTE\_CROSS\_ORGANIZATION                     | このビットが設定されている場合、信頼は[組織](/openspecs/windows_protocols/ms-adts/b645c125-a7da-4097-84a1-2fa7cea07714#gt_6fae7775-5232-4206-b452-f298546ab54f)の一部ではないドメインまたはフォレストに対するものです。このビットによって制御される動作は、[\[MS-KILE\]](/openspecs/windows_protocols/ms-kile/2a32282e-dd48-4ad9-a542-609804b02cc9)のセクション[3.3.5.7.5](/openspecs/windows_protocols/ms-kile/bac4dc69-352d-416c-a9f4-730b81ababb3)および[\[MS-APDS\]](/openspecs/windows_protocols/ms-apds/dd444344-fd7e-430e-b313-7e95ab9c338e)のセクション[3.1.5](/openspecs/windows_protocols/ms-apds/f47e40e1-b9ca-47e2-b139-15a1e96b0e72)で説明されています。<br>Windows Server 2003、Windows Server 2008、Windows Server 2008 R2、Windows Server 2012、Windows Server 2012 R2、およびWindows Server 2016でのみ評価されます。<br>フォレストおよび信頼されたフォレストがDS\_BEHAVIOR\_WIN2003以上のフォレスト機能レベルで動作している場合にのみ設定できます。                                                                                                                                        |
| 0x20  | TRUST\_ATTRIBUTE\_WITHIN\_FOREST                          | このビットが設定されている場合、信頼されたドメインは同じフォレスト内にあります。<br>Windows Server 2003、Windows Server 2008、Windows Server 2008 R2、Windows Server 2012、Windows Server 2012 R2、およびWindows Server 2016でのみ評価されます。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0x40  | TRUST\_ATTRIBUTE\_TREAT\_AS\_EXTERNAL                     | このビットが設定されている場合、ドメインへのクロスフォレスト信頼はSIDフィルタリングの目的で外部信頼として扱われます。クロスフォレスト信頼は外部信頼よりも[厳密にフィルタリング](/openspecs/windows_protocols/ms-adts/e9a2d23c-c31e-4a6f-88a0-6646fdb51a3c)されます。この属性は、クロスフォレスト信頼を外部信頼と同等に緩和します。<br>Windows Server 2003、Windows Server 2008、Windows Server 2008 R2、Windows Server 2012、Windows Server 2012 R2、およびWindows Server 2016でのみ評価されます。<br>SIDフィルタリングが使用されている場合にのみ評価されます。<br>TRUST\_ATTRIBUTE\_FOREST\_TRANSITIVEを持つクロスフォレスト信頼でのみ評価されます。<br>フォレストおよび信頼されたフォレストがDS\_BEHAVIOR\_WIN2003以上のフォレスト機能レベルで動作している場合にのみ設定できます。 |
| 0x80  | TRUST\_ATTRIBUTE\_USES\_RC4\_ENCRYPTION                   | このビットは、RC4キーを使用できるTRUST\_TYPE\_MITに設定された信頼に設定されます。歴史的に、MIT KerberosディストリビューションはDESおよび3DESキーのみをサポートしていました（[\[RFC4120\]](https://go.microsoft.com/fwlink/?LinkId=90458)、[\[RFC3961\]](https://go.microsoft.com/fwlink/?LinkId=90450)）。MIT 1.4.1は、Windows 2000に共通のRC4HMAC暗号化タイプを採用したため、MITディストリビューションの後のバージョンを展開する信頼されたドメインにはこのビットが必要でした。詳細については、「キーと信頼」、セクション[6.1.6.9.1](/openspecs/windows_protocols/ms-adts/c964fca9-c50e-426a-9173-5bf3cb720e2e)を参照してください。<br>TRUST\_TYPE\_MITでのみ評価されます。                                                                                                                                                                                                                                          |
| 0x200 | TRUST\_ATTRIBUTE\_CROSS\_ORGANIZATION\_NO\_TGT\_DELEGATION | このビットが設定されている場合、この信頼の下で付与されたチケットは委任のために信頼されてはなりません。このビットによって制御される動作は、[\[MS-KILE\]](/openspecs/windows_protocols/ms-kile/2a32282e-dd48-4ad9-a542-609804b02cc9)のセクション3.3.5.7.5で指定されています。<br>Windows Server 2012、Windows Server 2012 R2、およびWindows Server 2016でのみサポートされています。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0x400 | TRUST\_ATTRIBUTE\_PIM\_TRUST                              | このビットとTATEビットが設定されている場合、ドメインへのクロスフォレスト信頼はSIDフィルタリングの目的で特権ID管理信頼として扱われます。各信頼タイプがどのようにフィルタリングされるかについての詳細は、[\[MS-PAC\]](/openspecs/windows_protocols/ms-pac/166d8064-c863-41e1-9c23-edaaa5f36962)のセクション4.1.2.2を参照してください。<br>Windows Server 2016でのみ評価されます。<br>SIDフィルタリングが使用されている場合にのみ評価されます。<br>TRUST\_ATTRIBUTE\_FOREST\_TRANSITIVEを持つクロスフォレスト信頼でのみ評価されます。<br>フォレストおよび信頼されたフォレストがDS\_BEHAVIOR\_WINTHRESHOLD以上のフォレスト機能レベルで動作している場合にのみ設定できます。                                                                                                                                                                                                                                                                                                                                   |

-   **SID フィルタリング** \[タイプ = UnicodeString\]: 新しい信頼のための [SID フィルタリング](/previous-versions/windows/it-pro/windows-server-2003/cc772633(v=ws.10)) の状態:

    -   有効

    -   無効

        この属性が変更されていない場合、「**-**」の値または古い値が設定されます。

## セキュリティ監視の推奨事項

4716(S): 信頼されたドメイン情報が変更されました。

-   Active Directory ドメイン信頼設定の変更はすべて監視され、アラートがトリガーされるべきです。この変更が計画されていない場合は、変更の理由を調査してください。

## 匿名ログオンアカウント

イベントで報告されたアカウントが **匿名ログオン** である場合、システムの自動パスワードリセットによってパスワードが変更されたことを意味します。例えば:

```
Log Name:      Security
Source:        Microsoft-Windows-Security-Auditing
Date:          <time>
Event ID:      4716
Task Category: Authentication Policy Change
Level:         Information
Keywords:      Audit Success
User:          N/A
Computer:      <fqdn>
Description:
Trusted domain information was modified.    //When trust gets reset, this event generates
Subject:
 Security ID:  ANONYMOUS LOGON              //Confirms that anonymous logon account is reported when Automatic password reset for the trust is performed
 Account Name:  ANONYMOUS LOGON
 Account Domain:  NT AUTHORITY
 Logon ID:  0x3E6
```

イベント 4716 の後、イベント 4724 またはイベント 4742、またはその両方が表示される場合があります:

```
Log Name:      Security
Source:        Microsoft-Windows-Security-Auditing
Date:          <time>
Event ID:      4724
Task Category: User Account Management
Level:         Information
Keywords:      Audit Success
User:          N/A
Computer:      <FQDN>
Description:
An attempt was made to reset an account's password.

Subject:
	Security ID:		ANONYMOUS LOGON
	Account Name:		ANONYMOUS LOGON
	Account Domain:		NT AUTHORITY
	Logon ID:		0x3E6

Target Account:
	Security ID:		CONTOSO\CONTOSOPEERTREE$     //OBJECT representing the TRUST object
	Account Name:		CONTOSOPEERTREE$
	Account Domain:		CONTOSO
```

```
Log Name:      Security
Source:        Microsoft-Windows-Security-Auditing
Date:          <time>
Event ID:      4742
Task Category: Computer Account Management
Level:         Information
Keywords:      Audit Success
User:          N/A
Computer:      <FQDN>
Description:
A computer account was changed.

Subject:
	Security ID:		ANONYMOUS LOGON
	Account Name:		ANONYMOUS LOGON
	Account Domain:		NT AUTHORITY
	Logon ID:		0x3E6

Computer Account That Was Changed:
	Security ID:		CONTOSO\CONTOSOPEERTREE$
	Account Name:		CONTOSOPEERTREE$
	Account Domain:		CONTOSO

Changed Attributes:
	...
	Password Last Set:	<time>
	...

Additional Information:
	Privileges:		-
```
