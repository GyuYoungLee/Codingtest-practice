-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile

-- 모든 레코드 조회하기 (ORDER BY)
-- 모든 동물 (ANIMAL_ID 순 조회)
select animal_id, animal_type, datetime, intake_condition, name, sex_upon_intake
from animal_ins
order by animal_id;

-- 역순 정렬하기 (ORDER BY ~ DESC)
-- 모든 동물의 이름과 보호 시작일 (ANIMAL_ID 역순)
select name, datetime
from animal_ins
order by animal_id desc;

-- 아픈 동물 찾기 (WHERE ~ =)
-- 아픈 동물의 아이디와 이름 (아이디 순서)
select animal_id, name
from animal_ins
where intake_condition = 'Sick'
order by animal_id;

-- 어린 동물 찾기 (WHERE ~ !=)
-- 어린 동물의 아이디와 이름 (아이디 순서)
select animal_id, name
from animal_ins
where intake_condition != 'Aged'
order by animal_id;

-- 동물의 아이디와 이름 (ORDER BY)
-- 모든 동물의 아이디와 이름 (아이디 순서)
select animal_id, name
from animal_ins
order by animal_id;

-- 여러 기준으로 정렬하기 (ORDER BY ~ ASC, ~ DESC)
-- 모든 동물의 아이디와 이름, 보호 시작일 (이름 순, 보호시작일 역순)
select animal_id, name, datetime
from animal_ins
order by name, datetime desc;

-- 상위 n개 레코드 (LIMIT)
-- 가장 먼저 들어온 동물의 이름을 조회
select name
from animal_ins
order by datetime
limit 1;