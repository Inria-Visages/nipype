# -*- coding: utf-8 -*-
"""The anima registration module provides basic functions for interfacing with anima
   registration functions.
"""

from __future__ import (print_function, division, unicode_literals,
                        absolute_import)

from nipype.interfaces.base import (
    TraitedSpec,
    CommandLineInputSpec,
    CommandLine,
    File,
    traits
)

import os


class EddyCurrentCorrectionInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True, desc='input DW image')
    input_gradient_file = File(argstr='-I %s', desc='input gradients', mandatory=True)
    out_file = File(argstr='-o %s', desc='output (registered) image',
                    name_source=['input_file'], name_template='%s_ec_corrected.nrrd', keep_extension=False)
    out_gradients_file = File(argstr='-O %s', desc='output gradients',
                              name_source=['input_gradient_file'], name_template='%s_corr.bvec', keep_extension=False)

    metric_type = traits.Enum(0, 1, 2, argstr='--metric %d',
                              usedefault=True,
                              desc='Similarity metric between blocks (0: squared correlation coefficient, \
                                    1: correlation coefficient, 2: mean squares')
    block_spacing = traits.Int(5, argstr='--sp %d', usedefault=True,
                               desc='block spacing')
    block_search_radius = traits.Int(2, argstr='--sr %d', usedefault=True,
                                     desc='Search radius in pixels (exhaustive search window, rho start for bobyqa')
    symmetric_registration = traits.Enum(0, 1, 2, argstr='--sym-reg %d',
                                         usedefault=True,
                                         desc='Registration symmetry type, 0: asymmetric, 1: symmetric, 2: kissing')

    reference_index = traits.Int(0, argstr='-b %d', usedefault=True,
                                     desc='Reference image index')
    phase_encoding_direction = traits.Enum(1, 2, 0, argstr='-d %d', usedefault=True,
                                     desc='Phase encoding direction')

    pyramid_levels = traits.Int(3, argstr="-p %d", usedefault=True,
                                desc='number of pyramid levels')
    last_pyramid_level = traits.Int(0, argstr='-l %d', usedefault=True,
                                    desc='index of the last pyramid level explored')
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class EddyCurrentCorrectionOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output (registered) image')
    out_gradients_file = File(exists=True, desc='output gradients')


class EddyCurrentCorrection(CommandLine):
    _cmd = 'animaEddyCurrentCorrection'
    input_spec = EddyCurrentCorrectionInputSpec
    output_spec = EddyCurrentCorrectionOutputSpec

    def _list_outputs(self):
        outputs = super(EddyCurrentCorrection, self)._list_outputs()
        return outputs


class DistortionCorrectionInputSpec(CommandLineInputSpec):
    backward_file = File(exists=True, argstr='-b %s', mandatory=True, desc='Backward image')
    forward_file = File(exists=True, argstr='-f %s', mandatory=True, desc='Forward image')
    out_file = File(argstr='-o %s', desc='Output vector field',
                    name_source=['backward_file'], name_template='%s_dist_corr_tr.nrrd', keep_extension=False)

    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True, desc='number of threads to run on')
    gaussian_smoothing_sigma = traits.Float(2, argstr='-s %f', usedefault=True, desc='gaussian smoothing sigma')
    phase_encoding_correction = traits.Int(1, argstr='-d %d', usedefault=True,
                                           desc='Phase encoding direction')


class DistortionCorrectionOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Output vector field')


class DistortionCorrection(CommandLine):
    _cmd = 'animaDistortionCorrection'
    input_spec = DistortionCorrectionInputSpec
    output_spec = DistortionCorrectionOutputSpec

    def _list_outputs(self):
        outputs = super(DistortionCorrection, self)._list_outputs()
        return outputs


class BMDistortionCorrectionInputSpec(CommandLineInputSpec):
    backward_file = File(exists=True, argstr='-b %s', mandatory=True, desc='Backward image')
    forward_file = File(exists=True, argstr='-f %s', mandatory=True, desc='Forward image')
    out_file = File(argstr='-o %s', desc='Output corrected image',
                    name_source=['backward_file'], name_template='%s_dist_corr.nrrd', keep_extension=False)
    out_transform_file = File(argstr='-O %s', desc='Output vector field',
                              name_source=['backward_file'], name_template='%s_dist_corr_tr.nrrd',
                              keep_extension=False)

    metric_type = traits.Enum(0, 1, 2, argstr='--metric %d',
                              usedefault=True,
                              desc='Similarity metric between blocks (0: correlation coefficient, 1: \
                              squared correlation coefficient, 2: mean squares, default: 1)')
    block_spacing = traits.Int(2, argstr='--sp %d', usedefault=True,
                               desc='block spacing')
    block_search_radius = traits.Int(2, argstr='--sr %d', usedefault=True,
                                     desc='Search radius in pixels (exhaustive search window, rho start for bobyqa')
    minimal_block_std = traits.Float(10.0, argstr='-s %f', usedefault=True,
                                     desc='Threshold on block standard deviation')
    phase_encoding_direction = traits.Enum(1, 2, 0, argstr='-d %d', usedefault=True,
                                     desc='Phase encoding direction')
    pyramid_levels = traits.Int(3, argstr="-p %d", usedefault=True,
                                desc='number of pyramid levels')
    last_pyramid_level = traits.Int(0, argstr='-l %d', usedefault=True,
                                    desc='index of the last pyramid level explored')
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class BMDistortionCorrectionOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Output corrected image')
    out_transform_file = File(exists=True, desc='Output correction vector field')


class BMDistortionCorrection(CommandLine):
    _cmd = 'animaBMDistortionCorrection'
    input_spec = BMDistortionCorrectionInputSpec
    output_spec = BMDistortionCorrectionOutputSpec

    def _list_outputs(self):
        outputs = super(BMDistortionCorrection, self)._list_outputs()
        return outputs


class ApplyDistortionCorrectionInputSpec(CommandLineInputSpec):
    backward_file = File(argstr='-b %s', desc='Backward image')
    forward_file = File(argstr='-f %s', mandatory=True, desc='Forward image')
    out_file = File(argstr='-o %s', desc='Output vector field',
                    name_source=['forward_file'], name_template='%s_corr_applied.nrrd', keep_extension=False)
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True, desc='number of threads to run on')
    transformation_real_coordinates_out_file = File(argstr='-O %s', desc='Transformation in real coordinates')
    distortion_correction_field = traits.Str('', argstr='-t %s', usedefault=False, desc='distortion correction field')
    invert = traits.Bool(argstr='-I', desc='If set, invert the input field (after reverting if R option is on')
    reverse = traits.Bool(argstr='-R', desc='If set, apply the opposite of the input field to the forward image')
    voxel = traits.Bool(argstr='-V', desc='If set, the input correction field is assumed to be in voxel coordinates')


class ApplyDistortionCorrectionOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Output image (corrected)')
    transformation_real_coordinates_out_file = File(exists=True, desc='Output vector field in real coordinates')


class ApplyDistortionCorrection(CommandLine):
    _cmd = 'animaApplyDistortionCorrection'
    input_spec = ApplyDistortionCorrectionInputSpec
    output_spec = ApplyDistortionCorrectionOutputSpec

    def _list_outputs(self):
        outputs = super(ApplyDistortionCorrection, self)._list_outputs()
        return outputs


class DTIEstimatorInputSpec(CommandLineInputSpec):
    dwi_volume_file = File(argstr='-i %s', mandatory=True, desc='DWI volume')
    b_values_file = File(argstr='-b %s', mandatory=True, desc='b values')
    gradients_file = File(argstr='-g %s', mandatory=True, desc='Input gradients')
    corruption_mask_file = File(argstr='-m %s', desc='computation mask')
    reorient_DWI_file = File(argstr='-r %s', desc='Reorient DWI given as input')
    out_file = File(argstr='-o %s', desc='Result DTI image',
                    name_source=['dwi_volume_file'], name_template='%s_tensors.nrrd', keep_extension=False)
    b0_image_file = File(argstr='-O %s', desc='Result DTI image',
                         name_source=['dwi_volume_file'], name_template='%s_tensors_b0.nrrd', keep_extension=False)
    reorient_gradients_file = File(argstr='-R %s',
                                   desc='Reorient gradients so that they are in MrTrix format (in image coordinates)')
    noise_variance_image_file = File(argstr='-N %s', desc='Result noise variance image')
    number_of_threads = traits.Int(0, argstr='-p %d', usedefault=True, desc='number of threads to run on')
    b_no_scale = traits.Bool(argstr='-B', desc='Do not scale b-values according to gradient norm')
    b0_threshold = traits.Float(0, argstr='-t %f', usedefault=True, desc='B0 threshold')


class DTIEstimatorOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Output tensor image')
    b0_image_file = File(exists=True, desc='Output B0 image')


class DTIEstimator(CommandLine):
    _cmd = 'animaDTIEstimator'
    input_spec = DTIEstimatorInputSpec
    output_spec = DTIEstimatorOutputSpec

    def _list_outputs(self):
        outputs = super(DTIEstimator, self)._list_outputs()
        return outputs
