# 第15章：监控与日志

## 📚 学习目标

通过本章学习，你将掌握：
- Web应用监控体系设计
- FastAPI日志配置与采集
- 前端异常监控与上报
- Prometheus+Grafana监控实践
- 日志集中与可视化

## 📈 监控体系设计

### 15.1 监控对象
- 服务可用性（存活、响应时间）
- 性能指标（CPU、内存、QPS、延迟）
- 业务指标（注册量、活跃用户、订单量）
- 异常与报警

### 15.2 监控方案
- 基础监控：云厂商监控、Zabbix、Prometheus
- 日志监控：ELK/EFK、云日志服务
- 前端监控：Sentry、Fundebug、前端自建上报

## 📝 FastAPI日志配置

### 15.3 日志输出

```python
import logging
from fastapi import FastAPI

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(name)s %(message)s',
    handlers=[logging.StreamHandler()]
)

app = FastAPI()

@app.get("/log-demo")
def log_demo():
    logging.info("访问了log-demo接口")
    return {"msg": "日志已记录"}
```

### 15.4 日志采集与集中
- 日志文件挂载到宿主机
- Filebeat/Fluentd收集日志到ELK/EFK
- 云日志服务一键采集

## 🖥️ 前端异常监控

### 15.5 前端异常捕获

```javascript
window.onerror = function(message, source, lineno, colno, error) {
  // 发送到后端日志接口
  fetch('/api/v1/logs', {
    method: 'POST',
    body: JSON.stringify({ message, source, lineno, colno, error }),
    headers: { 'Content-Type': 'application/json' }
  })
}
```

### 15.6 Sentry集成

```javascript
import * as Sentry from '@sentry/vue'
import { BrowserTracing } from '@sentry/tracing'

Sentry.init({
  app,
  dsn: 'https://xxx@sentry.io/xxx',
  integrations: [new BrowserTracing()],
  tracesSampleRate: 1.0,
})
```

## 📊 Prometheus+Grafana监控

### 15.7 FastAPI暴露指标

```python
from prometheus_client import start_http_server, Summary
import time

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request():
    time.sleep(2)

if __name__ == '__main__':
    start_http_server(8001)
    while True:
        process_request()
```

### 15.8 Grafana可视化
- 添加Prometheus数据源
- 配置仪表盘展示QPS、延迟、错误率等

## 🗃️ 日志可视化

### 15.9 ELK/EFK日志平台
- Elasticsearch存储日志
- Logstash/Fluentd收集日志
- Kibana/Fluentd前端可视化

## 💻 实践项目

### 项目：全栈应用监控与日志
- FastAPI日志采集与报警
- 前端异常自动上报
- Prometheus+Grafana监控API
- ELK/EFK日志可视化

## 📝 本章小结

### 重点概念
- ✅ 监控体系与指标
- ✅ FastAPI与前端日志采集
- ✅ Prometheus+Grafana监控
- ✅ 日志集中与可视化

### 关键技能
- ✅ 配置日志与异常采集
- ✅ 集成Prometheus与Grafana
- ✅ 日志平台搭建与查询

## 🔗 扩展阅读
- [FastAPI日志与监控](https://fastapi.tiangolo.com/zh/advanced/monitoring/)
- [Prometheus官方文档](https://prometheus.io/docs/)
- [Grafana官方文档](https://grafana.com/docs/)
- [Sentry前端监控](https://docs.sentry.io/platforms/javascript/)
- [ELK Stack介绍](https://www.elastic.co/what-is/elk-stack)

## ❓ 常见问题

**Q: 如何快速定位线上故障？**
A: 结合日志、监控报警、链路追踪多手段定位。

**Q: 日志量大如何处理？**
A: 分级采集、定期归档、冷热分离、日志压缩。 