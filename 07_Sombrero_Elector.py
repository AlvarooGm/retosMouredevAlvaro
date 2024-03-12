'''

/*
 * Crea un programa que simule el comportamiento del sombrero selccionador del
 * universo mágico de Harry Potter.
 * - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal.
 * - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal).
 * - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que
 *   coloque al alumno en una de las 4 casas de Hogwarts:
 *   (Gryffindor, Slytherin , Hufflepuff y Ravenclaw)
 * - Ten en cuenta los rasgos de cada casa para hacer las preguntas
 *   y crear el algoritmo seleccionador:
 *   Por ejemplo, en Slytherin se premia la ambición y la astucia.
 */

1. ¿Qué valor consideras más importante en un estudiante: la valentía, la sabiduría, la lealtad o la ambición?
2. ¿Prefieres aprender mediante la práctica y la experiencia directa o a través del estudio y la reflexión profunda?
3. ¿Qué cualidad crees que te define mejor: la determinación, la creatividad, la paciencia o la astucia?
4. ¿Cuál es tu reacción instintiva frente a los desafíos: enfrentarlos de frente, analizarlos detenidamente, buscar apoyo en otros o encontrar una solución astuta? 
5. ¿Te sientes más atraído por la idea de explorar lo desconocido, descubrir nuevos conocimientos, proteger a tus seres queridos o alcanzar tus metas a toda costa?
6. ¿Cómo manejas la presión y el estrés: enfrentándolos con valentía, planificando cuidadosamente, confiando en tu red de apoyo o adaptándote rápidamente a las circunstancias?
7. ¿Qué tipo de habilidades consideras más valiosas: las mágicas, las intelectuales, las sociales o las prácticas?
8. ¿Prefieres liderar y tomar decisiones importantes, contribuir con ideas innovadoras, apoyar a tus compañeros o trabajar en estrecha colaboración con un grupo?
9. Ante la injusticia, ¿cuál sería tu reacción principal: luchar contra ella, buscar comprenderla y corregirla, proteger a los afectados o encontrar una solución que beneficie a todos?
10. ¿Qué animal mágico te representa mejor: el león, el águila, el tejón o la serpiente?


1. **Valentía, determinación y enfrentar desafíos de frente:** Gryffindor.
2. **Sabiduría, estudio y reflexión profunda:** Ravenclaw.
3. **Lealtad, paciencia y apoyo a los demás:** Hufflepuff.
4. **Astucia, adaptabilidad y soluciones ingeniosas:** Slytherin.

'''


preguntas = ['¿Qué valor consideras más importante en un estudiante: la valentía, la sabiduría, la lealtad o la ambición?','¿Prefieres aprender mediante la práctica y la experiencia directa o a través del estudio y la reflexión profunda?(1/2)','¿Qué cualidad crees que te define mejor: la determinación, la creatividad, la paciencia o la astucia?','¿Cuál es tu reacción instintiva frente a los desafíos: enfrentarlos de frente, analizarlos detenidamente, buscar apoyo en otros o encontrar una solución astuta?(1/2/3/4)']
cnt_Sly=0
cnt_Grif=0
cnt_Huff=0
cnt_Raven=0


for pr in preguntas:
    print(pr)
    respuesta = input('Responda: ')

    #preg 1
    if respuesta == 'valentia':
        cnt_Grif+=1
        pass
    elif respuesta == 'sabiduria':
        cnt_Raven+=1
        pass
    elif respuesta == 'lealtad':
        cnt_Huff+=1
        pass
    elif respuesta == 'ambicion':
        cnt_Sly+=1
        pass

    #preg 2
    if pr == preguntas[1]:
        if respuesta == '1':
            cnt_Grif+=1
            cnt_Huff+=1
            pass
        elif respuesta == '2':   
            cnt_Sly+=1 
            cnt_Raven+=1
            pass          

    #preg 3

    if respuesta == 'determinacion':
        cnt_Grif+=1
    elif respuesta == 'creatividad ':
        cnt_Raven+=1
    elif respuesta == 'paciencia ':
        cnt_Huff+=1
    elif respuesta == 'astucia':
        cnt_Sly+=1

    #preg 4

    if respuesta == '1':
        cnt_Grif+=1
    elif respuesta == '2':
        cnt_Raven+=1
    elif respuesta == '3':
        cnt_Huff+=1
    elif respuesta == '4':
        cnt_Sly+=1
    

if cnt_Grif > cnt_Huff  and cnt_Grif > cnt_Raven  and cnt_Grif > cnt_Sly :
    print('La casa elegida es Griffindor')
elif cnt_Huff > cnt_Grif and cnt_Huff  > cnt_Raven  and cnt_Huff  > cnt_Sly :
    print('La casa elegida es Hufflepuff')  
elif cnt_Raven > cnt_Grif and cnt_Raven  > cnt_Huff  and cnt_Raven  > cnt_Sly :
    print('La casa elegida es Ravenclaw') 
elif cnt_Sly > cnt_Grif and cnt_Sly  > cnt_Huff  and cnt_Sly  > cnt_Raven :
    print('La casa elegida es Slytherin')  
else:
     print('¿Qué animal mágico te representa mejor: el león, el águila, el tejón o la serpiente?(1/2/3/4)')      
     respuesta = input('Responda: ')
     if respuesta == '1':
            print('La casa elegida es Griffindor')
     elif respuesta == '2':
            print('La casa elegida es Hufflepuff')  
     elif respuesta == '3':
            print('La casa elegida es Ravenclaw') 
     elif respuesta == '4':
            print('La casa elegida es Slytherin')   