-- 코드를 입력하세요
SELECT truncate(PRICE,-4) as price_group,	count(PRODUCT_ID) as PRODUCTS
from PRODUCT 
group by price_group
ORDER by price_group