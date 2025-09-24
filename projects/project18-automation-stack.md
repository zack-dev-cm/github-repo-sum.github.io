---
layout: default
title: 'Project18 Automation Stack'
---

**Description**: Gives B2B teams a ready-to-launch Telegram bot, Mini App (TWA), Android/iOS/WebApp, and lead funnel powered by agentic workflows.

**Long Description**: Project18 delivers a full automation stack that launches a Telegram bot, companion Mini App, and AI-routed lead funnel in minutes. Under the hood it unifies GPT-5 orchestration, reusable MCP tools, multi-tenant data stores, and telemetry guardrails to keep every customer touchpoint observable and adaptive. The deployment bundles cover every layer from client experiences to observability, so teams can ship confidently.

**Key Features**:
- Instant Telegram bot & Mini App deployment
- Agentic workflows nurturing inbound leads
- Unified telemetry and safety guardrails
- Deployment bundles covering clients, delivery, orchestration, data, integration, and operations

**Tech Stack**: GPT-5 orchestration, MCP tools, Multi-tenant data stores, Telemetry guardrails.

**Links**: [Live Demo](https://project018-mcp-1095464065298.us-east1.run.app/)

**Thumbnail**: ![Project18 Automation Stack](https://placehold.co/600x400?text=Project18 "Project18 Automation Stack")

**Topology Snapshot**:

```
Clients Layer
  - Telegram Bot
  - Telegram Mini App
  - Landing + Console
        |
        v
Edge & Delivery Layer (CDN / Edge Functions)
        |
        v
Gateway & Policy Layer (API Gateway + Auth)
        |
        v
+-----------------------------------------+
|           Orchestration Layer           |
| Router -> Persona -> Workflow -> ToolBus|
|                   |                     |
|                   v                     |
|         MCP Tool Mesh Bridge            |
+-----------------------------------------+
        |
        v
Data & Knowledge Layer
  - Tenant DB / Secrets
  - Vector Store / Memories
  - Object & Telemetry Stores
        |
        v
Integration Layer (Connectors via MCP)
        |
        v
Operations Layer (Console, Alerts, Runbooks)
```

