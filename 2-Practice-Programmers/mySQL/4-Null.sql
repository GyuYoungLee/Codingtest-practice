-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile

-- 이름이 없는 동물의 아이디 (IS NULL)
-- 이름이 없는 채로 들어온 동물의 ID (ID 순 조회)
select animal_id
from animal_ins
where name is null
order by animal_id;

-- 이름이 있는 동물의 아이디 (IS NOT NULL)
-- 이름이 있는 동물의 ID (ID 순)
select animal_id
from animal_ins
where name is not null
order by animal_id;

-- NULL 처리하기 (IFNULL)
-- 이름이 없는 동물의 이름은 "No name"으로 표시 (ID 순)
select animal_type, ifnull(name, "No name"), sex_upon_intake
from animal_ins
order by animal_id;
