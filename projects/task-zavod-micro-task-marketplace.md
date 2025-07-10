---
layout: default
title: Task Zavod – Micro-Task Marketplace
---

**Description**: A platform for building, validating, and automatically processing payouts for micro-tasks. It addresses the complexities of crowdsourcing QA by allowing business users to define tasks in free-form text, which VLMs convert to structured tasks. Workers complete tasks via web or Telegram, with VLM-based auto-approval.
- Auto debug reports and feature requests for automated developer tasks
- Support real task performers  
- Reward and easy payment system
- Support vlm gui workers
- Integration with OpenAI Codex
- Integration with GCP Cloud Run/Cloud Build
- Support instant debugging%shipping, full ci-cd circle
- Support realtime app perfomance monitoring

**Problem**: For businesses:  Speed up software iteration for pre and post production, reduce resources need
             For task performers: Get decent and fast payments, Be respectful for job see how your work inpact the other people through the task you've done. 
             
             (Example : tasks is test button in the tg bot, task performers found the bug, and this bug is fixed on next release. Feedback and reward is provided to task performers)



**Key Features**: VLM-powered task structuring, automated approval & payout, web & Telegram interfaces, live status polling.

**Tech Stack**: Tornado (Web + SSE), SQLite, OpenAI, custom VLM, Telegram Bot API.

**Try App**: [Task Zavod](https://mcp-taskforge-1095464065298.us-central1.run.app/task_zavod)

<img src="samples/task_zavod/task_zavod.jpg" width="200" alt="Task Zavod example">

<img src="samples/task_zavod/task_zavod2.jpg" width="200" alt="Task Zavod example 2">

---
