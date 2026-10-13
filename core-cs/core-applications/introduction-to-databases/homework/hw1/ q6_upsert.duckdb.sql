INSERT INTO teams (yearID, lgID, teamID, franchID, teamRank, attendance) -- okay this acts as hey db I want
SELECT yearID, lgID, franchID, franchID, teamRank, attendance -- and then select, this and that to insert
FROM teams
WHERE yearID = 2024
ON CONFLICT (yearID, teamID) DO UPDATE 
SET attendance = -1;