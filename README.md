# 🚀 AI Document Portal

> **Enterprise-grade document intelligence powered by conversational AI**

Transform your document workflows with intelligent analysis, comparison, and chat capabilities. Built with FastAPI, LangChain, and modern RAG architecture.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green.svg)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://docker.com)
[![AWS](https://img.shields.io/badge/AWS-ECS%20Fargate-orange.svg)](https://aws.amazon.com/ecs)

## ✨ Features

### 🔍 **Document Analysis**
- Intelligent metadata extraction
- Structured document summaries  
- Multi-format support (PDF, DOCX, TXT)
- Batch processing capabilities

### 🆚 **Document Comparison**
- Page-by-page diff analysis
- AI-powered change detection
- Structured comparison reports
- Version control insights

### 💬 **Conversational RAG**
- Chat with single or multiple documents
- Context-aware responses
- Session-based memory
- Multi-document cross-referencing

### 🏢 **Enterprise Ready**
- Production FastAPI backend
- Modern glassmorphism UI
- AWS ECS Fargate deployment
- Auto-scaling infrastructure
- Comprehensive logging

## 🏗️ Architecture

```
Frontend (HTML/CSS/JS) ↔ FastAPI Backend ↔ Document Modules
                                     ↕
                           FAISS Vector Database
                                     ↕
                         Multi-LLM Support (Groq/Gemini)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Docker (optional)
- LLM API keys (Groq/Google)

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/document-portal.git
   cd document-portal
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080 --reload
   ```

5. **Access the portal**
   ```
   http://localhost:8080
   ```

### Docker Deployment

1. **Build the image**
   ```bash
   docker build -t document-portal .
   ```

2. **Run the container**
   ```bash
   docker run -p 8080:8080 --env-file .env document-portal
   ```

## 📁 Project Structure

```
document-portal/
├── src/
│   ├── __init__.py
│   ├── analyser.py          # Document analysis module
│   ├── doccompare.py        # Document comparison module
│   ├── singledocchat.py     # Single document chat
│   ├── multidocchat.py      # Multi-document chat
│   ├── logger.py            # Structured logging
│   └── exception/           # Custom exceptions
├── static/
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   └── assets/              # Static assets
├── templates/
│   └── index.html           # Main UI template
├── config/
│   └── model_config.yaml    # LLM model configuration
├── main.py                  # FastAPI application
├── Dockerfile              # Container configuration
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
└── README.md              # This file
```

## 🔧 Configuration

### Environment Variables

```bash
# Required API Keys
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key

# Optional Configuration
DEFAULT_MODEL=groq  # or google
LOG_LEVEL=INFO
MAX_FILE_SIZE=10485760  # 10MB
SESSION_TIMEOUT=3600    # 1 hour
```

### Model Configuration

Edit `config/model_config.yaml` to customize LLM settings:

```yaml
models:
  groq:
    model_name: "mixtral-8x7b-32768"
    temperature: 0.1
    max_tokens: 4096
  
  google:
    model_name: "gemini-1.5-flash"
    temperature: 0.1
    max_output_tokens: 8192
```

## 🎯 Usage Examples

### Document Analysis
```python
from src.analyser import DocumentAnalyser

analyser = DocumentAnalyser()
result = analyser.analyze_document("path/to/document.pdf")
print(result.summary)
```

### Document Comparison
```python
from src.doccompare import DocumentComparer

comparer = DocumentComparer()
result = comparer.compare_documents(
    "reference.pdf", 
    "updated.pdf"
)
print(result.changes)
```

### Chat with Documents
```python
from src.singledocchat import SingleDocChat

chat = SingleDocChat()
chat.load_document("document.pdf")
response = chat.query("What are the key findings?")
print(response.answer)
```

## 🔌 API Endpoints

### Core Endpoints
- `GET /` - Main application interface
- `GET /health` - Health check endpoint
- `POST /upload` - Document upload
- `POST /analyze` - Document analysis
- `POST /compare` - Document comparison
- `POST /chat` - Chat with documents

### API Documentation
- **Swagger UI**: `http://localhost:8080/docs`
- **ReDoc**: `http://localhost:8080/redoc`

## 🚀 Deployment

### AWS ECS Fargate

1. **Build and push to ECR**
   ```bash
   aws ecr get-login-password | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com
   docker build -t document-portal .
   docker tag document-portal:latest <account>.dkr.ecr.<region>.amazonaws.com/document-portal:latest
   docker push <account>.dkr.ecr.<region>.amazonaws.com/document-portal:latest
   ```

2. **Deploy with ECS**
   - Configure ECS cluster
   - Set up task definition with 8GB memory, 1024 CPU
   - Configure load balancer
   - Set environment variables in Secrets Manager

### Local Docker Compose

```yaml
version: '3.8'
services:
  document-portal:
    build: .
    ports:
      - "8080:8080"
    environment:
      - GROQ_API_KEY=${GROQ_API_KEY}
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
    volumes:
      - ./uploads:/app/uploads
```

## 🧪 Testing

```bash
# Run unit tests
python -m pytest tests/ -v

# Run with coverage
python -m pytest tests/ --cov=src --cov-report=html

# Load testing
pip install locust
locust -f tests/load_test.py
```

## 📊 Performance

- **Document Processing**: ~2-5 seconds per document
- **Vector Indexing**: ~1-2 seconds per 1000 chunks  
- **Chat Response**: ~1-3 seconds per query
- **Memory Usage**: ~500MB base + 100MB per indexed document
- **Concurrent Users**: Supports 100+ concurrent sessions


## 🐛 Troubleshooting

### Common Issues

**"Module not found" errors**
```bash
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

**Out of memory during processing**
- Reduce chunk size in configuration
- Process documents individually
- Increase Docker memory allocation

**Slow response times**
- Check API rate limits
- Verify network connectivity
- Monitor CloudWatch logs

### Debug Mode

```bash
export LOG_LEVEL=DEBUG
uvicorn main:app --reload --log-level debug
```

## 📈 Monitoring

### Health Checks
- `/health` - Application status
- `/metrics` - Performance metrics (if enabled)

### Logging
- Structured JSON logs
- CloudWatch integration
- Request/response tracking
- Error stack traces

## 🛡️ Security

- **API Key Management**: AWS Secrets Manager integration
- **Input Validation**: Comprehensive file type and size checks
- **Rate Limiting**: Built-in request throttling
- **Session Isolation**: User-specific document indexing
- **Error Handling**: No sensitive data in error responses

## 📚 Tech Stack

- **Backend**: FastAPI, Python 3.10, Uvicorn
- **AI/ML**: LangChain, FAISS, Google Embeddings
- **LLMs**: Groq (Mixtral), Google Gemini
- **Document Processing**: PyMuPDF, python-docx
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Infrastructure**: AWS ECS Fargate, ECR, Secrets Manager
- **DevOps**: Docker, GitHub Actions, CloudWatch
