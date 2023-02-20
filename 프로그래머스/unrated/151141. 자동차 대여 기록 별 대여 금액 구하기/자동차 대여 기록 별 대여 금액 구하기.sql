-- 코드를 입력하세요
SELECT
    HISTORY_ID,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE)+1 < 7
        THEN ROUND(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1) * 1.0)       
        WHEN DATEDIFF(END_DATE, START_DATE)+1 < 30
        THEN ROUND(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1) * 0.95)
        WHEN DATEDIFF(END_DATE, START_DATE)+1 < 90
        THEN ROUND(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1) * 0.92)
        ELSE ROUND(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1) * 0.85)
    END AS FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
INNER JOIN CAR_RENTAL_COMPANY_CAR USING (CAR_ID)
WHERE CAR_TYPE = '트럭'
ORDER BY FEE DESC, HISTORY_ID DESC;