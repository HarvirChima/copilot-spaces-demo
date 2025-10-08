# Customer Management API

A simple Flask-based REST API for managing customer data.

## Setup

```bash
pip install -r requirements.txt
```

## Run the API

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### GET /
Welcome message and API information

### GET /api/customers
Get all customers
- Query parameter: `status` (optional) - filter by status (active/inactive)

### GET /api/customers/<id>
Get a specific customer by ID

### POST /api/customers
Create a new customer
- Body: JSON with `name`, `email`, `phone`, and optional `status`

### PUT /api/customers/<id>
Update an existing customer
- Body: JSON with fields to update

### DELETE /api/customers/<id>
Delete a customer

## Example Usage

```bash
# Get all customers
curl http://localhost:5000/api/customers

# Get customer by ID
curl http://localhost:5000/api/customers/1

# Create a new customer
curl -X POST http://localhost:5000/api/customers \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Brown", "email": "alice@example.com", "phone": "555-0103"}'

# Update a customer
curl -X PUT http://localhost:5000/api/customers/1 \
  -H "Content-Type: application/json" \
  -d '{"status": "inactive"}'

# Delete a customer
curl -X DELETE http://localhost:5000/api/customers/1
```

## Demo Ideas for Copilot Spaces

1. **Add Authentication**: "Add JWT authentication to protect the API endpoints"
2. **Add Statistics Endpoint**: "Create an endpoint that returns customer statistics"
3. **Add Pagination**: "Implement pagination for the customers list"
4. **Add Search**: "Add a search endpoint to find customers by name or email"
5. **Write Tests**: "Create comprehensive unit tests for all endpoints"
