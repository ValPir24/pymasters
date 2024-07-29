FROM python:3.12-slim

WORKDIR /code

# Копіюємо файли залежностей до контейнера
COPY requirements.txt /code/

# Інсталюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проект до контейнера
COPY . /code

CMD ["uvicorn", "pymasters.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
 
   
