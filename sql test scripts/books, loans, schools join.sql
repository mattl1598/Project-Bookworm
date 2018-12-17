SELECT books.isbn, books.copy_no, schools.name
FROM books
LEFT JOIN loans
ON books.loan_id = loans.loan_id
LEFT JOIN schools
ON loans.school_id = schools.school_id;