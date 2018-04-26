from nipype.interfaces.anima import PyramidalBMRegistration
from nipype.interfaces.base import (
    File
)
import os


def test_PyramidalBMRegistrationI():
    i = PyramidalBMRegistration()
    assert i.cmd == 'animaPyramidalBMRegistration'

    i.inputs.moving_file = 'nipype/testing/data/tpm_00.nii.gz'
    i.inputs.reference_file = 'nipype/testing/data/tpm_00.nii.gz'
    i.inputs.out_file = 'nipype/testing/data/tpm_00_warped.nii.gz'
    i.inputs.out_transform_file = 'nipype/testing/data/tpm_00_warped.txt'

    results = i.run()

    assert os.path.abspath(results.outputs.out_file) == os.path.abspath(i.inputs.out_file)
    os.remove(os.path.abspath(results.outputs.out_file))
    assert os.path.abspath(results.outputs.out_transform_file) == os.path.abspath(i.inputs.out_transform_file)
    os.remove(os.path.abspath(results.outputs.out_transform_file))
