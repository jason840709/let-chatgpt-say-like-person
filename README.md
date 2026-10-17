# 讓 ChatGPT 正常說人話 · v2.8.1

讓 AI 用自然的臺灣繁體中文，把誰做了什麼、為什麼、結果代表什麼說清楚。改寫保留原意、數字、理由與證據強度，減少模糊代稱、未定義術語、過度壓縮與反覆免責。

[下載 v2.8.1 完整 Skill ZIP](https://github.com/jason840709/let-chatgpt-say-like-person/releases/download/v2.8.1/let-chatgpt-say-like-person-v2.8.1.zip) · [離線閱讀頁](https://github.com/jason840709/let-chatgpt-say-like-person/releases/download/v2.8.1/index.html) · [從 2.6.0 升級的差異](docs/upgrade-v2.6.0-to-v2.8.1.md) · [驗證範圍](VALIDATION.md)

## 相較公開版 2.6.0，這次改了什麼？

上一個 GitHub 正式版本是 **2.6.0**。2.7.x 與 2.8.0 是中間開發版本，這次直接發布 **2.8.1**。

- **讀到當句就能理解。** 主語、資料區段、自訂指標與模型依據要在用來推論之前交代，後文不能替前文補洞。清楚承接同一主語的句子可以保留，不必每句都添加「我們」。
- **改寫不偷改事實。** 保留建議與已完成工作的差別，檢查公式在一般參數下是否仍符合文字定義；不同案例的資料與技能裡的安排，不寫成眼前案件的既有事實。
- **減少重複讀取。** 六項核心原則集中在入口，示例與專項細則按需查閱。短回答通常只讀入口；重要說明加讀審稿手冊，修訂後複核受影響處。
- **審查記錄更準確。** 全文順讀與真正逐句供稿分開記錄；使用者明確要求逐句供稿時照做。歷史測試保留原受測版本，不因升版而改名成新版通過。

日常入口由 **15,335 bytes** 縮至 **8,329 bytes**，文字量減少 **45.7%**。

入口加審稿手冊由 **28,820 bytes** 縮至 **13,060 bytes**，文字量減少 **54.7%**。

以上比較相同公開檔案範圍，並非模型 token、費用或帳號額度的實測節省率。規則變短也不自動代表品質更高；測過的內容與限制見 [VALIDATION.md](VALIDATION.md)。

## 怎麼使用？

下載完整 ZIP，保留其中整個 **`let-chatgpt-say-like-person/`** 資料夾及 `references/`，再依所用工具的方式匯入。既有使用者可用新版資料夾取代舊版；公開啟用名稱仍是 **`let-chatgpt-say-like-person`**，不需改名。

如果從 GitHub 下載原始碼 ZIP，安裝時選擇直接包含 `SKILL.md` 的那一層。支援多種 AI 工具的方式各有差異，本專案不宣稱已逐一測過所有產品的自動觸發。

也可直接讓 AI 讀取 [SKILL.md](SKILL.md)，並確保它能取得相鄰的 [references/](references/)。只貼入口不包含全部專項細則。

```text
請使用 let-chatgpt-say-like-person 改寫下面的文章。
讀者是第一次接觸這個專案的同事。
請保留原意、數字、判斷理由和必要條件；不要補造未提供的事實。

［貼上原文］
```

普通對話和局部改寫通常只需核心自檢；完整研究、方法或重要決策說明，需要更完整的理解與證據檢查。獨立代理不是安裝必要條件，工具不支援時按實際完成範圍回報。

## 檔案與下載

| 檔案 | 用途 |
|---|---|
| [SKILL.md](SKILL.md) | 核心原則與按需閱讀入口 |
| [references/](references/) | 理解順序、數字統計、證據、中文句型、文件與審查細則 |
| [CHANGELOG.md](CHANGELOG.md) | 本次與歷史公開版本的修改紀錄 |
| [VALIDATION.md](VALIDATION.md) | 實際測試及其限制 |
| [升級差異](docs/upgrade-v2.6.0-to-v2.8.1.md) | 2.6.0 → 2.8.1 的方法、大小與相容性比較 |
| [index.html](index.html) | 由本版來源產生的離線閱讀頁；另附於 Release，不放入 Skill ZIP |
| [scripts/build_release.py](scripts/build_release.py) | 重建閱讀頁、Skill ZIP、檔案清單及 SHA-256 |

介面設定與圖示放在 `agents/`、`assets/`。重建檔案使用 Python 3 和 Markdown 套件；安裝或讀取 Skill 不需要執行建置腳本。

歡迎在 Issues 提供原回答、希望如何改善，以及所用模型與情境。請先移除材料中的私人資訊。
