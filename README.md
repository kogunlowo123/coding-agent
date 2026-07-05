# Coding Agent

[![CI](https://github.com/kogunlowo123/coding-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/coding-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Software Engineering | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

AI coding assistant that generates production-grade code from natural language specifications, understands codebase context, follows project conventions, and produces type-safe, tested implementations across multiple languages and frameworks.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `generate_code` | Generate production code from a specification |
| `explain_code` | Explain what a code block does in plain language |
| `complete_code` | Complete partial code with context-aware suggestions |
| `convert_code` | Convert code between languages or frameworks |
| `optimize_code` | Suggest performance and readability improvements |
| `scaffold_project` | Generate project boilerplate and directory structure |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/generate` | Generate code from specification |
| `POST` | `/api/v1/complete` | Context-aware code completion |
| `POST` | `/api/v1/explain` | Explain code in natural language |
| `POST` | `/api/v1/convert` | Convert between languages |
| `POST` | `/api/v1/optimize` | Suggest code optimizations |
| `POST` | `/api/v1/scaffold` | Generate project scaffolding |

## Features

- Code Generation
- Context Aware Completion
- Multi Language
- Convention Adherence
- Inline Documentation

## Integrations

- Github Connector
- Gitlab Connector
- Language Server
- Package Registry

## Architecture

```
coding-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── coding_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 6 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 6 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 4 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Custom LLM + Language Servers**

---

Built as part of the Enterprise AI Agent Platform.
