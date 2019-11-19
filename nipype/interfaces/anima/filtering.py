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
