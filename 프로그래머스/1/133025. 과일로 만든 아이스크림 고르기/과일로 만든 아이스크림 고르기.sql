-- 코드를 입력하세요
SELECT FIRST_HALF.flavor from FIRST_HALF
    join ICECREAM_INFO
    on FIRST_HALF.flavor = ICECREAM_INFO.flavor
where INGREDIENT_TYPE = 'fruit_based' 
    and total_order >=3000