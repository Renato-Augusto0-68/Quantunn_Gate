
import pygame
import sys, time
import random as r
from historia import livro_decisoes
from personagem import Personagem
# --- CONFIG INICIAL ---
pygame.init()
WIDTH, HEIGHT = 900, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quantunn Gate")

# Cores e fontes
WHITE = (255, 255, 255)
BLACK = (2, 2, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 150, 255)
CYAN = (0, 255, 255)
GRAY = (100, 100, 100)
DARK_GRAY = (50, 50, 50)
FONT = pygame.font.SysFont("Arial", 20)
BIGFONT = pygame.font.SysFont("Arial", 28, True)
TITLE_FONT = pygame.font.SysFont("Arial", 72, True)
SUBTITLE_FONT = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()
FPS = 60

player = Personagem()
h=livro_decisoes()

# --- FUNÇÕES ---
def draw_text(surface, text, pos, font, color=WHITE, max_width=850):
    words = text.split(' ')
    lines = []
    line = ''
    for word in words:
        test_line = line + word + ' '
        if font.size(test_line)[0] <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word + ' '
    lines.append(line)
    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (pos[0], pos[1] + y_offset))
        y_offset += font.get_linesize()
def die():
    pygame.display.update()
    pygame.quit()
    sys.exit()

class botao:
             def __init__(self,ano):
                 self.ano=ano
             def iniciar_viagem(self):
                 return (f"Acionando viagem para o ano {self.ano}.")
class viagem(botao):
                 def __init__(self,ano):
                     super().__init__(ano)
                     self.destino=2256-self.ano
                 def saída(self):
                     return (f" 'Bem vindo à {self.destino} anos.' ")
year=r.choice([2019,2025])
jogador=botao(year)
viagem1=viagem(year)

def show_ui():
    vida_text = FONT.render(f"Vida: {player.vida}%", True, GREEN)
    itens_text = FONT.render(f"Itens: {player.mostrar_items()}", True, WHITE)
    win.blit(vida_text, (20, HEIGHT - 60))
    win.blit(itens_text, (20, HEIGHT - 30))

input_box = pygame.Rect(30, HEIGHT - 90, 300, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
def get_player_name(prompt="Digite o nome do personagem:", default="JOGADOR"):
    active = False
    text = ""
    clock = pygame.time.Clock()
    while True:
        win.fill(BLACK)
        draw_text(win, prompt, (30, 30), FONT)
        color = color_active if active else color_inactive
        pygame.draw.rect(win, color, input_box, 2)
        txt_surface = FONT.render(text if text else default, True, WHITE)
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        show_ui()
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    return text.strip() if text.strip() != "" else default
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    if event.unicode.isprintable():
                        text += event.unicode

def investigar():
            show_text_block("Você entra no portão. Lá dentro, há uma moto cinza voadora fracamente iluminada por lâmpadas florescentes fracas, similar à uma Harley Davidson e uma espingarda Remington.")
            player.guardar_items("Espingarda Remington")
            show_text_block("Na parede cinza, repleta de posteres de projetos técnicos de dispostivos voadores, manchados de sangue, há um armário de munição para a espingada e uma jaqueta de couro marrom.")
            player.guardar_items("Munição")
            show_text_block("Você examina o armário. Do armário aparece um mutante cinza, constituído de tentáculos. Ele pula na sua direção tentando te atacar.")
            show_text_block(f" Ele pula em você e morde seu ombro,")
            player.dano(2)               
            show_text_block(f"mas você consegue desviar, pegar a {player.mostrar_items('Espingarda Remington')}, carregar e ")
            show_text_block("atirar. Você acerta na cabeça do mutante, abatendo o ser na hora. Ao olhar o cadáver do ser, você percebe uma camada subcutânea espessa de queratina, que age como colete improvisado")
            time.sleep(2)
            show_text_block(f"A moto possui um painel digital que mostra a energia restante, além da velocidade. Você sobe na moto e arromba uma porta de metal com a moto e sai voando. No caminho, você sente dor no ombro mordido pelo mutante.")
            player.recuperar(1)
            show_text_block("E, ao longo da longa estrada escura, de asfalto malfadado que você roda, o vento frio sopra e te deixa com frio")
            time.sleep(2)

def scene(text, options):
    selected = 0
    while True:
        win.fill(BLACK)
        draw_text(win, text, (20, 20), FONT)

        for i, option in enumerate(options):
            color = GREEN if i == selected else WHITE
            option_text = FONT.render(f"> {option['text']}", True, color)
            
            win.blit(option_text, (40, 300 + i * 30))

        show_ui()
        pygame.display.update()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    return options[selected]['action']

def show_text_block(text, delay=7700):
    win.fill(BLACK)

    draw_text(win, text, (30, 30), FONT)
    show_ui()
    pygame.display.update()
    pygame.time.delay(delay)

def events():
     events2=["Você vê um rosto marcado... Cicatrizes, peças expostas de matal, marcas de cirurgias, manchas de sangue e sérias deformações faciais e olheiras profundas... e um rosto que não parece humano, e nem totalmente desumano... Jrisk te encara, LUA PÁLIDA SORRI ABERTAMENTE... Não há caminhos: A LUA PÁLIDA SORRI ABERTAMENTE. O chão é macio. LUA PÁLIDA SORRI ABERTAMENTE. Jrisk, na forma da lua sorri abertamente para você...",
            "Você vê o que parece ser um carro e um prédio. O prédio derrete feito manteiga metálica na sua frente. A mesma coisa, o carro, e você sente um intenso e quase cegante brilho branco.... Ao longe, uma terrível conclusão sobre o final da batalha entre Prometeus, mutantes e humanos, paira no ar..."]
     return events2[r.randrange(len(events2))]

#   INÍCIO DO JOGO
from memorias import memories
from historia import livro_decisoes,Finald,ficar,sf,atencao,roubar,p2_4,créditos

intro1 = ("Quantunn Gate",
          "\n                                         Versão 1.35.2",
          "\n\n\n\n\n\n\n\n\n\n\n Bem vindo, ao futuro da raça humana"   
    )

escolha1=scene(f"{intro1}",[
  {"text":"Jogar","action":"iniciar"},    
  {"text":"Créditos","action":"créditos"}   
])

if escolha1=="créditos":
    for i in range(3):
        show_text_block(créditos(i))

if escolha1=="iniciar":
    show_text_block("Carregando...")
    time.sleep(5)
    show_text_block("\n\n\n\n                  A menor distancia entre dois pontos curvos é uma reta geodésica.\nEuclides")
    time.sleep(6)
    intro = (
        f"Você acorda em um quarto escuro, com lâmpadas flourescentes azuis. Seu medidor biológico futurista mostra {player.vida}% de vida. ",
        f"Você se lembra um pouco, daquele lugar e de como você acabou indo parar aí... Você estava vagando sozinho e... Não consegue se lembrar mais do porque estar nesse lugar.",
        "Mas, sente um tipo de incômodo... Cheiro de comida velha...",
        "Há um sistema de dutos de ventilação fazendo um barulho esquisito. Você não tem armas, ou celular. Muito menos um relógio. Há um violão na parede "
        "e dois caminhos: esquerda e direita.")

    escolha = scene(f"{intro}", [
        {"text": "Ir para esquerda", "action": "esquerda"},
        {"text": "Ir para direita", "action": "direita"}])

    if escolha == "direita":
        show_text_block("Você anda no caminho escuro, feito de metal. Você continua andando, e sem ver, cai no buraco. Você morre")
        die()

    elif escolha == "esquerda":
        escolha2 = scene(
        "Você encontra um portão de metal gigante. Não dá pra derrubar. Você volta e decide se vai pegar o violão ou tentar entrar, na marra...",
        [   {"text": "Pegar o violão", "action": "violao"},
            {"text": "Tentar arrombar a porta", "action": "arrombar"}])
    if escolha2 == "violao":
        for i in range(2):
            show_text_block(p2_4(i))        
        player.guardar_items("violão")
    
    else:
        show_text_block(f" Você corre, bate o ombro, e fica com menos vida (segundo o medidor biológico) e desloca o osso. Você urra de dor, e volta até a sala inicial com imensa dor.")
        player.dano()
        show_text_block("Mas, teimoso, continua onde começou, e tenta pega o violão. Mas não consegue pela dor... O portão continua fechado, e então o duto desaba.")
        time.sleep(2)
        show_text_block("Em você, pula um mutante cinza, repleto de tentáculos, pele deformada e um rosto sem olhos ou nariz. Ele te mata ")
        player.dano(3)
        die()
    
    escolha3 = scene("Você vai ficar onde está ou investigar o barulho?", [
    {"text": "Ficar", "action": "ficar"},
    {"text": "Investigar", "action": "investigar"}
    ])
    if escolha3=="ficar":
        for i in range(3):
            show_text_block(ficar(i))
        player.dano(5)
        die()
    elif escolha3 == "investigar":
            investigar()
            show_text_block(f"{player.show()}")            
            escolha4=scene(f"Está de noite, e no lado de fora, você lê: 'Prisão Blacksail, Since 2223. No caminho, você passa por uma televisão antiga. Nela, passam recortes de jornais e de documentários. A moto possui 56% de energia. Bastante, mas não suficiente para um trajeto maior que 60 Km. Então, decide se vai prestar atenção ou se vai roubar a energia para a moto.",[
                {"text": "Prestar atenção", "action": "atencao"},
                {"text": "Roubar energia", "action": "roubar"}
            ])
            if escolha4 == "atencao":
                player.recuperar()
                for i in range(4):
                    show_text_block(atencao(i))
                time.sleep(2)                    
            else:
                for i in range(3):
                    show_text_block(roubar(i))
                player.guardar_items("Lanterna")
                show_text_block(f"Você a usa para iluminar o local e dorme com a {player.mostrar_items('Espingarda Remington')}, no chão.")
                show_text_block("E, antes de dormir você se lembra de outras coisas que ocorreram no passado: ")
                show_text_block("Em 2078, surgiu o Crispr-CAS19. Um sistema de melhoria genética... Mas, por causa do preço, poucos tinham muito e o oposto também. Logo, disto iniciou-se uma guerra..."),
                time.delay(20)
                show_text_block("E com a guerra, veio a ascensão daqueles que vieram de falhas da tecnologia genética... Mutantes... E seu líder diabólico, Jrisk... ")
    player.recuperar()
    pygame.display.set_caption("Quantunn Gate - Capítulo 2")

    intro2 = (
    "Capítulo 2")

    show_text_block(f"{events()}")
    show_text_block("De dia, você acorda. Os posteres presos na parede do galpão ilustram aparentes planos militares, e você quer simplesmente resolver tudo.De preferência sair dalí, ao menos."),
    show_text_block("Você decide se vai analisar os planos na parede, ou não")  

    escolha5=scene("O que você faz?",[
        {"text": "Analisar os planos", "action": "analisar"},
        {"text": "Ignorar", "action": "ignorar"}]) 

    if escolha5 == "analisar":
        show_text_block("Você analisa os planos. O galpão aparentemente foi construído em cima do plano final mutante para o extermínio humano. Eles desenvolveram uma máquina chamada 'Quantunn Gate'. Não está claro o que ela faz. Apenas que utiliza de intensos campos eletromagnéticos, em teoria, capazes de promover a separação de prótons dos núcleos atômicos")
        time.sleep(2)
        show_text_block(" De qualquer forma, você estuda a sala... Existe o que parece ser uma sala de controle. Você deduz que controlam a máquina, apesar de não saber EXATAMENTE o que ela faz...")
        show_text_block("Os botões, quando ativados, mostram datas... como 2019, 2025 e 2001...")
        time.sleep(2)
        show_text_block("Você esbarra em um botão vermelho, que ativa a máquina. Você vê uma luz intensa e branca, e sente um intenso calor, e ouve uma voz que diz: 'Escolha o ano' ")
    else:
        show_text_block("Você vai embora do galpão em direção a um destino desconhecido. Lá, você reflete sobre a vida, o passado e futuro. lá, a vida parece fazer mais sentido sendo arpoveitado no que der e vier. Então você vira um monje e vive na montanha \n Parabéns, você desbloqueou o final secreto: 'Pacíficamente viver' Fim de jogo, obrigado por ter jogado meu jogo.")
        die()

    show_text_block(jogador.iniciar_viagem())
    if year==2025 ^ year==2019:
        show_text_block(botao.viagem(year).saída)

    for i in range(5):
     show_text_block(sf(i))
     time.sleep(2)
     if sf(i)==sf(-3):
          player.guardar_items("Roupas Antigas"),
     if sf(i)==sf(-2):
          show_text_block(f"{year}")
    pygame.display.set_caption("Quantunn Gate - Capítulo 3")
    intro3 = ("Capítulo 3")

    for i in range(10):
        show_text_block(Finald(i))
        if Finald(i)==(Finald(-3) or Finald(-1)):
            time.sleep(2)
        if Finald(i)==Finald(-3):
            player.dano(2)
        if Finald(i)==(Finald(-1)):
            die()
# CONTINUA AQUI — CAPÍTULO 3...