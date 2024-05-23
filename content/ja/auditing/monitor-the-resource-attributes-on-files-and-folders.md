---
title: ファイルとフォルダーのリソース属性を監視する
description: 高度なセキュリティ監査オプションを使用して、ファイルのリソース属性の設定変更の試みを監視する方法を学びます。
ms.assetid: 4944097b-320f-44c7-88ed-bf55946a358b
ms.reviewer:
ms.author: vinpa
ms.mktglfcycl: deploy
ms.sitesec: library
ms.pagetype: security
ms.localizationpriority: medium
author: vinaypamnani-msft
manager: aaroncz
audience: ITPro
ms.topic: reference
ms.date: 09/09/2021
---

# ファイルとフォルダーのリソース属性を監視する

このトピックは IT プロフェッショナル向けに、動的アクセス制御オブジェクトを監視するための高度なセキュリティ監査オプションを使用して、ファイルのリソース属性の設定変更の試みを監視する方法を説明します。

組織がリソースのために慎重に考え抜かれた認可構成を持っている場合、これらのリソース属性の変更は潜在的なセキュリティリスクを引き起こす可能性があります。例としては以下が含まれます：

- 高いビジネス価値としてマークされたファイルを低いビジネス価値に変更する。
- 保持のためにマークされたファイルの保持属性を変更する。
- 特定の部門に属するファイルの部門属性を変更する。

以下の手順を使用して、ファイルとフォルダーのリソース属性の変更を監視するための設定を構成します。これらの手順は、ネットワークに中央アクセス ポリシーを構成して展開したことを前提としています。中央アクセス ポリシーの構成と展開の詳細については、[動的アクセス制御: シナリオの概要](/windows-server/identity/solution-guides/dynamic-access-control--scenario-overview) を参照してください。

>**注:** サーバーの機能は、インストールされているオペレーティング システムのバージョンとエディション、アカウントの権限、およびメニュー設定に基づいて異なる場合があります。

**ファイルのリソース属性の変更を監視するには**

1. ドメイン管理者の資格情報を使用してドメイン コントローラーにサインインします。
2. サーバー マネージャーで、**ツール** をポイントし、**グループ ポリシーの管理** をクリックします。
3. コンソール ツリーで、柔軟なアクセス グループ ポリシー オブジェクトを右クリックし、**編集** をクリックします。
4. **コンピューターの構成** をダブルクリックし、**セキュリティ設定** をダブルクリックし、**高度な監査ポリシーの構成** をダブルクリックし、**ポリシーの変更** をダブルクリックし、**監査認可ポリシーの変更** をダブルクリックします。
5. **次の監査イベントを構成する** チェック ボックスを選択し、**成功** および **失敗** チェック ボックスを選択して、**OK** をクリックします。

ファイルのリソース属性を監視する設定を行った後、変更が監視されていることを確認します。

**ファイルのリソース属性の変更が監視されていることを確認する方法**

1.  監視したいリソースをホストしているサーバーに管理者の資格情報を使用してサインインします。
2.  昇格したコマンドプロンプトから、**gpupdate /force** と入力し、ENTER キーを押します。
3.  1つ以上のファイルやフォルダーのリソースプロパティを変更しようとします。
4.  サーバーマネージャーで、**ツール** をクリックし、**イベントビューアー** をクリックします。
5.  **Windows ログ** を展開し、**セキュリティ** をクリックします。
6.  変更しようとしたリソース属性に応じて、次のイベントを探します：

    -   ファイル属性の変更を追跡するイベント 4911
    -   中央アクセスポリシーの変更を追跡するイベント 4913

    注目すべき重要な情報には、リソース属性を変更しようとしている主体の名前とアカウントドメイン、主体が変更しようとしているオブジェクト、および試みられている変更に関する情報が含まれます。

### 関連リソース

- [動的アクセス制御オブジェクトを監視するための高度なセキュリティ監査オプションの使用](using-advanced-security-auditing-options-to-monitor-dynamic-access-control-objects.md)