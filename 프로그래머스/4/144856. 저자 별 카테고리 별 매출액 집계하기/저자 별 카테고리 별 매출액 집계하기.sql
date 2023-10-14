SELECT  A.AUTHOR_ID, 
        A.AUTHOR_NAME,
        B.CATEGORY,
        SUM(SALES * PRICE) AS TOTAL_SALES
FROM BOOK_SALES BS
JOIN BOOK B ON B.BOOK_ID = BS.BOOK_ID
JOIN AUTHOR A ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE DATE_FORMAT(BS.SALES_DATE,'%Y-%m') = '2022-01'
GROUP BY A.AUTHOR_ID, B.CATEGORY
ORDER BY A.AUTHOR_ID ASC, B.CATEGORY DESC;
