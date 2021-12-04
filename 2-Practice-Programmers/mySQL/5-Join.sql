-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile

-- 없어진 기록 찾기 (LEFT JOIN)
-- 나간 기록은 있는데, 들어온 기록이 없는 동물의 ID와 이름 (ID 순 조회)
select o.animal_id, o.name
from animal_outs o
    left join animal_ins i using(animal_id)
where i.animal_id is null
order by o.animal_id;

-- 있었는데요 없었습니다 (INNER JOIN)
-- 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름 (보호 시작일이 빠른 순)
select i.animal_id, i.name
from animal_ins i
    inner join animal_outs o using(animal_id)
where i.datetime > o.datetime
order by i.datetime;

-- 오랜 기간 보호한 동물(1) (LEFT JOIN)
-- 나간 기록은 있는데, 들어온 기록이 없는 가장 오래된 3마리의 이름과 보호 시작일 (보호 시작일 순)
select i.name, i.datetime
from animal_ins i
    left join animal_outs o using(animal_id)
where o.animal_id is null
order by i.datetime 
limit 3;

-- 보호소에서 중성화한 동물 (INNER JOIN)
-- 중성화되지 않았지만, 나갈 당시에는 중성화된 동물의 아이디, 종, 이름 (ID 순 조회)
select i.animal_id, i.animal_type, i.name
from animal_ins i
    inner join animal_outs o using(animal_id)
where 
    i.sex_upon_intake like 'Intact%'
    -- and (o.sex_upon_outcome like 'Neutered%' or o.sex_upon_outcome like 'Spayed%')
    and o.sex_upon_outcome regexp 'Neutered|Spayed'
order by i.animal_id;