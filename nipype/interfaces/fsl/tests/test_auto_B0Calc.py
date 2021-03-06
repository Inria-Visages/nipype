# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..possum import B0Calc


def test_B0Calc_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        chi_air=dict(
            argstr='--chi0=%e',
            usedefault=True,
        ),
        compute_xyz=dict(
            argstr='--xyz',
            usedefault=True,
        ),
        delta=dict(
            argstr='-d %e',
            usedefault=True,
        ),
        directconv=dict(
            argstr='--directconv',
            usedefault=True,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        extendboundary=dict(
            argstr='--extendboundary=%0.2f',
            usedefault=True,
        ),
        in_file=dict(
            argstr='-i %s',
            extensions=None,
            mandatory=True,
            position=0,
        ),
        out_file=dict(
            argstr='-o %s',
            extensions=None,
            name_source=['in_file'],
            name_template='%s_b0field',
            output_name='out_file',
            position=1,
        ),
        output_type=dict(),
        x_b0=dict(
            argstr='--b0x=%0.2f',
            usedefault=True,
            xor=['xyz_b0'],
        ),
        x_grad=dict(
            argstr='--gx=%0.4f',
            usedefault=True,
        ),
        xyz_b0=dict(
            argstr='--b0x=%0.2f --b0y=%0.2f --b0=%0.2f',
            xor=['x_b0', 'y_b0', 'z_b0'],
        ),
        y_b0=dict(
            argstr='--b0y=%0.2f',
            usedefault=True,
            xor=['xyz_b0'],
        ),
        y_grad=dict(
            argstr='--gy=%0.4f',
            usedefault=True,
        ),
        z_b0=dict(
            argstr='--b0=%0.2f',
            usedefault=True,
            xor=['xyz_b0'],
        ),
        z_grad=dict(
            argstr='--gz=%0.4f',
            usedefault=True,
        ),
    )
    inputs = B0Calc.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_B0Calc_outputs():
    output_map = dict(out_file=dict(extensions=None, ), )
    outputs = B0Calc.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
