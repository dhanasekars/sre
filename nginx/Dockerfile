# Use the official Nginx image
FROM nginx

RUN apt-get update && \
    apt-get install -y curl nano && \
    rm -rf /var/lib/apt/lists/*

ENV FASTAPI_UPSTREAM=app1

# Create the directory for templates if it doesn't exist
RUN mkdir -p /etc/nginx/templates

# Copy your Nginx configuration file to the container
COPY nginx.conf.template /etc/nginx/templates/nginx.conf.template
#
# Expose port 80
EXPOSE 80

# Start Nginx
CMD envsubst '${FASTAPI_UPSTREAM}' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'
