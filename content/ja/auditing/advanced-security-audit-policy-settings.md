---
title: 高度なセキュリティ監査ポリシー設定
description: IT プロフェッショナル向けのこのリファレンスは、Windows で利用可能な高度な監査ポリシー設定と、それらが生成する監査イベントに関する情報を提供します。
ms.assetid: 93b28b92-796f-4036-a53b-8b9e80f9f171
ms.author: vinpa
ms.mktglfcycl: deploy
ms.sitesec: library
ms.pagetype: security
author: vinaypamnani-msft
manager: aaroncz
audience: ITPro
ms.topic: reference
ms.date: 09/06/2021
---

# 高度なセキュリティ監査ポリシー設定 (Windows 10)

IT プロフェッショナル向けのこのリファレンスは、以下に関する情報を提供します:
- Windows で利用可能な高度な監査ポリシー設定
- これらの設定が生成する監査イベント

**セキュリティ設定\\高度な監査ポリシー構成**の下にあるセキュリティ監査ポリシー設定は、次のような正確に定義された活動を追跡することにより、重要なビジネス関連およびセキュリティ関連のルールに対する組織のコンプライアンスを監査するのに役立ちます:

- グループ管理者が財務情報を含むサーバーの設定やデータを変更した。
- 定義されたグループ内の従業員が重要なファイルにアクセスした。
- 検出されないアクセスに対する検証可能な保護手段として、正しいシステムアクセス制御リスト (SACL) が次のいずれかに適用されている:
    - すべてのファイルとフォルダー
    - コンピューター上のレジストリキー
    - ファイル共有

これらの監査ポリシー設定には、ローカルコンピューターのローカルセキュリティポリシースナップイン (secpol.msc) を使用するか、グループポリシーを使用してアクセスできます。

これらの高度な監査ポリシー設定により、監視したい動作のみを選択できます。次のような動作の監査結果を除外できます:
- あなたにとってほとんど関心がない、または全く関心がないもの
- 過剰な数のログエントリを生成するもの

さらに、セキュリティ監査ポリシーはドメイングループポリシーオブジェクトを使用して適用できるため、監査ポリシー設定を比較的簡単に変更、テスト、および選択されたユーザーやグループに展開できます。
**セキュリティ設定\\高度な監査ポリシー構成**の下にある監査ポリシー設定は、次のカテゴリで利用できます:

## アカウントログオン

このカテゴリのポリシー設定を構成することで、ドメインコントローラーまたはローカルのセキュリティアカウントマネージャー (SAM) でアカウントデータの認証を試みた記録を残すことができます。ログオンおよびログオフのポリシー設定やイベントとは異なり、アカウントログオンの設定およびイベントは使用されるアカウントデータベースに焦点を当てています。このカテゴリには次のサブカテゴリが含まれます:

-   [資格情報の検証の監査](audit-credential-validation.md)
-   [Kerberos 認証サービスの監査](audit-kerberos-authentication-service.md)
-   [Kerberos サービスチケット操作の監査](audit-kerberos-service-ticket-operations.md)
-   [その他のアカウントログオンイベントの監査](audit-other-account-logon-events.md)

## アカウント管理

このカテゴリのセキュリティ監査ポリシー設定は、ユーザーおよびコンピューターアカウントやグループの変更を監視するために使用できます。このカテゴリには次のサブカテゴリが含まれます:

-   [アプリケーショングループ管理の監査](audit-application-group-management.md)
-   [コンピューターアカウント管理の監査](audit-computer-account-management.md)
-   [配布グループ管理の監査](audit-distribution-group-management.md)
-   [その他のアカウント管理イベントの監査](audit-other-account-management-events.md)
-   [セキュリティグループ管理の監査](audit-security-group-management.md)
-   [ユーザーアカウント管理の監査](audit-user-account-management.md)

## 詳細な追跡

詳細な追跡セキュリティポリシー設定および監査イベントは、以下の目的で使用できます:
- 個々のアプリケーションおよびユーザーの活動を監視するため
- コンピューターの使用方法を理解するため

このカテゴリには次のサブカテゴリが含まれます:

- [DPAPI 活動の監査](audit-dpapi-activity.md)
- [PNP 活動の監査](audit-pnp-activity.md)
- [プロセス作成の監査](audit-process-creation.md)
- [プロセス終了の監査](audit-process-termination.md)
- [RPC イベントの監査](audit-rpc-events.md)
- [トークン権利調整の監査](audit-token-right-adjusted.md)

## DS アクセス

DS アクセスセキュリティ監査ポリシー設定は、Active Directory ドメインサービス (AD DS) 内のオブジェクトへのアクセスおよび変更の試行に関する詳細な監査記録を提供します。これらの監査イベントはドメインコントローラーでのみ記録されます。このカテゴリには次のサブカテゴリが含まれます:

-   [詳細なディレクトリ サービス レプリケーションの監査](audit-detailed-directory-service-replication.md)
-   [ディレクトリ サービス アクセスの監査](audit-directory-service-access.md)
-   [ディレクトリ サービスの変更の監査](audit-directory-service-changes.md)
-   [ディレクトリ サービス レプリケーションの監査](audit-directory-service-replication.md)

## ログオン/ログオフ

ログオン/ログオフのセキュリティ ポリシー設定と監査イベントにより、コンピューターへのインタラクティブまたはネットワーク経由のログオン試行を追跡できます。これらのイベントは、ユーザーの活動を追跡し、ネットワーク リソースへの潜在的な攻撃を特定するのに特に役立ちます。このカテゴリには、次のサブカテゴリが含まれます:

-   [アカウント ロックアウトの監査](audit-account-lockout.md)
-   [ユーザー/デバイス クレームの監査](audit-user-device-claims.md)
-   [IPsec 拡張モードの監査](audit-ipsec-extended-mode.md)
-   [グループ メンバーシップの監査](audit-group-membership.md)
-   [IPsec メイン モードの監査](audit-ipsec-main-mode.md)
-   [IPsec クイック モードの監査](audit-ipsec-quick-mode.md)
-   [ログオフの監査](audit-logoff.md)
-   [ログオンの監査](audit-logon.md)
-   [ネットワーク ポリシー サーバーの監査](audit-network-policy-server.md)
-   [その他のログオン/ログオフ イベントの監査](audit-other-logonlogoff-events.md)
-   [特別なログオンの監査](audit-special-logon.md)

## オブジェクト アクセス

オブジェクト アクセス ポリシー設定と監査イベントにより、ネットワークまたはコンピューター上の特定のオブジェクトまたはオブジェクトの種類へのアクセス試行を追跡できます。ファイル、ディレクトリ、レジストリ キー、またはその他のオブジェクトへのアクセス試行を監査するには、成功および/または失敗イベントに対して適切なオブジェクト アクセス監査サブカテゴリを有効にします。たとえば、ファイル操作を監査するにはファイル システム サブカテゴリを有効にする必要があり、レジストリ アクセスを監査するにはレジストリ サブカテゴリを有効にする必要があります。

これらの監査ポリシーが外部監査人に対して有効であることを証明するのはより困難です。すべての継承オブジェクトに適切な SACL が設定されていることを確認する簡単な方法はありません。この問題に対処するには、[グローバル オブジェクト アクセス監査](#global-object-access-auditing)を参照してください。

このカテゴリには、次のサブカテゴリが含まれます:

-   [アプリケーション生成の監査](audit-application-generated.md)
-   [認証サービスの監査](audit-certification-services.md)
-   [詳細ファイル共有の監査](audit-detailed-file-share.md)
-   [ファイル共有の監査](audit-file-share.md)
-   [ファイルシステムの監査](audit-file-system.md)
-   [フィルタリングプラットフォーム接続の監査](audit-filtering-platform-connection.md)
-   [フィルタリングプラットフォームパケットドロップの監査](audit-filtering-platform-packet-drop.md)
-   [ハンドル操作の監査](audit-handle-manipulation.md)
-   [カーネルオブジェクトの監査](audit-kernel-object.md)
-   [その他のオブジェクトアクセスイベントの監査](audit-other-object-access-events.md)
-   [レジストリの監査](audit-registry.md)
-   [リムーバブルストレージの監査](audit-removable-storage.md)
-   [SAMの監査](audit-sam.md)
-   [中央アクセスポリシーステージングの監査](audit-central-access-policy-staging.md)

## ポリシー変更

ポリシー変更の監査イベントは、ローカルシステムやネットワーク上の重要なセキュリティポリシーの変更を追跡することができます。ポリシーは通常、ネットワークリソースを保護するために管理者によって設定されるため、これらのポリシーの変更（または変更の試み）を追跡することは、ネットワークのセキュリティ管理において重要な側面です。このカテゴリには次のサブカテゴリが含まれます：

-   [監査ポリシー変更の監査](audit-audit-policy-change.md)
-   [認証ポリシー変更の監査](audit-authentication-policy-change.md)
-   [認可ポリシー変更の監査](audit-authorization-policy-change.md)
-   [フィルタリングプラットフォームポリシー変更の監査](audit-filtering-platform-policy-change.md)
-   [MPSSVCルールレベルポリシー変更の監査](audit-mpssvc-rule-level-policy-change.md)
-   [その他のポリシー変更イベントの監査](audit-other-policy-change-events.md)

## 特権使用

ネットワーク上の権限は、ユーザーやコンピュータが定義されたタスクを完了するために付与されます。特権使用のセキュリティポリシー設定と監査イベントは、1つまたは複数のシステムで特定の権限の使用を追跡することができます。このカテゴリには次のサブカテゴリが含まれます：

-   [非機密特権使用の監査](audit-non-sensitive-privilege-use.md)
-   [機密特権使用の監査](audit-sensitive-privilege-use.md)
-   [その他の特権使用イベントの監査](audit-other-privilege-use-events.md)

## システム

システムセキュリティポリシー設定と監査イベントにより、コンピュータに対する以下の種類のシステムレベルの変更を追跡できます:
- 他のカテゴリに含まれない
- セキュリティに関する潜在的な影響がある

このカテゴリには以下のサブカテゴリが含まれます:

-   [IPsec ドライバの監査](audit-ipsec-driver.md)
-   [その他のシステムイベントの監査](audit-other-system-events.md)
-   [セキュリティ状態の変更の監査](audit-security-state-change.md)
-   [セキュリティシステム拡張の監査](audit-security-system-extension.md)
-   [システムの整合性の監査](audit-system-integrity.md)

## グローバルオブジェクトアクセス監査

グローバルオブジェクトアクセス監査ポリシー設定により、管理者はファイルシステムまたはレジストリのオブジェクトタイプごとにコンピュータシステムアクセス制御リスト (SACL) を定義できます。指定されたSACLは、そのタイプのすべてのオブジェクトに自動的に適用されます。
監査人は、システム内のすべてのリソースが監査ポリシーによって保護されていることを証明できます。彼らはグローバルオブジェクトアクセス監査ポリシー設定の内容を確認することでこのタスクを実行できます。例えば、監査人が「グループ管理者によって行われたすべての変更を追跡する」というポリシー設定を見た場合、このポリシーが有効であることがわかります。

リソースSACLは診断シナリオにも役立ちます。例えば、管理者は次の方法でシステム内のどのオブジェクトがユーザーのアクセスを拒否しているかを迅速に特定できます:
- 特定のユーザーのすべての活動をログに記録するようにグローバルオブジェクトアクセス監査ポリシーを設定する
- ファイルシステムまたはレジストリの「アクセス拒否」イベントを追跡するようにポリシーを有効にすることが役立ちます

> [!NOTE]
> ファイルまたはフォルダのSACLとグローバルオブジェクトアクセス監査ポリシー設定（または単一のレジストリ設定SACLとグローバルオブジェクトアクセス監査ポリシー設定）がコンピュータに設定されている場合、有効なSACLはファイルまたはフォルダのSACLとグローバルオブジェクトアクセス監査ポリシーを組み合わせたものから導き出されます。これは、アクティビティがファイルまたはフォルダのSACLまたはグローバルオブジェクトアクセス監査ポリシーに一致する場合、監査イベントが生成されることを意味します。

このカテゴリには以下のサブカテゴリが含まれます:
-   [ファイルシステム (グローバルオブジェクトアクセス監査)](file-system-global-object-access-auditing.md)
-   [レジストリ (グローバルオブジェクトアクセス監査)](registry-global-object-access-auditing.md)

## 関連トピック

-   [基本的なセキュリティ監査ポリシー設定](basic-security-audit-policy-settings.md)
