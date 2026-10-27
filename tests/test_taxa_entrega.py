from src.pedido import calcular_taxa_entrega


def test_taxa_de_cinco_reais_para_dois_km_e_pedido_de_cinquenta():
    taxa = calcular_taxa_entrega(2, 50)

    assert taxa == 5


def test_taxa_de_sete_reais_para_quatro_km_e_pedido_de_cinquenta():
    taxa = calcular_taxa_entrega(4, 50)

    assert taxa == 7
