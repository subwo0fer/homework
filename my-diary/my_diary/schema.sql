CREATE TABLE IF NOT EXISTS diary (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    task_description TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT 'not done',
    deadline DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
)
