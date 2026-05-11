# Enterprise AI-Native ERP Platform

A modular, production-grade ERP platform inspired by SAP and Odoo, architected for the cloud-native era with AI-first workflows.

---

## 🚀 Overview

This ERP is a **Modular Monolith** designed for high scalability, strict tenant isolation, and intelligent automation. It serves as a unified core for managing complex business processes across various domains including Finance, HR, Supply Chain, and CRM.

### Key Architectural Pillars:
- **Multi-Tenancy**: Hard data isolation using PostgreSQL schema-per-tenant strategy via `django-tenants`.
- **Domain-Driven Design (DDD)**: Each business module (HR, Finance, etc.) is a bounded context with its own models and logic.
- **AI-Native**: Integrated LLM services for financial forecasting, anomaly detection, and workflow optimization.
- **Event-Driven**: Internal signaling for cross-module orchestration (e.g., Inventory depletion triggers Procurement).

---

## 🏗️ Technical Stack

- **Backend**: Python 3.12 + Django 5.x + Django REST Framework (DRF)
- **Frontend**: Next.js 14 (App Router) + TypeScript + TailwindCSS + Shadcn/UI
- **Database**: PostgreSQL 15 (with Schema-based multi-tenancy)
- **Caching/Messaging**: Redis 7
- **AI**: OpenAI GPT-4 / LangChain Integration
- **DevOps**: Docker, Kubernetes (K8s), GitHub Actions CI/CD

---

## 📂 Project Structure

```text
/erp-platform
├── /apps
│   └── /web-portal          # Next.js Frontend Portal (Next.js, TS, Tailwind)
├── /backend
│   └── /core-service        # Django Modular Monolith
│       ├── /erp_core        # Project config, settings, and URL routing
│       ├── /tenants         # Tenant management and schema routing
│       ├── /identity        # IAM, RBAC, and Auth services
│       ├── /organizations   # Corporate hierarchy and branch management
│       ├── /hrms            # Workforce, Payroll, and Attendance
│       ├── /finance         # General Ledger, AR/AP, and Taxation
│       ├── /workflow        # Orchestration engine for approvals & triggers
│       ├── /ai_intelligence # AI/ML agents and analytics services
│       └── /common          # Shared utilities and immutable Audit logging
├── /infrastructure
│   ├── docker-compose.yml   # Local development orchestration
│   └── /k8s                 # Production Kubernetes manifests
└── /docs
    ├── /architecture        # ERDs, Flowcharts, and ADRs
    └── /api                 # OpenAPI (Swagger) specifications
```

---

## 🧩 Core Modules

### 1. Identity & Access (IAM)
- **Role-Based Access Control (RBAC)**: Fine-grained permissions (View-only vs. Execute).
- **Security**: JWT with Refresh tokens and MFA support.
- **Audit**: Every action is captured in an immutable audit trail with `old_values` vs `new_values` JSON diffs.

### 2. HR & Workforce (HRMS)
- **Employee Lifecycle**: From onboarding to exit.
- **Payroll**: Automated salary calculations and tax deductions.
- **Attendance**: Real-time tracking and leave management integrated with Workflow Approvals.

### 3. Financial Management
- **General Ledger**: Double-entry bookkeeping system.
- **AR/AP**: Automated invoicing and vendor payment tracking.
- **Reporting**: Real-time balance sheets and P&L statements.

### 4. Workflow Orchestration
- **Approval Chains**: Dynamic N-level approvals for financial transactions.
- **Status Machine**: Track the lifecycle of vouchers, leaves, and purchase orders.

### 5. AI Business Intelligence
- **Smart Summaries**: AI-generated financial month-end reports.
- **Anomaly Detection**: Flags suspicious transactions or duplicate invoices.
- **Copilot**: Natural language interface for enterprise data querying.

---

## 🛠️ Getting Started

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.12+

### 1. Setup Infrastructure
```bash
cd infrastructure
docker-compose up -d
```

### 2. Initialize Backend
```bash
cd backend/core-service
python -m pip install -r requirements.txt
python manage.py migrate_schemas --shared
python manage.py create_tenant_superuser  # Create the global admin
```

### 3. Initialize Frontend
```bash
cd apps/web-portal
npm install
npm run dev
```

---

## 📈 Roadmap

- [ ] **Phase 1**: Core Tenant Engine & Auth (COMPLETED)
- [ ] **Phase 2**: Global Finance & HR Schema (COMPLETED)
- [ ] **Phase 3**: AI Integration for Financial Forecasting
- [ ] **Phase 4**: Real-time Notification via WebSockets / Redis PubSub
- [ ] **Phase 5**: Mobile Application (React Native)

---

## 🛡️ Security & Scalability
- **Horizontal Scaling**: Core service is stateless; designed for K8s HPA (Horizontal Pod Autoscaler).
- **Tenant Isolation**: Separate DB schemas ensure no data leakage between enterprise clients.
- **API Gateway**: Rate limiting and CORS policies configured in `erp_core/settings.py`.

---

## 📄 License
Enterprise Proprietary - Modern ERP Systems.
