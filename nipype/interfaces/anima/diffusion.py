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
    out_file = File(argstr='-o %s', desc='output (registered) image', mandatory=True)
    out_gradients_file = File(argstr='-O %s', desc='output gradients', mandatory=True)

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
        outputs = self.output_spec().get()
        outputs['out_file'] = os.path.abspath(self.inputs.out_file)
        outputs['out_gradients_file'] = self.inputs.out_gradients_file

        return outputs
