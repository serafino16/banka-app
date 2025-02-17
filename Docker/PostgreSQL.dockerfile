FROM postgres:15-alpine

ENV POSTGRES_USER=banka_user

ENV POSTGRES_PASSWORD=banka_password

ENV POSTGRES_DB=banka_database

EXPOSE 5432

CMD ["postgres"]
