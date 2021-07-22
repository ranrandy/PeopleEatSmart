# 1. Insert a new comment (rating)
INSERT INTO RatingComment (RatingValue, COMMENT, UserName, RecipeID)
VALUES(2, 'Bad', 'Randy', (SELECT RecipeID FROM Recipe WHERE Name = 'Dilly Bread'));
-- INSERT INTO RatingComment (RatingValue, COMMENT, UserName, RecipeID)
-- VALUES([int rating value], [comment string], [username string], (SELECT RecipeID FROM Recipe WHERE Name = [recipe name string]));


########################################## FINISHED ##########################################
# 1.1 (Alternative) Insert a new username
# -- I don't think of any good 'delete' operation except deleting an account.
# -- So, insert a new account first then we can do 'delete' is also okay.
INSERT INTO LoginInfo VALUES('Randy', '1234567');
-- INSERT INTO LoginInfo VALUES([username], [password]);
########################################## FINISHED ##########################################


# 2. Search (based on keyword) a recipe
SELECT Name, PictureURL, AvgRating, RatingCount 
FROM Recipe
WHERE Name LIKE '%spaghetti%';
-- SELECT Name, PictureURL, AvgRating, RatingCount 
-- FROM Recipe
-- WHERE Name LIKE '%[keyword]%';


# 3. Update password
UPDATE LoginInfo
SET Password = '7654321'
WHERE UserName = 'Randy';
-- UPDATE LoginInfo
-- SET Password = [new password]
-- WHERE UserName = [username];


# 4. Delete username
DELETE FROM LoginInfo
WHERE UserName = 'Randy';
-- DELETE FROM LoginInfo
-- WHERE UserName = [username];



# 5. Stage 3 Advanced Query 1
SELECT IngredientName, COUNT(RecipeID)
FROM IngredientOf NATURAL JOIN Ingredient NATURAL JOIN Recipe NATURAL JOIN Contains NATURAL JOIN Micronutrient m
WHERE AvgRating > 3 AND Quantity > 5 AND m.NutrientName = 'fiber'
GROUP BY IngredientID
ORDER BY COUNT(RecipeID) DESC;


# 6. Stage 3 Advanced Query 2
SELECT DISTINCT r.Name, AvgRating
FROM Ingredient i NATURAL JOIN Contains c NATURAl JOIN Micronutrient m NATURAL JOIN IngredientOf ino NATURAL JOIN Recipe r
WHERE m.NutrientName = 'calcium' AND r.AvgRating >= (SELECT AVG(AvgRating) FROM Recipe)


