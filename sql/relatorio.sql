WITH plataforma_vencedora AS(SELECT plataforma,COUNT(plataforma)
FROM raw_mental_health
GROUP BY plataforma
ORDER BY COUNT(plataforma) DESC
LIMIT 1)




SELECT COUNT(id) AS total_pesquisados,ROUND(AVG(idade),2)AS media_idade,
MAX(idade) AS maior_idade, MIN(idade) AS menor_idade,
plataforma_vencedora.plataforma
FROM raw_mental_health
CROSS JOIN plataforma_vencedora
GROUP BY plataforma_vencedora.plataforma