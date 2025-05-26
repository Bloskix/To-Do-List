🚀 To-Do List App
Welcome to the To-Do List application! This is a simple and efficient tool to manage your daily tasks, allowing you to organize your work and track your progress with ease.
🌟 Features
* Task Creation: Create tasks with a name, and optionally, a start date and an end date.
* Simple Subtasks: Add simple subtasks with names to break down your main tasks.
* Status Management: Clearly visualize your pending tasks and your completed tasks.
* Enhanced Security: Secure authentication system using JWT tokens and OAuth integration.
* Date Validation: Built-in validation to ensure logical date ranges for tasks.
🛠️ Technologies Used
This application is built with a modern and robust stack, ensuring performance and scalability.
Frontend
* Next.js: React framework for full-stack web application development.
* React: JavaScript library for building interactive user interfaces.
* TypeScript: JavaScript superset that adds static typing, improving code quality.
* Tailwind CSS: Utility-first CSS framework for rapid and flexible design.
* Shadcn UI: Beautiful and reusable UI components built with Tailwind CSS.
Backend
* Python: Primary programming language for the backend.
* FastAPI: Modern and fast web framework for building APIs with Python.
* PostgreSQL: Robust and open-source relational database for data storage.
* JWT & OAuth: Advanced authentication and authorization mechanisms.
⚙️ Setup and Running
Follow these steps to get the application up and running in your local environment.
Prerequisites
Make sure you have the following installed:
* Node.js (with pnpm)
* Python 3.x
* PostgreSQL
1. Database Setup
First, ensure your PostgreSQL instance is running.
Environment Variables for the Backend:
Create a .env file in the root of your backend directory (where main.py is located) with the following variables:
DB_HOST=your_db_host
DB_PORT=your_db_port
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
Migrations with Alembic:
Once the environment variables are configured, navigate to the backend directory and run the migrations to create the necessary tables in the database:
# Navigate to the backend directory
cd backend/

# Assuming Alembic is already configured, if not, first initialize Alembic
# alembic init migrations

# Generate a migration file (if needed for model changes)
# alembic revision --autogenerate -m "Initial setup"

# Apply migrations to the database
alembic upgrade head
2. Backend Setup
1. Create and activate a virtual environment:
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

2. Install dependencies (create a requirements.txt file with necessary dependencies like fastapi, uvicorn, psycopg2-binary, sqlalchemy, alembic, etc., if you don't have one yet):
pip install -r requirements.txt

(Note: If you don't have requirements.txt yet, make sure to install FastAPI, Uvicorn, SQLAlchemy, psycopg2-binary, and Alembic manually with pip install.)
3. Start the backend server:
uvicorn main:app --reload

The backend should be running at http://localhost:8000.
3. Frontend Setup
   1. Navigate to the frontend directory:
cd frontend/ # or the name of your frontend folder

   2. Install dependencies using pnpm:
pnpm install

   3. Create a .env.local file in the root of the frontend directory with the following environment variable:
NEXT_PUBLIC_API_URL=http://localhost:8000

   4. Start the Next.js development server:
pnpm run dev

The frontend should be available at http://localhost:3000 (or Next.js's default port).
🚀 Application Usage
Once both the backend and frontend are up and running:
      1. Register and Login: Access the application through the login interface. There should be a registration endpoint available for you to create a new user or a default user to log in with.
      2. Create Tasks: Once logged in, you can start creating your tasks and subtasks.
      3. Task Management: You will be able to move tasks between pending and completed sections, and edit their details.
🤝 Contribution
If you wish to contribute to this project, please follow the standard fork and pull request workflow.