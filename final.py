"""
Tomás Fonseca ist1103726 tomas.s.fonseca@tecnico.ulisboa.pt

Este programa simula um ecossistema de um prado no qual convivem animais os quais se movem, alimentam, reproduzem e
morrem.
"""

#                                                      TAD posição
# Representação posicao -> tuplo: (<abcissa>,<ordenada>)
#CONSTUTORES
def cria_posicao(pos_x,pos_y):
    """
    cria_posicao: integer x integer -> posicao
    Recebe os valores de uma posição e devolve a posição correspondente
    """
    if type(pos_x)!=int or type(pos_y)!=int or pos_x<0 or pos_y<0:
        raise ValueError ('cria_posicao: argumentos invalidos')
    return (pos_x,pos_y)

def cria_copia_posicao(pos):
    """
    cria_copia_posicao: posicao -> posicao
    Recebe uma posição e devolve uma nova cópia da posição
    """
    if not eh_posicao(pos):
        raise ValueError ('cria_copia_posicao: argumentos invalidos')
    return cria_posicao(pos[0],pos[1])

#SELETORES
def obter_pos_x(pos):
    """
    obter_pos_x: posicao -> integer
    Recebe uma posicao e devolve a componente x da posicao
    """
    return pos[0]

def obter_pos_y(pos):
    """
    obter_pos_y: posicao -> integer
    Recebe uma posicao e devolve a componente y da posicao
    """
    return pos[1]

#RECONHECEDORES
def eh_posicao(entrada):
    """
    eh_posicao: universal -> boolean
    Devolve True se a entrada for um TAD posicao (um tuplo com 2 integers maiores que 0), devolvendo False caso
    contrário
    """
    if type(entrada)!=tuple or len(entrada)!=2 or type(entrada[0])!=int or type(entrada[1])!=int or\
            entrada[0]<0 or entrada[1]<0:
        return False
    return True

def posicoes_iguais(pos1,pos2):
    """
    posicoes iguais: posicao x posicao -> boolean
    Recebe duas posicoes e devolve True se ambos os argumentos forem posições e tiverem as coordenadas iguais
    """
    return (pos1[0]==pos2[0] and pos1[1]==pos2[1])

def posicao_para_str(pos):
    """
    posicao_para_str: posicao -> str
    Recebe uma posicao e devolve o string '(x,y)', com x e y as coordenadas da posicao pos
    """
    str_pos = '('+str(obter_pos_x(pos))+', '+str(obter_pos_y(pos))+')'
    return str_pos

#FUNÇÕES DE ALTO NÍVEL
def obter_posicoes_adjacentes(pos):
    """ obter_posicoes_adjacentes: posicao -> tuple
        Recebe uma posicao e devolve um tuplo com as posicoes adjacentes à posição p, começando pela acima e seguindo no
        sentido horário """
    if eh_posicao(pos):
        x, y = obter_pos_x(pos),obter_pos_y(pos)
        pos_adjacentes = ()
        if y>0: #Se não estiver na linha superior (as coordenadas são positivas)
            pos_adjacentes += (cria_posicao(x,y-1),)
        pos_adjacentes += (cria_posicao(x+1,y),cria_posicao(x,y+1))
        if x>0: #Se não estiver na coluna da esquerda (as coordenadas são positivas)
            pos_adjacentes+=(cria_posicao(x-1,y),)
        return pos_adjacentes

def ordenar_posicoes(tup):
    """
    ordenar_posicoes: tuple -> tuple
    Recebe um tuplo e devolve um tuplo com as posicoes ordenadas de acordo com a ordem de leitura do prado
    """
    lst_pos, organizadas = list(tup), ()
    while lst_pos != []:
        pos = lst_pos[0]
        for i in lst_pos:
            if obter_pos_y(i) < obter_pos_y(pos) or (obter_pos_x(i) < obter_pos_x(pos) and \
                                                     obter_pos_y(i) == obter_pos_y(pos)):
                pos = i #Comparar e escolher a posição com o menor y, ou o menor x, caso as ordenadas sejam iguais
        organizadas += (pos,)
        lst_pos.remove(pos)
    return organizadas

#                                                       TAD animal
#Representação animal -> dicionário: {'especie':<cad. carateres espécie>,'idade':<número idade>,
# 'rep':<número freq. de reprodução>}
# Se for predador, para além destas três chaves ainda tem {'fome':<número fome>,'ali':<número freq. de alimentação>}
#CONSTRUTORES
def cria_animal(s,r,a):
    """
    cria_animal: string x int x int -> animal
    Recebe um string não vazio, s, que é a espécie do animal, um integer r>0 que corresponde à frequência de reprodução
    e um integer a>=0, correspondente à frequência de alimentação. Se a==0, o animal é uma presa, se não é predador
    """
    if type(s)!=str or s=='' or type(r)!=int or r<=0 or type(a)!=int or a<0:
        raise ValueError ('cria_animal: argumentos invalidos')
    if a==0:
        return {'especie':s,'idade':0,'rep':r} #Cria uma presa
    return {'especie':s,'idade':0,'rep':r,'fome':0,'ali':a} #Cria um predador

def cria_copia_animal(a):
    """
    cria_copia: animal -> animal
    Recebe um animal e devolve uma cópia do mesmo
    """
    if not eh_animal(a):
        raise ValueError ('cria_copia_animal: argumentos invalidos')
    if eh_presa(a):
        return cria_animal(a['especie'],a['rep'],0)
    elif eh_predador(a):
        return cria_animal(a['especie'],a['rep'],a['ali'])

#SELETORES
def obter_especie(a):
    """
    obter_especie: animal -> string
    Recebe um animal e devolve o string correspondente à especie
    """
    return a['especie']

def obter_freq_reproducao(a):
    """
    obter_freq_reproducao: animal -> int
    Recebe um animal e devolve o integer correspondente à frequência de alimentação
    """
    return a['rep']

def obter_freq_alimentacao(a):
    """
    obter_freq_alimentacao: animal -> int
    Recebe um animal e devolve o integer correspondente à frequêncai de alimentação
    """
    if 'ali' in a:
        return a['ali']
    return 0 #Caso seja presa

def obter_idade(a):
    """
    obter_idade: animal -> int
    Recebe um animal e devolve um integer correspondente à sua idade
    """
    return a['idade']

def obter_fome(a):
    """
    obter_fome: animal -> int
    Recebe um animal e devolve um integer correspondente à sua fome
    """
    if 'fome' not in a:
        return 0
    return a['fome'] #Caso seja predador

#MODIFICADORES
def aumenta_idade(a):
    """
    aumenta_idade: animal -> animal
    Recebe um animal e incrementa a sua idade em uma unidade, devolvendo o próprio animal
    """
    a['idade'] = obter_idade(a)+1
    return a

def reset_idade(a):
    """
    reset_idade: animal -> animal
    Recebe um animal e define o valor da sua idade como 0
    """
    a['idade'] = 0
    return a

def aumenta_fome(a):
    """
    aumenta_fome: animal -> animal
    Recebe um animal e incrementa a sua fome em uma unidade, devolvendo o próprio animal
    """
    if eh_predador(a):
        a['fome'] = obter_fome(a)+1
    return a

def reset_fome(a):
    """
    reset_fome: animal -> animal
    Recebe um animal e define o valor da sua fome como 0
    """
    a['fome'] = 0
    return a

#RECONHECEDORES
def eh_animal(arg):
    """
    eh_animal: universal -> booleano
    Recebe um argumento e devolve True se corresponder a um TAD animal, devolvendo False caso contrário
    """
    if type(arg)!=dict or (len(arg)!=3 and len(arg)!=5):
        return False
    if 'especie' not in arg or type('especie')!=str or arg['especie']=='':
            return False
    if 'idade' not in arg or type(arg['idade'])!=int or arg['idade']<0:
            return False
    if 'rep' not in arg or type(arg['rep'])!=int or arg['rep']<=0:
            return False
    if len(arg)==5:
        if 'fome' not in arg or type(arg['fome'])!=int or arg['fome']<0:
            return False
        if 'ali' not in arg or type(arg['ali'])!=int or arg['ali']<=0:
            return False
    return True #Garantido um tamanho igual a 3 ou 5, confirmamos se tem todas as entradas que estão num TAD animal

def eh_predador(arg):
    """
    eh_predador: universal -> booleano
    Recebe um argumento e devolve True se for um TAD animal do tipo predador, devolvendo False caso contrário
    """
    if eh_animal(arg) and len(arg)==5:
        return True
    return False

def eh_presa(arg):
    """
    eh_presa: universal -> booleano
    Recebe um argumento e devolve True se for um TAD animal do tipo presa, devolvendo False caso contrário
    """
    if eh_animal(arg) and len(arg)==3:
        return True
    return False

#TESTE
def animais_iguais(a1,a2):
    """
    animais_iguais: animal x animal -> booleano
    Recebe 2 argumentos e devolve True se ambos forem animais e iguais, devolvendo False caso contrário
    """
    if eh_animal(a1) and eh_animal(a2) and a1['especie']==a2['especie'] and a1['idade']==a2['idade'] and\
            a1['rep']==a2['rep']:
        if len(a1)==len(a2)==3:
            return True
        elif len(a1)==len(a2)==5 and a1['fome']==a2['fome'] and a1['ali']==a2['ali']:
            return True
    return False

#TRANSFORMADORES
def animal_para_char(a):
    """
    animal_para_char: animal -> str
    Recebe um animal e devolve um caráter correspondente à primeira letra da espécie do animal (minúscula para presas,
    maiúscula para predadores)
    """
    if eh_presa(a):
        return obter_especie(a)[0].lower()
    elif eh_predador(a):
        return obter_especie(a)[0].upper()

def animal_para_str(a):
    """
    animal_para_str: animal -> str
    Recebe um animal e, se for presa, devole um string na forma 'espécie [idade/freq_reproducao]' ou, se for predador
    'espécie [idade/freq_reproducao;fome/freq_alimentacao]'
    """
    if eh_presa(a):
        animal_em_str = obter_especie(a)+' ['+str(obter_idade(a))+'/'+str(obter_freq_reproducao(a))+']'
        return animal_em_str
    if eh_predador(a):
        animal_em_str = obter_especie(a)+' ['+str(obter_idade(a))+'/'+str(obter_freq_reproducao(a))+';'+\
                        str(obter_fome(a))+'/'+str(obter_freq_alimentacao(a))+']'
        return animal_em_str

#FUNÇÕES DE ALTO NÍVEL
def eh_animal_fertil(a):
    """
    eh_animal_fertil: animal -> booleano
    Recebe um animal e devolve True se a sua idade corresponder à sua frequência de reprodução
    """
    return obter_idade(a)>=obter_freq_reproducao(a)

def eh_animal_faminto(a):
    """
    eh_animal_faminto: animal -> booleano
    Recebe um animal e devolve True se a sua fome corresponder à sua frequência de alimentação
    """
    if eh_predador(a):
        return obter_fome(a)>=obter_freq_alimentacao(a)
    return False

def reproduz_animal(a):
    """
    reproduz_animal: animal -> animal
    Recebe um animal e devolve outro da mesma espécie com idade e fome igual a 0, modificando o primeiro animal,
    alterando a sua idade para 0
    """
    if eh_presa(a):
        reset_idade(a)
        return cria_animal(obter_especie(a),obter_freq_reproducao(a),0)
    if eh_predador(a):
        reset_idade(a)
        return cria_animal(obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a))

#                                                       TAD prado
# Representação prado -> dicionário: {'dim':<posicao>,'roc':<tuplo de posicoes de rochedos>,'ani_e_pos':<lista de listas
# contendo [<animal>,<posicao do animal>]
#CONSTRUTORES
def cria_prado(d,r,a,p):
    """cria_prado: posicao x tuplo x tuplo x tuplo -> prado
    Recebe uma posição d, correspondente à montanha do canto inferior direito, um tuplo r com as posições dos rochedos,
    um tuplo a com os animais e um tuplo p com as posições ocupadas pelos animais, respetivamente e devolve o prado,
    que representa internamente o mapa e os animais presentes."""
    if not eh_posicao(d) or type(r)!=tuple or type(a)!=tuple or a==() or type(p)!=tuple or len(a)!=len(p):
        raise ValueError('cria_prado: argumentos invalidos')
    pos_usadas,x_max,y_max = [],obter_pos_x(d),obter_pos_y(d)
    for pos in r:
        if not eh_posicao(pos):
            raise ValueError('cria_prado: argumentos invalidos')
        x,y = obter_pos_x(pos), obter_pos_y(pos)
        if not eh_posicao(pos) or not 0<x<x_max or not 0<y<y_max:
            raise ValueError('cria_prado: argumentos invalidos') #Se não estiver dentro dos limites do prado
        for us in pos_usadas:
            if posicoes_iguais(us,pos):
                raise ValueError('cria_prado: argumentos invalidos') #Se a posição se repetir
        pos_usadas+=[pos]
    for i in range(len(a)):
        if not eh_posicao(p[i]):
            raise ValueError('cria_prado: argumentos invalidos')
        x,y = obter_pos_x(p[i]),obter_pos_y(p[i])
        if not eh_animal(a[i]) or not 0<x<x_max or not 0<y<y_max: #Se não estiver dentro dos limites do prado
            raise ValueError('cria_prado: argumentos invalidos')
        for us in pos_usadas:
            if posicoes_iguais(us,p[i]):
                raise ValueError('cria_prado: argumentos invalidos') #Se a posição se repetir
        pos_usadas+=[p[i]]
    return {'dim':d,'roc':r,'ani_e_pos':[[x,y] for x,y in zip(a,p)]}

def cria_copia_prado(m):
    """
    cria_copia_prado: prado -> prado
    Recebe um prado e devolve uma cópia sua
    """
    if eh_prado(m):
        a,p=(),()
        for par in m['ani_e_pos']:
            a+=(par[0],) #Adicionamos ao tuplo a todos os animais
            p+=(par[1],) #Adicionamos ao tuplo p todas as posições do animais com o mesmo índice
        return cria_prado(m['dim'],m['roc'],a,p)

#SELETORES
def obter_tamanho_x(m):
    """
    obter_tamanho_x: prado -> int
    Recebe um prado e devolve o inteiro que corresponde à sua dimensão no eixo X
    """
    return obter_pos_x(m['dim'])+1

def obter_tamanho_y(m):
    """
    obter_tamanho_y: prado -> int
    Recebe um prado e devolve o inteiro que corresponde à sua dimensão no eixo Y
    """
    return obter_pos_y(m['dim'])+1

def obter_numero_predadores(m):
    """
    obter_numero_predadores: prado -> int
    Recebe um prado e devolve o inteiro que corresponde ao número de predadores
    """
    count = 0
    for par in m['ani_e_pos']:
        if eh_predador(par[0]):
            count+=1
    return count

def obter_numero_presas(m):
    """
    obter_numero_presa: prado -> int
    Recebe um prado e devolve o inteiro que corresponde ao número de presas
    """
    count = 0
    for par in m['ani_e_pos']:
        if eh_presa(par[0]):
            count+=1
    return count

def obter_posicao_animais(m):
    """
    obter_posicao_animais: prado -> tuplo posicoes
    Recebe um prado e devolve um tuplo com as posições organizadas por ordem de leitura do prado
    """
    pos = tuple([i[1] for i in m['ani_e_pos']]) #Cria um tuplo com todas as posições dos animais num prado
    return ordenar_posicoes(pos)

def obter_animal(m,p):
    """
    obter_animal: prado x posicao -> animal
    Recebe um prado e uma posicao e devolve o animal na posição correspondente
    """
    for par in m['ani_e_pos']:
        if posicoes_iguais(par[1],p):
            return par[0]

#MODIFICADORES
def eliminar_animal(m,p):
    """
    eliminar_animal: prado x posicao -> prado
    Recebe um prado e uma posição e devolve o mesmo prado, removendo o animal que se encontra na posição p.
    """
    return m['ani_e_pos'].remove([obter_animal(m,p),p]) #Remove a lista com o animal e a sua posição

def mover_animal(m,p1,p2):
    """
    mover_animal: prado x posicao x posicao -> prado
    Recebe um prado, uma posição p1, a atual, e outra posição p2, a nova. Devolve o mesmo prado, mudando o animal na
    posição p1 para a posição p2
    """
    ani,pos = obter_animal(m,p1),p1
    for par in m['ani_e_pos']:
        if animais_iguais(ani,par[0]) and posicoes_iguais(p1,par[1]):
            par[1]=p2
            break
    return m

def inserir_animal(m,a,p):
    """
    inserir_animal: prado x animal x posicao -> posicao
    Recebe um prado e devolve o mesmo prado, adicionando o animal a na posição p
    """
    m['ani_e_pos']+=[[a,p]] #Adiciona a lista com o novo animal e a sua posição
    return m

#RECONHECEDORES
def eh_prado(arg):
    """eh_prado: universal -> boolean
       Recebe um argumento e devolve True se corresponder a um TAD prado, False, caso contrário """
    if type(arg)!=dict or len(arg)!=3 or 'dim' not in arg or 'roc' not in arg or 'ani_e_pos' not in arg or not\
            eh_posicao(arg['dim']) or type(arg['roc'])!=tuple or type(arg['ani_e_pos'])!=list or arg['ani_e_pos']==[]:
        return False
    pos_usadas,x_max,y_max = [],obter_pos_x(arg['dim']),obter_pos_y(arg['dim'])
    for pos in arg['roc']:
        if not eh_posicao(pos):
            return False
        x,y = obter_pos_x(pos),obter_pos_y(pos)
        if not 0<x<x_max or not 0<y<y_max:
            return False #Se não estiver dentro dos limites do prado
        for us in pos_usadas:
            if posicoes_iguais(pos,us):
                return False #Se a posição se repetir
        pos_usadas+=[pos]
    for par in arg['ani_e_pos']:
        if type(par)!=list or len(par)!=2 or not eh_posicao(par[1]) or not eh_animal(par[0]):
            return False
        x, y = obter_pos_x(par[1]), obter_pos_y(par[1])
        if not 0<x<x_max or not 0<y<y_max:
            return False #Se não estiver dentro dos limites do prado
        for us in pos_usadas:
            if posicoes_iguais(us,par[1]):
                return False #Se a posição se repetir
        pos_usadas+=[par[1]]
    return True

def eh_posicao_animal(m,p):
    """
    eh_posicao_animal: prado x posicao -> booleano
    Recebe um prado e uma posicao e devolve True se aquela posicao estiver ocupada por um animal, False, caso contrário
    """
    for par in m['ani_e_pos']:
        if posicoes_iguais(par[1],p):
            return True
    return False

def eh_posicao_obstaculo(m,p):
    """
    eh_posicao_obstaculo: prado x posicao -> booleano
    Recebe um prado e uma posição e devolve True e aquela posição estiver ocupada por um rochedo ou por uma montanha,
    False caso contrário
    """
    if obter_pos_y(m['dim'])==obter_pos_y(p) or obter_pos_x(m['dim'])==obter_pos_x(p) or 0==obter_pos_y(p) or \
            0 == obter_pos_x(p):
        return True #Se estiver nos limites do prado, ou seja, se for uma montanha
    for pos in m['roc']:
        if posicoes_iguais(pos,p):
            return True
    return False

def eh_posicao_livre(m,p):
    """
    eh_posicao_livre: prado x posicao -> booleano
    Recebe um prado e uma posicao e devolve True se aquela posicao estiver livre, False, caso contrário
    """
    return (not eh_posicao_animal(m,p) and not eh_posicao_obstaculo(m,p))

#TESTES
def prados_iguais(p1,p2):
    """
    prados_iguais: prado x prado -> booleano
    Recebe dois prados e devolve True se forem iguais, devolvendo False caso contrário
    """
    if not posicoes_iguais(p1['dim'],p2['dim']) or len(p1['roc'])!=len(p2['roc']) or \
            len(p1['ani_e_pos'])!=len(p2['ani_e_pos']):
        return False
    for pos1 in p1['roc']:
        iguais = False
        for pos2 in p2['roc']:
            if posicoes_iguais(pos1,pos2):
                iguais = True
        if not iguais:
            return False
    for par1 in p1['ani_e_pos']:
        iguais = False
        for par2 in p2['ani_e_pos']:
            if animais_iguais(par1[0],par2[0]) and posicoes_iguais(par1[1],par2[1]):
                iguais = True
        if not iguais:
            return False #Se não encontrar um par igual ao par1 no prado 2
    return True

#TRANSFORMADOR
def prado_para_str(m):
    """
    prado_para_str: prado -> str
    Recebe um prado e devolve uma cadeia de caraceteres que o representa
    """
    s,y_max = '', obter_tamanho_y(m)
    for y in range(y_max):
        for x in range(obter_pos_x(m['dim']) + 1):
            pos = cria_posicao(x, y)
            if (y==0 and (x==0 or x==obter_pos_x(m['dim']))) or (y==obter_pos_y(m['dim']) and (x==0 or \
                    x==obter_pos_x(m['dim']))):
                s+='+'
            elif y==0 or y==obter_pos_y(m['dim']):
                s+='-'
            elif x==0 or x==obter_pos_x(m['dim']):
                s+='|'
            elif eh_posicao_animal(m,pos):
                s+=animal_para_char(obter_animal(m,pos))
            elif eh_posicao_obstaculo(m,pos):
                s+='@'
            else:
                s+='.'
        if y!=y_max-1:
            s+='\n' #Adiciona o caráter \n excepto à última linha
    return s

#FUNÇÕES DE ALTO NÍVEL
def obter_valor_numerico(m,p):
    """
    obter_valor_numerico: prado x posicao -> int
    Recebe um prado e uma posicao e devolve o valor numérico da posição p na ordem de leitura do prado m
    """
    return obter_tamanho_x(m)*obter_pos_y(p)+obter_pos_x(p) #Faz a conta do número de linhas até à linha y
                                                            # pelo número de colunas mais as colunas até à coluna x

def obter_movimento(m,p):
    """
    obter_movimento: prado x posicao -> posicao
    Recbe um prado e uma posição e devolve a posição nova do animal dentro do prado m, seguindo as regras de movimento
    """
    pos_disp, pos_livres, pos_presas = obter_posicoes_adjacentes(p),(),()
    if eh_predador(obter_animal(m,p)):
        for pos in pos_disp:
            if eh_posicao_animal(m,pos) and eh_presa(obter_animal(m,pos)):
                pos_presas += (pos,)
            if eh_posicao_livre(m,pos):
                pos_livres+=(pos,)
        if len(pos_presas)!=0: #Se houver posições com presas, o predador opta por estas
            return pos_presas[obter_valor_numerico(m,p)%len(pos_presas)]
    else:
        for pos in pos_disp:
            if eh_posicao_livre(m,pos):
                pos_livres+=(pos,)
    if len(pos_livres)==0:
        return p #Se não houver nenhuma posição livre, o animal não se move
    return pos_livres[obter_valor_numerico(m,p)%len(pos_livres)]

#                                                       FUNÇÕES ADICIONAIS
def geracao(m):
    """
    geracao: prado -> prado
    Recebe um prado e devolve o mesmo prado com as alterações feitas correspondentes à passagem de uma geração
    """
    animais_movidos, posicoes = [], obter_posicao_animais(m)
    for pos in posicoes:
        nao_movido = True
        for pos1 in animais_movidos:
            if posicoes_iguais(pos, pos1):
                nao_movido = False #Verifica se o animal já foi movido (i.e. um predador que ocupa a casa de uma presa)
        if nao_movido:
            animal, pos_nova = obter_animal(m, pos), obter_movimento(m, pos)
            aumenta_idade(animal)
            aumenta_fome(animal)
            if not posicoes_iguais(pos_nova, pos): #Só se move se a posição nova for diferente da atual
                if eh_predador(animal) and eh_presa(obter_animal(m, pos_nova)):
                    eliminar_animal(m, pos_nova)
                    reset_fome(animal)
                mover_animal(m, pos, pos_nova)
                animais_movidos += [pos_nova]
                if eh_animal_fertil(animal):
                    novo_animal = reproduz_animal(animal)
                    inserir_animal(m, novo_animal, pos)
                if eh_animal_faminto(animal):
                    eliminar_animal(m, pos_nova)
            elif eh_animal_faminto(animal): #Mesmo que não se mova, pode morrer à fome
                eliminar_animal(m, pos)
    return m

def simula_ecossistema(f,g,v):
    """
    simula_ecossistema: str x int x booleano -> tuplo
    Recebe uma cadeia de caracteres, f, um número inteiro, g, e um booleano, v, e devolve um tuplo com dois elementos:
    o número de predadores e o número de persas no prado, após a simulação. f corresponde ao nome do ficheiro que
    contém a configuração do prado a simular. g corresponde ao número de gerações a simular. v ativa o modo verboso se
    for True ou o modo quiet se Falso
    """
    fich = open(f,'r')
    linhas = fich.readlines()
    for i in range(len(linhas)):
        linhas[i] = eval(linhas[i]) #Substitui as linhas pelo eval de si mesmas (cria tuplos)
    dim, roc, a, p = cria_posicao(linhas[0][0],linhas[0][1]), tuple([cria_posicao(x,y) for x,y in linhas[1]]), (),()
    #dim corresponde à posição formada pelos dois valores do primeiro tuplo, linhas[0]
    #roc corresponde ao tuplo com todas as posições da segunda linha do ficheiro
    for linha in linhas[2:]:
        a+=(cria_animal(linha[0],linha[1],linha[2]),) #Cria um animal com as características de acordo com o ficheiro
        p+=(cria_posicao(linha[-1][0],linha[-1][1]),) #Cria uma posição pertencente ao animal
    prado = cria_prado(dim,roc,a,p)
    if v:
        return simula_ecossistema_verboso(prado,g)
    else:
        return simula_ecossistema_quiet(prado,g)

def simula_ecossistema_quiet(m,g):
    """
    simula_ecossistema_quiet: prado x int -> tuplo
    Recebe um prado e um número inteiro, o número de gerações a simular e devolve um tuplo com o número de predadores e
    de presas no prado após a simulação. Neste modo, mostra-se pela saída standard o prado, o número de presas e
    predadores e o número da geração no início e no fim da simulação
    """
    print('Predadores:',obter_numero_predadores(m),'vs Presas:',obter_numero_presas(m),'(Gen. 0)')
    print(prado_para_str(m),end='\n')
    for i in range(g):
        geracao(m)
    print('Predadores:', obter_numero_predadores(m), 'vs Presas:', obter_numero_presas(m), '(Gen. '+str(g)+')')
    print(prado_para_str(m))
    return (obter_numero_predadores(m), obter_numero_presas(m))

def simula_ecossistema_verboso(m,g):
    """
    simula_ecossistema_verboso: prado x int -> tuplo
    Recebe um prado e um número inteiro, o número de gerações a simular e devolve um tuplo com o número de predadores e
    de presas no prado após a simulação. Neste modo, após cada geração mostra-se o prado, o número de animais e a
    geração se o número de presas ou predadores se tenha alterado
    """
    print('Predadores:', obter_numero_predadores(m), 'vs Presas:', obter_numero_presas(m), '(Gen. 0)')
    print(prado_para_str(m),end='\n')
    for i in range(1,g+1):
        pred, pres = obter_numero_predadores(m), obter_numero_presas(m)
        geracao(m)
        if obter_numero_predadores(m)!=pred or obter_numero_presas(m)!=pres: #Caso o número de animais se altere
            print('Predadores:', obter_numero_predadores(m), 'vs Presas:', obter_numero_presas(m), '(Gen. '+str(i)+')')
            print(prado_para_str(m),end='\n')
    return (obter_numero_predadores(m),obter_numero_presas(m))