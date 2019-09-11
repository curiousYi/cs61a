CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT 
    dogs.name, sizes.size
  FROM dogs, sizes
  WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_height AS
  SELECT parents.child
  FROM dogs, parents
  WHERE dogs.name = parents.parent
  ORDER BY dogs.height DESC;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  with same_size (sib1, sib2, size) as
    (SELECT 
      dogs.name, doggo.name, size_of_dogs.size
      FROM dogs, dogs as doggo, parents, parents as doggo_parents,
      size_of_dogs, size_of_dogs as size_of_doggos
      WHERE dogs.name = parents.child AND doggo.name = doggo_parents.child AND dogs.name < doggo.name
      AND dogs.name = size_of_dogs.name AND doggo.name = size_of_doggos.name AND size_of_doggos.size = size_of_dogs.size
      AND parents.parent = doggo_parents.parent
      ORDER BY size_of_doggos.size
    )
  SELECT sib1 || ' and ' || sib2 || ' are ' || size || ' siblings' FROM same_size;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
CREATE TABLE stacks AS
  WITH heights(names_so_far, number_of_dogs, last_height, total_height) as (
    SELECT name, 1, height, height FROM dogs 
    UNION
    SELECT names_so_far || ',' || name, number_of_dogs + 1, height, total_height + height
    FROM dogs, heights
    WHERE number_of_dogs <= 3
    AND height > last_height
  )
  SELECT * FROM heights;
