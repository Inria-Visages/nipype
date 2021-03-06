# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..segmentation import DenoiseImage


def test_DenoiseImage_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        dimension=dict(argstr='-d %d', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        input_image=dict(
            argstr='-i %s',
            extensions=None,
            mandatory=True,
        ),
        noise_image=dict(
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=['input_image'],
            name_template='%s_noise',
        ),
        noise_model=dict(
            argstr='-n %s',
            usedefault=True,
        ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        output_image=dict(
            argstr='-o %s',
            extensions=None,
            hash_files=False,
            keep_extension=True,
            name_source=['input_image'],
            name_template='%s_noise_corrected',
        ),
        save_noise=dict(
            mandatory=True,
            usedefault=True,
            xor=['noise_image'],
        ),
        shrink_factor=dict(
            argstr='-s %s',
            usedefault=True,
        ),
        verbose=dict(argstr='-v', ),
    )
    inputs = DenoiseImage.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_DenoiseImage_outputs():
    output_map = dict(
        noise_image=dict(extensions=None, ),
        output_image=dict(extensions=None, ),
    )
    outputs = DenoiseImage.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
