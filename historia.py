def Finald(i):
    pf=[
        f"Fora de lá, você anda e encontra uma outra propaganda. Nela, está sendo dito sobre a criação da Crispr-CAS9. Você lê a matéria e percebe algo aterrador... ",
        "Ao lado da matéria, há uma propaganda, com uma foto do Mazelinha falando 'Que mazela!' ",
        "Em um muro ao lado, está escrito 'Riders on the storm... Into this house we're born... Like a dog without a bone, and an actor out of loan...' ",
        "Ao longo do céu escuro e poluído, com prédios cinzentos e águas poluídas do que parece ser São Paulo... Você visualiza algo ainda mais estranho",
        f" Você decide olhar",
        f"e pega a Espingarda Remington.",
        "O que aparece na sua frente, parece ser um cachorro contaminado com raiva... Ele saliva abertamente, com uma fúria doentil e repleta de baba, condição típica da doença",
        f"Ele pula em você e quase te morde... Em seguida recua e arranha seu braço. Você sente uma dor intensa e uma febre alta ",
        "Você, apesar de se sentir mal, acaba tendo de atirar no cachorro e ele morre. Você sente uma febre alta e uma dor intensa no braço. Você tenta se acalmar, mas a febre só aumenta.",
        "Obrigado por jogar meu jogo, fim da demo. Até a próxima!",
    ]
    return pf[i]

def ficar(i):
    p2=["No final da música, o portão se fecha."
    "Em seguida, um mutante pula em você enquanto termina de tocar. ",
    "Você morre. Game Over."]
    return p2[i]


def e2(i):
    p3=["Você pega o violão",
        "E começa a tocar a única música que sabe, e a que mais dói... Porque te faz lembrar de alguém: Riders on The Storm, de The Doors. No segundo refrão, você ouve um barulho gigantesco, como algo se movendo, enquanto os ruídos do duto parecem se aproximar. Você guarda o violão assim que ouve os barulhos."]
    return p3[i]

def atencao(i):
    p4=["Você observa atentamente. E do nada se lembra de seu nome...Richard. Em 2078, os primeiros processos de melhoria genética, via Crispr-CAS19, inicialmente processos supercaros, são iniciados. Humanos superiores em velocidade, força e inteligência são montados a dedo. Mas as falhas de sequenciamento da Crispr ou mesmo falhas genéticas são segregadas as escondidas. Os seres deformados passaram a ser chamados de mutantes",
    "Com o tempo, um imenso preconceito entre humanos melhorados [chamados de Prometeus], humanos comuns e mutantes se inicia. A princípio, os Prometeus não aceitam os comuns, por considerarem-se os 'legítimos humanos' que devem ocupar a Terra, e mutantes, por considerarem-os ainda mais inferiores que os comuns",
    "Assim, o preconceito se encaixou também dos comuns aos mutantes e dos murantes contra todos. E disto, iniciou se a guerra. Uma guerra que praticamente devastou toda a população humana (Prometeu ou não). No final, os mutantes assumiram o controle, liderados por Jrisk, a primeira anomalia genética, e consequentemente o primeiro mutante.",
    "Depois, você sai com a moto. No caminho a moto descarrega, mas antes dela morrer, você acha um galpão.",
    "Você para no galpão, aparentemente da resistência humana, e pega o farol, que ainda tem energia independente da moto, e usa pra iluminar o local. Depois, se deita no chão com a espingarda"]
    return p4[i]
            
def roubar():
    "Você redireciona a energia da TV para a moto e vai embora",
    "Você encontra um galpão, aparentemente militar, e decide parar, para dormir",
    "Você estaciona a moto dentro do galpão. Também descobre uma lanterna dentro da jaqueta."

def sf(i):
    p5=[
        "A última coisa que você vê, é um clarão cegante e puramente branco. Por alguns minutos, se torna a única coisa que você vê.",
        "Você sai em um beco escuro, marrom, com 3 janelas no lado direito e duas no esquerdo. No meio há apenas uma lixeira... Lá, você encontra uma muda de roupas e pega as roupas. Uma camisa branca e um jeans azul, com uma boina azul.",
        "Você pega as roupas que encontrou e sai do beco para outro lugar...",
        f"Lá fora, você lê a previsão do tempo em um outdoor: 28 de novembro de ",
        "..."]
    return p5[i]

class historia:
   def Finald(self):
        self.pf=[
            f"Fora de lá, você anda e encontra uma outra propaganda. Nela, está sendo dito sobre a criação da Crispr-CAS9. Você lê a matéria e percebe algo aterrador... ",
            "Ao lado da matéria, há uma propaganda, com uma foto do Mazelinha falando 'Que mazela!' ",
            "Em um muro ao lado, está escrito 'Riders on the storm... Into this house we're born... Like a dog without a bone, and an actor out of loan...' ",
            "Ao longo do céu escuro e poluído, com prédios cinzentos e águas poluídas do que parece ser São Paulo... Você visualiza algo ainda mais estranho",
            f" Você decide olhar",
            f"e pega a Espingarda Remington.",
            "O que aparece na sua frente, parece ser um cachorro contaminado com raiva... Ele saliva abertamente, com uma fúria doentil e repleta de baba, condição típica da doença",
            f"Ele pula em você e quase te morde... Em seguida recua e arranha seu braço. Você sente uma dor intensa e uma febre alta ",
            "Você, apesar de se sentir mal, acaba tendo de atirar no cachorro e ele morre. Você sente uma febre alta e uma dor intensa no braço. Você tenta se acalmar, mas a febre só aumenta.",
            "Obrigado por jogar meu jogo, fim da demo. Até a próxima!",
            ]
        return self.pf
   
   def ficar(self):
        self.p2=["No final da música, o portão se fecha."
            "Em seguida, um mutante pula em você enquanto termina de tocar. ",
            "Você morre. Game Over."]
        return self.p2
   
   def atencao(self):
        self.p4=["Você observa atentamente. E do nada se lembra de seu nome...Richard. Em 2078, os primeiros processos de melhoria genética, via Crispr-CAS19, inicialmente processos supercaros, são iniciados. Humanos superiores em velocidade, força e inteligência são montados a dedo. Mas as falhas de sequenciamento da Crispr ou mesmo falhas genéticas são segregadas as escondidas. Os seres deformados passaram a ser chamados de mutantes",
            "Com o tempo, um imenso preconceito entre humanos melhorados [chamados de Prometeus], humanos comuns e mutantes se inicia. A princípio, os Prometeus não aceitam os comuns, por considerarem-se os 'legítimos humanos' que devem ocupar a Terra, e mutantes, por considerarem-os ainda mais inferiores que os comuns",
            "Assim, o preconceito se encaixou também dos comuns aos mutantes e dos murantes contra todos. E disto, iniciou se a guerra. Uma guerra que praticamente devastou toda a população humana (Prometeu ou não). No final, os mutantes assumiram o controle, liderados por Jrisk, a primeira anomalia genética, e consequentemente o primeiro mutante.",
            "Depois, você sai com a moto. No caminho a moto descarrega, mas antes dela morrer, você acha um galpão.",
            "Você para no galpão, aparentemente da resistência humana, e pega o farol, que ainda tem energia independente da moto, e usa pra iluminar o local. Depois, se deita no chão com a espingarda"]
        return self.p4 
   
   def sf(self):
         self.p5=[
            "A última coisa que você vê, é um clarão cegante e puramente branco. Por alguns minutos, se torna a única coisa que você vê.",
            "Você sai em um beco escuro, marrom, com 3 janelas no lado direito e duas no esquerdo. No meio há apenas uma lixeira... Lá, você encontra uma muda de roupas e pega as roupas. Uma camisa branca e um jeans azul, com uma boina azul.",
            "Você pega as roupas que encontrou e sai do beco para outro lugar...",
            f"Lá fora, você lê a previsão do tempo em um outdoor: 28 de novembro de ",
            "..."]
         return self.p5

   def roubar(self):
        self.roubo=[
            "Você redireciona a energia da TV para a moto e vai embora",
            "Você encontra um galpão, aparentemente militar, e decide parar, para dormir",
            "Você estaciona a moto dentro do galpão. Também descobre uma lanterna dentro da jaqueta."]
        return self.roubo
   
   def showit(self,x):
        for i in range(len(x)): 
           return self.expose(x,i)

   def expose(self,x,i):
        return x[i]