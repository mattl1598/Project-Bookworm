select books.isbn, books.copy_no, loans.dates, schools.name
	from books, loans, schools
	join books loans ON books.loan_id = loans.loan_id
	join loans schools ON loans.school_id = schools.school_id
where books.isbn = 9780141047843
order by isbn