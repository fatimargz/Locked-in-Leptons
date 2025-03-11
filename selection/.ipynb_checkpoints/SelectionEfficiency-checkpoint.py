import awkward as ak
import dask_awkward as dak
from coffea import processor
import hist
import hist.dask as hda
import numpy as np

########################################################################################################################
# Define the Control Plot Processor object
########################################################################################################################

class SelectionEfficiency(processor.ProcessorABC):

    def __init__(self):
        pass
        
    def process(self, events):
        nEvents = ak.num(events, axis=0)

        events_PostSel = selection(events)
        nEvents_PostSel = ak.num(events_PostSel, axis=0)
        efficiency = nEvents_PostSel/nEvents

        return({"efficiency": efficiency})


    def postprocess(self, accumulator):
        pass

def selection(events):
    nLep_2 = events["lep_n"] == 2
    nPhoton_0 = events["photon_n"] == 0
    nJet_0 = events["jet_n"] == 0
    nLargeJet_0 = events["largeRjet_n"] == 0
    met_et10 = events["met_et"] > 20_000

    mask = nLep_2 & nPhoton_0 & nJet_0 & nLargeJet_0 & met_et10
    events_sel = events[mask]
    return(events_sel)