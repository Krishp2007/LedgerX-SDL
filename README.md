<div align="center">

# 📒 LedgerX - Smart Digital Ledger

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?logo=python&logoColor=white)](#)
[![Django](https://img.shields.io/badge/Django-5.0-092E20.svg?logo=django&logoColor=white)](#)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg?logo=bootstrap&logoColor=white)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](#)

**A modern, responsive web application replacing traditional paper ledgers (Udhar books) with a secure, digital point-of-sale and credit management solution.**

</div>

---

## 🚀 Key Features

### 👥 Customer & Credit Management
* **Digital Udhar Book:** Dedicated ledger page for each customer showing full transaction history.
* **Smart Balance Tracking:** Instantly calculates **Total Payable** (Credit) or **Advance Balance**.
* **Soft Deletes (Archives):** Hide inactive customers without losing their historical transaction data.
* **Instant Search:** Filter customers quickly by name or mobile number.

### 📦 Inventory & Product Catalog
* **Cloud Media:** Upload and manage product images seamlessly (powered by Cloudinary).
* **Real-time Stock Tracking:** Automatically deducts stock upon every successful sale.
* **Low Stock Alerts:** Visual UI badges for items dropping below custom thresholds (<10) or Out of Stock.

### 🧾 Point of Sale (POS) Billing
* **Frictionless Billing:** Add items, adjust quantities, and generate bills in seconds.
* **Dual Payment Modes:** Support for both **Cash** and **Credit (Udhar)** checkouts.
* **AJAX Customer Creation:** Add new walk-in customers directly from the billing screen without reloading.
* **Stock Protection:** Built-in safeguards prevent selling more items than currently available.

### 💰 Payments & UPI Integration
* **WhatsApp Reminders:** One-click automated payment reminders sent via WhatsApp deep-linking.
* **Smart UPI & QR Codes:** Generates dynamic payment links and QR codes that open GPay/PhonePe directly with the *exact amount pre-filled*.
* **Multi-Shop UPI Support:** Shopkeepers can configure their personal UPI IDs to receive funds directly into their own bank accounts.

### 📊 Reports & Analytics
* **Interactive Dashboard:** Real-time metrics for Today's Sales, Cash Inflow, Low Stock, and Active Customers.
* **Historical Reports:** Filter and export transaction histories by custom date ranges.
* **Best Sellers:** Identify top-performing products ranked by quantity sold.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.10+, Django 5.0
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla), Bootstrap 5
* **Database:** SQLite (Local) / PostgreSQL (Production ready via `dj_database_url`)
* **Media Storage:** Cloudinary (for scalable product/profile image hosting)
* **Emails & OTPs:** Brevo API (Transactional emails for Password Resets & Contact Forms)
* **Payments:** Python `qrcode` + UPI Deep Linking Protocols

---

## ⚙️ Installation & Setup

Follow these steps to run LedgerX on your local machine.

### 1. Clone the Repository
```bash
git clone https://github.com/krishp2007/ledgerx-sdl.git

cd ledgerx-sdl
```


### 2. Create and Activate Virtual Environment
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
* Create a .env file in the root directory (same folder as manage.py) and add your API keys
🔑 Environment Variables
To fully utilize all features (like image uploads and OTP emails), configure the following in your .env file:
```bash
# --- Core Django Settings ---
SECRET_KEY=your_secure_django_secret_key
DEBUG=True

# --- Database (Optional: defaults to SQLite if empty) ---
DATABASE_URL=postgres://user:password@localhost:5432/ledgerx

# --- Cloudinary (For Product & Profile Images) ---
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# --- Brevo (For OTP & Support Emails) ---
BREVO_API_KEY=your_brevo_api_key_here
DEFAULT_FROM_EMAIL=your_email_here
```

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server
```bash
python manage.py runserver
```

### 📂 Project Architecture
```bash
LedgerX/
├── accounts/       # User authentication, Shop profiles, Password recovery OTPs
├── customers/      # Customer DB, Udhar limits, ledger views
├── products/       # Inventory catalog, Cloudinary media, stock thresholds
├── sales/          # POS checkout logic, Transaction & Item records
├── qr/             # Dynamic UPI link & QR code rendering engine
├── reports/        # Analytics logic, Dashboard metrics
├── templates/      # Global UI layouts, Email HTML templates
├── static/         # Custom CSS, JS, Branding assets
└── manage.py       # Django administrative script
```


### 🤝 Contributing
Contributions, issues, and feature requests are welcome!

1. Fork the Project

2. Create your Feature Branch (git checkout -b feature/AmazingFeature)

3. Commit your Changes (git commit -m 'Add some AmazingFeature')

4. Push to the Branch (git push origin feature/AmazingFeature)

5. Open a Pull Request

### 📄 License
 Distributed under the MIT License. See LICENSE for more information.