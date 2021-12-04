-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile

-- 최댓값 구하기 (MAX)
-- 가장 최근에 들어온 동물
select max(datetime)
from animal_ins;

-- 최솟값 구하기 (MIN)
-- 가장 먼저 들어온 동물
select min(datetime)
from animal_ins;

-- 동물 수 구하기 (COUNT)
-- 동물이 몇 마리 들어왔는지
select count(animal_id)
from animal_ins;

-- 중복 제거하기 (distinct COUNT)
-- 동물의 이름은 몇 개인지, 이름 중복 제거
select count(distinct name)
from animal_ins;