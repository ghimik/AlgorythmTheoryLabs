BEGIN TRANSACTION;

INSERT INTO public.adjective (word)
VALUES
('яркий'),
('грустный'),
('волнительный'),
('светлый'),
('мрачный');

INSERT INTO public.noun (word)
VALUES
('свет'),
('тень'),
('жизнь'),
('сердце'),
('любовь');

INSERT INTO public.verb (word)
VALUES
('гореть'),
('блестеть'),
('лететь'),
('кружиться'),
('цвести');

COMMIT;