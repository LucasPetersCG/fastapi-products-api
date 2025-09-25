# FastAPI Products API

A RESTful API for product management built with FastAPI and Docker.

## Features

- CRUD operations for products
- Docker containerization
- FastAPI automatic documentation
- Pydantic models for data validation

## Technology Stack

- Python 3.9
- FastAPI
- Docker
- Pydantic

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/fastapi-products-api.git
cd fastapi-products-api
```

2. Start the application
```bash
docker-compose up -d
```

3. Access the API documentation at http://localhost:4000/docs

## API Endpoints

- `GET /api/products` - List all products
- `GET /api/products/{id}` - Get a specific product
- `POST /api/products` - Create a new product
- `PUT /api/products/{id}` - Update a product
- `DELETE /api/products/{id}` - Delete a product

## License

MIT License
