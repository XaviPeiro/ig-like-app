FROM postgres:16-alpine
LABEL authors="ras"

ENTRYPOINT ["top", "-b"]