from nipype.interfaces.anima import utils
from nipype.interfaces.base import (
    File
)
import os


def test_CropImage():
    ci = utils.CropImage()
    assert ci.cmd == 'animaCropImage'

    ci.inputs.in_file = 'nipype/testing/data/tpm_00.nii.gz'
    ci.inputs.out_file = 'nipype/testing/data/tpm_00_cropped.nii.gz'

    results = ci.run()

    assert os.path.abspath(results.outputs.out_file) == os.path.abspath(ci.inputs.out_file)
    os.remove(os.path.abspath(results.outputs.out_file))