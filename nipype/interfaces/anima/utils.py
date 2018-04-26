# -*- coding: utf-8 -*-
"""The anima utils module provides basic functions for interfacing with anima
   utility functions.
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


class ImageArithmeticInputSpec(CommandLineInputSpec):
    input_file = File(exists=True, argstr='-i %s', mandatory=True,
                      desc='input image')
    out_file = File(argstr='-o %s', desc='output image',
                    mandatory=True)
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


class AverageImagesInputSpec(CommandLineInputSpec):
    input_files = File(exists=True, argstr='-i %s', mandatory=True,
                      desc='input file list as text file')
    mask_files = File(exists=True, argstr='-m %s',
                      desc='masks file list as text file')
    out_file = File(argstr='-o %s', desc='output image',
                    mandatory=True)


class AverageImagesOutputSpec(TraitedSpec):
    out_file = File(exists=True, desc='output image')


class AverageImages(CommandLine):
    _cmd = 'animaAverageImages'
    input_spec = AverageImagesInputSpec
    output_spec = AverageImagesOutputSpec
