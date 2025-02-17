FROM dpage/pgadmin4

ENV PGADMIN_EMAIL=admin@banka.com

ENV PGADMIN_PASSWORD=admin

EXPOSE 80

COPY entrypoint.py Docker\entrypoint.py

CMD ["python3", "/entrypoint.py"]