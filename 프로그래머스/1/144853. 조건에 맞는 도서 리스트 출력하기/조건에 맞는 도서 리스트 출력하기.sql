-- 코드를 입력하세요
SELECT book_id, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE FROM BOOK
where year(Published_date)=2021 and CATEGORY='인문'
order by Published_date;