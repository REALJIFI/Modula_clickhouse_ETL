:: this will help to turn of printing
@echo off 

:: define the logfile
set LOGFILE=pipeline_log.txt

:: log the start time
echo running pipeline at %date% %time% >> %LOGFILE% 

:: run the main.py and log the output
C:\Program Files\YourPathHere\YourExecutable.exe main.py >> %LOGFILE% 2>&1

:: log the end time
echo pipeline completed at %date% %time% >> %LOGFILE% 

echo. >> %LOGFILE%

