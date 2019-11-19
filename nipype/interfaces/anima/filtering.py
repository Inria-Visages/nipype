# -*- coding: utf-8 -*-
"""The anima filtering module provides basic functions for interfacing with anima
   filtering functions.
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


class NLMeansInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                          desc='input noisy image')
    out_file = File(argstr='-o %s', desc='output denoised image',
                    name_source=['input_file'], name_template='%s_denoised.nrrd', keep_extension=False)
    weighting_method = traits.Enum(0, 1, argstr='-W %d',
                                   usedefault=True,
                                   desc='weighting method (0: exponential, 1: rician)')
    weight_threshold = traits.Float(0.0, argstr='-w %f',
                                    usedefault=True,
                                    desc='weight threshold: patches around have to be similar enough')
    beta_parameter = traits.Int(1, argstr="-b %d", usedefault=True,
                                desc='beta parameter for local noise estimation')
    mean_threshold = traits.Float(0.95, argstr='-m %f', usedefault=True,
                                  desc='minimun mean threshold')
    variance_threshold = traits.Float(0.5, argstr='-v %f', usedefault=True,
                                      desc='minimun variance threshold')
    patch_half_size = traits.Int(1, argstr='-S %d', usedefault=True,
                                 desc='patch half size in each direction')
    patch_search_step_size = traits.Int(1, argstr='-s %d', usedefault=True,
                                        desc='patch step size for searching')
    patch_half_neighborhood_size = traits.Int(5, argstr='-n %d', usedefault=True,
                                              desc='patch half neighborhood size')
    number_of_threads = traits.Int(0, argstr='-p %d', usedefault=True,
                                   desc='number of threads to run on')


class NLMeansOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output denoised image')


class NLMeans(CommandLine):
    _cmd = 'animaNLMeans'
    input_spec = NLMeansInputSpec
    output_spec = NLMeansOutputSpec

    def _list_outputs(self):
        outputs = super(NLMeans, self)._list_outputs()
        return outputs


class NLMeansTemporalInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True, desc='input noisy image')
    out_file = File(argstr='-o %s', desc='output denoised image', mandatory=True)
    patch_half_neighborhood_size = traits.Int(5, argstr='-n %d', usedefault=True, desc='patch half neighborhood size')
    patch_search_step_size = traits.Int(1, argstr='-s %d', usedefault=True, desc='patch step size for searching')
    patch_half_size = traits.Int(1, argstr='-S %d', usedefault=True, desc='patch half size in each direction')
    variance_threshold = traits.Float(0.5, argstr='-v %f', usedefault=True, desc='minimun variance threshold')
    mean_threshold = traits.Float(0.95, argstr='-m %f', usedefault=True, desc='minimun mean threshold')
    beta_parameter = traits.Int(1, argstr="-b %d", usedefault=True, desc='beta parameter for local noise estimation')
    weight_threshold = traits.Float(0.0, argstr='-w %f', usedefault=True, desc='weight threshold: patches around have to be similar enough')
    weighting_method = traits.Enum(0, 1, argstr='-W %d', usedefault=True, desc='weighting method (0: exponential, 1: rician)')
    number_of_threads = traits.Int(0, argstr='-p %d', usedefault=True, desc='number of threads to run on')


class NLMeansTemporalOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output denoised image')


class NLMeansTemporal(CommandLine):
    _cmd = 'animaNLMeansTemporal'
    input_spec = NLMeansTemporalInputSpec
    output_spec = NLMeansTemporalOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs


class GaussianSmoothingInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                      desc='input image')
    out_file = File(argstr='-o %s', desc='output smoothed image',
                    name_source=['input_file'], name_template='%s_smoothed.nrrd', keep_extension=False)
    gaussian_sigma = traits.Float(2.0, argstr='-s %f', usedefault=True,
                                  desc='Gaussian smoothing sigma value')


class GaussianSmoothingOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output smoothed image')


class GaussianSmoothing(CommandLine):
    _cmd = 'animaImageSmoother'
    input_spec = GaussianSmoothingInputSpec
    output_spec = GaussianSmoothingOutputSpec

    def _list_outputs(self):
        outputs = super(GaussianSmoothing, self)._list_outputs()
        return outputs


class DistortionCorrectionInputSpec(CommandLineInputSpec):
    backward_file = File(exists=True, argstr='-b %s', mandatory=True, desc='Backward image')
    forward_file = File(exists=True, argstr='-f %s', mandatory=True, desc='Forward image')
    out_file = File(argstr='-o %s', mandatory=True, desc='Output vector field')

    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True, desc='number of threads to run on')
    gaussian_smoothing_sigma = traits.Float(2, argstr='-s %f', usedefault=True, desc='gaussian smoothing sigma')
    number_distortion_correction = traits.Int(1, argstr='-d %d', usedefault=True, desc='number of the direction of distortion')


class DistortionCorrectionOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Output vector field')


class DistortionCorrection(CommandLine):
    _cmd = 'animaDistortionCorrection'
    input_spec = DistortionCorrectionInputSpec
    output_spec = DistortionCorrectionOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs


class BMDistortionCorrectionInputSpec(CommandLineInputSpec):
    backward_file = File(exists=True, argstr='-b %s', mandatory=True, desc='Backward image')
    forward_file = File(exists=True, argstr='-f %s', mandatory=True, desc='Forward image')
    out_file = File(argstr='-o %s', mandatory=True, desc='Output vector field')

    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True, desc='number of threads to run on')
    gaussian_smoothing_sigma = traits.Float(2, argstr='-s %f', usedefault=True, desc='gaussian smoothing sigma')
    number_distortion_correction = traits.Int(1, argstr='-d %d', usedefault=True, desc='number of the direction of distortion')


class BMDistortionCorrectionOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Output vector field')


class BMDistortionCorrection(CommandLine):
    _cmd = 'animaBMDistortionCorrection'
    input_spec = BMDistortionCorrectionInputSpec
    output_spec = BMDistortionCorrectionOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs


class ApplyDistortionCorrectionInputSpec(CommandLineInputSpec):
    backward_file = File(exists=True, argstr='-b %s', mandatory=False, desc='Backward image')
    forward_file = File(exists=True, argstr='-f %s', mandatory=True, desc='Forward image')
    out_file = File(argstr='-o %s', mandatory=True, desc='Output vector field')
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True, desc='number of threads to run on')
    transformation_real_coordinates_out_file = File(argstr='-O %s', mandatory=False, desc='Transformation in real coordinates')
    distortion_correction_field = traits.Str('', argstr='-t %s', usedefault=False, desc='distortion correction field')
    invert = traits.Bool(True, argstr='-I', usedefault=True, desc='If set, invert the input field (after reverting if R option is on')
    reverse = traits.Bool(True, argstr='-R', usedefault=True, desc='If set, apply the opposite of the input field to the forward image')
    voxel = traits.Bool(True, argstr='-V', usedefault=True, desc='If set, the input correction field is assumed to be in voxel coordinates')


class ApplyDistortionCorrectionOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='Output vector field')


class ApplyDistortionCorrection(CommandLine):
    _cmd = 'animaApplyDistortionCorrection'
    input_spec = ApplyDistortionCorrectionInputSpec
    output_spec = ApplyDistortionCorrectionOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs