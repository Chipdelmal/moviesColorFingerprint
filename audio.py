
import array
import numpy as np
from pydub.utils import get_array_type

def getSoundwave(
        sound, 
        STEP=1000,
        BITS=(0, 32767), SCALE=(0, 5), CLIP=(0, 10), MEAN_SIG=5e3,
        ROLL_PAD=10
    ):
    channels = sound.split_to_mono()
    bitDepth = channels[0].sample_width*8
    arrayType = get_array_type(bitDepth)
    # Get signal ------------------------------------------------------------------
    if len(channels)>1:
        sigRaw = [array.array(arrayType, sig) for sig in [i._data for i in channels]]
    else:
        sigRaw = [array.array(arrayType, sig) for sig in [i._data for i in channels*2]]
    sigAbs = [np.abs(np.array(sig), dtype=np.int64) for sig in sigRaw]
    sigSrt = sigAbs if (np.median(sigAbs[1]) < np.median(sigAbs[0])) else sigAbs[::-1]
    # Scale signal for plot -------------------------------------------------------
    M_POWER = np.mean(sigAbs[0]+sigAbs[1])/2
    sigSca = [np.interp(sig, BITS, (SCALE[0], SCALE[1]*MEAN_SIG/M_POWER)) for sig in sigSrt]
    sigClp = [np.clip(sig, CLIP[0], CLIP[1]) for sig in sigSca]
    # Get Kernel ------------------------------------------------------------------
    KERNEL = np.ones(STEP)/STEP
    sigSmt = [np.convolve(i, KERNEL, mode='full') for i in sigClp]
    sigPad = (np.pad(sigSmt[0], (ROLL_PAD, 0), mode='constant')[:-ROLL_PAD], sigSmt[1])
    sigSmp = [i[0::STEP] for i in sigPad]
    return sigSmp