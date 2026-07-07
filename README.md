# EcoStock

A simple REST API to manage food stock for a startup that redistributes food surpluses before they expire.

## What is this project?

Eco-Stock collects surplus food from businesses, stores it in **warehouses**, then redistributes it before the expiration date.

This API allows you to:
- manage warehouses (create, update, delete, retrieve)
- manage food products
- transfer a product from one warehouse to another
- perform an audit (count how many products are in a warehouse)
- secure access with a login system (JWT)

## What is it built with?

- **Python**
- **Django**: the web framework
- **Django REST Framework (DRF)**: to easily create the API
- **Simple JWT**: to handle user authentication
- **DRF-yasg**: to generate Swagger documentation

## The two main "objects"

### A warehouse 

It's a storage location. It has:
- a **name**
- a **location** (address)
- a **capacity** (maximum number of products it can hold)

### A product 

It's a food item stored in a warehouse. It has:
- a **name**
- a **quantity**
- an **expiration date**
- a **status**: `available`, `reserved`, or `expired`
- a **warehouse** it belongs to

A warehouse can contain multiple products, but a product belongs to only one warehouse at a time.

## How to install the project locally

### Step 1: Download the project

```bash
git clone https://github.com/<your-username>/ecostock-api.git
cd ecostock-api
```

### Step 2: Create a virtual environment

It's an isolated space to install Python libraries without mixing them with the rest of your computer.

```bash
python -m venv venv
```

Then activate it:

```bash
# On Mac or Linux
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

### Step 3: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 4: Create the database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create an admin account

```bash
python manage.py createsuperuser
```

It will ask you for a username, email, and password.

### Step 6: Start the server

```bash
python manage.py runserver
```

The project is now running on: **http://127.0.0.1:8000/**

## Important URLs

| URL | Purpose |
|---|---|
| `/admin/` | Visual interface to easily add/edit warehouses and products |
| `/api/` | The API itself, with all routes |
| `/api/token/` | To log in and receive a token |

## How authentication works (JWT)

 All actions require you to be **logged in**.

### 1. Log in to get a token

```bash
curl -X POST http://127.0.0.1:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "aram1", "password": "admin123"}'
```

You'll receive a response like this:

```json
{
  "access": "eyJhbGciOiJIUzI1NiIs...",
  "refresh": "eyJhbGciOiJIUzI1NiIs..."
}
```

The `access` token is your "access badge". You must send it with every protected request.

### 2. Use this token

In every request that modifies data, add this header:

```
Authorization: Bearer <your_access_token>
```

## 📡 All available routes

### For warehouses

| Method | URL | Action | Authentication required? |
|---|---|---|---|
| GET | `/api/warehouses/` | List all warehouses | No |
| POST | `/api/warehouses/` | Create a warehouse | Yes |
| GET | `/api/warehouses/1/` | Retrieve a specific warehouse | No |
| PUT | `/api/warehouses/1/` | Update a warehouse | Yes |
| DELETE | `/api/warehouses/1/` | Delete a warehouse | Yes |
| GET | `/api/warehouses/1/audit/` | Count products in this warehouse | No |

### For products

| Method | URL | Action | Authentication required? |
|---|---|---|---|
| GET | `/api/products/` | List all products | No |
| POST | `/api/products/` | Create a product | Yes |
| GET | `/api/products/1/` | Retrieve a specific product | No |
| PUT | `/api/products/1/` | Update a product | Yes |
| DELETE | `/api/products/1/` | Delete a product | Yes |
| POST | `/api/products/1/move/` | Move a product to another warehouse | Yes |

## 💡 Concrete examples

### Move a product to another warehouse

```bash
curl -X POST http://127.0.0.1:8000/api/products/1/move/ \
  -H "Authorization: Bearer <your_access_token>" \
  -H "Content-Type: application/json" \
  -d '{"warehouse_id": 2}'
```
 If the product is expired, the transfer is automatically denied.

### View a warehouse audit

```bash
curl http://127.0.0.1:8000/api/products/1/audit/
```




## File organization

```
ecostock-api/
├── ecostock_project/
│   ├── settings.py     → general project configuration
│   └── urls.py         → list of main URLs
├── stock/
│   ├── models.py       → Warehouse and Product models
│   ├── serializers.py  → transforms data into JSON
│   ├── views.py        → all logic (CRUD + move/audit actions)
│   ├── admin.py        → admin interface configuration
│   └── urls.py         → stock app URLs
├── requirements.txt    → list of libraries to install
└── manage.py           → Django command-line utility
```

## ✅ Key takeaways

- We use `ModelViewSet` to get full CRUD (create, read, update, delete) functionality with minimal code.
- We use `@action` to add custom actions like `move` and `audit`.
- **Read** routes are open to everyone.
- **Write** routes require authentication with a JWT token.

## 🧪 Possible next step

Add automated tests to verify that:
- an expired product cannot be transferred

## 👤 Author
Arame DIENG

Project created as part of learning backend development with Django REST Framework.