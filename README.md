# 🤖 RoboTech E-commerce Store  
### An Interactive Marketplace for Robotics and Electronics  

**RoboTech** is a Django-based e-commerce platform specialized in selling electronic components, sensors, and robotics kits for educational and development purposes. The system focuses on structured product management, secure authentication, and automated invoice generation.

---

## 🚀 Core Features

- **Product Management:**  
  Structured product catalog with categorized robotics components and detailed specifications.

- **User Authentication & Profiles:**  
  Secure authentication system with editable user profiles (email and phone number updates supported).

- **Invoice Generation:**  
  Automated invoice creation after successful checkout.

- **QR Code Integration:**  
  Each generated invoice includes a unique QR code for verification and tracking.

- **Responsive Interface:**  
  Mobile-first responsive design implemented using Bootstrap 5.

---

## 🛠 Technology Stack

- **Backend:** Python & Django  
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5  
- **Database:** SQLite (Development Environment)  
- **Deployment:** Gunicorn & WhiteNoise  

> Note: For production environments, PostgreSQL is recommended instead of SQLite.

---

## 🔧 Installation & Setup

### 1️. Clone the repository

```bash
git clone https://github.com/bariqa1/robotech-ecommerce.git
cd robotech-ecommerce
```

---

### 2️. Create and activate a virtual environment

```bash
python -m venv env

# Windows
env\Scripts\activate

# macOS / Linux
source env/bin/activate
```

---

### 3️. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️. Apply database migrations

```bash
python manage.py migrate
```

---

### 5️. Run the development server

```bash
python manage.py runserver
```

Then open your browser and navigate to:

```
http://127.0.0.1:8000/
```

