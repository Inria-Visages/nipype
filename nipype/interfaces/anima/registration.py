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
    InputMultiPath,
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
                    name_source=['moving_file'], name_template='%s_bmreg_lin.nrrd', keep_extension=False)
    input_transform_file = File(argstr='-i %s',
                                desc='input transformation matrix (ITK txt format)')
    out_transform_file = File(argstr='-O %s',
                              desc='output transformation matrix (ITK txt format)',
                              name_source=['moving_file'], name_template='%s_bmreg_lin_tr.txt', keep_extension=False)
    out_transform_type = traits.Enum(0, 1, 2, argstr='--ot %d',
                                     usedefault=True,
                                     desc='output transformation type (0: rigid, 1: translation, 2: affine)')

    input_transform_series = traits.List('', usedefault=True,
                                         desc='Input transformations list (previous transformations applied)')

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
    pyramid_levels = traits.Int(3, argstr="-p %d", usedefault=True,
                                desc='number of pyramid levels')
    last_pyramid_level = traits.Int(0, argstr='-l %d', usedefault=True,
                                    desc='index of the last pyramid level explored')
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class PyramidalBMRegistrationOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output (registered) image')
    out_transform_file = File(exists=True, desc='output affine matrix (ITK txt format)')
    out_transform_series = traits.List('', usedefault=True,
                                       desc='Output transformations list (input followed by current')


class PyramidalBMRegistration(CommandLine):
    _cmd = 'animaPyramidalBMRegistration'
    input_spec = PyramidalBMRegistrationInputSpec
    output_spec = PyramidalBMRegistrationOutputSpec

    def _list_outputs(self):
        outputs = super(PyramidalBMRegistration, self)._list_outputs()

        outputs['out_transform_series'] = self.inputs.input_transform_series
        if outputs['out_transform_file']:
            outputs['out_transform_series'].append(os.path.abspath(outputs['out_transform_file']))

        return outputs


class DenseSVFBMRegistrationInputSpec(CommandLineInputSpec):
    reference_file = File(exists=True, argstr='-r %s', mandatory=True,
                          desc='fixed image')
    moving_file = File(exists=True, argstr='-m %s', mandatory=True,
                       desc='moving image')
    out_file = File(argstr='-o %s', desc='output (registered) image',
                    name_source=['moving_file'], name_template='%s_bmreg_dense.nrrd', keep_extension=False)
    out_transform_file = File(argstr='-O %s',
                              desc='output SVF transform',
                              name_source=['moving_file'], name_template='%s_bmreg_dense_tr.nrrd', keep_extension=False)

    input_transform_series = traits.List('', usedefault=True,
                                         desc='Input transformations list (previous transformations applied)')

    metric_type = traits.Enum(0, 1, 2, argstr='--metric %d',
                              usedefault=True,
                              desc='Similarity metric between blocks (0: squared correlation coefficient, \
                                    1: correlation coefficient, 2: mean squares')
    block_spacing = traits.Int(2, argstr='--sp %d', usedefault=True,
                               desc='block spacing')
    block_search_radius = traits.Int(2, argstr='--sr %d', usedefault=True,
                                     desc='Search radius in pixels (exhaustive search window, rho start for bobyqa')
    symmetric_registration = traits.Enum(0, 1, 2, argstr='--sym-reg %d',
                                         usedefault=True,
                                         desc='Registration symmetry type, 0: asymmetric, 1: symmetric, 2: kissing')
    pyramid_levels = traits.Int(3, argstr="-p %d", usedefault=True,
                                desc='number of pyramid levels')
    last_pyramid_level = traits.Int(0, argstr='-l %d', usedefault=True,
                                    desc='index of the last pyramid level explored')
    number_of_threads = traits.Int(0, argstr='-T %d', usedefault=True,
                                   desc='number of threads to run on')


class DenseSVFBMRegistrationOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output (registered) image')
    out_transform_file = File(exists=True, desc='output SVF transform')
    out_transform_series = traits.List('', usedefault=True,
                                       desc='Output transformations list (input followed by current')


class DenseSVFBMRegistration(CommandLine):
    _cmd = 'animaDenseSVFBMRegistration'
    input_spec = DenseSVFBMRegistrationInputSpec
    output_spec = DenseSVFBMRegistrationOutputSpec

    def _list_outputs(self):
        outputs = super(DenseSVFBMRegistration, self)._list_outputs()

        outputs['out_transform_series'] = self.inputs.input_transform_series
        if outputs['out_transform_file']:
            outputs['out_transform_series'].append(os.path.abspath(outputs['out_transform_file']))

        return outputs


class TransformSerieXmlGeneratorInputSpec(CommandLineInputSpec):
    input_files = InputMultiPath(File(exists=True), argstr='-i %s', sep=' -i ', mandatory=True,
                                 desc='input transformations')
    input_inversion_flags = traits.ListInt(argstr='-I %s', sep=' -I ',
                                           desc='transformations inversion flags')
    dense_trsf_flag = traits.Bool(argstr='-D', desc='non linear transforms are dense fields')
    out_file = File(argstr='-o %s', desc='output XML file',
                    name_source=['input_files'], name_template='%s.xml', keep_extension=False)


class TransformSerieXmlGeneratorOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output XML file')


class TransformSerieXmlGenerator(CommandLine):
    _cmd = 'animaTransformSerieXmlGenerator'
    input_spec = TransformSerieXmlGeneratorInputSpec
    output_spec = TransformSerieXmlGeneratorOutputSpec

    def _list_outputs(self):
        outputs = super(TransformSerieXmlGenerator, self)._list_outputs()
        return outputs


class ApplyTransformSerieInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                      desc='input image')
    transform_file = File(exists=True, argstr='-t %s', mandatory=True,
                          desc='transform series file (XML)')
    out_file = File(argstr='-o %s', desc='output (resampled) image',
                    name_source=['input_file'], name_template='%s_warped.nrrd', keep_extension=False)
    geometry_file = File(exists=True, argstr='-g %s', mandatory=True,
                         desc='geometry image')
    interpolation_mode = traits.Enum('linear', 'nearest', 'bspline', 'sinc',
                                     argstr='-n %s', usedefault=True,
                                     desc='interpolation mode (one of nearest, linear, bspline, sinc)')

    number_of_threads = traits.Enum(0, argstr='-p %d', usedefault=True,
                                    desc='number of threads to run on')


class ApplyTransformSerieOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output (resampled) image')


class ApplyTransformSerie(CommandLine):
    _cmd = 'animaApplyTransformSerie'
    input_spec = ApplyTransformSerieInputSpec
    output_spec = ApplyTransformSerieOutputSpec

    def _list_outputs(self):
        outputs = super(ApplyTransformSerie, self)._list_outputs()
        return outputs
