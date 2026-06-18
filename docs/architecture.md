# PulseMesh Architecture

## Overview

PulseMesh is a realtime backend platform designed for:

- event streaming
- realtime notifications
- websocket communication
- async event processing
- distributed backend messaging

---

## Core Components

### Authentication Layer
JWT-based authentication system.

### WebSocket Gateway
Realtime bidirectional communication.

### Event Bus
Internal event dispatching architecture.

### Notification Engine
Processes and routes notifications.

### Worker Layer
Celery workers process async events.

### Redis Layer
Pub/sub and websocket channel layer.

### PostgreSQL
Persistent event and notification storage.

---

## High-Level Flow

Client
↓
WebSocket/API Gateway
↓
Event Bus
↓
Redis Channel Layer
↓
Workers / Notification Engine
↓
Realtime Delivery