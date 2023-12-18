-- 코드를 입력하세요
SELECT MCDP_CD AS 진료과코드,count(DATE_FORMAT(APNT_YMD,'%Y-%m')) AS 5월예약건수
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD,'%Y-%m')='2022-05'
group by 진료과코드
order by 5월예약건수,진료과코드;
