# 🍔 Food Express

**Food Express** is a fast, reliable, and interactive food ordering and delivery management system designed to connect customers, riders, and restaurant administrators.

Built with **Django**, the platform provides dedicated dashboards for different roles, ensuring a streamlined process from order placement to final delivery.


---

## 🚀 Key Features

- **Role-Based Dashboards** – Separate interfaces for Customers, Riders, and Administrators.
- **Smart Order Tracking** – Real-time status updates (Pending &rarr; Preparing &rarr; On The Way &rarr; Delivered/Rejected).
- **Two-Way Confirmation** – Customers can confirm if they actually received the order.
- **Menu Management** – Admins can easily add, update, and manage food categories and items.
- **Favorite Meals** – Customers can add food items to their favorites list for quick ordering.
- **Rider Allocation** – Seamlessly assign orders to delivery riders for fulfillment.
- **Responsive Design** – Optimized for desktops, tablets, and mobile devices.

---

### 🔐 Role-Based Access
- **Customers** &rarr; Browse food menus, add favorites, place orders, track status, and confirm delivery.
- **Riders** &rarr; View assigned deliveries, update delivery status ("On The Way", "Delivered").
- **Admins** &rarr; Oversee all operations, manage menu items, process orders, and handle rejections.

### 🔎 Smart Filtering & Search
- Filter orders by:
  - **Status** (Pending, Preparing, On The Way, etc.)
  - **Cities** (Bahawalpur, Multan, Lahore, Karachi, Islamabad)

---

## 🛠 Tech Stack

| Area | Technology |
| :--- | :--- |
| **Backend Framework** | Django 5.x (Python) |
| **Frontend** | HTML5, CSS3, Bootstrap 5.3 |
| **Database** | SQLite (Default) |
| **Image Processing** | Pillow |
| **Templating** | Django Template Engine (DTL) |
| **Authentication** | Django Auth System |

---

## 📸 App Screenshots

<p align="center">
  <img src="myproject/myapp/static/images/1.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/2.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/3.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/4.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/5.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/6.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/7.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/8.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/9.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/10.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/11.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/12.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/13.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/14.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/15.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/16.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/17.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/18.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/19.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
  <img src="myproject/myapp/static/images/20.png" width="90%" style="margin: 10px; border-radius: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
</p>

---

## 🔧 Getting Started

### Prerequisites
- Python 3.8+
- Git

**1. Clone the repository:**
```bash
git clone https://github.com/NoorMustafa4556/Food-Express-Django.git
```
```
cd Food-Express
```

**2. Create and activate a virtual environment:**
```bash
python -m venv env
```
## Windows
```
.\env\Scripts\activate
```
## Mac/Linux
```
source env/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Apply migrations:**
```bash
cd myproject
```
```
python manage.py makemigrations
```
```
python manage.py migrate

```

**5. Create a Superuser:**
```bash
python manage.py createsuperuser
```

**6. Run the server:**
```bash
python manage.py runserver
```

---

# 👋🏻 Hi, I'm Noor Mustafa

A passionate and results-driven **Software Developer** from **Bahawalpur, Pakistan**, specializing in building elegant, scalable, and high-performance applications using **Django** and **Flutter**.

With a strong understanding of **Full-Stack Development**, **UI/UX principles**, and **API integration**, I aim to deliver solutions that are not only functional but also user-centric and visually compelling.

---

## 🚀 What I Do
- 💻 **Web Development** – Building robust web apps with Django & React.
- 📱 **Mobile App Development** – Creating cross-platform apps with Flutter.
- 🔗 **API Integration** – Connecting frontends to powerful RESTful APIs.
- 🔐 **Secure Systems** – Implementing secure authentication and role-based access.

---

## 🌟 Projects I'm Proud Of
- 🍔 **[Food Express](https://github.com/NoorMustafa4556/Food-Express)** – A dynamic food ordering and delivery system linking customers, riders, and restaurant admins.
- 🩸 **[Blood Link](https://github.com/NoorMustafa4556/Blood-Link-App-Flutter)** – A modern blood donation app connecting donors and recipients.
- 🎓 **[UCMS](https://github.com/NoorMustafa4556/UCMS-University-Complaint-Management-System)** – A comprehensive university complaint management system.
- 🌤 **[Live Weather Check](https://github.com/NoorMustafa4556/Live-Weather-Check-App)** – Real-time weather forecast functionality.
- 🤖 **[AI Chatbot](https://github.com/NoorMustafa4556/Ai-ChatBot)** – Conversational AI powered by Google Gemini.

> 🎯 Check out all my repositories on [github.com/NoorMustafa4556](https://github.com/NoorMustafa4556?tab=repositories)

---

## 🧰 Tech Toolbox

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white"/>
  <img src="https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

## 📫 Let's Connect!

<p align="left">
  <a href="https://x.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="X / Twitter" height="30" width="40" />
  </a>
  <a href="https://www.linkedin.com/in/noormustafa4556/" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" />
  </a>
  <a href="https://www.facebook.com/NoorMustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="Facebook" height="30" width="40" />
  </a>
  <a href="https://instagram.com/noormustafa4556" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" />
  </a>
  <a href="https://wa.me/923087655076" target="blank">
    <img src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" />
  </a>
  <a href="https://www.tiktok.com/@noormustafa4556" target="blank">
    <img src="https://cdn-icons-png.flaticon.com/512/3046/3046122.png" alt="TikTok" height="30" width="30" />
  </a>
</p>

- 📍 **Location:** Bahawalpur, Punjab, Pakistan

---

> “Creating systems that solve real-world problems, one line of code at a time.”

---
