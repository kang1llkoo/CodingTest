SELECT A.title,
    A.board_id,
    B.reply_id,
    B.writer_id,
    B.contents,
    DATE_FORMAT(B.created_date, '%Y-%m-%d') as created_date
FROM used_goods_board as A
INNER JOIN used_goods_reply as B
ON A.board_id = B.board_id
WHERE SUBSTR(A.created_date, 1, 7) = '2022-10'
ORDER BY B.created_date asc, A.title asc