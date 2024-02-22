## Usage Tutorial

Follow these steps to get started with the project:

1. **Clone the Repository:** Clone this repository to your local system.
   
2. **Set Up Virtual Environment:**
   - For Windows:
     ```bash
     virtualenv venv
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     virtualenv venv
     source venv/bin/activate
     ```

3. **Install Requirements:** Install project dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database:** Initialize the SQLite3 database by running the following command:
   ```bash
   alembic upgrade head
   ```
   This will add `sql_app.db` to the root directory.

5. **Run the Server:** Start the Uvicorn server by executing:
   ```bash
   python main.py
   ```
   The server will automatically run on `localhost:8000`. You can modify the port in `main.py` if needed.

6. **Access the App:** Open your web browser and navigate to `http://127.0.0.1:8000` to start using the app!
