# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utilities import EMSegmentTransformToNewFormat


def test_EMSegmentTransformToNewFormat_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        inputMRMLFileName=dict(
            argstr='--inputMRMLFileName %s',
            extensions=None,
        ),
        outputMRMLFileName=dict(
            argstr='--outputMRMLFileName %s',
            hash_files=False,
        ),
        templateFlag=dict(argstr='--templateFlag ', ),
    )
    inputs = EMSegmentTransformToNewFormat.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_EMSegmentTransformToNewFormat_outputs():
    output_map = dict(outputMRMLFileName=dict(extensions=None, ), )
    outputs = EMSegmentTransformToNewFormat.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
