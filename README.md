
# 🧠 Alibaba Cloud ECI Sentiment Analyzer Demo

A practical, lightweight demo showcasing AI inference simulation on **Alibaba Cloud Elastic Container Instance (ECI)**. Designed for customer workshops, cloud adoption sessions, and training programs across Malaysia, Indonesia, and beyond.

> Built by **Shahjawadali** — Senior Training Advisor, Alibaba Cloud

---

## 🎯 Purpose
This demo replaces abstract examples (like dice rolls) with a **real-world AI use case**: sentiment analysis. It demonstrates:
- Containerized AI-like workloads on ECI
- Per-instance state isolation
- CPU load simulation (for autoscaling demos)
- Health checks and observability
- Simple yet transparent logic for educational clarity

---

## 🚀 Quick Start

### Build & Run Locally
```bash
docker build -t sentiment-demo .
docker run -p 5000:5000 sentiment-demo

## Deploy to Alibaba Cloud ECI
- Push image to Alibaba Cloud Container Registry (ACR)
- Create ECI instance with:
- Image: your ACR image
- Port: 5000
- Assign an Elastic IP (EIP)
- Allow inbound traffic on port 5000 in Security Group
