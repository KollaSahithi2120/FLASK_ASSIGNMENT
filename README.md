 Overview
This project consists of two major applications:
1. Financial Portfolio and Sentiment Analysis Dashboard: A Flask application that gathers financial data and sentiment analysis from multiple sources and visualizes portfolio trends. It includes role-based dashboards for different users like analysts, investors, and administrators.
2. Educational Performance Analysis Tool: An application that tracks student performance from various sources, processes the data, and displays insights on student progress and learning trends through dashboards for teachers, students, and administrators.

 Key Features:
 Financial Portfolio and Sentiment Analysis Dashboard:
- Data Sources: 
  - Financial data is pulled from [Finviz](https://finviz.com/quote.ashx?t=) for various stock tickers. This data is scraped to gather real-time stock price, financial metrics, and other essential data for visualizing portfolio trends.
  - Sentiment analysis is performed on data from social media platforms like Twitter, Google News, and other financial news sources.
- Role-Based Dashboards:
  - Analysts: Access to detailed sentiment and financial analysis.
  - Investors: Portfolio insights, trends, and investment recommendations.
  - Administrators: Full control over user access and data management.
- ETL: Extract, Transform, and Load (ETL) process to gather and clean data from multiple sources.
- Database Support: Switches between SQLite and PostgreSQL for database operations.
- Chart Visualizations: Includes 5+ charts for visualizing financial and sentiment data.
  
 Educational Performance Analysis Tool:
- Data Sources: 
  - Student performance data is pulled from a CSV file that contains various metrics such as student grades, subjects, and other related performance indicators.
  - The CSV data undergoes an ETL process to clean and organize the information before storing it in the database.
- Role-Based Dashboards:
  - Teachers: Access to student performance and trends.
  - Students: Track personal progress and achievements.
  - Administrators: Full control to monitor and manage student data.
- ETL: Process the data and perform necessary transformations to store it in the database.
- Database Support: Switches between PostgreSQL and Oracle for database operations.
- Chart Visualizations: Includes 5+ charts to visualize student performance trends and insights.

 Project Structure

 1. Financial Portfolio and Sentiment Analysis Dashboard:
- REGISTER: Contains code related to user registration and login functionality.
- FINANCE: Contains code related to financial data collection (from Finviz), processing, and sentiment analysis.
- SENTIMENT: Contains code for processing sentiment data from Twitter and Google News.
- DATABASE: Contains ORM (Object-Relational Mapping) code for handling database operations (SQLite and PostgreSQL).
- VISUALIZATIONS: Contains code for generating charts and graphs to display financial trends and sentiment analysis.

 2. Educational Performance Analysis Tool:
- REGISTER: Contains code related to user registration and login functionality.
- STUDENT: Contains student-related functionalities, such as pulling student performance data from a CSV file.
- EDUCATION: Contains code for processing educational data and displaying student progress.
- DATABASE: Contains ORM code for managing the database, supporting both PostgreSQL and Oracle databases.
- VISUALIZATIONS: Contains code for generating charts to display educational performance trends.

 Port Configuration
- Port 5000: Home screen for user authentication (login/register) and role selection.
- Port 5001: Backend application for data visualizations, insights, and predictions. This port is only accessible after successful login and role verification.

 Google Drive Link for Files
Since there were issues with files not opening in the Git repository and Git LFS, all files have been compressed and uploaded to a public Google Drive link. Please use the following link to access the files:
https://drive.google.com/file/d/1UTWLvhvbsasKgyEmkFzjeYqtjHU7x22g/view?usp=sharing .

 Visual Output
The output.doc file contains screenshots of the application’s output screens. Please refer to this document for a visual representation of the project’s user interface and data interactions.

 Setting Up the Project

 1. Clone the Repository
```bash
git clone https://github.com/KollaSahithi2120/FLASK_ASSIGNMENT.git
```

 2. Install Dependencies
Navigate to the project directory and install the required Python packages:
```bash
cd FLASK_ASSIGNMENT
pip install -r requirements.txt
```

 3. Running the Applications

 REGISTER (Port 5000)
To start the home screen where users can register, log in, and choose their role:
```bash
python app.py
```
This will run the home screen on localhost:5000.

 Financial Portfolio and Sentiment Analysis Dashboard (Port 5001) (code available in FINANCE FOLDER)
To start the backend application for financial data and sentiment analysis:
```bash
python app.py
```
This will run the backend on localhost:5001, but it will only be accessible after successful login on port 5000 as admin.

 Educational Performance Analysis Tool (Port 5001) (code available in STUDENT FOLDER)
To start the backend application for educational performance analysis:
```bash
python app.py
```
This will run the backend on localhost:5001, but it will only be accessible after successful login on port 5000 as admin.

 How It Works

- When the user accesses the home screen on port 5000, they can either register or log in by providing their credentials (email and password).
- Once logged in, the user is asked to select a role:
  - Admin: Full control to manage entries.
  - Editor: Can only edit existing entries.
  - Viewer: Can only view entries without any edit/delete privileges.
- Upon selecting the role and confirming the login, the user gains access to the backend application running on port 5001 for either the Financial Portfolio and Sentiment Analysis or Educational Performance Analysis functionality.
- The backend provides functionalities like data visualization and insights that users can interact with based on their role.

 Security and Authentication
Access to the application on port 5001 is restricted and requires authentication through a valid user login. This ensures that only authenticated users with the correct roles can interact with the backend.

 Troubleshooting

1. If you encounter issues with Git LFS or file access:
   - The files have been compressed and uploaded to Google Drive. Download them and place them in the project directory as needed.

2. Port Conflicts:
   - Ensure that ports 5000 and 5001 are not being used by other applications. If necessary, change the ports in the configuration files.

---

 Notes:
- If there are any issues with starting the applications or missing files, refer to the Google Drive link to access the full set of project files.
- The project is modular and can be extended with additional features based on the roles (Admin/Editor/Viewer) and their respective permissions.



