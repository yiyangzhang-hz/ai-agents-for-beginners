<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e4e06d3b5d6207459a019c05fee5eb4b",
  "translation_date": "2025-07-12T10:37:32+00:00",
  "source_file": "07-planning-design/README.md",
  "language_code": "hk"
}
-->
for 解決複雜任務。

## 總結

本文介紹了一個範例，說明如何建立一個能動態選擇已定義可用代理的規劃器。規劃器的輸出會將任務拆解並分配給代理執行，假設這些代理能存取執行任務所需的功能或工具。除了代理之外，還可以加入其他模式，如反思、摘要器和輪流聊天，以進一步自訂。

## 額外資源

* AutoGen Magnetic One - 一個通用的多代理系統，專門用於解決複雜任務，並在多個具挑戰性的代理基準測試中取得了優異成績。參考資料：

. 在此實作中，協調者會建立特定任務的計劃，並將這些任務委派給可用的代理。除了規劃外，協調者還會使用追蹤機制來監控任務進度，並在需要時重新規劃。

## 上一課

[建立值得信賴的 AI 代理](../06-building-trustworthy-agents/README.md)

## 下一課

[多代理設計模式](../08-multi-agent/README.md)

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或誤釋承擔責任。