@echo off
call docker exec prssai_worker sh -c "python prompt_silent.py %*"