---
title: システムの整合性を監査する
description: ポリシー設定「システムの整合性を監査する」は、オペレーティングシステムがセキュリティサブシステムの整合性を侵害するイベントを監査するかどうかを決定します。
ms.assetid: 942a9a7f-fa31-4067-88c7-f73978bf2034
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

# システムの整合性を監査する

システムの整合性を監査するかどうかを決定します。

セキュリティサブシステムの整合性を侵害する活動には、次のものが含まれます。

-   監査システムの障害により監査イベントが失われる。

-   プロセスが無効なローカルプロシージャコール (LPC) ポートを使用して、クライアントを偽装しようとしたり、クライアントアドレス空間に返信したり、クライアントアドレス空間を読み取ったり、クライアントアドレス空間から書き込んだりする。

-   リモートプロシージャコール (RPC) の整合性違反が検出される。

-   実行可能ファイルの無効なハッシュ値によるコード整合性違反が検出される。

-   暗号化タスクが実行される。

セキュリティサブシステムの整合性違反は重大であり、潜在的なセキュリティ攻撃を示している可能性があります。

**イベントボリューム**: 低。

| コンピュータの種類 | 一般的な成功 | 一般的な失敗 | 強化された成功 | 強化された失敗 | コメント                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------|-----------------|-----------------|------------------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ドメインコントローラー | はい             | はい             | はい              | はい              | このサブカテゴリの成功監査を推奨する主な理由は、RPC 整合性違反エラーと監査サブシステムエラー (イベント 4612) を取得できるようにするためです。ただし、「[4618](event-4618.md)(S): 監視されたセキュリティイベントパターンが発生しました」を手動で呼び出す予定がある場合は、このサブカテゴリの成功監査も有効にする必要があります。<br>このサブカテゴリの失敗監査を推奨する主な理由は、[コード整合性](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd348642(v=ws.10)) の失敗イベントを取得できるようにするためです。 |
| メンバーサーバー     | はい             | はい             | はい              | はい              | このサブカテゴリの成功監査を推奨する主な理由は、RPC 整合性違反エラーと監査サブシステムエラー (イベント 4612) を取得できるようにするためです。ただし、「[4618](event-4618.md)(S): 監視されたセキュリティイベントパターンが発生しました」を手動で呼び出す予定がある場合は、このサブカテゴリの成功監査も有効にする必要があります。<br>このサブカテゴリの失敗監査を推奨する主な理由は、[コード整合性](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd348642(v=ws.10)) の失敗イベントを取得できるようにするためです。 |
| ワークステーション   | はい             | はい             | はい              | はい              | このサブカテゴリの成功監査を推奨する主な理由は、RPC 整合性違反エラーと監査サブシステムエラー (イベント 4612) を取得できるようにするためです。ただし、「[4618](event-4618.md)(S): 監視されたセキュリティイベントパターンが発生しました」を手動で呼び出す予定がある場合は、このサブカテゴリの成功監査も有効にする必要があります。<br>このサブカテゴリの失敗監査を推奨する主な理由は、[コード整合性](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/dd348642(v=ws.10)) の失敗イベントを取得できるようにするためです。 |

**イベントリスト:**

-   [4612](event-4612.md)(S): 監査メッセージのキューイングのために内部リソースが枯渇し、一部の監査が失われました。

-   [4615](event-4615.md)(S): LPCポートの不正使用。

-   [4618](event-4618.md)(S): 監視されているセキュリティイベントパターンが発生しました。

-   [4816](event-4816.md)(S): RPCが受信メッセージの復号中に整合性違反を検出しました。

-   [5038](event-5038.md)(F): コード整合性により、ファイルのイメージハッシュが無効であると判断されました。ファイルは不正な変更により破損している可能性があり、無効なハッシュは潜在的なディスクデバイスエラーを示している可能性があります。

-   [5056](event-5056.md)(S): 暗号化の自己テストが実行されました。

-   [5062](event-5062.md)(S): カーネルモードの暗号化自己テストが実行されました。

-   [5057](event-5057.md)(F): 暗号化プリミティブ操作が失敗しました。

-   [5060](event-5060.md)(F): 検証操作が失敗しました。

-   [5061](event-5061.md)(S, F): 暗号化操作。

-   [6281](event-6281.md)(F): コード整合性により、イメージファイルのページハッシュが無効であると判断されました。ファイルはページハッシュなしで不適切に署名されているか、不正な変更により破損している可能性があります。無効なハッシュは潜在的なディスクデバイスエラーを示している可能性があります。

-   [6410](event-6410.md)(F): コード整合性により、ファイルがプロセスにロードするためのセキュリティ要件を満たしていないと判断されました。
