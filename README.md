# BigDSA — Backend

> AST-powered Big O complexity analysis

## What is BIGDSA - Backend?

BigDSA Backend is a REST API for analyzing the time complexity (Big O) of Python code using AST parsing and optional AI explanation via AI Model.
The name is a double reference — to **Big O notation** (the backbone of algorithm analysis) and to **Data Structures & Algorithms (DSA)**.

## Stack

- **FastAPI** — web framework
- **ast** — code parsing and AST traversal
- **radon** — code metrics
- **Redis** — caching analysis results
- **Groq (llama-3.3-70b-versatile)** — AI explanations
- **uv** — dependency management
- **Ruff / Black** — linting and formatting

---

## Architecture

```
app/
├── main.py                     # FastAPI app entry point
├── core/
│   ├── config.py               # Settings via pydantic-settings (.env)
│   ├── middleware.py            # CORS middleware setup
│   └── exceptions.py           # Custom exception types
├── features/
│   ├── temporal_complexity/    # Time complexity analysis feature
│   │   ├── router.py           # POST /api/analyze/temporal
│   │   ├── service.py          # Orchestration: cache → analyze → AI
│   │   ├── analyzer.py         # AST-based Big O inference
│   │   ├── request.py          # Request schema (Pydantic)
│   │   └── dto.py              # Response DTO
│   ├── spatial_complexity/     # Space complexity (WIP)
│   └── reports/                # Shared report value objects
│       ├── temporal_analysis_report.py
│       └── temporal_ai_report.py
└── shared/
    ├── ast/
    │   ├── parser.py           # Python AST parser wrapper
    │   ├── fingerprint.py      # Code fingerprint for cache keys
    │   ├── value_objects/      # NormalizedCode value object
    │   └── visitors/           # Loop and recursion AST visitors
    ├── cache/
    │   ├── service.py          # Redis get/set abstraction
    │   ├── client.py           # Redis client factory
    │   └── mixin.py            # CacheMixin for services
    └── ai/
        ├── ai.py               # Groq API wrapper
        ├── client.py           # AI client factory
        └── service.py          # AI prompt orchestration
```

### Request flow

```
POST /api/analyze/temporal
        │
        ▼
TemporalComplexityService
        │
        ├─ NormalizedCode + Fingerprint (cache key)
        │
        ├─ Cache hit? ──yes──▶ return cached TemporalAnalysisReport
        │
        └─ Cache miss ──▶ TemporalComplexityAnalyzer (AST)
                               │
                               ├─ LoopVisitors     → max loop depth
                               └─ RecursionVisitors → recursive functions
                               │
                               ▼
                         infer Big O notation
                               │
                      (if explain_ai=true)
                               │
                               ▼
                         AIService → Groq LLM → TemporalAIReport
```

---

## Endpoints

| Method | Path                    | Description                            |
| ------ | ----------------------- | -------------------------------------- |
| `GET`  | `/health`               | Health check                           |
| `POST` | `/api/analyze/temporal` | Analyze time complexity of Python code |

### `POST /api/analyze/temporal`

**Request body:**

```json
{
  "code": "for i in range(n):\n    for j in range(n):\n        pass",
  "explain_ai": false
}
```

**Response:**

```json
{
  "analysis": {
    "time_complexity": "O(n²)",
    "max_loop_depth": 2,
    "recursive": false
  },
  "ai": null
}
```

Set `explain_ai: true` to include an LLM-generated explanation of the result.

---

## Setup

### Prerequisites

- Python 3.12+
- Redis running on `localhost:6379`
- [uv](https://docs.astral.sh/uv/) installed

### 1. Clone and enter the project

```bash
mkdir big-dsa
cd big-dsa
git clone https://github.com/Riodev28/be-big-dsa.git backend
cd backend
```

### 2. Create the virtual environment and install dependencies

```bash
uv sync
```

To include dev dependencies:

```bash
uv sync --group dev
```

### 3. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env`:

```env
CACHE_URL=redis://localhost:6379
AI_API_KEY=your_groq_api_key_here
```

Get a free Groq API key at [console.groq.com](https://console.groq.com).

### 4. Start Redis

```bash
# Docker
docker run -d -p 6379:6379 redis
```

### 5. Run the server

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

Interactive docs: `http://localhost:8000/docs`

---

## Development

### Run tests

```bash
uv run pytest
```

### Lint

```bash
uv run ruff check .
```

### Format

```bash
uv run black .
```

### Run lint and format together

```bash
uv run ruff check . && uv run black .
```
