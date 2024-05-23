---
title: 監査アプリケーション生成
description: ポリシー設定「監査アプリケーション生成」は、アプリケーションがWindows監査APIを使用しようとしたときに監査イベントが生成されるかどうかを決定します。
ms.assetid: 6c58a365-b25b-42b8-98ab-819002e31871
ms.reviewer: 
manager: aaroncz
ms.author: vinpa
ms.pagetype: security
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: low
author: vinaypamnani-msft
ms.date: 09/06/2021
ms.topic: reference
---

# 監査アプリケーション生成

監査アプリケーション生成は、Authorization Manager [アプリケーション](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770563(v=ws.11))に関連するアクションのイベントを生成します。

監査アプリケーション生成のサブカテゴリは、このドキュメントの範囲外です。なぜなら、[Authorization Manager](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc726036(v=ws.11))は非常に稀に使用され、Windows Server 2012から非推奨となっているためです。

| コンピューターの種類 | 一般的な成功 | 一般的な失敗 | 強力な成功 | 強力な失敗 | コメント |
|-------------------|-----------------|-----------------|------------------|------------------|----------|
| ドメインコントローラー | IF              | IF              | IF               | IF               | IF – 環境で[Authorization Manager](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc726036(v=ws.11))を使用し、Authorization Manager [アプリケーション](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770563(v=ws.11))に関連するイベントを監視する必要がある場合、このサブカテゴリを有効にします。 |
| メンバーサーバー     | IF              | IF              | IF               | IF               | IF – 環境で[Authorization Manager](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc726036(v=ws.11))を使用し、Authorization Manager [アプリケーション](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770563(v=ws.11))に関連するイベントを監視する必要がある場合、このサブカテゴリを有効にします。 |
| ワークステーション       | IF              | IF              | IF               | IF               | IF – 環境で[Authorization Manager](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc726036(v=ws.11))を使用し、Authorization Manager [アプリケーション](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc770563(v=ws.11))に関連するイベントを監視する必要がある場合、このサブカテゴリを有効にします。 |

**イベントリスト:**

- 4665: アプリケーションクライアントコンテキストの作成が試みられました。

- 4666: アプリケーションが操作を試みました。

- 4667: アプリケーションクライアントコンテキストが削除されました。

- 4668: アプリケーションが初期化されました。
