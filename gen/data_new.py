# New prompts. Each answer ends with #rating (1 = obvious ... 7 = only specialists know it).
CARRO = """Gol#1;Uno#1;Fusca#1;Palio#2;Celta#2;Corsa#2;Onix#1;HB20#1;Civic#2;Corolla#1;Kombi#2;Brasília#3;Chevette#3;Opala#2;Monza#3;Kadett#4;Omega#4;
Santana#3;Parati#3;Saveiro#3;Voyage#3;Fox#2;Polo#2;Golf#2;Jetta#3;Passat#4;Tiguan#4;T-Cross#3;Nivus#3;Virtus#3;Up/Up!#3;Amarok#3;SpaceFox#4;CrossFox#4;
Logus#5;Pointer#5;Apollo#6;Variant#4;SP2#5;Karmann-Ghia#4;Puma GTE/Puma#5;Gurgel BR-800/BR-800#5;Siena#3;Strada#2;Toro#2;Mobi#2;Argo#2;Cronos#3;Pulse#3;
Fastback#3;Punto#3;Bravo#4;Stilo#3;Marea#4;Tempra#4;Tipo#4;Elba#5;Prêmio#5;Fiorino#3;Doblò/Doblo#3;Idea#4;Linea#4;Fiat 147/147#4;Oggi#6;Panorama#6;Ducato#4;
Freemont#5;Fiat 500/500#3;Prisma#3;Cobalt#4;Spin#3;Cruze#3;Tracker#2;S10#2;Montana#3;Agile#4;Classic#3;Vectra#3;Astra#3;Zafira#4;Meriva#4;Blazer#4;Caravan#4;
Veraneio#5;D-20#4;C-10#5;Marajó#5;Ipanema#5;Calibra#6;Tigra#5;Captiva#5;Camaro#3;Ka#2;Fiesta#2;Focus#3;Fusion#3;EcoSport#2;Ranger#2;Escort#3;Verona#5;
Del Rey#4;Corcel#4;Belina#4;Pampa#5;Maverick#4;Galaxie#5;Landau#5;Royale#6;Versailles#6;Mustang#2;F-1000#4;Courier#4;Edge#5;Territory#5;Bronco#4;Hilux#2;
Etios#3;Yaris#3;SW4#3;RAV4#4;Bandeirante#5;Prius#4;Corolla Cross#3;Fit#2;City#3;HR-V#2;WR-V#4;CR-V#4;Accord#4;Creta#2;Tucson#3;Santa Fe#4;ix35#4;Azera#5;
i30#4;Veloster#5;Clio#3;Sandero#2;Logan#3;Duster#2;Kwid#2;Captur#4;Oroch#4;Mégane#4;Scénic#4;Symbol#6;Fluence#4;Kardian#4;March#3;Versa#3;Kicks#2;Sentra#4;
Frontier#4;Livina#5;Tiida#5;Renegade#2;Compass#2;Commander#4;Wrangler#4;Cherokee#4;Peugeot 206/206#3;Peugeot 207/207#3;Peugeot 208/208#3;Peugeot 2008/2008#3;
Peugeot 3008/3008#4;Peugeot 306/306#5;Peugeot 307/307#4;Peugeot 308/308#4;Hoggar#6;C3#3;C4#4;Xsara Picasso/Picasso#4;Aircross#4;C4 Cactus#4;Xantia#6;ZX#6;
Pajero#3;L200#3;Lancer#4;ASX#4;Outlander#4;Eclipse Cross#5;Dolphin#3;Dolphin Mini#4;Seal#4;Song#4;Yuan#5;Niva#5;Laika#6;Sportage#3;Picanto#4;Cerato#4;Soul#4;
Sorento#5;Besta#5;Troller#4;Romi-Isetta/Isetta#6;Vemaguet#6;Belcar#6;Aero Willys#6;Rural Willys/Rural#5;Jeep Willys#4;Dart#5;Charger#4;Itamaraty#6;Chambord#6;
Gordini#6;Dauphine#6;Interlagos#6;Miura#6;Santa Matilde#7;Adamo#7;Lafer#7;Hofstetter#7"""

MARCA_CARRO = """Volkswagen/VW#1;Fiat#1;Chevrolet/GM#1;Ford#1;Toyota#1;Honda#1;Hyundai#1;Renault#1;Nissan#2;Jeep#2;Peugeot#2;Citroën#2;Mitsubishi#2;BMW#1;
Mercedes-Benz/Mercedes#1;Audi#1;Porsche#2;Ferrari#1;Lamborghini#2;Kia#2;BYD#2;Volvo#2;Land Rover#3;Jaguar#3;Chery/Caoa Chery#3;JAC#4;GWM/Great Wall#3;Lexus#3;
Subaru#3;Suzuki#3;Mazda#3;Dodge#3;RAM#3;Chrysler#4;Mini#3;Smart#4;Tesla#2;Maserati#3;Bugatti#3;McLaren#3;Aston Martin#3;Bentley#3;Rolls-Royce#3;Alfa Romeo#4;
Lancia#5;Seat#4;Skoda#5;Dacia#5;Opel#4;Lada#4;Troller#4;Gurgel#5;Puma#5;Willys#5;Simca#6;DKW/Vemag#6;Studebaker#6;Saab#5;Infiniti#5;Acura#5;Cadillac#4;Buick#5;
Pontiac#5;Lincoln#5;Hummer#4;Lotus#4;Pagani#5;Koenigsegg#5;Rimac#6;Lucid#6;Rivian#6;Polestar#6;Geely#5;NIO#6;Xpeng#6;Zeekr#6;Leapmotor#6;Mahindra#5;Tata#5;
Proton#6;Daewoo#5;SsangYong#5;Asia Motors#6;Effa#6;Lifan#5;Hafei#7;Changan/Chana#6;DFSK#6;Iveco#5;Scania#4;Agrale#6;Yamaha#2;Kawasaki#3;Ducati#3;
Harley-Davidson/Harley#2;Triumph#4;Royal Enfield#4;Dafra#5;Shineray#4;Haojue#5;KTM#4;Aprilia#5;MV Agusta#6;Benelli#5;Vespa#4;Piaggio#5;Traxx#6;Kasinski#6;
Sundown#6;Indian#5;Bajaj#5;Husqvarna#5;Moto Guzzi#6"""

VIDEOGAME = """Minecraft#1;GTA/Grand Theft Auto#1;FIFA/EA FC/EA Sports FC#1;Fortnite#1;Free Fire#1;Super Mario Bros./Super Mario#1;Pokémon#1;Roblox#1;
Counter-Strike/CS/CS:GO/CS2#1;League of Legends/LoL#1;Call of Duty/COD#1;The Sims#2;Tetris#1;Pac-Man#1;Sonic#1;Zelda/The Legend of Zelda#2;God of War#2;
Resident Evil#2;Valorant#2;Among Us#2;Fall Guys#3;Rocket League#3;Mortal Kombat#2;Street Fighter#2;Tekken#3;The Last of Us#2;Red Dead Redemption#2;
The Witcher#3;Elden Ring#3;Dark Souls#3;Skyrim/The Elder Scrolls#3;Fallout#3;Halo#3;Gears of War#4;Uncharted#3;Crash Bandicoot/Crash#2;Spyro#4;Donkey Kong#2;
Mario Kart#2;Super Smash Bros./Smash#3;Animal Crossing#3;Splatoon#4;Metroid#4;Kirby#3;Final Fantasy#3;Kingdom Hearts#4;Metal Gear/Metal Gear Solid#3;
Silent Hill#4;Assassin's Creed#2;Far Cry#3;Battlefield#3;Overwatch#3;Apex Legends#3;PUBG#2;Dota/Dota 2#3;World of Warcraft/WoW#3;Diablo#4;StarCraft#4;
Age of Empires#3;Counter-Strike dup#9;Ragnarok#4;Tibia#3;Grand Chase#4;Point Blank#4;Gunbound#5;Mu Online/Mu#5;Perfect World#5;Brawl Stars#3;Clash Royale#3;
Clash of Clans#2;Candy Crush#2;Subway Surfers#2;Angry Birds#2;Flappy Bird#3;Hollow Knight#4;Celeste#5;Undertale#4;Cuphead#3;Stardew Valley#3;Terraria#3;
Hades#4;Portal#4;Half-Life#4;Left 4 Dead#4;Team Fortress 2/TF2#4;BioShock#4;Dead Space#4;Mass Effect#4;Cyberpunk 2077/Cyberpunk#3;Baldur's Gate#4;
Hogwarts Legacy#3;Horizon Zero Dawn/Horizon#4;Ghost of Tsushima#4;Bloodborne#4;Sekiro#4;Death Stranding#4;Shadow of the Colossus#5;Ico#6;Okami#5;
Persona#5;Chrono Trigger#5;EarthBound#6;Mother 3#7;Disco Elysium#5;Outer Wilds#6;Kenshi#6;Rain World#6;Pathologic#7;Killer7#7;Shenmue#5;Gitaroo Man#7;
Vib-Ribbon#7;LSD: Dream Emulator#7;Seaman#7;Chulip#7;Horizon Chase#5;Dandara#6;Chroma Squad#6;Knights of Pen and Paper#6;Mônica no Castelo do Dragão#6;
Top Gear#3;International Superstar Soccer/ISS#3;Winning Eleven/PES/Pro Evolution Soccer#2;Bomba Patch#3;Need for Speed#2;Guitar Hero#3;Just Dance#3;
Pokémon GO#2;Genshin Impact#3;Hearthstone#4;Plants vs. Zombies#3;Five Nights at Freddy's/FNAF#3;Bully#3;Max Payne#4;Mafia#4;Watch Dogs#4;Sniper Elite#5;
Hitman#4;Tomb Raider#3;Prince of Persia#4;Castlevania#4;Mega Man#3;Contra#4;Double Dragon#4;Metal Slug#4;King of Fighters/KOF#4;Bomberman#3;Street Rod#6;
Alex Kidd#4;Golden Axe#4;Streets of Rage#4;Altered Beast#5;Toejam & Earl#6;Ecco the Dolphin#5;Earthworm Jim#5;Rock n' Roll Racing#5;Chrono Cross#6;
Xenogears#6;Vagrant Story#6;Parasite Eve#6;Legend of Dragoon#6;Digimon World#5;Harvest Moon#5;Lufia#7"""

CONSOLE = """PlayStation/PS1#1;PlayStation 2/PS2#1;PlayStation 3/PS3#2;PlayStation 4/PS4#1;PlayStation 5/PS5#1;PSP#2;PS Vita/Vita#4;PSone/PS One#4;Xbox#2;
Xbox 360#2;Xbox One#2;Xbox Series X/Series X#2;Xbox Series S/Series S#3;Nintendo Switch/Switch#1;Nintendo Switch 2/Switch 2#2;Wii#2;Wii U#3;GameCube#3;
Nintendo 64/N64#2;Super Nintendo/SNES#1;Nintendinho/NES#2;Game Boy#2;Game Boy Color#3;Game Boy Advance/GBA#3;Nintendo DS/DS#2;Nintendo 3DS/3DS#3;
Virtual Boy#5;Mega Drive#1;Master System#2;Sega Saturn/Saturn#4;Dreamcast#3;Game Gear#4;Sega CD#5;Sega 32X/32X#6;Atari 2600/Atari#2;Atari 7800#6;
Atari Jaguar/Jaguar#5;Atari Lynx/Lynx#6;Magnavox Odyssey/Odyssey#4;Odyssey²/Odyssey 2#6;Intellivision#5;ColecoVision#5;Neo Geo#4;Neo Geo Pocket#6;
TurboGrafx-16/PC Engine#5;3DO#5;CD-i/Philips CD-i#6;Polystation#3;Dynavision#5;Phantom System#6;Top Game#6;Steam Deck#3;ROG Ally#5;WonderSwan#6;N-Gage#5;
Ouya#6;Apple Pippin/Pippin#7;Nuon#7;Vectrex#6;Game.com#7;Pokémon Mini#7;Evercade#6;Analogue Pocket#6;Zeebo#5;Playdia#7;FM Towns Marty#7;Amiga CD32#6;PC-FX#7;
Sega Pico#6;Gizmondo#6;Game & Watch#4;Brick Game/Minigame#3"""

FILME_BR = """Cidade de Deus#1;Tropa de Elite#1;Tropa de Elite 2#2;Central do Brasil#2;O Auto da Compadecida/Auto da Compadecida#1;Ainda Estou Aqui#1;
Minha Mãe É uma Peça#1;Se Eu Fosse Você#2;De Pernas pro Ar#3;Carandiru#2;Bacurau#2;Que Horas Ela Volta#3;O Pagador de Promessas#3;Deus e o Diabo na Terra do Sol#4;
Terra em Transe#5;Vidas Secas#3;Macunaíma#4;Dona Flor e Seus Dois Maridos#3;Lisbela e o Prisioneiro#2;2 Filhos de Francisco/Dois Filhos de Francisco#2;
Meu Nome Não É Johnny#3;Cazuza#3;Elis#4;Tim Maia#3;Bingo: O Rei das Manhãs/Bingo#4;O Palhaço#3;Dois Coelhos#5;O Cheiro do Ralo#4;Estômago#5;
Bicho de Sete Cabeças#3;Abril Despedaçado#4;Cidade Baixa#5;O Ano em que Meus Pais Saíram de Férias#4;Linha de Passe#5;O Som ao Redor#5;Aquarius#4;Marighella#3;
Faroeste Caboclo#3;Somos Tão Jovens#4;Os Normais#3;Divã#4;Loucas pra Casar#4;Os Saltimbancos Trapalhões#4;O Trapalhão na Ilha do Tesouro#6;Xuxa e os Duendes#4;
Lua de Cristal#4;Super Xuxa contra Baixo Astral#5;O Menino e o Mundo#5;Uma História de Amor e Fúria#5;Bruna Surfistinha#3;Hoje Eu Quero Voltar Sozinho#4;
Tatuagem#5;À Meia-Noite Levarei Sua Alma#5;Esta Noite Encarnarei no Teu Cadáver#6;O Bandido da Luz Vermelha#5;Pixote#4;Eles Não Usam Black-Tie#5;Bye Bye Brasil#5;
Cabra Marcado para Morrer#6;Ilha das Flores#4;Limite#6;Ganga Bruta#7;São Paulo, Sociedade Anônima/São Paulo S.A.#7;O Invasor#5;Ônibus 174#4;Jogo de Cena#6;
Edifício Master#5;Branco Sai, Preto Fica#7;Era o Hotel Cambridge#7;Arábia#7;Mato Seco em Chamas#7;Medida Provisória#4;Turma da Mônica: Laços/Laços#3;Nosso Lar#3;
Chico Xavier#3;O Candidato Honesto#4;Até que a Sorte nos Separe#3;Cine Holliúdy#4;Minha Vida em Marte#4;Tô Ryca#4;Os Farofeiros#4;Marte Um#5;Carlota Joaquina#4;
Guerra de Canudos#4;Olga#3;Zuzu Angel#4;O Quatrilho#4;O Que É Isso, Companheiro#4;Orfeu Negro#5;Orfeu#5;Rio, 40 Graus#6;Assalto ao Banco Central#4;Besouro#5;
400 contra 1#5;VIPs#5;A Vida Invisível#5;Lavoura Arcaica#6;Madame Satã#5;Durval Discos#6;O Homem que Copiava#5;Saneamento Básico#5;Mazzaropi/Jeca Tatu#5"""

SERIE = """Friends#1;Breaking Bad#1;Game of Thrones#1;Stranger Things#1;La Casa de Papel/Money Heist#1;The Office#2;Grey's Anatomy#2;Round 6/Squid Game#1;
The Walking Dead#2;Dark#3;Sherlock#2;House/Dr. House#2;Lost#2;Prison Break#2;Two and a Half Men#3;How I Met Your Mother#2;The Big Bang Theory#2;
Os Simpsons/The Simpsons#1;Uma Família da Pesada/Family Guy#3;South Park#3;Rick and Morty#2;Peaky Blinders#2;The Crown#3;Succession#3;
Família Soprano/The Sopranos#3;The Wire#4;Mad Men#4;Better Call Saul#3;Dexter#2;Narcos#2;Vikings#2;The Boys#2;The Last of Us#2;Wandinha/Wednesday#2;Euphoria#3;
Elite#3;Bridgerton#3;Black Mirror#2;Westworld#3;Chernobyl#3;True Detective#3;Fargo#4;Twin Peaks#4;Arquivo X/The X-Files#3;Seinfeld#4;
Todo Mundo Odeia o Chris/Everybody Hates Chris#1;Um Maluco no Pedaço/The Fresh Prince of Bel-Air#2;Eu, a Patroa e as Crianças/My Wife and Kids#3;Chaves#2;
Chapolin#3;Brooklyn Nine-Nine/Brooklyn 99#3;Modern Family#3;Gossip Girl#3;Glee#3;Smallville#3;Supernatural/Sobrenatural#2;Grimm#4;Once Upon a Time#4;
Lúcifer/Lucifer#3;The Mandalorian#3;Andor#4;Loki#3;WandaVision#4;Ozark#3;Mindhunter#4;The Witcher#3;Arcane#3;Fleabag#4;Ted Lasso#4;Ruptura/Severance#4;
O Urso/The Bear#4;Xógum/Shōgun#4;Yellowstone#4;Mr. Robot#4;Halt and Catch Fire#6;Deadwood#6;A Sete Palmos/Six Feet Under#5;Oz#5;Freaks and Geeks#6;Firefly#5;
The Leftovers#5;Les Revenants#7;Borgen#6;The Killing#6;Peep Show#6;Spaced#7;Arrested Development#5;Community#4;Parks and Recreation#4;Malcolm/Malcolm in the Middle#2;
Plantão Médico/ER#4;24 Horas/24#3;Heroes#4;Sense8#4;Atlanta#5;Barry#5;The Expanse#5;Babylon 5#6;Battlestar Galactica#5;Doctor Who#4;Star Trek#3;
Bebê Rena/Baby Reindeer#4;Adolescência/Adolescence#3;Rebelde#2;Rebelde RBD/RBD#3;Carrossel#3;Maria do Bairro#3;A Usurpadora#3;Patito Feo#4;Floribella#4;
Violetta#4;Hannah Montana#2;iCarly#2;Os Feiticeiros de Waverly Place/Feiticeiros de Waverly Place#3;Drake e Josh/Drake & Josh#3;Zoey 101#4;Kenan e Kel/Kenan & Kel#4;
Barrados no Baile/Beverly Hills 90210#5;Twin Peaks dup#9;Kingdom#5;Alice in Borderland#4;Pousando no Amor/Crash Landing on You#5"""

GIRIA = """Mermão#1;Maneiro#1;Caô#1;Sinistro#1;Mó#2;Parada#2;Vacilão#2;Vacilo#2;Bagulho#2;Responsa#3;Tá ligado#1;Partiu#2;Coé/Qual é#1;Bolado#2;Caraca#2;Pô#1;
Irado#2;Neurótico#4;Perrengue#2;Tranquilão#3;Suave#2;Mané#2;Otário#3;Merrmo/Mermo#3;Bonde#2;Bagaça#4;Rolé#2;Brabo#2;Papo reto#2;Fala tu#3;Fechou#2;Formou#3;
Valeu#1;Sangue bom#3;Cria#2;Malandro#2;Brother/Bróder#2;Parceiro#2;Chapa quente#4;Patrão#3;Marrento#3;Neurose#4;Zoeira#3;Cabuloso#3;Na moral#3;Zé Mané#3;
Vapo#5;Ralar#4;Cagado#4;Pistola#3;Crocodilo#4;Pegar visão#4;Dar mole#3;Dar um perdido#4;Caozeiro#3;Muvuca#4;Mó cota#4;Brotar#3;Treta#3;Sussa#4;Calma, calabreso#5;
Mancada#3;Rapá#4;Qual foi#3;Desenrolo/Desenrolar#4;Embaçado#4;Mete o pé#3;Vazar#3;Me erra#4;Coroa#4;Maluco#3;Pagar de#4;Dar ruim#4;
Biscoiteiro/Biscoito#4;Mó onda#4;Tô de boa/De boa#3;Bota fé#5;Ficar bolado dup#9;Responsa dup#9;Fica tranquilo#5;Visão#4;Papo de visão#6;
Tá tranquilo, tá favorável#4;Bagulho doido#4;Moleque#3;Neurose dup#9;Firmeza#4;Caraca, mermão#5;Que isso#4;Gata#3;Novinha#3;
Desenrola#5;Cara de pau#4;Arregou/Arregar#3;Bancar#5;Bater de frente#5;Furar#4;Vacilar#3;Malandragem#3;Maluquice#5;Chapado#4;Tchutchuca#5;Fuleiro#5;Zoado#4"""

PRAIA = """Copacabana#1;Ipanema#1;Leblon#1;Barra da Tijuca/Barra#2;Arpoador#2;Prainha#3;Grumari#3;Joatinga#4;Recreio#3;Leme#3;Praia Vermelha#3;Praia de Botafogo#4;
Praia do Flamengo#4;Urca#4;São Conrado#3;Pepino#5;Reserva#5;Macumba#4;Abricó#5;Itacoatiara#4;Camboinhas#4;Piratininga#4;Icaraí#3;Geribá#3;Ferradura#3;
João Fernandes#3;Azeda#4;Tartaruga#4;Itaúna#4;Lopes Mendes#3;Dois Rios#5;Aventureiro#5;Trindade#4;Ponta Negra#3;Jericoacoara/Jeri#2;Canoa Quebrada#3;
Porto de Galinhas#1;Maragogi#2;Pipa#2;Praia do Forte#2;Morro de São Paulo#2;Itacaré#3;Trancoso#2;Arraial d'Ajuda#3;Caraíva#3;Boa Viagem#2;Iracema#3;
Praia do Futuro#3;Calhau#5;Cumbuco#3;Taíba#5;Baía do Sancho/Sancho#3;Baía dos Porcos#4;Atalaia#4;Pajuçara#3;Ponta Verde#3;Gunga#3;Praia do Francês/Francês#3;
Praia dos Carneiros/Carneiros#3;Tamandaré#4;Bombinhas#3;Jurerê#2;Joaquina#3;Praia Mole#3;Campeche#3;Balneário Camboriú/Camboriú#2;Guarujá#2;Pitangueiras#4;
Maresias#2;Juquehy#3;Camburi#4;Ilhabela#3;Ubatuba#3;Itamambuca#4;Gonzaga#4;Torres#4;Cassino#4;Capão da Canoa#4;Tramandaí#4;Praia do Pinho#5;Guarda do Embaú#4;
Praia do Rosa#3;Ilha do Mel#4;Matinhos#5;Caiobá#5;Lagoinha do Leste#5;Prumirim#6;Bonete#5;Castelhanos#4;Barra Grande#5;Tatajuba#6;Coqueirinho#5;Tambaba#5;
Cabo Branco#4;Tambaú#4;Madeiro#5;Genipabu#3;Praia do Sono#4;Cachadaço#5;Galheta#6;Pântano do Sul#6;Praia do Espelho#4;Taipu de Fora#5;Moreré#6;Prea#6;
Pontal do Atalaia#5;Praia do Cupe#5;Muro Alto#4;Paripueira#5;São Miguel dos Milagres#4;Patacho#5;Carro Quebrado#6;Ponta do Mutá#6;Algodões#6"""

CLUBE_EU = """Real Madrid#1;Barcelona#1;Manchester United#1;Manchester City#1;Liverpool#1;Chelsea#1;Arsenal#1;Bayern de Munique/Bayern#1;Juventus#1;Milan/AC Milan#1;
Inter de Milão/Inter#1;PSG/Paris Saint-Germain#1;Borussia Dortmund/Dortmund#2;Atlético de Madrid#2;Tottenham#2;Benfica#2;Porto#2;Sporting#2;Ajax#2;Roma#2;Napoli#2;
Lazio#3;Sevilla#3;Valencia#3;Villarreal#3;Real Betis/Betis#3;Athletic Bilbao#3;Real Sociedad#3;Celta de Vigo#4;Deportivo La Coruña/Deportivo#4;Espanyol#4;
Getafe#4;Mallorca#4;Osasuna#5;Rayo Vallecano#4;Girona#4;Las Palmas#5;Leganés#5;Eibar#5;Málaga#4;Granada#5;Cádiz#5;Elche#5;Levante#5;Alavés#5;Newcastle#2;
Aston Villa#3;West Ham#3;Everton#3;Leicester#3;Leeds#3;Wolverhampton/Wolves#3;Brighton#3;Fulham#4;Crystal Palace#4;Southampton#4;Nottingham Forest#3;
Burnley#4;Brentford#4;Bournemouth#4;Sunderland#4;Watford#5;Norwich#5;Sheffield United#5;Stoke City#5;Ipswich#5;Wrexham#4;Bayer Leverkusen/Leverkusen#2;
RB Leipzig/Leipzig#3;Schalke 04/Schalke#3;Werder Bremen#3;Wolfsburg#3;Eintracht Frankfurt#3;Borussia Mönchengladbach/Gladbach#4;Stuttgart#3;Hamburgo/Hamburger SV#3;
Hertha Berlim/Hertha#4;Colônia/Köln#4;Union Berlin#4;Freiburg#4;Hoffenheim#4;Mainz#4;St. Pauli#4;Kaiserslautern#4;Olympique de Marselha/Marseille#2;Lyon#2;
Monaco#2;Lille#3;Nice#3;Rennes#4;Bordeaux#4;Nantes#4;Saint-Étienne#4;Lens#4;Montpellier#5;Strasbourg#5;Toulouse#5;Fiorentina#3;Atalanta#3;Torino#4;Genoa#4;
Sampdoria#4;Bologna#4;Udinese#4;Parma#4;Cagliari#5;Hellas Verona/Verona#5;Sassuolo#5;Empoli#5;Lecce#5;Palermo#5;Como#5;Celtic#3;Rangers#3;Galatasaray#2;
Fenerbahçe#3;Beşiktaş/Besiktas#3;Trabzonspor#5;Shakhtar Donetsk/Shakhtar#3;Dínamo de Kiev/Dynamo Kiev#4;Zenit#3;Spartak Moscou/Spartak#4;CSKA Moscou/CSKA#4;
Lokomotiv Moscou#5;Olympiacos#3;Panathinaikos#4;AEK Atenas#5;PAOK#5;Feyenoord#3;PSV#3;AZ Alkmaar/AZ#4;Twente#5;Anderlecht#4;Club Brugge#4;Genk#5;
Standard de Liège#5;Basel#4;Young Boys#5;Red Bull Salzburg/Salzburg#4;Rapid Viena#5;Estrela Vermelha/Crvena Zvezda#4;Partizan#5;Dínamo Zagreb#4;Hajduk Split#6;
Steaua Bucareste/FCSB#4;Slavia Praga#5;Sparta Praga#5;Viktoria Plzeň#6;Legia Varsóvia#5;Ferencváros#5;Copenhague/FC Copenhagen#4;Brøndby#6;Malmö#5;AIK#6;
Rosenborg#5;Bodø/Glimt#5;Molde#6;HJK#6;Braga#3;Vitória de Guimarães#4;Boavista#4;Famalicão#6;Rio Ave#6;Marítimo#6;Gil Vicente#6;Estoril#6;Belenenses#6;
Ludogorets#6;Sheriff Tiraspol#6;APOEL#6;Maccabi Tel Aviv#6;Dínamo Tbilisi#7;BATE Borisov#7;Shamrock Rovers#7;Linfield#7;The New Saints#7;Lincoln Red Imps#7;
FC Santa Coloma#7;Tre Penne#7;Flora Tallinn#7"""

CERVEJA = """Skol#1;Brahma#1;Antarctica#1;Heineken#1;Budweiser#1;Itaipava#1;Amstel#2;Stella Artois#2;Corona#1;Original#2;Bohemia#2;Kaiser#2;Devassa#2;Eisenbahn#3;
Spaten#2;Petra#3;Crystal#3;Nova Schin/Schin#2;Bavaria#3;Sol#3;Polar#3;Serramalte#4;Colorado#3;Baden Baden#4;Therezópolis#4;Way Beer#5;Wäls#4;Bodebrown#5;
Dama Bier#6;Tupiniquim#6;Hocus Pocus#5;Praya#5;Patagonia#3;Beck's#3;Guinness#2;Hoegaarden#3;Leffe#4;Chimay#4;Duvel#4;Paulaner#3;Erdinger#3;Weihenstephaner#4;
Franziskaner#4;Warsteiner#4;Bitburger#5;Krombacher#5;Löwenbräu#5;Pilsner Urquell#4;Budweiser Budvar/Budvar#6;Kronenbourg#5;Peroni#3;Birra Moretti/Moretti#4;
Carlsberg#3;Tuborg#4;Asahi#4;Sapporo#4;Kirin#4;Tsingtao#5;Singha#5;Chang#5;Tiger#4;Estrella Galicia#3;Estrella Damm#4;Mahou#5;San Miguel#5;Super Bock#4;
Sagres#4;Quilmes#4;Cusqueña#5;Club Colombia#6;Aguila#6;Modelo#3;Dos Equis/XX#4;Pacífico#4;Tecate#4;Victoria#5;Miller#3;Coors#4;Michelob Ultra/Michelob#4;
Blue Moon#4;Samuel Adams#5;Brooklyn Lager/Brooklyn#5;BrewDog#5;Delirium Tremens/Delirium#4;Kwak#5;Westmalle#6;Westvleteren#7;Orval#6;Rochefort#6;La Trappe#6;
Köstritzer#6;Schneider Weisse#6;Ayinger#6;Rogue#6;Sierra Nevada#5;Lagunitas#5;Goose Island#4;Stone#6;Cerpa#5;Xingu#5;Belco#6;Caracu#4;Glacial#4;Proibida#4;
Conti#5;Império#4;Amazon Beer#6;Saint Bier#6;Ashby#6;Coruja#6;Opa Bier#6;Lohn Bier#7;Bamberg#6;Bierland#6;Backer#5;Blondine#7"""

BRINCADEIRA = """Pique-esconde/Esconde-esconde#1;Pega-pega/Pique-pega#1;Amarelinha#1;Queimada#1;Pular corda#1;Bola de gude/Bolinha de gude#2;Pião#2;Pipa/Papagaio#1;
Cabo de guerra#2;Estátua#2;Batata quente#2;Dança das cadeiras#2;Ciranda#2;Telefone sem fio#2;Passa anel#3;Adoleta#3;Elefante colorido#3;Mamãe da rua/Mãe da rua#4;
Polícia e ladrão/Polícia e bandido#2;Rouba-bandeira/Pique-bandeira#3;Taco/Bete/Bets#3;Elástico#3;Corre cotia#3;Cinco Marias/Saquinho#4;Ioiô#2;Bambolê#2;
Carrinho de rolimã#3;Peteca#2;Cama de gato#4;Stop/Adedonha#2;Forca#2;Jogo da velha#2;Batalha naval#3;Morto-vivo#2;Escravos de Jó#3;Seu mestre mandou/O mestre mandou#2;
Cabra-cega#3;Gato mia#4;Garrafão#5;Pique-alto#4;Pique-cola/Congela#3;Pula-sela/Pular carniça#4;Bafo/Bater figurinha#3;Bolha de sabão/Bolinha de sabão#3;
Detetive#3;Verdade ou desafio#2;Futebol de botão#3;Rouba-monte#4;Pebolim/Totó#3;Bilboquê#4;Perna de pau#4;Vai e vem#4;Corrida de saco#3;Ovo na colher#4;
Boca de forno#5;Sete pecados#6;Pé de lata#5;Cavalinho de pau#5;Massinha#3;Lego#2;Tazo#3;Barra-manteiga#5;Chicotinho queimado#5;Tampinha/Futebol de tampinha#4;
Trava-língua#4;Zerinho ou um#4;Par ou ímpar#3;Pedra, papel e tesoura/Jokenpô#2;Mímica#3;Mamãe, posso ir#5;Coelhinho sai da toca#5;Bobinho#4;Salada mista#4;
Gato e rato#4;Carrinho de mão#5;Cai no poço#6;Pique-pedra#6;Lenço atrás#5;Cobra-cega#5;Bola queimada dup#9;Gamão#5;Dominó#3;Damas#3;Uno#3;Banco Imobiliário#3;
Jogo do mico/Mico#4;Pescaria#4;Boneca#3;Casinha#3;Comidinha#4;Pula-pula#3;Escorrega/Escorregador#3;Gangorra#3;Balanço#3;Gira-gira#4;Trepa-trepa#4;Patinete#3;
Patins#3;Bicicleta#2;Velotrol#4;Bate-bate#5;Telefone de lata#4;Avião de papel#3;Barquinho de papel#4;Cata-vento#4;Estilingue/Atiradeira/Baladeira#4;Bodoque#6"""

PAO = """Pão francês/Pão de sal/Cacetinho#1;Pão de forma#1;Pão de queijo#1;Pão de mel#2;Pão sírio/Pão árabe/Pita#2;Baguete#2;Ciabatta#2;Croissant#2;Brioche#3;
Focaccia#3;Pão australiano#2;Pão italiano#2;Pão integral#2;Pão de batata#2;Pão de leite#2;Pão doce#2;Pão de milho#3;Broa#3;Bisnaguinha#2;Pão de hambúrguer#2;
Pão de cachorro-quente/Pão de hot dog#2;Sonho#3;Rosca#3;Panetone#2;Chocotone#3;Bagel#3;Naan#4;Tortilha#4;Chapati#5;Pão de centeio#3;Pumpernickel#5;Levain#3;
Pão de abóbora#4;Pão de alho#3;Pão sovado#3;Pão careca#4;Pão bengala#4;Pão de coco#4;Pão de minuto#4;Pão de frigideira#4;Pão de mandioca/Pão de aipim#4;
Melonpan#5;Shokupan#6;Mantou#6;Bao#4;Chalá/Challah#6;Pretzel#3;Pão kaiser#5;Pain de campagne#5;Fougasse#6;Pão alentejano#6;Pão de Deus#5;Bolo do caco#5;
Pão húngaro#5;Pão tatu#6;Pão de cará#5;Pão de batata-doce#5;Pão de aveia#4;Pão multigrãos#3;Pão sem glúten#4;Pão de fubá#4;Grissini#5;Torrada#3;Arepa#4;
Chipa#6;Cuñapé#7;Pandebono#7;Pão de nozes#5;Pão de passas#5;Pão preto#4;Pão de banana#5;Pão de mandioquinha#5;Pão de cebola#4;Pão de calabresa#4;
Pão de linguiça#4;Pão de leite condensado#5;Pão de cenoura#5;Pão de beterraba#6;Pão de espinafre#6;Pão de tapioca#5;Pão pullman#4;Pão caseiro#3;Pão de padaria dup#9;
Pão de ló#4;Pão bola/Pão d'água#5;Pão de sanduíche#5;Mini pão#5;Pão de azeitona#5;Pão de ervas#5;Pão de parmesão#5;Pão de fermentação natural#4;Pão sueco#6;
Pão de soda/Soda bread#6;Lavash#6;Injera#6;Pita dup#9;Roti#6;Paratha#6;Puri#7;Tsoureki#7;Kulich#7;Stollen#6;Colomba#5;Pão de Viena#6;Rosca de Reis#6;
Pão de Jerusalém#7;Simit#7;Khachapuri#7;Pão de batata recheado#5;Pão de cachorro dup#9;Bisnaga#4;Filão#4;Pão de mel dup#9;Pão de queijo mineiro dup#9"""

COBRA = """Jiboia/Boa constrictor#1;Sucuri/Anaconda#1;Cascavel#1;Jararaca#1;Cobra-coral/Coral#1;Naja/Cobra-de-capelo#1;Píton/Piton#2;Mamba-negra#2;Surucucu/Surucucu-pico-de-jaca#3;
Cobra-cipó#3;Caninana#3;Cobra-d'água#3;Muçurana/Mussurana#4;Urutu/Urutu-cruzeiro#3;Jararacuçu#3;Boipeva#5;Cobra-real/Naja-real#2;Víbora#3;Taipan#4;
Serpente-marinha/Cobra-do-mar#4;Cobra-papagaio#4;Cobra-verde#4;Falsa-coral#4;Periquitamboia#6;Jiboia-arco-íris/Salamanta#5;Sucuri-amarela#5;Cobra-espada#6;
Dormideira#6;Parelheira#6;Corredeira#6;Cobra-capim#6;Jararaca-ilhoa#5;Víbora-chifruda#5;Víbora-do-gabão#5;Krait#6;Cobra-tigre#6;Mamba-verde#4;Boomslang#6;
Áspide#5;Cobra-rato#5;Cobra-do-milho/Corn snake#4;Cobra-rei#5;Naja-cuspideira/Cobra-cuspideira#4;Serpente-voadora/Cobra-voadora#5;Píton-reticulada#4;
Píton-bola/Ball python#4;Boa-de-areia#6;Titanoboa#5;Cascavel-diamante#5;Sidewinder/Cascavel-chifruda#6;Víbora-de-russell#6;Echis/Víbora-serrilhada#7;
Cobra-de-coral-verdadeira dup#9;Bothrops#5;Jararaca-pintada#6;Cotiara#7;Urutu dup#9;Cobra-preta/Muçurana-preta#6;Cobra-de-pernas? #9;
Sucuri-verde#4;Jiboia-constritora dup#9;Cobra-chicote#6;Cobra-de-vidro#6;Anfisbena/Cobra-de-duas-cabeças#4;Cobra-cega#5"""

DISNEY = """O Rei Leão/Rei Leão#1;Frozen#1;Branca de Neve#1;Cinderela#1;A Bela e a Fera#1;A Pequena Sereia#1;Aladdin#1;Mulan#1;Pocahontas#2;Moana#1;Enrolados#2;
Zootopia#1;Encanto#1;Lilo & Stitch/Lilo e Stitch#1;Tarzan#2;Hércules#2;Pinóquio#2;Dumbo#2;Bambi#2;Peter Pan#2;Alice no País das Maravilhas#2;A Bela Adormecida#2;
Fantasia#3;Mogli/Mogli: O Menino Lobo#2;101 Dálmatas/Cento e Um Dálmatas#2;Robin Hood#3;Os Aristogatas/Aristogatas#3;A Dama e o Vagabundo#2;
O Corcunda de Notre Dame#3;Detona Ralph#2;Operação Big Hero/Big Hero 6#2;Raya e o Último Dragão#3;Wish#4;Bolt#3;A Princesa e o Sapo#3;Irmão Urso#3;
Atlantis: O Reino Perdido/Atlantis#3;A Nova Onda do Imperador#2;Planeta do Tesouro#4;Dinossauro#4;O Galinho Chicken Little/Chicken Little#3;A Família do Futuro#4;
Nem que a Vaca Tussa#5;O Cão e a Raposa#3;O Caldeirão Mágico#5;As Peripécias do Ratinho Detetive/Ratinho Detetive#5;Bernardo e Bianca#4;Oliver e Sua Turma#5;
A Espada Era a Lei#3;Alô, Amigos/Saludos Amigos#6;Você Já Foi à Bahia#6;Música, Maestro#7;Como É Bom Se Divertir#7;Tempo de Melodia#7;
As Aventuras de Ichabod e Sr. Sapo#7;Fantasia 2000#5;O Ursinho Pooh/Ursinho Pooh/Winnie the Pooh#3;Frozen 2#2;Moana 2#2;Mundo Estranho#5;Tinker Bell#4;Aviões#4;
O Rei Leão 2#4;Zootopia 2#3;Lilo & Stitch 2#5;Mogli 2#5;A Pequena Sereia 2#5;Aladdin e os 40 Ladrões#5;O Retorno de Jafar#5;Pocahontas 2#5;Mulan 2#5;
Tarzan 2#6;O Corcunda de Notre Dame 2#6;Cinderela 2#5;Bambi 2#6;Peter Pan: De Volta à Terra do Nunca#5;Bernardo e Bianca na Terra dos Cangurus#5;
A Dama e o Vagabundo 2#5;O Cão e a Raposa 2#6;Pateta: O Filme/A Extraordinária Aventura de Pateta#5;Mickey: Era uma Vez no Natal#6;DuckTales: O Filme#6;
Pequenos Grandes Heróis? #9;O Natal do Mickey#6;Recess? #9"""

ANIME = """Naruto#1;Dragon Ball#1;Dragon Ball Z#1;One Piece#1;Pokémon#1;Death Note#1;Attack on Titan/Shingeki no Kyojin#1;Cavaleiros do Zodíaco/Saint Seiya#1;
Demon Slayer/Kimetsu no Yaiba#1;Jujutsu Kaisen#2;My Hero Academia/Boku no Hero#2;Bleach#2;Fullmetal Alchemist#2;Hunter x Hunter#2;One Punch Man#2;Sailor Moon#2;
Yu Yu Hakusho#2;Yu-Gi-Oh#2;Digimon#2;Spy x Family#2;Chainsaw Man#2;Tokyo Ghoul#2;Sword Art Online#2;Code Geass#3;Neon Genesis Evangelion/Evangelion#3;
Cowboy Bebop#3;Steins Gate#4;Haikyuu#3;Kuroko no Basket#3;Blue Lock#3;Inazuma Eleven/Super Onze#4;Super Campeões/Captain Tsubasa#3;Slam Dunk#4;Fairy Tail#3;
Black Clover#3;Dr. Stone#4;Mob Psycho 100#4;Vinland Saga#4;Berserk#4;JoJo/JoJo's Bizarre Adventure#3;Hellsing#4;Trigun#5;Samurai X/Rurouni Kenshin#3;
Samurai Champloo#5;Inuyasha#3;Sakura Card Captors/Sakura#3;Shaman King#3;Beyblade#3;Doraemon#3;Frieren#3;Solo Leveling#2;Dandadan#3;Oshi no Ko#4;Kaguya-sama#5;
Toradora#5;Clannad#5;Shigatsu wa Kimi no Uso/Your Lie in April#5;Violet Evergarden#4;Akira#4;A Viagem de Chihiro#3;Meu Amigo Totoro/Totoro#3;Princesa Mononoke#4;
Your Name/Kimi no Na wa#3;O Castelo Animado#4;Ghost in the Shell#4;Paprika#6;Perfect Blue#5;Serial Experiments Lain/Lain#6;Texhnolyze#7;Ergo Proxy#6;Monster#5;
Mushishi#6;Kino no Tabi/Kino's Journey#6;Haibane Renmei#7;Ginga Eiyuu Densetsu/Legend of the Galactic Heroes#6;Ping Pong the Animation#6;Tatami Galaxy#7;
Boogiepop Phantom#7;Kaiba#7;Dennou Coil#7;Angel's Egg/Tenshi no Tamago#7;Kemonozume#7;Shin-chan/Crayon Shin-chan#3;Hamtaro#4;Medabots#4;Zatch Bell#4;Bakugan#3;
Speed Racer#4;Astro Boy#4;Fly/Dragon Quest: Dai no Daibouken#4;Shurato#5;Guerreiras Mágicas de Rayearth/Rayearth#5;Yugi dup#9;Dragon Ball Super#2;Boruto#3;
Fire Force#4;Konosuba#4;Re:Zero#4;Overlord#4;That Time I Got Reincarnated as a Slime/Tensura#5;No Game No Life#4;Noragami#4;Soul Eater#3;D.Gray-man#5;
Gintama#4;Great Teacher Onizuka/GTO#5;Hajime no Ippo#4;Initial D#4;Gurren Lagann#4;Kill la Kill#4;Cyberpunk: Edgerunners/Edgerunners#3;Devilman Crybaby#5;
Parasyte/Kiseijuu#4;Made in Abyss#5;The Promised Neverland/Yakusoku no Neverland#4;Erased/Boku dake ga Inai Machi#5;Another#5;Higurashi#6;Elfen Lied#5;
Gantz#5;Claymore#5;Mirai Nikki/Future Diary#5;Akame ga Kill#4;Btooom#6;Deadman Wonderland#5;Darker than Black#6;Baccano#6;Durarara#5;Psycho-Pass#5"""

METRO_RIO = """Central/Central do Brasil#1;Carioca#1;Uruguaiana#2;Cinelândia#2;Botafogo#2;Cardeal Arcoverde#3;Siqueira Campos#2;Cantagalo#3;General Osório#2;
Nossa Senhora da Paz#3;Jardim de Alah#3;Antero de Quental#3;São Conrado#3;Jardim Oceânico#2;Largo do Machado#2;Flamengo#3;Catete#3;Glória#3;Presidente Vargas#3;
Praça Onze#3;Estácio#2;Afonso Pena#4;São Francisco Xavier#4;Saens Peña#2;Uruguai#3;Cidade Nova#3;São Cristóvão#3;Maracanã#2;Triagem#4;Maria da Graça#4;
Nova América/Del Castilho#3;Inhaúma#4;Engenho da Rainha#4;Thomaz Coelho/Tomás Coelho#5;Vicente de Carvalho#4;Irajá#4;Colégio#5;Coelho Neto#5;
Acari/Fazenda Botafogo#6;Engenheiro Rubens Paiva#6;Pavuna#3"""

SIMPSONS = """Homer#1;Marge#1;Bart#1;Lisa#1;Maggie#1;Sr. Burns/Montgomery Burns/Burns#2;Smithers#3;Ned Flanders/Flanders#2;Moe#2;Apu#2;Milhouse#2;Krusty#2;Barney#3;
Chefe Wiggum/Wiggum#3;Ralph#3;Nelson#3;Diretor Skinner/Skinner#3;Edna Krabappel/Krabappel#4;Patty#4;Selma#4;Vovô Simpson/Abe Simpson/Abe#3;Sideshow Bob/Bob#3;
Otto#4;Zelador Willie/Willie#3;Cara dos Quadrinhos/Comic Book Guy#4;Dr. Hibbert#4;Dr. Nick#5;Lenny#4;Carl#4;Kent Brockman#5;Troy McClure#5;Lionel Hutz#5;
Prefeito Quimby/Quimby#4;Gordo Tony/Fat Tony#5;Professor Frink/Frink#4;Reverendo Lovejoy/Lovejoy#4;Helen Lovejoy#5;Todd#4;Rod#4;Maude Flanders/Maude#5;Martin#4;
Jimbo#5;Kearney#5;Dolph#6;Sherri e Terri#5;Uter#6;Hans Moleman/Moleman#5;Cletus#4;Brandine#6;Velha dos Gatos/Crazy Cat Lady#4;Gil#5;Snake#5;
Homem-Abelha/Bumblebee Man#5;Duffman#4;Comichão e Coçadinha/Itchy e Scratchy#3;Ajudante de Papai Noel/Santa's Little Helper#3;Bola de Neve/Snowball#4;
Kang e Kodos#4;Lurleen#6;Herb Powell/Herb#6;Mona Simpson/Mona#5;Jacqueline Bouvier#6;Agnes Skinner#5;Disco Stu#5;Ruth Powers#7;Rainier Wolfcastle/McBain#5;
Sideshow Mel#5;Bleeding Gums Murphy#6;Artie Ziff#6;Frank Grimes/Grimey#6;Porco-Aranha/Plopper#3;Jasper#6;Lou#6;Eddie#6;Dr. Marvin Monroe#7;Doris#6;Manjula#6;
Superintendente Chalmers/Chalmers#5;Arnie Pye#7;Dewey Largo/Largo#6;Lindsey Naegle#7;Hank Scorpio#6;Sideshow Raheem? #9;Squeaky Voiced Teen/Adolescente da voz fina#6;
Allison Taylor#7;Bernice Hibbert#7;Wendell#6;Lewis#7;Database#7;Señor Ding-Dong? #9;Stampy#6;Pinchy#7;Blinky#5;Mr. Teeny#6;Lyle Lanley#6;Llewellyn Sinclair#7"""
