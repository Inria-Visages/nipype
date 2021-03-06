# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..parcellation import Parcellate


def test_Parcellate_inputs():
    input_map = dict(
        dilation=dict(usedefault=True, ),
        freesurfer_dir=dict(),
        out_roi_file=dict(
            extensions=None,
            genfile=True,
        ),
        parcellation_name=dict(usedefault=True, ),
        subject_id=dict(mandatory=True, ),
        subjects_dir=dict(),
    )
    inputs = Parcellate.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Parcellate_outputs():
    output_map = dict(
        aseg_file=dict(extensions=None, ),
        cc_unknown_file=dict(extensions=None, ),
        dilated_roi_file_in_structural_space=dict(extensions=None, ),
        ribbon_file=dict(extensions=None, ),
        roi_file=dict(extensions=None, ),
        roi_file_in_structural_space=dict(extensions=None, ),
        roiv_file=dict(extensions=None, ),
        white_matter_mask_file=dict(extensions=None, ),
    )
    outputs = Parcellate.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
