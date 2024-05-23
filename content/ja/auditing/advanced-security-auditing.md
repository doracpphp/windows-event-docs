---
title: 高度なセキュリティ監査ポリシー
description: 高度なセキュリティ監査ポリシー設定は基本ポリシーと重複しているように見えるかもしれませんが、記録および適用の方法が異なります。詳細はこちらをご覧ください。
ms.assetid: 6FE8AC10-F48E-4BBF-979B-43A5DFDC5DFC
ms.reviewer:
ms.author: vinpa
ms.mktglfcycl: deploy
ms.sitesec: library
ms.pagetype: security
ms.localizationpriority: low
author: vinaypamnani-msft
manager: aaroncz
audience: ITPro
ms.topic: reference
ms.date: 09/6/2021
---

# 高度なセキュリティ監査ポリシー

高度なセキュリティ監査ポリシー設定は、**セキュリティ設定\\高度な監査ポリシー構成\\システム監査ポリシー**にあり、基本的なセキュリティ監査ポリシーと重複しているように見えますが、記録および適用の方法が異なります。
ローカルセキュリティポリシースナップインを使用してローカルコンピューターに基本的な監査ポリシー設定を適用すると、効果的な監査ポリシーを編集していることになります。そのため、基本的な監査ポリシー設定に加えた変更はAuditpol.exeに正確に構成されたとおりに表示されます。Windows 7以降では、高度なセキュリティ監査ポリシーはグループポリシーを使用して制御できます。

## このセクションでは

| 記事 | 説明 |
| - | - |
| [高度なセキュリティ監査ポリシーの計画と展開](planning-and-deploying-advanced-security-audit-policies.md) | ITプロフェッショナル向けのこの記事では、セキュリティポリシープランナーが考慮すべきオプションと、ネットワークに高度なセキュリティ監査ポリシーを含む効果的なセキュリティ監査ポリシーを展開するために完了する必要があるタスクについて説明します。 |
| [高度なセキュリティ監査のFAQ](advanced-security-auditing-faq.yml) | ITプロフェッショナル向けのこの記事では、セキュリティ監査ポリシーの理解、展開、および管理に関する質問と回答を一覧表示します。 |
| [動的アクセス制御オブジェクトを監視するための高度なセキュリティ監査オプションの使用](using-advanced-security-auditing-options-to-monitor-dynamic-access-control-objects.md) | このガイドでは、Windows 8およびWindows Server 2012で導入された設定とイベントを通じて可能になった高度なセキュリティ監査機能の設定プロセスについて説明します。 |
| [高度なセキュリティ監査ポリシー設定](advanced-security-audit-policy-settings.md) | ITプロフェッショナル向けのこのリファレンスでは、Windowsの高度な監査ポリシー設定とそれらが生成する監査イベントに関する情報を提供します。 |