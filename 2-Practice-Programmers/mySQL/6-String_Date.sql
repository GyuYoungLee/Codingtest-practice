-- noinspection SqlDialectInspectionForFile
-- noinspection SqlNoDataSourceInspectionForFile

-- 루시와 엘라 찾기 (IN)
-- 이름이 Lucy, Ella, Pickle, Rogan, Sabrina, Mitty인 동물의 아이디, 이름, 중성화 여부
select animal_id, name, sex_upon_intake
from animal_ins
where name in ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty');

-- 이름에 el이 들어가는 이름 찾기 (LIKE)
-- 이름에 "EL"이 들어가는 개의 아이디와 이름 (이름 순 조회)
select animal_id, name
from animal_ins
where animal_type = 'Dog' and name like '%el%'
order by name;

-- 중성화 여부 파악하기 (IF)
-- 동물의 아이디와 이름, 중성화 여부, 이때 중성화가 되어있다면 'O', 아니라면 'X' (아이디 순 조회)
select animal_id, name, if(sex_upon_intake regexp 'Neutered|Spayed', 'O', 'X')
from animal_ins
order by animal_id;

-- 오랜기간 보호한 동물 (DATEDIFF, TIMESTAMPDIFF)
-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름 조회 (보호 기간 긴 순)
select o.animal_id, o.name
from animal_outs o 
    inner join animal_ins i using(animal_id)
order by timestampdiff(minute, i.datetime, o.datetime) desc
limit 2;

-- DATETIME에서 DATE로 형 변환 (DATE_FORMAT)
-- 각 동물의 아이디와 이름, 들어온 날짜를 조회 (아이디 순 조회)
select animal_id, name, date_format(datetime, '%Y-%m-%d')
from animal_ins
order by animal_id;
