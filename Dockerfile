# 
FROM python:3.11.2

# 
WORKDIR /storeapi

# 
COPY ./requirements.txt /storeapi/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /storeapi/requirements.txt

# 
COPY ./app /storeapi/app

# 
CMD ["uvicorn", "app.main:product_store_api", "--host", "0.0.0.0", "--port", "8000"]
