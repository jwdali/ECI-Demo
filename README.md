
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


# ### ✅ Scoring Rules

| Condition                                      | Sentiment Label | Confidence (%)                     |
|------------------------------------------------|------------------|------------------------------------|
| More positive words than negative              | `"Positive"`     | `min(count_positive × 20, 100)`    |
| More negative words than positive              | `"Negative"`     | `min(count_negative × 20, 100)`    |
| Equal counts or no keywords matched            | `"Neutral"`      | `50`                               |

### 🧮 Examples

| Input Text                              | Matches                          | Sentiment  | Confidence |
|----------------------------------------|----------------------------------|------------|------------|
| `"I love this service!"`               | `love` → +1 positive            | Positive   | 20%        |
| `"This is amazing and great!"`         | `amazing`, `great` → +2         | Positive   | 40%        |
| `"Terrible experience, worst ever."`   | `terrible`, `worst` → +2        | Negative   | 40%        |
| `"It's okay."`                         | No keywords                     | Neutral    | 50%        |
| `"Good but bad"`                       | 1 positive, 1 negative          | Neutral    | 50%        |

> ⚠️ **Note**: Matching is **substring-based** (not word-boundary aware).  
> Example: `"goods"` will match `"good"`.  
> In production, use tokenization or a real NLP model — but for training demos, simplicity and transparency win.
