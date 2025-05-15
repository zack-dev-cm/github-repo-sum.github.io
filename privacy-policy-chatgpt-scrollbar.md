# Privacy Policy – Chat Navigator Extension  
_Last updated: 15 May 2025_

## 1.  Overview  
Chat Navigator (“**the Extension**”) adds a custom scrollbar, prompt-autocomplete and (optionally) crowd-sourced **Trending Prompts** to ChatGPT, DeepSeek Chat and Google AI Studio. This policy explains what data the Extension may handle and how it is protected.

---

## 2.  Data We Store

| Data | Where | Purpose | Sent off-device? |
|------|-------|---------|------------------|
| **UI preferences** (scrollbar colour, size, auto-hide, etc.) | `chrome.storage.sync` on your Google account | Restore your look & feel on every machine | **No** |
| **Custom autocomplete prompts** you save | `chrome.storage.sync` | Make your personal snippets available in the textarea dropdown | **No** |
| **Prompt text** you choose to share *(optional, disabled at any time)* | Secure POST to `https://adfeed-…run.app` | Build aggregated “Trending / Latest prompts” list for all users | **Yes – only when the “Share your prompt” switch is ON** |

*No other information (chat content, page history, personal identifiers, cookies, etc.) is accessed, collected or stored.*

---

## 3.  How We Use the Data  
* Provide and customise the on-page scrollbar and autocomplete UI.  
* If **Prompt Sharing** is enabled, upload the raw prompt text **only** (no headers, no user IDs) to calculate community statistics.

---

## 4.  Data Sharing & Disclosure  
* We **never sell** or transfer data to third parties.  
* Shared prompts are stored without personal identifiers and used exclusively for aggregate ranking.  

---

## 5.  Security  
All communication with the Trending-Prompts API uses HTTPS. Data in `chrome.storage.sync` is encrypted in transit and at rest by Google. Despite best efforts, no system can guarantee absolute security.

---

## 6.  Your Choices  
* **Settings panel → “Prompt Sharing” switch** – turn off at any time to stop all uploads (previously shared prompts remain anonymous and cannot be linked back to you).  
* **Reset to Defaults** – wipes all locally stored settings and custom prompts.  

---

## 7.  Updates to this Policy  
We may revise this notice when features change. The latest version is always bundled with the Extension and posted on the project’s GitHub page. Continued use after an update constitutes acceptance.

---

## 8.  Contact  
Questions or concerns? Email **kaisenaiko@gmail.com**.
