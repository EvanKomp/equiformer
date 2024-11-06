import sys
import fairchem.core.models

sys.modules['ocpmodels'] = fairchem.core

# Now safe to import nets
