import io

filepath = r'c:\Users\Barra\Documents\Ruk - Historia Completa\Ruk_Editado\Capitulo_09_Heroes_de_Davir.md'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if 'pendiente de ser devueltas' in line:
        line = line.replace('pendiente de ser devueltas', 'pendiente de ser devuelta')
    if 'e hundió la hoja sagrada' in line:
        line = line.replace('e hundió la hoja sagrada', 'y hundió la hoja sagrada')
    if 'Con sus últimas fuerzas, Korlan salió a trompicones de la tienda con la cabeza decapitada' in line:
        line = 'Pero Korlan, en un último aliento de vida, sacó una daga oculta y se la clavó profundamente en la garganta a Jezik. El general abrió los ojos, horrorizado, y se desplomó inerte. Con un esfuerzo titánico, Korlan empujó el cadáver ensangrentado de Jezik fuera de la tienda ante la vista de las tropas enemigas. Al presenciar el cuerpo sin vida de su líder, los pocos invasores que aún resistían rompieron filas y huyeron despavoridos. Korlan se dejó caer de espaldas dentro del recinto y exhaló su último suspiro, orgulloso del héroe que había ayudado a forjar.\n'
    if 'De pronto, un carruaje dorado irrumpió en el campamento' in line:
        # Skip until after Imi description
        new_lines.append('''De pronto, el rey Ásek irrumpió a caballo en el campamento, escoltado por la caballería blindada de la Guardia Real. Desmontó de un salto, vistiendo su armadura de combate curtida por la batalla.

—Mi rey, la guerra ha finalizado —anunció el Inferento Limaz e inclinó la cabeza con respeto.

—¿Fuiste tú el que hizo todo esto, Limaz?

—No fui yo, mi señor. Fue él. —Limaz señaló a Ruk.

El rey se acercó al joven héroe, cuyos ojos aún reflejaban el cansancio y el duelo por su padre.

—¿En serio eres el joven que abatió a esa monstruosidad y salvó a nuestro ejército? —preguntó el monarca con genuino asombro.

—Sí, majestad. Pero fue el valor de cada soldado y de mis amigos lo que hizo posible esta victoria —respondió Ruk con nobleza.

—Qué admirable lealtad —el rey sonrió ampliamente y le puso una mano en el hombro—. Como soberano, te ofrezco los máximos honores de la corte y la mano de mi hija menor, la princesa Imi, para unirte a la casa real.

Ruk miró a Riav a los ojos y dio un paso al frente con firmeza y serenidad.

—Majestad, es el honor más grande que podríais ofrecerme, pero debo declinar el compromiso real. Mi corazón y mi lealtad pertenecen a Riav, y mi deber es regresar con ella para reconstruir mi pueblo natal de Davir. Serviré a este reino como Caballero Guardián siempre que me necesitéis.

El rey Ásek observó el rostro de Ruk y la determinación de Riav a su lado. La severidad de su semblante dio paso a una profunda sonrisa de respeto.

—Un verdadero guerrero no traiciona a su corazón ni a su hogar. Que así sea, Ruk. Te nombro Caballero Guardián de Davir, con el título honorario de Edeka, "el que venció". Tenéis mi bendición para regresar a vuestra tierra.\n''')
        # Skip original lines up to 'Horas después'
        while i < len(lines) and 'Horas después' not in lines[i]:
            i += 1
        continue
    new_lines.append(line)
    i += 1

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Successfully edited Capitulo 9!')
