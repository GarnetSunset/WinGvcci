Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "loop.py" & Chr(34), 0
Set WshShell = Nothing