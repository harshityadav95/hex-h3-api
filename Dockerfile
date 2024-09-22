# Use the official Python 3.12 slim image as the base
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 80


HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl --fail http://localhost:80/health || exit 1

# Define the command to run when the container starts
# This command runs the FastAPI application using Uvicorn
# main.py: The main FastAPI application file
# --port 80: Specifies the port to listen on
#ENTRYPOINT ["fastapi", "run", "main.py", "--port", "8501"]


# Run app.py when the container launches
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
# 2. **`WORKDIR /app`:**
#    - This sets the working directory inside the container to `/app`.
#    - All subsequent commands will be executed within this directory.

# 3. **`RUN pip install --no-cache-dir --upgrade -r requirements.txt`:**
#    - This line installs the project dependencies listed in the `requirements.txt` file.
#    - `--no-cache-dir` disables caching of downloaded packages, ensuring a clean build.
#    - `--upgrade` upgrades packages to the latest available versions.

# 4. **`COPY . .`:**
#    - This copies all files and directories from the current directory (on the host machine) to the working directory inside the container (`/app`).

# 5. **`CMD ["uvicorn", "main:app\ refers to the `app` object (usually an instance of `FastAPI`) in the `main.py` file.
#    - `--host 0.0.0.0` makes the application accessible from outside the container.
#    - `--port 80` specifies the port to listen on (port 80 is the default HTTP port).

# **Key improvements in this rewritten version:**

# - **Using `uvicorn`:** The original command `["fastapi", "run", "main.py", "--port", "80"]` is not the recommended way to run FastAPI in production. `uvicorn` is a more performant and robust ASGI server for FastAPI.
# - **Specifying `main:app`:** This explicitly tells `uvicorn` where to find the FastAPI application object.
# - **Using `--host 0.0.0.0`:** This ensures the application is accessible from outside the container.

# This revised Dockerfile provides a more efficient and production-ready way to run your FastAPI application in a Docker container. Remember to create a `requirements.txt` file listing your project's dependencies and a `main.py` file containing your FastAPI application code.
