# Fundamental Parameters as used to derive instrumental parameters

This describes the FPA terms used to determine instrumental parameters in the 
["Fit Instr. profile from fundamental parms..."](./mainmenu.md#FPA_menuitem). These 
follow the general usage in the Topas program. They are converted to the values needed by the NIST code. Parameters names are listed in bold, followed by units in parentheses and are then described. 

### Basic Bragg-Brentano parameters

* **divergence (degrees)** - Angle in equatorial plane describing the sample illumination for a Bragg-Brentano instrument
* **soller_angle (degrees)** - Angular limit for divergence in equatorial plane as limited by Soller collimator(s)
* **Rs (mm)** - Diffractometer radius: source to sample and sample to detector distance
* **filament_length (mm)** - Length of x-ray filament when used in “line-focus” (filament oriented along the axial direction)
* **sample_length (mm)** - Illuminated sample length in axial direction. Typically the same as filament_length.
* **receiving_slit_length (mm)** - Length of the receiving slit in axial direction. Typically the same as filament_length.
* **LAC_cm (cm<sup>-1</sup>)** - :	The linear absorption coefficient adjusted for the sample packing density.
* **sample_thickness (mm)** - Thickness of sample measured along the radial direction in the equatorial plane
* **convolution_steps (none)** - The number of steps used for convolution for each step in the diffraction pattern. This results in more smooth convolutions. 
* **source_width (mm)** - Width of x-ray filament in projection in the equatorial plane.
* **tube-tails_L-tail (mm)** - Width for x-ray intensity occurring beyond the Wehnelt shadow as a projection in the axial direction and measured in the positive two-theta direction.
* **tube-tails_R-tail (mm)** - Width for x-ray intensity occurring beyond the Wehnelt shadow as a projection in the axial direction and measured in the negative two-theta direction.
* **tube-tails_rel-I (none)** - Fractional of x-ray intensity found in the tube tails vs. the main peak. Note that tube tails are modeled as a step function.

### Point detector parameter

* **receiving_slit_width (mm)** - Width of receiving slit placed in front of detector or possibly the diffracted beam monochromator (analyzer) measured in the equatorial plane

### Linear position-sensitive detector parameter

* **SiPSD_th2_angular_range (degrees)** - Angular (two-theta) range in equatorial plane that the entire Si PSD subtends (not implemented in Topas)

### Incident-beam monochromator (IBM) parameters

* **src_mono_mm (mm)** - Distance between the x-ray source (filament) and the monochromator, measured in the equatorial plane
* **focus_mono_mm (mm)** - Distance from monochromator crystal to focus slit, measured in the equatorial plane
* **passband_mistune (none)** - Offset for the tuning of the IBM to the center of the reference line of the spectrum, as a fraction of the IBM bandwidth
* **mono_src_proj_mn (micron)** - Bandwidth setting for the monochromator as set by the projection width of the xray source on the monochromator along beam direction and in the equatorial plane
* **passband_shoulder (none)** - Width of transition region from high-intensity, roughly flat region of the x-ray tube output to the to the tube tails region as a fraction of the IBM bandwidth
* **two_theta_mono (degrees)** - The full diffraction angle of the IBM crystal. This will be double the Bragg two-theta angle for the monochromator
* **mono_slit_attenuation (none)** - The attenuation of the Cu K alpha 2 source lines relative to the K alpha 1 lines as determined by the focal slit

If you use this, please cite M.H. Mendenhall, K. Mullen & J.P. Cline (2015), J. Res. of NIST, 120, p223. [DOI: 10.6028/jres.120.014](https://doi.org/10.6028/jres.120.014). If the incident beam monochromator model is used, please also cite: M.H. Mendenhall, D. Black & J.P. Cline (2019), J. Appl. Cryst., 52, p1087. [DOI: 10.1107/S1600576719010951](https://doi.org/10.1107/S1600576719010951).
