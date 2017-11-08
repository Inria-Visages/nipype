from ..base import (BaseInterface, Directory,
                    BaseInterfaceInputSpec, isdefined,
                    traits, TraitedSpec, File)
import os

class ConvertBrainvisionToFifFormatInputSpec(BaseInterfaceInputSpec):
    """ There is more option which can be added here, if needed:

misc : list or tuple of str | ‘auto’
    Names of channels or list of indices that should be designated MISC channels. Values should correspond to the electrodes in the vhdr file. If ‘auto’, units in vhdr file are used for inferring misc channels. Default is 'auto'.
preload : bool

    If True, all data are loaded at initialization. If False, data are not read until save.

response_trig_shift : int | None

    An integer that will be added to all response triggers when reading events (stimulus triggers will be unaffected). If None, response triggers will be ignored. Default is 0 for backwards compatibility, but typically another value or None will be necessary.

event_id : dict | None

    The id of special events to consider in addition to those that follow the normal Brainvision trigger format (‘S###’). If dict, the keys will be mapped to trigger values on the stimulus channel. Example: {‘SyncStatus’: 1; ‘Pulse Artifact’: 3}. If None or an empty dict (default), only stimulus events are added to the stimulus channel. Keys are case sensitive.

verbose : bool, str, int, or None

    If not None, override default verbose level (see mne.verbose() and Logging documentation for more).

"""
    vhdr_fname = traits.File(mandatory=True,
                             exists=True,
                            desc="Path to the EEG header file.")
    montage = traits.Str("None",
                         desc="Path or instance of montage containing electrode positions. "+
                                      "If None, sensor locations are (0,0,0). "+
                                      "See the documentation of mne.channels.read_montage() for more information."+
                              "The name of the montage file without the file extension (e.g. "+
                              "kind='easycap-M10' for 'easycap-M10.txt'). Files with extensions  .elc ,  .txt , .csd,"+
                              " .elp, .hpts, .sfp, .loc (.locs and .eloc) or .bvef are supported.")
    eog = traits.ListStr(('HEOGL', 'HEOGR', 'VEOGb'),
                         desc="Names of channels or list of indices that should be designated EOG channels. "+
                         "Values should correspond to the vhdr file Default is ('HEOGL', 'HEOGR', 'VEOGb')")
    scale = traits.Float(1,
                         desc="The scaling factor for EEG data. "
                              "Unless specified otherwise by header file, units are in microvolts. "
                              "Default scale factor is 1.")


class ConvertBrainvisionToFifFormatOutputSpec(TraitedSpec):
    outfile = traits.File(exists=True,
                          desc=".fif file red from the vhdr_fname file used as input.")


class ConvertBrainvisionToFifFormat(BaseInterface):
    """ Read .vhdr EEG files from Brainvision, and convert it into a .fif file, containing an object Raw usable by mne.
    See doc here: http://martinos.org/mne/stable/generated/mne.io.read_raw_brainvision.html#mne.io.read_raw_brainvision"""

    input_spec = ConvertBrainvisionToFifFormatInputSpec
    output_spec = ConvertBrainvisionToFifFormatOutputSpec

    def _run_interface(self, runtime):
        import mne
        fname = self.inputs.vhdr_fname
        montage = self.inputs.montage
        eog = self.inputs.eog
        scale = self.inputs.scale

        raw = mne.io.read_raw_brainvision(fname, montage=montage, eog=eog, misc='auto', scale=scale, preload=False,
                                          response_trig_shift=0, event_id=None, verbose=None)

        base, _ = os.path.splitext(fname)
        raw.save(base + '.fif')

        return runtime

    def _list_outputs(self):
        outputs = self._outputs().get()
        fname = self.inputs.volume
        base, _ = os.splitext(fname)
        outputs["outfile"] = os.path.abspath(base + '.fif')
        return outputs