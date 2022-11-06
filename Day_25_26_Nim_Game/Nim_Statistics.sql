SELECT * FROM nim_games;

CREATE VIEW v_raw_wins
AS
SELECT 
--player_a_id, -- i am going to merge queries
np.name PlayerName,
sum(game_result) wins,
count(game_result)-sum(game_result) losses
FROM nim_games ng 
JOIN nim_players np 
ON player_a_id = np.id 
GROUP BY player_a_id 
UNION -- https://www.sqlitetutorial.net/sqlite-union/
SELECT 
--player_b_id, -- we do not need the id
np.name PlayerName,
count(game_result)-sum(game_result) wins,
sum(game_result) losses
FROM nim_games ng 
JOIN nim_players np 
ON player_b_id = np.id 
GROUP BY player_b_id ;

CREATE VIEW v_grouped_wins
AS
SELECT PlayerName, 
SUM(wins) wins,
SUM(losses) wins
FROM v_raw_wins vrw 
GROUP BY PlayerName ;

