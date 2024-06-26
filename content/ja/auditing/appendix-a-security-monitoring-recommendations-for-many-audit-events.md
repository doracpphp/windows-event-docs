---
title: 付録 A、多くの監査イベントに対するセキュリティ監視の推奨事項
description: 特定のクラスのセキュリティ監査イベントに必要な監視の種類についての推奨事項を学びます。
ms.pagetype: security
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: low
author: vinaypamnani-msft
ms.date: 09/06/2021
ms.reviewer: 
manager: aaroncz
ms.author: vinpa
ms.topic: reference
---

# 付録 A: 多くの監査イベントに対するセキュリティ監視の推奨事項

このドキュメント、[高度なセキュリティ監査ポリシー設定](advanced-security-audit-policy-settings.md)のリファレンスは、個々の監査イベントに関する情報を提供し、それらを監査カテゴリおよびサブカテゴリ内にリストします。ただし、以下の全体的な推奨事項が適用されるイベントが多数あります。このドキュメント全体の「推奨事項」セクションからこの付録へのリンクがあります。

| **必要な監視の種類**                                                                                                                                                                                                                                                                                   | **推奨事項**                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **高価値アカウント**: 各アクションを監視する必要がある高価値のドメインまたはローカルアカウントがあるかもしれません。<br>高価値アカウントの例としては、データベース管理者、組み込みのローカル管理者アカウント、ドメイン管理者、サービスアカウント、ドメインコントローラーアカウントなどがあります。 | 高価値アカウントに対応する**「Subject\\Security ID」**の関連イベントを監視します。                                                              |
| **異常または悪意のある行動**: 異常を検出したり、潜在的な悪意のある行動を監視するための特定の要件があるかもしれません。例えば、勤務時間外のアカウント使用を監視する必要があるかもしれません。                                                                                | 異常または悪意のある行動を監視する場合、**「Subject\\Security ID」**（他の情報と共に）を使用して特定のアカウントがどのようにまたはいつ使用されているかを監視します。     |
| **非アクティブアカウント**: 非アクティブ、無効、またはゲストアカウント、または決して使用されるべきではない他のアカウントがあるかもしれません。                                                                                                                                                                                     | 使用されるべきではないアカウントに対応する**「Subject\\Security ID」**の関連イベントを監視します。                                                          |
| **アカウントの許可リスト**: 特定のイベントに対応するアクションを実行することが許可されているアカウントの特定の許可リストがあるかもしれません。                                                                                                                                                      | 許可リスト外のアカウントに対する**「Subject\\Security ID」**の関連イベントを監視します。                                                                 |
| **異なる種類のアカウント**: 特定のアクションが特定のアカウントタイプ（例えば、ローカルまたはドメインアカウント、マシンまたはユーザーアカウント、ベンダーまたは従業員アカウントなど）によってのみ実行されることを確認したいかもしれません。                                                                                 | 監視したいアクションに対応するイベントを特定し、それらのイベントについて**「Subject\\Security ID」**を確認してアカウントタイプが期待通りであるかを確認します。 |
| **外部アカウント**: 別のドメインからのアカウントや、特定のアクション（特定のイベントで表される）を実行することが許可されていない「外部」アカウントを監視しているかもしれません。                                                                                                                     | 別のドメインからのアカウントや「外部」アカウントに対応する**「Subject\\Account Domain」**の特定のイベントを監視します。                                         |
| **使用が制限されたコンピューターやデバイス**: 特定の人（アカウント）が通常はアクションを実行しない特定のコンピューター、マシン、またはデバイスがあるかもしれません。                                                                                                                                      | 関心のあるアクションを実行する**「Subject\\Security ID」**に対してターゲット**コンピューター:**（または他のターゲットデバイス）を監視します。                                 |
| **アカウント命名規則**: 組織にはアカウント名に対する特定の命名規則があるかもしれません。                                                                                                                                                                                                       | 命名規則に従わない名前に対して**「Subject\\Account Name」**を監視します。                                                                                        |

