-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
FROM ANIMAL_INS AS i join ANIMAL_OUTS AS o
on i.ANIMAL_ID=o.ANIMAL_ID
where (I.SEX_UPON_INTAKE like 'Intact%' and O.SEX_UPON_OUTCOME like 'Neutered%') 
or (I.SEX_UPON_INTAKE like 'Intact%' and O.SEX_UPON_OUTCOME like 'Spayed%')
