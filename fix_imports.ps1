Get-ChildItem backend -Recurse -Filter *.py | ForEach-Object {
    (Get-Content $_.FullName) `
    -replace 'from backend\.agents', 'from agents' `
    -replace 'from backend\.schemas', 'from schemas' `
    -replace 'from backend\.services', 'from services' `
    -replace 'from backend\.database', 'from database' `
    -replace 'from backend\.utils', 'from utils' `
    -replace 'from backend\.models', 'from models' |
    Set-Content $_.FullName
}