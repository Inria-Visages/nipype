# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..specialized import ACPCTransform


def test_ACPCTransform_inputs():
    input_map = dict(
        acpc=dict(argstr='--acpc %s...', ),
        args=dict(argstr='%s', ),
        debugSwitch=dict(argstr='--debugSwitch ', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        midline=dict(argstr='--midline %s...', ),
        outputTransform=dict(
            argstr='--outputTransform %s',
            hash_files=False,
        ),
    )
    inputs = ACPCTransform.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_ACPCTransform_outputs():
    output_map = dict(outputTransform=dict(extensions=None, ), )
    outputs = ACPCTransform.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
