-- first part 

/* select 
people.nameFirst as hof_first, 
people.nameLast as hoflast, 
teammate_people.nameFirst as teammate_first, 
teammate_people.nameLast as teammate_last
from people
inner join halloffame on
halloffame.playerID = people.playerID
inner join appearances on
appearances.playerID = halloffame.playerID
inner join appearances as teammates on
teammates.teamID = appearances.teamID and 
teammates.yearID = appearances.yearID and 
teammates.playerID != appearances.playerID
inner join people as teammate_people on
teammate_people.playerID = teammates.playerID
where halloffame.inducted = 'Y'
limit 10; */


-- second part


with teammate_ranks as (select 
people.playerID AS hof_id,
people.nameFirst || ' ' || people.nameLast AS hof_name,
teammate_people.nameFirst || ' ' || teammate_people.nameLast AS teammate_name,
appearances.yearID,
row_number() over (
    partition by people.playerID
    order by appearances.yearID asc, teammate_people.nameLast asc, teammate_people.nameFirst asc
) as rn 
from people
inner join halloffame on
halloffame.playerID = people.playerID
inner join appearances on
appearances.playerID = halloffame.playerID
inner join appearances as teammates on
teammates.teamID = appearances.teamID and 
teammates.yearID = appearances.yearID and 
teammates.playerID != appearances.playerID
inner join people as teammate_people on
teammate_people.playerID = teammates.playerID
where halloffame.inducted = 'Y')
select hof_name, teammate_name, yearID from teammate_ranks
where rn = 1
order by hof_name asc
limit 10;