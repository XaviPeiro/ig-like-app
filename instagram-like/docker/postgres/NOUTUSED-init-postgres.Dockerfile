FROM postgres:latest

WORKDIR /app

# Copy initialization script into the container
COPY docker/postgres/init-postgres.sh /app/docker/postgres/init-postgres.sh

# Grant execute permissions to the script
RUN chmod +x /app/docker/postgres/init-postgres.sh

ENTRYPOINT ["/app/docker/postgres/init-postgres.sh"]
