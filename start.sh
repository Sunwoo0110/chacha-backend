#!/bin/bash
cd app

uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2 --timeout-keep-alive 30 --keep-alive 10
