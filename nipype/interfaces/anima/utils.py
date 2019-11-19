# -*- coding: utf-8 -*-
"""The anima utils module provides basic functions for interfacing with anima
   utility functions.
"""

from __future__ import (print_function, division, unicode_literals,
                        absolute_import)

from nipype.interfaces.base import (
    TraitedSpec,
    BaseInterfaceInputSpec,
    BaseInterface,
    CommandLineInputSpec,
    CommandLine,
    InputMultiPath,
    File,
    traits
)

import os


class CropImageInputSpec(CommandLineInputSpec):
    def get_desc_size(dimension):
        return (
            'Size of ROI for the {}index dimension. '
            'The resulting croped image will go from {}index to {}size along the {}index axis. '
            'If 0 the dimension is collapsed.').format(
            dimension, dimension, dimension, dimension
        )

    def get_desc_index(dimension):
        return (
            'Start of ROI for the {}index dimension. '
            'The resulting croped image will go from {}index to {}size along the {}index axis.').format(
            dimension, dimension, dimension, dimension
        )

    in_file = File(exists=True, argstr='-i %s', mandatory=True,
                   desc='Input image to crop')
    out_file = File(argstr='-o %s', name_source=['in_file'], name_template='%s_cropped.nrrd', keep_extension=False,
                    desc='Output cropped image')

    tsize = traits.Int(argstr='-T %d', desc=get_desc_size('t'))
    tindex = traits.Int(argstr='-t %d', desc=get_desc_index('t'))
    zsize = traits.Int(argstr='-Z %d', desc=get_desc_size('z'))
    zindex = traits.Int(argstr='-z %d', desc=get_desc_index('z'))
    ysize = traits.Int(argstr='-Y %d', desc=get_desc_size('y'))
    yindex = traits.Int(argstr='-y %d', desc=get_desc_index('y'))
    xsize = traits.Int(argstr='-X %d', desc=get_desc_size('x'))
    xindex = traits.Int(argstr='-x %d', desc=get_desc_index('x'))
    bounding_box = traits.File(
        exists=True,
        argstr='-m %s',
        desc='A mask used instead of other arguments to determine a bounding box',
        xor=['tsize', 'tindex', 'zsize', 'zindex', 'ysize', 'yindex', 'xsize', 'xindex']
    )


class CropImageOutputSpec(TraitedSpec):
    out_file = File(desc='Cropped Image', exists = True)


class CropImage(CommandLine):
    _cmd = 'animaCropImage'

    input_spec = CropImageInputSpec
    output_spec = CropImageOutputSpec

    def _list_outputs(self):
        outputs = super(CropImage, self)._list_outputs()
        return outputs


class ConvertImageInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True, desc='input image.')
    out_file = File(argstr='-o %s', desc='output image', mandatory=False)
    space_reference_image = File(argstr='-s %s', mandatory=False, desc='Image used as space reference.')
    gradients = File(argstr='-g %s', mandatory=False, desc='input gradients.')
    reorient = traits.Str('', argstr='-R %s', usedefault=False, desc='Reorient the image in \'AXIAL\' or \'CORONAL\' or \'SAGITTAL\' direction.')
    information = traits.Bool(True, argstr='-I', usedefault=True, desc='Get image informations')


class ConvertImageOutputSpec(TraitedSpec):
    out_file = File(desc='Converted Image', exists = True)


class ConvertImage(CommandLine):
    _cmd = 'animaConvertImage'

    input_spec = ConvertImageInputSpec
    output_spec = ConvertImageOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs


class ImageArithmeticInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                      desc='input image')
    out_file = File(argstr='-o %s', desc='output image',
                    name_source=['input_file'], name_template='%s_arithmetic.nrrd', keep_extension=False)
    add_file = File(exists=True, argstr='-a %s',
                    desc='input added image')
    subtract_file = File(exists=True, argstr='-s %s',
                         desc='input subtracted image')
    multiply_file = File(exists=True, argstr='-m %s',
                         desc='input multiplied image')
    divide_file = File(exists=True, argstr='-d %s',
                       desc='input divided image')

    add_constant = traits.Float(0.0, argstr='-A %f',
                                usedefault=True, desc='added constant')
    subtract_constant = traits.Float(0.0, argstr='-S %f',
                                     usedefault=True, desc='subtracted constant')
    multiply_constant = traits.Float(1.0, argstr='-M %f',
                                     usedefault=True, desc='multiplied constant')
    divide_constant = traits.Float(1.0, argstr='-D %f',
                                   usedefault=True, desc='divided constant')
    power_constant = traits.Float(1.0, argstr='-P %f',
                                  usedefault=True, desc='power constant')

    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class ImageArithmeticOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output image')


class ImageArithmetic(CommandLine):
    _cmd = 'animaImageArithmetic'
    input_spec = ImageArithmeticInputSpec
    output_spec = ImageArithmeticOutputSpec

    def _list_outputs(self):
        outputs = super(ImageArithmetic, self)._list_outputs()
        return outputs


class AverageImagesInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                       desc='input file list as text file')
    mask_file = File(exists=True, argstr='-m %s',
                      desc='masks file list as text file')
    out_file = File(argstr='-o %s', desc='output image',
                    name_source=['input_file'], name_template='%s_average.nrrd', keep_extension=False)


class AverageImagesOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output image')


class AverageImages(CommandLine):
    _cmd = 'animaAverageImages'
    input_spec = AverageImagesInputSpec
    output_spec = AverageImagesOutputSpec

    def _list_outputs(self):
        outputs = super(ImageArithmetic, self)._list_outputs()
        return outputs


class MaskImageInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                      desc='input file')
    mask_file = File(exists=True, argstr='-m %s', mandatory=True,
                     desc='mask file')
    out_file = File(argstr='-o %s', desc='output image',
                    name_source=['input_file'], name_template='%s_masked.nrrd', keep_extension=False)


class MaskImageOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output image')


class MaskImage(CommandLine):
    _cmd = 'animaMaskImage'
    input_spec = MaskImageInputSpec
    output_spec = MaskImageOutputSpec

    def _list_outputs(self):
        outputs = super(MaskImage, self)._list_outputs()
        return outputs


class CreateFilesListInputSpec(BaseInterfaceInputSpec):
    input_files = InputMultiPath(File(exists=True), mandatory=True,
                                 desc='Files to be included in file list')
    out_file = File(desc='Text file containing the file list',
                    name_source=['input_files'], name_template='%s_list.txt', keep_extension=False)


class CreateFilesListOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Text file containing the file list')


class CreateFilesList(BaseInterface):
    input_spec = CreateFilesListInputSpec
    output_spec = CreateFilesListOutputSpec

    def _run_interface(self, runtime):
        files_list = self.inputs.input_files
        text_file = open(self.inputs.out_file, "w")

        for fname in files_list:
            text_file.write("%s\n" % fname)

        text_file.close()
        return runtime

    def _list_outputs(self):
        outputs = super(CreateFilesList, self)._list_outputs()
        return outputs
