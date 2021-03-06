# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..regutils import RegMeasure


def test_RegMeasure_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        flo_file=dict(
            argstr='-flo %s',
            extensions=None,
            mandatory=True,
        ),
        measure_type=dict(
            argstr='-%s',
            mandatory=True,
        ),
        omp_core_val=dict(
            argstr='-omp %i',
            usedefault=True,
        ),
        out_file=dict(
            argstr='-out %s',
            extensions=None,
            name_source=['flo_file'],
            name_template='%s',
        ),
        ref_file=dict(
            argstr='-ref %s',
            extensions=None,
            mandatory=True,
        ),
    )
    inputs = RegMeasure.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_RegMeasure_outputs():
    output_map = dict(out_file=dict(extensions=None, ), )
    outputs = RegMeasure.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
