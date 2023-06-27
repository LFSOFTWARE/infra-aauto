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
                 permite_mais_produto_pulmao, razao_social, regiao_armazenagem,	tipo_armazenagem, tipo_recebimento):

        self.setor_armazenagem = setor_armazenagem
        self.codigo_integracao = codigo_integracao
        self.area_setor = area_setor
        self.tipo_setor = tipo_setor
        self.permite_expedicao_produto = permite_expedicao_produto
        self.permite_mais_produto_pulmao = permite_mais_produto_pulmao
        self.razao_social = razao_social
        self.regiao_armazenagem = regiao_armazenagem
        self.tipo_armazenagem = tipo_armazenagem
        self.tipo_recebimento = tipo_recebimento


class DataFtp:
    def __init__(self, importacao, backup_importacao, exportacao, backup_exportacao, erro):
        self.importacao = importacao
        self.backup_importacao = backup_importacao
        self.exportacao = exportacao
        self.backup_exportacao = backup_exportacao
        self.erro = erro


class DataOr:
    def __init__(self, codigo_tipo_recebimento,	codigo_doca, placa_veiculo, quantidade_volume_recebido,	intervalo_integracao):
        self.codigo_tipo_recebimento = codigo_tipo_recebimento
        self.codigo_doca = codigo_doca
        self.placa_veiculo = placa_veiculo
        self.quantidade_volume_recebido = quantidade_volume_recebido
        self.intervalo_integracao = intervalo_integracao


class TipoPedidoI:
    def __init__(self, codigo_integracao, descricao, setor):
        self.codigo_integracao = codigo_integracao
        self.descricao = descricao
        self.setor = setor



class PadraoIntegracaoI:
    def __init__(self, tipo_palete_completo, tipo_palete_incompleto, tipo_palete_sobra, tipo_palete_unidade, quantidade_maxima_picking):
        
        self.tipo_palete_completo = tipo_palete_completo
        self.tipo_palete_incompleto = tipo_palete_incompleto
        self.tipo_palete_sobra = tipo_palete_sobra
        self.tipo_palete_unidade = tipo_palete_unidade
        self.quantidade_maxima_picking = quantidade_maxima_picking
