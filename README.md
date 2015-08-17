# AnaMouse
Igor Binary wave management system

This project is to eventually implement a python-based PXP file reader, and provide analysis for included waveforms. It threads the loading of new pxp files, and then provides classes to list waves, and extract waves into a Wave python class. This class works by setting two cursors on the included waveform, and then running methods to process the data between the cursors.

TODO:
  1. Implement a family class -- a dictionary of related wave objects (the same length).
      - methods to display, extract, plot against, etc.
