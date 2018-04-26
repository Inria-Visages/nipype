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
