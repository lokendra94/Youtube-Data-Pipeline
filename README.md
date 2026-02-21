YouTube Analytics Data Pipeline

📌 Project Overview

This project is an automated end-to-end data pipeline that collects YouTube channel statistics using the YouTube Data API, stores daily snapshots in a MySQL database, and visualizes performance trends in Power BI.

The system is scheduled to run automatically, enabling time-series analysis of subscriber growth, views, and engagement metrics.

---

🏗️ Architecture

```
YouTube Data API → Python (ETL) → MySQL → Power BI Dashboard
                           ↓
                 Windows Task Scheduler (Automation)
```

---

🚀 Features

* Automated YouTube API data extraction
* Daily snapshot storage in MySQL
* Time-series tracking of subscribers and views
* Subscriber growth calculation (latest vs previous snapshot)
* Engagement metric (Views per Video)
* Automated scheduling using Windows Task Scheduler
* Power BI dashboard with KPI and trend visualization

---

 🛠️ Technologies Used

* Python
* YouTube Data API v3
* MySQL
* Power BI
* Windows Task Scheduler

---

📂 Project Structure

```
youtube-analytics-project/
│
├── test_api.py               # Main ETL pipeline script
├── requirements.txt          # Python dependencies
├── create_tables.sql         # Database schema
├── youtube_dashboard.pbix    # Power BI dashboard
├── dashboard_screenshot.png  # Dashboard preview
└── README.md
```

---

⚙️ Setup Instructions

 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd youtube-analytics-project
```

---

2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

3️⃣ Configure API Key

Open `test_api.py` and replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual YouTube Data API key.

---

 4️⃣ Create Database

Open MySQL Workbench and run:

```sql
SOURCE create_tables.sql;
```

---

 5️⃣ Run the Pipeline

```bash
python test_api.py
```

This will:

* Fetch channel data
* Insert snapshot into MySQL
* Store timestamp for time-series analysis

---

 Dashboard

The Power BI dashboard includes:

* Current Subscribers (Latest Snapshot)
* Subscriber Growth
* Growth Percentage
* Views per Video
* Subscriber Trend Over Time
* Views Trend Over Time

(Dashboard preview available in `dashboard_screenshot.png`)

---

Automation

The ETL script is scheduled using Windows Task Scheduler to run daily, enabling automated data ingestion without manual execution.

---

 Example Analytical Insight

If views increase while subscribers remain flat, this may indicate:

* Evergreen content driving passive traffic
* Low subscriber conversion rate
* High casual viewer engagement

---

Learning Outcomes

Through this project, I gained hands-on experience with:

* API integration
* Database design and storage
* ETL pipeline development
* KPI calculation using DAX
* Time-series analysis
* Workflow automation

---

 Future Improvements

* Multi-channel tracking
* Rolling 7-day growth analysis
* Deployment to cloud database (AWS RDS)
* Power BI Service scheduled refresh
* Logging and error handling improvements

---

Author

Lokendra Chawla
BSc Bioinformatics Student
Aspiring Data Analyst

