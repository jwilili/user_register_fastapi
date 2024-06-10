# User Registration API

**Create a Virtual Environment**:
    ```sh
    python -m venv venv
    ```

 **Activate the Virtual Environment**:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

**Install the Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Build and Start the Docker Containers**:
    ```sh
    docker-compose up --build
    ```

2. **The API will be available at** `http://localhost:8000`.

## Running Tests

1. **Make sure the containers are running**:
    ```sh
    docker-compose up --build
    ```

2. **Run the tests**:
    ```sh
    pytest
    ```

## Environment Variables

You can configure the application using environment variables. Create a `.env` file at the root of the project with the following content:

```plaintext
DATABASE_URL=postgresql://user:password@localhost:5432/user_registration
SMTP_SERVER=smtp.example.com
SMTP_PORT=587
SMTP_USERNAME=your_email@example.com
SMTP_PASSWORD=your_password

