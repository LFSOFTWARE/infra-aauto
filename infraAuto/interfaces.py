class Empresa:
    def __init__(self, razao_social, fantasia, cnpj, tipo_inscricao, inscricao_estadual,
                 tipo, tipo_danfe, emite_nf, cep, numero, complemento,
                 entrega, cobranca, endereco_fiscal, impressao, armazem,
                 integracao_via_servico_rest, setor_armazenagem, codigo_integracao, area_setor,
                 tipo_setor, permite_expedicao_produto, permite_mais_produto_pulmao):

        self.razao_social = razao_social
        self.fantasia = fantasia
        self.cnpj = cnpj
        self.tipo_inscricao = tipo_inscricao
        self.inscricao_estadual = inscricao_estadual
        self.tipo = tipo
        self.tipo_danfe = tipo_danfe
        self.emite_nf = emite_nf
        self.cep = cep
        self.numero = numero
        self.complemento = complemento
        self.entrega = entrega
        self.cobranca = cobranca
        self.endereco_fiscal = endereco_fiscal
        self.impressao = impressao
        self.armazem = armazem
        self.integracao_via_servico_rest = integracao_via_servico_rest


class SetorI:
    def __init__(self, setor_armazenagem, codigo_integracao,
                 area_setor, tipo_setor, permite_expedicao_produto,
                 permite_mais_produto_pulmao, razao_social):

        self.setor_armazenagem = setor_armazenagem
        self.codigo_integracao = codigo_integracao
        self.area_setor = area_setor
        self.tipo_setor = tipo_setor
        self.permite_expedicao_produto = permite_expedicao_produto
        self.permite_mais_produto_pulmao = permite_mais_produto_pulmao
        self.razao_social = razao_social


class DataFtp:
    def __init__(self, importacao, backup_importacao, exportacao, backup_exportacao, erro):
        self.importacao = importacao
        self.backup_importacao = backup_importacao
        self.exportacao = exportacao
        self.backup_exportacao = backup_exportacao
        self.erro = erro
    