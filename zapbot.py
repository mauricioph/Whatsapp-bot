from selenium import webdriver
import time

class WhatsappBot:
    def __init__(self):
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["Leonardo Medeiros"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=options)
        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)


    def EnviarMensagens(self):
        # Parte 1 - A mensagem que você quer enviar
        azbonsonaro = ["atencioso", "agradável", "adorável", "amável", "afável", "amigo", "amoroso", "autêntico", "apaixonado", "animado", "alegre", "amigável", "amistoso", "afetivo", "afetuoso", "acolhedor", "aprazível", "atraente", "atrativo", "audaz", "aventureiro", "arrojado", "auspicioso", "aplicado", "altruísta", "assertivo", "atento", "ágil", "apto", "atilado", "astuto", "arguto", "ajuizado", "assombroso", "admirável", "airoso", "adônis", "afortunado", "acautelado", "angelical", "aberto", "acessível", "om", "bondoso", "bonito", "belo", "bem-educado", "bem-humorado", "bem-disposto", "bacana", "bendito", "batalhador", "baseado", "benemérito", "benfeitor", "benévolo", "benevolente", "brilhante", "brioso", "brincalhão", "bombástico", "beleza", "beldade", "bonachão", "bonacheirão", "barra-limpa", "benéfico", "benigno", "benfazejo", "benquisto", "bem-parecido", "bem-encarado", "bem-intencionado", "bem-comportado", "bem-apessoado", ". bem-aventurado", "bem-afortunado", "bem-amado", "bem-querente", "bem-ditoso", "bem-criado", "bem-dotado", "bem-posto", "bem-visto", "calmo", "caloroso", "camarada", "cândido", "capaz", "caridoso", "carinhoso", "carismático", "caritativo", "castiço", "cativante", "cauteloso", "cavalheiro", "celestial", "centrado", "charmoso", "cheiroso", "chique", "chistoso", "ciente", "circunspecto", "cívico", "civil", "civilizado", "clarividente", "clemente", "coerente", "colaborador", "colega", "comedido", "companheiro", "compassivo", "competente", "complacente", "comportado", "compreensivo", "confiante", "confiável", "confidente", "conhecedor", "consciencioso", "consciente", "contente", "convicto", "cooperador", "corajoso", "cordial", "correto", "cortês", "crânio", "credível", "crescido", "criativo", "criterioso", "crível", "cuidadoso", "culto", "calmo", "caloroso", "camarada", "cândido", "capaz", "caridoso", "carinhoso", "carismático", "caritativo", "castiço", "cativante", "cauteloso", "cavalheiro", "celestial", "centrado", "charmoso", "cheiroso", "chique", "chistoso", "ciente", "circunspecto", "cívico", "civil", "civilizado", "clarividente", "clemente", "coerente", "colaborador", "colega", "comedido", "companheiro", "compassivo", "competente", "complacente", "comportado", "compreensivo", "confiante", "confiável", "confidente", "conhecedor", "consciencioso", "consciente", "contente", "convicto", "cooperador", "corajoso", "cordial", "correto", "cortês", "crânio", "credível", "crescido", "criativo", "criterioso", "crível", "cuidadoso", "educado", "eficiente", "efusivo", "elegante", "eloquente", "emancipado", "eminente", "empático", "empenhado", "empolgado", "empreendedor", "encantador", "encorajador", "engenhoso", "engraçado", "entendido", "entusiasmado", "entusiasta", "equânime", "equilibrado", "esbelto", "esclarecido", "escrupuloso", "esforçado", "esmerado", "espantoso", "especial", "especialista", "esperançoso", "esperto", "espetacular", "espirituoso", "esplêndido", "esplendoroso", "espontâneo", "estonteante", "eterno", "evoluído", "excelente", "excelso", "exemplar", "exímio", "experiente", "extraordinário", "extrovertido", "extremoso", "exuberante", "fiel", "forte", "franco", "frontal", "firme", "fantástico", "fenomenal", "fabuloso", "fascinante", "formidável", "fidedigno", "formoso", "fofo", "feliz", "felizardo", "faceiro", "fervoroso", "gentil", "generoso", "genuíno", "gracioso", "grande", "grandioso", "gênio", "genial", "gentleman", "glorioso", "glamoroso", "gigante", "gigantesco", "guerreiro", "gracejador", "galanteador", "garboso", "grato", "gratífico", "galhardo", "galhofeiro", "gaiato", "gaiteiro", "grácil", "guapo", "honesto", "honrado", "humano", "honroso", "honorável", "herói", "heroico", "hábil", "habilidoso", "hercúleo", "hilário", "hilariante", "hílare", "hospitaleiro", "humanitário", "hospedeiro", "humilde", "húmile", "humildoso", "inteligente", "importante", "íntegro", "incrível", "ilustre", "interessante", "impressionante", "ímpar", "ideal", "imponente", "imaginativo", "impecável", "irreverente", "irresistível", "inigualável", "imparcial", "idôneo", "independente", "inspirador", "interventivo", "intuitivo", "intenso", "intelectual", "instruído", "imortal", "impávido", "iluminado", "imaculado", "idealista", "idílico", "idilista", "imparável", "inabalável", "incansável", "imbatível", "invencível", "insubmisso", "insubornável", "invulnerável", "incorruptível", "incorrupto", "imprescindível", "indispensável", "intemerato", "justo", "jovem", "jovial", "joia", "jeitoso", "jubilante", "jubiloso", "justiceiro", "jucundo", "leal", "legal", "lindo", "livre", "lutador", "louvável", "laudável", "legítimo", "lúcido", "lisonjeiro", "loquaz", "liberal", "liberto", "lícito", "líder", "letrado", "laborioso", "lançado", "lesto", "ledo", "lauto", "maravilhoso", "magnifico", "magnânimo", "majestoso", "magnificente", "maior", "melhor", "máximo", "merecedor", "maneiro", "modesto", "módico", "mavioso", "motivado", "marcante", "mágico", "magno", "magistral", "maestral", "meritório", "moderno", "moderado", "maduro", "meticuloso", "minucioso", "metódico", "notável", "nobre", "normal", "natural", "novo", "naturista", "obediente", "objetivo", "obsequioso", "observador", "obstinado", "oficioso", "operante", "oportuno", "ordeiro", "organizado", "original", "otimista", "ótimo", "pacato", "paciente", "pacificador", "pacífico", "parceiro", "parcimonioso", "perfeito", "perito", "perseverante", "persistente", "perspicaz", "pertinaz", "piedoso", "pioneiro", "poderoso", "poderoso", "polido", "ponderado", "pontual", "porreiro", "porreta", "possante", "potente", "prazenteiro", "preparado", "prestativo", "prestável", "prestigioso", "prevenido", "primoroso", "príncipe", "prócere", "prodígio", "prodigioso", "proeminente", "proficiente", "protetor", "provecto", "prudente", "pudibundo", "pudico", "pujante", "pulcro", "querido", "qualificado", "responsável", "respeitável", "respeitador", "respeitado", "respeitoso", "realizado", "renomado", "resistente", "resoluto", "resolvido", "resiliente", "robusto", "romântico", "risonho", "ridente", "radiante", "resplandecente", "reluzente", "refinado", "racional", "realista", "refletido", "relaxado", "receptivo", "reconhecido", "rápido", "simpático", "sábio", "sincero", "sensato", "sensacional", "seguro", "sorridente", "sossegado", "sublime", "solícito", "solidário", "sereno", "sensível", "sedutor", "sagaz", "saudável", "singular", "sociável", "sofisticado", "sério", "sexy", "sonhador", "santo", "são", "sentimental", "sapeca", "serelepe", "sabedor", "sadio", "talentoso", "ternurento", "terno", "tranquilo", "transparente", "tolerável", "triunfal", "triunfante", "tranquilizador", "único", "uno", "urbano", "unificador", "ultrafantástico", "ultracompetente", "ultraconfiante", "ultra-honesto", "ultracorreto", "ultra-autônomo", "ultraindependente", "ultranatural", "ultrarromântico", "ultra-humano", "ultracivilizado", "ultradivino", "ultramoderno", "verdadeiro", "valente", "valioso", "valoroso", "vencedor", "verídico", "venerável", "venturoso", "vistoso", "virtuoso", "versado", "versátil", "visionário", "vitorioso", "veemente", "venerado", "verossímil", "vanguardista", "venusto", "vetusto", "valido", "veloz", "viril", "varonil", "veraz", "vero", "verboso", "vibrante", "vigoroso", "viçoso", "verdejante", "vívido", "vivaço", "vivo", "vivaz", "vital", "vigilante", "zeloso", "zen", "zelador"]
        self.mensagem = "Diz que Bolsonaro é %s" %(azbonsonaro[x])
        
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo_ou_pessoa}']")
            time.sleep(3)
            # Aqui estou definindo 590, porque na lista acima tem 589 qualidades, portanto eu quero mandar todas as mensagens.
            for i in range(590):
                campo_grupo.click()
                chat_box = self.driver.find_element_by_class_name('_1Plpp')
                chat_box.click()
                # Repeti a mensagem aqui, para fazer o envio rapido
                azbonsonaro = ["atencioso", "agradável", "adorável", "amável", "afável", "amigo", "amoroso", "autêntico", "apaixonado", "animado", "alegre", "amigável", "amistoso", "afetivo", "afetuoso", "acolhedor", "aprazível", "atraente", "atrativo", "audaz", "aventureiro", "arrojado", "auspicioso", "aplicado", "altruísta", "assertivo", "atento", "ágil", "apto", "atilado", "astuto", "arguto", "ajuizado", "assombroso", "admirável", "airoso", "adônis", "afortunado", "acautelado", "angelical", "aberto", "acessível", "om", "bondoso", "bonito", "belo", "bem-educado", "bem-humorado", "bem-disposto", "bacana", "bendito", "batalhador", "baseado", "benemérito", "benfeitor", "benévolo", "benevolente", "brilhante", "brioso", "brincalhão", "bombástico", "beleza", "beldade", "bonachão", "bonacheirão", "barra-limpa", "benéfico", "benigno", "benfazejo", "benquisto", "bem-parecido", "bem-encarado", "bem-intencionado", "bem-comportado", "bem-apessoado", ". bem-aventurado", "bem-afortunado", "bem-amado", "bem-querente", "bem-ditoso", "bem-criado", "bem-dotado", "bem-posto", "bem-visto", "calmo", "caloroso", "camarada", "cândido", "capaz", "caridoso", "carinhoso", "carismático", "caritativo", "castiço", "cativante", "cauteloso", "cavalheiro", "celestial", "centrado", "charmoso", "cheiroso", "chique", "chistoso", "ciente", "circunspecto", "cívico", "civil", "civilizado", "clarividente", "clemente", "coerente", "colaborador", "colega", "comedido", "companheiro", "compassivo", "competente", "complacente", "comportado", "compreensivo", "confiante", "confiável", "confidente", "conhecedor", "consciencioso", "consciente", "contente", "convicto", "cooperador", "corajoso", "cordial", "correto", "cortês", "crânio", "credível", "crescido", "criativo", "criterioso", "crível", "cuidadoso", "culto", "calmo", "caloroso", "camarada", "cândido", "capaz", "caridoso", "carinhoso", "carismático", "caritativo", "castiço", "cativante", "cauteloso", "cavalheiro", "celestial", "centrado", "charmoso", "cheiroso", "chique", "chistoso", "ciente", "circunspecto", "cívico", "civil", "civilizado", "clarividente", "clemente", "coerente", "colaborador", "colega", "comedido", "companheiro", "compassivo", "competente", "complacente", "comportado", "compreensivo", "confiante", "confiável", "confidente", "conhecedor", "consciencioso", "consciente", "contente", "convicto", "cooperador", "corajoso", "cordial", "correto", "cortês", "crânio", "credível", "crescido", "criativo", "criterioso", "crível", "cuidadoso", "educado", "eficiente", "efusivo", "elegante", "eloquente", "emancipado", "eminente", "empático", "empenhado", "empolgado", "empreendedor", "encantador", "encorajador", "engenhoso", "engraçado", "entendido", "entusiasmado", "entusiasta", "equânime", "equilibrado", "esbelto", "esclarecido", "escrupuloso", "esforçado", "esmerado", "espantoso", "especial", "especialista", "esperançoso", "esperto", "espetacular", "espirituoso", "esplêndido", "esplendoroso", "espontâneo", "estonteante", "eterno", "evoluído", "excelente", "excelso", "exemplar", "exímio", "experiente", "extraordinário", "extrovertido", "extremoso", "exuberante", "fiel", "forte", "franco", "frontal", "firme", "fantástico", "fenomenal", "fabuloso", "fascinante", "formidável", "fidedigno", "formoso", "fofo", "feliz", "felizardo", "faceiro", "fervoroso", "gentil", "generoso", "genuíno", "gracioso", "grande", "grandioso", "gênio", "genial", "gentleman", "glorioso", "glamoroso", "gigante", "gigantesco", "guerreiro", "gracejador", "galanteador", "garboso", "grato", "gratífico", "galhardo", "galhofeiro", "gaiato", "gaiteiro", "grácil", "guapo", "honesto", "honrado", "humano", "honroso", "honorável", "herói", "heroico", "hábil", "habilidoso", "hercúleo", "hilário", "hilariante", "hílare", "hospitaleiro", "humanitário", "hospedeiro", "humilde", "húmile", "humildoso", "inteligente", "importante", "íntegro", "incrível", "ilustre", "interessante", "impressionante", "ímpar", "ideal", "imponente", "imaginativo", "impecável", "irreverente", "irresistível", "inigualável", "imparcial", "idôneo", "independente", "inspirador", "interventivo", "intuitivo", "intenso", "intelectual", "instruído", "imortal", "impávido", "iluminado", "imaculado", "idealista", "idílico", "idilista", "imparável", "inabalável", "incansável", "imbatível", "invencível", "insubmisso", "insubornável", "invulnerável", "incorruptível", "incorrupto", "imprescindível", "indispensável", "intemerato", "justo", "jovem", "jovial", "joia", "jeitoso", "jubilante", "jubiloso", "justiceiro", "jucundo", "leal", "legal", "lindo", "livre", "lutador", "louvável", "laudável", "legítimo", "lúcido", "lisonjeiro", "loquaz", "liberal", "liberto", "lícito", "líder", "letrado", "laborioso", "lançado", "lesto", "ledo", "lauto", "maravilhoso", "magnifico", "magnânimo", "majestoso", "magnificente", "maior", "melhor", "máximo", "merecedor", "maneiro", "modesto", "módico", "mavioso", "motivado", "marcante", "mágico", "magno", "magistral", "maestral", "meritório", "moderno", "moderado", "maduro", "meticuloso", "minucioso", "metódico", "notável", "nobre", "normal", "natural", "novo", "naturista", "obediente", "objetivo", "obsequioso", "observador", "obstinado", "oficioso", "operante", "oportuno", "ordeiro", "organizado", "original", "otimista", "ótimo", "pacato", "paciente", "pacificador", "pacífico", "parceiro", "parcimonioso", "perfeito", "perito", "perseverante", "persistente", "perspicaz", "pertinaz", "piedoso", "pioneiro", "poderoso", "poderoso", "polido", "ponderado", "pontual", "porreiro", "porreta", "possante", "potente", "prazenteiro", "preparado", "prestativo", "prestável", "prestigioso", "prevenido", "primoroso", "príncipe", "prócere", "prodígio", "prodigioso", "proeminente", "proficiente", "protetor", "provecto", "prudente", "pudibundo", "pudico", "pujante", "pulcro", "querido", "qualificado", "responsável", "respeitável", "respeitador", "respeitado", "respeitoso", "realizado", "renomado", "resistente", "resoluto", "resolvido", "resiliente", "robusto", "romântico", "risonho", "ridente", "radiante", "resplandecente", "reluzente", "refinado", "racional", "realista", "refletido", "relaxado", "receptivo", "reconhecido", "rápido", "simpático", "sábio", "sincero", "sensato", "sensacional", "seguro", "sorridente", "sossegado", "sublime", "solícito", "solidário", "sereno", "sensível", "sedutor", "sagaz", "saudável", "singular", "sociável", "sofisticado", "sério", "sexy", "sonhador", "santo", "são", "sentimental", "sapeca", "serelepe", "sabedor", "sadio", "talentoso", "ternurento", "terno", "tranquilo", "transparente", "tolerável", "triunfal", "triunfante", "tranquilizador", "único", "uno", "urbano", "unificador", "ultrafantástico", "ultracompetente", "ultraconfiante", "ultra-honesto", "ultracorreto", "ultra-autônomo", "ultraindependente", "ultranatural", "ultrarromântico", "ultra-humano", "ultracivilizado", "ultradivino", "ultramoderno", "verdadeiro", "valente", "valioso", "valoroso", "vencedor", "verídico", "venerável", "venturoso", "vistoso", "virtuoso", "versado", "versátil", "visionário", "vitorioso", "veemente", "venerado", "verossímil", "vanguardista", "venusto", "vetusto", "valido", "veloz", "viril", "varonil", "veraz", "vero", "verboso", "vibrante", "vigoroso", "viçoso", "verdejante", "vívido", "vivaço", "vivo", "vivaz", "vital", "vigilante", "zeloso", "zen", "zelador"]
                self.mensagem = "Diz que Bolsonaro é %s" %(azbonsonaro[i])
                chat_box.send_keys(self.mensagem)
                botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
                botao_enviar.click()



# Essa e a funcao que vai chamar a funcao para enviar as mensagens, nas modificacoes que eu fiz estou enviando
# 590 mensagens diferentes por vez, nesse range(5) estou definindo que sera 5 x 590 ou seja 2950 mensagens.

bot = WhatsappBot()
for x in range(5):
    bot.EnviarMensagens()
