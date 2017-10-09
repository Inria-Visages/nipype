# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..registration import Paint


def test_Paint_inputs():
    input_map = dict(args=dict(argstr='%s',
    ),
    averages=dict(argstr='-a %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_surf=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    out_file=dict(argstr='%s',
    hash_files=False,
    keep_extension=False,
    name_source=['in_surf'],
    name_template='%s.avg_curv',
    position=-1,
    ),
    subjects_dir=dict(),
    template=dict(argstr='%s',
    mandatory=True,
    position=-3,
    ),
    template_param=dict(),
    terminal_output=dict(deprecated='1.0.0',
    nohash=True,
    ),
    )
    inputs = Paint.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Paint_outputs():
    output_map = dict(out_file=dict(),
    )
    outputs = Paint.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
