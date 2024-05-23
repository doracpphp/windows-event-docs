---
title: 4675(S) SIDがフィルタリングされました。
description: Active Directoryの特定の信頼関係に対してSIDがフィルタリングされたときに生成されるセキュリティイベント4675(S)について説明します。
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

# 4675(S): SIDがフィルタリングされました。

このイベントは、特定のActive Directory信頼関係に対してSIDがフィルタリングされたときに生成されます。

SIDフィルタリングの詳細については、こちらをご覧ください: <https://technet.microsoft.com/library/cc772633(v=ws.10).aspx>.

> **注**&nbsp;&nbsp;**セキュリティ識別子 (SID)** は、トラスティ（セキュリティプリンシパル）を識別するために使用される可変長の一意の値です。各アカウントには、Active Directoryドメインコントローラーなどの権限によって発行され、セキュリティデータベースに保存される一意のSIDがあります。ユーザーがログオンするたびに、システムはデータベースからそのユーザーのSIDを取得し、そのユーザーのアクセストークンに配置します。システムは、以降のすべてのWindowsセキュリティとのやり取りでユーザーを識別するためにアクセストークン内のSIDを使用します。ユーザーまたはグループの一意の識別子としてSIDが使用された場合、それは他のユーザーまたはグループを識別するために再利用されることはありません。SIDの詳細については、[セキュリティ識別子](/windows/access-protection/access-control/security-identifiers)をご覧ください。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[ログオンの監査](audit-logon.md)

***イベントスキーマ:***

*SIDがフィルタリングされました。*

*ターゲットアカウント:*

> *セキュリティID:%1*
>
> *アカウント名:%2*
>
> *アカウントドメイン:%3*

*信頼情報:*

> *信頼方向:%4*
>
> *信頼属性:%5*
>
> *信頼タイプ:%6*
>
> *TDOドメインSID:%7*
>
> *フィルタリングされたSID:%8*

***必要なサーバーロール:*** Active Directoryドメインコントローラー。

***最小OSバージョン:*** Windows Server 2008。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

- 特定またはすべてのActive Directory信頼関係に対するすべてのSIDフィルタリングイベント/操作を監視する必要がある場合、このイベントを使用して必要な情報をすべて取得できます。

It looks like you haven't pasted the Markdown content yet. Please provide the content you want translated into Japanese.
