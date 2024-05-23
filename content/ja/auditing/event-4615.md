---
title: 4615(S) LPCポートの無効な使用。
description: セキュリティイベント4615(S) LPCポートの無効な使用について説明します。LPCポートの無効な使用イベントは発生しないようです。
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

# 4615(S): LPCポートの無効な使用。

このイベントは発生しないようです。

***サブカテゴリ:***&nbsp;[システム整合性の監査](audit-system-integrity.md)

***イベントスキーマ:***

*LPCポートの無効な使用。*

*サブジェクト:*

> *セキュリティID%1*
>
> *アカウント名:%2*
>
> *アカウントドメイン:%3*
>
> *ログオンID:%4*

*プロセス情報:*

> *PID:%7*
>
> *名前:%8*

*無効な使用:%5*

*LPCサーバーポート名:%6*

*Windowsローカルセキュリティ機関 (LSA) は、ローカルプロシージャコール (LPC) ポートを使用してWindowsカーネルと通信します。このイベントが表示された場合、アプリケーションが誤ってまたは意図的にこのポートにアクセスしたことを示します。このポートはLSA専用に予約されています。アプリケーション（プロセス）を調査して、この通信チャネルを改ざんしようとしていないことを確認する必要があります。*

***必要なサーバーロール:*** なし。

***最小OSバージョン:*** Windows Server 2008, Windows Vista。

***イベントバージョン:*** 0。

## セキュリティ監視の推奨事項

-   このドキュメントには、このイベントに対する推奨事項はありません。
