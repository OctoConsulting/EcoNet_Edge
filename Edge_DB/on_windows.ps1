# run using powershell.exe on_windows.ps1
docker build -t database_mk1 .
docker run -it -p 5432:5432 -e POSTGRES_PASSWORD=changemeoctobby database_mk1