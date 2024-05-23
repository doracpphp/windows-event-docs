---
title: IPsecクイックモードの監査
description: ポリシー設定「IPsecクイックモードの監査」は、クイックモード交渉中のIKEプロトコルおよびAuthIPの結果に対して監査イベントが生成されるかどうかを決定します。
ms.assetid: 7be67a15-c2ce-496a-9719-e25ac7699114
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

# IPsecクイックモードの監査

IPsecクイックモードの監査を使用すると、クイックモード交渉中にインターネットキー交換プロトコル（IKE）および認証済みインターネットプロトコル（AuthIP）によって生成されたイベントを監査できます。

IPsecクイックモードの監査サブカテゴリは、このドキュメントの範囲外です。このサブカテゴリは主にIPsecクイックモードのトラブルシューティングに使用されるためです。

| コンピュータの種類 | 一般的な成功 | 一般的な失敗 | 強力な成功 | 強力な失敗 | コメント |
|-------------------|-----------------|-----------------|------------------|------------------|----------|
| ドメインコントローラー | IF              | IF              | IF               | IF               | IF - このサブカテゴリは主にIPsecクイックモードのトラブルシューティング、またはIPsecクイックモード操作のトレースや監視に使用されます。 |
| メンバーサーバー     | IF              | IF              | IF               | IF               | IF - このサブカテゴリは主にIPsecクイックモードのトラブルシューティング、またはIPsecクイックモード操作のトレースや監視に使用されます。 |
| ワークステーション   | IF              | IF              | IF               | IF               | IF - このサブカテゴリは主にIPsecクイックモードのトラブルシューティング、またはIPsecクイックモード操作のトレースや監視に使用されます。 |

- 4977(S): クイックモード交渉中に、IPsecが無効な交渉パケットを受信しました。この問題が続く場合、ネットワークの問題やこの交渉を変更またはリプレイしようとする試みを示している可能性があります。

- 5451(S): IPsecクイックモードのセキュリティアソシエーションが確立されました。

- 5452(S): IPsecクイックモードのセキュリティアソシエーションが終了しました。

It looks like you haven't pasted the Markdown content yet. Please provide the content you want translated into Japanese.
