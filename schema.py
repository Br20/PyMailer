instructions = [
    'DROP TABLE IF EXISTS email;',
    """
    CREATE TABLE email(
        id INT PRIMARY KEY AUTO_INCREMENT,
        addr_to TEXT NOT NULL,
        subject TEXT NOT NULL,
        context TEXT NOT NULL
    );
    """
]
