# 📱 SMS Sending Application with Django and Twilio

This is a simple SMS sending web application built with **Django** and powered by the **Twilio API**. The app allows users to send SMS messages to specified phone numbers via a web interface.

---

## 🚀 Features

- Send SMS messages using Twilio.
- Simple and user-friendly interface.
- Error handling and feedback for successful or failed SMS attempts.
- Secure handling of sensitive information using `.env` files.

---

## 🛠️ Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS
- **API**: Twilio
- **Environment Management**: `django-environ`

---

## 📂 Project Structure

```
sms_project/
│-- sms_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
│-- sms_app/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── send_sms.html
│       └── index.html
│
│-- manage.py
│-- .env
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Caeilanlightwood77/sms_project.git
cd sms_project
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project's root directory and add your Twilio credentials:

```env
SECRET_KEY=your-secret-key
DEBUG=True

TWILIO_ACCOUNT_SID=your-twilio-account-sid
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=your-twilio-phone-number
```

### 5. Apply Migrations

```bash
python manage.py migrate
```

### 6. Run the Server

```bash
python manage.py runserver
```

### 7. Access the Application

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## 🔧 How to Use the App

1. **Home Page** (`/`):  
   - Welcome page with a link to the SMS form.

2. **Send SMS Page** (`/api/send_sms/`):  
   - Enter the recipient's phone number (in international format, e.g., `+1234567890`).
   - Enter the message.
   - Click the **Send** button.

3. **Feedback**:  
   - A **green success message** if the SMS is sent successfully.
   - A **red error message** if the SMS fails to send.

---

## 🌐 Twilio Configuration

1. **Create a Twilio Account**:  
   Sign up at [Twilio](https://www.twilio.com/) if you don't have an account.

2. **Get Your Credentials**:  
   - **Account SID**
   - **Auth Token**
   - **Twilio Phone Number**

3. **Add Credentials to `.env`**:

   ```env
   TWILIO_ACCOUNT_SID=your-twilio-account-sid
   TWILIO_AUTH_TOKEN=your-twilio-auth-token
   TWILIO_PHONE_NUMBER=your-twilio-phone-number
   ```

---

## 📦 `requirements.txt`

```plaintext
Django==5.1.3
twilio==8.8.0
django-environ==0.11.2
```

---

## ⚠️ Important Notes

- Ensure your Twilio account has enough balance and that the recipient's phone number is verified if you're using a trial account.
- Keep the `.env` file out of version control by adding it to `.gitignore`:

  ```gitignore
  .env
  ```

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request.

---

### 👥 Project Contributors

- **Name**: **Dextarfinity**
- **Github**: [Dextarfinity](https://github.com/Dextarfinity)

- **Name**: **DjYoon04**
- **Github**: [DjYoon04](https://github.com/DjYoon04)

- **Name**: **kyleneangela**
- **Github**: [kyleneangela](https://github.com/kyleneangela)

- **Name**: Caeilanlightwood
- **Email**: caeilanlightwood77@gmail.com
- **GitHub**: [Caeilanlightwood77](https://github.com/Caeilanlightwood77)
