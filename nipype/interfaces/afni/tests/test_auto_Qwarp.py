# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Qwarp


def test_Qwarp_inputs():
    input_map = dict(Qfinal=dict(argstr='-Qfinal',
    ),
    Qonly=dict(argstr='-Qonly',
    ),
    allsave=dict(argstr='-allsave',
    xor=['nopadWARP', 'duplo', 'plusminus'],
    ),
    args=dict(argstr='%s',
    ),
    ballopt=dict(argstr='-ballopt',
    xor=['workhard', 'boxopt'],
    ),
    base_file=dict(argstr='-base %s',
    copyfile=False,
    mandatory=True,
    ),
    baxopt=dict(argstr='-boxopt',
    xor=['workhard', 'ballopt'],
    ),
    blur=dict(argstr='-blur %s',
    ),
    duplo=dict(argstr='-duplo',
    xor=['gridlist', 'maxlev', 'inilev', 'iniwarp', 'plusminus', 'allsave'],
    ),
    emask=dict(argstr='-emask %s',
    copyfile=False,
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    expad=dict(argstr='-expad %d',
    xor=['nopadWARP'],
    ),
    gridlist=dict(argstr='-gridlist %s',
    copyfile=False,
    xor=['duplo', 'plusminus'],
    ),
    hel=dict(argstr='-hel',
    xor=['nmi', 'mi', 'lpc', 'lpa', 'pear'],
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='-source %s',
    copyfile=False,
    mandatory=True,
    ),
    inilev=dict(argstr='-inlev %d',
    xor=['duplo'],
    ),
    iniwarp=dict(argstr='-iniwarp %s',
    xor=['duplo'],
    ),
    iwarp=dict(argstr='-iwarp',
    xor=['plusminus'],
    ),
    lpa=dict(argstr='-lpa',
    xor=['nmi', 'mi', 'lpc', 'hel', 'pear'],
    ),
    lpc=dict(argstr='-lpc',
    position=-2,
    xor=['nmi', 'mi', 'hel', 'lpa', 'pear'],
    ),
    maxlev=dict(argstr='-maxlev %d',
    position=-1,
    xor=['duplo'],
    ),
    mi=dict(argstr='-mi',
    xor=['mi', 'hel', 'lpc', 'lpa', 'pear'],
    ),
    minpatch=dict(argstr='-minpatch %d',
    ),
    nmi=dict(argstr='-nmi',
    xor=['nmi', 'hel', 'lpc', 'lpa', 'pear'],
    ),
    noXdis=dict(argstr='-noXdis',
    ),
    noYdis=dict(argstr='-noYdis',
    ),
    noZdis=dict(argstr='-noZdis',
    ),
    noneg=dict(argstr='-noneg',
    ),
    nopad=dict(argstr='-nopad',
    ),
    nopadWARP=dict(argstr='-nopadWARP',
    xor=['allsave', 'expad'],
    ),
    nopenalty=dict(argstr='-nopenalty',
    ),
    nowarp=dict(argstr='-nowarp',
    ),
    noweight=dict(argstr='-noweight',
    ),
    num_threads=dict(nohash=True,
    usedefault=True,
    ),
    out_file=dict(argstr='-prefix %s',
    genfile=True,
    name_source=['in_file'],
    name_template='%s_QW',
    ),
    out_weight_file=dict(argstr='-wtprefix %s',
    ),
    outputtype=dict(),
    overwrite=dict(argstr='-overwrite',
    ),
    pblur=dict(argstr='-pblur %s',
    ),
    pear=dict(argstr='-pear',
    ),
    penfac=dict(argstr='-penfac %f',
    ),
    plusminus=dict(argstr='-plusminus',
    xor=['duplo', 'allsave', 'iwarp'],
    ),
    quiet=dict(argstr='-quiet',
    xor=['verb'],
    ),
    resample=dict(argstr='-resample',
    ),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    verb=dict(argstr='-verb',
    xor=['quiet'],
    ),
    wball=dict(argstr='-wball %s',
    ),
    weight=dict(argstr='-weight %s',
    ),
    wmask=dict(argstr='-wpass %s %f',
    ),
    workhard=dict(argstr='-workhard',
    xor=['boxopt', 'ballopt'],
    ),
    )
    inputs = Qwarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Qwarp_outputs():
    output_map = dict(base_warp=dict(),
    source_warp=dict(),
    warped_base=dict(),
    warped_source=dict(),
    weights=dict(),
    )
    outputs = Qwarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
