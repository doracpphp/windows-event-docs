---
title: レジストリ (グローバルオブジェクトアクセス監査)
description: 高度なセキュリティ監査ポリシー設定、レジストリ (グローバルオブジェクトアクセス監査) は、グローバルシステムアクセス制御リスト (SACL) を構成することを可能にします。
ms.assetid: 953bb1c1-3f76-43be-ba17-4aed2304f578
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

# レジストリ (グローバルオブジェクトアクセス監査)

このトピックは IT プロフェッショナル向けに、高度なセキュリティ監査ポリシー設定、**レジストリ (グローバルオブジェクトアクセス監査)** について説明します。これにより、コンピュータのレジストリにグローバルシステムアクセス制御リスト (SACL) を構成することができます。

このポリシーのプロパティページで **セキュリティの構成** チェックボックスを選択すると、ユーザーまたはグループをグローバル SACL に追加できます。これにより、レジストリのオブジェクトタイプごとにコンピュータシステムアクセス制御リスト (SACL) を定義することができます。指定された SACL は、その後すべてのレジストリオブジェクトタイプに自動的に適用されます。

このポリシー設定は、オブジェクトアクセスの **レジストリ** セキュリティポリシー設定と組み合わせて使用する必要があります。詳細については、[レジストリの監査](audit-registry.md) を参照してください。

## 関連トピック

- [高度なセキュリティ監査ポリシー設定](advanced-security-audit-policy-settings.md)
