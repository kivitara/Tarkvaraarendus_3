import pygame

# Funktsioon pildi ekraanil hoidmiseks
def hoiame():

    running = True  # anname muutujale running väärtuse True
    while running:  # loome tsükli pildi ekraanil hoidmiseks
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()  # uuendame ekraani pilti
    pygame.quit()  # paneme ekraani kinni


# Tsykli funktsioon mis joonistab ruute nagu näidispildil
'''def konkreetne():

    # Toome kõigepealt kasti ekraanile
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("tsykkel")
    screen.fill([0, 255, 0])

    # Hakkame joonistama
    a = 0           # Määrame joonistuse algkoordinaadid
    b = 0
    while b < 480:  # Joonistame ridadesse niikaua, kuni ekraan saab täis
        while a < 640:  # Joonistame veergudesse niikaua, kuni ekraan saab täis
            pygame.draw.rect(screen, [255, 0, 225], [a, b, 20, 20], 1) # Joonistame ristküliku
            a = a + 20  # määrame uue alguspunkti koordinaadi x teljel ruudu küljepikkuse võrra
        b = b + 20  # määrame uue alguspunkti koordinaadi Y teljel ruudu küljepikkuse võrra
        a = 0  # Kuna rida sai täis, siis alustame uuelt realt
    hoiame()        # Pöördume funktsiooni "hoiame" poole, et pilti ka näha oleks'''


# Tsykli funktsiooni, et joonistada ruute etteantud parameetritega
def joonista(color, veerud, read, kylg):

    # Toome kõigepealt kasti ekraanile
    pygame.init()
    screen = pygame.display.set_mode([640, 480])
    pygame.display.set_caption("tsykkel")
    screen.fill([0, 255, 0])

    # Hakkame joonistama
    a = 0  # ruudu alguspunkti koordinaadi muutujad
    b = 0
    for rida in range(read):  # joonista niipalju ridu, kui taheti
        for veerg in range(veerud):  # joonista niipalju veerge kui sooviti
            pygame.draw.rect(screen, color, [a, b, kylg, kylg], 1)  # joonistame etteantud väärtustega
            a = a + kylg  # muudame x -telje alguspunkti koordinaati
        b = b + kylg  # muudame y -telje alguspunkti koordinaati
        a = 0  # alustame uut rida veeru alguspunktist
    hoiame()        # Pöördume funktsiooni "hoiame" poole, et näeksime tulemust


# Küsime kumba joonistuse varianti kasutame
print('''Kuidas joonistan?
      1 - Nagu pildil
      2 - Määrad ise parameetrid''')
esmane = 0              # anname muutujale väärtuseks nulli, et saaks vale sisestuse korral uuesti tsyklit täita
while esmane == 0:      # jooksutame tsyklit niikaua, kuni saame soovitud sisestuse
    esmane = int(input())       # ootame numbri sisestust
    if esmane == 2:             # Kui sooviti ise parameetreid määrata siis täidame järgmised read
        # Küsime ja määrame ruutude parameetrid
        kylg = int(input("Kylje pikkus? "))
        read = int(input("Mitu rida? "))
        veerud = int(input("Mitu veergu? "))
        print('''Vali värv
              1 - punane
              2 - kollane
              3 - sinine
              4 - valge
              5 - must''')
        sisestus = 0            # Teeme jälle tsykli, et saada soovitud sisestus
        while sisestus == 0:
            sisestus = int(input())
            if sisestus == 1:
                color = (255, 0, 0)
            elif sisestus == 2:
                color = (255, 255, 100)
            elif sisestus == 3:
                color = (0, 0, 255)
            elif sisestus == 4:
                color = (255, 255, 255)
            elif sisestus == 5:
                color = (0, 0, 0)
            else:
                print('Seda värvi praegu pole, proovi uuesti')
                sisestus = 0

        # Müüd kui kõik soovitud parameetrid on sisestatud, pöördume funktsiooni "joonista" poole, et hakata joonistama
        joonista(color, veerud, read, kylg)

    elif esmane == 1:       # kui sooviti sarnast kujundit nagu ülesande näidises oli, siis määrame kindlad parameetrid
        kylg = 20
        color = (255, 0, 255)
        veerud = 32
        read = 24
        joonista(color, veerud, read, kylg)

        #konkreetne()        # pöördume selle funktsiooni poole, millel oleme ise paramneetrid määranud

    else:
        print("Sellist varianti ma ei pakkunud. Proovi uuesti")
        esmane = 0


