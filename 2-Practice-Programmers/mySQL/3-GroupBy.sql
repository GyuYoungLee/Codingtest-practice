-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile

-- 고양이와 개는 몇 마리 있을까 (GROUP BY)
-- 고양이와 개가 각각 몇 마리인지 조회 (animal_type 순)
select animal_type, count(animal_type)
from animal_ins
group by animal_type
order by animal_type;

-- 동명 동물 수 찾기 (GROUP BY ~ HAVING)
-- 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회 (이름 순)
select name, count(name)
from animal_ins
group by name
having count(name) >= 2
order by name;

-- 입양 시각 구하기(1) (WHERE ~ GROUP BY)
-- 각 시간대별로 입양이 몇 건이나 발생했는지 조회 (시간대 순)
select hour(datetime), count(datetime)
from animal_outs
where hour(datetime) >=9 and hour(datetime) < 20
group by hour(datetime)
order by hour(datetime);

-- 입양 시각 구하기(2) (WITH RECURSIVE)
-- 각 시간대별로 입양이 몇 건이나 발생했는지 조회 (시간대 순)
with recursive time as (
    select 0 as h
    union all
    select h + 1 from time where h < 23
)
select h from time;

select hour(datetime), count(datetime)
from animal_outs
group by hour(datetime);

with recursive time as (
    select 0 as h
    union all
    select h + 1 from time where h < 23
)
select h, count(datetime)
from time
    left join animal_outs on h = hour(datetime)
group by h
order by h;