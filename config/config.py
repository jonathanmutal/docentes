ASD = 'ASD'
PASD = 'PASD'
HA = 'HA'
PAA = 'PAA'
NOA = 'NOA'
JQA = 'JQA'
PBA = 'PBA'
BA = 'BA'
OT = 'OT'

SITUACION = [
    (ASD, 'Activo sin descuentos'),
    (PASD, 'Pendiente de alta sin descuentos'),
    (HA, 'Historico que aporto'),
    (PAA, 'Pendiente de alta que aporto'),
    (NOA, 'No afiliado que aporto'),
    (JQA, 'Jubilado que aporto'),
    (PBA, 'Pendiente de baja que aporto'),
    (BA, 'Baja que aporto'),
    (OT, 'Otra situación')
]

NONE = 'none'
HIST = 'hist'
BAJA = 'baja'
PEND_B = 'pend_b'
PEND_A = 'pend_a'
PASIVO = 'pasivo'
JUB = 'jub'
JUBA = 'juba'
ACTIVO = 'activo'
BECARIEA = 'becariea'
BECARIE = 'becarie'
CONTRATADEA = 'contratadea'
CONTRATADE = 'contratade'

STATE = [
    (NONE, 'No afiliado'),
    (HIST, 'Histórico'),
    (BAJA, 'Desafiliado'),
    (PEND_B, 'Pendiente de baja'),
    (PEND_A, 'Pendiente de alta'),
    (PASIVO, 'No cotizante'),
    (JUB, 'Jubilado'),
    (JUBA, 'Jubilado Activo'),
    (ACTIVO, 'Activo'),
    (BECARIEA, 'Becarie cotizante'),
    (BECARIE, 'Becarie no cotizante'),
    (CONTRATADEA, 'Contratade activo'),
    (CONTRATADE, 'Contratade no cotizante')
]

## Sera usado para gestion_de_cambios_wizard, en vez de tener muchos ifs.
DOCENTE_APORTO = {
    HIST: HA,
    BAJA: BA,
    PEND_B: PBA,
    PEND_A: PAA,
    JUB: JQA,
    NONE: NOA
}

DOCENTE_NO_APORTO = {
    ACTIVO: ASD,
    PEND_A: PASD
}