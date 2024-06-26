---
title: 監査ファイルシステム
description: 高度なセキュリティ監査ポリシー設定である監査ファイルシステムは、ユーザーがファイルシステムオブジェクトにアクセスしようとしたときに監査イベントが生成されるかどうかを決定します。
ms.assetid: 6a71f283-b8e5-41ac-b348-0b7ec6ea0b1f
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

# 監査ファイルシステム

> [!NOTE]
> 古いオペレーティングシステムバージョンへの適用性の詳細については、記事 [監査ファイルシステム](/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn319068(v=ws.11)) を参照してください。

監査ファイルシステムは、ユーザーがファイルシステムオブジェクトにアクセスしようとしたときにオペレーティングシステムが監査イベントを生成するかどうかを決定します。

監査イベントは、システムアクセス制御リスト ([SACL](/windows/win32/secauthz/access-control-lists)) が設定されているオブジェクトに対してのみ生成され、要求されたアクセスの種類（書き込み、読み取り、変更など）および要求を行ったアカウントが [SACL](/windows/win32/secauthz/access-control-lists) の設定と一致する場合にのみ生成されます。

成功監査が有効になっている場合、対応する SACL を持つファイルシステムオブジェクトに任意のアカウントが正常にアクセスするたびに監査エントリが生成されます。失敗監査が有効になっている場合、対応する SACL を持つファイルシステムオブジェクトにユーザーがアクセスしようとして失敗するたびに監査エントリが生成されます。

これらのイベントは、機密性が高いまたは価値のあるファイルオブジェクトのアクティビティを追跡するために不可欠です。

**イベントボリューム**: ファイルシステム [SACL](/windows/win32/secauthz/access-control-lists) の設定方法によって異なります。

デフォルトのファイルシステム [SACL](/windows/win32/secauthz/access-control-lists) では監査イベントは生成されません。

このサブカテゴリを使用すると、ユーザーがファイルシステムオブジェクトにアクセスしようとする試み、ファイルシステムオブジェクトの削除および権限変更操作、ハードリンク作成アクションを監査できます。

唯一のイベント「[4658](event-4658.md): オブジェクトへのハンドルが閉じられました」は、[監査ハンドル操作](audit-handle-manipulation.md) サブカテゴリに依存します（成功監査が有効である必要があります）。その他のすべてのイベントは追加の設定なしで生成されます。


| コンピュータの種類 | 一般的な成功 | 一般的な失敗 | 強い成功 | 強い失敗 | コメント                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------|-----------------|-----------------|------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ドメインコントローラー | IF              | IF              | IF               | IF               | ファイルシステムセキュリティ監視ポリシーを策定し、異なるオペレーティングシステムテンプレートおよび役割に対して適切な[SACL](/windows/win32/secauthz/access-control-lists)を定義することを強くお勧めします。収集した情報の使用方法と分析方法を計画していない場合は、このサブカテゴリを有効にしないでください。また、効果のない余分な[SACL](/windows/win32/secauthz/access-control-lists)を削除することも重要です。そうしないと、監査ログが無駄な情報で過負荷になります。<br>失敗イベントは、特定のファイルシステムオブジェクトへのアクセスが失敗した試行を示すことができます。<br>まず、重要なコンピュータに対してファイルシステムセキュリティ監視ポリシーを策定した後、このサブカテゴリを有効にすることを検討してください。 |
| メンバーサーバー     | IF              | IF              | IF               | IF               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ワークステーション   | IF              | IF              | IF               | IF               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

**イベントリスト:**

-   [4656](event-4656.md)(S, F): オブジェクトへのハンドルが要求されました。

-   [4658](event-4658.md)(S): オブジェクトへのハンドルが閉じられました。

-   [4660](event-4660.md)(S): オブジェクトが削除されました。

-   [4663](event-4663.md)(S): オブジェクトへのアクセスが試みられました。

-   [4664](event-4664.md)(S): ハードリンクの作成が試みられました。

-   [4985](event-4985.md)(S): トランザクションの状態が変更されました。

-   [5051](event-5051.md)(-): ファイルが仮想化されました。

-   [4670](event-4670.md)(S): オブジェクトの権限が変更されました。
