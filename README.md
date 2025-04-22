# Locked-in-Leptons
Final Project for C2-THE-P2 Course, Spring 2025 : https://github.com/jahreda/c2-the-p2

The objective of this project is to train a ML model to identify events with true MET and program this MET tagger to an FPGA. This project follows closely the (hls4ml tutorial)[https://github.com/fastmachinelearning/hls4ml-tutorial]. Two applications were done using a BDT and DNN.  

'presentation.pdf`: Goes into into details behind our motives, analysis, and results. 

`DNN`: Contains analysis done for DNN application.

`BDT`: Contains analysis done for BDT application.

`environment.yml`: environment created for hls4ml tutorial.

## Set-Up
First sign into vmlab and clone this repository. 
``` ssh $USER@vmlab.niu.edu
git clone https://github.com/fatimargz/Locked-in-Leptons.git```

Create a conda environment from the environment.yml file 
`conda env create -f environment.yml`

Activate the new environment: 
`conda activate hls4ml-tutorial`

Source vitis:
`source /opt/metis/el8/contrib/amdtools/xilinx-2023.1/Vitis/2023.1/settings64.sh`

Begin port forwarding a jupyter notebook: 
`jupyter lab --no-browser --port 8080`

In a separate terminal, connect to the vmlab with the port used above for jupyter lab. Replace `$USER` with your username.
`ssh -L 8080:local:host:8080 $USER@vmlab.niu.edu`
