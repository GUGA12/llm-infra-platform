FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
EXPOSE 8080
# 问题: 为什么容器里不用 --reload? workers 数怎么定?
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
