@echo off
call docker exec -it prssai_worker sh -c "python prompt.py %*"