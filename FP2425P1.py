# This is the Python script for your project

def eh_tabuleiro(tabuleiro): 
    """
    Ver se é tabuleiro (tuplo constituído por m tuplos, cada um com n valores) m x n

    Arg:
        tabuleiro (tuple): recebe um tuplo constituído por m tuplos, cada um com n valores

    Return:
        booleano (bolean): True se for tabuleiro e False se não for
        
    """

    if isinstance(tabuleiro, tuple) and 2 <= len(tabuleiro) <= 100: #verificar se o tabuleiro é tuplo e se o tamanho (das linhas) está entre 2 e 100
        for m in tabuleiro:
            if isinstance(m, tuple) and 2 <= len(m) <= 100 and len(m) == len(tabuleiro[0]): #verificar se é constituído por tuplos, se o tamanho está entre 2 e 100 e se o tamanho dos tuplos é igual ao tamanho do primeiro (negação para ser mais fácil fazer o check)
                for n in m:
                    if type(n) != int or n not in (1, -1, 0): #verificar se os tuplos são constituídos por inteiros
                        return False
            else:
                return False
        return True
    return False

def eh_posicao(arg):
    """
    Ver se é posição (inteiro entre 0 e 10000)

    Arg:
        arg (int): recebe um inteiro

    Return:
        booleano (bolean): True se for posição e False se não for posição
        
    """
    if type(arg) == int and 0 < arg <= 10000: #ver se o argumento é inteiro e está entre 0 e 10000 (100x100)
        return True
    return False

def obtem_dimensao(tab): 
    """
    Obtem um tuplo com o valor das linhas (m) e colunas (n)

    Arg:
        tab (tuple): recebe um tabuleiro

    Return:
        tuplo (tuple): devolve um tuplo com o valor das linhas e colunas
        
    """
    return (len(tab), len(tab[0])) #tamanho do tabuleiro corresponde às linhas e o tamanho do primeiro tuplo do tabuleiro (m) corresponde às colunas

def obtem_valor(tab, pos):  
    """
    Obtem o valor correspondente à posição do tabuleiro

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        valor (int): devolve um inteiro com o valor correspondente à posição do tabuleiro
        
    """
    l = ((pos-1) // len(tab[0])) #linha
    c = ((pos-1) % len(tab[0])) #coluna
    return tab[l][c]   

def obtem_coluna(tab, pos): 
    """
    Obtem um tuplo, ordenado do menor ao maior número, com as posições que formam a coluna em que está contida a posição

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        r (tuple): devolve um tuplo, ordenado do menor ao maior número, com as posições que formam a coluna em que está contida a posição
        
    """
    r = ()
    i = 0
    for m in tab:
        while eh_posicao(pos - len(m)): #obter o valor da posição inicial da coluna (subtrair até ser posição) para ordenar o tuplo
            pos -= len(m)
        else:
           r += (pos + len(m)*i,) #adicionar os valores pela ordem certa
           i += 1
    return r

def obtem_linha(tab, pos): 
    """
    Obtem um tuplo, ordenado do menor ao maior número, com as posições que formam a linha em que está contida a posição

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        r (tuple): devolve um tuplo, ordenado do menor ao maior número, com as posições que formam a linha em que está contida a posição
        
    """
    l = ((pos-1) // len(tab[0])) #valor da linha
    r = ()
    i = 1
    for m in tab:
        for n in m:
            r += (len(m)*l + i,) #somar cada posição pela ordem certa
            i += 1
        return r
    
def obtem_diagonais(tab, pos): 
    """
    Obtem um tuplo formado por dois tuplos (ordenados do menor ao maior número), um com as posições diagonais e outro com as posições antidiagonais em que está contida a posição

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        tuplo (tuple): devolve um tuplo formado por dois tuplos (ordenados do menor ao maior número), um com as posições diagonais e outro com as posições antidiagonais em que está contida a posição
        
    """
    d, a = (), () #diagonais e antidiagonais
    pos_d, pos_a = pos, pos #posição diagonais e posição antidiagonais
    n = len(tab[0])
    m = len(tab)

    while (pos_a + n - 1) <= (n*m) and (pos_a - 1)%n != 0: #coluna da direita, menor q a ultima posiçlao
        pos_a = pos_a + n - 1
    while eh_posicao(pos_d - n - 1) and (pos_d - 1)%n != 0: #coluna da esquerda, posição
        pos_d = pos_d - n - 1
    
    while eh_posicao(pos_a):
        if pos_a % n == 0: #coluna direita
            a += (pos_a,)
            break
        else:
            a += (pos_a,)
            pos_a = pos_a - n + 1

    while 0 < (pos_d) <= (n*m):
        if pos_d % n == 0: #coluna esquerda
            d += (pos_d,)
            break
        else:
            d += (pos_d,)
            pos_d = pos_d + n + 1
    return (d, a)

def tabuleiro_para_str(tab): 
    """
    Obtem uma string que correspondente ao tabuleiro

    Arg:
        tab (tuple): recebe um tabuleiro

    Return:
        r (str): devolve a cadeia de caracteres correspondente ao tabuleiro
        
    """
    r = ""
    for i, m in enumerate(tab):
        for pos, n in enumerate(m):
            if n == 1:
                r += "X"
            elif n == -1:
                r += "O"
            else:
                r += "+"
            if pos < len(m) - 1: #separadores entre colunas
                r += "---"
        if i < len(tab) - 1: #separadores entre linhas
            r += "\n|"+ ("   |"*(len(m) - 2)) + "   |\n"
    return r

def eh_posicao_valida(tab, pos):
    """
    Ver se é posição do tabuleiro

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        booleano (bolean): True se for posição e False se não for
        
    """
    if eh_posicao(pos) and eh_tabuleiro(tab):
        if pos <= len(tab[0])*len(tab): #limitar as posições à posição máxima
            return True
        return False
    raise ValueError("eh_posicao_valida: argumentos invalidos")

def eh_posicao_livre(tab, pos): 
    """
    Ver se é posição livre do tabuleiro (com valor 0)

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        booleano (bolean): True se for posição livre e False se não for
        
    """
    if eh_posicao(pos) and eh_tabuleiro(tab):
        if eh_posicao_valida(tab, pos):
            if obtem_valor(tab, pos) == 0:
                return True
            return False
        raise ValueError("eh_posicao_livre: argumentos invalidos")
    raise ValueError("eh_posicao_livre: argumentos invalidos")

def obtem_posicoes_livres(tab): 
    """
    Obtem um tuplo (ordenado do menor ao maior número) com todas as posições livres no tabuleiro (valor 0)

    Arg:
        tab (tuple): recebe um tabuleiro

    Return:
        r (tuple): devolve um tuplo (ordenado do menor ao maior número) com todas as posições livres no tabuleiro (valor 0) 
        
    """
    if eh_tabuleiro(tab):
        r = ()
        c = 0
        for m in tab:
            for pos, n in enumerate(m): #índice e valor
                if n == 0:
                    r += (pos + 1 + len(m)*c,) #+1 ao índice para obter a posição
            c += 1
        return r    
    raise ValueError("obtem_posicoes_livres: argumento invalido")

def obtem_posicoes_jogador(tab, jog): 
    """
    Obtem um tuplo (ordenado do menor ao maior número) com todas as posições ocupadas pelo jogador

    Arg:
        tab (tuple): recebe um tabuleiro
        jog (int): recebe um inteiro que respresenta o jogador (1 para X e -1 para O)

    Return:
        r (tuple): devolve um tuplo (ordenado do menor ao maior número) com todas as posições ocupadas pelo jogador 
        
    """
    if eh_tabuleiro(tab) and type(jog) == int and (jog == 1 or jog == -1): 
        r = ()
        c = 0
        for m in tab:
            for pos, n in enumerate(m): #indíce e valor
                if n == jog:
                    r += (pos + 1 + len(m)*c,) #+1 ao índice para obter a posição
            c += 1
        return r    
    raise ValueError("obtem_posicoes_jogador: argumentos invalidos")

def obtem_posicoes_adjacentes(tab, pos): 
    """
    Obtem um tuplo (ordenado do menor ao maior número) com todas as posições adjacentes à posição recebida

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        r (tuple): devolve um tuplo (ordenado do menor ao maior número) com todas as posições adjacentes à posição recebida 
        
    """
    if eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos):
        r = () #resultado
        d = obtem_diagonais(tab, pos)[0] #tuplo das diagonais
        a = obtem_diagonais(tab, pos)[1] #tuplo das anti-diagonais
        p = (obtem_coluna(tab, pos), obtem_linha(tab, pos), d, a) #posições associadas
        for t in p: #por cada tuplo
            for i, n in enumerate(t): #por cada valor
                if n == pos:
                    if i - 1 >= 0:
                        r += (t[i - 1],)
                    if i + 1 < len(t):
                        r += (t[i + 1],)
        return tuple(sorted(r)) #ordenar o tuplo
    raise ValueError("obtem_posicoes_adjacentes: argumentos invalidos")

def distância_vertical(tab, pos): #auxiliar
    """
    Obtem o valor das coordenadas y da posição recebida

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        l (int): devolve o valor da linha correspondente à posição recebida 
        
    """
    l = ((pos-1) // len(tab[0])) + 1
    return l

def distância_horizontal(tab, pos): #auxiliar
    """
    Obtem o valor das coordenadas x da posição recebida

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        c (int): devolve o valor da coluna correspondente à posição recebida 
        
    """
    c = ((pos-1) % len(tab[0])) + 1
    return c

def distancia(tab, pos1, pos2): #auxiliar
    """
    Obtem o valor da distância entre duas posições recebidas

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição

    Return:
        d (int): devolve o valor da distância entre duas posições recebidas 
        
    """
    d = max(abs(distância_horizontal(tab, pos1) - distância_horizontal(tab, pos2)), abs(distância_vertical(tab, pos1) - distância_vertical(tab, pos2))) #fórmula de chebyshev
    return d

def ordena_posicoes_tabuleiro(tab, tup):
    """
    Obtem um tuplo com as posições em ordem ascendente de distância à posição central do tabuleiro (posições com a mesma distância são ordenadas do menor ao maior número)

    Arg:
        tab (tuple): recebe um tabuleiro
        tup (tuple): recebe um tuplo de posições do tabuleiro

    Return:
        r (tuple): devolve um tuplo com as posições em ordem ascendente de distância à posição central do tabuleiro 
        
    """
    if eh_tabuleiro(tab) and type(tup) == tuple:
        if all(isinstance(i, int) and eh_posicao_valida(tab,i) for i in tup):
            if tup:
                m = len(tab) #linhas
                n = len(tab[0]) #colunas
                c = (m // 2)*n + n//2 + 1 #centro do tabuleiro (fórmula do enunciado)
                if c in tup:
                    r = (c,)
                else:
                    r = ()
                d_max = distancia(tab, tab[0][0], c) #distância máxima
                for j in range(1, d_max + 1):
                    for i in tup:
                        d = distancia(tab, i, c) #distância entre os valores do tuplo recebido e o centro
                        if d == j: #adiciona ao tuplo em função da distância
                            r += (i,)           
                return r
            else:
                return ()
        raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")
    raise ValueError("ordena_posicoes_tabuleiro: argumentos invalidos")

def marca_posicao(tab, pos, jog):
    """
    Obtem um novo tabuleiro com uma nova pedra correspondente ao do jogador recebido

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição livre
        jog (int): recebe um inteiro que respresenta o jogador (1 para X e -1 para O)

    Return:
        r (tuple): devolve um tabuleiro com o valor da posição recebida alterada pelo valor do jogador
        
    """
    if eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos) and eh_posicao_livre(tab, pos) and type(jog) == int and (jog == 1 or jog == -1):
        l = ((pos-1) // len(tab[0])) #linha
        c = ((pos-1) % len(tab[0])) #coluna
        r, nova_l = (), () #resultado e nova linha (a que vai ser alterada)
        for i, m in enumerate(tab): #indice da coluna e valor
            if i == l:
                for j, n in enumerate(m): #indice da linha e valor
                    if j == c: #caso seja a linha e coluna da posição para alterar
                        nova_l += (jog,) 
                    else:
                        nova_l += (n,)
                r += (nova_l,)
            else:
                r += (m,)
        return r
    raise ValueError("marca_posicao: argumentos invalidos")

def consec(tab, pos, jog, direcao): #auxiliar
    """
    Obtem o número de consecutivos da posição recebida

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição livre
        jog (int): recebe um inteiro que respresenta o jogador (1 para X e -1 para O)
        direcao (tuple): recebe um tuplo com as posiçôes correspondentes a uma direção (horizontal, vertical, diagonal e antidiagonal)

    Return:
        consec (int): Devolve o número de consecutivos à posição recebida
        
    """
    consec = 0
    i_pos = (pos-1) // len(tab[0])
    for i in range(i_pos, len(direcao) + 1): #da esquerda para a direita
        if 0 <= i < len(direcao): #se i pertencer
            n = direcao[i]
            if obtem_valor(tab, n) == jog:
                consec += 1
            else: 
                break
        else: 
            break
    for i in range(i_pos - 1, -1, -1): #da direita para a esquerda
        if 0 <= i < len(direcao): #se i pertencer
            n = direcao[i]
            if obtem_valor(tab, n) == jog:
              consec += 1
            else:
                break
        else:
            break
    return consec

def verifica_k_linhas(tab, pos, jog, k):
    """
    Ver se existe uma linha que contenha k ou mais pedras consecutivas

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição livre
        jog (int): recebe um inteiro que respresenta o jogador (1 para X e -1 para O)
        k (int): recebe um inteiro positivo

    Return:
        booleano (bolean): True se exitir e False se não
        
    """
    if eh_tabuleiro(tab) and eh_posicao(pos) and eh_posicao_valida(tab, pos) and type(jog) == int and (jog == 1 or jog == -1) and type(k) == int and k > 0:
        l_pos = obtem_linha(tab, pos)
        c_pos = obtem_coluna(tab, pos)
        d_pos = obtem_diagonais(tab, pos)[0]
        a_pos = obtem_diagonais(tab, pos)[1]
        if obtem_valor(tab, pos) != jog:
            return False
        if consec(tab, pos, jog, l_pos) >= k or consec(tab, pos, jog, c_pos) >= k or consec(tab, pos, jog, d_pos) >= k or consec(tab, pos, jog, a_pos) >= k:
            return True
        return False
    raise ValueError("verifica_k_linhas: argumentos invalidos")

def jogador_k(tab, jog, k): #auxiliar
    """
    Ver se o jogador tem k em linha

    Arg:
        tab (tuple): recebe um tabuleiro
        pos (int): recebe uma posição livre
        k (int): recebe um inteiro positivo

    Return:
        booleano (bolean): True se tiver e False se não
        
    """
    pos_jog = obtem_posicoes_jogador(tab, jog)
    for pos in pos_jog:
        if verifica_k_linhas(tab, pos, jog, k) == True:
            return True
    return False

def eh_fim_jogo(tab, k):
    """
    Ver se o jogo terminou (jogador com k em linha ou sem mais posições livres)

    Arg:
        tab (tuple): recebe um tabuleiro
        k (int): recebe um inteiro positivo

    Return:
        booleano (bolean): True se terminou e False se não
        
    """
    if eh_tabuleiro(tab) and type(k) == int and k > 0:
        if (jogador_k(tab, 1, k) or jogador_k(tab, -1, k)) or obtem_posicoes_livres(tab) == (): #um dos dois casos para o jogo terminar
            return True
        return False       
    raise ValueError("eh_fim_jogo: argumentos invalidos")

def escolhe_posicao_manual(tab):
    """
    Obtem a posição selecionada pelo jogador caso seja livre    

    Arg:
        tab (tuple): recebe um tabuleiro

    Return:
        r (int): Devolve um inteiro (posição) introduzido pelo jogador se for posição livre
        
    """
    if eh_tabuleiro(tab):
        while True:
            r = input("Turno do jogador. Escolha uma posicao livre: ")
            if r.isdigit(): #se for número
                r = int(r)
                if r in obtem_posicoes_livres(tab):
                    return r
    raise ValueError("escolhe_posicao_manual: argumento invalido")

def escolhe_posicao_auto(tab, jog, k, lvl):
    """
    Obtem a posição selecionada em função da estratégia escolhida

    Arg:
        tab (tuple): recebe um tabuleiro
        jog (int): recebe um inteiro que respresenta o jogador (1 para X e -1 para O)
        k (int): recebe um inteiro positivo
        lvl (str): recebe uma cadeia de caracteres correspondente à estratégia

    Return:
        int (int): Devolve a posição selecionada
        
    """
    if eh_tabuleiro(tab) and type(jog) == int and (jog == 1 or jog == -1) and type(k) == int and k > 0 and (lvl == "facil" or lvl == "normal" or lvl == "dificil"):
        if not eh_fim_jogo(tab, k): 
            livres = obtem_posicoes_livres(tab) #livres
            ocu_jog = obtem_posicoes_jogador(tab, jog) #ocupadas pelo jog
            adj_jog = () #adjacentes às ocupadas pelo jog
            pos_val = ()
            if lvl == "facil":
                for i in ocu_jog:
                    adj_jog += obtem_posicoes_adjacentes(tab, i)
                for i in adj_jog:
                    for j in livres:
                        if i == j:
                            pos_val += (j,)
                if not pos_val: #se for vazio
                    pos_val = livres
                return ordena_posicoes_tabuleiro(tab, pos_val)[0]
            if lvl == "normal":
                jog_bot = -jog
                L = k
                m = obtem_dimensao(tab)[0] #linhas
                n = obtem_dimensao(tab)[1] #colunas
                ultimo_elemento = m*n
                while L > 0:
                    for l_jog in ordena_posicoes_tabuleiro(tab, livres): 
                        if l_jog in range(l_jog, ultimo_elemento + 1): #iterar por cada elemento até ao último do tab
                            tab_sim = marca_posicao(tab, l_jog, jog) #novo tabuleiro
                            if verifica_k_linhas(tab_sim, l_jog, jog, k): 
                                L -= 1 
                            return l_jog 
                    for l_jog_bot in ordena_posicoes_tabuleiro(tab, livres):
                        if l_jog_bot in range(l_jog_bot, ultimo_elemento + 1):
                            tab_sim = marca_posicao(tab, l_jog_bot, jog_bot)
                            if verifica_k_linhas(tab_sim, l_jog_bot, jog_bot, k):
                                L -= 1
                            return l_jog_bot
        raise ValueError(("escolhe_posicao_auto: argumentos invalidos"))
    raise ValueError("escolhe_posicao_auto: argumentos invalidos")

def jogo_mnk(cfg, jog, lvl):
    """
    Obtem a posição selecionada em função da estratégia escolhida

    Arg:
        tab (tuple): recebe um tabuleiro
        jog (int): recebe um inteiro que respresenta o jogador (1 para X e -1 para O)
        k (int): recebe um inteiro positivo
        lvl (str): recebe uma cadeia de caracteres correspondente à estratégia

    Return:
        int (int): Devolve a posição selecionada
        
    """
    if type(cfg) == tuple and len(cfg) == 3 and type(jog) == int and (jog == 1 or jog == -1) and (lvl == "facil" or lvl == "normal" or lvl == "dificil"):
        if type(cfg[2]) == int and cfg[2] > 0 and type(cfg[0]) == int and  2 <= cfg[0] <= 100 and type(cfg[1]) == int and 2 <= cfg[1] <= 100:
            m = cfg[0] #obter os valores dentro do cfg
            n = cfg[1]
            k = cfg[2]       
            tab = ()

            for i in range(1, n+1): #fazer o tabuleiro
                tab += (0,)
            tab = (tab,)*m
            tab_vis = tabuleiro_para_str(tab)
            print("Bem-vindo ao JOGO MNK.")

            if jog == 1: #peça do jogador
                jog_bot = -1
                turno_jogador = True
                print("O jogador joga com 'X'.")
            else:
                jog_bot = 1
                turno_jogador = False
                print("O jogador joga com 'O'.")
                
            while not eh_fim_jogo(tab, k): #loop do jogo
                print(tab_vis)
                if turno_jogador:
                    pos = escolhe_posicao_manual(tab)
                    tab = marca_posicao(tab, pos, jog)
                    tab_vis = tabuleiro_para_str(tab) #mudar tabuleiro
                    turno_jogador = False #mudar de jogador
                else: 
                    print(f"Turno do computador ({lvl}):")
                    pos = escolhe_posicao_auto(tab, jog_bot, k, lvl)
                    tab = marca_posicao(tab, pos, jog_bot)
                    tab_vis = tabuleiro_para_str(tab)
                    turno_jogador = True
            print(tab_vis)

            if jogador_k(tab, jog, k): #se o jogador tiver k em linha
                print("VITORIA")
                return jog
            elif jogador_k(tab, jog_bot, k): #se o bot tiver k em linha
                print("DERROTA")
                return jog_bot
            else:
                print("EMPATE")
                return 0
        raise ValueError("jogo_mnk: argumentos invalidos")
    raise ValueError("jogo_mnk: argumentos invalidos")