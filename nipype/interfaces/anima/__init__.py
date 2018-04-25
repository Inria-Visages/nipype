# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Nipype Anima interfaces
----------------------

This module defines the API of Anima interfaces.
"""

# Registration stuff
from .registration import (PyramidalBMRegistration)

# Filtering stuff
from .filtering import (NLMeans)

# Utility stuff
from .utils import (
    CropImage,
    ImageArithmetic,
    AverageImages
)