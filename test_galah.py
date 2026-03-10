from astropy.io import fits
import pandas as pd
galah = fits.open("GALAH_DR3_main_allstar_v2.fits")
galah.info()