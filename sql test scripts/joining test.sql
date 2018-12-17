SELECT books.isbn, books.copy_no, loans.loan_id, loans.date, loans.school_id, loans.active
	FROM books
	JOIN books loaned_books ON books.isbn = loaned_books.isbn
	JOIN books loaned_books ON books.copy_no = loaned_books.copy_no
	JOIN loaned_books loans ON loaned_books.loan_id loans.loan_id 
ORDER BY isbn