@echo off
call docker exec prssai_worker sh -c "python article_silent.py %*"