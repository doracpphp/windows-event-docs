---
title: ディレクトリ サービス レプリケーションの監査
description: ディレクトリ サービス レプリケーションの監査は、2 つのドメイン コントローラー間のレプリケーションが開始または終了したときに監査イベントが作成されるかどうかを決定するポリシー設定です。
ms.assetid: b95d296c-7993-4e8d-8064-a8bbe284bd56
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

# ディレクトリ サービス レプリケーションの監査

ディレクトリ サービス レプリケーションの監査は、2 つのドメイン コントローラー間のレプリケーションが開始および終了したときに、オペレーティング システムが監査イベントを生成するかどうかを決定します。

**イベント ボリューム**: ドメイン コントローラーで中程度。

| コンピューターの種類 | 一般的な成功 | 一般的な失敗 | 強い成功 | 強い失敗 | コメント                                                                                                                                                                                                                   |
|-----------------------|---------------|---------------|------------|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ドメイン コントローラー | いいえ        | いいえ        | IF         | IF         | IF - このサブカテゴリのイベントは通常、情報提供を目的としており、これらのイベントを使用して悪意のある活動を検出することは困難です。主に Active Directory レプリケーションのトラブルシューティングに使用されます。 |
| メンバー サーバー     | いいえ        | いいえ        | いいえ     | いいえ     | このサブカテゴリはドメイン コントローラーでのみ意味があります。                                                                                                                                                           |
| ワークステーション   | いいえ        | いいえ        | いいえ     | いいえ     | このサブカテゴリはドメイン コントローラーでのみ意味があります。                                                                                                                                                           |

**イベントリスト:**

-   [4932](event-4932.md)(S): Active Directory 名前付けコンテキストのレプリカの同期が開始されました。

-   [4933](event-4933.md)(S, F): Active Directory 名前付けコンテキストのレプリカの同期が終了しました。
