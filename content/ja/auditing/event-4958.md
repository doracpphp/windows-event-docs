---
title: 4958(F) Windows Firewall は、このコンピューターで構成されていない項目を参照しているため、次のルールを適用しませんでした。
description: このコンピューターで構成されていない項目を参照しているため、Windows Firewall が次のルールを適用しなかったことを示すセキュリティ イベント 4958(F) について説明します。
ms.pagetype: security
ms.mktglfcycl: deploy
ms.sitesec: library
ms.localizationpriority: low
author: vinaypamnani-msft
ms.date: 09/08/2021
ms.reviewer: 
manager: aaroncz
ms.author: vinpa
ms.topic: reference
---

# 4958(F): Windows Firewall は、このコンピューターで構成されていない項目を参照しているため、次のルールを適用しませんでした。

高度なセキュリティを備えた Windows Firewall は、ローカル コンピューターで解決できないパラメーターを含むルールを処理しました。そのため、このルールはコンピューター上で強制できず、ファイアウォールの実行時状態から除外されます。この除外は必ずしもエラーではありません。適用されたコンピューターでのルールの適用性を確認してください。

このドキュメントには、このイベントの例はありません。

***サブカテゴリ:***&nbsp;[MPSSVC ルールレベル ポリシー変更の監査](audit-mpssvc-rule-level-policy-change.md)

***イベント スキーマ:***

*Windows Firewall は、このコンピューターで構成されていない項目を参照しているため、次のルールを適用しませんでした:
ルール情報:
%tID:%t%1
%t名前:%t%2
エラー情報:
%tエラー:%t%3
%t理由:%t%4*

***必要なサーバー ロール:*** なし。

***最小 OS バージョン:*** Windows Server 2008、Windows Vista。

***イベント バージョン:*** 0。

## セキュリティ監視の推奨事項

-   このイベントは、ソフトウェアの問題、Windows Firewall レジストリ エラーまたは破損、またはグループ ポリシー設定の誤設定の兆候である可能性があります。このイベントを監視し、状態の原因を調査することをお勧めします。通常、このイベントは構成の問題を示しており、セキュリティの問題を示しているわけではありません。
