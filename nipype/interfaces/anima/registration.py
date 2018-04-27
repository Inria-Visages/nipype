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


class PyramidalBMRegistrationInputSpec(CommandLineInputSpec):
    reference_file = File(exists=True, argstr='-r %s', mandatory=True,
                          desc='fixed image')
    moving_file = File(exists=True, argstr='-m %s', mandatory=True,
                       desc='moving image')
    out_file = File(argstr='-o %s', desc='output (registered) image',
                    mandatory=True)
    out_transform_file = File(argstr='-O %s',
                              desc='output affine matrix (ITK txt format)')
    out_transform_type = traits.Enum(0, 1, 2, argstr='--ot %d',
                                     usedefault=True,
                                     desc='output transformation type (0: rigid, 1: translation, 2: affine)')
    metric_type = traits.Enum(0, 1, 2, argstr='--metric %d',
                              usedefault=True,
                              desc='Similarity metric between blocks (0: squared correlation coefficient, \
                                    1: correlation coefficient, 2: mean squares')
    blocks_spacing = traits.Int(5, argstr='--sp %d', usedefault=True,
                                desc='block spacing')
    blocks_search_radius = traits.Int(2, argstr='--sr %d', usedefault=True,
                                      desc='Search radius in pixels (exhaustive search window, rho start for bobyqa')
    pyramid_levels = traits.Int(3, argstr="-p %d", usedefault=True,
                                desc='number of pyramid levels')
    last_pyramid_level = traits.Int(0, argstr='-l %d', usedefault=True,
                                    desc='index of the last pyramid level explored')
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class PyramidalBMRegistrationOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output (registered) image')
    out_transform_file = File(exists=True, desc='output affine matrix (ITK txt format)')


class PyramidalBMRegistration(CommandLine):
    _cmd = 'animaPyramidalBMRegistration'
    input_spec = PyramidalBMRegistrationInputSpec
    output_spec = PyramidalBMRegistrationOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)

        if self.inputs.out_transform_file:
            outputs['out_transform_file'] = os.path.abspath(self.inputs.out_transform_file)

        return outputs


class DenseSVFBMRegistrationInputSpec(CommandLineInputSpec):
    reference_file = File(exists=True, argstr='-r %s', mandatory=True,
                          desc='fixed image')
    moving_file = File(exists=True, argstr='-m %s', mandatory=True,
                       desc='moving image')
    out_file = File(argstr='-o %s', desc='output (registered) image',
                    mandatory=True)
    out_transform_file = File(argstr='-O %s',
                              desc='output SVF transform')
    metric_type = traits.Enum(0, 1, 2, argstr='--metric %d',
                              usedefault=True,
                              desc='Similarity metric between blocks (0: squared correlation coefficient, \
                                    1: correlation coefficient, 2: mean squares')
    blocks_spacing = traits.Int(2, argstr='--sp %d', usedefault=True,
                                desc='block spacing')
    blocks_search_radius = traits.Int(2, argstr='--sr %d', usedefault=True,
                                      desc='Search radius in pixels (exhaustive search window, rho start for bobyqa')
    pyramid_levels = traits.Int(3, argstr="-p %d", usedefault=True,
                                desc='number of pyramid levels')
    last_pyramid_level = traits.Int(0, argstr='-l %d', usedefault=True,
                                    desc='index of the last pyramid level explored')
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class DenseSVFBMRegistrationOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output (registered) image')
    out_transform_file = File(exists=True, desc='output SVF transform')


class DenseSVFBMRegistration(CommandLine):
    _cmd = 'animaDenseSVFBMRegistration'
    input_spec = DenseSVFBMRegistrationInputSpec
    output_spec = DenseSVFBMRegistrationOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)

        if self.inputs.out_transform_file:
            outputs['out_transform_file'] = os.path.abspath(self.inputs.out_transform_file)

        return outputs


class ApplyTransformSerieInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                      desc='input image')
    transform_file = File(exists=True, argstr='-t %s', mandatory=True,
                          desc='transform series file (XML)')
    out_file = File(argstr='-o %s', desc='output (resampled) image',
                    mandatory=True)
    geometry_file = File(exists=True, argstr='-g %s', mandatory=True,
                         desc='geometry image')
    interpolation_mode = traits.Enum('linear', 'nearest', 'bspline', 'sinc',
                                     argstr='-n %s', usedefault=True,
                                     desc='interpolation mode (one of nearest, linear, bspline, sinc, \
                                           default is linear)')

    number_of_threads = traits.Enum(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class ApplyTransformSerieOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output (resampled) image')


class ApplyTransformSerie(CommandLine):
    _cmd = 'animaApplyTransformSerie'
    input_spec = ApplyTransformSerieInputSpec
    output_spec = ApplyTransformSerieOutputSpec

    def _list_outputs(self):
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        return outputs
