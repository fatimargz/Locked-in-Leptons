from SelectionEfficiency import *
from coffea.nanoevents import BaseSchema
import dask
import yaml
from coffea.util import save
from coffea.dataset_tools import preprocess
import argparse
from coffea.dataset_tools import (
    apply_to_fileset,
    max_chunks,
    preprocess,
)
import time
import matplotlib.pyplot as plt
from distributed.diagnostics import MemorySampler


if __name__ == "__main__": # To prevent infinite subprocesses
    
    # Get configuration file
    parser = argparse.ArgumentParser()
    parser.add_argument('cfgyml', type=str,
                        help='<Required> Filepath for YAML configuration file.')
    args = parser.parse_args()
    cfgyml = args.cfgyml
    # Open Config file and read it
    with open(cfgyml, 'r') as f:
        cfg = yaml.full_load(f)
    
    # Store config file options
    fileset = cfg["fileset"]
    print(fileset)
    
    #Open events at datapath
    dataset_runnable, dataset_updated = preprocess(
        fileset,
        align_clusters=False,
        step_size=100_000,
        files_per_batch=1,
        skip_bad_files=True,
        save_form=False,
    )
    
    Processor = SelectionEfficiency()
    to_compute = apply_to_fileset(
                            Processor,
                            dataset_runnable,
                            schemaclass=BaseSchema
    )


    from distributed import Client
    client = Client()

    (out,) = dask.compute(to_compute)
    print(out)