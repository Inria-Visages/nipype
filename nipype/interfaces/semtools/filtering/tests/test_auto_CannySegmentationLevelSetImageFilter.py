# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..featuredetection import CannySegmentationLevelSetImageFilter


def test_CannySegmentationLevelSetImageFilter_inputs():
    input_map = dict(
        advectionWeight=dict(argstr='--advectionWeight %f', ),
        args=dict(argstr='%s', ),
        cannyThreshold=dict(argstr='--cannyThreshold %f', ),
        cannyVariance=dict(argstr='--cannyVariance %f', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        initialModel=dict(
            argstr='--initialModel %s',
            extensions=None,
        ),
        initialModelIsovalue=dict(argstr='--initialModelIsovalue %f', ),
        inputVolume=dict(
            argstr='--inputVolume %s',
            extensions=None,
        ),
        maxIterations=dict(argstr='--maxIterations %d', ),
        outputSpeedVolume=dict(
            argstr='--outputSpeedVolume %s',
            hash_files=False,
        ),
        outputVolume=dict(
            argstr='--outputVolume %s',
            hash_files=False,
        ),
    )
    inputs = CannySegmentationLevelSetImageFilter.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_CannySegmentationLevelSetImageFilter_outputs():
    output_map = dict(
        outputSpeedVolume=dict(extensions=None, ),
        outputVolume=dict(extensions=None, ),
    )
    outputs = CannySegmentationLevelSetImageFilter.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
