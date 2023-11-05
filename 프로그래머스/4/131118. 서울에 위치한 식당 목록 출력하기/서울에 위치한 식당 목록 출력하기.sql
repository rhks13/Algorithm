-- 코드를 입력하세요
SELECT REST_INFO.REST_ID,	REST_INFO.REST_NAME,	REST_INFO.FOOD_TYPE,	REST_INFO.FAVORITES,	REST_INFO.ADDRESS,	round(avg(REST_REVIEW.REVIEW_SCORE),2) as SCORE 
from REST_INFO
right join REST_REVIEW
on rest_info.REST_ID = rest_review.REST_ID
where address like '서울%'
group by REST_ID
order by score desc, favorites desc

