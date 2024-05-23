---
title: <EventData> 内の XML データ名要素のリストを取得する方法
description: IT プロフェッショナル向けのこのリファレンス記事では、PowerShell を使用して <EventData> に表示される XML データ名要素のリストを取得する方法について説明します。
ms.mktglfcycl: deploy
ms.sitesec: library
ms.pagetype: security
ms.localizationpriority: medium
author: vinaypamnani-msft
ms.date: 09/09/2021
ms.reviewer:
manager: aaroncz
ms.author: vinpa
ms.topic: reference
---

# EventData 内の XML データ名要素のリストを取得する方法

セキュリティ ログは、すべてのイベント スキーマを取得できるマニフェストを使用します。

昇格された PowerShell プロンプトから次のコマンドを実行します:

```powershell
$secEvents = get-winevent -listprovider "microsoft-windows-security-auditing"
```

`.events` プロパティは、ローカル マシンのマニフェストにリストされているすべてのイベントのコレクションです。

各イベントには、イベント プロパティに使用される XML テンプレートの `.Template` プロパティがあります (存在する場合)。

例えば:

```powershell
PS C:\WINDOWS\system32> $SecEvents.events[100]


Id          : 4734
Version     : 0
LogLink     : System.Diagnostics.Eventing.Reader.EventLogLink
Level       : System.Diagnostics.Eventing.Reader.EventLevel
Opcode      : System.Diagnostics.Eventing.Reader.EventOpcode
Task        : System.Diagnostics.Eventing.Reader.EventTask
Keywords    : {}
Template    : <template xmlns="http://schemas.microsoft.com/win/2004/08/events">
                <data name="TargetUserName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="TargetDomainName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="TargetSid" inType="win:SID" outType="xs:string"/>
                <data name="SubjectUserSid" inType="win:SID" outType="xs:string"/>
                <data name="SubjectUserName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="SubjectDomainName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="SubjectLogonId" inType="win:HexInt64" outType="win:HexInt64"/>
                <data name="PrivilegeList" inType="win:UnicodeString" outType="xs:string"/>
              </template>

Description : A security-enabled local group was deleted.

              Subject:
                Security ID:            %4
                Account Name:           %5
                Account Domain:         %6
                Logon ID:               %7

              Group:
                Security ID:            %3
                Group Name:             %1
                Group Domain:           %2

              Additional Information:
                Privileges:             %8



PS C:\WINDOWS\system32> $SecEvents.events[100].Template
<template xmlns="http://schemas.microsoft.com/win/2004/08/events">
  <data name="TargetUserName" inType="win:UnicodeString" outType="xs:string"/>
  <data name="TargetDomainName" inType="win:UnicodeString" outType="xs:string"/>
  <data name="TargetSid" inType="win:SID" outType="xs:string"/>
  <data name="SubjectUserSid" inType="win:SID" outType="xs:string"/>
  <data name="SubjectUserName" inType="win:UnicodeString" outType="xs:string"/>
  <data name="SubjectDomainName" inType="win:UnicodeString" outType="xs:string"/>
  <data name="SubjectLogonId" inType="win:HexInt64" outType="win:HexInt64"/>
  <data name="PrivilegeList" inType="win:UnicodeString" outType="xs:string"/>
</template>

```

## データ名要素をイベント説明の名前にマッピングする

&lt;Template&gt; と &lt;Description&gt; を使用して、XML ビューに表示されるデータ名要素をイベント説明に表示される名前にマッピングできます。

&lt;Description&gt; は単なるフォーマット文字列です (`Console.Writeline` や `sprintf` ステートメントに慣れている場合)、そして &lt;Template&gt; は &lt;Description&gt; の入力パラメーターのソースです。

セキュリティ イベント 4734 を例に使用します:

```xml
Template    : <template xmlns="http://schemas.microsoft.com/win/2004/08/events">
                <data name="TargetUserName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="TargetDomainName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="TargetSid" inType="win:SID" outType="xs:string"/>
                <data name="SubjectUserSid" inType="win:SID" outType="xs:string"/>
                <data name="SubjectUserName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="SubjectDomainName" inType="win:UnicodeString" outType="xs:string"/>
                <data name="SubjectLogonId" inType="win:HexInt64" outType="win:HexInt64"/>
                <data name="PrivilegeList" inType="win:UnicodeString" outType="xs:string"/>
              </template>

Description : A security-enabled local group was deleted.

              Subject:
                Security ID:            %4
                Account Name:           %5
                Account Domain:         %6
                Logon ID:               %7

              Group:
                Security ID:            %3
                Group Name:             %1
                Group Domain:           %2

              Additional Information:
                Privileges:             %8

```

**Subject: Security ID:** テキスト要素の場合、テンプレートの 4 番目の要素 **SubjectUserSid** が使用されます。

**Additional Information Privileges:** の場合、8 番目の要素 **PrivilegeList** が使用されます。

この原則に対する注意点は、イベントのスキーマと説明の改訂を示すバージョン (SYSTEM 要素内) と呼ばれるイベントの見落とされがちなプロパティです。ほとんどのイベントには 1 つのバージョンがあります (すべてのイベントにはセキュリティ/4734 の例のようにバージョン =0 があります) が、セキュリティ/4624 やセキュリティ/4688 のようないくつかのイベントには、イベントが生成される OS バージョンに応じて少なくとも 3 つのバージョン (バージョン 0、1、2) があります。最新バージョンのみがセキュリティ ログでイベントを生成するために使用されます。いずれにせよ、テンプレートが取得されるイベント バージョンは、説明のために同じイベント バージョンを使用する必要があります。

It seems like you haven't pasted the Markdown content yet. Please provide the content you want translated, and I'll proceed with the translation following the specified rules.
