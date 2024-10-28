@echo off

:: define the logfile
set LOGFILE=pipeline_log.txt

:: Set working directory to where main.py is located
cd /d "C:\path\to\your\script\directory"

:: Set Python path explicitly and enclose in quotes
set "PYTHON_PATH=C:\Program Files\Python312\python.exe"

:: log the start time
echo running pipeline at %date% %time% >> %LOGFILE%

:: run the main.py and log the output, with path enclosed in quotes
"%PYTHON_PATH%" main.py >> %LOGFILE% 2>&1

:: log the end time
echo pipeline completed at %date% %time% >> %LOGFILE%

echo. >> %LOGFILE%
