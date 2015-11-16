"""
Run HepatoNet FBA simulations.

HepatoNet1 was functionally tested, i.e. various biochemical functions were tested with the network.
Depending on the test different boundary conditions have to be set.

Necessary to set
* exchange set (i.e. what are boundary species)
* FBA constraints (i.e. upper and lower bounds, which substances are not balanced -> new boundary species)
* objective function for the simulation
The FASIMU formulation must be translated into a standard FBA formulation.

"""

import cobra
from fba.cobra.cobra_tools import print_flux_bounds

print roadrunner.__version__
print cobra.__version__

#################################
# load ode and fba model
#################################
from toymodel_settings import fba_file, comp_file

# fba model
cobra_fba = cobra.io.read_sbml_model(fba_file)
# ode model
rr_comp = roadrunner.RoadRunner(comp_file)
sel = ['time'] \
        + ["".join(["[", item, "]"]) for item in rr_comp.model.getBoundarySpeciesIds()] \
        + ["".join(["[", item, "]"]) for item in rr_comp.model.getFloatingSpeciesIds()] \
        + rr_comp.model.getReactionIds()
rr_comp.timeCourseSelections = sel
rr_comp.reset()


# load HepatoNet

# run simple simulation




