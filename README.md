# 讓 ChatGPT 正常說人話 · v2.6.0

讓 AI 用自然中文把事情講清楚：讀者知道你在說什麼、為什麼這樣判斷，以及建議怎麼做。保留原意、數字、證據強度與必要條件，刪掉沒有幫助的套話和重複免責。

規則與範例以**臺灣繁體中文**為主。英文尚未充分測試。目前版本為 **v2.6.0**。

[下載 v2.6.0 完整 Skill ZIP](https://github.com/jason840709/let-chatgpt-say-like-person/releases/download/v2.6.0/let-chatgpt-say-like-person-v2.6.0.zip) · [下載離線閱讀頁](https://github.com/jason840709/let-chatgpt-say-like-person/releases/download/v2.6.0/index.html) · [版本修改紀錄](CHANGELOG.md) · [驗證範圍](VALIDATION.md)

## 適合處理什麼？

- 把 AI 腔、翻譯腔或過度壓縮的文字改成自然中文。
- 解釋研究與技術方法，讓讀者看懂操作、比較條件和判斷理由。
- 寫作或審閱報告、論文草稿、決策建議，以及 README、AGENTS 等交接文件。
- 清楚交代數字的對象、比例分母、比較基準與證據能支持的結論。

普通對話可保留自然語氣，正式文件則去掉客套前言與後續邀請。純程式修改、原文搬運和單純檔案轉換，不因碰到數字或文件格式就啟動研究審查。

## v2.6.0 改了什麼？

以前的規則集中在很長的 SKILL.md。新版保留短入口，將細則放入七份 `references/`，依任務讀取相關章節。

這次也修正了幾項實際要求：

1. **檢查依內容分級。** 短回答與局部潤稿做核心檢查；完整方法解釋與重要決策做較完整審查。聊天中的完整說明同樣適用，PDF 等檔案形式另外做版面檢查。
2. **改寫守住來源。** 來源衝突分別呈現，不自行融合成新版本；保留判斷依據、時間和負責動作的人，不把 AI 建議改成人類命令。
3. **代稱看理解，不查禁字。** 「前者」「這個」若能從當句及前一句辨認，可以自然使用；需要讀者回頭猜時才展開。
4. **增加資訊不能靠編造。** 刪掉重複句本身就是合格改寫。新增發現要有來源，計算差值則清楚保留原數字。
5. **檢查範圍一致。** 沒有統計推論或互動元件，就略過相應項目。工具不支援獨立代理時，採作者逐句檢查並如實交代。

完整變動見 [CHANGELOG.md](CHANGELOG.md)。

## 怎麼使用？

### 支援 Skill 的工具

下載上面的 ZIP，保留其中整個 `let-chatgpt-say-like-person/` 資料夾與內部結構，再依工具的說明匯入或放入 skill 目錄。啟用方式因產品而異，對外 skill 名稱仍是 **`let-chatgpt-say-like-person`**。

原始碼的 `SKILL.md` 位於儲存庫根目錄；若下載 GitHub 的原始碼 ZIP，安裝時選擇直接包含 `SKILL.md` 的那一層資料夾。

### 直接提供給 AI

請先讓 AI 讀取 [SKILL.md](SKILL.md)，並確保它能取得同目錄的 [references/](references/)；入口會指示何時讀哪些細則。只貼 SKILL.md 不包含整套細則。只支援單一文字輸入的工具，可依任務一併貼入所需參考章節。

```text
請使用 let-chatgpt-say-like-person 改寫下面的文章。
讀者是沒有參與專案的工程師。
請保留原意、數字、證據強度與必要條件，讓讀者看懂做法和理由。

［貼上原文］
```

撰寫新文件時，可補上資料、讀者與用途：

```text
請依照這份 skill，用臺灣繁體中文撰寫技術說明。
讀者是第一次接觸專案的同事，目的是理解問題、做法與目前結果。
請以附上的材料為依據，說清楚判斷理由；缺少的資訊請具體指出。
```

## 檔案

| 檔案 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | 核心原則、任務路由與檢查範圍 |
| [references/](references/) | 讀者理解、數字統計、主張證據、對話介面、自然中文、文件與完整審查細則 |
| [agents/openai.yaml](agents/openai.yaml) | 支援此格式的工具使用的介面設定 |
| [assets/icon.svg](assets/icon.svg) | 圖示 |
| [CHANGELOG.md](CHANGELOG.md) | 版本修改紀錄 |
| [VALIDATION.md](VALIDATION.md) | 本版實際測過的內容與驗證限制 |
| [index.html](https://github.com/jason840709/let-chatgpt-say-like-person/blob/main/index.html) | 儲存庫另附的完整離線閱讀頁；下載後以瀏覽器開啟，不在 Skill ZIP 內 |
| [scripts/build_release.py](https://github.com/jason840709/let-chatgpt-say-like-person/blob/main/scripts/build_release.py) | 儲存庫另附的重建腳本，可產生閱讀頁、Skill ZIP 與 SHA-256 清單 |

寫作規則可獨立使用；讀取材料、重算數字和檢查成品，需要 AI 環境提供相應工具。獨立代理不是安裝必要條件。

## 驗證與回報問題

2.6.0 已做格式檢查、獨立文件審查，以及三組新舊版實際輸出比較；最後修訂另有定向回歸測試。測試重點是原意、數字、理由、來源與決策條件，而不是以字數少或否定詞少判斷品質。案例數有限，尚未完成跨模型、各產品自動觸發或使用者盲評，詳見 [驗證範圍](VALIDATION.md)。

歡迎在 GitHub Issues 提供難讀的原回答、希望的改寫，以及模型與使用情境。具體例子有助於判斷是哪條規則沒有落實。貼上材料前，請移除私人資訊。
