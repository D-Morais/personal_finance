import unicodedata
import re
from difflib import get_close_matches
from spellchecker import SpellChecker

spell = SpellChecker(language="pt")


KEYWORDS = {

    # ================= DESPESAS ================= #
    "Alimentacao": {
        "ifood": 5,
        "uber eats": 4,
        "delivery": 4,
        "restaurante": 4,
        "lanchonete": 3,
        "hamburguer": 3,
        "pizza": 3,
        "pastel": 3,
        "padaria": 3,
        "cafeteria": 3,
        "cafe": 2,
        "almoco": 4,
        "jantar": 4,
        "comida": 3,
        "marmita": 3,
        "self service": 3,
        "sorveteria": 2,
        "acai": 2,
        "fast food": 3,
        "lanche": 2,
        "xis": 2,
        "cachorro quente": 3,
        "refeicao": 3
    },

    "Transporte": {
        "uber": 5,
        "99": 5,
        "taxi": 4,
        "onibus": 4,
        "metro": 4,
        "trem": 3,
        "combustivel": 4,
        "gasolina": 4,
        "etanol": 3,
        "diesel": 3,
        "estacionamento": 3,
        "pedagio": 3,
        "passagem": 3,
        "bilhete": 2,
        "aluguel carro": 3,
        "manutencao veiculo": 3
    },

    "Moradia": {
        "aluguel": 5,
        "condominio": 4,
        "energia": 4,
        "luz": 4,
        "agua": 4,
        "internet": 4,
        "telefone": 3,
        "vivo": 2,
        "claro": 2,
        "tim": 2,
        "iptu": 3,
        "gas": 3,
        "tv a cabo": 2,
        "manutencao casa": 3
    },

    "Saude": {
        "farmacia": 4,
        "remedio": 4,
        "medicamento": 4,
        "consulta": 4,
        "medico": 4,
        "dentista": 4,
        "hospital": 5,
        "plano de saude": 5,
        "exame": 3,
        "laboratorio": 3,
        "psicologo": 3,
        "fisioterapia": 3
    },

    "Lazer": {
        "cinema": 4,
        "netflix": 3,
        "spotify": 3,
        "youtube premium": 4,
        "prime video": 3,
        "hbo": 3,
        "disney": 3,
        "bar": 3,
        "balada": 3,
        "viagem": 4,
        "hotel": 4,
        "airbnb": 4,
        "show": 3,
        "evento": 3,
        "ingresso": 3,
        "futebol": 3,
        "jogo": 2
    },

    "Compras": {
        "mercado": 4,
        "supermercado": 4,
        "atacadao": 3,
        "carrefour": 3,
        "extra": 3,
        "shopping": 3,
        "compras": 2,
        "loja": 2,
        "roupa": 3,
        "calcado": 3,
        "tenis": 3,
        "camisa": 3,
        "eletrodomestico": 3,
        "celular": 3,
        "eletronico": 3
    },

    "Educacao": {
        "curso": 4,
        "faculdade": 5,
        "mensalidade": 4,
        "escola": 5,
        "udemy": 3,
        "alura": 3,
        "ebook": 2,
        "livro": 2,
        "material escolar": 3,
        "pos graduacao": 4
    },

    # ================= RENDAS ================= #
    "Salario": {
        "salario": 5,
        "pagamento": 4,
        "folha pagamento": 5,
        "pro labore": 4,
        "remuneracao": 4,
        "holerite": 5
    },

    "Freelance": {
        "freelance": 5,
        "projeto": 3,
        "servico": 3,
        "pix cliente": 4,
        "pagamento cliente": 4,
        "contrato": 3
    },

    "Investimentos": {
        "dividendo": 5,
        "rendimento": 4,
        "juros": 4,
        "tesouro direto": 4,
        "cdb": 4,
        "fii": 5,
        "acao": 4,
        "lucro investimento": 5
    },

    "Extras": {
        "comissao": 4,
        "bonus": 4,
        "premio": 4,
        "cashback": 3,
        "reembolso": 3,
        "venda": 3
    }
}


# ---------- NORMALIZAÇÃO ----------
def normalizar_texto(texto: str):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = texto.encode("ascii", "ignore").decode("utf-8")
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto


# ---------- CORREÇÃO ORTOGRÁFICA ----------
def ortografia_correta(texto):
    palavras = texto.split()
    corrigida = []

    for palavra in palavras:
        palavra_corrigida = spell.correction(palavra)
        corrigida.append(palavra_corrigida if palavra_corrigida else palavra)

    return " ".join(corrigida)


# ---------- CORREÇÃO POR SIMILARIDADE ----------
def corrigir_por_similaridade(palavra, todas_keywords):
    matches = get_close_matches(palavra, todas_keywords, n=1, cutoff=0.75)

    return matches[0] if matches else palavra


def calcular_score(texto: str, keywords_categoria: dict) -> int:
    score = 0
    for palavra, peso in keywords_categoria.items():
        if palavra in texto:
            score += peso

    return score


def sugestao_categoria(descricao: str):
    desc = normalizar_texto(descricao)
    #print(desc_normalizado)
    #desc = ortografia_correta(desc_normalizado)
    # 3) lista palavras-chave
    todas_palavras = []
    for categoria in KEYWORDS.values():
        todas_palavras.extend(categoria.keys())

    tokens = desc.split()

    # 4) similaridade
    corrigido = [
        corrigir_por_similaridade(t, todas_palavras)
        for t in tokens
    ]

    texto_corrigido = " ".join(corrigido)

    scores = {}

    for categoria, palavras in KEYWORDS.items():
        score = 0
        for palavra, peso in palavras.items():
            if palavra in texto_corrigido:
                score += peso
        scores[categoria] = score

    melhor = max(scores, key=scores.get)

    if scores[melhor] == 0:
        return "Outros", 10

    return melhor, scores[melhor]
