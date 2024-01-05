-- 조회수가 가장 높은 중고거래 게시물
-- 첨부파일경로
-- FILE ID 내림차순
-- /home/grep/src/ + 게시글ID, 파일ID, 파일이름, 파일확장자
SELECT
CONCAT("/home/grep/src/", BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) AS FILE_PATH
FROM USED_GOODS_FILE
WHERE BOARD_ID = (
    SELECT BOARD_ID
    FROM USED_GOODS_BOARD
    ORDER BY VIEWS DESC
    LIMIT 1
)
ORDER BY FILE_ID DESC;

SELECT CONCAT("/home/grep/src/",F.BOARD_ID,"/", F.FILE_ID, F.FILE_NAME, F.FILE_EXT) AS FILE_PATH
FROM USED_GOODS_BOARD AS B
JOIN USED_GOODS_FILE AS F
ON B.BOARD_ID = F.BOARD_ID
WHERE B.VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY F.FILE_ID DESC