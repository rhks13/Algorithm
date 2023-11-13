-- 코드를 입력하세요
# SELECT HISTORY_ID,	CAR_ID,	date_format(START_DATE,'%Y-%m-%d') as START_DATE,	date_format(END_DATE,'%Y-%m-%d') as END_DATE,	
# CASE 
#     when DATEDIFF(END_DATE,START_DATE)+1 >=30 then '장기 대여'
#     else '단기 대여'
# end as RENT_TYPE
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where start_date like "%2022-09%"
# order by 'history_id' desc

SELECT history_id, car_id, DATE_FORMAT(start_date, '%Y-%m-%d') START_DATE,
        DATE_FORMAT(end_date, '%Y-%m-%d') END_DATE,
        CASE WHEN DATEDIFF(end_date, start_date)+1 >= 30 THEN '장기 대여'
                ELSE '단기 대여'
            END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '%2022-09%'
ORDER BY history_id DESC;