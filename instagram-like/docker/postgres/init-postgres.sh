#!/bin/bash

echo " Starting migrations..."
alembic upgrade head
