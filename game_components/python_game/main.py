from tkinter import font
import pygame,sys,time
import random as r
import cv2
import os
from opencv_functions.process_image import detectAndDisplay; 
from pygame_functions.personagem import Personagem
from pygame_functions.process_functs import Finald, investigar, ficar,sf,atencao,roubar,p2_4,créditos,begin,len_of_function

# --- CONFIG INICIAL ---
pygame.init()
WIDTH, HEIGHT = 900, 700
win = pygame.display.set_mode((WIDTH, HEIGHT))
screen=pygame.display.set_caption("Quantunn Gate")
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

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
TITLE_FONT = pygame.font.SysFont("Arial", 24, True)
SUBTITLE_FONT = pygame.font.SysFont("Arial", 18,False,True)
clock = pygame.time.Clock()
FPS = 30
version="1.7.5"
activate=False
control=False
player = Personagem()

# Botão de pular texto
largura_botao = 110
altura_botao = 40
margem = 8 
pos_x = WIDTH - largura_botao - margem  
pos_y = (HEIGHT - altura_botao) // 1.019999
skip_text_button = pygame.Rect(pos_x, pos_y, largura_botao, altura_botao)

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
    
    if activate==True:
        vida_text = FONT.render(f"Vida: {player.vida}%", True, GREEN)
        itens_text = FONT.render(f"Itens: {player.mostrar_items()}", True, WHITE)
        win.blit(vida_text, (20, HEIGHT - 60))
        win.blit(itens_text, (20, HEIGHT - 30))
    if activate==False:
         versao_text=FONT.render(f"Versão: {version}",True, GREEN)
         equipe_text=FONT.render("Desenvolvido pela Invisble Label",True,WHITE)
         win.blit(versao_text, (20, HEIGHT - 60))
         win.blit(equipe_text, (20, HEIGHT-40))
    input_box = pygame.Rect(30, HEIGHT - 90, 300, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')


class _SilentChannel:
    def play(self, *args, **kwargs):
        return None

    def stop(self):
        return None

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    print(f"{BASE_DIR}")
    BASE_DIR = os.path.normpath(os.path.join(BASE_DIR,".."))

    inicial_theme=os.path.join(BASE_DIR,"game_music", "opening_theme.wav")
    credits_theme = os.path.join(BASE_DIR, "game_music", "credits_theme2.wav")
    game_theme = os.path.join(BASE_DIR, "game_music", "deff_theme.wav")

    inicial_theme1 = pygame.mixer.Sound(inicial_theme)
    credits2_theme1 = pygame.mixer.Sound(credits_theme)
    game_theme1 = pygame.mixer.Sound(game_theme)

    game_channel = pygame.mixer.Channel(0)
except pygame.error:
    inicial_theme1 = None
    credits_theme1 = None
    game_theme1 = None
    game_channel = _SilentChannel()

def scene(text, options):
    choice = None
    selected = 0
    last_choice_time = 0  
    
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

        # Processar eventos pygame primeiro
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_RETURN:
                    return options[selected]['action']
                  if control==False:  
                        if event.key == pygame.K_UP:
                            selected = (selected - 1) % len(options)
                        elif event.key == pygame.K_DOWN:
                            selected = (selected + 1) % len(options)
              

        ret, frame = cap.read()
        if ret:
            frame = cv2.flip(frame, 1)  
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detectar rostos
            faces = face_cascade.detectMultiScale(gray, 1.3, 2)
            choice = detectAndDisplay(frame, faces)
            
            # Cooldown para evitar mudanças muito rápidas
            current_time = pygame.time.get_ticks()
            if choice is not None and (current_time - last_choice_time) > 300:
                last_choice_time = current_time
                if activate==True:
                   if control==True:
                    if choice == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif choice == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                


def draw_button(surface, text="Pular texto?", retangulo=skip_text_button, cor_fundo=GREEN):
    # Desenha o fundo do botão
    pygame.draw.rect(surface, cor_fundo, retangulo, border_radius=10)
    
    # Renderiza o texto
    texto_surf = FONT.render(text, True, WHITE)
    
    # Centraliza o texto no botão
    texto_rect = texto_surf.get_rect(center=retangulo.center)
    surface.blit(texto_surf, texto_rect)

def show_text_block(text,font=FONT,delay=9700):
    start_time = pygame.time.get_ticks()
    while True:
        win.fill(BLACK)
        draw_text(win, text, (30, 30), font)
        if activate==True:
            draw_button(win)
        
        show_ui()
        pygame.display.update()
        
        if pygame.time.get_ticks() - start_time >= delay:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and activate:
                    if skip_text_button.collidepoint(event.pos):
                        return 
    clock.tick(FPS)                      
    
def events():
     events2=["Você vê um rosto marcado... Cicatrizes, peças expostas de matal, marcas de cirurgias, manchas de sangue e sérias deformações faciais e olheiras profundas... e um rosto que não parece humano, e nem totalmente desumano... Jrisk te encara, LUA PÁLIDA SORRI ABERTAMENTE... Não há caminhos: A LUA PÁLIDA SORRI ABERTAMENTE. O chão é macio. LUA PÁLIDA SORRI ABERTAMENTE. Jrisk, na forma da lua sorri abertamente para você...",
            "Você vê o que parece ser um carro e um prédio. O prédio derrete feito manteiga metálica na sua frente. A mesma coisa, o carro, e você sente um intenso e quase cegante brilho branco.... Ao longe, uma terrível conclusão sobre o final da batalha entre Prometeus, mutantes e humanos, paira no ar..."]
     return events2[r.randrange(len(events2))]

#   INÍCIO DO JOGO

game_channel.play(inicial_theme1,loops=-1)
show_text_block("Melhor jogar com fone de ouvido.",font=TITLE_FONT)
show_text_block("O jogo pode ser jogado de 2 formas: Convencionalmente, o sistema usado é o teclado. Cima/baixo para mover as opções, e enter para selecionar.",font=TITLE_FONT)
show_text_block("Também pode ser jogado, por meio da biblioteca python OpenCV (controle via webcam). Mova a cabeça para esquerda/direita para alterar a opção, e use enter para selecionar a opção.",font=TITLE_FONT)
show_text_block("Escolha a forma de jogar que dê para você jogar (se não tem webcam, use o teclado).",font=TITLE_FONT)
show_text_block("Esta ainda é a Demo deste jogo!",font=TITLE_FONT)
time.sleep(2)

intro1 = ("Quantunn Gate"
          "Bem vindo, ao futuro "
    )

escolha1=scene(f"{intro1}",[
  {"text":"Jogar","action":"iniciar"},    
  {"text":"Créditos","action":"créditos"}   
])

if escolha1=="créditos":
    game_channel.stop()
    game_channel.play(credits2_theme1,loops=-1)
    for i in range(len_of_function(créditos)):
        show_text_block(créditos(i))


if escolha1=="iniciar":
    
    modo_jogo=scene(f"Você quer jogar via teclado, ou pela webcam?",[
        {"text":"jogar com teclado","action":"teclado"},  
        {"text":"jogar sem teclado","action":"opencv"}  
    ])

    if modo_jogo=="teclado":
        control=False
    if modo_jogo=="opencv":
         control=True

    game_channel.stop()
    game_channel.play(game_theme1,loops= -1)
    show_text_block("Carregando...")
    time.sleep(5)
    show_text_block("                       'A menor distancia entre dois pontos curvos é uma reta geodésica.', Euclides de Alexandria        ",SUBTITLE_FONT)
    time.sleep(3)
    activate=True

    
    for i in range(len_of_function(begin)):
        show_text_block(begin(i))

    decisao = (
        "Há um sistema de dutos de ventilação fazendo um barulho esquisito. Você não tem armas, ou celular. Muito menos um relógio. Há um violão na parede "
        "e dois caminhos: esquerda e direita.")
    
    escolha = scene(f"{decisao}", [
        {"text": "Ir para esquerda", "action": "esquerda"},
        {"text": "Ir para direita", "action": "direita"}])

    if escolha == "esquerda":
        show_text_block("Você anda no caminho escuro, feito de metal. Você continua andando, e sem ver, cai no buraco. Você morre")
        die()

    elif escolha == "direita":
        escolha2 = scene(
        "Você encontra um portão de metal gigante. Não dá pra derrubar. Você volta e decide se vai pegar o violão ou tentar entrar, na marra...",
        [   {"text": "Pegar o violão", "action": "violao"},
            {"text": "Tentar arrombar a porta", "action": "arrombar"}])
    if escolha2 == "violao":
        for i in range(len_of_function(p2_4)):
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
        for i in range(len_of_function(ficar)):
            show_text_block(ficar(i))
        player.dano(5)
        die()    
    elif escolha3 == "investigar":
            for i in range(len_of_function(investigar)):
                show_text_block(investigar(i))
                if i==3:
                    player.dano(2)
                elif i==5 or i==7:
                    time.sleep(2)
                if i==6:
                    player.recuperar(1)
                if i==0: 
                    player.guardar_items("Espingarda Remington")
                if i==1:
                    player.guardar_items("Munição")       
    escolha4=scene(f"Está de noite, e no portão que você arrombou, está escrito: 'Prisão Blacksail, Since 2223. No caminho, você passa por uma televisão antiga. Nela, passam recortes de jornais e de documentários. A moto possui 56% de energia. Bastante, mas não suficiente para um trajeto maior que 60 Km. Então, decide se vai prestar atenção ou se vai roubar a energia para a moto.",[
                {"text": "Prestar atenção", "action": "atencao"},
                {"text": "Roubar energia", "action": "roubar"}
                ])
    if escolha4 == "atencao":
                player.recuperar()
                for i in range(len_of_function(atencao)):
                    show_text_block(atencao(i))
                time.sleep(2)  
                                  
    else:
                for i in range (len_of_function(roubar)):
                    show_text_block(roubar(i))
                player.guardar_items("Lanterna")
                show_text_block(f"Você a usa para iluminar o local e dorme com a {player.mostrar_items('Espingarda Remington')}, no chão.")
                show_text_block("E, antes de dormir você se lembra de outras coisas que ocorreram no passado: ")
    show_text_block("Alguns anos atrás, surgiu a Crispr-CAS19. Um sistema de melhoria genética... Mas, por causa do acesso difícil, poucos tinham e o muitos não. Aqueles que o tinham, se autobatizaram de Prometeus.  Mas o limite do que se poderia ou não, não existia muito bem… Então todo mundo queria sua parte. Logo, disto iniciou-se uma guerra, entre os grupos..."),
    time.sleep(5)
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

    for i in range(len_of_function(sf)):
     show_text_block(sf(i))
     time.sleep(2)
     if sf(-1):
          player.guardar_items("Roupas Antigas")
          show_text_block(f"{year}")

    pygame.display.set_caption("Quantunn Gate - Capítulo 3")
    intro3 = ("Capítulo 3")

    for i in range(len_of_function(Finald)):
        show_text_block(Finald(i))
        if Finald(i)==(Finald(-5) or Finald(-1)):
            time.sleep(2)
            if Finald(i)==Finald(-5):
                player.dano(2)
            elif Finald(i)==(Finald(-1)):
                 die()
    

# CONTINUA AQUI — CAPÍTULO 3...