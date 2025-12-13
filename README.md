# 📢 College Notice Management System

A role-based **Notice Management System** built with **Django** that allows teachers to create and manage notices, while students can view and save important notices. This project is designed as a clean, scalable academic project suitable for college submissions, demos, and portfolios.

---

## 🚀 Features

### 👨‍🏫 Teacher Features

* Create notices with:

  * Title & message
  * Attachments (Images, GIFs, Videos, PDFs, files)
  * Category (Exam, Event, General, etc.)
  * Priority (Low / Medium / High)
  * Expiry date
  * Pin / Unpin notice
* Edit & delete **only their own notices**
* View list of notices created by them
* View public notices (read-only)

### 👨‍🎓 Student Features

* View all public notices
* Save / unsave notices (favorites)
* View saved notices separately
* Media preview support (image, gif, video, pdf)

### 🔐 Authentication & Authorization

* Login / Logout
* Role-based access (Teacher / Student)
* Teachers cannot edit other teachers' notices
* Students cannot modify notices

---

## 🛠️ Tech Stack

* **Backend**: Django 5.x
* **Frontend**: HTML, Bootstrap 5
* **Database**: SQLite (default, easily replaceable)
* **Authentication**: Django Auth + Custom Profile model

---

## 📂 Project Structure

```
college_mgmt/
│
├── core/                 # Authentication, Profile, Dashboards
│   ├── models.py         # Profile model (role, saved notices)
│   ├── views.py          # Login, teacher & student dashboards
│   └── decorators.py     # Role-based access control
│
├── notices/              # Notice management app
│   ├── models.py         # Notice model
│   ├── views.py          # CRUD, save, public & saved notices
│   ├── forms.py          # NoticeForm
│   └── urls.py
│
├── templates/            # HTML templates
│   ├── core/
│   └── notices/
│
├── media/                # Uploaded files
├── db.sqlite3
└── manage.py
```

---

## 🧩 Database Models (Simplified)

### Profile Model

* Linked to Django User
* Role: `teacher` / `student`
* Saved notices (ManyToMany)

### Notice Model

* Title, message
* Attachment (FileField)
* Category, priority
* Expiry date
* Pinned flag
* Created by (Teacher)
* Created timestamp

---

## ⚙️ Project Setup & Configuration

### 1️⃣ Clone the Repository

```bash
git clone <repo-url>
cd college_mgmt
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv env
source env/bin/activate      # Linux/Mac
env\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install django
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 👥 User Roles Setup

1. Create users via admin panel
2. Each user gets a `Profile`
3. Set role as:

   * `teacher` → Can create & manage notices
   * `student` → Can view & save notices

---

## 🖼️ Media Handling

Supported formats:

* Images: JPG, PNG, GIF (preview supported)
* Videos: MP4, WEBM (playable)
* Documents: PDF (view/download)

Media files are stored in `/media/` and served via Django media settings.

---

## 🔑 Important URLs

| URL                   | Description               |
| --------------------- | ------------------------- |
| `/login/`             | Login page                |
| `/teacher/dashboard/` | Teacher dashboard         |
| `/student/dashboard/` | Student dashboard         |
| `/notices/`           | Teacher notice management |
| `/notices/public/`    | Public notice board       |
| `/notices/saved/`     | Student saved notices     |

---

## 🌟 Why This Is a Good Project

* Real-world problem (college notice system)
* Proper role-based access control
* Clean separation of apps
* Media handling & preview
* Scalable feature design
* Suitable for:

  * College project
  * Django portfolio
  * Resume showcase

---

## 🔮 Future Enhancements

* Email / WhatsApp notification
* Search & filters
* Notice analytics (views count)
* Comment & reply system
* Admin approval workflow

---

## 👤 Author

**Ajay Joshi**
Django | MERN | Competitive Programming | GATE CSE Qualified

---

## 📜 License

This project is for educational purposes and free to use.

---

✨ *Feel free to fork, improve, and showcase this project!*
