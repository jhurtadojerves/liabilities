### Build and install packages
FROM python:3.10

RUN python --version

COPY . /app/
WORKDIR /app

EXPOSE 8000

# Install Python dependencies
RUN pip install -U pip && pip install -r requirements_dev.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
